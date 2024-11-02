---
title: "Selecting a Base Image"
linktitle: "Selecting a Base Image"
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

When building and deploying container-based software applications, teams often rely on a "base image." This foundational layer typically consists of a set of software packages associated with a specific Linux distribution. To make an informed choice about which base image to use, software developers, security professionals, and infrastructure teams must evaluate several critical criteria. This article outlines key considerations to guide your selection process:

<ins>__Key Criteria for Base Image Selection__</ins>

- **Core Functionality:** Ensure that the base image provides the essential features and functionalities required for your application.
- **Known Vulnerabilities:** Investigate the number of known vulnerabilities associated with the base image.
- **Rebuild Frequency:** Consider how often the base image is rebuilt.
- **Package Count:** Evaluate the number of packages included in the base image. A minimal image with only essential packages can reduce the attack surface and improve performance.
- **Update Frequency and Security Hygiene:** Examine the update frequency and overall security practices of the underlying distribution.
- **Maintainer Support:** Assess the level of support provided by the maintainers of the base image.
- **Image Size:** Consider the size of the base image in megabytes (MB).
- **Image Signing:** Check whether the base image is signed. Signed images provide an additional layer of security.
- **Software Bill of Materials (SBOM):** Determine if the base image includes a Software Bill of Materials (SBOM).

After reading this section, Software professionals will have a mental checklist that makes them better prepared to select an appropriate base image for container-based software applications. 

## Ensure the base image contains needed core functionality

First and foremost, the base image needs to contain the necessary minimum functionality. For instance, for a team that is developing a Python application, this would include the Python runtime, the software that translates source code into machine code. Without the appropriate core functionality, the base image will be unable to serve the needs of the software developer and his or her application. More technical users might also be interested in aspects such as whether there is glibc or musl support.

## Choose an image with few or no known vulnerabilities

