---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 28th    | `sha256:55147ce86108f20e9c63cf2c483904525edc39bfb5d11f6c58d573ec68feabdf` |
|  `latest`     | June 28th    | `sha256:53eff7d5cf0ed838d64a9cf69de7b97f5086f7b0150475c6896e5ec9c5414762` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-15.0.10` `openjdk-15` `openjdk-15.0` `openjdk-15.0.10.5`                 | July 2nd     | `sha256:410fcd3a4f076e4709e1517015d45e0e37c0a481784d446861213e372c393169` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | July 2nd     | `sha256:a0cf34e6aa3fffe84dfa03e61d76a18a019008c97552972ba456d10a3173ca9a` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | July 2nd     | `sha256:ea760e82438bc4b2aa168632cd40726ca24ae2a7487056c214fdf099ce678397` |
|  `openjdk-17.0.11-dev` `openjdk-17-dev` `openjdk-17.0-dev`                         | July 2nd     | `sha256:7d3fc5a98ea530254bdf281c7bb7579d108548368a8a3670dca6df78831107c1` |
|  `openjdk-22.0` `openjdk-22` `latest` `openjdk-22.0.1`                             | July 2nd     | `sha256:deef2cc7a455feda45835349c371f45a64861ba4b59c310e68ca13110d17c229` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0.2.12` `openjdk-14.0`                  | July 2nd     | `sha256:4ba018de255628ab45a11a744eec8e1a89cef404b27525d71b0221c3c812218b` |
|  `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev` `openjdk-16-dev`   | July 2nd     | `sha256:c5aa1babfcbc4dbaabdef64fa5924df461fd0f4169f20959c4c5a26031c73fb8` |
|  `openjdk-17` `openjdk-17.0` `openjdk-17.0.11`                                     | July 2nd     | `sha256:cb68d6b0740bde0532efbc0ab4850c52c1748b072abaa2196bc33a31f9725632` |
|  `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | July 2nd     | `sha256:883e4d16687edb927b8b790fbfe86486ba620fa000bcd956df40ebeeef03c0e0` |
|  `openjdk-16` `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2`                   | July 2nd     | `sha256:5587675ba1b637adba2aae5d3d3313f3302a718e25a43e9399bf0fd4079839d1` |
|  `openjdk-22.0-dev` `latest-dev` `openjdk-22-dev` `openjdk-22.0.1-dev`             | July 2nd     | `sha256:60bc5ee6d3417681e2eb2fd50ab35488c21bb1afed22764c6a28f3221109343a` |
|  `openjdk-11-dev` `openjdk-11.0-dev` `openjdk-11.0.23-dev`                         | July 2nd     | `sha256:3e4ad96fda7d73e7e9adba977a6c2e08168dc289acc25f55230f4e8437f15a81` |
|  `openjdk-8.412-dev` `openjdk-8.412.08-dev` `openjdk-8-dev`                        | July 2nd     | `sha256:8faa0d84ca31bd7a969bbfd66c16ebdedc31af4f8e75637d4c939c1dd0e4d695` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | July 2nd     | `sha256:16a364da1a1d817a04da8e5b286499881c8756c4fdd848b889e1a7f916b42ba3` |
|  `openjdk-8.412` `openjdk-8` `openjdk-8.412.08`                                    | July 2nd     | `sha256:0473f2ecdd7991f413b65e47f7ab7cfa59f7c02a1c67257b5550557f0f594d61` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | July 2nd     | `sha256:3bd0c9fb1fee9c6bdc4169aacf59f29f83071b5b8f79600db451c2ff3dbb440d` |

