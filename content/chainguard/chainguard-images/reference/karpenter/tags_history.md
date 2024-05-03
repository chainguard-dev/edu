---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/karpenter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/karpenter/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/karpenter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/karpenter/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:83b4361f303033c68a916d0e3c94bf4407a7f410c504e2c403fbe3956b7eb5c3` |
|  `latest`     | April 26th   | `sha256:9bf50de7cb239835c36bbc713843b08d18aa8e3182d6867311bd560457a69f1e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0-dev` `0.36.1-dev` `0.36-dev` | May 2nd      | `sha256:c4b5aed3eecc7887b084f2ca29bc95a303864134b68028db38c0748c840c142c` |
|  `0` `0.36` `0.36.1` `latest`                 | May 2nd      | `sha256:97cf424b2adbd18187f8aac7a7ed7e79f9aa1a5d70e0263853795f44ce8915da` |
|  `0.35` `0.35.4`                              | May 2nd      | `sha256:522835c066fd3f2c9ad82e82becfe4c8299130372b2131a081c390b5f9e13b91` |
|  `0.35-dev` `0.35.4-dev`                      | May 2nd      | `sha256:d0d43b83881842b799bdb0085f54322c98b147f4793a4d1fe2c4d199d2780675` |
|  `0.36.0-dev`                                 | April 24th   | `sha256:1b83625e12dddb2f149638a7285b740842a4170620be390641c328f205d033f2` |
|  `0.36.0`                                     | April 24th   | `sha256:0f1a24830639d33071b2b664059e959446c245422e297d1e10767a05c8d45df5` |
|  `0.27.2`                                     | April 19th   | `sha256:4920dd60eb95cc5ad09a92de21c100c4bfe6f10f9a1b493266009f2400294c73` |
|  `0.27.2-dev`                                 | April 19th   | `sha256:930f5d798690e11cfdede6413133fb4d96c03c7d502153060e267db2ef7373c4` |

