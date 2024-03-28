---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed | Digest                                                                    |
|--------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-21-dev` | March 27th   | `sha256:1cdf55c02bfb68fd184ba9a0a7a750b772c1baecf5cb5437f5a3453fcdd47788` |
|  `latest` `openjdk-21`         | March 27th   | `sha256:df57dd1bfa07b428527c79df63c736c7ac4bda7a838f0a9c747bd92ccf660710` |
|  `openjdk-11-dev`              | March 27th   | `sha256:4714dffa347671c6cd9c3d0e0ce5b6ce0b3d0e9ae5f0a4d376fd8f8333c525e0` |
|  `openjdk-11`                  | March 27th   | `sha256:26ad703665ea17445962097e6bba4fff3dbeed5eb861c838b68b414667bf0ec2` |
|  `openjdk-17`                  | March 27th   | `sha256:f2dcca6ef9a8f7de07449918341a00cf98c7cff19c3b8ce6e2942177fcdeb878` |
|  `openjdk-17-dev`              | March 27th   | `sha256:01996af210e7011a64babad4c5362abf373a5fbeaf64d3c0b434f698eea94cd0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-3.9` `openjdk-11` `openjdk-11-3.9.6` `openjdk-11-3`                              | March 27th   | `sha256:a55774494f0d9d622bb5ad1a18f9a4e9f9b776286856865ade63161fa5dcbdf0` |
|  `openjdk-21-3.9.6` `openjdk-21-3` `latest` `openjdk-21` `openjdk-21-3.9`                     | March 27th   | `sha256:f2d5cc8a5d309f7f42392fbd78db5e20f21ed6ade9aae9ac2e71be8b44650d5e` |
|  `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-dev` `openjdk-17-3.9.6-dev`              | March 27th   | `sha256:00f24a0ee8dc255c859cbac6cc1f2127353020f1d4dae49e0fd59c683e5fecd1` |
|  `openjdk-17-3.9` `openjdk-17-3.9.6` `openjdk-17` `openjdk-17-3`                              | March 27th   | `sha256:23503636949af1853bb87c2d4ea76f1cc576147d8b3594cc9a4659a2a96a73ad` |
|  `openjdk-21-3.9-dev` `openjdk-21-3-dev` `openjdk-21-dev` `latest-dev` `openjdk-21-3.9.6-dev` | March 27th   | `sha256:a2c35c6408e7e0b9e1e65e97b888f28897371aa32df5cc1c0b202fb8db159371` |
|  `openjdk-11-3-dev` `openjdk-11-3.9.6-dev` `openjdk-11-dev` `openjdk-11-3.9-dev`              | March 27th   | `sha256:694247066b731a0792766e90889097392e5dc55460888cb847c3975127fe1980` |

