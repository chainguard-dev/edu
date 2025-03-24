---
title: "How Chainguard Container Images are Tested"
linktitle: "How Images are Tested"
aliases:
- /chainguard/chainguard-images/images-testing/
- /chainguard/chainguard-images/about/images-testing/
type: "article"
description: "A conceptual article outlining testing requirements for Chainguard Images."
date: 2024-03-21T11:07:52+02:00
lastmod: 2023-03-21T11:07:52+02:00
draft: false
tags: ["Overview", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "about"
weight: 015
toc: true
---

Chainguard Images are minimal, distroless container images that you can use to build and run secure applications. Given the importance of secure, highly performant images, Chainguard performs testing to ensure our Images match the functionality of upstream and other external counterparts.

This article provides a high-level overview of Chainguard's approach to testing when building new Images to ensure their security and consistency with comparable container images.


## Build requirements for new Images

Chainguard has a set of requirements in place that new Images must meet in order to be included in our [Images Directory](https://images.chainguard.dev?utm=docs). These requirements fall into two categories:

* Image standards
* Application testing


### Image standards

When building a new Image, Chainguard will take steps to ensure it meets the following standards:

| **Requirement** 	  |  **Explanation**     |
| --- | --- |
| **Size**     |  Any new Chainguard Images should be smaller than their external counterparts, though exceptions may occur.    |
|  **CVEs**     | When scanned with a CVE scanning tool like Grype, new Images should return zero CVEs. If an Image does return CVEs in its scan results it should include an explanation, though some reported CVEs may be false positives. Refer to our [Security Advisories](https://images.chainguard.dev/security?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-images-testing) for more information.	  |
|  **Kubernetes accessibility**     | Containers used for Kubernetes-based deployments must be able to run inside of a Kubernetes cluster.     |
|  **Architecture**     | Chainguard Images must be built for both the `x86_64` and `aarch64` architectures.      |

### Application testing

Chainguard performs the following checks on new Images to ensure that the applications contained within them meet the needs of most use cases:

| **Requirement** 	  |  **Explanation**     |
| --- | --- |
|  **Functionality**     | The application is tested to comply with is upstream counterpart's core feature set.   |
|  **Builder Images**     | Chainguard's builder Images can in fact build new, functional images.     |


## Automated tests

In addition to the Image build requirements outlined previously, Chainguard also performs a number of automatic checks for new Images as part of our CI/CD process. 

Depending on the Image, Chainguard performs various representative tests, such as functional and integration tests. For example, for applications primarily deployed with a Helm chart, the Image is deployed to an ephemeral Kubernetes cluster using the accepted Helm chart, which is validated in various ways.

When applicable, Chainguard will develop functional tests for Images. These tests vary by application, but can generally be thought of as integration tests that run after an Image is built but before it gets tagged.

Our goal for these tests is that they fully evaluate the Image's deployment in a representative environment; for example, Images running Kubernetes applications are tested in a Kubernetes cluster and builder or toolchain applications are tested with a `docker run` command or part of a `docker build` process. This means that our Images work with the existing upstream deployment methods, such as Helm charts or Kustomize manifests, helping us to ensure that an Image is as close to a drop-in replacement as possible.

Additionally, Chainguard performs automated tests on every package included in our Images. These tests run on every new build within an ephemeral container environment before the build is published. This allows us to validate the representative functionality of each package.


## Learn more

Chainguard's rigorous Image testing standards and frequent updates ensure that they will work as expected with few (and often zero) vulnerabilities. If you're having trouble working with a specific Chainguard Image, we encourage you to check out its relevant Overview page in our [Chainguard Images Directory](https://images.chainguard.dev/directory?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-images-testing).

For general help with using Chainguard Images, you can refer to our [Debugging Distroless Images](/chainguard/chainguard-images/debugging-distroless-images/) guide or our [Images FAQs](/chainguard/chainguard-images/faq/). For help with specific issues or questions not covered in these resources, please [contact our support team](https://support.chainguard.dev?utm=docs).