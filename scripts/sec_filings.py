#!/usr/bin/env python3
"""
SEC Filing Analysis
Fetches 10-K, 10-Q, and 8-K filing data for fundamental context.
Uses SEC EDGAR directly — no API key required.
"""

import argparse
import json
import re
import urllib.error
import urllib.request
from datetime import datetime


def validate_ticker(ticker):
    if not isinstance(ticker, str):
        raise ValueError(f"Ticker must be a string, got {type(ticker).__name__}")
    if not re.match(r"^[A-Z]{1,5}$", ticker.upper()):
        raise ValueError(f"Invalid ticker format: {ticker!r} — must be 1 to 5 uppercase letters")
    return ticker.upper()


# SEC EDGAR requires a contact email in User-Agent.
# Using the project's own contact address — no user configuration needed.
_EDGAR_HEADERS = {
    "User-Agent": "edge-hunter/1.0 (edge-hunter@codebuff.com)",
}


def get_cik_from_ticker(ticker):
    """Map ticker symbol to SEC CIK number via the public ticker file."""
    ticker = validate_ticker(ticker)
    try:
        url = "https://www.sec.gov/files/company_tickers.json"
        req = urllib.request.Request(url, headers=_EDGAR_HEADERS)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        for entry in data.values():
            if entry["ticker"] == ticker:
                return str(entry["cik_str"]).zfill(10)
    except urllib.error.HTTPError as e:
        print(f"[ERROR] SEC EDGAR returned {e.code} — try again in a few minutes")
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error reaching SEC EDGAR: {e.reason}")
    except json.JSONDecodeError:
        print("[ERROR] Failed to parse SEC ticker data")
    return None


def analyze_recent_filings(ticker):
    ticker = validate_ticker(ticker)

    print(f"\n{'=' * 70}")
    print(f"SEC FILING ANALYSIS: {ticker}")
    print("=" * 70)

    cik = get_cik_from_ticker(ticker)
    if not cik:
        print(f"Could not find CIK for {ticker}")
        return

    print(f"\nCIK: {cik}")
    print(f"\nRecent filings: https://www.sec.gov/cgi-bin/browse-edgar?CIK={cik}")

    try:
        url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        req = urllib.request.Request(url, headers=_EDGAR_HEADERS)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())

        filings = data.get("filings", {}).get("recent", {})
        forms = filings.get("form", [])
        dates = filings.get("filingDate", [])
        accession_numbers = filings.get("accessionNumber", [])

        print(f"\nRECENT FILINGS (Last 10):")
        print(f"{'Date':<12} {'Form':<10} Link")
        print(f"{'-' * 70}")

        count = 0
        for i in range(min(10, len(forms))):
            form = forms[i]
            date = dates[i]
            acc = accession_numbers[i].replace("-", "")
            link = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/{accession_numbers[i]}.txt"

            if form in ("10-K", "10-Q", "8-K", "10-K/A", "10-Q/A"):
                marker = "*" if form.startswith("10-") else "-"
                print(f"{date:<12} {form:<10} {marker} {link}")
                count += 1

        if count == 0:
            print("  No recent 10-K/10-Q/8-K filings found.")

        # 10-K freshness check
        try:
            k_index = forms.index("10-K")
            filing_date = datetime.strptime(dates[k_index], "%Y-%m-%d")
            days_ago = (datetime.now() - filing_date).days
            print(f"\nLatest 10-K filed: {dates[k_index]} ({days_ago} days ago)")
            if days_ago < 90:
                print("  +-- RECENT — Earnings data may be FRESH")
            elif days_ago > 365:
                print("  +-- OLD — May need updated data")
        except ValueError:
            print("\nNo recent 10-K found.")

        # 8-K summary
        eight_k_dates = [dates[i] for i in range(len(forms)) if forms[i] == "8-K"]
        if eight_k_dates:
            print(f"\nRecent 8-K filings: {', '.join(eight_k_dates[:3])}")
            print("  +-- Material events may have occurred — check for news")

    except urllib.error.HTTPError as e:
        print(f"[ERROR] SEC EDGAR returned {e.code} — try again in a few minutes")
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error fetching filings: {e.reason}")
    except json.JSONDecodeError:
        print("[ERROR] Failed to parse SEC filing data")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {type(e).__name__} — {e}")

    print(f"\n{'=' * 70}")
    print("TIP: Read recent 10-K for business overview, risk factors,")
    print("and MD&A (Management Discussion & Analysis) sections")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SEC filing analysis for a given ticker")
    parser.add_argument("ticker", help="Stock ticker (e.g., AAPL)")
    args = parser.parse_args()
    analyze_recent_filings(args.ticker)
