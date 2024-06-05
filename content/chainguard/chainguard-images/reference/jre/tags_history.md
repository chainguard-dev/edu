---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
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
|  `latest-dev` | June 1st     | `sha256:f987b7e16ac7ac32f7acb1436f1ed247f66ef469d29ee873e79b46299fd68978` |
|  `latest`     | May 30th     | `sha256:3694ef39efed5f5e8f51f81a3b0636d5d4f6d1d2172e550500764ac2055fa64e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-16.0-dev` `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev`   | June 1st     | `sha256:c3ea26557f2dec370c5faa84dc8302b9c317eb06e3e1c45ff85a1f62bf5a93c3` |
|  `openjdk-17.0.11-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | June 1st     | `sha256:3450d221689f81a3121daf1edaea1eff6369280fa1ea806b900ccdee329545de` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | June 1st     | `sha256:f2add71fa7c07d95dcd5c33af097da57fcb6e27e248ddba0c3333c9df6fabbb9` |
|  `openjdk-14-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev`  | June 1st     | `sha256:acb1ac58bc8a1156802c400b4bb03afdae4345af508a313ed386d2c652b056f3` |
|  `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` | June 1st     | `sha256:629d9722edc424a8a0690c53dc6c4df7615f852c2d9bb147cf04593b15bc9f69` |
|  `openjdk-8-dev` `openjdk-8.412.08-dev` `openjdk-8.412-dev`                        | June 1st     | `sha256:e287088f86daf698b91182933efc1fe39564ed4552c2c7cad11247f4d165a019` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | June 1st     | `sha256:463230ba142989cc169f85a4617e38ea34188b46872d75808241838b6ebd6fa9` |
|  `openjdk-22.0-dev` `latest-dev` `openjdk-22.0.1-dev` `openjdk-22-dev`             | June 1st     | `sha256:ff74438dc95f92e17075bb864f842850c73eab07fe645716e0f75c210fb6c038` |
|  `openjdk-14.0` `openjdk-14` `openjdk-14.0.2.12` `openjdk-14.0.2`                  | May 30th     | `sha256:9f6e225c8796c87255d1b4b62790a6038238465fa498f859307aba28d01da694` |
|  `openjdk-15.0.10` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0`                 | May 30th     | `sha256:5ccd17cbdf3942964dea972d71194c32a610b49574510b8528d3ce377c968950` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | May 30th     | `sha256:6a7090b93f1bef0514bf849f835b8905c6e06a338bb8e05d2cf43105285c44a5` |
|  `latest` `openjdk-22` `openjdk-22.0.1` `openjdk-22.0`                             | May 30th     | `sha256:0a90112d2ecfb1bace666023ef94092c57b73cc20676fb369e50b86a6e218a0e` |
|  `openjdk-17.0` `openjdk-17` `openjdk-17.0.11`                                     | May 30th     | `sha256:65fbda4c3b41d4f58cbe2867e36253c2d26e086be3be79e624f86e943e84f0fd` |
|  `openjdk-16.0` `openjdk-16` `openjdk-16.0.2` `openjdk-16.0.2.7`                   | May 30th     | `sha256:71ee530229bada5de058ca101b291d484141ef82e952b59b5b5e0b11cd9ddf96` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | May 30th     | `sha256:f11df5872f9f4ec0cf52fd861ce04a8a6ff6c7a8dee9681cc083854d5aa16319` |
|  `openjdk-8.412.08` `openjdk-8` `openjdk-8.412`                                    | May 30th     | `sha256:4300e16b46d94df59645b51fbdf9d689ac0fcb25a7f58e513c5813c9f3ccc44f` |

