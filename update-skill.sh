#!/bin/bash
# Update deep-market-analysis skill to latest version
# Run: ~/.agents/skills/deep-market-analysis/update-skill.sh

set -e

SKILL_DIR=~/.agents/skills/deep-market-analysis

echo "🔄 Updating deep-market-analysis skill..."

cd "$SKILL_DIR" 2>/dev/null || {
    echo "❌ Error: Skill not found at $SKILL_DIR"
    echo "Run this first: git clone https://github.com/Timmy6942025/deep-market-analysis.git ~/.agents/skills/deep-market-analysis"
    exit 1
}

git pull origin main

echo "✅ Update complete!"
echo "📋 Latest changes:"
git log --oneline -3
