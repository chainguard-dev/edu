---
title: "Understanding Chainguard's Starter Images"
linktitle: "Starter Images"
aliases:
- /chainguard/chainguard-images/differences-development-production/
- /chainguard/chainguard-images/about/differences-development-production/
type: "article"
description: "Learn about Chainguard's Starter Images and what makes them different from our regular minimal container images."
date: 2024-11-01T07:52:00+02:00
lastmod: 2025-01-17T07:52:00+02:00
draft: false
tags: ["CHAINGUARD IMAGES", "PRODUCT", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "about"
weight: 020
toc: true
---

Chainguard Container Images follow a distroless philosophy, meaning that only software absolutely necessary for a specific workload is included in an image. Chainguard's minimal images provide a runtime for production workloads and are designed to have as few packages as possible. This means they typically do not contain package managers such as apk, shells such as bash, or development utilities such as Git or text editors.

However, there are times when an organization would prefer to run container images that do include a shell or package manager, but otherwise only contain the minimum dependencies needed to function. For cases like this, Chainguard offers its **Starter Images**. 

Starter images (sometimes referred to as `-dev` images) are designed for development tasks such as building, testing, or debugging. They can be used to build software artifacts that are then copied into minimal images as part of a multi-stage build, or to test workflows interactively in an environment similar to a minimal image. Starter images contain familiar utilities such as package managers and shells, and are tagged with `:latest-dev`. 

While we encourage you to use minimal images in your live deployments, `-dev` images are useful for many parts of the development lifecycle, and are even secure and production-ready. This article explains some of the key differences between Starter Images and Chainguard's standard minimal variants, and outlines ways they come together in creating a secure deployment.

## Minimal Images Security

Chainguard's standard minimal images have the following advantages:

- Minimal images contain fewer packages. While Chainguard moves quickly to patch CVEs in all images, minimal images still experience fewer CVEs overall. Reducing the number of packages also reduces the potential number of unknown vulnerabilities that might apply to an image.
- Not all executables are created equal. Shells such as bash, package managers such as apk, and communication-ready utilities such as Git and cURL are general-purpose tools that are broadly exploitable.
- A smaller image can use fewer resources and reduce deployment time. In some cases, especially with images that are already large, a smaller version can make a deployment more stable or robust.
- Removing unnecessary components increases the observability and transparency of the image. Reducing the number of components can also facilitate risk assessment or post-incident reporting.


## Using Starter Images

Like our minimal container images, Chainguard's Starter Images also feature few-to-zero CVEs, include useful attestations such as SLSA provenance and SBOMs, and follow other security best practices. You should feel comfortable using these secure images in production if they better fit your use case.

Though we encourage the use of minimal images in your final deployment, Starter Images have many use cases. These include:

- **Building**: In many Dockerfile builds, you will need to generate software artifacts such as static binaries or virtual environments as part of the build process. Starter Images are ideal for this use case, and after generation artifacts can be copied to a minimal image for use. Check out [How to Port a Sample Application to Chainguard Images](/chainguard/migration/porting-apps-to-chainguard/) for a detailed example.
- **Debugging**: Our Starter Images contain a number of useful utilities, but are otherwise designed to be as close as possible to the minimal variant. This makes them useful for debugging, since you can test out build steps or the build environment using interactive shells and package managers. Refer to our article on [Debugging Distroless Images](/chainguard/chainguard-images/troubleshooting/debugging-distroless-images/#1-using-dev--debug-image-variants) for more on this use case.
- **Training**: In the case of AI images, you can use a `-dev` variant to train a model, then run the model in inference using a minimal image.
- **Deploying**: Though we encourage you to use our minimal images in your live deployment where possible, our Starter Images similarly have few-to-zero CVEs and are suitable for production.

## Special Considerations

It’s likely already clear that switching to Chainguard's minimal images requires a few changes in development and deployment. Here are a few additional considerations:

* Since we don’t include general-purpose shells in our minimal images, the entrypoint to these images will vary by each image’s use case. Check the documentation for each image, and note that Dockerfile commands such as `CMD` will be directed to the image-specific entrypoint. Because we aim to keep our Starter images as close as possible to our minimal images, these changes to the entrypoint also affect the Starter variants.
* Chainguard Images use a less privileged user by default. When using our Starter images, you will need to explicitly access the image with the root user — such as by including the `--user root` option — to perform tasks such as installing packages with apk.

## Conclusion

If you're just starting out, using Chainguard's minimal images can be an adjustment. Our Starter images provide options and flexibility as you secure your production infrastructure. Starter images are also secure and ready for use in production.

### Resources

* [Blog: Minimal container images: Towards a more secure future](https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future)
* [Chainguard Academy: Overview of Chainguard Images](/chainguard/chainguard-images/overview#why-distroless)
* [Chainguard Academy: Debugging Distroless Images](/chainguard/chainguard-images/debugging-distroless-images/)