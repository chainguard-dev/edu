---
title: "Image Overview: apache-nifi"
linktitle: "apache-nifi"
type: "article"
layout: "single"
description: "Overview: apache-nifi Chainguard Image"
date: 2024-05-20 00:48:18
lastmod: 2024-05-20 00:48:18
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/apache-nifi/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/apache-nifi/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/apache-nifi/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/apache-nifi/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Apache NiFi was made for dataflow. It supports highly configurable directed graphs of data routing, transformation, and system mediation logic.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/apache-nifi:latest
```


<!--body:start-->
### Usage

To get started with Chainguard's NiFi image, run it with Docker:

```bash
docker run -p 8443:8443 --name nifi cgr.dev/chainguard/apache-nifi:latest
```

NiFi will take a moment to start. Once it is finished, you'll see a message stating the Web UI is available:
     
```
NiFi has started. The UI is available at the following URLs
```

To obtain the username and password, check the Docker logs:

```bash
docker logs nifi | grep Generated
```

You can now access the Web UI at [localhost:8443](https://localhost:8443).

A user guide for NiFi can be found [here](https://nifi.apache.org/docs/nifi-docs/html/user-guide.html).

<!--body:end-->

