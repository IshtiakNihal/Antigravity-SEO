#!/usr/bin/env bash
# Antigravity SEO One-Click Installer for Linux / macOS
# Installs Antigravity SEO globally into ~/.gemini/config/skills/antigravity-seo

set -e

echo "=============================================="
echo "   Installing Antigravity SEO Skill for AGY   "
echo "=============================================="

TARGET_DIR="$HOME/.gemini/config/skills/antigravity-seo"

if [ -d "$TARGET_DIR" ]; then
    echo "Existing Antigravity SEO installation found at: $TARGET_DIR"
    echo "Updating repository..."
    cd "$TARGET_DIR"
    git pull origin main
else
    echo "Cloning Antigravity SEO into: $TARGET_DIR"
    mkdir -p "$(dirname "$TARGET_DIR")"
    git clone https://github.com/IshtiakNihal/Antigravity-SEO.git "$TARGET_DIR"
fi

echo ""
echo "Antigravity SEO Skill installed successfully!"
echo "The skill is now globally available in Google Antigravity."

