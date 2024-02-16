---
title: "Image Overview: dex"
linktitle: "dex"
type: "article"
layout: "single"
description: "Overview: dex Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-16 00:30:51
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/dex/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/dex/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dex/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dex/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[dex](https://dexidp.io) is a federated OpenID Connect provider.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/dex:latest
```
<!--getting:end-->

<!--body:start-->
## Using dex

`dex` has several operating modes, the most common being kubernetes, installed via `helm` using the upstream source shown below:

```bash
helm repo add dex https://charts.dexidp.io
helm install --generate-name --wait dex/dex -f values.yaml
```

An example `values.yaml` file is provided below:

```yaml
# values.yaml
image:
  repository: cgr.dev/chainguard/dex
  tag: latest

config:
  issuer: "http://127.0.0.1:5556/dex"

  storage:
    type: memory

  web:
    http: 0.0.0.0:5556

  expiry:
    deviceRequests: "5m"
    signingKeys: "6h"
    idTokens: "24h"
    authRequests: "24h"

  logger:
    level: "info"
    format: "text"

  oauth2:
    responseTypes: [ "code" ]
    skipApprovalScreen: false
    alwaysShowLoginScreen: false

  enablePasswordDB: true

  connectors:
  - type: mockCallback
    id: mock
    name: Example
```

> WARNING: The example above should _not_ be used in production, it simply exists to get up and running quickly.

For an incomplete values file that only contains the minimum required settings to use the Chainguard Images variant, use the snippet below:

```yaml
# non functional defaults! fill in with your own values.yaml
image:
  repository: cgr.dev/chainguard/dex
  tag: latest
```
<!--body:end-->

