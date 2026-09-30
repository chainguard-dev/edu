#!/usr/bin/env python3
"""
Generate the package catalog JSON that backs the MCP server's
find_package_equivalent tool.

Reads the Debian, Fedora, and Alpine to Wolfi package mappings from
data/package-mappings.yaml, which the autodocs-platform workflow copies nightly
from chainguard-dev/dfc.

This script was generate_image_catalog.py and also listed container images. The
image list came from a README snapshot that had stopped updating, so it was
removed (DOCS-138); live image data now comes from the cg-oci MCP server.

Usage:
    python3 scripts/generate_package_catalog.py \
        --mappings data/package-mappings.yaml \
        --output scripts/package-mappings.json \
        --commit abc123
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from typing import Any, Dict, Optional

try:
    import yaml
except ImportError:
    print(
        "Error: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr
    )
    sys.exit(1)


def load_package_mappings(mappings_path: str) -> Dict[str, Any]:
    """Load and parse the package-mappings.yaml file."""
    with open(mappings_path, "r") as f:
        return yaml.safe_load(f)


def build_catalog(
    mappings: Dict[str, Any],
    commit: Optional[str] = None,
) -> Dict[str, Any]:
    """Build the catalog from the package mappings."""
    packages_map = mappings.get("packages", {})

    # Build packages index (Debian/Fedora/Alpine -> Wolfi)
    packages = {}
    for distro, pkg_map in packages_map.items():
        packages[distro] = {}
        if pkg_map:
            for os_pkg, wolfi_pkgs in pkg_map.items():
                if isinstance(wolfi_pkgs, list):
                    packages[distro][os_pkg] = wolfi_pkgs
                else:
                    packages[distro][os_pkg] = []

    total_packages = sum(len(pkg_map) for pkg_map in packages.values() if pkg_map)

    catalog = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source_commit": commit or "unknown",
            "total_packages_mapped": total_packages,
        },
        "packages": packages,
    }

    return catalog


def main():
    parser = argparse.ArgumentParser(
        description="Generate the package catalog JSON from dfc's package mappings"
    )
    parser.add_argument(
        "--mappings",
        required=True,
        help="Path to data/package-mappings.yaml (source of package equivalents)",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output path for package-mappings.json",
    )
    parser.add_argument(
        "--commit",
        default=None,
        help="Source commit SHA for metadata",
    )

    args = parser.parse_args()

    print(f"Loading package mappings from {args.mappings}...", file=sys.stderr)
    mappings = load_package_mappings(args.mappings)

    catalog = build_catalog(mappings, args.commit)
    total = catalog["metadata"]["total_packages_mapped"]
    if total == 0:
        # find_package_equivalent would answer every lookup with "no match", so
        # stop the build rather than ship an empty catalog.
        print(f"Error: no package mappings found in {args.mappings}", file=sys.stderr)
        sys.exit(1)
    print(f"Catalog built: {total} package mappings", file=sys.stderr)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(catalog, f, indent=2, sort_keys=False)

    print(f"Catalog written to {args.output}", file=sys.stderr)

    # Print summary to stdout for CI logs
    print(json.dumps(catalog["metadata"], indent=2))


if __name__ == "__main__":
    main()
