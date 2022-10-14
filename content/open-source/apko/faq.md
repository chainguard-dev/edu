---
title: "apko FAQs"
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
apko images are defined declaratively using a YAML file. There are no building steps; instead, you'll define a system state that apko will reproduce into a one-layer image.

### Are apko images compatible with Docker?
Yes, all images built with apko conform to the OCI standard, and thus work with Docker. OCI stands for [Open Container Initiative](https://opencontainers.org), a governance body responsible for defining container standards.

### How does apko differ from Docker?
apko is primarily a _composition_ tool, unlike Docker, which builds containers by running multiple steps that consist of user defined shell commands.

With apko, all software is installed via apk packages named in the YAML file. This contrasts with Dockerfiles, which allow users to install additional software via package managers, copy files from the host, and download arbitrary content from the internet. The steps in a Dockerfile typically must run in a specific order for the build to work, while with apko it doesn't matter in which order you define your list of packages. Your YAML declares a system state the build will reach at the end, a design that allows for reproducible pipelines.

This is an important design principle that allows apko to account for all software that is included within an image and provide a complete, high-quality software bill of materials (SBOM).

### What is an SBOM and why is it important?
An SBOM is a software bill of materials, which is a list containing detailed information about all software that is included within a software artifact, whether it's an application or a container image.

SBOMs provide visibility into the software you depend on. They can allow automated systems to quickly identify issues such as unpatched vulnerabilities, since SBOMs typically include the version of each dependency listed.

### How can I copy application files to an apko image?
Any and all content that goes into a container image built with apko must be available as an `apk` package. You can use [melange](/open-source/melange) to build an apk packaging your application, or you can use a Docker [multistage build](https://docs.docker.com/build/building/multi-stage/) within a Dockerfile to build the application in a separate environment and then copy the artifacts on top of an apko base image that will serve as your production runtime.


### Can I mix packages from Alpine repositories into a Wolfi-based image?
No, it's not possible to mix Alpine apks with Wolfi apks. If your image requires dependencies that are currently only available for Alpine, you might consider opening a new issue in the [wolfi-os](https://github.com/chainguard-dev/wolfi-os/) repository to suggest the new package addition, or use [melange](https://github.com/chainguard-dev/melange) to build a custom apk for your image.

### Can I use apko to build a Debian/Ubuntu image?
No. apko is based on the [apk](https://wiki.alpinelinux.org/wiki/Package_management) package format, because it [has different design principles](/open-source/apko/apk-package-manager) that make it better suited for declarative pipelines that are reproducible. apko doesn't support `.deb` or other package formats.
