---
title: "Custom Assembly FAQs"
linktitle: "FAQs"
identifier: "Custom Assembly FAQs"
type: "article"
description: "Answers to you Questions about Chainguard's Custom Assembly tool"
date: 2025-02-19T11:07:52+02:00
lastmod: 2025-03-21T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
    identifier: "Custom Assembly FAQs"
weight: 002
toc: true
contentType: "product-docs"
---

## What is Chainguard’s Custom Assembly?
Custom Assembly is a tool from Chainguard that allows users to build customized container images by assembling packages from a curated, secure set of base images provided by Chainguard.

## How does Custom Assembly help with container image security?
While no system is perfectly secure, Custom Assembly is designed to help you build container images with a strong security posture. By using only guarded packages from Chainguard’s curated and actively maintained images, you benefit from daily CVE scanning and Chainguard’s CVE remediation SLA. This helps minimize risk and provides a clear path for responding to vulnerabilities.

## Can I remove base packages from an image?
No. Base packages such as glibc, busybox, and others included in your selected starting image cannot be removed. You can think of them as the "crust"—you can add toppings, but not change the crust.

## Can I include any package I want in a custom image?
Not exactly. You can only include packages from images you’re entitled to through your Chainguard subscription to stay covered by the SLA.

If you add packages from the general Wolfi OSS repository (not part of a paid image), those packages are not covered by Chainguard’s SLA and may contain unpatched CVEs.

## Is runtime support included for my application?
No. Chainguard supports the Custom Assembly tooling itself but does not debug runtime behavior. For example, if your app crashes due to misconfiguration or conflicting dependencies, you’re responsible for resolving it.

## Can I build FIPS-compliant custom images?
FIPS packages can be used with Custom Assembly, but there is no guarantee that your resulting image will operate in FIPS mode. The FIPS Commitment does not apply to custom images.

## Will I know what’s in my custom image?
Yes. Each image comes with:

* Full build logs
* Software Bill of Materials (SBOMs)
* Provenance metadata

These tools help you understand exactly what's inside your container.

## Is Custom Assembly Covered by an SLA?
Today, Chainguard delivers an [SLA for CVE remediation](https://www.chainguard.dev/legal/cve-sla?utm_source=docs) for all our container images. 

However, when you re-configure Chainguard’s standard, off-the-shelf images, we cannot extend our SLA to packages you add on because we do not have control over the build. You’re thus responsible for maintaining these added packages or run the risk of accruing CVEs.

Customized images built using Custom Assembly will maintain the same engineering and security best practices as Chainguard’s standard containers, with all packages guarded under our CVE remediation SLA.

One bit of nuance in all this is that the SLA doesn’t directly apply to the images customized with Custom Assembly; it only directly applies to the source image. BUT — **as long as you include only _guarded package-versions_ from images that your organization is entitled to**, which are scanned daily for CVEs, you will benefit from the SLA.

When you use Custom Assembly, you’re not just randomly sticking together packages from anywhere. You’re assembling from the curated, protected library of packages that your organization has been granted access to by Chainguard. And if a vulnerability crops up in an entitled package? We’re already on it.

## What Isn’t Covered by an SLA?
So customized images benefit from Chainguard’s CVE SLA — that’s great! But what isn’t supported? 

The following is a list of things that our SLA **won’t** cover:

### You can’t remove base packages
At the moment, base packages included in the starting image — like `glibc`, `busybox`, or core utilities — are **locked in**. So if you select mysql as the base image, any customized images built from it will include the mysql container image's base packages.

Let’s put it like this: you can add toppings, but you can’t change the crust.

### You can’t pull in just any package
With Custom Assembly, you can **only use packages** from the images you’re entitled to through your Chainguard subscription and still be covered by our SLA.

For example, if you add packages from sources like Wolfi (OSS packages), those additions are not covered by the SLA.  The main reason is that a Wolfi package that’s in a paid image is supported and actively maintained. There isn’t a guarantee that free Wolfi packages will be supported and may include CVEs, so we can’t guarantee that the CVE SLA will hold. 

It’s important to understand what is included in your Custom Assembly, as unsupported packages added from external sources may leave you exposed to untracked vulnerabilities. Like we said before, you can pick your own toppings, but you can’t bring your own pepperoni from home.

### We don’t debug your app
You’ll get full **build logs, SBOMs, and provenance** for each image. But if your app throws a `Segmentation fault (core dumped)` after adding 6 versions of `openssl`… yeah, that one’s on you. 

Along these same lines, Chainguard cannot guarantee FIPS compliance for container images built with Custom Assembly. You’re of course allowed to use Custom Assembly with FIPS container images, but this use may result in the custom image not being compliant with FIPS requirements.

Specifically, the SLA states that “in no event shall the FIPS Commitment apply to any Images used with Custom Assembly.” This indicates that while FIPS packages can be used in a custom image, there is no guarantee that the final custom image will operate in FIPS mode.

To sum this point up: Chainguard supports the Custom Assembly tooling, not the runtime behavior of what you build. It’s your party — we're just delivering the pizza!

## What can I do to maintain a strong security posture with Custom Assembly?
While you can't eliminate risk entirely, there are several best practices that help you maintain a secure custom image:
Use only packages from Chainguard images you’re entitled to, which are covered by the CVE remediation SLA.

* Avoid adding external or unsupported packages unless you’re prepared to monitor and patch them independently.
* Rebuild regularly to incorporate upstream fixes and updates.
* Review SBOMs and provenance metadata to verify what's in your image.


Custom Assembly provides the tools and defaults for secure image creation — but ongoing vigilance is key.

## Why Not Use `apk add` to Add Packages?

{{< blurb/why_ca >}}


## Custom Assembly Troubleshooting
Build failures can occur for a number of reasons, including the following:

* It’s possible for you to select packages that conflict with each other. For example, if two packages install the same files, Custom Assembly may not be able to resolve the conflict and result in a failed build.
* Large images taking longer than 1 hour to build will fail with a timeout error.
* When using Custom Assembly through `chainctl`, you choose to add a package which you don't have access to.

In any case, you won’t know whether a container image build fails until after it’s complete. If you need assistance troubleshooting, please [reach out](https://www.chainguard.dev/contact?utm=docs).
