---
title: "Selecting a base image"
description: "Criteria for selecting a base image"
lead: "What to look for when choosing a hardened, minimal base image"
type: "article"
date: 2022-08-04T15:21:01+02:00
lastmod: 2022-08-04T15:21:01+02:00
contributors: ["John Speed Meyers"]
draft: false
tags: ["Conceptual"]
images: []
menu:
  docs:
    parent: "software-security"
weight: 10
toc: true
---

Software teams building and deploying container-based software applications often use a “base image,” an initial set of software packages often associated with a Linux distribution. Software developers, security professionals, and infrastructure teams seeking to make an informed decision about what base image to use must consider a number of criteria when selecting a base image appropriate for their needs. To help these parties make a more informed decision when selecting a base image, this article describes a range of criteria:

- Ensuring the image contains needed core functionality
- The number of known vulnerabilities
- The frequency at which the image is rebuilt
- The number of packages
- The update frequency and security hygiene of the underlying distribution
- The amount of maintainer support associated with the base image
- The size of the image in MB
- Whether the image is signed
- Whether the image has an SBOM

After reading this section, software professionals will have a mental checklist that makes them better prepared to select a base image for container-based software applications.

## Ensure the base image contains needed core functionality

First and foremost, the base image needs to contain the necessary minimum functionality. For instance, for a team that is developing a Python application, this would include the Python runtime, the software that translates source code into machine code. Without the appropriate core functionality, the base image will be unable to serve the needs of the software developer and his or her application. More technical users might also be interested in aspects such as whether there is glibc or musl support.

## Choose an image with few or no known vulnerabilities

Another key factor is the number of known vulnerabilities associated with the packages inside the image. Popular open source scanners such as [`trivy`](https://github.com/aquasecurity/trivy) and [`grype`](https://github.com/anchore/grype) allow a user to scan container images to identify vulnerabilities. Known vulnerabilities, consistently ranked a [critical security threat](https://owasp.org/www-project-top-ten/) for web applications, allow attackers to exploit a piece of software without the work of discovering a previously unknown vulnerability. Recent empirical software security [research](https://decan.lexpage.net/files/EMSE-2021.pdf) indicates that many popular images have hundreds of known vulnerabilities.

Software teams should select base images with as few known vulnerabilities as possible. This not only has security benefits but also reduces the toil of manually triaging vulnerabilities, i.e. determining whether the vulnerability is a true positive or false positive and whether the vulnerability is exploitable in the context of the deployed application.

While some specialists point out that many reported vulnerabilities have never been known to be exploited [in the wild](https://www.cisa.gov/known-exploited-vulnerabilities), this observation should not be mistaken as an invitation to disregard vulnerability counts. Because many, perhaps most, compromises are never reported, any list of vulnerabilities known to have been exploited should be treated as imperfect knowledge. Other vulnerabilities might have been exploited in the wild and no defender knows yet. In short, maintaining a low known vulnerability count reduces security risk and staff toil, thereby enabling faster development.

## Choose an image that is frequently rebuilt

Of course, choosing an image that has a low vulnerability count today does not guarantee a low vulnerability count tomorrow. New vulnerabilities can arise, new non-security bugs are patched, and new features emerge for the many packages inside a base image. To enable a software team to take advantage of new fixes, security or otherwise, developers ought to prefer images that are rebuilt frequently. Rebuilding entails using the latest versions of all the constituent packages, which reduces the vulnerability count and enables downstream consumers of the base image to upgrade the version if desired.

Some research suggests that over half of the container images found on Docker hub, a repository for container images, haven’t been updated for four months or longer. Update cadences for official Docker images, a curated set of images, can have similarly slow update cadences. When selecting a base image, a software team should   examine the frequency of updating.

## Choose an image with a minimal number of packages

Choosing base images with a minimal number of packages is also a sensible principle. This reduces the “attack surface” and also reduces complexity. Fewer packages, all things equal, means fewer vulnerabilities (both known and unknown). Additionally, for teams that must use a pinned imaged and thus can’t take advantage of frequent rebuilds, fewer packages also means a slower vulnerability accumulation rate.

Additionally, choosing [“distroless”](https://edu.chainguard.dev/software-security/videos/distroless/) images, which strips out package managers, package manager dependencies, and other build-time dependencies, is another way to ensure that your team is choosing a secure-by-default base image.

## Choose an image based on a software distribution that prioritizes package update frequency and security hygiene

The packages inside a container are often sourced from a Linux distribution such as Debian, Ubuntu, or [Wolfi](https://edu.chainguard.dev/open-source/wolfi/overview/). The update frequency and hence the security of an image therefore also depends on the software development practices associated with that distribution. Software teams should therefore assess the distribution underlying the packages in their images. All things equal, software teams should prefer a distribution that prioritizes frequent updates so that vulnerabilities are quickly fixed.

## Choose an image with maintainers that actively support it

Not all container images are actively maintained. Like open source software packages in general, container images require one or more persons to ensure timely and frequent rebuilds, to manage broader security concerns, and to respond to bugs and issues. Unmaintained or lightly maintained images can pose a problem to software teams that want to prioritize development velocity and security. Without the ability to rapidly work with upstream image maintainers, software teams must either accept the risk of using old versions of the image that potentially haveunpatched bugs, or consider creating and maintaining a fork with the overhead associated with that course of action.

## Choose an image that is smaller

Smaller images (fewer MB) means less storage costs and less transmission costs. When an image is pulled thousands of times a day, even a small difference in size can quickly add to the cost.

## Choose an image that is signed

Software signing ensures that attackers that tamper with a software artifact, such as a container image, can be detected. Software teams should choose to use container images that have been signed, with tools such as [Cosign](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/), and verify the signatures to ensure that the images on which they depend are tamper-free.

## Choose an image with an SBOM

A [software bill of materials](https://edu.chainguard.dev/open-source/sbom/what-is-an-sbom/) (SBOM), a list of ingredients for a piece of software, provides visibility into the components of a piece of software, enabling transparency and informed decision-making. Choosing base images with SBOMs generated by the party responsible for building the artifact helps the image consumer better make decisions related to the security and health of the code.

## Self-assessment

[True or False] The frequency at which a container image is rebuilt does not affect the number of known software vulnerabilities associated with the container image.

[True or False] Choosing base images with few or no known vulnerabilities reduces security risk and reduces staff toil.

For readers interested in an example of images that prioritize the criteria described above, [Chainguard Images](https://github.com/chainguard-images) offers one option.
