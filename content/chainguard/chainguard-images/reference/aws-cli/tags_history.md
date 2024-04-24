---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-24 00:53:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 23rd   | `sha256:b231463a4586fb88d9e7c9de72bf6822b18ffcf1990a7e8cc186edba49671889` |
|  `latest-dev` | April 23rd   | `sha256:ac1bd5e3ec1a3265ffb8729aa82dfdbc69f68b7f189a24312383e73792283c2d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.32.71` `1.32` `1`                 | April 22nd   | `sha256:d4cca3f7a9b3b4b9a8bfe8e7648093f83a934590e2e62945f975d57ddf38e5b5` |
|  `1-dev` `1.32.71-dev` `latest-dev` `1.32-dev` | April 22nd   | `sha256:78ff8fcd5993c0692e7dd96af558464ce2014e57e7ce3f801dfbdf5024f0e4fb` |
|  `1.32.70`                                     | March 25th   | `sha256:6698fbd968e5d786f787afaa5ebb34feb88efa8297ea23a81342a988884b7c0f` |
|  `1.32.70-dev`                                 | March 25th   | `sha256:3bbbba05c5f5dadf3f55bb6f67bf775dd0be110cb2d33337215e5fd3ac798bda` |

