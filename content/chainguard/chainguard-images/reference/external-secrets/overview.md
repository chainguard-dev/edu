---
title: "Image Overview: external-secrets"
type: "article"
description: "Overview: external-secrets Chainguard Image"
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

[cgr.dev/chainguard/external-secrets](https://github.com/chainguard-images/images/tree/main/images/external-secrets)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:1fc194a3841e8fc4e5aecfa54437b7affe89d98f38ade69e843d366fd5650246` |
|  `latest`     | July 14th    | `sha256:6d0bce976f04816dcef1d3f163b19457bc9922ca77681d60eb44cdc912ea3a80` |
|               | July 12th    | `sha256:034ffdc1a6399f7b72131988b30bacd373fdd680fbeb6474cf96dd63c136ca2e` |
|               | July 7th     | `sha256:0f6319818aa52823d8dfb70270065316f82112494eb8c80888edf2abd1b0aab4` |
|               | July 7th     | `sha256:66c18ef07d8656170434a4f0f9d3a7510889bff7038326909b56a88d474af2a1` |
|               | June 21st    | `sha256:6d18968c3766633de27665dd134b4dc711c927b53cbb924917ffb966b1540d30` |
|               | June 21st    | `sha256:d55cd0e0c7d6db36b61a6456d49db6d3a5dbac977fa023a14718a5ef91619aab` |



Minimal External Secrets image 

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-secrets:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
  
$ helm repo add external-secrets https://charts.external-secrets.io
$ helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --set image.repository=cgr.dev/chainguard/external-secrets  \
    --set image.tag=latest \
    --create-namespace 
    <other configuration parameters here>
```

See the [configuration](https://github.com/external-secrets/external-secrets/tree/main/deploy/charts/external-secrets) docs for more examples.

