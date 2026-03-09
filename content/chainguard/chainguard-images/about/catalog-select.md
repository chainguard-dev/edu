---
title: "Chainguard Catalog Select"
linktitle: "Catalog Select"
type: "article"
description: "Learn about Chainguard's Catalog Select, an offering allowing teams to try out five Chainguard container images for free."
date: 2026-03-09T07:52:00+02:00
lastmod: 2026-03-09T07:52:00+02:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "about"
weight: 060
toc: true
---

Chainguard Catalog Select is a free way to try production-grade Chainguard Containers without committing to a full subscription. It lets you choose a set of five container images from the broader Chainguard catalog so you can validate security, performance, and operational fit in your own environment before you buy.

## What is Catalog Select?

With Chainguard Catalog Select, users can choose any five non-FIPS images from our catalog of secure-by-default containers. Any Helm charts that depend on those images are included and count toward the five-image limit. Users also get access to one image customized with [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/), allowing them to add extra packages or custom certificates directly into the image. 

Catalog Select is designed as a standalone free plan, separate from paid Catalog Pricing or per-image subscriptions. It's meant for teams who want to try Chainguard Containers in real workloads before committing to a larger rollout, giving them a better understanding of how Chainguard’s hardened images and CVE posture behave in practice.

> **Note**: Catalog Select is an offering intended for potential customers to evaluate Chainguard, not for existing Chainguard Containers customers.


## How Catalog Select works

### 1. Sign up with your organization

Catalog Select is designed for business use. Sign-ups are limited to corporate email domains (for example, `@company.com`) rather than personal email addresses.

After you submit [the request form](), our team will quickly review and enable access for qualified organizations.


### 2. Choose your five images

Once your organization is enabled, you can browse the Chainguard catalog and select up to five non-FIPS images to be provisioned to your organization. Additionally, you can use Chainguard's Custom Assembly tool to customize one image. 


### 3. Integrate with your registry and pipelines

After selecting your five container images, you're free to use them however you like. For example, you can pull them into your CI/CD pipelines and runtime environments, or pull them through a third-party registry like [JFrog Artifactory](/chainguard-images/chainguard-registry/pull-through-guides/artifactory/artifactory-images-pull-through/). These container images are also covered by Chainguard’s standard hardening, rebuild, and CVE-remediation processes, although they are not covered by [Chainguard's CVE SLA](https://www.chainguard.dev/legal/cve-policy).


### 4. Upgrade when you’re ready

After trying out Chainguard Containers with Catalog Select, you can reach out to our sales team to upgrade to one of Chainguard's paid plans:

* [Catalog Pricing](/chainguard/chainguard-images/about/pricing/) — a subscription that grants broad access to the full Chainguard Containers catalog with self-service provisioning through the Console.
* Per-image pricing — a scoped set of images licensed individually, often used for tightly defined image deployments.

Moving to a paid plan means moving off of Catalog Select; the free five-image entitlement is not stacked on top of a paid subscription.


## Plan limitations and terms

Catalog Select allows users to try out Chainguard Containers, but it comes with certain limitations, including the following:

* You can select up to five non-FIPS images. Once chosen, these images cannot be swapped or replaced during the lifetime of the free plan.
    * FIPS-validated images are not included in Catalog Select.
* Teams that sign up for Catalog Select will only have access to Chainguard's digital support, including [documentation](https://edu.chainguard.dev/), [courses](https://courses.chainguard.dev/), the [Community Slack channel](https://www.chainguard.dev/unchained/the-chainguard-slack-community-is-here), and the [public support knowledge base](https://support.chainguard.dev/hc/en-us). Catalog Select users will not be able to create support tickets.
* [Chainguard's CVE SLA](https://www.chainguard.dev/legal/cve-policy) does not apply to container images obtained through Catalog Select.
* The free plan supports a single user account in the Chainguard Console for your organization. You can still integrate images into CI/CD and production using tokens, but you cannot invite other users to your organization, nor can other users pull your selected containers.
* Commercial Builds, Chainguard's bespoke paid build services, are not included. The plan includes one Custom Assembly build, but not an ongoing build-as-a-service arrangement.
* Catalog Select does not include the ability to upload and host your own custom images in Chainguard’s registry. You consume Chainguard-provided images only.
* Catalog Select cannot be combined with an existing Chainguard Containers license. Existing customers remain on their current paid plans; this free offering can’t be used to subsidize or partially offset paid image counts.


## Frequently asked questions

### Can I change my five images after I select them?

No. Once you’ve selected your five images under Catalog Select, that selection is fixed for the life of the free plan and cannot be swapped or replaced.

If you anticipate needing different images over time, we recommend talking to our team about Catalog Pricing or per-image licensing.

### Does Catalog Select include FIPS images or Chainguard Commercial Builds?

No. FIPS images and Chainguard Commercial Builds are not included in Catalog Select.

If you require FIPS-validated images or dedicated commercial build work, you’ll need a paid plan that includes those capabilities.

### I’m already a Chainguard Containers customer. Can I add Catalog Select to my account?

No. Catalog Select is a distinct, standalone free plan meant for new organizations. It can’t be combined with existing licenses or used to "carve out" a subset of images from a current subscription.

### Can I use Catalog Select to pay for only some of the images I need?

No. Catalog Select is not a discount instrument for larger deployments. You can’t, for example, license 10 images but expect to pay for only five by applying this plan to the rest.

If you know you’ll need more than five images, it’s usually better to start with Catalog Pricing or per-image licensing so you can scale cleanly.

### What happens if I decide to upgrade to a paid plan?

When you upgrade:

* Your organization moves off the free Catalog Select plan.
* You gain access to the broader capabilities of your chosen paid tier (for example, full Catalog Pricing with self-service provisioning and, optionally, FIPS access), as well as Chainguard's full support services and CVE SLA.
* Pricing is based on the paid plan’s terms (such as developer bands for Catalog Pricing or image counts for per-image plans).

Our team will work with you to map your existing Catalog Select images into the right long-term structure.


## Get started

To sign up for Catalog Select, fill out [this form]() and our team will review the request and enable access if your organization qualifies. Once enabled, you can begin piloting up to five secure container images from the Chainguard catalog. 