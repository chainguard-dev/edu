---
title: "Guardener Container Image Migration"
linktitle: "Container Image Migration"
description: "Configure Guardener to open a pull request that replaces the container images a repository already uses with Chainguard container images."
type: "article"
date: 2026-10-08T02:59:03+00:00
lastmod: 2026-10-08T02:59:03+00:00
draft: false
tags: ["GitHub", "Chainguard Containers", "Migration"]
images: []
menu:
  docs:
    parent: "guardener-github"
weight: 48
toc: true
---

Guardener scans the default branch of a repository for container image references and opens a pull request that replaces them with Chainguard container images your organization already has. As your repository and your organization's images change, Guardener keeps that pull request up to date.

{{< beta feature="Guardener" access="organizations that have installed and linked the Chainguard App" >}}

Container Image Migration and [Container Image Suggestions](/chainguard/guardener/github/image-suggestions/) work together. Image Suggestions reviews the images that each new pull request adds, and migration replaces the images the repository already uses. Each has its own setting in `.chainguard/images.yaml`, so you can use either one or both.

A migration pull request changes image references only. Guardener doesn't build your images, run your tests, or convert your Dockerfiles, so review and test the pull request as you would any other change.

## Prerequisites

Before you enable Container Image Migration, make sure that:

- The Chainguard App is installed with access to the repository, and your GitHub organization is linked to your Chainguard organization, as described in [Getting started](/chainguard/guardener/github/getting-started/). You don't need to change the [repository visibility scope](/chainguard/guardener/github/app-connections/#repository-visibility-scope): unlike Image Suggestions, migration runs on private repositories even with the default `PUBLIC` scope.
- Your Chainguard organization has the replacement images. Guardener doesn't add images for you. Adding an image isn't always self-service: how you do it depends on your subscription, and the steps are in [The container isn't in your organization's catalog](/chainguard/containers/troubleshooting/container-version-troubleshooting/#the-container-isnt-in-your-organizations-catalog).

## Enable Container Image Migration

Add a `migrate` block to the repository's `.chainguard/images.yaml` file, and set `enabled` inside it to `true`:

```yaml
enabled: true
migrate:
  enabled: true
```

The top-level `enabled` key controls Image Suggestions, and the `migrate.enabled` key controls migration. Image Suggestions is on whenever the file exists. To get only migration pull requests, set the top-level `enabled` to `false`:

```yaml
enabled: false
migrate:
  enabled: true
```

Commit the file to the repository's default branch. Guardener reads `.chainguard/images.yaml` only from the default branch, and the push that adds or changes the file starts the first migration.

To set migration once for every repository in your organization, commit the file to your organization's `.github` repository instead, as described in [Configuration](/chainguard/guardener/github/configuration/#organization-level-configuration-with-the-github-repository). A repository's own `.chainguard/images.yaml` replaces the organization file entirely, so a repository file without a `migrate` block turns migration off for that repository.

## When migration runs

Guardener runs a migration for a repository at the following times:

- After a push to the default branch that adds, changes, or removes `.chainguard/images.yaml` in that repository.
- On a schedule, about once every `migrate.period`. The default and minimum period is 24 hours.
- On demand, when you run `chainctl guardener github migrate create`, as described in [Run an on-demand migration](#run-an-on-demand-migration).

Each run scans the whole default branch again. A scheduled run therefore picks up images that your organization added since the last run, as well as new image references in the repository. Changes to the organization-level file in your `.github` repository take effect at each repository's next scheduled run.

## Review the migration pull request

Guardener keeps one image migration pull request per repository, separate from the [Hardened Actions](/chainguard/guardener/github/actions-security/) migration pull request. The pull request is titled **Migrate container images to Chainguard equivalents**, and its description lists the following:

- **Changed files**: every file that the pull request edits.
- **Not migrated**: each reference that Guardener found and left unchanged, with the reason.

Each run plans its changes against the latest commit on the default branch. If the migration pull request is open, Guardener updates it only when the planned changes differ from the ones it already has. After you merge or close the pull request, the next run opens a new one if there's anything left to change. Guardener never merges the pull request itself.

Closing the pull request doesn't turn migration off. To stop migration for a repository, set `migrate.enabled: false`.

To make your own changes to the pull request, add the `skip:guardener/images` label or assign the pull request to someone first. Guardener then stops updating it. Don't push to the pull request's branch, under `guardener/images/`, without first adding the label or an assignee, because Guardener force-pushes the branch on each update.

When nothing is left to change, Guardener doesn't open a pull request, and it doesn't close one that's already open. If you make the same changes yourself, close the open migration pull request.

## What migration changes

Migration reads Dockerfiles, YAML files, and JSON files across the whole repository. It skips files under `node_modules`, `vendor`, `.terraform`, and `testdata` directories.

| Files | What Guardener changes |
| --- | --- |
| Dockerfiles: `Dockerfile`, `Dockerfile.*`, `*.dockerfile`, and `Containerfile` | The image in each `FROM` instruction, in every build stage. |
| YAML and JSON, such as Kubernetes manifests, Compose files, and Helm values | Each literal `image` value. Guardener doesn't read Helm chart templates. |
| Terraform (`*.tf`, `*.tfvars`), shell scripts (`*.sh`), and Makefiles | Nothing. Guardener doesn't read these files. To find the images they use, run [`chainctl images discover`](/chainguard/containers/migration/migration-tools/images-discover/). |

Guardener chooses each replacement the same way as Image Suggestions. When Chainguard publishes a Federal Information Processing Standards (FIPS) variant of an image, Guardener prefers it unless you set `prefer_fips: false`. Guardener keeps the reference's tag when Chainguard maintains it. Otherwise, it uses the newest maintained version on the same minor version line or, failing that, in the same major version. If the version changes, check its release notes before you merge. When a reference has both a tag and a digest, the replacement is also pinned by digest.

Guardener leaves a reference unchanged and lists it under **Not migrated** in the following cases:

- Your Chainguard organization doesn't have the replacement image, or doesn't have a matching tag. After you add the image, the next run migrates the reference.
- Chainguard doesn't publish an equivalent image.
- The reference isn't one literal value on its own line. For example, it's assembled from a Dockerfile `ARG`, it's split across Helm `registry`, `repository`, and `tag` keys, or another image shares its line.
- The Dockerfile build stage, or a stage built on it, runs commands with `RUN`, a shell-form `CMD` or `ENTRYPOINT`, or an `ONBUILD` instruction. Chainguard container images without a `-dev` suffix usually have no shell or package manager, so swapping only the image could break the build. To convert the whole Dockerfile, use [Dockerfile migration](/chainguard/guardener/dockerfile-migration/).
- The Dockerfile build stage sets `CMD` without `ENTRYPOINT`. Many Chainguard container images set `ENTRYPOINT` to their runtime, so the command could change.
- The reference has a tag that Chainguard doesn't maintain, and no maintained version is close enough to replace it, so the only replacement would be the `latest` tag.
- The reference is pinned by digest without a tag, so there's no version to carry over.

## Exclude files and images

To keep Guardener from changing specific files or images, add a `migrate.ignore` block:

```yaml
migrate:
  enabled: true
  ignore:
    files:
      - "Dockerfile.dev"
      - "examples/*"
    images:
      - "busybox:*"
```

Both lists take glob patterns. A `*` matches any characters except `/`, and `**` doesn't match across directories.

- `ignore.files` matches a file's path from the repository root, or its file name. In this example, `examples/*` matches `examples/Dockerfile` but not `examples/app/Dockerfile`.
- `ignore.images` matches the image reference as written in the file, with Dockerfile `ARG` defaults filled in. In this example, `busybox:*` matches `busybox:1.36`, but it doesn't match `docker.io/library/busybox:1.36` or `busybox` with no tag.

Ignored files and images don't appear in the migration pull request.

## Run an on-demand migration

Rather than waiting for the next scheduled run, you can start a migration right away with `chainctl`. For example, you might do this after you add an image to your organization. An on-demand run performs the same migration as a scheduled run and uses the same configuration. It doesn't change the schedule.

Before you start, make sure that:

- You have `chainctl` 0.2.375 or later. Earlier versions migrate only GitHub Actions. To update, run `chainctl update`.
- The repository has `migrate.enabled: true` in its own `.chainguard/images.yaml` file or in the organization-level file.
- You hold the `guardener.images.migrate` capability on the Chainguard organization that's linked to the repository's GitHub organization. The built-in `viewer`, `editor`, and `owner` roles include it, as do `guardener.user` and `guardener.admin`. For more information, refer to the [Built-in roles and capabilities reference](/platform/administration/iam-organizations/roles-role-bindings/capabilities-reference/).

Run `chainctl guardener github migrate create` with the repository:

```shell
chainctl guardener github migrate create <owner>/<repo>
```

The command runs every migration that the repository opts in to: Container Image Migration through `.chainguard/images.yaml` and Hardened Actions migration through `.chainguard/actions.yaml`. Each opens or updates its own pull request.

By default, the command waits up to 10 minutes for the migrations to finish and then prints one result for each:

```
Repository: https://github.com/<owner>/<repo>
Triggered by: you@example.com (user)
Actions: migration is not enabled here or in repository configuration
Images: https://github.com/<owner>/<repo>/pull/43
Status: completed
```

In this example, the repository opts in to Container Image Migration only. The `Images:` line reports one of the following results:

| Result | Meaning |
| --- | --- |
| A pull request URL | Guardener opened or updated the migration pull request. |
| `no changes needed` | Guardener found nothing it could change. This includes references whose replacement your organization doesn't have yet. To see the replacement for every reference, run [`chainctl images discover`](/chainguard/containers/migration/migration-tools/images-discover/). |
| `migration is not enabled here or in repository configuration` | The repository doesn't have `migrate.enabled: true`. |
| `failed` | Guardener couldn't finish the migration. The message in parentheses says why, such as a missing capability or a [scan limit](#limits). |

When any migration fails, the last line reads `Status: completed with failures`, and the command exits with an error. To return without waiting, or to check a migration later, refer to [Check a migration operation](/chainguard/guardener/github/actions-security/#check-a-migration-operation).

## Limits

Because migration reads the whole repository, it has the following limits. When a repository exceeds one, Guardener doesn't open or update the migration pull request, and an on-demand run reports `Images: failed` with the limit it reached. To bring the repository under the limit, exclude directories or files with [`migrate.ignore.files`](#exclude-files-and-images).

| Limit | Value |
| --- | --- |
| Image references, counted once per file, line, and image | 100 |
| Image reference occurrences | 1,000 |
| Files in Helm chart `templates` directories, which Guardener checks so it can skip them | 300 |
| Total size of the files read | 128 MiB |

Guardener also skips any file larger than 1 MiB and lists it under **Not migrated**.

## Configuration reference

The following keys in `.chainguard/images.yaml` control migration:

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `migrate.enabled` | boolean | `false` | Turns migration pull requests on for the repository. |
| `migrate.period` | duration | `24h` | How often Guardener runs a scheduled migration, written as a Go duration such as `168h` for one week. A period shorter than 24 hours, or a value that isn't a duration, uses 24 hours. |
| `migrate.ignore.files` | list of glob patterns | None | Files that migration doesn't read. |
| `migrate.ignore.images` | list of glob patterns | None | Image references that migration leaves unchanged. |
| `prefer_fips` | boolean | `true` | Ranks FIPS variants before standard variants, for both migration and Image Suggestions. |

The top-level `enabled` key controls Image Suggestions only. For more information, refer to the [Image Suggestions configuration reference](/chainguard/guardener/github/image-suggestions/#configuration-reference).

## Full example

The following `.chainguard/images.yaml` file turns on Image Suggestions and weekly migration pull requests. It prefers standard images to FIPS variants, and it leaves a development Dockerfile and every `busybox:<tag>` reference unchanged:

```yaml
enabled: true
prefer_fips: false
migrate:
  enabled: true
  period: "168h"
  ignore:
    files:
      - "Dockerfile.dev"
    images:
      - "busybox:*"
```

Commit the file to the repository's default branch. The push that adds or changes it starts a migration.

## Next steps

- **[Container Image Suggestions](/chainguard/guardener/github/image-suggestions/)** — Get suggestions on the images each new pull request adds.
- **[`chainctl images discover`](/chainguard/containers/migration/migration-tools/images-discover/)** — Find replacements for every image a repository uses, including the ones migration can't change.
- **[Dockerfile migration](/chainguard/guardener/dockerfile-migration/)** — Convert a whole Dockerfile to use Chainguard container images.
