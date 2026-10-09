---
title: "Guardener on GitHub"
linktitle: "GitHub App"
description: "Guardener secures and maintains your repositories through the Chainguard App, with capabilities you enable per repository with .chainguard/ configuration files."
type: "article"
date: 2026-07-13T00:00:00+00:00
lastmod: 2026-10-08T02:59:03+00:00
draft: false
tags: ["GitHub"]
images: []
menu:
  docs:
    parent: "guardener"
weight: 10
toc: true
---

Guardener's GitHub capabilities run through the **Chainguard App**, a single hardened GitHub App that also backs other Chainguard products. Those capabilities are opt-in per repository through configuration files committed to a `.chainguard/` directory, so installing the app has no effect on a repository until you enable a capability.

{{< beta feature="Guardener" access="organizations that have installed and linked the Chainguard App" >}}

## Getting set up

- **[Getting started](/chainguard/guardener/github/getting-started/)** — Install the Chainguard App and link your Chainguard organization to your GitHub organization.
- **[App connections](/chainguard/guardener/github/app-connections/)** — Set up, inspect, and remove the connections between your Chainguard organization and your GitHub organizations.
- **[Configuration](/chainguard/guardener/github/configuration/)** — Understand the `.chainguard/` configuration model that all of Guardener's GitHub capabilities share.

## Capabilities

- **[Hardened Actions](/chainguard/guardener/github/actions-security/)** — Recommends and migrates your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents, through non-blocking pull request review comments or automated migration pull requests. Migration pull requests run on a schedule and can also be [triggered on demand](/chainguard/guardener/github/actions-security/#run-an-on-demand-migration) with `chainctl`.
- **[Container Image Suggestions](/chainguard/guardener/github/image-suggestions/)** — Recommends Chainguard container images for the container images a pull request adds or changes, through non-blocking review comments with one-click suggested changes where possible.
- **[Container Image Migration](/chainguard/guardener/github/image-migration/)** — Replaces the container images a repository already uses with Chainguard container images through a migration pull request. Migration runs on a schedule and can also be [triggered on demand](/chainguard/guardener/github/image-migration/#run-an-on-demand-migration) with `chainctl`.
- **[Commit Verification](/chainguard/guardener/github/commit-verification/)** — Enforces cryptographically signed commits against a policy you control, supporting both keyless (Sigstore) signatures and static keys such as GPG.

Each capability is configured with its own file in the `.chainguard/` directory.

> **Note:** For Dockerfile migration, which runs locally through `chainctl agent dockerfile` rather than the Chainguard App, refer to [Dockerfile migration](/chainguard/guardener/dockerfile-migration/).
