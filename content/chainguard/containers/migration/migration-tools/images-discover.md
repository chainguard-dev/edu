---
title: "Find Chainguard replacements with chainctl images discover"
linktitle: "chainctl images discover"
description: "Scan a repository for container image references and see which Chainguard Containers replace them, and whether your organization can pull them today."
type: "article"
date: 2026-10-02T00:00:00+00:00
lastmod: 2026-10-02T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Migration", "chainctl"]
images: []
menu:
  docs:
    parent: "migration"
weight: 5
toc: true
---

`chainctl images discover` reads the image references in a directory, such as a repository checkout, and reports the Chainguard Container that replaces each upstream image. For each replacement, it also tells you whether your organization can pull it today. Use it to size a migration before you start, or to find what's left after one.

The command only reports. It doesn't edit any files. To get replacements suggested on pull requests as images are introduced, enable [Guardener container image suggestions](/chainguard/guardener/github/image-suggestions/). To convert a Dockerfile, use the [Dockerfile Converter](/chainguard/containers/migration/migration-tools/dockerfile-conversion/).

## Prerequisites

- `chainctl` [installed](/platform/chainctl-usage/how-to-install-chainctl/) and authenticated with `chainctl auth login`. If `chainctl images discover --help` reports an unknown command, update `chainctl`.
- Access to the Chainguard organization whose images you want to check. If your identity can access more than one organization, pass `--parent` with the organization name.

## Scan a repository

From the root of a repository, run:

```shell
chainctl images discover
```

To scan another directory, pass its path:

```shell
chainctl images discover ./services
```

The command reads the following files, skipping `.git`, `node_modules`, `vendor`, `.terraform`, and `testdata` directories:

- **Dockerfiles**: every `FROM` instruction, in every build stage, with `ARG` defaults substituted. `FROM scratch` and references to earlier build stages are skipped.
- **YAML and JSON**: Kubernetes manifests, Compose files, Helm values, and any other `image` value. Helm values are read as written, not rendered, so a reference computed inside a chart template isn't seen.
- **Terraform, shell scripts, and Makefiles**: lines about an image, such as an `image` argument or a `docker run` command.

Images used only in `COPY --from` or `RUN --mount` instructions aren't reported.

## Read the results

For each reference, the output shows the file, the current image, and up to three Chainguard replacements, best first. Each replacement has a status:

| Status | Meaning | What to do |
| --- | --- | --- |
| `entitled` | Your organization has this image and the tag, ready to pull. | Switch the reference to the suggested image. |
| `entitled, not ready` | Your organization has this image, but the suggested tag isn't in your repository yet. | Wait for the tag to sync, or choose another tag. |
| `available to add` | Chainguard publishes this image, but your organization doesn't have it. | Add the image to your organization, then switch. |
| `no maintained tag for <tag>` | Chainguard publishes this image, but no maintained tag matches the one you asked for. | Choose a maintained tag. Use `--all-candidates` to list them. |
| `on chainguard` | The reference already uses a Chainguard image. | Nothing. |
| `not available` | Chainguard doesn't publish a replacement. | Nothing to move to. Keep the image or find an alternative. |

References with no replacement are listed too, so the output shows everything a migration would leave behind.

## Check a single image

To check one image without scanning files, pass `--image`. You can repeat it:

```shell
chainctl images discover --image nginx:1.29 --image redis:7.4
```

To see every matching variant and all of its maintained tags, pass one image to `--all-candidates`:

```shell
chainctl images discover --all-candidates nginx:1.29
```

## How replacements are chosen

`chainctl images discover` matches an image to a Chainguard Container by catalog alias first. Otherwise, it matches the end of the repository path, so `registry.example.com/cache/dotnet/sdk` keeps `dotnet/sdk`. A match identifies the Chainguard offering for that software, not an image with identical contents, so test the replacement before you ship it.

The suggested tag follows the reference you wrote:

- A digest-pinned reference stays digest-pinned once the image is in your organization.
- A variant tag, such as `python:3.12-slim`, resolves to the same version without the variant suffix.
- When the requested version isn't maintained, the suggestion moves to the newest maintained version on the same minor line, then the same major line, never to an older line.
- When no version of that major line is maintained, the suggestion falls back to `latest`. Check these before you switch, because `latest` can be a different major version.

FIPS variants rank first by default. To rank standard images first, pass `--fips=false`:

```shell
chainctl images discover --fips=false
```

## Use the results in scripts

Pass `-o json` for machine-readable output. Each result includes the file, line, build stage, requested tag, how the match was made, and every ranked candidate.

```shell
chainctl images discover -o json
```

For every flag, refer to the [`chainctl images discover` reference](/platform/chainctl/chainctl-docs/chainctl_images_discover/).
