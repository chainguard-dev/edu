---
title: "wazero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wazero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/wazero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/wazero/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/wazero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/wazero/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 11th   | `sha256:4ccf5c66c30922a83a87e3b96f4c08835f1f61cc10fff51ec86fc4f80155c0cc` |
|  `latest`     | April 4th    | `sha256:820b3c637ff8b52017eb6e36091f0bd0ed0bf6bcb3e540adf4b44cd75b9ea4da` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.7-dev` `1-dev` `1.7.0-dev` | April 11th   | `sha256:9b2efa0651ddb5d06207f230565fc32cd08dd489e98975891b719811083e790e` |
|  `latest` `1` `1.7` `1.7.0`                 | April 3rd    | `sha256:0085750aebcf356339c8cf2c77d7ebab067aaae80414dd217c17ae52bb99233f` |
|  `1.6.0-dev` `1.6-dev`                      | March 14th   | `sha256:3c0a93ae52271f8a662a63303866ebc91c32392793a3de4624c27d1fa3f38a06` |
|  `1.6` `1.6.0`                              | March 14th   | `sha256:0836ad07b9c3792c5bcb7dea7fb71c5c871477b4726b0ced23186ed85c54bcf9` |

