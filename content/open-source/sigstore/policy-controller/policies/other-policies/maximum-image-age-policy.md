---
title: "Limit the “Build Horizon” of Build Artifacts with the Maximum Image Age Policy"
linktitle: "Limit “Build Horizon”"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/maximum-image-age-policy/
type: "article"
description: "Understanding the Maximum Image Age Policy"
date: 2023-04-10T15:22:20+01:00
lastmod: 2023-04-11T15:22:20+01:00
draft: false
images: []
tags: ["policy-controller", "Policies", "Enforce", "Product"]
menu:
  docs:
    parent: "other-policies"
weight: 100
toc: true
---

The age of your build artifacts can have serious maintenance and security implications for your Kubernetes workloads. Stale software incurs technical debt and is often more likely to contain vulnerabilities that can put your workloads at risk. Additionally, as we discuss in our article [The Principle of Ephemerality](https://www.chainguard.dev/unchained/the-principle-of-ephemerality), refreshing your build artifacts frequently makes it difficult for an attacker to maintain a toehold in your software should they successfully breach your build system without your knowledge.

The importance of freshness applies to a range of software, such as “off-the-shelf” components like monitoring tools, dependencies you compile into your software like base images, and the software you develop and maintain yourself. That said, tracking the age of every piece of software you use in your workloads can be a daunting task. As pointed out in our blog post [Conquer your Build Horizon with Chainguard Enforce](https://www.chainguard.dev/unchained/conquer-your-build-horizon-with-chainguard-enforce-in-2023), stale software can slip through the cracks despite best efforts.

## Maximum image age policy

One way to address this problem is to impose a “build horizon” on software artifacts. A term first coined at Google, a _build horizon_ refers to the maximum age allowed for build artifacts. The Maximum Image Age policy, compatible with Chainguard Enforce and Sigstore, automatically checks the age of build artifacts in your Kubernetes workloads. You can use this policy to fail images or raise warnings based on their age.

Written in [Rego](/chainguard/chainguard-enforce/policies/chainguard-enforce-rego-policies/) (to take advantage of Rego’s time functions), this policy imposes a maximum age of 30 days on all images and can be customized for other age limits. The age is measured using the container image's configuration, which has a "created" field. Note that some build tools may fail this check because they build reproducibly, and use a fixed date (such as the Unix epoch) as their creation time, but many of these tools support specifying `SOURCE_DATE_EPOCH`, which aligns the creation time with the date of the source commit.

Here is the policy in full:

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: maximum-image-age-rego
  annotations:
    catalog.chainguard.dev/title: Maximum image age
    catalog.chainguard.dev/description: |
      This checks that the maximum age an image is allowed to
      have is 30 days old.  This is measured using the container
      image's configuration, which has a "created" field.

      Some build tools may fail this check because they build
      reproducibly, and use a fixed date (e.g. the Unix epoch)
      as their creation time, but many of these tools support
      specifying SOURCE_DATE_EPOCH, which aligns the creation
      time with the date of the source commit.

    catalog.chainguard.dev/labels: rego
spec:
  images: [{ glob: "**" }]
  authorities: [{ static: { action: pass } }]
  mode: warn
  policy:
    fetchConfigFile: true
    type: "rego"
    data: |
      package sigstore

      nanosecs_per_second = 1000 * 1000 * 1000
      nanosecs_per_day = 24 * 60 * 60 * nanosecs_per_second

      # Change this to the maximum number of days to allow.
      maximum_age = 30 * nanosecs_per_day

      isCompliant[response] {
        created := time.parse_rfc3339_ns(input.config[_].created)

        response := {
          "result" : time.now_ns() < created + maximum_age,
          "error" : "Image exceeds maximum allowed age."
        }
      }
```

## Implementing this policy

You can use this policy freely with the open source [Sigstore policy-controller](/open-source/sigstore/policy-controller/how-to-install-policy-controller) to block new deployments of images based on their age.

However, the Maximum Image Age Policy is particularly useful for monitoring the age of artifacts that are _already admitted_ in your workloads. If you are searching for a way to continuously enforce the Maximum Image Age Policy on _all_ existing images in your Kubernetes workloads, you can use Chainguard Enforce. With [Chainguard Enforce](https://www.chainguard.dev/chainguard-enforce), all of your images will be continuously evaluated against this policy, even if they passed the policy when initially admitted. You can set Enforce to send a notification (including posting to Slack, or opening a GitHub issue) if and when a deployed image falls out of compliance so that corrective action may be taken.

To learn more about Chainguard Enforce, you can read the [Enforce Overview](/chainguard/chainguard-enforce/enforce-overview/) and browse the [Enforce documentation](/chainguard/chainguard-enforce/). You can also request access to the product by selecting Chainguard Enforce for Kubernetes on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs).
