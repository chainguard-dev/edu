---
title: "argocd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argocd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-06 00:43:57
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
|  `latest`     | May 2nd      | `sha256:7f0e50c26ba7ee171fecd8d3a18b62b1fa04eca18a5fe9492c5ce4adb95ac611` |
|  `latest-dev` | May 2nd      | `sha256:160f8b6b4f490a6849be93dd725425add2dd64c9a9a2ab7cbb3848dc13df0473` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.8.18-dev` `2.8-dev`                       | May 2nd      | `sha256:eef6d98907cbc445c8b95661ea7dddac630a40877e6a5ab9f1216dbfcf426df1` |
|  `2.8` `2.8.18`                               | May 2nd      | `sha256:5c9eeffa76b44367c0a6ad1c6a07e369e6096bc366506b00048c1fb2eed8c171` |
|  `2.9-dev` `2.9.14-dev`                       | May 2nd      | `sha256:db7f7a5a7ce85d762cccedb0cc56ca5613bd458337bb7ff9b3e09333ef3c1f33` |
|  `latest-dev` `2-dev` `2.10.9-dev` `2.10-dev` | May 2nd      | `sha256:a877d17dd8aa70a1e7255bb7ef44988ebdf0e4b73d07ac935bbe27c526925789` |
|  `latest` `2.10.9` `2.10` `2`                 | May 2nd      | `sha256:43362fb06988e6f2a1ccac541facd2995205d401d6160c97c7b91f42a4cc74c8` |
|  `2.9` `2.9.14`                               | May 2nd      | `sha256:0b43103e62a5f7c4bb565a429da51ec6329057893fb0802ec33eb427b436501c` |
|  `2.10.8-dev`                                 | April 30th   | `sha256:872cc6fcb00e697aea311d5cdd3bf4d740c91e3e9a318d06b956f3099431c8d2` |
|  `2.8.17-dev`                                 | April 30th   | `sha256:919149827054d3490063fe6fbe0a0aa78206cd186fbf3d921fdcbdb988395c4a` |
|  `2.9.13-dev`                                 | April 30th   | `sha256:0f35e1d8d32d21d568e81297c586dd7da3b8d384bda082af2014f337d2f9378e` |
|  `2.8.17`                                     | April 29th   | `sha256:69566465198b1c1db338e72ef27d64fdf73d42d53e1f98e2f87bda4deac725fa` |
|  `2.9.13`                                     | April 29th   | `sha256:7ba474287e591df4d20e953ef918b73eaeb1e26de762c9f8e37a4b109230e5b7` |
|  `2.10.8`                                     | April 26th   | `sha256:e48c512dff7dbdbd9fdefddf6bfe05e98bd77a4e35a468ef5f2fb0700ea4dfdf` |
|  `2.10.7`                                     | April 23rd   | `sha256:50218ae3b33b0af9c793dabba7435b8fb77a39521eda1bfc9d23945f6c54a5db` |
|  `2.10.7-dev`                                 | April 23rd   | `sha256:6262d1e511833ee8344116e6ab73e8a2f4eb2bb7fcbaf2113f8646552be641f5` |
|  `2.8.16`                                     | April 21st   | `sha256:f81b20ada8339a7d3848a356e20c93765e9d7a6106c6bca6d412c23975a8f5a5` |
|  `2.9.12`                                     | April 21st   | `sha256:90b28bf4160d99bff6af800dd334b561bc2867b7e4e96cca198383471f8ce5fe` |
|  `2.9.12-dev`                                 | April 21st   | `sha256:617bca4a2f42cb93c93d94d62a78918011b97ed3c37ba73c099254a079963cf2` |
|  `2.8.16-dev`                                 | April 21st   | `sha256:056792cc246aced905fb12271501f9eed528a3b22af8d43d937f921e728cdc17` |
|  `2.10.6-dev`                                 | April 11th   | `sha256:c2277302406e9642d8b57246cf2cc083389e7e7a81f5f25126ebd53c63ef15ca` |
|  `2.8.15-dev`                                 | April 11th   | `sha256:540f85d39410a3dc4ef0f320db5041f55cb22238a7509ec6797c0f0fa1e7ccee` |
|  `2.9.11-dev`                                 | April 11th   | `sha256:1ee148b262fe7953c4f201c9ad947c9f14dfef115b59bf546fa2a59804a9b58d` |
|  `2.10.6`                                     | April 9th    | `sha256:79f1a0a134129e3fe4d5b7701a4ff162679b156343d5adffaa88dae5a1600804` |

