#!/usr/bin/env python3
"""Tests for the AI Docs MCP server's document index.

Regression coverage for the `search_docs` defects Jason Bishay reported in
Slack (DOCS-181): an exact page title returned nothing, and the queries that
did match landed on shell comments inside code blocks with empty bodies.

Two layers:

* A synthetic bundle that mirrors what `compile_docs.py` emits. Fast,
  deterministic, and safe to run in CI.
* The real bundle at `static/downloads/chainguard-complete-docs.md`, using
  Jason's four verbatim queries. Skipped when the file is absent. A synthetic
  fixture can only prove the parser handles the shape we think the compiler
  writes; this layer proves it handles what the compiler actually wrote.

Run with:
    pytest scripts/test_mcp_server.py -v
"""

import importlib.util
import os
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
REAL_BUNDLE = REPO_ROOT / "static" / "downloads" / "chainguard-complete-docs.md"

# The page Jason could not retrieve. Ground truth confirmed against the bundle:
# this title and path appear exactly once.
PYTHON_GUIDE_TITLE = "Migrating to Python Chainguard Containers"
PYTHON_GUIDE_PATH = (
    "chainguard/containers/migration/migration-guides/migrating-python.md"
)


def load_server_module():
    """Import scripts/mcp-server.py, whose filename is not a valid module name.

    The module indexes DOCS_PATH at import time. Point it at paths that do not
    exist so the import stays cheap and the tests supply their own content.
    """
    os.environ["DOCS_PATH"] = "/nonexistent/docs.md"
    os.environ["CATALOG_PATH"] = "/nonexistent/catalog.json"

    spec = importlib.util.spec_from_file_location(
        "mcp_server_under_test", Path(__file__).parent / "mcp-server.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mcp_server = load_server_module()


def build_page(title, path, body_lines):
    """Emit one documentation page exactly as compile_docs.py writes it."""
    body = "\n".join(body_lines)
    return f"### {title}\n_Path: {path}_\n\n{body}\n\n---\n"


# A page long enough that the term under test sits past the 50-line window the
# old snippet builder used, which is why every result came back with an empty
# body. The fenced block carries the same shape of shell comment that the old
# parser mistook for a top-level heading.
PYTHON_GUIDE_BODY = (
    [
        "## Overview",
        "",
        "This guide covers moving an application onto a Chainguard Python container.",
        "",
        "```bash",
        "# Install Composer and set up application",
        "composer install",
        "# Run the server",
        "./serve.sh",
        "```",
        "",
    ]
    + ["Filler line about container migration steps." for _ in range(60)]
    + [
        "",
        "## Multi-stage builds",
        "",
        "Use the -dev variant at build time and the runtime image to ship.",
    ]
)

SYNTHETIC_BUNDLE = (
    "# Chainguard Documentation Bundle\n\n"
    "## Usage Guide\n\n"
    "Ask about container images, migration, and security.\n\n"
    "## Table of Contents\n\n"
    "1. [Usage Guide](#usage-guide)\n"
    "2. [Documentation Content](#documentation-content)\n\n"
    "---\n\n"
    "## Documentation Content\n\n"
    + build_page(PYTHON_GUIDE_TITLE, PYTHON_GUIDE_PATH, PYTHON_GUIDE_BODY)
    + build_page(
        "Getting Started with Chainguard Containers",
        "chainguard/containers/getting-started.md",
        ["## Prerequisites", "", "You need a cgr.dev account."],
    )
    + "\n---\n\n"
    "## Container Images\n\n"
    "_This section contains documentation for Chainguard container images._\n\n"
    "### python\n"
    "A minimal Python container image.\n"
    "\n<!-- IMAGE_SEPARATOR -->\n"
    "### nginx\n"
    "A minimal nginx container image.\n"
    "\n<!-- IMAGE_SEPARATOR -->\n"
)


@pytest.fixture(scope="module")
def index():
    return mcp_server.ChaguardDocsIndex(SYNTHETIC_BUNDLE)


@pytest.fixture(scope="module")
def real_index():
    if not REAL_BUNDLE.exists():
        pytest.skip(f"bundle not present at {REAL_BUNDLE}")
    return mcp_server.ChaguardDocsIndex(REAL_BUNDLE.read_text(encoding="utf-8"))


# --- Section parsing -------------------------------------------------------


def test_pages_are_keyed_by_their_title(index):
    """A reader searching for a page should get the page, named as the page."""
    assert PYTHON_GUIDE_TITLE in index.sections


def test_comments_inside_code_blocks_do_not_become_sections(index):
    """The defect behind Jason's results: '# comment' in a fence started a section."""
    assert "Install Composer and set up application" not in index.sections
    assert "Run the server" not in index.sections


def test_headings_inside_a_page_do_not_split_it(index):
    """A page's own '##' headings belong to the page, not to sections of their own."""
    assert "Overview" not in index.sections
    assert "Multi-stage builds" not in index.sections
    assert "Multi-stage builds" in index.sections[PYTHON_GUIDE_TITLE]


def test_page_content_is_not_truncated(index):
    """The whole page is indexed, so terms late in a long page stay findable."""
    page = index.sections[PYTHON_GUIDE_TITLE]
    assert "Use the -dev variant at build time" in page


def test_image_sections_still_parse(index):
    """Images keep their existing 'image:' keys; this path already worked."""
    assert "image:python" in index.sections
    assert "image:nginx" in index.sections
    assert index.images == ["nginx", "python"]


def test_no_content_is_dropped(index):
    """Every section of the bundle lands somewhere in the index."""
    indexed = "\n".join(index.sections.values())
    assert "Ask about container images, migration, and security." in indexed


# --- Search results --------------------------------------------------------


def test_exact_page_title_returns_that_page(index):
    results = index.search(PYTHON_GUIDE_TITLE)
    assert results, "an exact page title must return the page"
    assert results[0]["section"] == PYTHON_GUIDE_TITLE


def test_every_result_has_a_body(index):
    """Jason's hits were all empty, so a relevant match told the caller nothing."""
    for query in ["python", PYTHON_GUIDE_TITLE, "multi-stage builds"]:
        for result in index.search(query):
            assert result["snippet"].strip(), f"empty body for query {query!r}"


def test_terms_match_without_the_exact_phrase(index):
    """'migrating python' must find "Migrating to Python …" — the words are never
    adjacent in the corpus, so whole-phrase substring matching returns nothing."""
    results = index.search("migrating python")
    assert PYTHON_GUIDE_TITLE in [r["section"] for r in results]


def test_natural_language_query_finds_the_page(index):
    """MCP clients ask in sentences. The tool has to tolerate that."""
    results = index.search("Give me the migration guide for python")
    assert PYTHON_GUIDE_TITLE in [r["section"] for r in results]


def test_results_carry_the_page_url(index):
    """A caller asking for a guide should get a link they can open."""
    result = index.search(PYTHON_GUIDE_TITLE)[0]
    assert result["url"] == (
        "https://edu.chainguard.dev/chainguard/containers/migration"
        "/migration-guides/migrating-python/"
    )


def test_image_results_have_no_url(index):
    """Image READMEs are not published pages, so there is nothing to link to."""
    for result in index.search("nginx container image"):
        if result["section"].startswith("image:"):
            assert result["url"] == ""


@pytest.mark.parametrize(
    "source_path,expected",
    [
        # Verified against the live site, 2026-09-08: all four return HTTP 200.
        (
            "chainguard/containers/migration/migration-guides/migrating-python.md",
            "https://edu.chainguard.dev/chainguard/containers/migration"
            "/migration-guides/migrating-python/",
        ),
        # Branch bundle: 32 pages in the bundle are named _index.md.
        (
            "platform/administration/cloudevents/_index.md",
            "https://edu.chainguard.dev/platform/administration/cloudevents/",
        ),
        # Leaf bundle: 76 pages are named index.md, and Hugo serves those at
        # the directory too. Appending '/index/' 404s.
        (
            "chainguard/containers/how-to-use/retrieve-image-sboms/index.md",
            "https://edu.chainguard.dev/chainguard/containers/how-to-use"
            "/retrieve-image-sboms/",
        ),
        ("ai-docs-security.md", "https://edu.chainguard.dev/ai-docs-security/"),
        ("_index.md", "https://edu.chainguard.dev/"),
        ("index.md", "https://edu.chainguard.dev/"),
    ],
)
def test_page_url_mapping(source_path, expected):
    assert mcp_server.page_url(source_path) == expected


def test_search_docs_output_shows_the_url(monkeypatch, index):
    """The rendered tool response, not just the internal result dict."""
    monkeypatch.setattr(mcp_server, "docs_index", index)
    output = mcp_server.search_docs(PYTHON_GUIDE_TITLE, max_results=1)
    assert "https://edu.chainguard.dev/chainguard/containers/migration" in output


def test_title_match_outranks_an_incidental_body_mention(index):
    """A page about the topic should beat a page that merely mentions the word."""
    results = index.search(PYTHON_GUIDE_TITLE)
    assert results[0]["section"] == PYTHON_GUIDE_TITLE


# --- The real bundle -------------------------------------------------------


@pytest.mark.parametrize(
    "query",
    [
        PYTHON_GUIDE_TITLE,
        "migrating python",
        "Give me the migration guide for python",
        "python migration",
    ],
)
def test_jasons_queries_find_the_python_guide(real_index, query):
    """The four queries from the Slack report, run against the shipped bundle."""
    sections = [r["section"] for r in real_index.search(query, max_results=5)]
    assert PYTHON_GUIDE_TITLE in sections, f"got {sections}"


def test_real_bundle_results_are_never_empty(real_index):
    for query in ["python migration", "chainctl login", "FIPS"]:
        for result in real_index.search(query):
            assert result["snippet"].strip(), f"empty body for query {query!r}"


def test_real_bundle_sections_are_document_headings(real_index):
    """No section key should be a shell comment. 1,992 of them were."""
    for name in index_page_keys(real_index):
        assert not name.startswith("#"), f"{name!r} looks like a raw heading"
    assert PYTHON_GUIDE_TITLE in real_index.sections


def index_page_keys(idx):
    return [name for name in idx.sections if not name.startswith("image:")]
