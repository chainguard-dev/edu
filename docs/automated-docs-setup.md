# AI documentation bundle pipeline

This guide explains how the compiled documentation bundle is built, published,
and refreshed.

## Overview

The bundle combines two sources, both from this repository:

- edu content, from `content/`
- Dockerfile Converter (dfc) package and image mappings, from
  `data/package-mappings.yaml`

The `.github/workflows/compile-ai-docs-from-gcs.yaml` workflow compiles them
into a single Markdown file and publishes it. `scripts/compile_docs.py` writes
the bundle, and `scripts/generate_package_catalog.py` writes
`package-mappings.json`, the catalog behind the MCP server's
`find_package_equivalent` and `find_image_equivalent` tools. The build also
ships the catalog as `image-catalog.json`, its earlier name.

The nightly `autodocs-platform.yaml` workflow keeps
`data/package-mappings.yaml` current: it downloads dfc's `builtin-mappings.yaml`
and includes any change in its pull request. To change a mapping, change it in
[chainguard-dev/dfc](https://github.com/chainguard-dev/dfc), not here.

## Publishing targets

One workflow owns every target, so a given commit produces one bundle
everywhere:

| Target | Refreshed |
| -- | -- |
| `ghcr.io/chainguard-dev/ai-docs` on GHCR, signed with cosign | Every run |
| Artifact Registry, then the `mcp-server` Cloud Run service | Every run |
| `gs://academy-all-docs/compiled/` | Every run |
| `static/downloads/chainguard-complete-docs.md`, served at edu.chainguard.dev | Nightly, by pull request |

The served download is the exception. Hugo publishes `static/downloads/`
straight from git, so that copy only changes when a commit lands. The nightly
scheduled run compares the freshly compiled bundle against the committed one,
ignoring the embedded `_Compiled on:_` timestamp, and opens a pull request only
when the content differs. Merging that pull request is what refreshes the
public download.

The nightly run also checks the age of the served bundle and fails when it
falls more than 14 days behind, which catches a refresh pull request that
nobody merged.

## Triggers

The workflow runs on:

- An `ai-docs-source-updated` repository dispatch event, which
  `export-edu-docs-to-gcs.yaml` sends after a push to `main` that changes
  content
- A push to `main` that changes `scripts/` or the workflow itself, so a server
  fix deploys without waiting for the nightly run
- The nightly schedule, at 02:00 UTC
- A manual run from the **Actions** tab

Only the scheduled and manual runs open a pull request.

## Authentication

The compile job federates a GCP token through workload identity to write to
the bucket and to deploy. The publish job federates a separate GitHub token
through octo-sts, using the trust policy in
`.github/chainguard/ai-docs.sts.yaml`, which grants only `contents: write` and
`pull_requests: write`.

Keeping the two jobs separate means the job that builds and signs container
images never holds a git-write credential.

## Test the compilation locally

Compile the bundle and the catalog from a checkout of this repository:

```bash
python3 scripts/compile_docs.py
python3 scripts/generate_package_catalog.py \
  --mappings data/package-mappings.yaml \
  --output /tmp/package-mappings.json
```

The bundle lands in `static/downloads/chainguard-complete-docs.md`. Don't
commit that file; the nightly pull request owns it.

To run the MCP server's unit tests:

```bash
pip install -r scripts/mcp-requirements.txt pytest pyyaml
pytest scripts/test_mcp_server.py scripts/test_mcp_transport.py scripts/test_compile_docs.py
```

## Troubleshoot

**The served download is stale.** Check for an open `[AI Docs] Refresh the
documentation bundle` pull request. If none exists, check whether the nightly
run succeeded.

**The bundle has no DFC mappings page.** The compile log shows `WARNING:
data/package-mappings.yaml not found` instead of `DFC mappings added`. Confirm
the file exists on `main`.

**The compile job fails on size.** The bundle has a 50 MB ceiling. Something
in `content/` has grown unexpectedly.

**The compile job fails on the credential scan.** The bundle carries a pattern
that looks like a real key. Find it in the workflow log, then fix the source
document rather than the scan.
