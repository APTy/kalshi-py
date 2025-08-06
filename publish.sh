#!/bin/bash

set -e

echo "🚀 Starting Kalshi Python client publication..."

if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Make sure you're in the kalshi-py directory."
    exit 1
fi

echo ""
echo "🔍 Checking current version..."
CURRENT_VERSION=$(grep '^version = ' pyproject.toml | cut -d'"' -f2)
echo "Current version: $CURRENT_VERSION"

echo ""
echo "🧪 Running tests..."
uv run python test_client.py

echo ""
echo "🔍 Checking for uncommitted changes..."
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Warning: You have uncommitted changes. Consider committing them first."
    echo "Uncommitted files:"
    git status --porcelain
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Publication cancelled."
        exit 1
    fi
fi

echo ""
echo "📦 Building package..."
uv build

echo ""
echo "🔍 Checking if version already exists on PyPI..."
if uv pip index versions kalshi-py | grep -q "$CURRENT_VERSION"; then
    echo "❌ Error: Version $CURRENT_VERSION already exists on PyPI."
    echo "Please update the version in pyproject.toml before publishing."
    exit 1
fi

echo ""
echo "📤 Publishing to PyPI..."
echo "This will publish version $CURRENT_VERSION to PyPI."
read -p "Are you sure? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Publication cancelled."
    exit 1
fi

uv publish

echo ""
echo "🎉 Successfully published kalshi-py version $CURRENT_VERSION to PyPI!"
echo ""
echo "Next steps:"
echo "1. Create a git tag: git tag v$CURRENT_VERSION"
echo "2. Push the tag: git push origin v$CURRENT_VERSION"
echo "3. Create a GitHub release for version $CURRENT_VERSION"
