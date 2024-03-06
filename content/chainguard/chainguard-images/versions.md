---
title: "Chainguard Images Product Release Lifecycle"
linktitle: "Product Release Lifecycle"
type: "article"
description: "Understanding Chainguard's Approach to Image Versions"
date: 2024-01-08T08:49:31+00:00
lastmod: 2024-03-06T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 950
toc: true
---

[Chainguard Images](https://images.chainguard.dev/?utm_source=docs) are able to offer low-to-zero known vulnerabilities because they are updated frequently. Because of this continuous release cycle, the best way to mitigate vulnerabilities is to use the newest build of each Chainguard Image available. Chainguard keeps Images up to date by doing one or more of the following:

* Applying new releases from upstream projects
* Rapidly applying upstream patches to current releases — you can read more about this in our blog post, “[How Chainguard fixes vulnerabilities before they're detected](https://www.chainguard.dev/unchained/how-chainguard-fixes-vulnerabilities?utm_source=docs)”
* Applying Chainguard patches to OSS software

Upstream projects are updated frequently for many reasons, including to combat CVEs, and Chainguard ensures that the most up-to-date software is available in all Chainguard Images. Additionally, Chainguard often identifies CVEs and other issues before scanners can detect them, so Chainguard may offer a patch to a vulnerable dependency to support a low-to-zero vulnerability Chainguard Image. 

The best way to mitigate vulnerabilities is to continually update to the latest patched releases of software, but testing and updating can take time and effort. To support flexibility and user choice, Chainguard aims to offer multiple versions of a Chainguard Image that provide the lowest number of vulnerabilities realistically possible. 

This document provides an overview of Chainguard’s approach to updates, releases, and versions within Chainguard Images. For more specific guidance, please [contact us](https://www.chainguard.dev/contact?utm_source=docs). 

## Open Source Release Tracks

In order to understand how Chainguard releases Chainguard Images, it’s first important to understand how different open source projects version and release software. This is because Chainguard Images are built on open source software. There are generally two open source approaches: multiple releases across different versions, or a single release track. In rare cases, open source projects don’t follow a release pattern at all. 

### Multiple Releases Maintained by a Given Open Source Project

Popular open source projects often provide maintenance for a number of release tracks concurrently. For example, Java, Go, Postgres, and Kubernetes patch multiple release versions, each on their own defined maintenance schedule. For these types of projects, Chainguard will maintain every version track of the upstream software that receives updates from the project.

### Single Release Track Maintained by a Given Open Source Project 

Many open source projects support only a single stream of releases that are continuously incremented; often, this is simply the latest release. In the case of a single release track, any security fix that is published will only be applied to the most recent release of the project, and the project release tags will be updated to indicate a new version is available. For this type of project, Chainguard only warrants that the latest release of the software and its corresponding version tags have the most up-to-date patches available.

## What Chainguard Supports and Maintains for Chainguard Images

There are several scenarios that define what Chainguard agrees to maintain regarding software versions in the Chainguard Images Directory. All Images that Chainguard currently supports are those with upstream software that is still supported and maintained, and Chainguard patches and rebuilds these Images daily. If you have purchased an Image during its lifecycle that is no longer being supported upstream, you will still be able to access this Image, _but_ Chainguard will not be patching or rebuilding this Image and the Image will start to accrue CVEs. It is recommended to upgrade to an actively maintained version. 

The table provides some example scenarios to help illustrate our approach. 

| **Category**	| **Example** | **Maintained Upstream Releases** | **Chainguard Patches** | **Chainguard No Longer Patches** | 
|---------------|-------------|----------------------------------|------------------------|----------------------------------|
| **Multiple Release Tracks** | [Go](https://images.chainguard.dev/directory/image/go/versions?utm_source=docs)       | 1.21, 1.20                 | `:latest`, 1, 1.21, 1.20 | 1.21.old, 1.20.old, 1.19, 1.18 |
|                             | [Python](https://images.chainguard.dev/directory/image/python/versions?utm_source=docs)   | 3.12, 3.11, 3.10, 3.9, 3.8 | `:latest`, 3, 3.8 and above | 3.7 and below, 3.8.old, 3.9.old, 3.10.old, 3.11.old, 3.12.old | 
|                             | [Postgres](https://images.chainguard.dev/directory/image/postgres/version?utm_source=docs) | 16, 15, 14, 13, 12         | `:latest`, 16, 15, 14, 13, 12 | 11 (EOL November 9, 2023) | 
| **Single Release Track**    | [Cosign](https://images.chainguard.dev/directory/image/cosign/versions?utm_source=docs)   | 2                          | `:latest`, 2, 2.2 | 2.1, 2.0, 1.x, 0.x | 
|                             | [Bank-Vaults](https://images.chainguard.dev/directory/image/bank-vaults/versions?utm_source=docs) | 1 | `:latest`, 1 | Any previous version tag
| **No Release Track**        | [envoyproxy/ratelimit](https://images.chainguard.dev/directory/image/envoy-ratelimit/versions?utm_source=docs) | No versioned releases | `:latest` | Any previous version tag |

_Note that "Maintained Upstream Releases" is current as of November 2023._

## What Chainguard Image Versions to Expect

When you use freely-available Chainguard Developer Images, you will have access to the `:latest` version of any Image available to the public. In some cases, you will also have access to the `:latest-dev` version, which includes a shell and package manager. For example, the Python Image has both `cgr.dev/chainguard/python:latest` and `cgr.dev/chainguard/python:latest-dev`. Many of the programming languages have these options available, including the Java JDK and JRE Images, PHP, Go, Node, Ruby, and Rust. 

If you are using our enterprise Chainguard Production Images, you will have access to more versions. The Chainguard approach is as follows: 

* For **multiple-release track projects**, you will have access to major and minor versions that are actively maintained. 
* For **single-release track projects**, you will receive the `:latest` tag as well as every versioned tag that is released over time.

## Chainguard Patches and Maintenance

For multiple release software projects with release schedules clearly published, Chainguard will maintain every currently supported version of the software that is maintained by the upstream project. In other words, Chainguard will apply every patch that is available to every maintained version of the upstream software.

For single release track software projects, Chainguard will maintain only the `:latest` version of the software by applying patches and incrementing the version tag when a new patch is released.

Actively maintained Chainguard Images are rebuilt on a daily cadence, so you can be sure the Image you are using is up to date.

## Wolfi Packages in Chainguard Images

Chainguard Images only contain packages that are either built and maintained internally by Chainguard or packages from the [Wolfi Project](https://github.com/wolfi-dev). These packages follow the same conventions of minimalism and rapid updates as Chainguard Images. 

Starting in March of 2024, Chainguard will maintain one version of each Wolfi package at a time. These will track the latest version of the upstream software in the package. Chainguard will end patch support for previous versions of packages in Wolfi. Existing packages will not be removed from Wolfi and you may continue to use them, but be aware that older packages will no longer be updated and will accrue vulnerabilities over time. The tools we use to build packages and images remain freely available and open source in Wolfi.

This change ensures that Chainguard can provide the most up-to-date patches to all packages for our Images customers. Note that specific package versions can be made available in Production Images. If you have a request for a specific package version, please [contact support](https://support.chainguard.dev/hc/en-us).

## SLAs

A vulnerability and patch service-level agreement (SLA) is available for Chainguard Production Images. If you are currently using Chainguard Developer Images, there are no SLAs available, but you will have access to frequently updated and patched Images with low-to-zero CVEs.

If you are a Chainguard Production Images user, Chainguard vulnerability and patch SLAs apply only to supported and maintained versions of upstream projects as clearly published by the upstream projects or published images that can be rebuilt using updated compilers and/or libraries. In the case of single-release track projects, this means that the Chainguard vulnerability and patch SLAs apply only to the latest version and corresponding version tags of the upstream projects. Images that use open source applications that have reached their end of life are no longer patched.

## End of Life and End of Support Software

When an open source application version is no longer maintained by the upstream project or has otherwise met its end of life (EOL), Chainguard will generally no longer provide patches to that software. While the Chainguard Production Images organization directory will continue to have previously purchased Images available, new builds will no longer be published and vulnerabilities are expected to accumulate in those Images over time. It is recommended to move to an up-to-date, actively maintained version. 

For software applications that maintain multiple concurrent release tracks, Chainguard will endeavor to provide reasonable notice when a particular software release version is expected to reach EOL status, thus no longer updated.

No EOL notice will be provided for single-release applications where the only supported release is the `:latest` or corresponding version tag.
