---
title: "Chainguard Guardener GitHub App"
linktitle: "GitHub App"
description: "The Chainguard Guardener GitHub App secures and maintains your repositories through capabilities you enable per repository with .chainguard/ configuration files."
type: "article"
date: 2026-07-13T00:00:00+00:00
lastmod: 2026-07-13T00:00:00+00:00
draft: false
tags: ["GitHub"]
images: []
menu:
  docs:
    parent: "guardener"
weight: 030
toc: true
---

The Chainguard Guardener GitHub App is a single, hardened bot that runs against your repositories. Its capabilities are opt-in per repository through configuration files committed to a `.chainguard/` directory, so installing the app has no effect on a repository until you enable a capability.

{{< beta feature="Chainguard Guardener" access="organizations that have installed and linked the Chainguard Guardener GitHub App" >}}

## Getting set up

- **[Getting started](/chainguard/guardener/github/getting-started/)** — Install the GitHub App and link your Chainguard organization to your GitHub organization.
- **[Configuration](/chainguard/guardener/github/configuration/)** — Understand the `.chainguard/` configuration model that all the GitHub App capabilities share.

## Capabilities

- **[Hardened Actions](/chainguard/guardener/github/actions-security/)** — Recommends and migrates your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents, either through non-blocking pull request review comments or automated migration pull requests.
- **[Commit Verification](/chainguard/guardener/github/commit-verification/)** — Enforces cryptographically signed commits against a policy you control, supporting both keyless (Sigstore) signatures and static keys such as GPG.

Each capability is configured with its own file in the `.chainguard/` directory.

> **Note:** For Dockerfile migration, which runs locally through `chainctl agent dockerfile` rather than the GitHub App, see [Dockerfile migration](/chainguard/guardener/dockerfile-migration/).
