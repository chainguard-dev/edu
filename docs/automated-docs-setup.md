# AI documentation bundle pipeline

This guide explains how the compiled documentation bundle is built, published,
and refreshed.

## Overview

The bundle combines documentation from four sources:

- edu content, from `content/` in this repository
- Container image READMEs, from the images-private repository
- Course content, from the courses repository
- Dockerfile Converter package mappings, from the dfc repository

Each source repository exports a tarball to the `academy-all-docs` bucket in
the `chainguard-academy` GCP project, then sends an `ai-docs-source-updated`
repository dispatch event to this repository. The
`.github/workflows/compile-ai-docs-from-gcs.yaml` workflow compiles the
sources into a single markdown file and publishes it.

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

- An `ai-docs-source-updated` repository dispatch event from any source
  repository
- The nightly schedule, at 02:00 UTC
- A manual run from the **Actions** tab

Only the scheduled and manual runs open a pull request.

## Export workflows

Each source repository needs an export workflow. Use the templates in
`.github/workflows/templates/`:

- `export-docs-to-gcs.yaml`
- `export-images-docs-to-gcs.yaml`
- `export-courses-docs-to-gcs.yaml`

The templates authenticate with workload identity federation against the
`chainguard-academy` pool. They don't use personal access tokens.

## Authentication

The compile job federates a GCP token through workload identity to read from
and write to the bucket. The publish job federates a separate GitHub token
through octo-sts, using the trust policy in
`.github/chainguard/ai-docs.sts.yaml`, which grants only `contents: write` and
`pull_requests: write`.

Keeping the two jobs separate means the job that builds and signs container
images never holds a git-write credential.

## Test the compilation locally

The compile script reads the three external sources from sibling directories.
To compile edu content alone, create empty placeholders:

```bash
mkdir -p ../courses ../images-private ../dfc
python3 scripts/compile_docs.py
```

The result lands in `static/downloads/chainguard-complete-docs.md`. Expect a
much smaller file than the published bundle, because it contains no image
READMEs. Don't commit that file.

## Troubleshoot

**The served download is stale.** Check for an open `[AI Docs] Refresh the
documentation bundle` pull request. If none exists, check whether the nightly
run succeeded.

**The bundle is missing image documentation.** The images-private export is
failing, so the compile job is rebuilding from an old tarball. Read the
`Metadata information:` block in the `Download documentation from GCS` step,
which prints the `export_time` for each source.

**The compile job fails on size.** The bundle has a 50 MB ceiling. Something
in a source export has grown unexpectedly.

**The compile job fails on the credential scan.** The bundle carries a pattern
that looks like a real key. Find it in the workflow log, then fix the source
document rather than the scan.
