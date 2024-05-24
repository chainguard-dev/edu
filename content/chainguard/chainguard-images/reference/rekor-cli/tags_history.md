---
title: "rekor-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the rekor-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rekor-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rekor-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/rekor-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rekor-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 23rd     | `sha256:81808e25c79608642e916cc6b167bb8a4f93f242db1df29586259a588df30e01` |
|  `latest`     | May 23rd     | `sha256:6a4eebd671d8b1e21a3b2c95cf05c20f846caa8bf866eeddd2b0652e21f29231` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.3-dev` `latest-dev` `1-dev` `1.3.6-dev` | May 23rd     | `sha256:97eecc2eb83687d2f0e078ccc5666684e020b1018bfd0c429652649978248248` |
|  `1.3` `1` `1.3.6` `latest`                 | May 23rd     | `sha256:b62c3aef264a728e75f60be7acd49bed910007810de7d0229268f30380a133a8` |

