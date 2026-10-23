---
title: "Guardener overview"
linktitle: "Guardener overview"
description: "Guardener is a tool for managing and hardening your source code, with a growing suite of capabilities you opt into independently."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-10-23T16:30:59+00:00
draft: false
tags: ["Overview"]
images: []
menu:
  docs:
    parent: "guardener"
weight: 5
toc: true
---

Guardener is a tool for managing and hardening your source code. Rather than adding a separate integration for every task, Guardener provides a growing suite of capabilities that you opt into independently. Some capabilities run through the Chainguard App, a hardened GitHub App, and are configured per repository through files committed to your codebase; others, such as Dockerfile migration, run locally through `chainctl`.

## Optional features

Each Guardener capability is an optional feature: it stays off until you turn it on. Guardener and its optional features are subject to the [Guardener terms](https://www.chainguard.dev/legal/guardener-terms) and the [Code Analysis Terms](https://www.chainguard.dev/legal/code-analysis-terms). Under those terms, all of them are Technology Previews, including the features in Early Access.

| Optional feature | What it does | How to turn it on | Stage |
| ---------------- | ------------ | ----------------- | ----- |
| [Hardened Actions](/chainguard/guardener/github/actions-security/) | Recommends hardened, SHA-pinned replacements from Chainguard Actions for your GitHub Actions in pull request review comments and opens migration pull requests on a schedule or on demand. | Add `.chainguard/actions.yaml` to a repository. | Early Access |
| [Container Image Suggestions](/chainguard/guardener/github/image-suggestions/) | Recommends Chainguard container images for the images that a pull request adds or changes, with one-click suggested changes where possible. | Add `.chainguard/images.yaml` to a repository. | Early Access |
| [Container Image Migration](/chainguard/guardener/github/image-migration/) | Opens a pull request, on a schedule or on demand, that replaces a repository's existing container images with Chainguard container images. | Add a `migrate` block to `.chainguard/images.yaml`. | Early Access |
| [Commit Verification](/chainguard/guardener/github/commit-verification/) | Checks that an authorized signer signed every commit in a pull request. Supports keyless (Sigstore) signatures and static keys such as GPG. | Add `.chainguard/source.yaml` to a repository. | Beta |
| [Dockerfile migration](/chainguard/guardener/dockerfile-migration/) | Uses AI to iteratively convert your Dockerfiles to use Chainguard Containers. Docker builds run on your machine. | Join the waitlist, then run `chainctl agent dockerfile` commands. | Beta |
| [Skill hardening](/chainguard/agent-skills/skill-hardening/) | Hardens the agent skills you upload and reports what changed. | Run `chainctl skills harden`. | Beta |
| [Chainguard Harness](https://www.chainguard.dev/harness) | Finds exploitable vulnerabilities in your application code with a frontier AI model and returns fixes a Chainguard engineer has reviewed. | Join the waitlist, then give Chainguard read-only access to your code through the Chainguard App or send a source archive. | Beta |

Chainguard adds optional features over time and updates this table when it does.

## Where to start

- **[GitHub App](/chainguard/guardener/github/)** — Install the app, link your organization, and configure Guardener's GitHub capabilities (Hardened Actions, Container Image Suggestions, Container Image Migration, and Commit Verification):
    - **[Getting started](/chainguard/guardener/github/getting-started/)** — Install the Chainguard App and link your Chainguard organization to your GitHub organization.
    - **[Configuration](/chainguard/guardener/github/configuration/)** — Understand the `.chainguard/` configuration model and how features are enabled per repository.
- **[Dockerfile migration](/chainguard/guardener/dockerfile-migration/)** — Migrate your Dockerfiles to Chainguard Containers using the `chainctl agent dockerfile` commands.

## Support

For questions or feedback, contact your Chainguard account team or email [support@chainguard.dev](mailto:support@chainguard.dev).
