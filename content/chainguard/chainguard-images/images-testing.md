---
title: "How Chainguard Images are Tested"
linktitle: "How Images are Tested"
type: "article"
description: "A conceptual article outlining testing requirements for Chainguard Images."
date: 2024-03-13T11:07:52+02:00
lastmod: 2023-03-13T11:07:52+02:00
draft: false
tags: ["Overview", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 550
toc: true
---

Chainguard Images are minimal, distroless container images that you can use to build and run secure applications. A frequently-asked question about these Images relates to what kind of testing Chainguard performs on them to ensure they match the functionality of their upstream counterparts.

This article provides a high level overview of what testing Chainguard performs when building new Images to ensure their security and that they provide an experience consistent with their external counterparts.


## Build requirements for new Images

Chainguard has a set of requirements in place that new Images must meet in order to be included in our library of Images. These requirements fall into two categories:

* Image standards
* Application testing


### Image standards

When building a new Image, Chainguard will take steps to ensure it meets the following standards:

| **Requirement** 	  |  **Explanation**     |
| --- | --- |
| **Size**     |  Any new Chainguard Images should be smaller than their external counterparts. Any Images that aren't smaller than their counterparts must include an explanation as to why.     |
|  **CVEs**     | When scanned with a CVE scanning tool like Grype, new Images should return zero CVEs. Again, if an Image does return CVEs in its scan results it should include an explanation. 	  |
|  **Kubernetes accessibility**     | Containers used for Kubernetes-based deployments must be able to run inside of a Kubernetes cluster.     |
|  **Architecture**     | Chainguard Images must be built for both the `x86_64` and `aarch64` architectures.      |

### Application testing

Chainguard performs the following checks on new Images to ensure that the applications contained within them meet the needs of most use cases:

| **Requirement** 	  |  **Explanation**     |
| --- | --- |
|  **Functionality**     | The application is tested to comply with it's upstream counter parts core feature set.   |
|  **Builder Images**     | Chainguard's builder Images can in fact build new, functional images.     |


## Automated tests

In addition to the Image build requirements outlined previously, Chainguard also performs a number of automatic checks for new Images as part of our CI/CD process. 

Depending on the Image, Chainguard peforms various representative tests, such as functional and integration tests. For example, for applications primarily deployed with a Helm chart, the Image is deployed to an ephemeral Kubernetes cluster using the accepted Helm chart and validated in various ways.

When applicable, Chainguard will develop functional tests for Images. These tests vary by application, but can generally be thought of as integration tests that run after an Image is built but before it gets tagged.

Our goal for these tests is that they fully evaluate the Image's deployment in a representative environment; for example, Images running Kubernetes applications are tested in a Kubernetes cluster and builder or toolchain applications are tested with a `docker run` command or part of a `docker build`. This means that our Images work with the existing upstream deployment methods, such as Helm charts or Kustomize manifests, helping us to ensure that an Image is as close to a drop-in replacement as possible.

Additionally, Chainguard performs automated tests on every package included in our Images. These tests run on every new build within an ephemeral container environment before the build is published. This allows us to validate the representative functionality of each package.


## Learn more

Chainguard's rigorous Image testing standards and frequent updates ensure that they will work as expected with few (and often zero) vulnerabilities. If you're having trouble working with a specific chainguard Image, we encourage you to check out its Overview page in our [Image reference documentation](/chainguard/chainguard-images/reference/).

For general help with using Chainguard Images, you can refer to our [Debugging Distroless Images](/chainguard/chainguard-images/reference/) guide or our [Images FAQs](/chainguard/chainguard-images/faq/). For help with specific issues or questions not covered in these resources, please [contact our support team](https://support.chainguard.dev).