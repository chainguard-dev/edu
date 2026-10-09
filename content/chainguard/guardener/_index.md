---
title: "Guardener"
linktitle: "Guardener"
description: "Guardener is a tool for managing and hardening your source code, with a growing suite of capabilities you opt into independently."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-10-08T02:59:03+00:00
draft: false
images: []
weight: 30
---

Guardener is a tool for managing and hardening your source code. Rather than adding a separate integration for every task, Guardener provides a growing suite of capabilities that you opt into independently. Some capabilities run through the Chainguard App, a hardened GitHub App, and are configured per repository through files committed to your codebase; others, such as Dockerfile migration, run locally through `chainctl`.

{{< beta feature="Guardener" access="organizations that have installed and linked the Chainguard App" >}}

Guardener's capabilities fall into two groups:

- **[GitHub App](/chainguard/guardener/github/)** — Capabilities that run through the Chainguard App and are enabled per repository with `.chainguard/` configuration files:
    - **[Hardened Actions](/chainguard/guardener/github/actions-security/)** — Recommends and migrates your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents, through non-blocking pull request review comments or migration pull requests that run on a schedule or [on demand](/chainguard/guardener/github/actions-security/#run-an-on-demand-migration).
    - **[Container Image Suggestions](/chainguard/guardener/github/image-suggestions/)** — Recommends Chainguard container images for the container images a pull request adds or changes, through non-blocking review comments with one-click suggested changes where possible.
    - **[Container Image Migration](/chainguard/guardener/github/image-migration/)** — Replaces the container images a repository already uses with Chainguard container images through a migration pull request that Guardener opens on a schedule or on demand.
    - **[Commit Verification](/chainguard/guardener/github/commit-verification/)** — Enforces cryptographically signed commits against a policy you control, supporting both keyless (Sigstore) signatures and static keys such as GPG.
- **[Dockerfile migration](/chainguard/guardener/dockerfile-migration/)** — Uses AI to iteratively convert your Dockerfiles to Chainguard Containers. This capability runs locally through `chainctl agent dockerfile` commands.

Additional capabilities will be added over time, each with its own opt-in configuration.

## Where to start

- **[GitHub App](/chainguard/guardener/github/)** — Install the app, link your organization, and configure Guardener's GitHub capabilities (Hardened Actions, Container Image Suggestions, Container Image Migration, and Commit Verification):
    - **[Getting started](/chainguard/guardener/github/getting-started/)** — Install the Chainguard App and link your Chainguard organization to your GitHub organization.
    - **[Configuration](/chainguard/guardener/github/configuration/)** — Understand the `.chainguard/` configuration model and how features are enabled per repository.
- **[Dockerfile migration](/chainguard/guardener/dockerfile-migration/)** — Migrate your Dockerfiles to Chainguard Containers using the `chainctl agent dockerfile` commands.

## Support

For questions or feedback, contact your Chainguard account team or email [support@chainguard.dev](mailto:support@chainguard.dev).
