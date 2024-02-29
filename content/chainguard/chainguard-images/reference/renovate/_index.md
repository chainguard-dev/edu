---
title: "Image Overview: renovate"
linktitle: "renovate"
type: "article"
layout: "single"
description: "Overview: renovate Chainguard Image"
date: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/renovate/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/renovate/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/renovate/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/renovate/provenance_info/" >}}
{{</ tabs >}}



Minimal Renovate image mirroring the `renovate:full` configuration to self-host the [renovate bot](https://docs.renovatebot.com/getting-started/running/#self-hosting-renovate).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/renovate:latest
```

### Pulling the Image

Run the following to pull the image to your local system and execute the command `--version`:

```shell
docker run --rm cgr.dev/chainguard-private/renovate:latest --version
```

You should get output similar to this:

```
37.6.3
```

You can run the renovate bot on a renovate test repo by using the following command:

```shell
export RENOVATE_TOKEN=github_personal_access_token
docker run --rm -e RENOVATE_TOKEN cgr.dev/chainguard-private/renovate:latest renovate-tests/gomod1
```

