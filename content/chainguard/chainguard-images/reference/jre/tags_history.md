---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 12th   | `sha256:b191a17fdeff11e0d56b084ef11e683789f0e2ac239cfa5fcd8a80e37ae01bea` |
|  `latest`     | March 8th    | `sha256:8dd98b3edb5ec1038c108cc1e473e07aa3906c88b49afbbc5dd3cd9d8c7cb6bf` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8-dev` `openjdk-8.392.08-dev` `openjdk-8.392-dev`                        | March 12th   | `sha256:ff351c31c43a7149c4a9ad77fce170dc0a873b2bf154f413817ed331bbcc848e` |
|  `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` | March 12th   | `sha256:34f4cbadb03c4f7b7b6a44a5a8feb83d2766f5a2a59b902c71d30564747c6c85` |
|  `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | March 12th   | `sha256:fbea2861edd4d52f7ba62e68ee827e71e72095d86a1c0eec122bf3a4fe943bca` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `latest-dev` `openjdk-21.0.2-dev`             | March 12th   | `sha256:98c53e13e9148d23ca2e2da62e2ba66dde3b534f1228027d08396a0f081980b4` |
|  `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16-dev`   | March 12th   | `sha256:08277897085f09e52f1fbcaece280e4210c5da519a07582d23cc40df15a6e32c` |
|  `openjdk-11.0.22-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | March 12th   | `sha256:51febb1d0012f79f6d745074062dc0585dd2c237419e7df345517af5f353542c` |
|  `openjdk-17-dev` `openjdk-17.0.10-dev` `openjdk-17.0-dev`                         | March 12th   | `sha256:06f4411c853acbe7437ebd841b625fc4173d545360a665001c1ef6b6d5e6605f` |
|  `openjdk-21` `openjdk-21.0.2` `openjdk-21.0` `latest`                             | March 8th    | `sha256:4ee5f4d7672994fb4bb4333f9fe16d3c19788ecf1afbcf7251f2c48d40310520` |
|  `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15.0` `openjdk-15`                 | March 8th    | `sha256:2f8e9792675ab7528b8cd6d592bd37d6add0e77acd2a1da7d074fa318816e8a4` |
|  `openjdk-14` `openjdk-14.0.2` `openjdk-14.0` `openjdk-14.0.2.12`                  | March 8th    | `sha256:7ef80f172f8641c57a77b0fe05336106e379a46ebcc2c8bfa423256b9b109baf` |
|  `openjdk-8.392.08` `openjdk-8` `openjdk-8.392`                                    | March 8th    | `sha256:eefe47eedcd13b2275a1754d1be98f7a360f9a859894d6c66bd7c2256809b445` |
|  `openjdk-17` `openjdk-17.0` `openjdk-17.0.10`                                     | March 8th    | `sha256:babef543b96b66b46ee62eed5a4773659cdfa745b56d98471c9430cc71074a9f` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.22`                                     | March 8th    | `sha256:40714c48ca889b3aa4f53c2bdb7b039c38a5788043738c19875e5c3d6d4a7502` |
|  `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0`                   | March 8th    | `sha256:368ab28c975a4adfb3039c4d8713f095407e380dd09a0c91d4eff850af8be3c4` |

