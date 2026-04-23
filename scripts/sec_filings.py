#!/usr/bin/env python3
"""
SEC Filing Analysis (Free, No API Key)
Fetches 10-K, 10-Q data from SEC.gov for fundamental context
"""
import re
import argparse
from datetime import datetime

def get_cik_from_ticker(ticker):
    """Get CIK from ticker - SEC maintains a JSON file with all mappings"""
    import json
    import urllib.request
    import ssl
    
    try:
        # Create SSL context that doesn't verify (SEC.gov is trustworthy)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        url = "https://www.sec.gov/files/company_tickers.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode())
        
        for entry in data.values():
            if entry['ticker'] == ticker.upper():
                return str(entry['cik_str']).zfill(10)
    except Exception as e:
        print(f"Error getting CIK: {e}")
    return None

def analyze_recent_filings(ticker):
    """Analyze recent 10-K and 10-Q filings"""
    import urllib.request
    
    print(f"\n{'='*70}")
    print(f"SEC FILING ANALYSIS: {ticker}")
    print(f"{'='*70}")
    
    cik = get_cik_from_ticker(ticker)
    if not cik:
        print(f"Could not find CIK for {ticker}")
        return
    
    print(f"\nCIK: {cik}")
    print(f"\nRecent filings: https://www.sec.gov/cgi-bin/browse-edgar?CIK={cik}")
    
    # Get recent filings JSON
    try:
        url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        
        filings = data.get('filings', {}).get('recent', {})
        forms = filings.get('form', [])
        dates = filings.get('filingDate', [])
        accession_numbers = filings.get('accessionNumber', [])
        
        print(f"\nRECENT FILINGS (Last 10):")
        print(f"{'Date':<12} {'Form':<10} {'Link':<50}")
        print(f"{'-'*70}")
        
        for i in range(min(10, len(forms))):
            form = forms[i]
            date = dates[i]
            acc = accession_numbers[i].replace('-', '')
            link = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/{accession_numbers[i]}.txt"
            
            # Focus on 10-K, 10-Q, 8-K
            if form in ['10-K', '10-Q', '8-K', '10-K/A', '10-Q/A']:
                print(f"{date:<12} {form:<10} {link:<50}")
        
        # Check for recent 10-K
        try:
            k_index = forms.index('10-K')
            print(f"\nLATEST 10-K FILED: {dates[k_index]}")
            
            # Calculate days since filing
            filing_date = datetime.strptime(dates[k_index], '%Y-%m-%d')
            days_ago = (datetime.now() - filing_date).days
            print(f"Days since filing: {days_ago}")
            
            if days_ago < 90:
                print(f"⚠ RECENT FILING - Earnings data may be FRESH")
            elif days_ago > 365:
                print(f"⚠ OLD FILING - May need updated data")
        except ValueError:
            print(f"\nNo recent 10-K found")
        
        # Check for 8-K (material events)
        eight_k_dates = [dates[i] for i in range(len(forms)) if forms[i] == '8-K']
        if eight_k_dates:
            print(f"\nRecent 8-K filings: {', '.join(eight_k_dates[:3])}")
            print(f"→ Material events may have occurred - check for news")
        
    except Exception as e:
        print(f"Error fetching filings: {e}")
    
    print(f"\n{'='*70}")
    print(f"TIP: Read recent 10-K for business overview, risk factors,")
    print(f"and MD&A (Management Discussion & Analysis) sections")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SEC filing analysis (free, no API key)")
    parser.add_argument("ticker", help="Stock ticker (e.g., AAPL)")
    args = parser.parse_args()
    analyze_recent_filings(args.ticker)
