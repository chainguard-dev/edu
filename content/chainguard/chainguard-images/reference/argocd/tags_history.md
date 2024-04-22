---
title: "argocd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argocd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argocd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 5th    | `sha256:fe69663fa01f007889fee5d36e08ccadab0337ff795404dffbfde86fbc617c25` |
|  `latest-dev` | April 5th    | `sha256:fe53c69165514dd9c9c512c3591d36eef877123b2bf97487867c50918d7a63e7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.8` `2.8.16`                               | April 21st   | `sha256:f81b20ada8339a7d3848a356e20c93765e9d7a6106c6bca6d412c23975a8f5a5` |
|  `2.9` `2.9.12`                               | April 21st   | `sha256:90b28bf4160d99bff6af800dd334b561bc2867b7e4e96cca198383471f8ce5fe` |
|  `2-dev` `2.10-dev` `latest-dev` `2.10.7-dev` | April 21st   | `sha256:c22f3564106c3d1ba504dd834a2cc3c936c8b24b97be0063c301bed32cdaf0e8` |
|  `latest` `2.10.7` `2.10` `2`                 | April 21st   | `sha256:bf23cb09d5a16fe727012a9ef7973e2f92e9c1c2459f1727f113f6db91027823` |
|  `2.9-dev` `2.9.12-dev`                       | April 21st   | `sha256:617bca4a2f42cb93c93d94d62a78918011b97ed3c37ba73c099254a079963cf2` |
|  `2.8-dev` `2.8.16-dev`                       | April 21st   | `sha256:056792cc246aced905fb12271501f9eed528a3b22af8d43d937f921e728cdc17` |
|  `2.10.6-dev`                                 | April 11th   | `sha256:c2277302406e9642d8b57246cf2cc083389e7e7a81f5f25126ebd53c63ef15ca` |
|  `2.8.15-dev`                                 | April 11th   | `sha256:540f85d39410a3dc4ef0f320db5041f55cb22238a7509ec6797c0f0fa1e7ccee` |
|  `2.9.11-dev`                                 | April 11th   | `sha256:1ee148b262fe7953c4f201c9ad947c9f14dfef115b59bf546fa2a59804a9b58d` |
|  `2.10.6`                                     | April 9th    | `sha256:79f1a0a134129e3fe4d5b7701a4ff162679b156343d5adffaa88dae5a1600804` |
|  `2.8.15`                                     | April 5th    | `sha256:4a14231bbd42371a1f1c1183e7b2a6cc913119c474df8d41a58f2c24f12715e0` |
|  `2.9.11`                                     | April 5th    | `sha256:d814fdb62605b424e8640d3d983310e1b069704cb0a61d3dd0f042835a9acf01` |
|  `2.8.14`                                     | April 3rd    | `sha256:a9e5ba91622614cac1366a3de93634b2fa13b43618654375185a9cb1ae1da714` |
|  `2.9.10`                                     | April 3rd    | `sha256:e0da385f642aff4ad7bc0841b0691c9220635b27058669e55f9889b74a809c67` |
|  `2.9.10-dev`                                 | April 3rd    | `sha256:0f94626de1aa4cbf48f16ef2565b65066019e5ec67c83b3258e6f28910a98c01` |
|  `2.8.14-dev`                                 | April 3rd    | `sha256:6f92defc78b76776ea203f7f3daa77e4f7d8e53f5174abe353d029e72a56b91f` |
|  `2.9.9-dev`                                  | April 2nd    | `sha256:ca4341f0ff9da260199e444affa71453656ac54fa7d30283070d26cd4f45a7d7` |
|  `2.10.5-dev`                                 | April 2nd    | `sha256:c1fe8c05a190e88b614abbfbbe423d78b54021e160d65f589ce1ccbf60eecc00` |
|  `2.10.5`                                     | March 28th   | `sha256:f357620790b95c3e5c23e894bddc091a55c798039d163b757ddc1221676c0db8` |
|  `2.10.4-dev`                                 | March 28th   | `sha256:b7c95ad651a2a8c2223439084ba18d42d5d3ab88f9be57bbc358fcaed8ff783d` |
|  `2.8.13`                                     | March 28th   | `sha256:0b57c67c7295d963b4786de2b58a14cba682f2e0d62eb417267e54f1ff3b9311` |
|  `2.9.9`                                      | March 28th   | `sha256:39586c48eade21d63f61e579ba1fd4ef9a35511eac4bd26cc7bddeae81449837` |
|  `2.8.13-dev`                                 | March 28th   | `sha256:4d31e6e9ae109f6806e077b718d4ea4d03ce711b129f92dfea78dc65c790785f` |
|  `2.10.4`                                     | March 28th   | `sha256:b9b7627e97b464ca7541420320a2ca0cdc129ac258dc1314e1363550872db6fc` |

