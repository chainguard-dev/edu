---
title: "Image Overview: authservice"
linktitle: "authservice"
type: "article"
layout: "single"
description: "Overview: authservice Chainguard Image"
date: 2024-06-23 00:43:06
lastmod: 2024-06-23 00:43:06
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/authservice/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/authservice/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/authservice/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/authservice/provenance_info/" >}}
{{</ tabs >}}

<!--overview:start-->

## Overview

authservice helps delegate the OIDC Authorization Code Grant Flow to the Istio mesh. authservice is compatible with any standard OIDC Provider as well as other Istio End-user Auth features, including Authentication Policy and RBAC. Together, they allow developers to protect their APIs and web apps without any application code required.


To get more information about the image, please visit the GitHub [repository](https://github.com/istio-ecosystem/authservice/).

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/authservice:latest
```


<!--body:start-->

## Usage

There are different ways to use the `authservice` image. You can try to run the image with the following docker-compose file:

```yaml
version: "3.9"

services:
  envoy:
    image: cgr.dev/chainguard/envoy:latest
    command: -c /etc/envoy/envoy-config.yaml --log-level warning
    ports:
      - "8080:80"
    volumes:
      - type: bind
        source: envoy-config.yaml
        target: /etc/envoy/envoy-config.yaml

  ext-authz:
    image: cgr.dev/chainguard-private/authservice:latest
    volumes:
      - type: bind
        source: authz-config.json
        target: /etc/authservice/config.json
```

> **Note**: You need to create the `envoy-config.yaml` and `authz-config.json` files in the same directory as the `docker-compose.yaml` file. You could find the contents of the files in the [GitHub repository](https://github.com/istio-ecosystem/authservice/tree/main/e2e/mock).


Then you should start the services:

```bash

docker-compose up -d
```

Once your services are up and running, you can access the `authservice` service by sending a request to the `envoy` service. The `envoy` service will forward the request to the `authservice` service.

```bash
curl http://localhost:8080
```

You should see the response from the `authservice` service:

```bash
Access allowed
```

<!--body:end-->

