---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-07 00:51:54
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 6th    | `sha256:d5a4ad05d58561a44f4d200c6b7c63963a446774ec06bf75b1c8396289ad8889` |
|  `latest`     | March 6th    | `sha256:f07c063df78dc741a38636b9c5e1b7610f14ee38099925f7158acdf526927464` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.13.4-dev` `3.13-dev`                      | March 6th    | `sha256:f7da13d4269370ea4e933226c6a76b08bfc37bfa35a2449bd79bbd71329c777a` |
|  `latest` `3.14` `3.14.0` `3`                 | March 6th    | `sha256:2ecb32eef77e8d6259ddd3b66b5c6c77a850545018986d2bbcc601ecc9fa64eb` |
|  `3.13` `3.13.4`                              | March 6th    | `sha256:d832591952ad18945ba36edf6cd2f9fb945f89743ad2ee2fe3fa153c1e86e640` |
|  `3.14.0-dev` `latest-dev` `3-dev` `3.14-dev` | March 6th    | `sha256:a7749c538c541bce257597b4acb748718e2580120382081da93dfdce2efb4252` |
|  `3.12-dev` `3.12.0-dev`                      | March 5th    | `sha256:9e054bca14928ae79f7f8d66fd0dabfdb44451e87ff9c32476fbea20696709f4` |
|  `3.12` `3.12.0`                              | March 5th    | `sha256:f7e51dd5e386a33ac1c401c5b17c8ac979f7e9e3a36df63f2178f37f0dde7d42` |

