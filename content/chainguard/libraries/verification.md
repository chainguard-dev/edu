---
title: "Chainguard Libraries Verification"
linktitle: "Verification"
description: "Learn how to verify Java and Python dependencies are from Chainguard Libraries using the chainver tool for enhanced supply chain security"
type: "article"
date: 2025-07-03T12:00:00+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 004
toc: true
---

## Overview

Chainguard's `chainver` tool enables verification that your Java and Python dependencies come from Chainguard Libraries, providing critical visibility into your software supply chain security. By verifying binary artifacts across your projects and repositories, you can ensure dependencies are sourced from Chainguard's hardened build environment rather than potentially compromised public repositories, identify opportunities to improve security posture, and maintain compliance with supply chain security policies.

Chainguard provides the command line tool `chainver` to enable this
verification with the following features:

* Use a signature-based binary identification and a checksum fallback.
* Support different binary formats, including JAR, WAR, EAR, ZIP, TAR, WHL, and
  APK files as well as container images.
* Allow analysis of directories and nested archive files.
* Create output in text, json, yaml, and CSV format.

## Requirements

The following requirements must be met:

* Linux, MacOS, or Windows operating system.
* x86_64 or arm64 processor architecture.
* `chainctl` installed and available on the `PATH`.
* `cosign` installed and available on the `PATH`.
* Sufficient [network access](/chainguard/libraries/network-requirements/) available.

## Access 

[Download the latest release - version 0.3.5](https://dl.enforce.dev/chainver/0.3.5/chainver-v0.3.5.zip)

Use the following script to automatically determine the latest available version
and download the ZIP archive.

```shell
# Get the latest version
export LATEST=$(curl -s "https://storage.googleapis.com/us.artifacts.prod-enforce-fabc.appspot.com/?prefix=chainver/" | \
  grep -oE 'chainver/[0-9]+\.[0-9]+\.[0-9]+/' | \
  sed 's|chainver/||g' | sed 's|/$||g' | \
  sort -V | tail -1)
# Download the release zip file
curl -LO "https://dl.enforce.dev/chainver/${LATEST}/chainver-v${LATEST}.zip"
```

Extract the ZIP archive and find archives for different operating systems and
processor architectures in the created `chainver-package/archives` directory:

```
chainver_0.3.5_Linux_x86_64.tar.gz
chainver_0.3.5_Darwin_arm64.tar.gz
chainver_0.3.5_Darwin_x86_64.tar.gz
chainver_0.3.5_Linux_arm64.tar.gz
chainver_0.3.5_Windows_x86_64.zip
```

Extract the package, in the example for MacOS and ARM processor, and copy it to
a directory that is on the `PATH`:

```shell
$ tar xfvz chainver_0.3.5_Darwin_arm64.tar.gz
x LICENSE
x README.md
x chainver
```

Verify running `chainver` and inspect the version:

```shell
$ chainver version
ChainVer version 0.3.5 (3277bb5)
  built with go1.24.0 on darwin/arm64
```

## Documentation

Detailed installation and user instructions are included with the provided
distribution in the `chainver-package/README.md` file  and with the `chainver
help` command.
