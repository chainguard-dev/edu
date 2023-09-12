---
title: "Image Overview: karpenter"
type: "article"
description: "Overview: karpenter Chainguard Image"
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

[cgr.dev/chainguard/karpenter](https://github.com/chainguard-images/images/tree/main/images/karpenter)

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest`     | September 11th | `sha256:15788beb2a4168d8c75459a8c6a81bc6c1f63df7cfb8fe73ddfb34e7f8242949` |
|  `latest-dev` | September 11th | `sha256:d97c2b034d36727aa20b28f991d671a0ed178834a041f9019c5a68fe0bdf993f` |



Minimal image with Karpenter. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/karpenter:latest
```

## Using Karpenter

The Chainguard Karpenter image contains the `karpenter` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://karpenter.sh/preview/getting-started/getting-started-with-karpenter/) but edit
the Helm command to use the Chainguard image. To do this, you'll first need to retrieve the digest
of the Chainguard image, which you can do with
[crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane) or Docker:

```
$ DIGEST=$(crane digest --platform linux/amd64 cgr.dev/chainguard/karpenter:latest)
$ echo $DIGEST
sha256:8a178372c9e105300104d48065d61022fe1bd268737edaba4ac83e2c10159276

$ docker manifest inspect cgr.dev/chainguard/karpenter | \
  jq '.manifests[] | select(.platform.architecture == "amd64").digest'
$ echo $DIGEST
sha256:8a178372c9e105300104d48065d61022fe1bd268737edaba4ac83e2c10159276
```
Note that you need to specify the platform required to get the correct digest.

Finally, edit the `helm upgrade` command to include the following lines:

```
--set controller.image.repository=cgr.dev/chainguard/karpenter \
--set controller.image.digest=$DIGEST \
```

