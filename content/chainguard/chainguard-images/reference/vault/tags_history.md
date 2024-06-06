---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 2nd     | `sha256:a873af234cad221782367bad58e8a262a44048f68c04e1a07f7f7f735f8dbfb2` |
|  `latest`     | May 31st     | `sha256:27f8bd7517d7df0d6748e1ccd8d75e0d49cb3a9a5ea345968ae94fc03839199d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16` `1.16.3` `1` `latest`                 | June 5th     | `sha256:e750633df7cf9efabbb8788682c42447ef1905a0b6707d11bf61524a8f581b8f` |
|  `1.16.3-dev` `1-dev` `latest-dev` `1.16-dev` | June 5th     | `sha256:9084b65e76cc7cdf8fbb01e1dc744e3f8f80a2106c7e244e9a1dea53de2deadd` |
|  `1.14.12-dev` `1.14-dev`                     | June 5th     | `sha256:d32b45473fd7b8de7d21f67601572cefadf7bea3fc44b0bb950b645a8624ae37` |
|  `1.14` `1.14.12`                             | June 5th     | `sha256:f5f1766e9f39013e2af43387f10b92b846b6cdf9e920bac2ce855008c3e94e69` |
|  `1.15` `1.15.8`                              | June 5th     | `sha256:b684183246593f8ecb832fd606486d5984ee8535448ff3e881aa1153ed9bbbe3` |
|  `1.15-dev` `1.15.8-dev`                      | June 5th     | `sha256:642ca31530092adf16ff11c2a49cf478a68a09e8b5c12b691461fabd3e026d9c` |
|  `1.16.2-dev`                                 | June 1st     | `sha256:85725e757f182bc6867f8d3bfd667c06df6f3ea19bedf502002088fed57ac045` |

