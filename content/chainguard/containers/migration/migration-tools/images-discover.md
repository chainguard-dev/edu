---
title: "Find Chainguard replacements with chainctl images discover"
linktitle: "chainctl images discover"
description: "Scan a repository for container image references and see which Chainguard container images replace them, and whether your organization can pull them today."
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

`chainctl images discover` reads the image references in a directory, such as a repository checkout, and reports the Chainguard container image that replaces each upstream image. For each replacement, it also tells you whether your organization can pull it today. Use it to size a migration before you start, or to find what's left after one.

The command only reports. It doesn't edit any files. To get replacements suggested on pull requests as images are introduced, enable [Guardener Container Image Suggestions](/chainguard/guardener/github/image-suggestions/). To convert a Dockerfile, use the [Dockerfile Converter](/chainguard/containers/migration/migration-tools/dockerfile-conversion/).

## Prerequisites

- `chainctl` [installed](/platform/chainctl-usage/how-to-install-chainctl/) and authenticated with `chainctl auth login`. If `chainctl images discover --help` reports an unknown command, update `chainctl`.
- Access to the Chainguard organization whose images you want to check, with a role that grants the `groups.list`, `repo.list`, and `tag.list` capabilities. If your identity can access more than one organization, pass `--parent` with the organization name or ID. Without it, the command asks you to choose in a terminal and exits with an error in CI.

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

- **Dockerfiles**: every `FROM` instruction, in every build stage, with `ARG` defaults substituted. The command skips `FROM scratch`, references to earlier build stages, and references that depend on an `ARG` with no default.
- **YAML and JSON**: Kubernetes manifests, Compose files, Helm values, and any other `image` value, including Helm-style `image` mappings split into `registry`, `repository`, and `tag` keys. A mapping with an empty tag uses the chart's `appVersion`. Helm values are read as written, not rendered, so a reference computed inside a chart template isn't seen.
- **Terraform, shell scripts, and Makefiles**: lines about an image, such as an `image` argument or a `docker run` command.

Images used only in `COPY --from` or `RUN --mount` instructions aren't reported.

## Read the results

For each reference, the output shows the file, the current image, and up to three Chainguard replacements, best first:

```
---------------------|------------------|---------------------------------------|------------------
 FILE                | CURRENT IMAGE    | CHAINGUARD IMAGE                      | STATUS
---------------------|------------------|---------------------------------------|------------------
 app/Dockerfile      | python:3.12-slim | cgr.dev/my-org/python-fips:3.12       | entitled
                     |                  | cgr.dev/my-org/python:3.12            | entitled
---------------------|------------------|---------------------------------------|------------------
 app/Dockerfile      | node:22          | cgr.dev/my-org/node:22                | entitled
                     |                  | cgr.dev/my-org/node-fips:22           | available to add
---------------------|------------------|---------------------------------------|------------------
 deploy/compose.yaml | nginx:1.29       | cgr.dev/my-org/nginx:1.31.6           | entitled
                     |                  | cgr.dev/my-org/nginx-fips:1.31.6      | available to add
                     |                  | cgr.dev/my-org/nginx-otel-fips:1.31.6 | available to add
---------------------|------------------|---------------------------------------|------------------
 deploy/compose.yaml | redis:7.4        | cgr.dev/my-org/redis-fips:7.4         | available to add
                     |                  | cgr.dev/my-org/redis:7.4              | available to add
                     |                  | cgr.dev/my-org/redis-sentinel:7.4     | available to add
---------------------|------------------|---------------------------------------|------------------
```

In a narrow terminal, the same results print as a list instead of a table. Each replacement has a status:

| Status | Meaning | What to do |
| --- | --- | --- |
| `entitled` | Your organization has this image and the tag, ready to pull. | Switch the reference to the suggested image. |
| `entitled, not ready` | Your organization has this image, but the suggested tag isn't in your repository yet. | Wait for the tag to sync, or choose another tag. |
| `available to add` | Chainguard publishes this image, but your organization doesn't have it. | [Add the image to your organization](/chainguard/containers/troubleshooting/container-version-troubleshooting/#the-container-isnt-in-your-organizations-catalog), then switch. |
| `no maintained tag for <tag>` | Chainguard publishes this image, but no maintained tag matches the one you asked for. | Choose a maintained tag. Use `--all-candidates` to list them. |
| `on chainguard` | The reference already uses a Chainguard image. | No action needed. |
| `not available` | Chainguard doesn't publish a replacement. | Nothing to move to. Keep the image or find an alternative. |

Whether adding an image is self-service depends on your subscription. Refer to [The container isn't in your organization's catalog](/chainguard/containers/troubleshooting/container-version-troubleshooting/#the-container-isnt-in-your-organizations-catalog) for the steps and the roles each one needs.

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

`chainctl images discover` matches an image to a Chainguard container image by catalog alias first. Otherwise, it tries progressively shorter suffixes of the repository path, so `registry.example.com/cache/dotnet/sdk` can match `dotnet/sdk`, and a path ending in `nginx` can match `nginx`. A match identifies the Chainguard offering for that software, not an image with identical contents, so test the replacement before you ship it. To match on image contents instead, use [Image Matcher](/chainguard/containers/migration/migration-tools/image-matcher/).

The suggested tag follows the reference you wrote:

- A maintained tag stays as written.
- An untagged reference becomes `latest`, the tag Docker uses anyway.
- A digest-pinned reference stays digest-pinned once the image is in your organization. Until then, the suggestion uses a tag, because the digest isn't known yet.
- A variant tag, such as `python:3.12-slim`, resolves to the same version without the variant suffix.
- When the requested version isn't maintained, the suggestion moves to the newest maintained version on the same minor line, then the same major line, never to an older line.
- When no version of that major line is maintained, the suggestion falls back to `latest`. Check a `latest` suggestion before you switch, because it can be a different major version.

Images your organization already has rank ahead of images it doesn't. Within each group, FIPS variants rank first by default. To rank standard images first, pass `--fips=false`:

```shell
chainctl images discover --fips=false
```

## Use the results in scripts

Pass `-o json` for machine-readable output. Each result includes the file, line, build stage, requested tag, how the match was made, and every ranked candidate.

```shell
chainctl images discover -o json
```

For every flag, refer to the [`chainctl images discover` reference](/platform/chainctl/chainctl-docs/chainctl_images_discover/).
