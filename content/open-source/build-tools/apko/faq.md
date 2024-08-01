---
title: "apko FAQs"
aliases:
- /open-source/apko/faq
type: "article"
lead: "Frequently asked questions about apko"
description: "Frequently asked questions about apko"
date: 2022-10-10T11:07:52+02:00
lastmod: 2024-07-31T11:07:52+02:00
draft: false
tags: ["apko", "FAQ",]
images: []
menu:
  docs:
    parent: "apko"
weight: 50
toc: true
---

## Do I need to understand apko to use Chainguard Images?
No. Chainguard built [apko](https://github.com/chainguard-dev/apko) as part of its open source tooling around the [Wolfi](/open-source/wolfi) operating system. While you can check out the [project on GitHub](https://github.com/chainguard-dev/apko) and learn more, it's not a prerequisite for using or [working with Chainguard Images](/chainguard/chainguard-images/working-with-images).

## How are apko images defined?
apko images are defined declaratively using a YAML file. It was designed this way to facilitate reproducible builds — run apko twice, and you'll get the same output.

## Does apko provide SBOMs?
Yes, apko builds include high-quality [SBOMs](/open-source/sbom/what-is-an-sbom/) (software bills of materials) for all builds. This is a key feature of the tooling that Chainguard has developed to ensure that users can trust the software they are running.

## Can I use apko images with Docker?
Yes, images built with apko are fully OCI compliant and can be used with any container runtime that supports the OCI image format.

## Can I mix Wolfi and Alpine package repositories to create my apko build environment?
No, it's not possible to mix Wolfi apks with Alpine apks.

## Can I execute arbitrary commands in apko builds such as in RUN steps in Dockerfiles?
No, you can't execute arbitrary commands in apko builds. apko provides directives for creating users and setting up directories and permissions, but any additional steps necessary at build time, such as the installation of packages and execution of shell commands, must be defined in apk packages that should be included in the list of build dependencies. This is an implementation feature to allow for reproducible builds and high-quality SBOMs.
