---
title: "Overview of Chainguard Images"
linktitle: "Overview"
type: "article"
description: "Chainguard Images Overview"
lead: "A primer on Chainguard Images and the distroless approach"
date: 2022-09-01T08:49:31+00:00
lastmod: 2024-04-30T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Product", "Overview"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 010
toc: true
---

[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) are a collection of container images designed for security and minimalism. 

Many Chainguard Images are distroless; they contain only an open-source application and its runtime dependencies. These images do not even contain a shell or package manager. Chainguard Images are built with [Wolfi](/open-source/wolfi/overview), our Linux _undistro_ designed from the ground up to produce container images that meet the requirements of a secure software supply chain.

The main features of Chainguard Images include:

- Minimalist design, with no unnecessary software bloat
- Automated nightly builds to ensure Images are completely up-to-date and contain all available security patches
- [High quality build-time SBOMs](/chainguard/chainguard-images/working-with-images/retrieve-image-sboms/) (software bill of materials) attesting the provenance of all artifacts within the Image
- [Verifiable signatures](/chainguard/chainguard-images/working-with-images/retrieve-image-sboms/) provided by [Sigstore](/open-source/sigstore/cosign/an-introduction-to-cosign/)
- Reproducible builds with Cosign and apko ([read more about reproducibility](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds))

Chainguard Images are available from the [Chainguard Registry](/chainguard/chainguard-registry/overview/) and can be pulled from `cgr.dev`. You can review images files [on GitHub](https://github.com/chainguard-images) and can find complete lists of available Chainguard Images in the [public Images Directory](https://images.chainguard.dev/) or within the [Chainguard Console](https://console.enforce.dev/). 


## Why Minimal Container Images

The fewer dependencies a given piece of software uses, the lower likelihood that it will be impacted by CVEs. By minimizing the number of dependencies and thus reducing their potential attack surface, Chainguard Images inherently contain few to zero CVEs. Chainguard Images are rebuilt nightly to ensure they are completely up-to-date and contain all available security patches. With this nightly build approach, our engineering team sometimes [fixes vulnerabilities before they’re detected](https://www.chainguard.dev/unchained/how-chainguard-fixes-vulnerabilities?utm_source=docs).

Note that there is often a `-dev` variant of each Chainguard Image available. For example, the `-dev` variant of the `mariadb:latest` Image is `mariadb:latest-dev`. These images typically contain a shell and tools like a package manager to allow users to more easily debug and modify the image. We recommend for production environments that you use Chainguard's `-dev` Images in a multi-stage Docker build; this will allow you to use a `-dev` variant image as a builder container, and then promote that build to an image that removes anything unnecessary.


## Why Distroless

[Distroless images](/chainguard/chainguard-images/getting-started-distroless/) are the result of pushing minimalism in containers to the next level. When compared to traditional base images such as [Alpine](https://hub.docker.com/_/alpine) or [Debian](https://hub.docker.com/_/debian), they are more stripped back, lacking even a shell or package managers. However, compared to the empty “scratch” image, they do contain structure essential for the majority of Linux applications such as root certificates for TLS and core files like `/etc/passwd`.

[Wolfi](https://github.com/wolfi-dev) is a community Linux distribution developed by Chainguard for the container and cloud-native era. Chainguard started the Wolfi project to enable building Chainguard Images, which required a Linux distribution with components at the appropriate granularity and with support for [glibc](https://www.gnu.org/software/libc/). 

### A Note about Wolfi packages

Chainguard Images only contain packages that come from the Wolfi Project or those that are built and maintained internally by Chainguard. As of March of 2024, Chainguard will maintain one version of each Wolfi package at a time. These will track the latest version of the upstream software in the package. Chainguard offers patch support only for the latest version of the upstream software in the package. Existing packages will not be removed from Wolfi and you may continue to use them, but be aware that older packages will no longer be updated and will accrue vulnerabilities over time. The tools we use to build packages and images remain freely available and open source in [Wolfi](https://github.com/wolfi-dev).

This change ensures that Chainguard can provide the most up-to-date patches to all packages for our Images users. Note that specific package versions can be made available in Production Images. If you have a request for a specific package version, please [contact support](https://www.chainguard.dev/contact?utm=docs).


## Production and Developer Images

There are two different tracks of Chainguard Images: Production Images and Developer Images. Developer Images are publicly available and free to use by anyone. Developer Images always represent images tagged with `:latest` or `:latest-dev`. 

Production Images are enterprise-ready images that come with patch SLAs and features such as [Federal Information Processing Standard (FIPS) readiness](/chainguard/chainguard-images/images-features/fips-images/) and [unique time stamped tags](/chainguard/chainguard-images/images-features/unique-tags/). There are also specific major and minor versions of open source software available as Production Images. 

You can access Images directly from the [Chainguard Registry](/chainguard/chainguard-registry/overview/). The Chainguard Registry provides public access to all public Chainguard Images, and provides customer access for Production Images after logging in and authenticating.

You can find complete lists of all the Developer and Production Images available to you in [the Chainguard Console](https://console.enforce.dev/?utm=docs). After logging in you will be able to find all the current Developer Images in the **Public images** tab. If you've selected an appropriate Organization in the drop-down menu above the left hand navigation, you can find your organization's Production Images in the **Organization images** tab.


## Comparing Images

The following graph shows a comparison between the official Nginx image and Chainguard's [Nginx image](https://images.chainguard.dev/directory/image/nginx/overview), based on the number of CVEs (common vulnerabilities and exposures) detected by [Grype](https://github.com/anchore/grype):

{{< rumble title="Nginx" description="Comparing the latest official Nginx image with cgr.dev/chainguard/nginx" left="nginx:latest" right="cgr.dev/chainguard/nginx:latest" >}}

The major advantage of distroless images is the reduced size and complexity, which results in a vastly reduced attack surface. This is evidenced by the results from security scanners, which detect far fewer potential vulnerabilities in Chainguard Images.

You can review more comparisons of Chainguard Images and external images by checking out our [Vulnerability Comparisons](/chainguard/chainguard-images/vuln-comparison/) dashboard.

`chainctl`, Chainguard's command line interface tool, comes with a useful `diff` feature that also allows you to [compare two Chainguard Images](/chainguard/chainguard-images/comparing-images/comparing-images/).  


## Architecture

By default, all Wolfi-based images are built for x86_64 (also known as AMD64) and AArch64 (also known as ARM64) architectures. Being able to provide multi-platform Chainguard Images enables the support of more than one runtime environment, like those available on all three major clouds, AWS, GCP, and Azure. The macOS M1 and M2 chips are also based on ARM architecture. Chainguard Images allow you to take advantage of ARM's power consumption and cost benefits.

You can confirm the available architecture of a given Chainguard Image with Crane. In this example, we'll use the latest Ruby image, but you can opt to use an alternate image.

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

This verifies that the Ruby Chainguard Image is built for both AMD64 and ARM64 architectures.

You can read more about our support of ARM64 in our blog on [Building Wolfi from the ground up](https://www.chainguard.dev/unchained/building-wolfi-from-the-ground-up-and-announcing-arm64-support?utm=docs).
