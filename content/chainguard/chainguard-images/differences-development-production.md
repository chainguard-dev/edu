---
title: "Differences Between Development and Production Images"
linktitle: " Dev vs. Production Images"
type: "article"
description: "Learn about the differences between development and production Chainguard Images"
date: 2024-11-01:07:52+02:00
lastmod: 2024-11-01:07:52+02:00
draft: false
tags: ["Chainguard Images", "Product", ]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 605
toc: true
---

Chainguard Images follow a distroless philosophy, meaning that only software absolutely necessary for a specific workload is included in an image. For this reason, most Chainguard Images come in two variants:

- **Production**: These images provide a runtime for production workloads. Designed to be as minimal as possible, production images do not contain package managers such as apk, shells such as b/a/sh, or development utilities such as Git or text editors. Production Chainguard Images are tagged `:latest`.  
- **Development**: These images are designed for development tasks such as building, testing, or debugging. They can be used to build software artifacts that are then copied into production images as part of a multi-stage build, or to test workflows interactively in an environment similar to a production image. Development images contain familiar utilities such as package managers and shells. While our production images have advantages related to security, development images are also secure and production-ready. Development images are tagged `:latest-dev`.

While we encourage you to use production images in your live deployments, development images are useful for many parts of the dev lifecycle. This article explains some of the key differences between these variants and outlines ways these variants come together in creating a secure deployment.

## Production Image Security

Our production images have the following advantages:

- Production images contain fewer packages. While Chainguard moves quickly to patch CVEs in all images, production images still experience fewer CVEs overall. Reducing the number of packages also reduces the potential number of unknown vulnerabilities that might apply to an image.  
- Not all executables are created equal. Shells such as bash, package managers such as apk, and communication-ready utilities such as Git and curl are general-purpose tools that are broadly exploitable.  
- A smaller image can use fewer resources and reduce deployment time. In some cases, especially with already-large images, a smaller version can make a deployment more stable or robust.  
- Removing unnecessary components increases the observability and transparency of the image. Reducing the number of components can facilitate risk assessment or post-incident reporting.

While our production images can be considered to have advantages for security, the development variants of Chainguard Images are also low-to-no CVE, include useful attestations such as SLSA provenance and SBOMs, and follow other security best practices. You should feel comfortable using these secure images in production if they better fit your use case.

## Using Development Images

Though we encourage the use of production images in your final deployment, development images have many use cases. These include:

- **Building**: In many Dockerfile builds, you will need to generate software artifacts such as static binaries or virtual environments as part of the build process. Development images are ideal for this use case, and after generation artifacts can be copied to a production image for use. See [How to Port a Sample Application to Chainguard Images]](/chainguard/migration/porting-apps-to-chainguard/) for a detailed example.
- **Debuging**: Our development images contain a number of useful utilities, but are otherwise designed to be as close as possible to the production variant. This makes them useful for debugging, since you can test out build steps or the build environment using interactive shells and package managers. See [Debugging Distroless Images](/chainguard/chainguard-images/debugging-distroless-images/) for more on this use case.
- **Training**: In the case of AI images, you can use a development variant to train a model, then run the model in inference using a production image.  
- **Deploying**: Though we encourage you to use our production images in your live deployment where possible, our development images are low-to-no CVE and are suitable for production.

## Special Considerations

It’s likely already clear that switching to our production images requires a few changes in development and deployment. Here are a few additional considerations:

* Since we don’t include general-purpose shells in our production images, the entrypoint to these images will vary by each image’s use case. Check the documentation for each image, and note that Dockerfile commands such as `CMD` will be directed to the image-specific entrypoint. Because we aim to keep our development images as close as possible to our production images, these changes to entrypoint also affect development images.  
* Chainguard Images use a less privileged user by default. When using our development images, you will need to explicitly access the image with the root user — such as by using the `--user root` option — to perform tasks such as installing packages with apk.

## Conclusion

Taking the step into distroless by using our production Chainguard Images can be an adjustment. Our development images provide options and flexibility as you secure your production infrastructure. Development images are also secure and ready for use in production.

## Resources

* [Blog: Minimal container images: Towards a more secure future](https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future)  
* [Chainguard Academy: Overview of Chainguard Images](/chainguard/chainguard-images/overview#why-distroless)  
* [Chainguard Academy: Debugging Distroless Images](https://edu.chainguard.dev/chainguard/chainguard-images/debugging-distroless-images/)

