#!/usr/bin/env python3
"""Tests for the AI Docs MCP server's document index.

Regression coverage for the `search_docs` defects reported in Slack
(DOCS-181): an exact page title returned nothing, and the queries that did
match landed on shell comments inside code blocks with empty bodies.

Two layers:

* A synthetic bundle that mirrors what `compile_docs.py` emits. Deterministic,
  so this is where every assertion about search behavior lives, including the
  four verbatim queries from the report.
* The real bundle at `static/downloads/chainguard-complete-docs.md`. Skipped
  when the file is absent. A synthetic fixture can only prove the parser
  handles the shape we think the compiler writes; this layer proves it handles
  what the compiler actually wrote.

The real-bundle layer asserts structure only, and derives whatever page
identities it needs from the bundle at run time. That bundle is refreshed
nightly from live content, so an assertion naming a specific page title or
path is a time bomb: the Containers reorganization (#3926) retitled one page
and turned every PR touching `scripts/` red two days later. Keep content
identities out of this file.

Run with:
    pytest scripts/test_mcp_server.py -v
"""

import importlib.util
import os
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
REAL_BUNDLE = REPO_ROOT / "static" / "downloads" / "chainguard-complete-docs.md"

# The page that could not be retrieved, as it was titled at the time. The
# synthetic bundle below is built from these two values, so they are fixture
# inputs, not ground truth: nothing here has to match a page in content/, and
# nothing breaks when the real page is retitled or moved. Do not try to keep
# them in sync — see the module docstring.
#
# The title's shape is load-bearing. 'Migrating' and 'Python' are not adjacent
# in it, which is what makes test_reported_queries_find_the_python_guide a
# real test of per-term scoring rather than phrase matching. Leave it alone.
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
def real_bundle_text():
    if not REAL_BUNDLE.exists():
        pytest.skip(f"bundle not present at {REAL_BUNDLE}")
    return REAL_BUNDLE.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def real_index(real_bundle_text):
    return mcp_server.ChaguardDocsIndex(real_bundle_text)


# --- Section parsing -------------------------------------------------------


def test_pages_are_keyed_by_their_title(index):
    """A reader searching for a page should get the page, named as the page."""
    assert PYTHON_GUIDE_TITLE in index.sections


def test_comments_inside_code_blocks_do_not_become_sections(index):
    """The defect behind the reported results: '# comment' in a fence started one."""
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
    """The reported hits were all empty, so a relevant match told the caller nothing."""
    for query in ["python", PYTHON_GUIDE_TITLE, "multi-stage builds"]:
        for result in index.search(query):
            assert result["snippet"].strip(), f"empty body for query {query!r}"


