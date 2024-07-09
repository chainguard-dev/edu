---
title: "Image Overview: mattermost"
linktitle: "mattermost"
type: "article"
layout: "single"
description: "Overview: mattermost Chainguard Image"
date: 2024-07-09 00:39:12
lastmod: 2024-07-09 00:39:12
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/mattermost/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/mattermost/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/mattermost/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/mattermost/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Community edition of Mattermost, a self-hostable chat service with file sharing, search, and integrations. It is designed as an internal chat for organisations and companies, and mostly markets itself as an open-source alternative to Slack and Microsoft Teams.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/mattermost:latest
```


<!--body:start-->
## Usage

To deploy Mattermost on Kubernetes, you can follow the [official documentation](https://docs.mattermost.com/install/install-kubernetes.html).

You can also jump to [official Helm Chart](https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-team-edition) if you want to deploy Mattermost using Helm.

You can also check [TESTING.md](https://github.com/chainguard-images/images-private/blob/main/images/mattermost/TESTING.md) for how we test and deploy the `Mattermost` image.
<!--body:end-->

