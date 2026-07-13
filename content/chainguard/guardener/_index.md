---
title: "Chainguard Guardener"
linktitle: "Chainguard Guardener"
description: "Chainguard Guardener is a tool for managing and hardening your source code, with a growing suite of capabilities you opt into independently."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-07-08T00:00:00+00:00
draft: false
images: []
weight: 025
---

Chainguard Guardener is a tool for managing and hardening your source code. Rather than adding a separate integration for every task, the Guardener provides a growing suite of capabilities that you opt into independently. Some capabilities run through a hardened GitHub App and are configured per repository through files committed to your codebase; others, such as Dockerfile migration, run locally through `chainctl`.

{{< beta feature="Chainguard Guardener" access="organizations that have installed and linked the Chainguard Guardener GitHub App" >}}

The Guardener's capabilities fall into two groups:

- **[GitHub App](/chainguard/guardener/github/)** — Capabilities that run through the Guardener GitHub App and are enabled per repository with `.chainguard/` configuration files:
  - **[Hardened Actions](/chainguard/guardener/github/actions-security/)** — Recommends and migrates your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents, either through non-blocking pull request review comments or automated migration pull requests.
  - **[Commit Verification](/chainguard/guardener/github/commit-verification/)** — Enforces cryptographically signed commits against a policy you control, supporting both keyless (Sigstore) signatures and static keys such as GPG.
- **[Dockerfile migration](/chainguard/guardener/dockerfile-migration/)** — Uses AI to iteratively convert your Dockerfiles to Chainguard Containers. This capability runs locally through `chainctl agent dockerfile` commands.

Additional capabilities will be added over time, each with its own opt-in configuration.

## Where to start

- **[GitHub App](/chainguard/guardener/github/)** — Install the app, link your organization, and configure the GitHub App capabilities (Hardened Actions and Commit Verification):
  - **[Getting started](/chainguard/guardener/github/getting-started/)** — Install the GitHub App and link your Chainguard organization to your GitHub organization.
  - **[Configuration](/chainguard/guardener/github/configuration/)** — Understand the `.chainguard/` configuration model and how features are enabled per repository.
- **[Dockerfile migration](/chainguard/guardener/dockerfile-migration/)** — Migrate your Dockerfiles to Chainguard Containers using the `chainctl agent dockerfile` commands.

## Support

For questions or feedback, contact your Chainguard account team or email [support@chainguard.dev](mailto:support@chainguard.dev).
