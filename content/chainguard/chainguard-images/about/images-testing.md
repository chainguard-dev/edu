---
title: "How Chainguard Containers are Tested"
linktitle: "How We Test"
aliases:
- /chainguard/chainguard-images/images-testing/
- /chainguard/chainguard-images/about/images-testing/
type: "article"
description: "A conceptual article outlining testing requirements for Chainguard Containers."
date: 2024-03-21T11:07:52+02:00
lastmod: 2025-04-07T11:07:52+02:00
draft: false
tags: ["Overview", "Chainguard Containers", "Product"]
images: []
menu:
  docs:
    parent: "about"
weight: 015
toc: true
---

Chainguard Containers are minimal, distroless container images that you can use to build and run secure applications. Given the importance of secure, highly performant images, Chainguard performs testing to ensure our container images match the functionality of upstream and other external counterparts.

This article provides a high-level overview of Chainguard's approach to testing when building new container images to ensure their security and consistency with comparable container images.


## Build requirements for new container images

Chainguard has a set of requirements in place that new container images must meet in order to be included in our [Containers Directory](https://images.chainguard.dev?utm=docs). These requirements fall into two categories:

* Container image standards
* Application testing


### Container image standards

When building a new container image, Chainguard will take steps to ensure it meets the following standards:

| **Requirement** 	  |  **Explanation**     |
| --- | --- |
| **Size**     |  Any new Chainguard Containers should be smaller than their external counterparts, though exceptions may occur.    |
|  **CVEs**     | When scanned with a CVE scanning tool like Grype, new container images should return zero CVEs. If a container image does return CVEs in its scan results it should include an explanation, though some reported CVEs may be false positives. Refer to our [Security Advisories](https://images.chainguard.dev/security?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-images-testing) for more information.	  |
|  **Kubernetes accessibility**     | Containers used for Kubernetes-based deployments must be able to run inside of a Kubernetes cluster.     |
|  **Architecture**     | Chainguard Containers must be built for both the `x86_64` and `aarch64` architectures.      |

### Application testing

Chainguard performs the following checks on new container images to ensure that the applications contained within them meet the needs of most use cases:

| **Requirement** 	  |  **Explanation**     |
| --- | --- |
|  **Functionality**     | The application is tested to comply with is upstream counterpart's core feature set.   |
|  **Builder Containers**     | Chainguard's builder containers can in fact build new, functional container images.     |


## Automated tests

In addition to the container image build requirements outlined previously, Chainguard also performs a number of automatic checks for new container images as part of our CI/CD process. 

Depending on the container image, Chainguard peforms various representative tests, such as functional and integration tests. For example, for applications primarily deployed with a Helm chart, the container image is deployed to an ephemeral Kubernetes cluster using the accepted Helm chart, which is validated in various ways.

When applicable, Chainguard will develop functional tests for container images. These tests vary by application, but can generally be thought of as integration tests that run after a container image is built but before it gets tagged.

Our goal for these tests is that they fully evaluate the container image's deployment in a representative environment; for example, container images running Kubernetes applications are tested in a Kubernetes cluster and builder or toolchain applications are tested with a `docker run` command or part of a `docker build` process. This means that our container images work with the existing upstream deployment methods, such as Helm charts or Kustomize manifests, helping us to ensure that a container image is as close to a drop-in replacement as possible.

Additionally, Chainguard performs automated tests on every package included in our container images. These tests run on every new build within an ephemeral container environment before the build is published. This allows us to validate the representative functionality of each package.


## Learn more

Chainguard's rigorous container image testing standards and frequent updates ensure that they will work as expected with few (and often zero) vulnerabilities. If you're having trouble working with a specific Chainguard Container, we encourage you to check out its relevant Overview page in our [Chainguard Containers Directory](https://images.chainguard.dev/directory?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-images-testing).

For general help with using Chainguard Containers, you can refer to our [Debugging Distroless Container Images](/chainguard/chainguard-images/debugging-distroless-images/) guide or our [Chainguard Containers FAQs](/chainguard/chainguard-images/faq/). For help with specific issues or questions not covered in these resources, please [contact our support team](https://support.chainguard.dev?utm=docs).