Another key factor is the number of known vulnerabilities associated with the packages inside the image. Popular open source scanners such as [`trivy`](https://github.com/aquasecurity/trivy) and [`grype`](https://github.com/anchore/grype) allow a user to scan container images to identify vulnerabilities. Known vulnerabilities, consistently ranked a [critical security threat](https://owasp.org/www-project-top-ten/) for web applications, allow attackers to exploit a piece of software without the work of discovering a previously unknown vulnerability. Recent empirical software security [research](https://decan.lexpage.net/files/EMSE-2021.pdf) indicates that many popular images have hundreds of known vulnerabilities.

Software teams should prioritize base images with the fewest known vulnerabilities. This practice not only enhances security but also minimizes the burden of manual vulnerability triage—determining whether a vulnerability is a true positive or false positive and assessing its exploitability within the context of the deployed application.

While some specialists point out that many reported vulnerabilities have never been known to be exploited [in the wild](https://www.cisa.gov/known-exploited-vulnerabilities), this observation should not be mistaken as an invitation to disregard vulnerability counts. Because many, perhaps most, compromises are never reported, any list of vulnerabilities known to have been exploited should be treated as imperfect knowledge. Other vulnerabilities might have been exploited in the wild and no defender knows yet. In short, maintaining a low known vulnerability count reduces security risk and staff toil, thereby enabling faster development.

Chainguard focuses on providing secure container images with a commitment to minimizing known vulnerabilities (CVEs). To know more, please visit [Vulnerability Comparisons in popular external images compared to Chainguard Images](https://edu.chainguard.dev/chainguard/chainguard-images/vuln-comparison/)

## Choose an image that is frequently rebuilt

While selecting a base image with a low vulnerability count is essential, it is important to recognize that this does not guarantee a continued low vulnerability count over time. New vulnerabilities can emerge, existing non-security bugs may be patched, and new features can be added to the various packages within a base image. To ensure that software teams can benefit from the latest fixes—whether security-related or otherwise—developers should prioritize images that are rebuilt frequently.

Frequent rebuilding involves using the latest versions of all constituent packages, which not only reduces the overall vulnerability count but also allows downstream users of the base image to upgrade to newer versions as needed. This practice is crucial for maintaining a secure and up-to-date development environment.

Research indicates that over half of the container images available on Docker Hub, a popular repository for container images, have not been updated in four months or longer. Similarly, official Docker images can exhibit slow update cadences. Therefore, when selecting a base image, software teams should closely examine the update frequency to ensure they are using images that are actively maintained and regularly refreshed.

## Choose an image with a minimal number of packages

Choosing base images with a minimal number of packages is also a sensible principle. This reduces the “attack surface” and also reduces complexity. Fewer packages, all things equal, means fewer vulnerabilities (both known and unknown). Additionally, for teams that must use a pinned imaged and thus can’t take advantage of frequent rebuilds, fewer packages also means a slower vulnerability accumulation rate.

Additionally, choosing [“distroless”](/software-security/videos/distroless/) images, which strips out package managers, package manager dependencies, and other build-time dependencies, is another way to ensure that your team is choosing a secure-by-default base image.

Many Chainguard Images are [distroless](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started-distroless/); they contain only an open-source application and its runtime dependencies. These images do not even contain a shell or package manager. Chainguard Images are built with [Wolfi](https://edu.chainguard.dev/open-source/wolfi/overview), our Linux undistro designed to produce container images that meet the requirements of a secure software supply chain.

## Choose an image based on a software distribution that prioritizes package update frequency and security hygiene

The packages inside a container are often sourced from a Linux distribution such as Debian, Ubuntu, or [Wolfi](/open-source/wolfi/overview/). Consequently, the update frequency and overall security of a container image are closely tied to the software development practices and policies of the underlying distribution. Therefore, it is crucial for software teams to evaluate the distribution that supplies the packages in their images.By choosing a distribution that prioritizes frequent updates and has robust security practices, teams can enhance the security and reliability of their containerized applications. This proactive approach helps ensure that vulnerabilities are addressed swiftly, reducing the risk of exploitation in production environments.

Chainguard Images are regularly updated. To Know more, Please visit our [Images directory](https://images.chainguard.dev/) and look for __last changed__ of any images.

## Choose an image with maintainers that actively support it

Not all container images are actively maintained. Like open source software packages in general, container images require one or more persons to ensure timely and frequent rebuilds, manage broader security concerns, and respond to bugs and issues. Unmaintained or lightly maintained images can pose a problem to software teams that want to prioritize development velocity and security. Without the ability to rapidly work with upstream image maintainers, software teams must either accept the risk of using old versions of the image that potentially have unpatched bugs, or consider creating and maintaining a fork with the overhead associated with that course of action.

## Choose an image that is smaller

Choosing smaller images (fewer MBs) offers multiple benefits, including reduced storage and transmission costs, faster deployment times, and improved performance. Software teams can effectively leverage smaller images to enhance their development and deployment processes while maintaining cost efficiency. This strategic approach is particularly important in today's cloud-driven environments, where every MB saved can contribute to significant savings and improved operational efficiency.

## Choose an image that is signed

Software signing ensures that attackers that tamper with a software artifact, such as a container image, can be detected. Software teams should choose to use container images that have been signed, with tools such as [Cosign](/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/), and verify the signatures to ensure that the images on which they depend are tamper-free.

All Chainguard Images contain verifiable signatures. To Know more, Please visit our [Images directory](https://images.chainguard.dev/) and look for __Provenance__ of any images.

## Choose an image with an SBOM

A [Software bill of materials](/open-source/sbom/what-is-an-sbom/) (SBOM), a list of ingredients for a piece of software, provides visibility into the components of a piece of software, enabling transparency and informed decision-making. Choosing base images with SBOMs generated by the party responsible for building the artifact helps the image consumer make better-informed decisions related to the security and health of the code.

All Chainguard Images contain high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within. To Know more, Please visit our [Images directory](https://images.chainguard.dev/) and look for __SBOM__ of any images.

## Self-assessment

<details>
  <summary>
   [True or False] The frequency at which a container image is rebuilt does not affect the number of known software vulnerabilities associated with the container image.
  </summary>
False: Infrequently rebuilt images accumulate vulnerabilities as new vulnerabilities are discovered for the packages inside an image.
</details>

<details>
  <summary>
   [True or False] Choosing base images with few or no known vulnerabilities reduces security risk and reduces staff toil.
  </summary>
True: Fewer known vulnerabilities, all things equal, makes the attacker's job harder and reduces the vulnerability triage burden on security teams and developers.
</details>

<br/>

> [!TIP]
> For those seeking examples of container images that meet the criteria outlined above, [Chainguard Images](https://github.com/chainguard-images) presents a compelling option.

