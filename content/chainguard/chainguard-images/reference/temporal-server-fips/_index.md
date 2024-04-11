---
title: "Image Overview: temporal-server-fips"
linktitle: "temporal-server-fips"
type: "article"
layout: "single"
description: "Overview: temporal-server-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/temporal-server-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/temporal-server-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/temporal-server-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/temporal-server-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image for [Temporal](https://docs.temporal.io/), a durable execution platform that handles intermittent failures and retries failed operations
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/temporal-server-fips:latest
```


<!--body:start-->
## Usage

The default entrypoint for this image is `/etc/temporal/entrypoint.sh`

To test:

```shell
$ docker run cgr.dev/chainguard/temporal-server:latest start --config <config dir path relative to root (default: "config")>

USAGE:
   temporal-server [global options] command [command options]  

VERSION:
   1.22.0

COMMANDS:
   start    Start Temporal server
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --root value, -r value    root directory of execution environment (default: ".") [$TEMPORAL_ROOT]
   --config value, -c value  config dir path relative to root (default: "config") [$TEMPORAL_CONFIG_DIR]
   --env value, -e value     runtime environment (default: "development") [$TEMPORAL_ENVIRONMENT]
   --zone value, --az value  availability zone [$TEMPORAL_AVAILABILITY_ZONE, $TEMPORAL_AVAILABILTY_ZONE]
   --allow-no-auth           allow no authorizer (default: false) [$TEMPORAL_ALLOW_NO_AUTH]
   --help, -h                show help (default: false)
   --version, -v             print the version (default: false)
```

Notes: 

* Here's the docker compose repo link for further reference on how this image can run https://github.com/temporalio/docker-compose
* For Helm Chart working, here's the reference: https://github.com/temporalio/helm-charts/tree/master#install-temporal-with-helm-chart 
TLDR, for a miminal helm installation:

```
helm -n temporaltest install \
    --set server.replicaCount=1 \
    --namespace temporaltest \
    --create-namespace \
    --set cassandra.config.cluster_size=1 \
    --set prometheus.enabled=false \
    --set grafana.enabled=false \
    --set elasticsearch.enabled=false \
    --set server.image.repository=cgr.dev/chainguard/temporal-server \
    --set server.image.tag=latest \
    temporaltest . --timeout 15m
```
<!--body:end-->

