---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
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
|  `latest-dev` | June 6th     | `sha256:b8d783868cdaf379c6b5fba46e3d6e058ff8ae24b9f65b7e25bf80f1a8a7791b` |
|  `latest`     | June 6th     | `sha256:294c1c18c46cd9eb83db0ae950fcd903d51dab2f15cc266d52347a056c5c0421` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-22` `latest` `openjdk-22.0` `openjdk-22.0.1`                             | June 6th     | `sha256:d4cba237646c00ec18c42b5fba1d5eec65bd812b82571412413fa80665363708` |
|  `openjdk-22-dev` `latest-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev`             | June 6th     | `sha256:fe5c413571c7c2bc40efac8b38039b12e192f9727cdd58a92f207e2fa71f8b89` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10` `openjdk-15.0.10.5`                 | June 6th     | `sha256:8d25240c32fa9d12017eeabe51df91c1aa1a9997ae4291f9de95401f06674127` |
|  `openjdk-16.0-dev` `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev`   | June 6th     | `sha256:15a0a7315d00c396081110993bfded97e87f7c21280a3e6865b07f7d7d7fa96b` |
|  `openjdk-16.0.2` `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16`                   | June 6th     | `sha256:d54e1e85b1b8a0ceee083cc7b196a798fc9b941e8561c47a8b527b403ecdfb7b` |
|  `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | June 6th     | `sha256:3e92dd6cec6de64061ff62b6641d83c21ac62b36beadac8181055938378ccc13` |
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14`                  | June 6th     | `sha256:32a83d185d097bd6839af57abe73912520013f1aeabbf1f5daed3e20fda80f3e` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | June 6th     | `sha256:d887d381f693110c598102af3f8b274dea060dc031c1b7fdb9aaf67ae14b102a` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | June 5th     | `sha256:3450d221689f81a3121daf1edaea1eff6369280fa1ea806b900ccdee329545de` |
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | June 5th     | `sha256:f2add71fa7c07d95dcd5c33af097da57fcb6e27e248ddba0c3333c9df6fabbb9` |
|  `openjdk-8` `openjdk-8.412` `openjdk-8.412.08`                                    | June 5th     | `sha256:4300e16b46d94df59645b51fbdf9d689ac0fcb25a7f58e513c5813c9f3ccc44f` |
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | June 5th     | `sha256:463230ba142989cc169f85a4617e38ea34188b46872d75808241838b6ebd6fa9` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | June 5th     | `sha256:65fbda4c3b41d4f58cbe2867e36253c2d26e086be3be79e624f86e943e84f0fd` |
|  `openjdk-8-dev` `openjdk-8.412.08-dev` `openjdk-8.412-dev`                        | June 5th     | `sha256:e287088f86daf698b91182933efc1fe39564ed4552c2c7cad11247f4d165a019` |
|  `openjdk-21` `openjdk-21.0` `openjdk-21.0.3`                                      | June 5th     | `sha256:f11df5872f9f4ec0cf52fd861ce04a8a6ff6c7a8dee9681cc083854d5aa16319` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | June 5th     | `sha256:6a7090b93f1bef0514bf849f835b8905c6e06a338bb8e05d2cf43105285c44a5` |

