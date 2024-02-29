---
title: "Image Overview: opentofu"
linktitle: "opentofu"
type: "article"
layout: "single"
description: "Overview: opentofu Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/opentofu/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentofu/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/opentofu/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentofu/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[opentofu](https://github.com/opentofufoundation/opentofu) lets you declaratively manage your cloud infrastructure.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/opentofu:latest
```
<!--getting:end-->

<!--body:start-->
The image sets `opentofu` as the entrypoint. To run it:

```
Usage: opentofu [global options] <subcommand> [args]

The available commands for execution are listed below.
The primary workflow commands are given first, followed by
less common or more advanced commands.

Main commands:
  init          Prepare your working directory for other commands
  validate      Check whether the configuration is valid
  plan          Show changes required by the current configuration
  apply         Create or update infrastructure
  destroy       Destroy previously-created infrastructure

All other commands:
  console       Try opentofu expressions at an interactive command prompt
  fmt           Reformat your configuration in the standard style
  force-unlock  Release a stuck lock on the current workspace
  get           Install or upgrade remote opentofu modules
  graph         Generate a Graphviz graph of the steps in an operation
  ...
```
<!--body:end-->

