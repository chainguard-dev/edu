---
title: "Registry Overview"
type: "article"
description: "An Overview of Chainguard's Registry"
date: 2023-03-21T16:36:47+00:00
lastmod: 2025-04-11T16:36:47+00:00
draft: false
images: []
tags: ["Chainguard Containers", "Registry", "Product"]
menu:
  docs:
    parent: "registry"
weight: 005
toc: true
---

Chainguard's registry provides public access to all public Chainguard Containers, and provides customer access for image variants through login and authentication.

While all public Chainguard Containers are freely available, logging in with a Chainguard account and authenticating when pulling from the registry provides a mechanism for Chainguard to contact you if there are any current or known upcoming issues with images you are pulling.

If you would like to learn more about **Chainguard Containers**, you can review our [documentation](/chainguard/chainguard-images/overview/), and you can request further information through our [inquiry form](https://www.chainguard.dev/contact?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement).

## Status

You can check the status of Chainguard's registry at [https://status.cgr.dev](https://status.cgr.dev/).

## Network Requirements

Refer to our [Network Requirements](/chainguard/administration/network-requirements) reference page for details about how to ensure access to Chainguard's registry in environments using firewalls, access control lists, and proxies.

## Using a Caching Proxy with Chainguard's registry

Chainguard does not offer an SLA for uptime for the Chainguard's registry. In order to minimize production dependency on the Chainguard's registry, we recommend that customers use a pull-through proxy for maximum reliability.

We currently provide documentation on how you can set up a pull-through cache for the Chainguard's registry on the following platforms:

* [Google Artifact Registry](/chainguard/chainguard-registry/pull-through-guides/artifact-registry-pull-through/)
* [JFrog Artifactory](/chainguard/chainguard-registry/pull-through-guides/artifactory/)
* [Sonatype Nexus](/chainguard/chainguard-registry/pull-through-guides/nexus-pull-through/)
* [Cloudsmith](/chainguard/chainguard-registry/pull-through-guides/cloudsmith-pull-through/)
