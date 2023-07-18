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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:70c344c5250d58c8b01dc6af4e9c552e1dc5d67c5ee83babd1d7a2dfb64a8492` |
|  `latest`     | July 11th    | `sha256:1b8d7f33a13810d3e5bd24218087e08593354c5673c7b8480dc9369e8775a5ff` |
|               | July 4th     | `sha256:d76d1c0e6f120d5c42455995778122136ecf97829a860a3735e3315532f5063f` |
|               | June 26th    | `sha256:4a3d8f489e5e26aeca8997a090b8b94f714c404f68b91ff66d536ec5001166e2` |



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

