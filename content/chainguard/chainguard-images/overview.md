---
title: "Overview of Chainguard Containers"
linktitle: "Overview"
type: "article"
description: "Chainguard Containers Overview"
lead: "A primer on Chainguard Containers and the distroless approach"
date: 2022-09-01T08:49:31+00:00
lastmod: 2025-05-27T08:49:31+00:00
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

Many Chainguard Containers are [distroless](/chainguard/chainguard-images/getting-started-distroless/); they contain only an open-source application and its runtime dependencies. These images do not even contain a shell or package manager, and are often paired with an equivalent development variant (sometimes referred to as a `dev` variant) that allows further customization, for build and debug purposes. Chainguard Containers are built with Chainguard OS, designed from the ground up to produce container images that meet the requirements of a secure software supply chain.

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

## Why Multi-Layer Container Images

Chainguard originally took a single-layer approach to container images built [with apko](/open-source/build-tools/apko/getting-started-with-apko/) in order to offer simplicity and clarity. However, in an effort to deliver better stability, security, and efficiency for larger and more complex applications, Chainguard introduced multi-layer container images in May 2025. This approach leverages container runtime caching so that a layer used by multiple images does not need to be downloaded more than once, and you don't need to download the whole image each time there is an update on one layer.

Chainguard's approach to layering is a "per-origin" strategy, where packages that derive from the same upstream source are grouped in the same layer because they tend to receive updates together. 

We observed that this approach achieved the following:
* A ~70% reduction in the total size of unique layer data across our image catalog compared to the single-layer approach
* A 70-85% reduction in the cumulative bytes transferred when simulating sequential pulls of updated images like PyTorch and NeMo

To maximize the stability and re-useability of our layers, Chainugard identified, analyzed, and implemented three additional technical changes:
* Added in additional final layer that captures frequently updated OS-level metadata
* Developed intelligent layer ordering to optimize compatibility 
* Ensured sufficient layer counts to optimize parallel downloads by container clients 

The primary benefit of this layered approach is that when one package changes only its particular layer is affected, and all the other layers don't need to be re-downloaded, supporting greater efficiency and developer velocity.

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
