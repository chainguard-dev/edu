---
title: "Image Overview: zot"
linktitle: "zot"
type: "article"
layout: "single"
description: "Overview: zot Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/zot/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/zot/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/zot/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/zot/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [zot](https://github.com/project-zot/zot) binary. **EXPERIMENTAL**
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/zot:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Create a zot config file:

```
cat <<EOF > zot-config.yaml
distspecversion: 1.1.0-dev
http:
  address: 0.0.0.0
  port: 5000
storage:
  rootdirectory: /var/lib/zot/data
EOF
```

Create a fresh `data` directory (this will store all OCI blobs as
[OCI Image Layout](https://github.com/opencontainers/image-spec/blob/main/image-layout.md)):

```
rm -rf data && mkdir data && chmod go+wrx data
```

Run the server:

```
docker run --rm -p 5000:5000 \
  -v "${PWD}/zot-config.yaml":/zot-config.yaml \
  -v "${PWD}/data":/var/lib/zot/data \
  cgr.dev/chainguard/zot:latest \
  serve /zot-config.yaml
```

Then in another terminal, try pushing an image with crane:
```
crane cp \
  cgr.dev/chainguard/bash:latest \
  localhost:5000/demo:latest
```

Then try pulling and running the image:
```
docker run --rm \
  localhost:5000/demo:latest \
  -c 'echo hello world'
```
<!--body:end-->

