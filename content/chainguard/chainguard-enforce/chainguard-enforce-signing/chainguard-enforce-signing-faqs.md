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

**Chainguard Enforce Signing is in _Beta Preview_. You can request access to the product selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs).**

Chainguard Enforce Signing is powered by [Sigstore](https://www.sigstore.dev/), a suite of open source security tools. Enabling you to generate digital signatures for software artifacts, Enforce Signing will enforce signing and verification inside your organization using the individual identities of your team members and [ephemeral keys](https://www.chainguard.dev/unchained/the-principle-of-ephemerality).

Enforce Signing helps organizations ensure the integrity of container images, code commits, and other software artifacts with private signatures that can be validated at any point that verification is needed. Additionally, you can bring your own key and certificate to work with Chainguard Enforce Signing, so key usage can be monitored and audited against your organization's compliance requirements. 

Chainguard Enforce Signing is built with privacy in mind. While Sigstore is built on [transparency](https://docs.sigstore.dev/rekor/overview) by design, Enforce Signing will not store any of your information in a public transparency log. This enables you to conform to your organization's privacy requirements while still being able to get the value of Sigstore.

## FAQs

Here are some of the frequently asked questions on Chainguard Enforce Signing. Please [contact us](https://www.chainguard.dev/contact?utm_source=docs) if you have additional questions.

### Where are signing keys stored?

Keys are stored as KMS resources in your own AWS or GCP project. When you set up an account association, you’ll give Chainguard access to sign with your KMS key. Since the key is in your project, you can set up audit logging to see when your key has been used.

### Does Chainguard have access to my private key?

Chainguard has permissions to sign with your KMS key, which is how certificates from Enforce Signing are issued. Chainguard can’t see the private key and we recommend setting up audit logging to track each time the key has been used.

### Which cloud providers are supported?

Currently, we support Enforce Signing on GCP and AWS. For GCP, you can use the GCP CA service directly for Enforce Signing. For both GCP and AWS, you can set up a KMS-based certificate authority by providing your own KSM key and a valid root certificate chain.

### Does Enforce Signing support AWS Private CA?

Neither the open source Sigstore project nor Enforce Signing currently supports AWS Private CA. If you’re interested in using Enforce Signing with AWS Private CA, please [let us know](https://www.chainguard.dev/contact?utm_source=docs).
