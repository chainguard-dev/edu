---
title: "Chainguard Catalog Starter"
linktitle: "Catalog Starter"
type: "article"
description: "Learn about Chainguard Catalog Starter, an offering allowing teams to try out five Chainguard container images for free."
date: 2026-03-09T07:52:00+02:00
lastmod: 2026-07-13T00:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "about"
weight: 060
toc: true
---

Chainguard Catalog Starter is a way to try production-grade Chainguard Containers for free, without committing to a full subscription. It lets you choose a set of five container images from the broader Chainguard catalog so you can validate security, performance, and operational fit in your own environment before you buy.

{{< beta feature="Chainguard Catalog Starter" >}}

To sign up for Catalog Starter, follow the steps on this page. Once set up, you can start piloting up to five secure container images from the Chainguard catalog.

## What is Catalog Starter?

With Chainguard Catalog Starter, users can choose any five non-FIPS images from our catalog of secure-by-default containers. Any Helm charts that depend on those images are included and count toward the five-image limit.

Catalog Starter is designed as a standalone free plan, separate from paid Catalog or per-image subscriptions. It's meant for teams who want to try Chainguard Containers in real workloads before committing to a larger rollout, giving them a better understanding of how Chainguard’s hardened images and CVE posture behave in practice.

> **Note**: Catalog Starter is best suited for small teams to get them started right away. When you are ready to standardize on Chainguard and deploy organization-wide, we have several paid plans that provide unlimited user access to the Chainguard Containers and additional features like Custom Assembly, FIPS images, EOL/EmeritOSS image versions, a contractual CVE-remediation SLA, and dedicated support.

## Sign up for Catalog Starter

### 1. Sign up and select your images

