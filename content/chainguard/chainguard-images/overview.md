---
title: "Overview of Chainguard Images"
linktitle: "Overview"
type: "article"
description: "Chainguard Images Overview"
lead: "A primer on Chainguard Images and the distroless approach"
date: 2022-09-01T08:49:31+00:00
lastmod: 2022-09-01T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Product", "Overview"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 100
toc: true
---

[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) is a collection of container images designed for security and minimalism.

Many of the images are distroless; they contain only an application and its runtime dependencies. These images do not even contain a shell or package manager.

Chainguard Images are built with [Wolfi](/open-source/wolfi/overview), our Linux _undistro_ designed from the ground up to produce container images that meet the requirements of a secure software supply chain.

Main features include:

- Minimalist design, no bloating from unnecessary software
- High quality build-time SBOMs (software bill of materials) attesting the provenance of all artifacts within the image
- Verifiable signatures provided by [Sigstore](/open-source/sigstore/cosign/an-introduction-to-cosign/)
- Automated nightly builds to ensure images are completely up-to-date and contain all available security patches
- Reproducible builds with Cosign and apko ([read more about reproducibility](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds))

Chainguard Images are available from the [Chainguard Registry](/chainguard/chainguard-images/registry/overview/) and can be pulled from `cgr.dev`. You can review images files [on GitHub](https://github.com/chainguard-images).

## Why Distroless

[Distroless images](https://blog.chainguard.dev/minimal-container-images-towards-a-more-secure-future/) are the result of pushing minimalism in containers to the next level. When compared to traditional base images such as [Alpine](https://hub.docker.com/_/alpine) or [Debian](https://hub.docker.com/_/debian), they are more stripped back, lacking even a shell or package managers. However, compared to the empty “scratch” image, they do contain structure essential for the majority of Linux applications such as root certificates for TLS and core files like `/etc/passwd`.

## Comparing Images

The following graph shows a comparison between the official Nginx image and Chainguard's [Nginx image](/chainguard/chainguard-images/reference/nginx/overview/), based on the number of CVEs (common vulnerabilities and exposures) detected by [Grype](https://github.com/anchore/grype):

{{< rumble title="Nginx" description="Comparing the latest official Nginx image with cgr.dev/chainguard/nginx" left="nginx:latest" right="cgr.dev/chainguard/nginx:latest" >}}

The major advantage of distroless images is the reduced size and complexity, which results in a vastly reduced attack surface. This is evidenced by the results from security scanners, which detect far fewer potential vulnerabilities in Chainguard Images.

You can review more comparisons of Chainguard Images and external images by checking out our [Vulnerability Comparisons](/chainguard/chainguard-images/vuln-comparison/) dashboard.

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

You can read more about our support of ARM64 in our blog on [Building Wolfi from teh ground up](https://www.chainguard.dev/unchained/building-wolfi-from-the-ground-up-and-announcing-arm64-support).