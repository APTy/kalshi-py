#!/bin/bash

set -e

echo "📚 Building kalshi-py documentation..."

# Install dependencies if needed
if ! uv run python -c "import mkdocs" 2>/dev/null; then
    echo "📦 Installing documentation dependencies..."
    uv add --dev mkdocs mkdocs-material mkdocstrings[python] mkdocs-gen-files mkdocs-literate-nav mkdocs-section-index
fi

# Build documentation
echo "🔨 Building documentation..."
uv run mkdocs build

echo "✅ Documentation built successfully!"
echo ""
echo "To serve the documentation locally:"
echo "  uv run mkdocs serve"
echo ""
echo "To deploy to GitHub Pages:"
echo "  uv run mkdocs gh-deploy"
