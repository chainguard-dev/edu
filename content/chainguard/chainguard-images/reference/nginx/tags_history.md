---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 1st      | `sha256:f88a263fe3c02e944aa654d6a6d7bb044a3aa6048e1a86b14f81ac6e6e4d0a14` |
|  `latest-dev` | May 1st      | `sha256:3d2fcf62e20d8db433bc1ad340c56be205a6f725ca618341ebf3c8c868179e40` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.24.0` `stable` `1.24`                     | May 2nd      | `sha256:63e23a6193cd1bd2c2d69c4946192390a949da0c341e62109f400176c295494b` |
|  `1-dev` `1.25.5-dev` `latest-dev` `1.25-dev` | May 2nd      | `sha256:76352634b1babff0626dd0ad61f53c7f2ff9dfb278fca2bbb7d186109594c2de` |
|  `1.25.5` `mainline` `1.25` `latest` `1`      | May 2nd      | `sha256:19a0cbc089b40326b41016ed9ae7607d8f24675b337dc58a7092cbfd8967de6f` |
|  `1.24.0-dev` `1.24-dev`                      | May 2nd      | `sha256:14a0f8003b3c5c16ce921d054b305a979e763e9ae0df8424531bf76e7e445ebe` |
|  `1.25.4`                                     | April 16th   | `sha256:677b3c605e597b50e973f0a8bc265756ae86bb8b294105defc9e97e02654ef57` |
|  `1.25.4-dev`                                 | April 16th   | `sha256:01447112852762699d88c95bc0e4c3f83f9b7a0ec7e416df9ab7e8fcbda9c5dd` |

