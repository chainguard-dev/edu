---
title: "Guardener Container Image Suggestions"
linktitle: "Container Image Suggestions"
description: "Configure Guardener to recommend Chainguard container images for the container images a pull request adds or changes."
type: "article"
date: 2026-10-02T00:00:00+00:00
lastmod: 2026-10-02T00:00:00+00:00
draft: false
tags: ["GitHub", "Chainguard Containers", "Migration"]
images: []
menu:
  docs:
    parent: "guardener-github"
weight: 45
toc: true
---

Guardener reviews pull requests that add or change container image references and recommends the Chainguard container image that replaces each upstream image. Where it can, Guardener includes the replacement as a one-click suggested change.

{{< beta feature="Guardener" access="organizations that have installed and linked the Chainguard App" >}}

Guardener reads only the lines a pull request adds or changes, so it catches upstream images as they're introduced but doesn't review the images a repository already uses. To find replacements for every image in a repository, run [`chainctl images discover`](/chainguard/containers/migration/migration-tools/images-discover/).

## Prerequisites

Before you enable Image Suggestions, make sure that:

- The Chainguard App is installed and your GitHub organization is linked to your Chainguard organization, as described in [Getting started](/chainguard/guardener/github/getting-started/). The link is needed on public repositories too, because Guardener checks each replacement against your Chainguard organization. Without a link, the pull request check reports that container image recommendations are unavailable.
- To get Image Suggestions on private repositories, your organization's [repository visibility scope](/chainguard/guardener/github/app-connections/#repository-visibility-scope) is `ALL`. With the default `PUBLIC` scope, Guardener skips private repositories without leaving a comment or a check run.

## Enable Image Suggestions

Add a `.chainguard/images.yaml` file to your repository:

```yaml
enabled: true
```

The file turns the feature on. To opt one repository out of an [organization-level default](/chainguard/guardener/github/configuration/#organization-level-configuration-with-the-github-repository), set `enabled: false` in that repository's file.

Guardener reads `.chainguard/images.yaml` from the pull request's base branch, not from the pull request. A pull request that adds the file doesn't get Image Suggestions itself. Pull requests opened after it merges do.

## Choose FIPS or standard images

Images your organization already has rank ahead of images it doesn't. Within each group, Guardener ranks the FIPS variant first when Chainguard publishes one. To rank standard images first, set `prefer_fips: false`:

```yaml
enabled: true
prefer_fips: false
```

## What Guardener reviews

Guardener reads the files a pull request changes and keeps only the image references on added or changed lines.

| Files | What Guardener reads | Suggested change |
| --- | --- | --- |
| Dockerfiles: `Dockerfile`, `Dockerfile.*`, `*.dockerfile`, and `Containerfile` | Every `FROM` instruction, in every build stage | Yes |
| YAML and JSON, such as Kubernetes manifests, Compose files, and Helm values | Every `image` value, and Helm-style `image` mappings split into `registry`, `repository`, and `tag` keys | Yes |
| Terraform (`*.tf`, `*.tfvars`), shell scripts (`*.sh`), and Makefiles | Lines about an image, such as an `image` argument or a `docker run` command | No; reported only |

A few details apply to specific formats:

- In a Dockerfile, Guardener substitutes `ARG` defaults into `FROM` lines. It skips `FROM scratch`, `FROM` lines that name an earlier build stage, and references that depend on an `ARG` with no default.
- Helm values are read as written, not rendered. A reference computed inside a chart template isn't seen. An `image` mapping with an empty tag uses the chart's `appVersion`.
- Images used only in `COPY --from` or `RUN --mount` instructions aren't read.

Guardener skips files under `node_modules`, `vendor`, `.terraform`, and `testdata` directories.

## How Guardener responds

Guardener skips draft pull requests and reviews them once they're marked ready for review.

For each changed reference that has a Chainguard replacement, Guardener leaves a review comment naming the replacement it selected. Guardener ranks replacements the same way as `chainctl images discover` and recommends the first one.

The review is non-blocking. Guardener doesn't request changes, and its `actions-recommender-images` check run, which is separate from the Hardened Actions check, completes as successful or neutral, never as failed. The check run summarizes every changed reference, including the ones Guardener couldn't recommend a replacement for.

A comment includes a one-click suggested change when all of the following are true:

- The file is a Dockerfile, YAML file, or JSON file.
- The reference is one literal value on its own line. It isn't assembled from a Dockerfile `ARG` or a split Helm `image` mapping, and no other image shares the line.
- Your Chainguard organization already has the replacement image, with a matching tag.

Otherwise, the comment names the replacement so you can make the change yourself, or add the image to your organization first. Adding an image isn't always self-service: how you do it depends on your subscription, and the steps are in [The container isn't in your organization's catalog](/chainguard/containers/troubleshooting/container-version-troubleshooting/#the-container-isnt-in-your-organizations-catalog).

A suggested change swaps one image reference for another. Guardener doesn't restructure a Dockerfile: it doesn't rename packages, split a build into stages, or change the user or entry point. Review and test the change as you would any other. To convert a whole Dockerfile, use [Dockerfile migration](/chainguard/guardener/dockerfile-migration/).

## Limits

To keep reviews fast on large pull requests, Guardener stops reading at the following limits. Anything past a limit isn't reviewed, and the check run reports that the review stopped early.

| Limit | Value |
| --- | --- |
| Changed files read per pull request | 300 |
| Image references per pull request, counted once per file, line, and image | 100 |
| Image reference occurrences per pull request | 1,000 |

Guardener also skips any single file larger than 1 MiB, and the check run lists it under the files it couldn't analyze.

## Configuration reference

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `true` when the file exists | Turns Image Suggestions on or off for the repository. |
| `prefer_fips` | boolean | `true` | Ranks FIPS variants before standard variants. Images your organization already has still rank first. |

## Next steps

- **[`chainctl images discover`](/chainguard/containers/migration/migration-tools/images-discover/)** — Find replacements for every image a repository already uses.
- **[Configuration](/chainguard/guardener/github/configuration/)** — Set Image Suggestions once for your whole organization.
- **[Dockerfile migration](/chainguard/guardener/dockerfile-migration/)** — Convert a Dockerfile to use Chainguard container images.
