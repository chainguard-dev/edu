---
title: "Chainguard Actions telemetry and privacy"
linktitle: "Telemetry and privacy"
description: "Learn what usage telemetry Chainguard hardened actions send, what data is collected, and how to control it."
type: "article"
date: 2026-07-16T00:00:00+00:00
lastmod: 2026-07-16T00:00:00+00:00
draft: false
tags: ["Chainguard Actions", "Telemetry", "Privacy"]
menu:
  docs:
    parent: "actions"
weight: 002
toc: true
---

Every Chainguard hardened action runs a best-effort "phone-home" pre-hook that records a usage event to `https://actions.enforce.dev/actions/v1/record`. The hook is fire-and-forget, with a 2 second timeout that fails open, so it cannot break your build.

## What we collect

What we collect depends on whether your workflow grants `id-token: write`:

- **Without `id-token: write`:** we record your repository name, a timestamp, and an "unverified" flag.
- **With `id-token: write`:** the hook mints a GitHub OIDC token scoped to the `actions.chainguard.dev` audience and sends it so we can verify the record. From that token we store metadata: repository, actor, ref, sha, workflow path, repository visibility, and run identifiers.

The hook never grants itself `id-token: write`. It only uses the permission if your workflow already grants it. If you would rather we receive only your repository name, do not grant `id-token: write` to that job.

## About the token

It is a short-lived, audience-locked GitHub OIDC token. Because it is locked to the `actions.chainguard.dev` audience, it cannot be used against GitHub, a cloud provider, or any other service. The underlying `ACTIONS_ID_TOKEN_REQUEST_TOKEN` never leaves the runner; it is used locally only to mint the audience-scoped token.

## Learn more

- [Chainguard Actions overview](/chainguard/actions/overview/)
- For other questions, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).
