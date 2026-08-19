#!/usr/bin/env python3
"""
Generate image catalog JSON for the MCP server.

Builds the image list from compiled documentation (sourced from images-private
via GCS) and the package mappings from package-mappings.yaml (Debian, Fedora,
Alpine to Wolfi equivalents).

Usage:
    python3 scripts/generate_image_catalog.py \
        --docs static/downloads/chainguard-complete-docs.md \
        --mappings data/package-mappings.yaml \
        --output scripts/image-catalog.json \
        --commit abc123
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set

try:
    import yaml
except ImportError:
    print(
        "Error: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr
    )
    sys.exit(1)


def extract_image_names(container_section: str) -> List[str]:
    """Return image names from the compiled '## Container Images' section text.

    compile_docs.py writes each image as
        ### <name>
        <README content>
        <!-- IMAGE_SEPARATOR -->
    so we split on the separator and take the first '### ' heading of each block.
    This is robust to '###' subheadings inside a README (which defeated the older
    regexes) and to image names containing underscores (e.g. sql_exporter).
    Uppercase scaffolding directories such as TEMPLATE are excluded by the
    lowercase-only name pattern.

    NOTE: keep this identical to extract_image_names in scripts/mcp-server.py.
    The catalog and the MCP server must agree on the image set; see DOCS-138.
    """
    names = []
    for block in container_section.split("<!-- IMAGE_SEPARATOR -->"):
        heading = re.search(r"^### (\S+)\s*$", block, re.MULTILINE)
        if heading and re.fullmatch(r"[a-z0-9][a-z0-9_-]*", heading.group(1)):
            names.append(heading.group(1))
    return names


def extract_images_from_docs(docs_path: str) -> Dict[str, Dict[str, Any]]:
    """Extract image names and documentation from compiled docs.

    The compiled docs contain image documentation sourced from images-private,
    organized under '## Container Images' with each image as a '### name' section.
    """
    images = {}
    if not docs_path or not os.path.exists(docs_path):
        return images

    with open(docs_path, "r") as f:
        content = f.read()

    # Find the Container Images section
    container_section = re.search(r"^## Container Images\n", content, re.MULTILINE)
    if not container_section:
        return images

    for name in extract_image_names(content[container_section.end() :]):
        images[name] = {
            "name": name,
            "registry_ref": f"cgr.dev/chainguard/{name}",
            "has_documentation": True,
        }

    return images


def load_package_mappings(mappings_path: str) -> Dict[str, Any]:
    """Load and parse the package-mappings.yaml file."""
    with open(mappings_path, "r") as f:
        return yaml.safe_load(f)


def build_catalog(
    images: Dict[str, Dict[str, Any]],
    mappings: Dict[str, Any],
    commit: Optional[str] = None,
) -> Dict[str, Any]:
    """Build the catalog from images (from docs) and package mappings."""
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
            "total_images": len(images),
            "total_packages_mapped": total_packages,
        },
        "images": images,
        "packages": packages,
    }

    return catalog


def scrape_registry_tags(catalog: Dict[str, Any]) -> Dict[str, Any]:
    """Optionally scrape cgr.dev registry for tag metadata.

    This is an opt-in feature that adds tag listings to each image entry.
    Uses stdlib urllib to avoid extra dependencies.
    """
    import urllib.request
    import urllib.error

    print(
        "Scraping registry for tag metadata (this may take a while)...", file=sys.stderr
    )
    updated = 0

    for name, entry in catalog["images"].items():
        registry_url = f"https://cgr.dev/v2/chainguard/{name}/tags/list"
        try:
            req = urllib.request.Request(registry_url, method="GET")
            req.add_header("Accept", "application/json")
            # nosec B310: registry_url is a hardcoded https://cgr.dev/... reference,
            # not attacker-controlled and never file:/ or a custom scheme.
            with urllib.request.urlopen(req, timeout=10) as resp:  # nosec B310
                data = json.loads(resp.read().decode())
                tags = data.get("tags", [])
                entry["registry_tags"] = tags[:20]
                updated += 1
        except (urllib.error.URLError, urllib.error.HTTPError, Exception):
            entry["registry_tags"] = []

    print(
        f"  Scraped tags for {updated}/{len(catalog['images'])} images", file=sys.stderr
    )
    return catalog


def main():
    parser = argparse.ArgumentParser(
        description="Generate image catalog JSON from compiled docs and package mappings"
    )
    parser.add_argument(
        "--docs",
        required=True,
        help="Path to compiled docs markdown (source of image list)",
    )
    parser.add_argument(
        "--mappings",
        required=True,
        help="Path to data/package-mappings.yaml (source of package equivalents)",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output path for image-catalog.json",
    )
    parser.add_argument(
        "--commit",
        default=None,
        help="Source commit SHA for metadata",
    )
    parser.add_argument(
        "--scrape-registry",
        action="store_true",
        help="Scrape cgr.dev for tag metadata (opt-in, slow)",
    )

    args = parser.parse_args()

    # Extract images from compiled docs (sourced from images-private)
    print(f"Extracting images from {args.docs}...", file=sys.stderr)
    images = extract_images_from_docs(args.docs)
    if not images:
        print("Warning: No images found in compiled docs", file=sys.stderr)
    else:
        print(f"  Found {len(images)} images", file=sys.stderr)

    # Load package mappings
    print(f"Loading package mappings from {args.mappings}...", file=sys.stderr)
    mappings = load_package_mappings(args.mappings)

    # Build catalog
    catalog = build_catalog(images, mappings, args.commit)
    print(
        f"Catalog built: {catalog['metadata']['total_images']} images, "
        f"{catalog['metadata']['total_packages_mapped']} package mappings",
        file=sys.stderr,
    )

    # Optionally scrape registry
    if args.scrape_registry:
        catalog = scrape_registry_tags(catalog)

    # Write output
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(catalog, f, indent=2, sort_keys=False)

    print(f"Catalog written to {args.output}", file=sys.stderr)

    # Print summary to stdout for CI logs
    print(json.dumps(catalog["metadata"], indent=2))


if __name__ == "__main__":
    main()
