---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/az/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/az/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/az/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/az/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 15th     | `sha256:77f6fa4bfdae20337adb020e479942ce916a6840b08a0365720cc9b473548e1b` |
|  `latest`     | May 15th     | `sha256:3970e9441499f056c62914388e6c078a92ef5aba5538bbe59c6c80c7bae0b6b0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `2.60` `2` `2.60.0`                 | May 15th     | `sha256:752abbc68c2eadba77399dc849b3988190d39ed65ec57423cf41e8eae6811a37` |
|  `latest-dev` `2.60.0-dev` `2.60-dev` `2-dev` | May 15th     | `sha256:29f72977a363cf348c5552be5bd01efab617c7dcab9a6c046de5862b7714a078` |
|  `2.59-dev` `2.59.0-dev`                      | April 29th   | `sha256:2dae57e4903bb057f1152588ee958d5d9c4f06ca45a96a69942c18b79fce858a` |
|  `2.59.0` `2.59`                              | April 25th   | `sha256:3940fcf63420f9c47bb62f711da794643fe351ec83de9e84d5be4f55f4b20ede` |

