---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
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
|  `latest-dev` | March 7th    | `sha256:08340e9deb777ed6af831b62ad25bfbd9d626fa706a132124c266fd4d44fe922` |
|  `latest`     | March 6th    | `sha256:f07c063df78dc741a38636b9c5e1b7610f14ee38099925f7158acdf526927464` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.12` `3.12.0`                              | March 7th    | `sha256:a4ab6584c944d435d81f7a2b80d510b1d5b13fd104b5603e7e3fad8cf9d3686f` |
|  `3.14.0` `3.14` `latest` `3`                 | March 7th    | `sha256:4c09af4de25937d101bd894e25a4dd138ef9dcf031d49de522e800236b222982` |
|  `3.13` `3.13.4`                              | March 7th    | `sha256:8ac04747ba8b924b21cfcbe1b1d8d06b6b0ed6d8dc12506be2064e214b2220d5` |
|  `latest-dev` `3.14.0-dev` `3-dev` `3.14-dev` | March 7th    | `sha256:bb8afa8ebc59e991d52d67a346fed88ccd4aeeb481ffed39483b7d886a8f9022` |
|  `3.13.4-dev` `3.13-dev`                      | March 7th    | `sha256:25d3dcdcacfa7784087ab09c5dc4423e20b63f068e54f425546ccccfa8b264ab` |
|  `3.12.0-dev` `3.12-dev`                      | March 7th    | `sha256:820a4e095c3c6f504710c6c16e8539fa8c6514ad81cd5c3eb69da5ed01b79500` |

