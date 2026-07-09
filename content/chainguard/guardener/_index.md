---
title: "Chainguard Guardener"
linktitle: "Chainguard Guardener"
description: "Chainguard Guardener is a GitHub automation app — a single, hardened bot that helps secure and maintain your repositories."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-07-08T00:00:00+00:00
draft: false
images: []
weight: 025
---

Chainguard Guardener is a GitHub automation app: a single, hardened bot that helps secure and maintain your repositories. Rather than adding a separate integration for every task, the Guardener provides a growing suite of capabilities that you opt into independently, per repository, through configuration files committed to your codebase.

{{< beta feature="Chainguard Guardener" access="organizations that have installed and linked the Chainguard Guardener GitHub App" >}}

The Guardener's capabilities include:

- **[Actions Security](/chainguard/guardener/actions-security/)** — Recommends and migrates your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents, either through non-blocking pull request review comments or automated migration pull requests.
- **[Commit Verification](/chainguard/guardener/commit-verification/)** — Enforces cryptographically signed commits against a policy you control, supporting both keyless (Sigstore) signatures and static keys such as GPG.
- **[Dockerfile migration](/chainguard/migration/the-guardener/)** — Uses AI to iteratively convert your Dockerfiles to Chainguard Containers. This capability runs locally through `chainctl agent dockerfile` commands rather than the GitHub App. See the [Dockerfile migration guide](/chainguard/migration/the-guardener/) for details.

Additional capabilities will be added over time, each with its own opt-in configuration.

## Where to start

- **[Getting started](/chainguard/guardener/getting-started/)** — Install the GitHub App and link your Chainguard organization to your GitHub organization.
- **[Configuration](/chainguard/guardener/configuration/)** — Understand the `.chainguard/` configuration model and how features are enabled per repository.
- **[Actions Security](/chainguard/guardener/actions-security/)** — Configure hardened-action recommendations and automated migration pull requests.
- **[Commit Verification](/chainguard/guardener/commit-verification/)** — Configure a signing policy for commits in pull requests.

## How it works

Once installed and linked, the Guardener listens for events on your repositories (such as opened pull requests) and reads its configuration from the `.chainguard/` directory in each repository. Each capability is disabled until you add and enable its configuration file, so installing the app has no effect on a repository until you opt in.

Because configuration lives in your repository, it is reviewed, versioned, and audited like any other code change.

## Support

For questions or feedback, contact your Chainguard account team or email [support@chainguard.dev](mailto:support@chainguard.dev).
