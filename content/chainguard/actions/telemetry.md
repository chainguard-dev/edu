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

Every Chainguard hardened action runs a best-effort "phone-home" pre-hook that records a usage and entitlement event to `https://actions.enforce.dev/actions/v1/record`. This page documents what the hook sends, what Chainguard stores, and how you can control it.

The hook is fire-and-forget. It has a 2 second timeout and fails open, so it can never block or break your workflow.

## What we collect

What Chainguard receives depends on whether your workflow grants the `id-token: write` permission to the job running the action.

- **Without `id-token: write`:** we record only your repository name, a timestamp, and an "unverified" flag. Nothing else.
- **With `id-token: write`:** the hook mints a GitHub OIDC token scoped to the `actions.chainguard.dev` audience and includes it so we can verify the record. From that verified token we store usage and entitlement metadata: repository, actor, ref, sha, workflow path, repository visibility, and run identifiers.

The hook never grants itself the `id-token: write` permission. It only uses the permission if your workflow already grants it. If you would rather Chainguard receive only your repository name, do not grant `id-token: write` to the job that runs the action.

## About the OIDC token

When it is sent, the token is a short-lived, audience-locked GitHub OIDC token. Because it is locked to the `actions.chainguard.dev` audience, it cannot be replayed against GitHub, a cloud provider, or any other service. The underlying `ACTIONS_ID_TOKEN_REQUEST_TOKEN` never leaves the runner; it is used locally only to mint the audience-scoped token.

## Why we collect it

The telemetry lets Chainguard verify that an organization is entitled to the hardened actions it uses and understand how the actions are used so we can improve them. It is usage and entitlement metadata, not the contents of your build.

## Data retention

Operational logs that include telemetry events are retained for a limited period (approximately 30 days). A durable analytics copy of usage and entitlement metadata is retained in accordance with our [Privacy Notice](https://www.chainguard.dev/legal/privacy-notice).

## Learn more

- [Chainguard Actions overview](/chainguard/actions/overview/)
- [Chainguard Privacy Notice](https://www.chainguard.dev/legal/privacy-notice)
- For other questions, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).
