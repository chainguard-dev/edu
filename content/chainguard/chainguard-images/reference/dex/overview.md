---
title: "Image Overview: dex"
type: "article"
description: "Overview: dex Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/dex](https://github.com/chainguard-images/images/tree/main/images/dex)

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 7th | `sha256:0a05871e1f59b06d01192c26ee4db787fcff442df71a8ec5e2dea919b73ade3e` |
|  `latest`     | September 7th | `sha256:fcabcbdf7b66de95227c98d23afbd84627eb04bba7dd832b4ad549721400bfc6` |



[dex](https://dexidp.io) is a federated OpenID Connect provider.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/dex
```

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

