---
title: "FAQs"
type: "article"
lead: "Frequently asked questions about apko"
description: "Frequently asked questions about apko"
date: 2022-10-10T11:07:52+02:00
lastmod: 2022-10-10T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "apko"
weight: 900
toc: true
---

### How are apko images defined?
apko images are defined in a declarative way using YAML files. There are no building steps; instead, you'll define a system state that apko will reproduce into a one-layer image.

### Are apko images compatible with Docker?
Yes, all images built with apko are OCI, and thus work with Docker. OCI stands for _Open Container Initiative_, a standard format that drives interoperability across the container and cloud-native industry.

### How does apko differ from Docker?
apko is primarily a _composition_ tool, unlike Docker, which incorporates arbitrary building steps.
This is an important design principle of apko in order to account for all software that is included within an image, providing a complete, high-quality software bill of material (SBOM). It also allows for a reproducible pipeline, and the use of a declarative language to define system state (YAML).

### What is an SBOM and why is it important?
An SBOM is a Software Bill of Materials, which is a list containing detailed information about all software that is included within a software artifact, whether it's an application, a container image, or a physical appliance.

SBOMs provide visibility into the software you depend on. They can allow automated systems to quickly identify issues such as unpatched vulnerabilities, since SBOMs typically include the version of each dependency listed.

### How can I copy application files to an apko image?
Any and all content that goes into a container image built with apko must be available as an `apk` package. You can use [melange](/open-source/melange) to build an apk packaging your application, or you can use a Docker [multistage build]() within a Dockerfile to build the application in a separate environment and then incorporate the artifacts into an apko image that will serve as your production runtime.


### Can I mix packages from Alpine repositories into a Wolfi-based image?
No, it's not possible to mix Alpine apks with Wolfi apks. If your image requires dependencies that are currently only available for Alpine, you might consider opening a new issue in the [wolfi-os](https://github.com/chainguard-dev/wolfi-os/) repository to suggest the new package addition, or use [melange](https://github.com/chainguard-dev/melange) to build a custom apk for your image.

### Can I use apko to build a Debian/Ubuntu image?
No. apko is based on the [apk](https://wiki.alpinelinux.org/wiki/Package_management) package format, because it [has different design principles](/open-source/apko/apk-package-manager) that make it better suited for declarative pipelines that are reproducible. apko doesn't support `.deb` or other package formats.
