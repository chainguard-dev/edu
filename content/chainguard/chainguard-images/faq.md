---
title: "Chainguard Images FAQs"
type: "article"
description: "Frequently asked questions about Chainguard Images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2022-09-01T08:49:31+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 500
toc: true
---

### How do Chainguard Images relate to the Google Distroless Images?
The [Google distroless](https://github.com/GoogleContainerTools/distroless) images follow a similar
philosophy to many of our images: they are minimal images that don't include package managers or
shells. The main difference is in the implementation. The Google distroless images are built with
[Bazel](https://bazel.build) and based on the Debian distribution, whereas Chainguard Images are
built with [apko](/open-source/apko) and based on the [Wolfi](/open-source/wolfi)
undistro. We believe our approach is more maintainable and extensible.

### What is an "undistro"?
We call Wolfi an undistro because unlike a typical Linux distribution, Wolfi is a stripped-down distribution designed for the cloud-native era. Most notably, we don’t include a Linux kernel, instead relying on the environment (such as the container runtime) to provide this.

### Which images are available?
You can check which images are already available at the [Chainguard Images Reference](https://edu.chainguard.dev/chainguard/chainguard-images/reference/) page or directly at our [GitHub Repository](https://github.com/chainguard-images).

### What is an SBOM and why is it important?
An SBOM is a Software Bill of Materials, which is a list containing detailed information about all software that is included within a software artifact, whether it's an application, a container image, or a physical appliance.

SBOMs provide visibility into the software you depend on. They can allow automated systems to quickly identify issues such as unpatched vulnerabilities, since SBOMs typically include the version of each dependency listed.

### Who maintains Chainguard Images?
[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) are officially maintained by [Chainguard](https://chainguard.dev) employees, but they are also open source, which means any community member is welcome to suggest improvements.

### How often are Chainguard Images updated?
All images are rebuilt and updated every night to incorporate any available new patches and package updates.

### Can I simply replace my current base image with a Chainguard Image and it will work out of the box?
Chainguard Images are distroless, which means they are minimalist and most of them don't come with a package manager. Depending on your stack, you may need to include additional software by copying artifacts from multi-stage builds.

### Which image versions are publicly available?
The `latest` tags of all images are publicly available and do not require authentication. Starting in April, only authenticated users will have access to older tags.

