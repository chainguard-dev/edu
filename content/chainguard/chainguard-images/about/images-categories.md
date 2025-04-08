---
title: "Understanding Chainguard's Container Image Categories"
linktitle: "Image Categories"
type: "article"
description: "Reference guide outlining how Chainguard Containers are categorized."
date: 2025-04-03T11:07:52+02:00
lastmod: 2025-04-03T11:07:52+02:00
draft: false
tags: ["CONCEPTUAL", "CHAINGUARD IMAGES", "PRODUCT"]
images: []
menu:
  docs:
    parent: "about"
weight: 027
toc: true
---

Chainguard Containers are a collection of curated, distroless container images designed with a focus on software supply chain security. Chainguard's container images are designed to be slim runtimes for production environments, emphasizing security and efficiency by removing unnecessary elements. Additionally, the images are designed to be easily integrated into existing workflows, helping organizations to build better, more secure software.

Within the [Chainguard Images Directory](https://images.chainguard.dev/), Chainguard Containers are organized into five general categories (with some falling into multiple categories):

* **Starter**
* **Base**
* **Application**
* **FIPS**
* **AI**

This conceptual article will outline each of these categories in turn, including their uses as well as examples of images from each category. It will also highlight important considerations one should make when using images from these categories.


## Starter Containers

Chainguard offers a set of container images that are publicly available and don’t require authentication for download and use; they are free to use for everyone. We refer to these as our *Starter Containers*, and they cover several use cases for different language ecosystems. Starter Containers are limited to the latest build of a given image, and are always tagged as `latest` and `latest-dev`.

You can access these images directly from the Chainguard Registry from the `chainguard` repository. For example, to download the cURL Starter image, you could run a command like the following:

```shell
docker pull cgr.dev/chainguard/curl
```

To access any other image, you will need to do so through your organization's private Chainguard repository. The following example will pull the `chainguard-base` image from the `chainguard.edu` organization's repository:

```shell
docker pull cgr.dev/chainguard.edu/chainguard-base
```

Note that you won't have access to the organization's repository used in this example, but if your organization has access to the `chainguard-base` image you will be able to pull this image using your organization's repository name in place of `chainguard.edu`. The Chainguard Registry provides public access to all Starter images, and provides customer access for Production images after logging in and authenticating.

For a complete list of Starter images that are currently available, check out the [**Starter** category on Chainguard's Images Directory](https://images.chainguard.dev/?category=starter). Registered users can also access all Starter and available Production images in the [Chainguard Console](https://console.chainguard.dev/overview). After logging in you will be able to find all the currently available Starter Images in the **Public images** tab. 

### Production Containers

The rest of Chainguard's Containers, those that **are not** Starter images and not included in the free tier of images, are referred to as *Production Images*. Production images are enterprise-ready images that come with patch SLAs and features such as Federal Information Processing Standard (FIPS) readiness and unique time-stamped tags. Unlike Starter images, which are typically paired with only the latest version of an upstream package, Production images offer specific major and minor versions of open source software.

As with the Starter Container category, any container image considered a Production image will also fall into at least one of the other categories listed in this guide. To view the Production container images that your organization has access to, select the appropriate organization in the drop-down menu above the left-hand navigation and then click the **Organization images** tab.


## Base Containers

Base Containers are meant to be extended by users with their own packages and applications. Examples include [chainguard-base](https://images.chainguard.dev/directory/image/chainguard-base/overview), [Go](https://images.chainguard.dev/directory/image/go/overview), and [Python](https://images.chainguard.dev/directory/image/python/overview).

Chainguard is responsible for releasing fully-patched toolchains and Base Containers, while customers are responsible for patching any applications and dependencies they add to a Chainguard Container. It is recommended to use a fully-patched Chainguard toolchain image to build the application, and a fully-patched Chainguard Base container image to layer the final application on.

When migrating to a Chainguard Base container image you should first check the images’s overview page on the Images Directory for usage details and any compatibility notes. You should understand the libraries, runtime requirements, and operating system dependencies of the applications you plan to have running on the Base container image.

It is a best practice to use the same versions of any languages or applications that will be running on the Chainguard Base container image as what is currently running in your environment. Do not upgrade language or application versions at the same time that you migrate. Following the migration, you should thoroughly test and monitor your application.

If you need a package to use with your Chainguard Base Container, Wolfi packages are available using `apk`. Ensure you only use Wolfi packages, as Alpine APK’s are not compatible with Wolfi. Additionally, it is important to note that vendor-provided packages need to be glibc-based and their functionality should be fully tested along with the application. For additional tips, please refer to our guide on [Troubleshooting apko Builds](/open-source/build-tools/apko/troubleshooting/).

> **Note**: Base Containers often require more customization by the user. Be aware that Chainguard offers a customization platform called [Custom Assembly](/chainguard/chainguard-images/features/custom-assembly/) to streamline this requirement without customers having to stand up their own custom pipelines.


## Application Containers

In contrast with Base container images, which are intended to be built upon, Application Containers are designed to be used directly, often by plugging into systems like Helm. Some examples of Chainguard's Application images include [nginx](https://images.chainguard.dev/directory/image/nginx/overview), [Fulcio](https://images.chainguard.dev/directory/image/fulcio/overview), and [apko](https://images.chainguard.dev/directory/image/apko/overview). 

When it comes to maintaining Application container images, Chainguard is responsible for rebuilding the upstream project with the latest toolchain and patching static and dynamic dependencies where such a change is non-breaking. Customers are responsible for tracking a supported version of the Chainguard Container.

When migrating to a Chainguard Application container image you should first check the image’s overview page on the Images Directory for usage details and any compatibility notes. There may be user ID, permissions, or volume path differences with the Chainguard image that you should be aware of. It is a best practice to use the same version of the Chainguard Application container image as what is currently running in your environment.


## AI Container

Artificial intelligence and machine learning (AI/ML) systems are used in a wide variety of high-stakes applications, including information retrieval, medical research, fraud identification, military operations, autonomous vehicle navigation, and more. If compromised by malicious actors, the consequences could be disastrous and far reaching.

Due to their unique features and uses, these systems often pose a greater risk than traditional software systems. Chainguard offers a suite of CPU- and GPU-enabled AI Containers which can help to mitigate these risks. Some of these AI container images include [NeMo](https://images.chainguard.dev/directory/image/nemo/overview), [PyTorch](https://images.chainguard.dev/directory/image/pytorch/overview), and [TensorFlow](https://images.chainguard.dev/directory/image/tensorflow/overview).

These images are hardened, minimal, and optimized for efficient AI development and deployment. By leveraging Chainguard AI Containers, organizations can confidently secure their AI infrastructure, streamline vulnerability management, and maintain high performance with low-to-zero vulnerabilities. Rather than starting with tens, dozens, or hundreds of CVEs in your application or pipeline, you start with a clean slate. 

To learn more about Chainguard's AI Containers and their uses, we encourage you to check out our course on [Securing the AI/ML Supply Chain](https://courses.chainguard.dev/securing-ai).

## FIPS Containers

FIPS — or, Federal Information Processing Standards — are publicly announced standards developed by the National Institute of Standards and Technology (NIST). Chainguard offers images that use FIPS-validated cryptographic software modules to help users ensure that their applications meet FIPS standards.

Chainguard offers FIPS versions of many of its container images, so FIPS Containers will fall into more than one category. Some Chainguard container images with FIPS variants are [nginx](https://images.chainguard.dev/directory/image/tensorflow/overview), [PHP](https://images.chainguard.dev/directory/image/php-fips/overview), and [PyTorch](https://images.chainguard.dev/directory/image/pytorch-fips/overview). 

For more information, please refer to our conceptual article on [Chainguard FIPS Images](/chainguard/chainguard-images/features/fips/fips-images/).


## Container Image Type Considerations

There is some overlap between the different container image categories outlined in this guide. For example, the [PyTorch](https://images.chainguard.dev/directory/image/pytorch/overview) image is an AI image, but it is also part of our free tier, meaning it's also a Starter image. 

Many customers purchase both Application and Base Containers. Note that it often takes more time to migrate your applications to a Base container image in comparison to an Application image due to the complexity of coordinating multiple teams, testing, and release schedules. We recommend starting with and migrating to Application container images first while your teams get trained and onboarded with Base container images.

A common requirement for many customers is to add a company-specific certificate or other security related content. The three most common ways to accomplish this are:

1. Using [incert](/chainguard/chainguard-images/features/incert-custom-certs/)
2. Running the `update-ca-certificates` utility within a Dockerfile
3. Using the Java `keytool` utility within a Dockerfile

The process of adding or updating certificates, configuring APK repositories, and implementing other organization-specific customizations into an image is commonly known as creating a "Golden Image". This approach enables these standard modifications to be applied once and then distributed across all teams, thereby reducing the risk of errors and minimizing friction during the migration process.


## Learn More

By reading this guide, you should have a better understanding of how Chainguard categorizes its container images and what these categories mean. To recap:

* **Starter**: Chainguard's free tier of container images
* **Base**: Containers meant to be built upon
* **Application**: Containers meant to be run directly
* **FIPS**: Contain FIPS-validated cryptographic modules
* **AI**: Containers for running AI/ML workloads securely

For more information on Chainguard Containers, please refer to the other resources in the [About section](/chainguard/chainguard-images/about/). In particular, you may find our conceptual article on [Chainguard's Shared Responsibility Model](/chainguard/chainguard-images/about/shared-responsibility-model/) to be of interest.