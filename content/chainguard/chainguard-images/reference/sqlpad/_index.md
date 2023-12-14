---
title: "Image Overview: sqlpad"
linktitle: "sqlpad"
type: "article"
layout: "single"
description: "Overview: sqlpad Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-12-14 00:19:07
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/sqlpad/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/sqlpad/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sqlpad/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sqlpad/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal Wolfi-based image for sqlpad, which is a web application for generating and running SQL queries and visualizing the results. For more information, please refer to the [applications documentation](https://github.com/sqlpad/sqlpad) on github.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/sqlpad:latest
```
<!--getting:end-->

<!--body:start-->
## Important note about data and docker

Unless data volumes are mapped outside the containers, you will lose data inside SQLPad and various database when the containers are shutdown and removed.

If you are using these examples as a starter for something you are working on, you may want to ensure your data is safe before getting into any serious work.

## Running from command line

```sh
# The most minimal example, mapping port 3000 to local docker host
docker run -p 3000:3000 cgr.dev/chainguard/sqlpad:latest

# volume and env vars being set and run in background
# directory `~/docker-volumes` must be shared with docker to work
docker run --name sqlpad -p 127.0.0.1:3000:3000 --volume ~/docker-volumes/sqlpad-postgres:/var/lib/sqlpad --detach cgr.dev/chainguard/sqlpad:latest

# To list running docker images
docker ps

# To stop running docker image by name. (otherwise use container id from `docker ps`)
docker stop sqlpad
```

## Deploying via Helm
A Helm chart is provided for deploying sqlpad in Kubernetes. This can be found in the applications [GitHub repository](https://github.com/sqlpad/sqlpad/tree/master/sqlpad-charts).
Below is an example, using the Chainguard image with the vendor's Helm chart:
```bash
git clone https://github.com/sqlpad/sqlpad.git && cd sqlpad/sqlpad-charts
helm dependency update
helm -n sqlpad install sqlpad  \
    --namespace sqlpad \
    --create-namespace \
    --set image.repository=cgr.dev/chainguard/sqlpad\
    --set image.tag=latest \
    ./
```
<!--body:end-->

