---
title: "apko FAQs"
type: "article"
lead: "Frequently asked questions about apko"
description: "Frequently asked questions about apko"
date: 2022-10-10T11:07:52+02:00
lastmod: 2023-10-23T11:07:52+02:00
draft: false
tags: ["apko", "FAQ",]
images: []
menu:
  docs:
    parent: "apko"
weight: 50
toc: true
---

### How are melange packages defined?
melange apks are defined declaratively using a YAML file.

### Are melange apks compatible with Alpine?
Yes, melange apks are built to be compatible with apk-based systems including Alpine.

### Can I mix Alpine and Wolfi package repositories to create my melange build environment?
No, it's not possible to mix Alpine apks with Wolfi apks. If you have unmet dependencies, you'll need to build those first as separate packages.

### Is it mandatory to sign packages with a melange key?
Signing packages is not mandatory, but it is a recommended practice that is enforced by some systems. Signing packages allows users and automated systems to verify that the package they downloaded was built by the same person who signed it, and that it hasn't been tampered with.

### Can I create custom pipelines and embed them into my main pipeline?
Although melange supports inclusion of sub-pipelines, this feature currently only supports the built-in pipelines (such as `make`, `split` and others) that can be found at the [pkg/build/pipelines](https://github.com/chainguard-dev/melange/tree/main/pkg/build/pipelines) directory on the main project repository.
The ability to embed custom pipelines is on the roadmap, but it's not a priority at the moment.
