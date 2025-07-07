---
title: "Chainguard Libraries Verification"
linktitle: "Verification"
description: "Verifying binaries or projects for Chainguard Libraries"
type: "article"
date: 2025-07-03T12:00:00+00:00
lastmod: 2025-07-03T12:00:00+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 004
toc: true
---

## Overview

At any point in time of your use of Chainguard Libraries you can verify binary
artifacts, project setups, or even entire directories and repositories for the
use of binaries supplied by Chainguard Libraries. This allows you to check
adoption of Chainguard Libraries, find opportunities for further replacements or
gaps in Chainguard Libraries, and identify artifacts originating from other,
less trusted sources.

Chainguard provides the command line tool `chainver` to enable this
verification with the following features:

* Use a signature-based binary identification and a checksum fallback.
* Support different binary formats, including JAR, WAR, EAR, ZIP, TAR, WHL, and
  APK files as well as container images.
* Allow analysis of directories and nested archive files.
* Create output in text, json, yaml, and csv format.

## Requirements

The following requirements must be met:

* Linux, MacOS, or Windows operating system.
* x86_64 or arm64 processor architecture.
* `chainctl` installed and available on the `PATH`.
* `cosign` installed and available on the `PATH`.
* Sufficient [network access](/chainguard/libraries/network-requirements) available.

## Access 

chainver is available to customers upon request. The archive includes binaries
for different operating systems and processor architectures.

## Documentation

Detailed installation and user instructions are included with the provided
distribution and with the `chainver help` command.
