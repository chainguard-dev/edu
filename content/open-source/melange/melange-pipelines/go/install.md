---
title: "go/install"
type: "article"
description: "Reference docs for the install melange pipeline"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["melange", "Reference"]
images: []
menu:
  docs:
    parent: "melange"
weight: 600
toc: true
---


Run a build using the go compiler

### Dependencies
- go
- busybox
- ca-certificates-bundle
- git


### Reference
| Input         | Description                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| `package`*    | Import path to the package                                                                                        |
| `version`     | Package version to install. This can be a version tag (v1.0.0), a commit hash or another ref (eg latest or HEAD). |
| `prefix`      | Prefix to relocate binaries Default is set to `usr`                                                               |
| `install-dir` | Directory where binaries will be installed Default is set to `bin`                                                |
| `ldflags`     | List of [pattern=]arg to pass to the go compiler with -ldflags                                                    |
| `tags`        | A comma-separated list of build tags to pass to the go compiler                                                   |


### Example
There are no examples available.
