---
title: "Chainguard Guardener Hardened Actions"
linktitle: "Hardened Actions"
description: "Configure Chainguard Guardener to recommend and migrate your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-08-10T00:00:00+00:00
draft: false
tags: ["GitHub", "Automation"]
images: []
menu:
  docs:
    parent: "guardener-github"
weight: 030
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

With just `enabled: true`, the Guardener posts non-blocking recommendation comments on pull requests that touch your workflows. It does not open pull requests of its own.

## Enable automated migration pull requests

To have the Guardener periodically open and maintain a pull request that migrates your workflows, enable the `migrate` block:

```yaml
enabled: true
migrate:
  enabled: true
  period: "168h"
```

The Guardener opens (and keeps updated) a single migration pull request on the cadence you set with `period`.

## Run an on-demand migration

Instead of waiting for the next scheduled run — for example, right after enabling migration, or after Chainguard publishes a hardened equivalent for an action you use — you can trigger the migration immediately with `chainctl`.

An on-demand run performs exactly the same migration as the scheduled flow: it opens (or updates) the repository's single migration pull request and honors the same `.chainguard/actions.yaml` configuration, including `migrate.ignore`. Because it shares the opt-in gate, the repository (or its organization, through the [org-level `.github` configuration](/chainguard/guardener/github/configuration/)) must have `migrate.enabled: true`; if migration is not enabled, the run completes as a no-op without opening a pull request. Triggering an on-demand run does not change the periodic schedule.

Before you start, make sure that:

- The Guardener GitHub App is installed and your Chainguard organization is linked to your GitHub organization, as described in [Getting started](/chainguard/guardener/github/getting-started/). The migration must be requested through the Chainguard organization that owns the GitHub App installation.
- You hold the `guardener.actions.migrate` capability on that Chainguard organization. Organization owners have it, and it is included in the built-in `guardener.user` and `guardener.admin` roles. Refer to the [Built-in roles and capabilities reference](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/) for more information on roles.

Run `chainctl guardener github migrate create` with the repository to migrate:

```shell
chainctl guardener github migrate create <owner>/<repo> \
  --parent <group-name>
```

The repository can be given as `owner/repo` shorthand or as a full URL (`https://github.com/owner/repo`); only github.com repositories are supported today. `--parent` is the Chainguard organization that owns the GitHub App installation — if you omit it, `chainctl` prompts you to select one.

By default the command waits for the migration to finish (up to 10 minutes, adjustable with `--timeout`) and prints the result:

```
Repository: https://github.com/<owner>/<repo>
Triggered by: you@example.com (user)
Status: completed
Pull request: https://github.com/<owner>/<repo>/pull/42
```

When there is nothing to migrate — every action is already on a Chainguard equivalent, the ignore rules exclude everything, or the repository has not enabled migration — the run reports `Status: completed (no changes needed)` instead of a pull request.

If the migration fails because the GitHub App installation does not cover the repository (for example, the app was installed on **selected repositories** and this one isn't included), the error says so; grant the app access to the repository in your GitHub organization settings and trigger the migration again.

## Check a migration operation

Pass `--wait=false` to return immediately instead of waiting. The command prints an operation name of the form `operations/migrate/<group>/<id>`, which you can check later with `chainctl guardener github migrate get`:

```shell
chainctl guardener github migrate get operations/migrate/<group>/<id>
```

The owning organization is derived from the operation name, so no `--parent` is needed. Add `--wait` to poll until the operation completes (bounded by `--timeout`, 10 minutes by default). Interrupting a waiting `migrate create` is also safe — the migration keeps running server-side, and the command prints the operation name so you can check it later.

For the complete set of flags and options, refer to the `chainctl` reference:

- [`chainctl guardener github migrate`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github_migrate/)
- [`chainctl guardener github migrate create`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github_migrate_create/)
- [`chainctl guardener github migrate get`](/chainguard/chainctl/chainctl-docs/chainctl_guardener_github_migrate_get/)

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
