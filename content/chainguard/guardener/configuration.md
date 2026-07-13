---
title: "Configuring Chainguard Guardener"
linktitle: "Configuration"
description: "Understand Chainguard Guardener's .chainguard/ configuration model and how to enable features per repository."
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

Chainguard Guardener is configured entirely through files committed to a `.chainguard/` directory — either in each repository, or once at the organization level in your `.github` repository. This page explains the configuration model that all the Guardener features share. For the specific options of each feature, see its dedicated page.

## The `.chainguard/` directory

The Guardener reads its configuration from the `.chainguard/` directory at the root of each repository. Every feature has its own file:

```text
.chainguard/
├── actions.yaml   # Actions Security
└── source.yaml    # Commit Verification
```

Because these files live in your repository, your configuration is reviewed through pull requests, versioned in git history, and audited like any other code change.

## Features are opt-in per repository

Installing the Guardener GitHub App does not change any repository on its own. Each feature stays disabled until you add its configuration file and enable it. This means you can:

- Roll a feature out to one repository at a time.
- Try a feature in report-only or non-blocking mode before enforcing it.
- Keep different repositories on different configurations.

A repository with no `.chainguard/` files is unaffected by the Guardener even when the app is installed and the organization is linked.

## Available features

| Feature                                                           | Config file                | What it does                                                                |
| ----------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------- |
| [Actions Security](/chainguard/guardener/actions-security/)       | `.chainguard/actions.yaml` | Recommends and migrates GitHub Actions to hardened, SHA-pinned equivalents. |
| [Commit Verification](/chainguard/guardener/commit-verification/) | `.chainguard/source.yaml`  | Verifies that commits in a pull request are signed by an authorized signer. |

Additional features will be added over time, each with its own `.chainguard/` file and opt-in configuration.

## Organization-level configuration with the `.github` repository

Rather than committing `.chainguard/` files to every repository, you can define configuration once at the organization level. The Guardener reads a `.chainguard/` directory from your organization's `.github` repository and applies it as the default for every repository in the organization.

The `.github` repository is a special repository that GitHub already uses for organization-wide defaults (such as community health files and default workflows). The Guardener follows the same convention:

```text
.github/                # your organization's .github repository
└── .chainguard/
    ├── actions.yaml     # org-wide default for Actions Security
    └── source.yaml      # org-wide default for Commit Verification
```

To use org-level configuration:

1. Create a repository named `.github` in your organization if you don't already have one.
2. Add the Guardener GitHub App to the `.github` repository (or install it on **All repositories**).
3. Commit your `.chainguard/` configuration files to the default branch of the `.github` repository.

Once in place, every repository the Guardener can access inherits this configuration without needing its own `.chainguard/` files.

### How repository and organization configuration combine

Configuration committed directly to a repository takes precedence over the organization-level configuration from the `.github` repository:

- A repository with its own `.chainguard/<feature>.yaml` file uses that file for the feature, ignoring the org-level default for it.
- A repository without a given feature file falls back to the org-level default in the `.github` repository.
- A feature that is configured in neither place stays disabled for the repository.

This lets you set a baseline for the whole organization and override it only where a specific repository needs different behavior.

> **Note:** The Guardener reads the org-level configuration from the default branch (that is, `main`) of the `.github` repository, just as it does for per-repository configuration.

## Applying configuration changes

To add or update the Guardener configuration:

1. Create or edit the relevant file in `.chainguard/` on a branch.
2. Open a pull request with your change.
3. Merge the pull request. The Guardener picks up the new configuration for subsequent events.

> **Note:** The Guardener uses the repo's default branch (that is, `main`) for its configuration.

## Next steps

- **[Actions Security](/chainguard/guardener/actions-security/)** — Configure `.chainguard/actions.yaml`.
- **[Commit Verification](/chainguard/guardener/commit-verification/)** — Configure `.chainguard/source.yaml`.
