---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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
|  `latest-dev` | June 9th     | `sha256:c243045a31d9d14eaceefc74b3dbb359f80633518b33c7b3691e8ae77766eab9` |
|  `latest`     | June 6th     | `sha256:294c1c18c46cd9eb83db0ae950fcd903d51dab2f15cc266d52347a056c5c0421` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | June 8th     | `sha256:835109c7d9828a854e903b3309f119f9b6c9862521689fcf60985fbe762c4c85` |
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | June 8th     | `sha256:7340ad48800dafea2035614cabf76a527c110c8cff73f467f36a767a61255a22` |
|  `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev`   | June 8th     | `sha256:2abca0bc98e68ff0b689c46a026d072f5de9b6b8f77725bb4c0b43a02a4d89eb` |
|  `openjdk-11.0.23-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | June 8th     | `sha256:d950f8e3e0a5f47b130d34678d32e28a0f0c4a19171ba45a5bd9de0b99c891a9` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | June 8th     | `sha256:2fbd2b8a3998eaa7d2ef25dc8a3935911e85a58dd2fc299f9e6f551930aedbb1` |
|  `openjdk-14.0-dev` `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev`  | June 8th     | `sha256:2f79cd4b6db201a2edad9b56e5ba01bd6343756c059ad7d558792b4bf7c21049` |
|  `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` | June 8th     | `sha256:f2cd6e189bcf036d7034f037470d1d3bf1f68ff02306922098897a54424ead3a` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `latest-dev`             | June 8th     | `sha256:9b567c223e3ac892ff5328f870e95b82823adc40602cd1d17d0c45aa6b77a62c` |
|  `openjdk-8.412.08` `openjdk-8` `openjdk-8.412`                                    | June 7th     | `sha256:4d869ef53545dfaef562bcc980220295cb3fd0c7b3ccc5cce162199f10a6576c` |
|  `openjdk-22` `latest` `openjdk-22.0` `openjdk-22.0.1`                             | June 6th     | `sha256:d4cba237646c00ec18c42b5fba1d5eec65bd812b82571412413fa80665363708` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10` `openjdk-15.0.10.5`                 | June 6th     | `sha256:8d25240c32fa9d12017eeabe51df91c1aa1a9997ae4291f9de95401f06674127` |
|  `openjdk-16.0.2` `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16`                   | June 6th     | `sha256:d54e1e85b1b8a0ceee083cc7b196a798fc9b941e8561c47a8b527b403ecdfb7b` |
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14`                  | June 6th     | `sha256:32a83d185d097bd6839af57abe73912520013f1aeabbf1f5daed3e20fda80f3e` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | June 5th     | `sha256:65fbda4c3b41d4f58cbe2867e36253c2d26e086be3be79e624f86e943e84f0fd` |
|  `openjdk-21` `openjdk-21.0` `openjdk-21.0.3`                                      | June 5th     | `sha256:f11df5872f9f4ec0cf52fd861ce04a8a6ff6c7a8dee9681cc083854d5aa16319` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | June 5th     | `sha256:6a7090b93f1bef0514bf849f835b8905c6e06a338bb8e05d2cf43105285c44a5` |

