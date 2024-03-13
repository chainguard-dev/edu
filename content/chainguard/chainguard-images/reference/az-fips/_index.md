---
title: "Image Overview: az-fips"
linktitle: "az-fips"
type: "article"
layout: "single"
description: "Overview: az-fips Chainguard Image"
date: 2024-03-13 00:52:18
lastmod: 2024-03-13 00:52:18
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/az-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/az-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/az-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/az-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Azure CLI
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/az:latest
```
<!--getting:end-->

<!--body:start-->

## Overview

Azure Command-Line Interface (CLI) used to create and manage Azure resources.
The Azure CLI is available across Azure services and is designed to get you
working quickly with Azure, with an emphasis on automation.

### Docker setup

To make sure you have the latest image version available, start by running a `docker pull` command:

```shell
docker pull cgr.dev/chainguard/az
```

Then, run the image with the `--version` flag to make sure it is functional:

```shell
docker run -it --rm cgr.dev/chainguard/az --version
```
You should get output similar to this:

```
azure-cli                         2.55.0

core                              2.55.0
telemetry                          1.1.0
...
```
<!--body:end-->

