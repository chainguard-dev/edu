#!/usr/bin/env python3
"""
Generate image catalog JSON from package-mappings.yaml.

Produces a structured catalog of Chainguard container images and package
mappings for use by the MCP server. Optionally cross-references compiled
docs to set has_documentation flags, and can scrape the registry for tag
metadata.

Usage:
    python3 scripts/generate_image_catalog.py \
        --mappings data/package-mappings.yaml \
        --docs static/downloads/chainguard-complete-docs.md \
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
    print("Error: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def load_mappings(mappings_path: str) -> Dict[str, Any]:
    """Load and parse the package-mappings.yaml file."""
    with open(mappings_path, "r") as f:
        return yaml.safe_load(f)


def extract_documented_images(docs_path: str) -> Set[str]:
    """Extract image names that have documentation from the compiled docs."""
    documented = set()
    if not docs_path or not os.path.exists(docs_path):
        return documented

    with open(docs_path, "r") as f:
        content = f.read()

    # Look for image sections under "## Container Images"
    container_section = re.search(r"^## Container Images\n", content, re.MULTILINE)
    if container_section:
        section_content = content[container_section.end() :]
        for match in re.finditer(r"\n### ([a-z0-9\-]+)\n", section_content):
            documented.add(match.group(1))

    return documented


def parse_chainguard_ref(value: str) -> Dict[str, str]:
    """Parse a Chainguard image value into name, tag, and registry ref."""
    # Value may be like "chainguard-base:latest" or just "nginx"
    if ":" in value:
        name, tag = value.rsplit(":", 1)
    else:
        name = value
        tag = "latest"

    return {
        "name": name,
        "tag": tag,
        "registry_ref": f"cgr.dev/chainguard/{name}:{tag}",
    }


def build_catalog(
    mappings: Dict[str, Any],
    documented_images: Set[str],
    commit: Optional[str] = None,
) -> Dict[str, Any]:
    """Build the image catalog from parsed mappings data."""
    images_map = mappings.get("images", {})
    packages_map = mappings.get("packages", {})

    # Build images index: collect all unique Chainguard image names
    images = {}
    upstream_to_chainguard = {}

    for upstream, chainguard_value in images_map.items():
        parsed = parse_chainguard_ref(chainguard_value)
        cg_name = parsed["name"]

        # Track upstream-to-chainguard mapping
        upstream_to_chainguard[upstream] = parsed["registry_ref"]

        # Build or update the image entry
        if cg_name not in images:
            images[cg_name] = {
                "name": cg_name,
                "registry_ref": f"cgr.dev/chainguard/{cg_name}",
                "upstream_mappings": [],
                "has_documentation": cg_name in documented_images,
                "variants": [],
            }

        images[cg_name]["upstream_mappings"].append(upstream)

        # Track variants (tags other than "latest")
        tag = parsed["tag"]
        if tag != "latest" and tag not in images[cg_name]["variants"]:
            images[cg_name]["variants"].append(tag)

    # Build packages index
    packages = {}
    for distro, pkg_map in packages_map.items():
        packages[distro] = {}
        if pkg_map:
            for os_pkg, wolfi_pkgs in pkg_map.items():
                if isinstance(wolfi_pkgs, list):
                    packages[distro][os_pkg] = wolfi_pkgs
                else:
                    # Handle empty or null mappings
                    packages[distro][os_pkg] = []

    # Calculate totals
    total_upstream = len(upstream_to_chainguard)
    total_packages = sum(
        len(pkg_map) for pkg_map in packages.values() if pkg_map
    )

    catalog = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
            "source_commit": commit or "unknown",
            "total_images": len(images),
            "total_upstream_mappings": total_upstream,
            "total_packages_mapped": total_packages,
        },
        "images": images,
        "upstream_to_chainguard": upstream_to_chainguard,
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

    print("Scraping registry for tag metadata (this may take a while)...", file=sys.stderr)
    updated = 0

    for name, entry in catalog["images"].items():
        registry_url = f"https://cgr.dev/v2/chainguard/{name}/tags/list"
        try:
            req = urllib.request.Request(registry_url, method="GET")
            req.add_header("Accept", "application/json")
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                tags = data.get("tags", [])
                entry["registry_tags"] = tags[:20]  # Limit to 20 tags
                updated += 1
        except (urllib.error.URLError, urllib.error.HTTPError, Exception) as e:
            # Graceful degradation: just skip images we can't reach
            entry["registry_tags"] = []

    print(f"  Scraped tags for {updated}/{len(catalog['images'])} images", file=sys.stderr)
    return catalog


def main():
    parser = argparse.ArgumentParser(
        description="Generate image catalog JSON from package-mappings.yaml"
    )
    parser.add_argument(
        "--mappings",
        required=True,
        help="Path to data/package-mappings.yaml",
    )
    parser.add_argument(
        "--docs",
        default=None,
        help="Path to compiled docs markdown (for has_documentation flag)",
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

    # Load mappings
    print(f"Loading mappings from {args.mappings}...", file=sys.stderr)
    mappings = load_mappings(args.mappings)

    # Extract documented images
    documented = set()
    if args.docs:
        print(f"Cross-referencing docs from {args.docs}...", file=sys.stderr)
        documented = extract_documented_images(args.docs)
        print(f"  Found {len(documented)} documented images", file=sys.stderr)

    # Build catalog
    catalog = build_catalog(mappings, documented, args.commit)
    print(
        f"Catalog built: {catalog['metadata']['total_images']} images, "
        f"{catalog['metadata']['total_upstream_mappings']} upstream mappings, "
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
