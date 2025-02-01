---
title: "Differences Between Distroless and -dev Images"
linktitle: "Distroless vs. -dev Images"
aliases:
- /chainguard/chainguard-images/differences-development-production/
- /chainguard/chainguard-images/about/differences-development-production/
- /chainguard/chainguard-images/about/differences-distroless-dev/
type: "article"
description: "Learn about the differences between distroless and -dev Chainguard Images"
date: 2024-11-01T07:52:00+02:00
lastmod: 2025-01-17T07:52:00+02:00
draft: false
tags: ["Chainguard Images", "Product", ]
images: []
menu:
  docs:
    parent: "about"
weight: 020
toc: true
---

Chainguard Images follow a distroless philosophy, meaning that only software absolutely necessary for a specific workload is included in an image. For this reason, most Chainguard Images come in two variants:

- **Distroless**: Chainguard's [distroless](/chainguard/chainguard-images/about/getting-started-distroless/) images provide a runtime for production workloads. Designed to be as minimal as possible, distroless images do not contain package managers such as apk, shells such as bash, or development utilities such as Git or text editors.
- **-dev**: `-dev`  images, so named because they are tagged `:latest-dev`, are designed for development tasks such as building, testing, or debugging. They can be used to build software artifacts that are then copied into distroless images as part of a multi-stage build, or to test workflows interactively in an environment similar to a distroless image. `-dev` images contain familiar utilities such as package managers and shells. While our distroless images have advantages related to security, `-dev` images are also secure and production-ready.

While we encourage you to use distroless images in your live deployments, `-dev` images are useful for many parts of the development lifecycle. This article explains some of the key differences between these variants and outlines ways they come together in creating a secure deployment.

## Distroless Image Security

Our distroless images have the following advantages:

- Distroless images contain fewer packages. While Chainguard moves quickly to patch CVEs in all images, distroless images still experience fewer CVEs overall. Reducing the number of packages also reduces the potential number of unknown vulnerabilities that might apply to an image.
- Not all executables are created equal. Shells such as bash, package managers such as apk, and communication-ready utilities such as Git and cURL are general-purpose tools that are broadly exploitable.
- A smaller image can use fewer resources and reduce deployment time. In some cases, especially with images that are already large, a smaller version can make a deployment more stable or robust.
- Removing unnecessary components increases the observability and transparency of the image. Reducing the number of components can also facilitate risk assessment or post-incident reporting.


## Using `-dev` Images

 While distroless images can be considered to have advantages for security, the `-dev` variants of Chainguard Images also feature few-to-zero CVEs, include useful attestations such as SLSA provenance and SBOMs, and follow other security best practices. You should feel comfortable using these secure images in production if they better fit your use case.

Though we encourage the use of distroless images in your final deployment, `-dev` images have many use cases. These include:

- **Building**: In many Dockerfile builds, you will need to generate software artifacts such as static binaries or virtual environments as part of the build process. `-dev` images are ideal for this use case, and after generation artifacts can be copied to a distroless image for use. Check out [How to Port a Sample Application to Chainguard Images](/chainguard/migration/porting-apps-to-chainguard/) for a detailed example.
- **Debugging**: Our `-dev` images contain a number of useful utilities, but are otherwise designed to be as close as possible to the distroless variant. This makes them useful for debugging, since you can test out build steps or the build environment using interactive shells and package managers. Refer to our article on [Debugging Distroless Images](/chainguard/chainguard-images/troubleshooting/debugging-distroless-images/#1-using-dev--debug-image-variants) for more on this use case.
- **Training**: In the case of AI images, you can use a `-dev` variant to train a model, then run the model in inference using a distroless image.
- **Deploying**: Though we encourage you to use our distroless images in your live deployment where possible, our `-dev` images similarly have few-to-zero CVEs and are suitable for production.

## Special Considerations

It’s likely already clear that switching to Chainguard's distroless images requires a few changes in development and deployment. Here are a few additional considerations:

* Since we don’t include general-purpose shells in our distroless images, the entrypoint to these images will vary by each image’s use case. Check the documentation for each image, and note that Dockerfile commands such as `CMD` will be directed to the image-specific entrypoint. Because we aim to keep our `-dev` images as close as possible to our distroless images, these changes to the entrypoint also affect `-dev` images.
* Chainguard Images use a less privileged user by default. When using our -dev` images, you will need to explicitly access the image with the root user — such as by including the `--user root` option — to perform tasks such as installing packages with apk.

## Conclusion

If you're just starting out, using Chainguard's distroless images can be an adjustment. Our `-dev`images provide options and flexibility as you secure your production infrastructure. `-dev` images are also secure and ready for use in production.

### Resources

* [Blog: Minimal container images: Towards a more secure future](https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future)
* [Chainguard Academy: Overview of Chainguard Images](/chainguard/chainguard-images/overview#why-distroless)
* [Chainguard Academy: Debugging Distroless Images](/chainguard/chainguard-images/debugging-distroless-images/)