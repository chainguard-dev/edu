---
title: "Registry overview"
type: "article"
description: "Learn about Chainguard's container registry, including public access to free images, authenticated access for production images, and network requirements"
date: 2023-03-21T16:36:47+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
images: []
tags: ["Chainguard Containers", "Registry"]
menu:
  docs:
    parent: "registry"
weight: 010
toc: true
aliases:
- /chainguard/chainguard-registry/overview/
- /chainguard/chainguard-images/chainguard-registry/overview/
- /chainguard/containers/chainguard-registry/overview/
---

Chainguard Registry hosts more secure container images with two access tiers: public Free images available to everyone, and production images that require authentication for enterprise features like SLAs and version pinning. The registry integrates with standard container tools while providing enhanced security through signed images and comprehensive metadata.

While all public Chainguard Containers are freely available, logging in with a Chainguard account and authenticating when pulling from the registry provides a mechanism for Chainguard to contact you if there are any current or known upcoming issues with images you are pulling.

If you would like to learn more about **Chainguard Containers**, you can review our [documentation](/chainguard/containers/overview/), and you can request further information through our [inquiry form](https://www.chainguard.dev/contact?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement).

## Status

You can check the status of Chainguard's registry at [https://status.cgr.dev](https://status.cgr.dev/).

## Network requirements

Refer to our [Network requirements](/chainguard/containers/registry/network-requirements/) reference page for details about how to ensure access to Chainguard's registry in environments using firewalls, access control lists, and proxies.

## Using a caching proxy with Chainguard's registry

Chainguard does not offer an SLA for uptime for the Chainguard's registry. In order to minimize production dependency on the Chainguard's registry, we recommend that customers use a pull-through proxy for maximum reliability.

We currently provide documentation on how you can set up a pull-through cache for the Chainguard's registry on the following platforms:

* [Amazon ECR](/chainguard/containers/registry/pull-through-guides/ecr-pull-through/)
* [Google Artifact Registry](/chainguard/containers/registry/pull-through-guides/artifact-registry-pull-through/)
* [JFrog Artifactory](/chainguard/containers/registry/pull-through-guides/artifactory-containers-pull-through/)
* [Sonatype Nexus](/chainguard/containers/registry/pull-through-guides/nexus-pull-through/)
* [Cloudsmith](/chainguard/containers/registry/pull-through-guides/cloudsmith-pull-through/)
