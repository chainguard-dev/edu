---
title: "Chainguard Images FAQs"
linktitle: "FAQs"
type: "article"
description: "Frequently asked questions about Chainguard Images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2024-08-08T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "FAQ", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 015
toc: true
---

Learn answers to your questions about [Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs).

## Which Linux distribution is used as base for Chainguard Images?
Chainguard Images are based on [Wolfi](/open-source/wolfi/), a Linux _undistro_ we built specifically to address software supply chain security issues. We call it an undistro because it doesn't contain certain software you'd normally find in a traditional Linux distribution such as Debian or Alpine. Wolfi is a minimal Linux distribution designed specifically to be used as a base for stripped-down container images.

## How do Chainguard Images relate to the Google Distroless Images?
The [Google distroless](https://github.com/GoogleContainerTools/distroless) images follow a similar philosophy to many of our images: they are minimal images that don't include package managers or shells. The main difference is in the implementation. The Google distroless images are built with [Bazel](https://bazel.build) and based on the Debian distribution, whereas Chainguard Images are built with [apko](/open-source/apko) and based on [Wolfi](/open-source/wolfi). We believe our approach is more maintainable and extensible.

## Which images are available?
There are currently hundreds of Chainguard Images available, which are segmented as **Developer** or **Production**. You can read more about this in the [next question](#what-options-do-i-have-to-use-chainguard-images).

Chainguard Images are primarily available from the [Chainguard Registry](/chainguard/chainguard-registry/overview/), but a selection of developer images is also available on [Docker Hub](https://hub.docker.com/u/chainguard). You can find the complete list of available Chainguard Images in our public [Images Directory](https://images.chainguard.dev/) or within the [Chainguard Console](https://console.chainguard.dev/).

## What options do I have to use Chainguard Images?
You can get free Chainguard Images for your organization. You can also upgrade for more versions, SLAs, and dedicated support.

Developer | Production
-------|-----------------------
Free for everyone, anywhere. | [Contact us](https://www.chainguard.dev/contact?utm_source=docs) for pricing.
Latest versions | Major and minor versions
Community support | Enterprise SLAs
[Developer Docs](https://edu.chainguard.dev/chainguard/chainguard-images/) | Customer support

You can read more about the differences between Developer and Production Images in our [Images Overview](/chainguard/chainguard-images/overview/#production-and-developer-images).

## Are Chainguard Images available on Docker Hub?

Yes, Chainguard Developer Images are available on [Docker Hub](https://hub.docker.com/u/chainguard?utm_source=academy&utm_medium=referral&utm_campaign=FY25-DockerHub-Orgprofile). As a Docker Verified Publisher, Chainguard has met Docker's stringent standards for security, quality, and transparency. This status signifies that our container images are trusted, reliable, and have undergone rigorous verification processes. If you wish to use Production Images, you need to use the [Chainguard Registry](/chainguard/chainguard-registry/overview/).

## What is an SBOM and why is it important?
An SBOM is a Software Bill of Materials, which is a list containing detailed information about all software that is included within a software artifact, whether it's an application, a container image, or a physical appliance.

SBOMs provide visibility into the software you depend on. They can allow automated systems to quickly identify issues such as unpatched vulnerabilities, since SBOMs typically include the version of each dependency listed.

## Who maintains Chainguard Images?
[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) are officially maintained by [Chainguard](https://chainguard.dev) engineers.

## How often are Chainguard Images updated?
Chainguard Images are rebuilt every night to ensure that new package versions and security updates in upstream Wolfi are quickly applied.

## Can I simply replace my current base image with a Chainguard Image and it will work out of the box?
Chainguard Images are designed to be minimal, and many of them don't come with a package manager. Depending on your stack and specific dependencies, you may need to include additional software by combining `-dev` images and our [distroless](/chainguard/chainguard-images/getting-started-distroless/) images in a multi-stage Docker build.

## What packages are available in Chainguard Images?

Chainguard Images only contain packages that come from the [Wolfi Project](https://github.com/wolfi-dev) or those that are built and maintained internally by Chainguard.

Starting in March of 2024, Chainguard will maintain one version of each Wolfi package at a time. These will track the latest version of the upstream software in the package. Chainguard will end patch support for previous versions of packages in Wolfi. Existing packages will not be removed from Wolfi and you may continue to use them, but be aware that older packages will no longer be updated and will accrue vulnerabilities over time. The tools we use to build packages and images remain freely available and open source in [Wolfi](https://github.com/wolfi-dev).

This change ensures that Chainguard can provide the most up-to-date patches to all packages for our Images customers. Note that specific package versions can be made available in Production Images. If you have a request for a specific package version, please [contact us](https://www.chainguard.dev/contact?utm=docs).

## What does Chainguard do when a CVE is published, but a patch is not available from the owner of the OSS code?
Chainguard investigates the CVE and marks relevant images as affected or not. If Chainguard can identify a patch that's unreleased, Chainguard may apply a patch before it lands upstream. In either case, when the patch lands upstream, Chainguard picks it up and rolls it out.

## I added software on top of one of Chainguard's base images, why are there CVEs?
Chainguard is not responsible for CVEs in software you add on top of base images.

## Do I need to authenticate into Chainguard to use Chainguard Images?
Logging in is optional if you are only using Developer Images. That being said, there are benefits for all users who authenticate to the Chainguard Registry, as Chainguard provides notifications of version updates, breaking changes, or critical security updates.

To learn how to authenticate into the Chainguard Registry, you can review our [authentication documentation](/chainguard/chainguard-registry/authenticating/) . You can read more about the thought process behind authentication in our blog post, [Scaling Chainguard Images with a growing catalog and proactive security updates](https://www.chainguard.dev/unchained/scaling-chainguard-images-with-a-growing-catalog-and-proactive-security-updates).
