---
title: "Overview of Chainguard Containers"
linktitle: "Overview"
type: "article"
description: "Chainguard Containers Overview"
lead: "A primer on Chainguard Containers and the distroless approach"
date: 2022-09-01T08:49:31+00:00
lastmod: 2025-04-07T08:49:31+00:00
draft: false
tags: ["Chainguard Containers", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 010
toc: true
---

[Chainguard Containers](https://www.chainguard.dev/chainguard-images?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement) are a collection of container images designed for security and minimalism.

Many Chainguard Containers are [distroless](/chainguard/chainguard-images/getting-started-distroless/); they contain only an open-source application and its runtime dependencies. These images do not even contain a shell or package manager, and are often paired with an equivalent development variant (sometimes referred to as a `dev` variant) that allows further customization, for build and debug purposes. Chainguard Containers are built with [Wolfi](/open-source/wolfi/overview), our Linux _undistro_ designed from the ground up to produce container images that meet the requirements of a secure software supply chain.

The main features of Chainguard Containers include:

- Minimal design, with no unnecessary software bloat
- Automated nightly builds to ensure container images are completely up-to-date and contain all available security patches
- [High quality build-time SBOMs](/chainguard/chainguard-images/working-with-images/retrieve-image-sboms/) (software bill of materials) attesting the provenance of all artifacts within the container image
- [Verifiable signatures](/chainguard/chainguard-images/working-with-images/retrieve-image-sboms/) provided by [Sigstore](/open-source/sigstore/cosign/an-introduction-to-cosign/)
- Reproducible builds with Cosign and apko ([read more about reproducibility](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds))

Chainguard Containers are primarily available from [Chainguard's registry](/chainguard/chainguard-registry/overview/), but a selection of developer images is also available on [Docker Hub](https://hub.docker.com/u/chainguard). You can find the complete list of available Chainguard Containers in our public [Containers Directory](https://images.chainguard.dev/?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-overview) or within the [Chainguard Console](https://console.chainguard.dev/).


## Why Minimal Container Images

The fewer dependencies a given piece of software uses, the lower likelihood that it will be impacted by CVEs. By minimizing the number of dependencies and thus reducing their potential attack surface, Chainguard Containers inherently contain few to zero CVEs. Chainguard Containers are rebuilt nightly to ensure they are completely up-to-date and contain all available security patches. With this nightly build approach, our engineering team sometimes [fixes vulnerabilities before they’re detected](https://www.chainguard.dev/unchained/how-chainguard-fixes-vulnerabilities?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement).

Note that there is often a development variant of each Chainguard Container available. These are sometimes called the `-dev` variant, as their tags include the `-dev` suffix (as in `:latest-dev`). For example, the development variant of the `mariadb:latest` container image is `mariadb:latest-dev`. These container images typically contain a shell and tools like a package manager to allow users to more easily debug and modify the image.

## Distroless and Wolfi

[Distroless images](/chainguard/chainguard-images/getting-started-distroless/) are the result of pushing minimalism in containers to the next level. When compared to traditional base images such as [Alpine](https://hub.docker.com/_/alpine) or [Debian](https://hub.docker.com/_/debian), they are more stripped back, lacking even a shell or package managers. However, when compared to the empty "scratch" image, they do contain structure essential for the majority of Linux applications such as root certificates for TLS and core files like `/etc/passwd`. To create such images, Chainguard developed its own Linux distribution, [Wolfi](/open-source/wolfi/overview/), a reference to the world's [smallest Octopus](https://en.wikipedia.org/wiki/Octopus_wolfi).

Wolfi is a community Linux distribution developed by Chainguard for the container and cloud-native era. Chainguard started the Wolfi project to enable building Chainguard Containers, which required a Linux distribution with components at the appropriate granularity and with support for [glibc](https://www.gnu.org/software/libc/).

### A Note about Wolfi packages

Chainguard Containers only contain packages that come from the Wolfi Project or those that are built and maintained internally by Chainguard. As of March 2024, Chainguard will maintain one version of each Wolfi package at a time. These will track the latest version of the upstream software in the package. Chainguard offers patch support only for the latest version of the upstream software in the package. Existing packages will not be removed from Wolfi and you may continue to use them, but be aware that older packages will no longer be updated and will accrue vulnerabilities over time. The tools we use to build packages and images remain freely available and open source in [Wolfi](https://github.com/wolfi-dev).

This change ensures that Chainguard can provide the most up-to-date patches to all packages for our container images users. Note that specific package versions can be made available in . If you have a request for a specific package version, please [contact support](https://www.chainguard.dev/contact?utm=docs).

## Production and Starter Containers

Chainguard offers a collection of container images that are publicly available and don't require authentication, being free to use by anyone. We refer to these images as **Starter containers**, and they cover several use cases for different language ecosystems. Starter images are limited to the latest build of a given image, tagged as `latest` and `latest-dev`.

Production containers are enterprise-ready images that come with patch SLAs and features such as [Federal Information Processing Standard (FIPS) readiness](/chainguard/chainguard-images/images-features/fips-images/) and [unique time stamped tags](/chainguard/chainguard-images/images-features/unique-tags/). Unlike Starter containers, which are typically paired with only the latest version of an upstream package, Production containers offer specific major and minor versions of open source software.

You can access our container images directly from [Chainguard's registry](/chainguard/chainguard-registry/overview/). Chainguard's registry provides public access to all public Chainguard Containers, and provides customer access for Production Containers after logging in and authenticating.

For a complete list of Starter containers that are currently available, check our [Containers Directory](https://images.chainguard.dev/?category=developer). Registered users can also access all Starter and Production containers in the [Chainguard Console](https://console.chainguard.dev/?utm=docs). After logging in you will be able to find all the current Starter containers in the **Public containers** tab. If you've selected an appropriate Organization in the drop-down menu above the left hand navigation, you can find your organization's Production containers in the **Organization images** tab.


## Comparing Container Images

The following graph shows a comparison between the official Nginx image and Chainguard's [Nginx container image](https://images.chainguard.dev/directory/image/nginx/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-overview), based on the number of CVEs (common vulnerabilities and exposures) detected by [Grype](https://github.com/anchore/grype):

{{< rumble title="Nginx" description="Comparing the latest official Nginx image with cgr.dev/chainguard/nginx" left="nginx:latest" right="cgr.dev/chainguard/nginx:latest" >}}

The major advantage of distroless images is the reduced size and complexity, which results in a vastly reduced attack surface. This is evidenced by the results from security scanners, which detect far fewer potential vulnerabilities in Chainguard Containers.

You can review more comparisons of Chainguard Containers and external images by checking out our [Vulnerability Comparisons](/chainguard/chainguard-images/vuln-comparison/) dashboard.

`chainctl`, Chainguard's command line interface tool, comes with a useful `diff` feature that also allows you to [compare two Chainguard Containers](/chainguard/chainguard-images/how-to-use/comparing-images/).


## Architecture

By default, all Wolfi-based images are built for x86_64 (also known as AMD64) and AArch64 (also known as ARM64) architectures. Being able to provide multi-platform Chainguard Containers enables the support of more than one runtime environment, like those available on all three major clouds, AWS, GCP, and Azure. The macOS M1 and M2 chips are also based on ARM architecture. Chainguard Containers allow you to take advantage of ARM's power consumption and cost benefits.

You can confirm the available architecture of a given Chainguard Container with Crane. In this example, we'll use the latest Ruby image, but you can opt to use an alternate image.

```sh
crane manifest cgr.dev/chainguard/ruby:latest |jq -r '.manifests []| .platform'
```

Once you run this command, you'll receive output similar to the following.

```
{
  "architecture": "amd64",
  "os": "linux"
}
{
  "architecture": "arm64",
  "os": "linux"
}
```

This verifies that the Ruby Chainguard Container is built for both AMD64 and ARM64 architectures.

You can read more about our support of ARM64 in our blog on [Building Wolfi from the ground up](https://www.chainguard.dev/unchained/building-wolfi-from-the-ground-up-and-announcing-arm64-support?utm=docs).
