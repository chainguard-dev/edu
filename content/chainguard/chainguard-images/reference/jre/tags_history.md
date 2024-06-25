---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
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
|  `latest-dev` | June 24th    | `sha256:937ea69d34e2c8283ab338e44d636e876fd0664e5d60b1f5ebf481dbad540267` |
|  `latest`     | June 24th    | `sha256:55990d6994ef1c5b50b05d0be5ce7b3d45e6f992018133cc725aa6436595a7f9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | June 24th    | `sha256:994a1a9970d94263eb157aa3e3d331d54e5f5ca53b5c3d3072a33eec78629d54` |
|  `openjdk-22-dev` `openjdk-22.0-dev` `latest-dev` `openjdk-22.0.1-dev`             | June 24th    | `sha256:42c93ad4ba7ee5de4c80532e99db828b5b08917c7081aaba409066bc9679ede0` |
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | June 24th    | `sha256:3d8629cf000079336001a1e9a494612dcdad9551f61625ede5e98f2ae60ee093` |
|  `openjdk-8.412` `openjdk-8` `openjdk-8.412.08`                                    | June 24th    | `sha256:760eee089a5a457286c86c9d0978ef387d8505ae0c48c3e4e8a446a8c5a0da63` |
|  `openjdk-22.0` `openjdk-22.0.1` `openjdk-22` `latest`                             | June 24th    | `sha256:1b96694e2410033be933819340a5fab4a6ef2ea14be7e1020210fb7018880fde` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | June 24th    | `sha256:6dc794bf3e573d80c42c87e6806ad4311ecb3b2411c53487ebef2762c89029fb` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | June 23rd    | `sha256:50701d026d72daf479234806d4d0a8d228972d59bb215b1a0bc2b016ea7f2587` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev`   | June 23rd    | `sha256:49455ac7bed4ec0658cb4d3d6b9a0b2c23b178b8305aaba6849f6bd645166944` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | June 23rd    | `sha256:7ce11cf39b891908aecabb33887af34fdd22a2da72e07f4874ba8916e2bf9eff` |
|  `openjdk-17-dev` `openjdk-17.0.11-dev` `openjdk-17.0-dev`                         | June 23rd    | `sha256:f87841c552e67f33a9eac866704de625946e50c04cfab7a323d688dbf27004de` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | June 23rd    | `sha256:9d830a31f0b3f2af3f5f39f9e89c2f2aace25e9660c7e80c3b0f8b16f9b92735` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0.2`                  | June 21st    | `sha256:82b80dcfc13d06d1993e65b5a70607a36cba6a89c81b72125527e75ed2908ba2` |
|  `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15` `openjdk-15.0.10`                 | June 21st    | `sha256:42c8eb7e2af013209a60a7790a9f0172ac9b5c840eebfc43f7dcadda6efa9f53` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | June 21st    | `sha256:7512f448eeac1db9b60bafa33b34723ba2f0dfc2057fd884a1de238f43147875` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0`                   | June 21st    | `sha256:ce37fa61a748b8e3eabf9573c5f4fffd18d0e9eb42a215be896aa0d516eb2c3c` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | June 21st    | `sha256:15cc64da72bd170da9338e3c33d16f40d1e7e4be6cc9149222afd4e672e1cadb` |

