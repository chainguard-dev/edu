---
title: "go/build"
aliases:
- /open-source/melange/melange-pipelines/go/build
type: "article"
description: "Reference docs for the go/build melange pipeline"
date: 2023-04-06T11:07:52+02:0
lastmod: 2023-04-06T11:07:52+02:0
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


### Reference
| Input         | Description                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `packages`*   | List of space-separated packages to compile. Files con also be specified.This value is passed as an argument to go build. All paths are relativeto inputs.modroot. |
| `tags`        | A comma-separated list of build tags to pass to the go compiler                                                                                                    |
| `output`*     | Filename to use when writing the binary. The final install location inside the apk will be in prefix / install-dir / output                                        |
| `modroot`     | Top directory of the go module, this is where go.mod lives. Before buidingthe go pipeline wil cd into this directory. Default is set to `.`                        |
| `prefix`      | Prefix to relocate binaries Default is set to `usr`                                                                                                                |
| `ldflags`     | List of [pattern=]arg to pass to the go compiler with -ldflags                                                                                                     |
| `install-dir` | Directory where binaries will be installed Default is set to `bin`                                                                                                 |


### Example
There are no examples available.
