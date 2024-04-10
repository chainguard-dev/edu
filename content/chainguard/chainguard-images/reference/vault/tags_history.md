---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-10 00:53:55
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
|  `latest-dev` | April 9th    | `sha256:cbc01c542db07e8f1ad42dc7e128e94245e9f463e35220fb929d32335ae23e2c` |
|  `latest`     | March 28th   | `sha256:7e9cf7926e07bc22fc0a2702c62294617150d262aba404adc92b358de8737d34` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.14-dev` `1.14.10-dev` `latest-dev` `1-dev` | April 9th    | `sha256:be1b75505f4a1dbbc3c565ee6b28d7a625feba80c7770e344278741ec5ce818a` |
|  `1.13.13-dev` `1.13-dev`                      | April 9th    | `sha256:c1346a21aad63f2c2557f99a5c264aa1d931f75d06775c6a20ad5c31a23e1626` |
|  `1.13` `1.13.13`                              | March 28th   | `sha256:6d59be0807b4cb738c4f300be9033903b4c51f4a190385d7110ae30be2a6b0c7` |
|  `latest` `1` `1.14` `1.14.10`                 | March 28th   | `sha256:e53f50a49ecf38393595171fc0acb1396b442dae0c1b0ca579dbfb80b643c574` |

