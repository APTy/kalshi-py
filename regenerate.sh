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

echo ""
echo "💾 Backing up critical custom files..."
cp pyproject.toml pyproject.toml.backup
cp uv.lock uv.lock.backup
cp README.md README.md.backup
if [ -f "kalshi_py/__init__.py" ]; then
    cp kalshi_py/__init__.py kalshi_py/__init__.py.backup
fi

echo ""
echo "🔨 Regenerating client library..."
uv run openapi-python-client generate --path openapi.yaml --meta uv --output-path . --overwrite --config openapi-config.yaml

echo ""
echo "🔄 Restoring custom files..."
cp pyproject.toml.backup pyproject.toml
cp uv.lock.backup uv.lock
cp README.md.backup README.md
if [ -f "kalshi_py/__init__.py.backup" ]; then
    cp kalshi_py/__init__.py.backup kalshi_py/__init__.py
fi

echo ""
echo "🧹 Cleaning up backup files..."
rm pyproject.toml.backup uv.lock.backup README.md.backup
if [ -f "kalshi_py/__init__.py.backup" ]; then
    rm kalshi_py/__init__.py.backup
fi

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

echo ""
echo "🎉 Regeneration complete!"
echo ""
echo "Next steps:"
echo "1. Review the generated code"
echo "2. Test the client: uv run python test_client.py"
echo "3. Update version in pyproject.toml if needed"
echo "4. Commit your changes"
