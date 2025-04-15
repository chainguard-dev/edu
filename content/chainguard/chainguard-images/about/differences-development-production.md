---
title: "Understanding Chainguard's Container Variants"
linktitle: "Container Variants"
aliases:
- /chainguard/chainguard-images/differences-development-production/
- /chainguard/chainguard-images/about/differences-development-production/
type: "article"
description: "Learn about Chainguard's development container images and how they differ from our standard images."
date: 2024-11-01T07:52:00+02:00
lastmod: 2025-04-11T07:52:00+02:00
draft: false
tags: ["CHAINGUARD CONTAINERS", "PRODUCT"]
images: []
menu:
  docs:
    parent: "about"
weight: 020
toc: true
---

Chainguard Containers follow a distroless philosophy, meaning that only software absolutely necessary for a specific workload is included in an image. Designed to be as minimal as possible, Chainguard's standard container images do not contain package managers such as apk, shells such as b/a/sh, or development utilities such as Git or text editors. However, this distroless approach isn't suitable for every use case. For this reason, most Chainguard Containers have what's called a *development* variant.

These variants are designed for development tasks such as building, testing, or debugging. They can be used to build software artifacts that are then copied into standard images as part of a multi-stage build, or to test workflows interactively in an environment similar to a standard image. Development images contain familiar utilities such as package managers and shells. While our standard images have advantages related to security, development images are also secure and production-ready. Development images are tagged `:latest-dev`.

To benefit from the most minimal potential attack surface, we recommend using a multi-stage build that leverages the development container image as a builder for a distroless standard container image. However, development images are useful as they are throughout the development lifecycle. This article explains some of the key features of development container variants and how they differ from our standard container images and outlines ways these variants come together in creating a secure deployment.

> **Note**: Any time this article mentions to Chainguard's "standard" container images, it's referring to our minimal, distroless container images. In the context of this article, any non-development variant is considered a "standard" container image.

## Chainguard Container Security

Chainguard's standard container images have the following advantages:

- Our standard container images contain fewer packages. While Chainguard moves quickly to patch CVEs in all images, our standard, distroless images still experience fewer CVEs overall. Reducing the number of packages also reduces the potential number of unknown vulnerabilities that might apply to an image.
- Not all executables are created equal. Shells such as bash, package managers such as apk, and communication-ready utilities such as Git and curl are general-purpose tools that are broadly exploitable.
- A smaller image can use fewer resources and reduce deployment time. In some cases, especially with already-large images, a smaller version can make a deployment more stable or robust.
- Removing unnecessary components increases the observability and transparency of the image. Reducing the number of components can facilitate risk assessment or post-incident reporting.

While our standard images can be considered to have advantages for security, the development variants of Chainguard Containers are also low-to-no CVE, include useful attestations such as SLSA provenance and SBOMs, and follow other security best practices. You should feel comfortable using these secure development images in production if they better fit your use case.

## Using Development Images

Though using Chainguard's standard container images in your final deployment will give you the benefits of distroless, development images have many use cases. These include:

- **Building**: In many Dockerfile builds, you will need to generate software artifacts such as static binaries or virtual environments as part of the build process. Development images are ideal for this use case, and after these artifacts have been generated they can be copied to a standard image for use. See [How to Port a Sample Application to Chainguard Containers](/chainguard/migration/porting-apps-to-chainguard/) for a detailed example.
- **Debugging**: Our development images contain a number of useful utilities, but are otherwise designed to be as close as possible to the standard variant. This makes them useful for debugging, since you can test out build steps or the build environment using interactive shells and package managers. See [Debugging Distroless Images](/chainguard/chainguard-images/debugging-distroless-images/) for more on this use case.
- **Training**: In the case of AI images, you can use a development variant to train a model, then run the model in inference using a standard image.
- **Deploying**: Development images are low-to-no CVE and are suitable for production.

## Special Considerations

It’s likely already clear that switching to our standard images requires a few changes in development and deployment. Here are a few additional considerations:

* Since we don’t include general-purpose shells in most standard container images, the entrypoint to these images will vary by each image’s use case. Check the documentation for each image, and note that Dockerfile commands such as `CMD` will be directed to the image-specific entrypoint. Because we aim to keep our development images as close as possible to our standard images, these changes to entrypoint also affect development container images.
* Chainguard Containers use a less privileged user by default. When using our development images, you will need to explicitly access the image with the root user — such as by using the `--user root` option — to perform tasks such as installing packages with apk.

## Conclusion

Taking the step into distroless by using our standard Chainguard Containers can be an adjustment. Our development images provide options and flexibility as you secure your production infrastructure. Development images are also secure and ready for use in production.

## Resources

* [Blog: Minimal container images: Towards a more secure future](https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future)
* [Chainguard Academy: Overview of Chainguard Containers](/chainguard/chainguard-images/overview#why-distroless)
* [Chainguard Academy: Debugging Distroless Images](/chainguard/chainguard-images/debugging-distroless-images/)