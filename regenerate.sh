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
echo "🔧 Cleaning up OpenAPI spec to shorten model names..."
sed -i '' 's/github\.com\.Kalshi\.exchange-infra\.svc-api2\.//g' openapi.yaml

echo ""
echo "💾 Backing up critical custom files..."
cp pyproject.toml pyproject.toml.backup
cp uv.lock uv.lock.backup
cp README.md README.md.backup
if [ -f ".gitignore" ]; then
    cp .gitignore .gitignore.backup
fi
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
if [ -f ".gitignore.backup" ]; then
    cp .gitignore.backup .gitignore
fi
if [ -f "kalshi_py/__init__.py.backup" ]; then
    cp kalshi_py/__init__.py.backup kalshi_py/__init__.py
fi

echo ""
echo "🧹 Cleaning up backup files..."
rm pyproject.toml.backup uv.lock.backup README.md.backup
if [ -f ".gitignore.backup" ]; then
    rm .gitignore.backup
fi
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
echo "📚 Regenerating API documentation..."
if [ -f "generate_api_docs.py" ]; then
    echo "🔨 Generating API docs from updated code..."
    uv run python generate_api_docs.py
    echo "✅ API documentation regenerated!"
else
    echo "⚠️  No generate_api_docs.py found, skipping API doc generation"
fi

echo ""
echo "📚 Building documentation..."
if [ -f "mkdocs.yml" ]; then
    echo "🔨 Building documentation with updated API..."
    uv run mkdocs build
    echo "✅ Documentation rebuilt successfully!"
else
    echo "⚠️  No mkdocs.yml found, skipping documentation rebuild"
fi

echo ""
echo "🎉 Regeneration complete!"
echo ""
echo "Next steps:"
echo "1. Review the generated code"
echo "2. Test the client: uv run python test_client.py"
echo "3. Review the updated documentation: uv run mkdocs serve"
echo "4. Update version in pyproject.toml if needed"
echo "5. Commit your changes"
