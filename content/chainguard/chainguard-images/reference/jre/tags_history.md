---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
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
|  `latest`     | May 30th     | `sha256:3694ef39efed5f5e8f51f81a3b0636d5d4f6d1d2172e550500764ac2055fa64e` |
|  `latest-dev` | May 24th     | `sha256:a9fc4404a3029beefd3c9bbd197f0848da57268ceb8111971093b49bf4493595` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-22-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev` `latest-dev`             | May 30th     | `sha256:d243dfc48ab82e44e1f19321818118a2ad5e6bc5e2fce488872910bcf24cfdad` |
|  `openjdk-14.0` `openjdk-14` `openjdk-14.0.2.12` `openjdk-14.0.2`                  | May 30th     | `sha256:9f6e225c8796c87255d1b4b62790a6038238465fa498f859307aba28d01da694` |
|  `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev`   | May 30th     | `sha256:64e6f97a6b86e5613ddc5215e142127c9e986aaa04908ab44fe27c8c730ac28b` |
|  `openjdk-15.0.10` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0`                 | May 30th     | `sha256:5ccd17cbdf3942964dea972d71194c32a610b49574510b8528d3ce377c968950` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | May 30th     | `sha256:6a7090b93f1bef0514bf849f835b8905c6e06a338bb8e05d2cf43105285c44a5` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | May 30th     | `sha256:3d6ffac589a5ebd86110c44c72bb2c70918d3b32836aa5e2b02f931250ecb9f2` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14.0.2-dev` `openjdk-14-dev`  | May 30th     | `sha256:5616b4ae6e65a49ffbd8cf8be2324c7b67f1f6c11850dfbade183835df5bb4ee` |
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | May 30th     | `sha256:8c60f5004122afdd7c4dd0422aff01b629d315c59d053501cc8fd194bd558572` |
|  `latest` `openjdk-22` `openjdk-22.0.1` `openjdk-22.0`                             | May 30th     | `sha256:0a90112d2ecfb1bace666023ef94092c57b73cc20676fb369e50b86a6e218a0e` |
|  `openjdk-17.0` `openjdk-17` `openjdk-17.0.11`                                     | May 30th     | `sha256:65fbda4c3b41d4f58cbe2867e36253c2d26e086be3be79e624f86e943e84f0fd` |
|  `openjdk-8.412.08-dev` `openjdk-8-dev` `openjdk-8.412-dev`                        | May 30th     | `sha256:37a9aa8df0753a3be0c17b9b8224c7edd768c4453b8ff6a9e88078a509acabee` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.11-dev`                         | May 30th     | `sha256:7a239d93d0f331b0cb34f0c84d5112739cfc0ba65867a56145c5458da715dc96` |
|  `openjdk-16.0` `openjdk-16` `openjdk-16.0.2` `openjdk-16.0.2.7`                   | May 30th     | `sha256:71ee530229bada5de058ca101b291d484141ef82e952b59b5b5e0b11cd9ddf96` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | May 30th     | `sha256:f11df5872f9f4ec0cf52fd861ce04a8a6ff6c7a8dee9681cc083854d5aa16319` |
|  `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | May 30th     | `sha256:096e54aacd42b4f2964cb7fcedaa6dbe7545a0843ccdfe5225611513ac819b8a` |
|  `openjdk-8.412.08` `openjdk-8` `openjdk-8.412`                                    | May 30th     | `sha256:4300e16b46d94df59645b51fbdf9d689ac0fcb25a7f58e513c5813c9f3ccc44f` |
|  `openjdk-8.392` `openjdk-8.392.08`                                                | May 24th     | `sha256:bee10fb31837f16c5619ab12bd23f4306aca19ccc0b9bcbe56414e409bf4df2c` |
|  `openjdk-8.392-dev` `openjdk-8.392.08-dev`                                        | May 24th     | `sha256:6b4e5dbd3bd694eb6e7e092b52b90a93912a07a68f83949a1f9dbf7f86345aed` |
|  `openjdk17.0.7.7-dev` `openjdk17.0.7-dev`                                         | May 24th     | `sha256:7ae7e3f4fd4d3ed8dc5079df0f2a3d8f5eb7a0bbb299c43b26087d0a0e606491` |
|  `openjdk17.0.7.7` `openjdk17.0.7`                                                 | May 24th     | `sha256:987c691df173a241a4398d60014a6f061e007e4323f19d9c487b95c7623dfeaa` |
|  `openjdk11.0.19.5` `openjdk11.0.19`                                               | May 16th     | `sha256:677dee78db811af812e1bb2bd33c1f247a5a4e0418169c194d965fc618768bba` |
|  `openjdk11.0.19.5-dev` `openjdk11.0.19-dev`                                       | May 16th     | `sha256:30327ab04c691b2d4f2bfa4391531384ea89b4e204cc65b90eee78a5cbc83156` |

