---
title: "How to disable policy enforcement"
type: "article"
description: "Quickly handle incident responses in Chainguard Enforce"
date: 2022-11-29T08:49:31+00:00
lastmod: 2023-01-12T08:49:31+00:00
draft: true
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 700
toc: true
---

> _This document relates to Chainguard Enforce. In order to follow along, you will need access to Chainguard Enforce. You can request access through selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._


Change the behavior of the policies by letting the controller warn instead of failing

Configure it via a configMap for all the images not matching any defined policy https://docs.sigstore.dev/policy-controller/overview/#admission-of-images (explained in the last paragraph of this subsection)

An example of no policy matched:

    If the image does not match against any policy
    Fallback to deprecated policy-controller validation behavior
    Validation will be attempted against the secret defined under cosign.secretKeyRef.name during helm installation.
    If a valid signature or attestation is obtained, image is admitted
    If no valid signature or attestation is obtained, image is denied

Configuring policy-controller ClusterImagePolicy