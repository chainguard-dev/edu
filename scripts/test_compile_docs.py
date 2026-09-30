#!/usr/bin/env python3
"""Tests for the AI docs bundle compiler, scripts/compile_docs.py.

These compile a real bundle from the checkout's content/ and data/ into a
temporary file, so they need no network and no GCS access.

Run with:
    pytest scripts/test_compile_docs.py -v
"""

import importlib.util
import os
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parent
MAPPINGS_FILE = REPO_ROOT / "data" / "package-mappings.yaml"

sys.path.insert(0, str(SCRIPTS))
import compile_docs  # noqa: E402


def load_server_module():
    """Import scripts/mcp-server.py, whose filename is not a valid module name."""
    os.environ["DOCS_PATH"] = "/nonexistent/docs.md"
    os.environ["CATALOG_PATH"] = "/nonexistent/catalog.json"
    spec = importlib.util.spec_from_file_location(
        "mcp_server_for_compile_tests", SCRIPTS / "mcp-server.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def bundle_text(tmp_path_factory):
    output = tmp_path_factory.mktemp("bundle") / "bundle.md"
    compile_docs.compile_documentation(str(output))
    return output.read_text(encoding="utf-8")


def test_bundle_carries_the_dfc_mappings_verbatim(bundle_text):
    """DOCS-174: the mappings were downloaded, then silently dropped.

    Ground truth is the committed file itself, read here without the compiler.
    """
    heading = (
        f"### {compile_docs.DFC_SECTION_TITLE}\n"
        f"_Path: {compile_docs.DFC_SECTION_PATH}_\n"
    )
    assert heading in bundle_text

    expected = MAPPINGS_FILE.read_text(encoding="utf-8")
    assert f"```yaml\n{expected}\n```" in bundle_text


def test_dfc_section_is_indexed_and_links_to_the_mappings_page(bundle_text):
    """The server treats the section as a page and links the rendered tables."""
    server = load_server_module()
    index = server.ChaguardDocsIndex(bundle_text)
    assert compile_docs.DFC_SECTION_TITLE in index.sections

    results = index.search(compile_docs.DFC_SECTION_TITLE, max_results=5)
    urls = [r["url"] for r in results if r["section"] == compile_docs.DFC_SECTION_TITLE]
    assert urls == [
        "https://edu.chainguard.dev/chainguard/containers/reference/package-name-mappings/"
    ]


def test_bundle_has_no_image_or_course_sections(bundle_text):
    """Both sources were frozen snapshots, removed in DOCS-138."""
    assert "\n## Container Images\n" not in bundle_text
    assert "<!-- IMAGE_SEPARATOR -->" not in bundle_text
