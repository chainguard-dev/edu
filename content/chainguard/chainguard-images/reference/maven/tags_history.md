---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
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
|  `latest-dev` `openjdk-21-dev` | May 14th     | `sha256:a31ac15b62939ee49d7dd1f001bb1089b807bc0d666da89ef989ac0107fb42f4` |
|  `openjdk-11-dev`              | May 14th     | `sha256:bb61fded0660b7301e8bddcd5ac8e86449ad5c2783bd36e2ba5d155f5014e023` |
|  `openjdk-17-dev`              | May 14th     | `sha256:d8ab338b1bc6575f27900fdbdb05f226155478ccee50860d7a67442dcd76b673` |
|  `openjdk-21` `latest`         | May 13th     | `sha256:d49a54888b4e7c2c236b9409d0b287118fbe79446b68868a22ba451a8f25b6f6` |
|  `openjdk-11`                  | May 13th     | `sha256:64f225220340c7e9a049ccae61a5015a8f8dabca520f6a918d66db76641ab81c` |
|  `openjdk-17`                  | May 13th     | `sha256:cfe390dfd649846ebfc3afbfd1951acd571fc51a79aaaf185ec5cc9cdd20cb1d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-dev` `openjdk-11-3.9-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3-dev`              | May 14th     | `sha256:2aae50cd5ad71e669a7531be9da49e0840113a3e0a22cbaeb1dcfafd6ac0c6a3` |
|  `openjdk-17-3.9.6-dev` `openjdk-17-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev`              | May 14th     | `sha256:c3a47f8b490c67a1a902c6d6e3427e6d3c2be18a096f2f10d516cc5b8eda1948` |
|  `openjdk-21-3-dev` `latest-dev` `openjdk-21-3.9.6-dev` `openjdk-21-dev` `openjdk-21-3.9-dev` | May 14th     | `sha256:9fc8968764479d561f4ec415b74c0188809db6d130e5987b2493cfb72632cd2a` |
|  `openjdk-17` `openjdk-17-3.9.6` `openjdk-17-3` `openjdk-17-3.9`                              | May 13th     | `sha256:1a052c9cb5ca5cb609d667297b0f2642bb2f407b7e4239a6f1f5f106f8ba76c2` |
|  `openjdk-21` `openjdk-21-3.9` `openjdk-21-3.9.6` `latest` `openjdk-21-3`                     | May 13th     | `sha256:92ad1460a373a518d11ec834e60fa083b173644eb2118ed45fd8c136a1e60708` |
|  `openjdk-11-3.9.6` `openjdk-11` `openjdk-11-3.9` `openjdk-11-3`                              | May 13th     | `sha256:b1ee8619da65650b055d93456f938343066df12e44edffadd9be8b69cbd4cf0f` |
|  `openjdk-17-3.9.1`                                                                           | May 13th     | `sha256:0e4eaeb21b03f72e24767d4696b49935cd6b8838852d89e5243ba19fee27afc8` |
|  `openjdk-11-3.9.1`                                                                           | May 13th     | `sha256:617690269a5361add65e7ef9ed24d5daf94300c5728c41d796a92b680d7d5b41` |

