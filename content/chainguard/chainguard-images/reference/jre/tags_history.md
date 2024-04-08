---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
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
|  `latest-dev` | April 5th    | `sha256:c173704b288f5fbf4807bca2c3b4e1ff45fb0b0252efc98288d2f27b346d3367` |
|  `latest`     | March 28th   | `sha256:42ffe937ebd7f481639885e6e0d793789c5bcec647f3cd8beaba3288581e196a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.10-dev`                         | April 5th    | `sha256:1b3e6dea6f506c579ae76cfafcc1ac9aff4dda49c31056ee3f394966cc86994f` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.22-dev`                         | April 5th    | `sha256:c7d1bf6a3b590fc85798db44ad5ebdaa4ab4da7b24a1e322f236083085f0ad52` |
|  `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | April 5th    | `sha256:fb954ccc464d208ec893173ad8133d02b8bf5b9718bf733b9571fc355abb888d` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | April 5th    | `sha256:4cfb2294a7b1ed61701a5e93fe47fa88d395f5a51910cb0e1573ac2b50a17ac0` |
|  `openjdk-22.0.0-dev` `latest-dev` `openjdk-22-dev` `openjdk-22.0-dev`             | April 5th    | `sha256:f451b29af5eee01fa69f2d306fb462eb35086db882b870ac271e87b2ba75dcd3` |
|  `openjdk-8.392-dev` `openjdk-8.392.08-dev` `openjdk-8-dev`                        | April 5th    | `sha256:701d5c0114daa250e2765f11a3fd5ac6a420d4b587c198e4f71b5b25415be494` |
|  `openjdk-21.0.2-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | April 5th    | `sha256:b40e5f5395854326a01fddcf4b8a99c80e75275e807698d77585fc8642acb1a6` |
|  `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16-dev` `openjdk-16.0.2.7-dev`   | April 5th    | `sha256:7afe2c6029c6bc1775959a0cd1c28de90e572cbcd182f83f4ad29f4718b6c24f` |
|  `openjdk-22.0` `latest` `openjdk-22` `openjdk-22.0.0`                             | March 28th   | `sha256:ca818f359331ef98fd4db7f1a332e384e5959d48bc5b6143945a579249354e5e` |
|  `openjdk-21` `openjdk-21.0.2` `openjdk-21.0`                                      | March 28th   | `sha256:4de5381d2de037371d3002a066325242a62a0d5665dc8c2a834debfbbdb2b1ec` |
|  `openjdk-15` `openjdk-15.0.10` `openjdk-15.0` `openjdk-15.0.10.5`                 | March 28th   | `sha256:f8df439cc079513d04fcd1f3403b369cd5336ccceb12b37f949af7b096d4a1ae` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.22`                                     | March 28th   | `sha256:a7455928b2c6d8725e13a3659aec352a7a99e2936f026741e979870b520ea39a` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2` `openjdk-14`                  | March 28th   | `sha256:044ad3727afb45b63aa97878b8b1f76cbe1e4534d2274b8a14d681bfbfcd542e` |
|  `openjdk-17.0.10` `openjdk-17` `openjdk-17.0`                                     | March 28th   | `sha256:24115abc079fb3bd9de16b2507e68fdd497f85e9bb10ebcad1adca925684aa18` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0`                   | March 28th   | `sha256:c9b9fa231da3307202e253b719945e9d75535897874a19bf50dc9caec82431be` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | March 28th   | `sha256:352322c1270276d8dc473e469130cf5b0c9f20c5613e9dac3f5e5d7f11881d61` |

