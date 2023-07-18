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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:f6cd6eec1a33ff25994554672f18b013c63e4510cea18d43d2ad8213977c9033` |
|  `latest`     | July 14th    | `sha256:36a99af2a9f19e5962aec3f9a012eefc7638044e3f2d4e0e8fa0419976a2b95b` |
|               | July 12th    | `sha256:8745d367c643f1b8504477b5fb985a27ded58b898c57eefe88d6692c248a19a0` |
|               | June 27th    | `sha256:54d9e45d239daa4a2455bb08ed3212b061163b8ad90e1b93d8226efb0c67de7c` |
|               | June 27th    | `sha256:17dc0fbbf99dd00377b000ae2e3ee5202ac19b72e13f17a3b8c6136ea7d3f502` |



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

