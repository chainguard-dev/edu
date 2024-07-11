---
title: "melange FAQs"
aliases:
- /open-source/melange/faq
type: "article"
lead: "Frequently asked questions about melange"
description: "Frequently asked questions about melange"
date: 2022-10-17T11:07:52+02:00
lastmod: 2022-10-17T11:07:52+02:00
draft: false
tags: ["melange", "FAQ"]
images: []
menu:
  docs:
    parent: "melange"
weight: 900
toc: true
---

## Do I need to understand melange to use Chainguard Images?

No. Chainguard built [melange](https://github.com/chainguard-dev/melange) as part of its open source tooling used for the [Wolfi](/open-source/wolfi) operating system. While you can check out the [project on GitHub](https://github.com/chainguard-dev/melange) and learn more, it’s not a prerequisite for using or working with [Chainguard Images](/chainguard/chainguard-images).

## How are melange packages defined?
melange apks are defined declaratively using a YAML file.

## Are melange apks compatible with Alpine?
Yes, melange apks are built to be compatible with apk-based systems including Alpine.

## Can I mix Alpine and Wolfi package repositories to create my melange build environment?
No, it's not possible to mix Alpine apks with Wolfi apks. If you have unmet dependencies, you'll need to build those first as separate packages.

## Is it mandatory to sign packages with a melange key?
Signing packages is not mandatory, but it is a recommended practice, because it allows users and automated systems to verify that the package they downloaded was built by the same person who signed it, and that it hasn't been tampered with.

## What happens if I don't provide a key to sign my package(s)?
Some systems may prevent installation of your apk if they can't attest the package provenance. This is the case with apko, which by default will fail any builds that reference unsigned packages.

## Can I create custom pipelines and embed them into my main pipeline?
Although melange supports inclusion of sub-pipelines, this feature currently only supports the built-in pipelines (such as `make`, `split` and others) that can be found at the [pkg/build/pipelines](https://github.com/chainguard-dev/melange/tree/main/pkg/build/pipelines) directory on the main project repository.
The ability to embed custom pipelines is on the roadmap, but it's not a priority at the moment.

