---
title: "Image Overview: bun"
linktitle: "bun"
type: "article"
layout: "single"
description: "Overview: bun Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/bun/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bun/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/bun/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bun/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [bun](https://bun.sh/) tool.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/bun:latest
```


<!--body:start-->
## Usage

The `bun` image contains the `bun` CLI and is most similar to the upstream `distroless` variant.

To get started:

```shell
$ docker run cgr.dev/chainguard/bun
Bun is a fast JavaScript runtime, package manager, bundler, and test runner. (1.0.20 (09d51486))

Usage: bun <command> [...flags] [...args]

Commands:
  run       ./my-script.ts       Execute a file with Bun
            lint                 Run a package.json script
  test                           Run unit tests with Bun
  x         prisma               Execute a package binary (CLI), installing if needed (bunx)
  repl                           Start a REPL session with Bun

  install                        Install dependencies for a package.json (bun i)
  add       svelte               Add a dependency to package.json (bun a)
  remove    @evan/duckdb         Remove a dependency from package.json (bun rm)
  update    jquery               Update outdated dependencies
  link      [<package>]          Register or link a local npm package
  unlink                         Unregister a local npm package
  pm <subcommand>                Additional package management utilities

  build     ./a.ts ./b.jsx       Bundle TypeScript & JavaScript into a single file

  init                           Start an empty Bun project from a blank template
  create    @zarfjs/zarf         Create a new project from a template (bun c)
  upgrade                        Upgrade to latest version of Bun.
  <command> --help               Print help text for command.

Learn more about Bun:            https://bun.sh/docs
Join our Discord community:      https://bun.sh/discord
```

<!--body:end-->

