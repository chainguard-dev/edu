---
title: "Configuring The Guardener"
linktitle: "Configuration"
description: "Understand The Guardener's .chainguard/ configuration model and how to enable features per repository."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-07-08T00:00:00+00:00
draft: false
tags: ["GitHub", "Configuration"]
images: []
menu:
  docs:
    parent: "guardener"
weight: 020
toc: true
---

The Guardener is configured entirely through files committed to the `.chainguard/` directory in each repository. This page explains the configuration model that all The Guardener features share. For the specific options of each feature, see its dedicated page.

## The `.chainguard/` directory

The Guardener reads its configuration from the `.chainguard/` directory at the root of each repository. Every feature has its own file:

```text
.chainguard/
├── actions.yaml   # Actions Security
└── source.yaml    # Commit Verification
```

Because these files live in your repository, your configuration is reviewed through pull requests, versioned in git history, and audited like any other code change.

## Features are opt-in per repository

Installing The Guardener GitHub App does not change any repository on its own. Each feature stays disabled until you add its configuration file and enable it. This means you can:

- Roll a feature out to one repository at a time.
- Try a feature in report-only or non-blocking mode before enforcing it.
- Keep different repositories on different configurations.

A repository with no `.chainguard/` files is unaffected by The Guardener even when the app is installed and the organization is linked.

## Available features

| Feature                                                           | Config file                | What it does                                                                |
| ----------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------- |
| [Actions Security](/chainguard/guardener/actions-security/)       | `.chainguard/actions.yaml` | Recommends and migrates GitHub Actions to hardened, SHA-pinned equivalents. |
| [Commit Verification](/chainguard/guardener/commit-verification/) | `.chainguard/source.yaml`  | Verifies that commits in a pull request are signed by an authorized signer. |

Additional features will be added over time, each with its own `.chainguard/` file and opt-in configuration.

## Applying configuration changes

To add or update The Guardener configuration:

1. Create or edit the relevant file in `.chainguard/` on a branch.
2. Open a pull request with your change.
3. Merge the pull request. The Guardener picks up the new configuration for subsequent events.

> **Note:** The Guardener uses the repo's default branch (that is, `main`) for its configuration.

## Next steps

- **[Actions Security](/chainguard/guardener/actions-security/)** — Configure `.chainguard/actions.yaml`.
- **[Commit Verification](/chainguard/guardener/commit-verification/)** — Configure `.chainguard/source.yaml`.
