---
title: "Overview of Chainguard Containers"
linktitle: "Overview"
type: "article"
description: "Learn about Chainguard Containers, distroless images, and how they provide enhanced security through minimal attack surface and comprehensive supply chain features."
lead: "Chainguard Containers are security-hardened container images built with a distroless approach, containing only essential application components and runtime dependencies."
date: 2022-09-01T08:49:31+00:00
lastmod: 2025-07-23T16:52:56+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 005
toc: true
---

[Chainguard Containers](https://www.chainguard.dev/chainguard-images?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement) are container images designed for enhanced security through minimalism and supply chain integrity. These images follow a distroless philosophy, containing only the application and its essential runtime dependencies, without shells, package managers, or other common utilities that can increase attack surface.

Many Chainguard Containers implement a [distroless approach](/chainguard/chainguard-images/getting-started-distroless/), which means they exclude shells, package managers, and other utilities typically found in container images. This design significantly reduces potential security vulnerabilities. For development and debugging purposes, Chainguard provides `-dev` variants that include necessary tools while maintaining security best practices. All images are built using Chainguard OS, an operating system specifically designed to meet secure software supply chain requirements.

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

To maximize the stability and re-usability of our layers, Chainguard identified, analyzed, and implemented three additional technical changes:
* Added in an additional final layer that captures frequently updated OS-level metadata
* Developed intelligent layer ordering to optimize compatibility
* Ensured sufficient layer counts to optimize parallel downloads by container clients

The primary benefit of this layered approach is that when one package changes it impacts only its particular layer, requiring only that layer to be downloaded again. Because the other layers don't need to be downloaded again, Chainguard's multi-layer container images support greater efficiency and developer velocity.

## Production and Starter Containers

Chainguard offers a collection of container images that are publicly available and don't require authentication, being free to use by anyone. We refer to these images as **Starter containers**, and they cover several use cases for different language ecosystems. Starter images are limited to the latest build of a given image, tagged as `latest` and `latest-dev`.

Production containers are enterprise-ready images that come with patch SLAs and features such as [Federal Information Processing Standard (FIPS) readiness](/chainguard/chainguard-images/images-features/fips-images/) and [unique time stamped tags](/chainguard/chainguard-images/images-features/unique-tags/). Unlike Starter containers, which are typically paired with only the latest version of an upstream package, Production containers offer specific major and minor versions of open source software. Chainguard offers two pricing options for Production containers: Per-Image Pricing and [Catalog Pricing](/chainguard/chainguard-images/about/pricing/).

You can access our container images directly from [Chainguard's registry](/chainguard/chainguard-registry/overview/). Chainguard's registry provides public access to all public Chainguard Containers, and provides customer access for Production Containers after logging in and authenticating.

For a complete list of Starter containers that are currently available, check our [Containers Directory](https://images.chainguard.dev/?category=developer). Registered users can also access all Starter and Production containers in the [Chainguard Console](https://console.chainguard.dev/?utm=docs). After logging in you will be able to find all the current Starter containers in the **Public containers** tab. If you've selected an appropriate Organization in the drop-down menu above the left hand navigation, you can find your organization's Production containers in the **Organization images** tab.


## Comparing Container Images

The following graph shows a comparison between the official Nginx image and Chainguard's [Nginx container image](https://images.chainguard.dev/directory/image/nginx/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-overview), based on the number of CVEs (common vulnerabilities and exposures) detected by [Grype](https://github.com/anchore/grype):

{{< rumble title="Nginx" description="Comparing the latest official Nginx image with cgr.dev/chainguard/nginx" left="nginx:latest" right="cgr.dev/chainguard/nginx:latest" >}}

The major advantage of distroless images is the reduced size and complexity, which results in a vastly reduced attack surface. This is evidenced by the results from security scanners, which detect far fewer potential vulnerabilities in Chainguard Containers.

You can review more comparisons of Chainguard Containers and external images by checking out our [Vulnerability Comparisons](/chainguard/chainguard-images/vuln-comparison/) dashboard.

`chainctl`, Chainguard's command line interface tool, comes with a useful `diff` feature that also allows you to [compare two Chainguard Containers](/chainguard/chainguard-images/how-to-use/comparing-images/).


## Architecture

By default, all Wolfi-based images are built for x86_64 (also known as AMD64) and AArch64 (also known as ARM64) architecture with the following CPU Instruction Set Architecture (ISA) baseline features:

* x86_64: x86-64-v2 (Sapphire Rapids)
* AArch64: Armv8-A with CRC and Cryptographic extensions (Neoverse V2)

Being able to provide multi-platform Chainguard Containers enables the support of more than one runtime environment, like those available on all three major clouds, AWS, GCP, and Azure. The macOS M1 and M2 chips are also based on ARM architecture. Chainguard Containers allow you to take advantage of ARM's power consumption and cost benefits.

You can confirm the available architecture of a given Chainguard Container with Crane. In this example, we'll use the latest Ruby image, but you can opt to use an alternate image.

```shell
crane manifest cgr.dev/chainguard/ruby:latest |jq -r '.manifests []| .platform'
```

Once you run this command, you'll receive output similar to the following.

```output
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


## Annotations

All Chainguard Containers include metadata in the form of *annotations* (also commonly referred to as "*labels*"). These annotations provide important information about a container image's origin, contents, and characteristics. The annotations are visible in every container image's **Specifications** tab in both the [Chainguard Console](https://console.chainguard.dev) and [Directory](https://images.chainguard.dev/), and can also be inspected programmatically using container tools.

Chainguard Containers follow the [Open Container Initiative (OCI) Image Specification](https://github.com/opencontainers/image-spec/blob/main/annotations.md) for annotations. Chainguard sets the following standard OCI annotations on its container images:

* `org.opencontainers.image.authors`: Contact details for the Chainguard Container's author (typically `Chainguard Team https://www.chainguard.dev/`)
* `org.opencontainers.image.url`: URL to the container image's Overview page in the Chainguard Directory (for example, `https://images.chainguard.dev/directory/image/nginx/overview`)
* `org.opencontainers.image.source`: URL to the source code used to build the image in the Chainguard images repository
* `org.opencontainers.image.base.digest`: The SHA256 digest of the base image used to build this container image
* `org.opencontainers.image.vendor`: The distributing organization, always set to `Chainguard`
* `org.opencontainers.image.created`: Timestamp indicating when the image was built; specifically, this annotation is calculated from the build time of the most recently built package within the container image

In addition to the standard OCI annotations, Chainguard sets custom annotations (which begin with `dev.chainguard` instead of `org.opencontainers`) that provide additional context about the container image. However, the `dev.chainguard` labels are an internal implementation detail that support Chainguard platform features. They are not set universally across all Chainguard Containers and can change from time to time. 

### Retrieving annotation information

You can inspect a Chainguard Container's annotations using the `docker inspect` command. The following example uses [`jq`](https://jqlang.org/), a command-line JSON processor, to filter the output to only show the `apko` image's annotations:

```shell
docker pull cgr.dev/chainguard/apko:latest
docker inspect cgr.dev/chainguard/apko:latest | jq '.[].Config.Labels'
```

This will output all the annotations set on the image:

```output
{
  "dev.chainguard.package.main": "apko",
  "org.opencontainers.image.authors": "Chainguard Team https://www.chainguard.dev/",
  "org.opencontainers.image.created": "2025-10-14T09:49:49Z",
  "org.opencontainers.image.source": "https://github.com/chainguard-images/images/tree/main/images/apko",
  "org.opencontainers.image.url": "https://images.chainguard.dev/directory/image/apko/overview",
  "org.opencontainers.image.vendor": "Chainguard"
}
```

You can also inspect image annotations using [`crane`](https://github.com/google/go-containerregistry/tree/main/cmd/crane):

```shell
crane config cgr.dev/chainguard/apko:latest | jq '.config.Labels'
```

This returns the same annotation information as the `docker inspect` command, but without requiring you to download the container image beforehand.

### Adding container image annotations

OCI labels are specific to a container image, not to an entire layer. This means that for base images, annotation information is often overridden later on with more accurate details after the image has been ingested. For example, the `image.author` annotation might be reset to reflect the customer consuming the container image.

Some users relabel their container images after they've been ingested. As an example, it may make sense add an annotation like `com.mycompany.image.source=chainguard` to your Chainguard Containers; this would allow you to filter for all the container images provided by Chainguard at `mycompany`. 

Some package mirroring tools support this functionality, but we recommend using Chainguard's [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/) tool to add custom annotations to your Chainguard Containers. Refer to our guide on [managing Custom Assembly resources with `chainctl`](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/#adding-custom-annotations-with-custom-assembly) for more information.
