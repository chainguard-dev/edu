---
title: "Image Overview: bash"
linktitle: "bash"
type: "article"
layout: "single"
description: "Overview: bash Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/bash/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bash/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/bash/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bash/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image with only Bash and libc. Suitable for running any small scripts or binaries that need Bash instead of the BusyBox shell.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/bash:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

You open up an interactive shell in the Bash Image with a command like the following:

```sh
docker run -it cgr.dev/chainguard/bash:latest /bin/bash
```

You can also use a bind mount to test scripts from your local machine on the Bash Image:

```sh
docker run -it --rm -v /path/to/local-script.sh:/container-script.sh cgr.dev/chainguard/bash:latest /container-script.sh
```
<!--body:end-->

