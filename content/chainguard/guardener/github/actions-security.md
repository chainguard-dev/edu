---
title: "Chainguard Guardener Hardened Actions"
linktitle: "Hardened Actions"
description: "Configure Chainguard Guardener to recommend and migrate your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-07-08T00:00:00+00:00
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
- **Automated migration pull requests** — a periodically maintained pull request that updates workflows across your repository.

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
- **[Configuration](/chainguard/guardener/configuration/)** — Review the shared `.chainguard/` configuration model.
