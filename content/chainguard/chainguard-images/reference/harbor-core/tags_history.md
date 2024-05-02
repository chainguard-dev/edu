---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 29th   | `sha256:3a814a86291f75b71f03c22e457dca2b9ddf8e92176ac2622864267f791c333f` |
|  `latest-dev` | April 29th   | `sha256:93a65cc31f22fb1d3b8faf6d6d5a2c5da4d92896dc9c39e1a51e92adccf1f4ff` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.10.2` `2.10` `2` `latest`                 | May 1st      | `sha256:243c97238f8da1fd144811dd971d245fb7c5fee1ce3e180c21bf0e02916c9807` |
|  `2.10.2-dev` `2-dev` `2.10-dev` `latest-dev` | May 1st      | `sha256:660495fa011a224e0c144be2f04417b02d78e3ece783df4dd9b233b03fd7108d` |
|  `2.8.6-dev` `2.8-dev`                        | May 1st      | `sha256:a2580666162954a7d00b751518e182c9afe8eff8aa47ced8574c546ff082ebd6` |
|  `2.9.4` `2.9`                                | May 1st      | `sha256:454dad19ae36bc9df1db1ca12339022555428f563ff6236c937b353ed37d98ed` |
|  `2.8.6` `2.8`                                | May 1st      | `sha256:5eb886af262dffc70bc9308dffda3a22bd484ec11579193d5f51dfbb3beba8bb` |
|  `2.9.4-dev` `2.9-dev`                        | May 1st      | `sha256:ab9982ff2932e77dfa7a4801f6870fd51a28bf81babfbfe2ecf2cd63a5d8cc35` |
|  `2.8.5`                                      | April 21st   | `sha256:0658ade46bdeda39ef4c73cb1b482e12054bec8d9d92b308519d94e65f7e376b` |
|  `2.8.5-dev`                                  | April 21st   | `sha256:dc04549f03607e7f9ce712f17398058a98f1a19092042f922830d1190f976229` |

