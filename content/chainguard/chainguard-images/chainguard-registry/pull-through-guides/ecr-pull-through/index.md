---
title: "How to Set Up Pull Through from Chainguard's Registry to Amazon ECR"
linktitle: "Amazon ECR"
type: "article"
description: "Overview of using Amazon ECR as a pull-through cache for Chainguard's registry."
date: 2026-03-31T00:00:00+00:00
lastmod: 2026-03-31T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Registry"]
images: []
menu:
  docs:
    parent: "pull-through-guides"
toc: true
weight: 007
---

In March 2026, AWS [announced support](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-ecr-pull-through-cache-chainguard/) for using Amazon Elastic Container Registry (ECR) as a pull-through cache for Chainguard's registry. This means you can configure ECR to automatically cache Chainguard container images, reducing your dependency on Chainguard's registry for production workloads.

For setup and configuration instructions, refer to the official AWS documentation:

* [Amazon ECR pull through cache rules](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html)
* [Pulling an image with a pull through cache rule](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-working-pulling.html)

## Learn More

You can review our [Registry Overview](/chainguard/chainguard-registry/overview/) to learn more about Chainguard's registry, or check out our [Containers documentation](/chainguard/chainguard-images/overview/) to learn more about Chainguard Containers.
