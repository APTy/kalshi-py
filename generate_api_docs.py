#!/usr/bin/env python3
"""
Generate API documentation from actual Python modules.
This script automatically discovers all API functions and creates documentation files.
"""

import importlib
import inspect
from pathlib import Path


def get_api_endpoints_from_files(api_dir):
    """Get all API endpoints from individual files in an API directory."""
    endpoints = []
    api_path = Path(f"kalshi_py/api/{api_dir}")

    if not api_path.exists():
        return endpoints

    for py_file in api_path.glob("*.py"):
        if py_file.name == "__init__.py":
            continue

        # Extract the endpoint name from the filename
        endpoint_name = py_file.stem.replace("_", " ").title()
        module_name = f"kalshi_py.api.{api_dir}.{py_file.stem}"

        # Get the functions from this module
        functions = []
        try:
            module = importlib.import_module(module_name)
            for name, obj in inspect.getmembers(module):
                if inspect.isfunction(obj) and not name.startswith("_"):
                    functions.append((name, module_name))
        except ImportError as e:
            print(f"Warning: Could not import {module_name}: {e}")

        if functions:
            endpoints.append((endpoint_name, functions))

    return sorted(endpoints, key=lambda x: x[0])


def generate_api_doc(api_name, api_dir, output_file):
    """Generate documentation for an API module."""
    endpoints = get_api_endpoints_from_files(api_dir)

    if not endpoints:
        print(f"No endpoints found in {api_dir}")
        return

    with open(output_file, "w") as f:
        f.write(f"# {api_name.title()} API Reference\n\n")
        f.write("## Endpoints\n\n")

        for endpoint_name, functions in endpoints:
            f.write(f"### {endpoint_name}\n\n")

            # Group functions by type (sync, asyncio, etc.)
            sync_funcs = [f for f in functions if f[0] == "sync"]
            asyncio_funcs = [f for f in functions if f[0] == "asyncio"]
            sync_detailed_funcs = [f for f in functions if f[0] == "sync_detailed"]
            asyncio_detailed_funcs = [f for f in functions if f[0] == "asyncio_detailed"]

            # Document sync function (most commonly used)
            if sync_funcs:
                func_name, module_path = sync_funcs[0]
                f.write("**Synchronous API Call**\n\n")
                f.write(f"::: {module_path}.{func_name}\n")
                f.write("    handler: python\n")
                f.write("    options:\n")
                f.write("      show_source: true\n")
                f.write("      show_root_heading: true\n")
                f.write("      heading_level: 4\n")
                f.write("      members_order: source\n")
                f.write("      filters: ['!^_']\n\n")

            # Document asyncio function
            if asyncio_funcs:
                func_name, module_path = asyncio_funcs[0]
                f.write("**Asynchronous API Call**\n\n")
                f.write(f"::: {module_path}.{func_name}\n")
                f.write("    handler: python\n")
                f.write("    options:\n")
                f.write("      show_source: true\n")
                f.write("      show_root_heading: true\n")
                f.write("      heading_level: 4\n")
                f.write("      members_order: source\n")
                f.write("      filters: ['!^_']\n\n")

            # Document detailed functions if they exist
            if sync_detailed_funcs:
                func_name, module_path = sync_detailed_funcs[0]
                f.write("**Synchronous Detailed Response**\n\n")
                f.write(f"::: {module_path}.{func_name}\n")
                f.write("    handler: python\n")
                f.write("    options:\n")
                f.write("      show_source: true\n")
                f.write("      show_root_heading: true\n")
                f.write("      heading_level: 4\n")
                f.write("      members_order: source\n")
                f.write("      filters: ['!^_']\n\n")

            if asyncio_detailed_funcs:
                func_name, module_path = asyncio_detailed_funcs[0]
                f.write("**Asynchronous Detailed Response**\n\n")
                f.write(f"::: {module_path}.{func_name}\n")
                f.write("    handler: python\n")
                f.write("    options:\n")
                f.write("      show_source: true\n")
                f.write("      show_root_heading: true\n")
                f.write("      heading_level: 4\n")
                f.write("      members_order: source\n")
                f.write("      filters: ['!^_']\n\n")


def main():
    """Generate all API documentation."""
    # API modules to document
    api_modules = {
        "market": "market",
        "portfolio": "portfolio",
        "communications": "communications",
        "collection": "collection",
        "milestone": "milestone",
        "structured_target": "structured_target",
        "api_keys": "api_keys",
        "default": "default",
    }

    docs_dir = Path("docs/api")
    docs_dir.mkdir(exist_ok=True)

    print("🔍 Discovering API endpoints...")

    for api_name, api_dir in api_modules.items():
        output_file = docs_dir / f"{api_name}.md"
        print(f"📝 Generating {api_name} API docs...")
        generate_api_doc(api_name, api_dir, output_file)

    print("✅ API documentation generated!")
    print("\nTo build the docs:")
    print("  ./docs.sh")


if __name__ == "__main__":
    main()
