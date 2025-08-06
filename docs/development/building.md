# Building

This guide explains how to build and publish the kalshi-py package.

## Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Access to PyPI (for publishing)

## Development Build

### Install Dependencies

```bash
uv sync --group dev
```

### Build Package

```bash
uv build
```

This creates both source distribution (sdist) and wheel files in the `dist/` directory.

### Build Specific Formats

```bash
# Build wheel only
uv build --wheel

# Build source distribution only
uv build --sdist
```

## Testing the Build

### Install from Local Build

```bash
# Build the package
uv build

# Install from the built wheel
pip install dist/kalshi_py-*.whl
```

### Test Installation

```python
import kalshi_py
print(kalshi_py.__version__)

# Test basic functionality
from kalshi_py import Client
client = Client(base_url="https://api.elections.kalshi.com/trade-api/v2")
```

## Publishing

### Update Version

1. Update the version in `pyproject.toml`:

   ```toml
   [project]
   version = "2.0.6.3"  # Increment version
   ```

2. Update the version in `openapi-config.yaml`:
   ```yaml
   package_version_override: "2.0.6.3"
   ```

### Build and Publish

```bash
# Build the package
uv build

# Publish to PyPI
uv publish
```

### Publishing to Test PyPI

```bash
# Publish to Test PyPI first
uv publish --repository testpypi
```

## Continuous Integration

The project uses GitHub Actions for automated builds and testing:

- **Build and Test**: Runs on every push and pull request
- **Publish**: Runs on releases to automatically publish to PyPI

## Version Management

This project follows [Semantic Versioning](https://semver.org/):

- **Major version**: Breaking changes
- **Minor version**: New features (backward compatible)
- **Patch version**: Bug fixes (backward compatible)

## Release Process

1. **Update version** in `pyproject.toml` and `openapi-config.yaml`
2. **Update changelog** (if applicable)
3. **Create a release** on GitHub
4. **GitHub Actions** will automatically build and publish to PyPI

## Troubleshooting

### Build Errors

- **Missing dependencies**: Run `uv sync --group dev`
- **Version conflicts**: Check `pyproject.toml` for correct version
- **Permission errors**: Ensure you have write access to the directory

### Publishing Errors

- **Authentication**: Ensure you have PyPI credentials configured
- **Version already exists**: Increment the version number
- **Network issues**: Check your internet connection and PyPI status

### Testing Issues

- **Import errors**: Ensure the package is installed correctly
- **API errors**: Check your API credentials and network connection
