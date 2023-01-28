---
title: "Overview and FAQs"
type: "article"
description: "Overview and FAQs of Chainguard Enforce Signing"
date: 2023-01-27T15:56:52-07:00
lastmod: 2022-01-27T15:56:52-07:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-signing"
weight: 10
toc: true
---

> _This documentation is related to Chainguard Enforce Signing. You can request access to the product selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Chainguard Enforce Signing is powered by the open source security tool suite [Sigstore](https://www.sigstore.dev/). Enabling you to generate digital signatures for software artifacts, Enforce Signing will enforce signing and verification inside your organization using the individual identities of your team members and [ephemeral keys](https://www.chainguard.dev/unchained/the-principle-of-ephemerality).

Enforce Signing helps organizations ensure the integrity of container images, code commits, and other software artifacts with private signatures that can be validated at any point that verification is needed. Additionally, you can bring your own key and certificate to work with Enforce Signing, so key usage can be monitored and audited against your organization's compliance requirements. 

Enforce Signing is built with privacy in mind. While Sigstore is built on [transparency](https://docs.sigstore.dev/rekor/overview) by design, Enforce Signing will not store any of your information in a public transparency log. This enables you to conform to your organization's privacy requirements while still being able to get the value of Sigstore.

<!-- ## FAQs

To add  -->