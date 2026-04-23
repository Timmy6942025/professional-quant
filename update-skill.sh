#!/bin/bash
# Update professional-quant skill to latest version
# Run: ~/.agents/skills/professional-quant/update-skill.sh

set -e

SKILL_DIR=~/.agents/skills/professional-quant

echo "🔄 Updating professional-quant skill..."

cd "$SKILL_DIR" 2>/dev/null || {
    echo "❌ Error: Skill not found at $SKILL_DIR"
    echo "Run this first: git clone https://github.com/Timmy6942025/professional-quant.git ~/.agents/skills/professional-quant"
    exit 1
}

git pull origin main

echo "✅ Update complete!"
echo "📋 Latest changes:"
git log --oneline -3