@pytest.mark.parametrize(
    "query",
    [
        # The exact title. Returned nothing at all.
        PYTHON_GUIDE_TITLE,
        # Terms that are never adjacent in the page, so whole-phrase substring
        # matching finds nothing.
        "migrating python",
        # MCP clients ask in sentences. The tool has to tolerate that.
        "Give me the migration guide for python",
        "python migration",
    ],
)
def test_reported_queries_find_the_python_guide(index, query):
    """The four queries from the Slack report (DOCS-181).

    These ran against the real bundle until 2026-09-10. That coupled them to a
    live page title, and a retitle broke CI on unrelated PRs. The synthetic
    bundle tests the same search behavior and cannot rot.
    """
    sections = [r["section"] for r in index.search(query, max_results=5)]
    assert PYTHON_GUIDE_TITLE in sections, f"got {sections}"


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
        # These exercise page_url(), a pure function, so a moved page cannot
        # fail the test — but pick paths that exist so the examples stay
        # legible. All four verified HTTP 200 on the live site, 2026-09-10.
        (
            "chainguard/containers/migration/migration-guides/python.md",
            "https://edu.chainguard.dev/chainguard/containers/migration"
            "/migration-guides/python/",
        ),
        # Branch bundle: pages named _index.md serve at their directory.
        (
            "platform/administration/cloudevents/_index.md",
            "https://edu.chainguard.dev/platform/administration/cloudevents/",
        ),
        # Leaf bundle: pages named index.md serve at the directory too, so
        # appending '/index/' 404s. Around one in eight pages is one of these.
        (
            "chainguard/containers/security-and-compliance"
            "/retrieve-image-sboms/index.md",
            "https://edu.chainguard.dev/chainguard/containers"
            "/security-and-compliance/retrieve-image-sboms/",
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
#
# Structural assertions only. Every ground truth here is read out of the
# bundle at run time, so nothing in this section names a page. See the module
# docstring for why.

# Exact-title retrieval is a rate, not a per-page guarantee. Twelve pages are
# titled with a single common word — 'Cosign', 'Wolfi', 'chainctl', 'Rekor',
# 'melange' — and lose to the hundreds of pages that mention the term. That is
# a scoring nuance, not the DOCS-181 defect, and not worth gating a merge on.
# Measured 2026-09-10 over all 592 distinct titles: 528 ranked first, 580 in
# the top five, 12 missed.
TITLE_SAMPLE_SIZE = 40
MIN_TITLE_HIT_RATE = 0.9


def pages_declared_in(bundle_text):
    """The page titles the compiler declared, read straight out of the raw text.

    Ground truth has to come from somewhere other than the index, or these
    assertions are tautologies: a mis-parsed bundle still contains whatever
    junk keys it mis-parsed into, and searching for one of those keys happily
    returns it. An earlier version of this section sampled titles from the
    index itself, and the pre-fix parser passed every one of its assertions.

    compile_docs.py writes every page as a '### <title>' line followed by a
    '_Path: <path>_' line, and nothing else in the bundle carries that pair.
    This deliberately plain line scan is a second implementation of that rule,
    independent of ChaguardDocsIndex.
    """
    docs_region = bundle_text.split("\n## Container Images\n")[0]
    lines = docs_region.split("\n")
    return [
        lines[i - 1].removeprefix("### ").strip()
        for i, line in enumerate(lines)
        if i and line.startswith("_Path: ") and lines[i - 1].startswith("### ")
    ]


def sampled(titles, count=TITLE_SAMPLE_SIZE):
    """A deterministic sample spread across the bundle rather than the first N.

    Searching every title takes about two minutes: each query scans an 11 MB
    string. Striding keeps the sample representative without that cost.
    """
    stride = max(1, len(titles) // count)
    return titles[::stride][:count]


def test_real_bundle_declares_many_pages(real_bundle_text):
    """Guards the ground truth itself, so the equality check cannot go vacuous.

    The bundle declared 597 pages (592 distinct titles) on 2026-09-10 and only
    grows. If the compiler's page signature ever changes, this fails here
    rather than silently agreeing with an index that found nothing either.
    """
    assert len(pages_declared_in(real_bundle_text)) > 300


def test_real_bundle_keys_are_the_declared_pages(real_index, real_bundle_text):
    """Every indexed page is a declared page, and every declared page is indexed.

    The DOCS-181 defect: the old parser started a section at any line
    beginning '# ', so shell comments inside fenced blocks became keys. Run
    against the 2026-09-10 bundle it yields 2,295 keys, exactly one of which
    is a real page, and misses 591 of the 592 declared pages — which is why
    whole guides were unfindable by their own title.

    This replaced an assertion that no key starts with '#'. That one never
    caught the defect: the old parser stripped the marker before using the
    line as a key, so none of its 2,295 keys started with '#' either.
    """
    declared = set(pages_declared_in(real_bundle_text))
    indexed = set(index_page_keys(real_index)) - {"Bundle Usage Guide"}

    # A handful of titles repeat across languages ('Global configuration'
    # exists for Java, JavaScript and Python), and the index qualifies those
    # with their source path to keep them distinct.
    indexed = {
        name.split(" (")[0] if name.endswith(".md)") else name for name in indexed
    }

    assert indexed == declared, (
        f"{len(indexed - declared)} indexed pages are not declared pages, "
        f"{len(declared - indexed)} declared pages are missing from the index"
    )


def test_real_bundle_exact_titles_return_their_page(real_index, real_bundle_text):
    """Searching a real page's exact title returns that page.

    The headline reported symptom, measured against titles taken from the raw
    bundle rather than from the index under test.
    """
    titles = sampled(pages_declared_in(real_bundle_text))
    missed = [
        title
        for title in titles
        if title not in [r["section"] for r in real_index.search(title, max_results=5)]
    ]
    hit_rate = 1 - len(missed) / len(titles)
    assert hit_rate >= MIN_TITLE_HIT_RATE, (
        f"{hit_rate:.0%} of {len(titles)} exact titles returned their page "
        f"(want {MIN_TITLE_HIT_RATE:.0%}); missed {missed}"
    )


def test_real_bundle_results_are_never_empty(real_index):
    for query in ["python migration", "chainctl login", "FIPS"]:
        for result in real_index.search(query):
            assert result["snippet"].strip(), f"empty body for query {query!r}"


def index_page_keys(idx):
    return [name for name in idx.sections if not name.startswith("image:")]
