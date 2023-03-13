---
title: "apko YAML Reference"
type: "article"
description: "A reference guide for writing YAML for apko"
date: 2022-10-10T11:07:52+02:00
lastmod: 2022-10-10T11:07:52+02:00
draft: false
tags: ["APKO", "REFERENCE"]
images: []
menu:
  docs:
    parent: "apko"
weight: 150
toc: true
---

This page provides a reference for apko's YAML specification.

## contents
This section defines sources and packages you want to include in your image.

| Directive    | Description                                                                                      |
|--------------|:-------------------------------------------------------------------------------------------------|
| repositories | A list of apk repositories for this image. Supports either Alpine or Wolfi apk repositories.     |
| packages     | A list containing all packages that should be installed as part of a given image's requirements. |

_*It is not recommended to mix Alpine apks with Wolfi apks._

#### Example:

```yaml
contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/edge/main
  packages:
    - alpine-base
```

## entrypoint
This section defines an entry point command for your image.

| Directive | Description                                                                                 |
|-----------|:--------------------------------------------------------------------------------------------|
| command   | The command that should be executed as entry point for this image.                          |


#### Example:

```yaml
entrypoint:
  command: /usr/bin/php81
```

## archs
The architectures to build. This top-level directive expects a list with all architectures that should be a target for the build.
By default, apko will try to build for all architectures that are currently supported.

#### Example:

```yaml
archs:
  - x86_64
```

## environment
This section defines environment variables that will be set for this image.

#### Example:

```yaml
environment:
  PATH: /usr/sbin:/sbin:/usr/bin:/bin
  myVAR: "test"
```

## accounts
This section defines users and groups that should be added to this image.

| Directive | Description                                                         |
|-----------|:--------------------------------------------------------------------|
| groups    | A list with the groups that should be present in this image.        |
| users     | A list with the user accounts that should be present in this image. |
| run-as    | The default user to run the entrypoint command.                     |


#### Example:

```yaml
accounts:
  groups:
    - groupname: nonroot
      gid: 65532
  users:
    - username: nonroot
      uid: 65532
  run-as: root
```
