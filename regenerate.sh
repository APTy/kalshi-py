#!/bin/bash

set -e

echo "🚀 Starting Kalshi Python client regeneration..."

if [ ! -f "openapi.yaml" ]; then
    echo "❌ Error: openapi.yaml not found. Make sure you're in the kalshi-py directory."
    exit 1
fi

echo ""
echo "📥 Fetching latest OpenAPI specification from Kalshi..."
curl -s https://docs.kalshi.com/openapi.yaml -o openapi.yaml

echo ""
echo "📦 Ensuring openapi-python-client is installed..."
uv add openapi-python-client --dev

if [ -d "kalshi_py" ]; then
    echo ""
    echo "💾 Backing up existing kalshi_py directory..."
    if [ -d "kalshi_py_backup" ]; then
        rm -rf kalshi_py_backup
    fi
    cp -r kalshi_py kalshi_py_backup
fi

echo ""
echo "🔨 Regenerating client library..."
uv run openapi-python-client generate --path openapi.yaml --meta uv --output-path . --overwrite --config openapi-config.yaml

echo ""
echo "🎨 Formatting generated code..."
uv run ruff format kalshi_py/

echo ""
echo "🔍 Checking for linting issues..."
if uv run ruff check kalshi_py/; then
    echo "✅ No linting issues found!"
else
    echo "⚠️  Linting issues found. You may want to address these manually."
fi

if [ -d "kalshi_py_backup" ] && [ -d "kalshi_py" ]; then
    echo ""
    echo "🧹 Cleaning up backup..."
    rm -rf kalshi_py_backup
fi

echo ""
echo "🎉 Regeneration complete!"
echo ""
echo "Next steps:"
echo "1. Review the generated code"
echo "2. Test the client: uv run python test_client.py"
echo "3. Update version in pyproject.toml if needed"
echo "4. Commit your changes"