1. Go to [console.chainguard.dev/signup](https://console.chainguard.dev/signup).
2. Sign in with a business email address and create a new account. Catalog Starter requires a corporate email domain — personal email addresses and social media sign-ins are not supported.
3. Enter your company name.
4. Click **Set up an organization**.
5. Complete the form and click **Submit**.
6. Click **Select images**, choose between one and five images, and confirm your selection. You can also go to the **Images** page at any time to make or change your selection.

Once you've added all five images, a prompt directs you to contact Chainguard if you need access to additional images.

### 2. Integrate with your registry and pipelines

After you complete signup, you're free to use the five images you selected however you like. For example, you can pull them into your CI/CD pipelines and runtime environments, or pull them through a third-party registry like [JFrog Artifactory](/chainguard/chainguard-images/chainguard-registry/pull-through-guides/artifactory/artifactory-images-pull-through/). These container images are the same as those provided to Chainguard's paying customers, and are covered by Chainguard’s standard hardening, rebuild, and CVE-remediation processes, although they are not covered by [Chainguard's CVE SLA](https://www.chainguard.dev/legal/cve-policy).

### 3. Upgrade when you’re ready

After trying out Chainguard Containers with Catalog Starter, you can reach out to our sales team to upgrade to one of Chainguard's paid plans:

* [Catalog Pricing](/chainguard/chainguard-images/about/pricing/) — a subscription that grants broad access to the full Chainguard Containers catalog with self-service provisioning through the Console.
* Per-image pricing — a scoped set of images licensed individually, often used for tightly defined image deployments.

Moving to a paid plan means moving off Catalog Starter; the free five-image entitlement is not stacked on top of a paid subscription.

## Plan limitations and terms

Catalog Starter allows users to try out Chainguard Containers, but it comes with certain limitations, including the following:

* You can select up to five non-FIPS images. Once chosen, these images cannot be swapped or replaced during the lifetime of the free plan.
* The following types of Chainguard Containers are not included in the Catalog Starter plan:
    * [FIPS-validated images](/chainguard/fips/fips-images/)
    * Images that fall under the [EOL Grace Period](/chainguard/chainguard-images/features/eol-gp-overview/#understanding-chainguards-eol-grace-period)
    * Images whose software is part of [Chainguard EmeritOSS](https://github.com/chainguard-forks/)
* Teams using Chainguard Catalog Starter will not have access to the support services available to paying customers: they will not be added to Chainguard's support platform, be able to create support tickets, or have access to root cause analysis (RCA) or phone escalations.
    * Catalog Starter users will still have access to Chainguard resources like our [documentation](https://edu.chainguard.dev/), [courses](https://courses.chainguard.dev/), the [Community Slack channel](https://www.chainguard.dev/unchained/the-chainguard-slack-community-is-here), and the [public support knowledge base](https://support.chainguard.dev/hc/en-us).
* [Chainguard's CVE SLA](https://www.chainguard.dev/legal/cve-policy) does not apply to container images obtained through Catalog Starter.
* The free plan does not support user management or role-based access control (RBAC). If a colleague from the same company signs up for Catalog Starter, your organization's administrator receives an email with instructions for adding them. You cannot add users directly. Any additional users in your organization have access to the five images selected by the first user and cannot change them.
* Users in a Catalog Starter organization are assigned the `limited_owner` role, which allows them to browse the Console, pull images, and create pull tokens, but does not include permission to invite other users to the organization or access features like [Custom Assembly](/chainguard/chainguard-images/features/custom-assembly/).
* Neither Custom Assembly nor Commercial Builds, Chainguard's bespoke paid build services, are included in the Catalog Starter plan.
* Catalog Starter cannot be combined with an existing Chainguard Containers license. Existing customers remain on their current paid plans; this free offering can’t be used to subsidize or partially offset paid image counts.

## Frequently asked questions

### Can I change my five images after I select them?

No. Once you’ve selected your five images under Catalog Starter, that selection is fixed for the life of the free plan and cannot be swapped or replaced.

If you anticipate needing different images over time, we recommend talking to our team about Catalog Pricing or per-image licensing.

### Does Catalog Starter include FIPS images or Chainguard Commercial Builds?

No. FIPS images and Chainguard Commercial Builds are not included in the Catalog Starter plan.

If you require FIPS-validated images or dedicated commercial build work, you’ll need a paid plan that includes those capabilities.

### Can my colleagues and I use the same Catalog Starter images?

Yes. If a Catalog Starter organization already exists for your email domain, the administrator of that organization receives an email with instructions for adding you to it. Once added, you'll have access to the five images the first user selected, and neither of you will be able to change them.

Catalog Starter does not include user management or RBAC, so users can't add others to their Chainguard organization themselves.

### I’m already a Chainguard Containers customer. Can I add Catalog Starter to my account?

No. Catalog Starter is a distinct, standalone free plan meant for new organizations. It can’t be combined with existing licenses or used to "carve out" a subset of images from a current subscription.

If you try to sign up using an email domain already associated with a paid Chainguard account, you’ll receive an error message. Contact your Chainguard account administrator for access to your organization’s existing account.

### Can I use Catalog Starter to cover some of the images I need?

No. Catalog Starter is not a discount instrument for larger deployments. You can’t, for example, license 10 images but expect to pay for only five by applying this plan to the rest.

If you know you’ll need more than five images, it’s usually better to start with Catalog Pricing or per-image licensing so you can scale cleanly.

### Can I sign up using a social media account?

No. Catalog Starter requires a business email address. If you sign in using a social login (such as GitHub or Google), you'll be prompted to create a new account with a business email instead.

### What happens if I decide to upgrade to a paid plan?

When you upgrade:

* Your organization moves off the free Catalog Starter plan.
* You gain access to the broader capabilities of your chosen paid tier (for example, full Catalog Pricing with self-service provisioning and, optionally, FIPS access), as well as Chainguard's full support services and CVE SLA.
* Pricing is based on the paid plan’s terms (such as developer bands for Catalog Pricing or image counts for per-image plans).

Our team will work with you to map your existing Catalog Starter images into the right long-term structure.
