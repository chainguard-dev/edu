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
|  `latest`     | August 3rd   | `sha256:d6e5a6caa40403633182137322efe1a8f65484771a7796f61c25f8972e29d781` |
|  `latest-dev` | August 3rd   | `sha256:bb81a33d5ac8ec3fcad24e88591a824f179230c30d02ede517ba32ea860cb322` |



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

