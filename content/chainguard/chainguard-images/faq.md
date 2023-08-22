---
title: "Chainguard Images FAQs"
linktitle: "FAQs"
type: "article"
description: "Frequently asked questions about Chainguard Images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2023-08-22T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "FAQ", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 500
toc: true
---

Learn answers to your questions about [Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs).

## Which Linux distribution is used as base for Chainguard Images?
Chainguard images are based on [Wolfi](/open-source/wolfi/), a Linux _undistro_ we built specifically to address software supply chain security issues.
We do have some images with Alpine-based variants in order to support musl or unusual architectures.

## How do Chainguard Images relate to the Google Distroless Images?
The [Google distroless](https://github.com/GoogleContainerTools/distroless) images follow a similar
philosophy to many of our images: they are minimal images that don't include package managers or
shells. The main difference is in the implementation. The Google distroless images are built with
[Bazel](https://bazel.build) and based on the Debian distribution, whereas Chainguard Images are
built with [apko](/open-source/apko) based on the [Wolfi](/open-source/wolfi) or Alpine
distributions. We believe our approach is more maintainable and extensible.

## What is an "undistro"?
We call Wolfi an undistro because unlike a typical Linux distribution, Wolfi is a stripped-down distribution designed for the cloud-native era. Most notably, we don’t include a Linux kernel, instead relying on the environment (such as the container runtime) to provide this.

## Which images are available?

There are currently over 100 Chainguard Images available, which are segmented in [three catalog tiers](#what-are-the-different-catalog-tiers-of-chainguard-images). You can read more about the tiers in the [next question](#what-are-the-different-catalog-tiers-of-chainguard-images).

Our full Images Catalog is available on the Chainguard Console at [https://console.enforce.dev/images/catalog](https://console.enforce.dev/images/catalog) (you will need to be logged in). 

To review our public catalog, you can check out either the [Chainguard Images Reference Docs](https://edu.chainguard.dev/chainguard/chainguard-images/reference/) or the  [GitHub Repository](https://github.com/chainguard-images).

Chainguard Images are available through the [Chainguard Registry](/chainguard/chainguard-images/registry/overview/).

## What are the different catalog tiers of Chainguard Images?

The Public Chainguard Images Catalog is available at no cost to users. Our paid catalogs currently include Standard and Custom subscription tiers, featuring enterprise-grade patching SLAs and customer support. 

The **Public Catalog** includes no cost access to the latest version of all images from applications and middleware, development and build tools and language runtimes.

The **Standard Catalog** includes the Public Catalog, plus all upstream supported older versions of programming languages and development tools. This includes Maven, Gradle, Kubectl, Ko, and more.

The **Custom Catalog** includes the Standard Catalog plus access to a custom set of images of your choosing. Chainguard offers a full suite of databases, web servers, proxies, monitoring tools, and SDK images.

Review the comparison table below for additional information about our catalog tiers.

Catalog | Public Catalog | Standard Catalog | Custom Catalog
--------|----------------|------------------|---------------
**Versions** | `:latest`, `:latest-dev`, and images by digest | All upstream supported version tags including ``:latest`` and ``:latest-dev`` | All upstream supported version tags including ``:latest`` and ``:latest-dev``, plus end-of-life versions
**Image Signatures** | Yes | Yes | Yes 
**SBOMS and Attestations** | Yes | Yes | Yes
**SLSA Provenance** | Build Level 2 | Build Level 2 | Build Level 2
**Notifications** | Only when logged in, via email | Yes, webhook and email | Yes, webhook and email
**Images Web Console** | Only when logged in | Yes | Yes
**FIPS** | N/A | Available on Request ($) | Available on Request ($)
**OIDC Federation** | None | Yes | Yes
**Patch SLA** | None | 14 business days | 7 business days
**Support** | None | Chainguard Direct Support | Chainguard Direct Support

## What is an SBOM and why is it important?
An SBOM is a Software Bill of Materials, which is a list containing detailed information about all software that is included within a software artifact, whether it's an application, a container image, or a physical appliance.

SBOMs provide visibility into the software you depend on. They can allow automated systems to quickly identify issues such as unpatched vulnerabilities, since SBOMs typically include the version of each dependency listed.

## Who maintains Chainguard Images?
[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) are officially maintained by [Chainguard](https://chainguard.dev) employees, but they are also open source, which means any community member is welcome to suggest improvements.

## Can I simply replace my current base image with a Chainguard Image and it will work out of the box?
Chainguard Images are designed to be minimalist, and many of them are distroless, which means they don't come with a package manager. Depending on your stack and specific dependencies, you may need to include additional software by combining development images and distroless images in a multi-stage Docker build.

## How often are Chainguard Images updated?
Chainguard Images are rebuilt every night to ensure that new package versions and security updates in upstream Wolfi are quickly applied.

## Do I need to authenticate into Chainguard to use Chainguard Images?
Logging in is optional if you are only using `:latest` and `:latest-dev` tags or image digests. 

As of August 16, 2023, all other tags for Chainguard Images in the Public catalog are unavailable without paying for access to the Standard or Custom catalogs. This means that Public catalog users, including open source projects, will either need to pin to the digest they currently use, migrate to the software version associated with `:latest`, or build upon [wolfi-base](/chainguard/chainguard-images/reference/wolfi-base/) to build their desired image.

There are benefits for all users who authenticate to the Chainguard Registry, as Chainguard provides notifications of version updates, breaking changes, or critical security updates. However, users can continue to pull Images by digest or Images tagged `:latest` anonymously. 

To learn how to authenticate into the Chainguard Registry, you can review our [authentication documentation](/chainguard/chainguard-images/registry/authenticating/). You can read more about our Images catalogs and some of the thought process behind authentication in our blog post, [Scaling Chainguard Images with a growing catalog and proactive security updates](https://www.chainguard.dev/unchained/scaling-chainguard-images-with-a-growing-catalog-and-proactive-security-updates). You can read about the August 16, 2023 changes in the [Important updates for Chainguard Images public catalog users](https://www.chainguard.dev/unchained/important-updates-for-chainguard-images-public-catalog-users) blog post.
