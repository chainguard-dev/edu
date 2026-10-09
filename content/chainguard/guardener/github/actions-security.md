---
title: "Guardener Hardened Actions"
linktitle: "Hardened Actions"
description: "Configure Guardener to recommend and migrate your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-10-08T02:59:03+00:00
draft: false
tags: ["GitHub", "Automation"]
images: []
menu:
  docs:
    parent: "guardener-github"
weight: 40
toc: true
---

The Hardened Actions feature recommends and migrates your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents. Pinning actions to a specific commit SHA — rather than a mutable tag or branch — protects your workflows from supply chain attacks in which an upstream tag is moved to point at malicious code.

Hardened Actions operates in two independent modes:

- **Pull request recommendations** — non-blocking review comments that suggest hardened action alternatives, with one-click suggestion blocks.
- **Automated migration pull requests** — a periodically maintained pull request that updates workflows across your repository. You can also [trigger this migration on demand](#run-an-on-demand-migration) with `chainctl` instead of waiting for the next scheduled run.

You can enable either mode on its own or both together.

## Enable Hardened Actions

Add a `.chainguard/actions.yaml` file to your repository:

```yaml
enabled: true
```

With just `enabled: true`, Guardener posts non-blocking recommendation comments on pull requests that touch your workflows. It does not open pull requests of its own.

## Enable automated migration pull requests

To have Guardener periodically open and maintain a pull request that migrates your workflows, enable the `migrate` block:

```yaml
enabled: true
migrate:
  enabled: true
  period: "168h"
```

Guardener opens (and keeps updated) a single migration pull request on the cadence you set with `period`.

## Run an on-demand migration

Instead of waiting for the next scheduled run — for example, right after enabling migration, or after Chainguard publishes a hardened equivalent for an action you use — you can trigger the migration immediately with `chainctl`.

An on-demand run performs exactly the same migration as the scheduled flow: it opens (or updates) the repository's single migration pull request and honors the same `.chainguard/actions.yaml` configuration, including `migrate.ignore`. Because it shares the opt-in gate, the repository (or its organization, through the [org-level `.github` configuration](/chainguard/guardener/github/configuration/)) must have `migrate.enabled: true`; if migration is not enabled, the run completes as a no-op without opening a pull request. Triggering an on-demand run does not change the periodic schedule.

Before you start, make sure that:

- The Chainguard App is installed and your Chainguard organization is linked to your GitHub organization, as described in [Getting started](/chainguard/guardener/github/getting-started/). The migration must be requested through the Chainguard organization that owns the Chainguard App installation.
- You hold the `guardener.actions.migrate` capability on that Chainguard organization. The built-in `viewer`, `editor`, and `owner` roles include it, as do `guardener.user` and `guardener.admin`. Each built-in role that includes either migration capability includes both. Refer to the [Built-in roles and capabilities reference](/platform/administration/iam-organizations/roles-role-bindings/capabilities-reference/) for more information on roles.

Run `chainctl guardener github migrate create` with the repository to migrate:

```shell
chainctl guardener github migrate create <owner>/<repo>
```

The repository can be given as `owner/repo` shorthand or as a full URL (`https://github.com/owner/repo`); only github.com repositories are supported today. The migration runs under the Chainguard organization that owns the Chainguard App installation. `chainctl` selects that organization automatically when only one is available and prompts you when there are several; pass `--parent <group-name>` to name it explicitly.

With `chainctl` 0.2.375 or later, the command runs every migration that the repository opts in to, so it also opens or updates the [Container Image Migration](/chainguard/guardener/github/image-migration/) pull request when `.chainguard/images.yaml` enables it. Earlier versions of `chainctl` run only the Hardened Actions migration.

Each migration checks its own capability. If you hold `guardener.actions.migrate` but not `guardener.images.migrate`, the `Images:` line reports a permission error and the command exits with an error, even when the repository doesn't use image migration.

By default, the command waits for the migrations to finish (up to 10 minutes, adjustable with `--timeout`) and prints one result for each:

```
Repository: https://github.com/<owner>/<repo>
Triggered by: you@example.com (user)
Actions: https://github.com/<owner>/<repo>/pull/42
Images: migration is not enabled here or in repository configuration
Status: completed
```

In this example, the repository opts in to Hardened Actions migration only. When there's nothing to migrate — every action is already on a Chainguard equivalent, or the ignore rules exclude everything — the `Actions:` line reads `no changes needed` instead of a pull request URL. When the repository hasn't enabled Hardened Actions migration, it reads `migration is not enabled here or in repository configuration`. If a migration fails, its line reads `failed` with the reason, the last line reads `Status: completed with failures`, and the command exits with an error.

If the migration fails because the Chainguard App installation does not cover the repository (for example, the app was installed on **selected repositories** and this one isn't included), the error says so; grant the app access to the repository in your GitHub organization settings and trigger the migration again.

## Check a migration operation

Pass `--wait=false` to return immediately instead of waiting. The command prints an operation name of the form `operations/migrate/<group>/<id>`, which you can check later with `chainctl guardener github migrate get`:

```shell
chainctl guardener github migrate get operations/migrate/<group>/<id>
```

The owning organization is derived from the operation name, so no `--parent` is needed. Add `--wait` to poll until the operation completes (bounded by `--timeout`, 10 minutes by default). Interrupting a waiting `migrate create` is also safe — the migration keeps running server-side, and the command prints the operation name so you can check it later.

For the complete set of flags and options, refer to the `chainctl` reference:

- [`chainctl guardener github migrate`](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate/)
- [`chainctl guardener github migrate create`](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate_create/)
- [`chainctl guardener github migrate get`](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate_get/)

## Exclude files and actions

Use the `migrate.ignore` block to exclude specific workflow files or upstream actions from automated migration. Both fields accept glob patterns:

```yaml
enabled: true
migrate:
  enabled: true
  period: "168h"
  ignore:
    files:
      - "release.yml"
      - "*.deprecated.yml"
    actions:
      - "actions/checkout"
      - "actions/*"
```

- `ignore.files` — workflow files (under `.github/workflows/`) to skip.
- `ignore.actions` — upstream actions to leave untouched.

## Configuration reference

| Field                    | Default | Purpose                                                                             |
| ------------------------ | ------- | ----------------------------------------------------------------------------------- |
| `enabled`                | `true`  | Enables inline pull request recommendation comments.                                |
| `migrate.enabled`        | `false` | Opts into automated migration pull requests.                                        |
| `migrate.period`         | `24h`   | How often the migration pull request is refreshed. Clamped to a minimum of one day. |
| `migrate.version-strategy` | `exact` | Version selection when no exact equivalent exists. Set to `smallest-major-bump` to migrate older pins to the closest Chainguard-supplied major version. |
| `migrate.ignore.files`   | —       | Glob patterns for workflow files to skip during migration.                          |
| `migrate.ignore.actions` | —       | Glob patterns for upstream actions to skip during migration.                        |

The `period` value is a Go-style duration string (for example, `24h`, `168h` for one week).

## Full example

A complete `.chainguard/actions.yaml` enabling both recommendations and weekly automated migration, while leaving the `actions/*` family and a release workflow untouched:

```yaml
enabled: true
migrate:
  enabled: true
  period: "168h"
  ignore:
    files:
      - "release.yml"
    actions:
      - "actions/*"
```

## Next steps

- **[Commit Verification](/chainguard/guardener/github/commit-verification/)** — Require cryptographically signed commits in pull requests.
- **[Configuration](/chainguard/guardener/github/configuration/)** — Review the shared `.chainguard/` configuration model.
