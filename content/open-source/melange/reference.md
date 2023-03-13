---
title: "melange YAML Reference"
type: "article"
description: "A reference guide for writing YAML for melange"
date: 2022-10-17T11:07:52+02:00
lastmod: 2022-10-17T11:07:52+02:00
draft: false
tags: ["MELANGE", "REFERENCE"]
images: []
menu:
  docs:
    parent: "melange"
weight: 150
toc: true
---

This page provides a reference for melange's YAML specification.

## package
This section defines metadata about the apk package being built.


| Directive             | Expects                                                                                                                                    |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                | (String) Name of the package.                                                                                                              |
| `version`             | (String) Version of the package.                                                                                                           |
| `epoch`               | (String) Useful to force the package to be seen as newer than any previous version with a lower epoch.                                     |
| `description`         | (String) A description of the package.                                                                                                     |
| `target-architecture` | (Array) Architectures for which the package will be built. Use 'all' for all available architectures.                                      |
| `copyright`           | (Array) License and copyright information.                                                                                                 |
| `dependencies`        | (Array) List of runtime dependencies for this package. These will get pulled via apk as system dependencies when the package is installed. |

#### Example

```yaml
package:
  name: hello
  version: 2.12
  epoch: 0
  description: 'the GNU hello world program'
  target-architecture:
    - all
  copyright:
    - paths:
        - '*'
      attestation: |
        Copyright 1992, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2005,
        2006, 2007, 2008, 2010, 2011, 2013, 2014, 2022 Free Software Foundation,
        Inc.
      license: GPL-3.0-or-later
  dependencies:
    runtime:

```

## environment
This section defines the build environment, specifying dependencies that need to be present at build time.

| Directive  | Expects                                                                                                                          |
|------------|----------------------------------------------------------------------------------------------------------------------------------|
| `contents` | (Array) Defines the packages that will be installed for running the build pipeline, and the repositories where to download them. |

#### Example

```yaml
environment:
  contents:
    repositories:
      - 'https://dl-cdn.alpinelinux.org/alpine/edge/main'
    packages:
      - alpine-baselayout-data
      - busybox
      - build-base
      - scanelf
      - ssl_client
      - ca-certificates-bundle

```
_NOTE: do not mix Alpine apk repositories with Wolfi apk repositories when defining your software sources._

## pipeline
Defines the build steps.

| Directive | Expects                                           |
|-----------|---------------------------------------------------|
| `uses`    | (String) Uses a built-in pipeline.                |
| `with`    | (Array) Provide parameters to a "uses" directive. |

#### Example

```yaml
- uses: fetch
  with:
    uri: https://ftp.gnu.org/gnu/hello/hello-${{package.version}}.tar.gz
    expected-sha256: cf04af86dc085268c5f4470fbae49b18afbc221b78096aab842d934a76bad0ab
- uses: autoconf/configure
- uses: autoconf/make
- uses: autoconf/make-install
- uses: strip

```
## subpackages
Creates subpackages for documentation and additional (dev) headers, which may not be necessary at runtime.


| Directive  | Expects  |
|------------|----------|
| `name`     | (String) |
| `pipeline` | (Array)  |


#### Example

```yaml
subpackages:
  - name: hello-doc
    pipeline:
      - uses: split/manpages

```
