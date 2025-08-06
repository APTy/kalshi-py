# Contributing

Thank you for your interest in contributing to kalshi-py!

## Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/kalshi/kalshi-py.git
   cd kalshi-py
   ```

2. **Install development dependencies**

   ```bash
   uv sync --group dev
   ```

3. **Install the package in development mode**
   ```bash
   uv pip install -e .
   ```

## Code Style

This project uses [ruff](https://github.com/astral-sh/ruff) for linting and formatting.

- **Check code style**: `uv run ruff check .`
- **Format code**: `uv run ruff format .`
- **Fix issues**: `uv run ruff check --fix .`

## Running Tests

```bash
uv run python test_client.py
```

## Documentation

To build and serve the documentation locally:

```bash
./docs.sh
uv run mkdocs serve
```

## Making Changes

1. **Create a feature branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**

   - Follow the code style guidelines
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**

   ```bash
   uv run ruff check .
   uv run python test_client.py
   ```

4. **Commit your changes**

   ```bash
   git add .
   git commit -m "Add your feature description"
   ```

5. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Pull Request Guidelines

- Provide a clear description of the changes
- Include tests for new functionality
- Update documentation if needed
- Ensure all tests pass
- Follow the existing code style

## Issues

If you find a bug or have a feature request, please:

1. Check existing issues first
2. Create a new issue with a clear description
3. Include steps to reproduce (for bugs)
4. Provide code examples (for feature requests)

## License

By contributing to kalshi-py, you agree that your contributions will be licensed under the same license as the project.
