---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-02 00:32:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 1st     | `sha256:de46005f2761bd18a5a5085cd754011b3099642110907603aa2f698481e39f8e` |
|  `latest-dev` | July 1st     | `sha256:e8d04a7fb42eb128d92e3bf7a13f801e16f19d15e18ecc97b480369b700158cb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.7` `1.16`                              | June 28th    | `sha256:63f58b28956be43e4a4e5dd498896e15b7dd4acc7f013bafb4f0bee7a24092ce` |
|  `1.16.7-dev` `1.16-dev`                      | June 28th    | `sha256:14b585f514d40e4bb40906373996e441ebc878d082658e8302a17eec37ad02b2` |
|  `1.15-dev` `1.15.11-dev`                     | June 28th    | `sha256:12a906296d72f21c545c6146bfdff21f6eb390f298656317457855db50e81751` |
|  `1.15.11` `1.15`                             | June 28th    | `sha256:806debede516a08c137a14e5b93febaa1aba8ba27deeeec87779ed858ebeaed3` |
|  `1.17.4` `1.17` `latest` `1`                 | June 28th    | `sha256:c6bb1e91c3c3f09545b3a95804f296ff47250c3be75481937b522a762767342d` |
|  `1.17.4-dev` `1.17-dev` `latest-dev` `1-dev` | June 28th    | `sha256:637033704b2ffbdd7b200052711e6584764911272caf90a6f60451f9414687ce` |

