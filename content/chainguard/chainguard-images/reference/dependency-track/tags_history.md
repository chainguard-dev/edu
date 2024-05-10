---
title: "dependency-track Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dependency-track Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dependency-track/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dependency-track/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dependency-track/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dependency-track/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 8th      | `sha256:5c1562d85bbde2449a19c36860576b809381adf5d8b4ee2cd4fae1c78f5ec8db` |
|  `latest`     | May 8th      | `sha256:cfc4586b2c27d575b8121777e153527e40dfd3f29610f19043e969ba0deef4ca` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4.11.0-dev` `4.11-dev` `4-dev` `latest-dev` | May 7th      | `sha256:725e491f81c5463bfa0c0d2484284908610d59ecf945f5cffd5fbf4553d49c48` |
|  `4.11.0` `4` `latest` `4.11`                 | May 7th      | `sha256:996df376317989e57a8bb319895e6c1e04ad7c80bac29814cdb1a2e50c5a0626` |
|  `4.10-dev` `4.10.1-dev`                      | May 2nd      | `sha256:c274b306b668e2d2a37122c866e927b6e574fdd6b669f137befae732c3d61fbb` |
|  `4.10.1` `4.10`                              | May 2nd      | `sha256:1d19779826424532fdd25332cdfa169d9909f037d015d4b606def95696e538d4` |

