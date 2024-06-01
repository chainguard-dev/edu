---
title: "docker-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the docker-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/docker-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/docker-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/docker-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/docker-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 31st     | `sha256:866981ae545a7545141dfef0856ba0793f379a24c4bfe712b814e6d279e958df` |
|  `latest-dev` | May 31st     | `sha256:e0d31ce69cd6e1c8f2997d15183984dc6453c9efe30c08d3cac5ca4a20d3aaf4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `26-dev` `26.1-dev` `26.1.3-dev` `latest-dev` | May 30th     | `sha256:d0d265d1fa1a52da67de0fdd4d1bbaf7131efe7ca87e6c02d0c4701d30ac2d80` |
|  `latest` `26.1.3` `26` `26.1`                 | May 29th     | `sha256:a915161d0835cf064c6d3a3d6c10d911257ab8eff8873ac074da71dda69232a8` |
|  `24.0.6-dev` `24.0-dev` `24-dev`              | May 24th     | `sha256:2bd49653fd8754aa76a5582eddee88ca73b2be689de8484975e5a68e8d962ecf` |
|  `24` `24.0.6` `24.0`                          | May 23rd     | `sha256:c6524219a4d47932d6a7de77df8796768d9519a49fac59d10bb43e050cb125cf` |

