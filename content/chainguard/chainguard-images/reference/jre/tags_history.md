---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
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
|  `latest-dev` | April 1st    | `sha256:d6078b1cefba13a92b762f8bce26dc164028a0f350e72429771066dfa6287d27` |
|  `latest`     | March 28th   | `sha256:42ffe937ebd7f481639885e6e0d793789c5bcec647f3cd8beaba3288581e196a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` | April 1st    | `sha256:95b8978387692ac958bb9ad09e0f146af1ba0f5a3738bf5b63ddff268246d034` |
|  `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | April 1st    | `sha256:a765c008beb7b24ecded99957b319cc87ee900a1a7c451aa1c44727bc82f9708` |
|  `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0.2-dev`   | April 1st    | `sha256:06b025c26acce404030315f09dbc916ebe12adf32b3358e57d439e4d7a02632b` |
|  `openjdk-11.0.22-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | April 1st    | `sha256:fcd17afe384f8dcb8afb72dc6c5fd5711096af71079dc27ed29aa1814ec99157` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `latest-dev` `openjdk-22.0.0-dev`             | April 1st    | `sha256:43d7046a3e0316e6b69c159cd0429d7f064fa529be254574b9586e45c11feb58` |
|  `openjdk-8.392.08-dev` `openjdk-8-dev` `openjdk-8.392-dev`                        | April 1st    | `sha256:3e4570fa02c7c876de09475e68192ec60fc8127470fc6b5e9d6975204f1acaeb` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.10-dev`                         | April 1st    | `sha256:7c3af6da443523e73423ef812abd76ec1f2dc32ce6c549ed9caf3aee491981d9` |
|  `openjdk-21.0-dev` `openjdk-21.0.2-dev` `openjdk-21-dev`                          | April 1st    | `sha256:ab3bf92d66551985d4ca2ac9f1e6e3b611e3f9b57a3991b023fa435a26971760` |
|  `openjdk-22.0` `latest` `openjdk-22` `openjdk-22.0.0`                             | March 28th   | `sha256:ca818f359331ef98fd4db7f1a332e384e5959d48bc5b6143945a579249354e5e` |
|  `openjdk-21` `openjdk-21.0.2` `openjdk-21.0`                                      | March 28th   | `sha256:4de5381d2de037371d3002a066325242a62a0d5665dc8c2a834debfbbdb2b1ec` |
|  `openjdk-15` `openjdk-15.0.10` `openjdk-15.0` `openjdk-15.0.10.5`                 | March 28th   | `sha256:f8df439cc079513d04fcd1f3403b369cd5336ccceb12b37f949af7b096d4a1ae` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.22`                                     | March 28th   | `sha256:a7455928b2c6d8725e13a3659aec352a7a99e2936f026741e979870b520ea39a` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2` `openjdk-14`                  | March 28th   | `sha256:044ad3727afb45b63aa97878b8b1f76cbe1e4534d2274b8a14d681bfbfcd542e` |
|  `openjdk-17.0.10` `openjdk-17` `openjdk-17.0`                                     | March 28th   | `sha256:24115abc079fb3bd9de16b2507e68fdd497f85e9bb10ebcad1adca925684aa18` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0`                   | March 28th   | `sha256:c9b9fa231da3307202e253b719945e9d75535897874a19bf50dc9caec82431be` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | March 28th   | `sha256:352322c1270276d8dc473e469130cf5b0c9f20c5613e9dac3f5e5d7f11881d61` |

