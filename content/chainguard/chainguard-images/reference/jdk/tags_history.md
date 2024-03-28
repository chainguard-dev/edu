---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 21st   | `sha256:c00f2614ae5432dd37ae408202d611727933be8385d76940a3ec0eb20bf9f7df` |
|  `latest-dev` | March 21st   | `sha256:dac4fe409b693cb1fd773330d2c445e3b33dbf6f5ae0e91996e87ee2d8d6f37a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-dev` `openjdk-11.0-dev` `openjdk-11.0.22-dev`                         | March 27th   | `sha256:d28d0eacbb588f9ae5c420901a5bad781351215be9a34128470bd676469de4a4` |
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | March 27th   | `sha256:54334eac7390fba68455bc7be41ce68e3ebe20fc190b8072fcac6d4b1867933e` |
|  `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0.2-dev`  | March 27th   | `sha256:221a996173501721551a7fa878451aa5b3515c69cba1e4ff4d51b9f3e1efd2fa` |
|  `openjdk-16` `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2`                   | March 27th   | `sha256:638aae90fc86c74ca55047160377e82e0f45ce14efb3f36ce3d02ff7abaedd45` |
|  `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0`                 | March 27th   | `sha256:fdf313b803fba972c1bcc4cc2736ff689db2cd1042b23ff58028cabdc365c5e2` |
|  `openjdk-21.0` `openjdk-21.0.2` `openjdk-21`                                      | March 27th   | `sha256:e0f0502a2def1eecb834a52d72b4e6015f4f773b6600202895403f54e9ef487d` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14` `openjdk-14.0.2`                  | March 27th   | `sha256:1975576ae22773cb18dddafb44b9357b2a7ec4e5009d844f1e7b3482ffeac791` |
|  `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0.2-dev`   | March 27th   | `sha256:51bec2d2e2dbf43946de49a2070346df9027d861212cbb1fdb528ca51d87491b` |
|  `openjdk-21-dev` `openjdk-21.0.2-dev` `openjdk-21.0-dev`                          | March 27th   | `sha256:9a6c784909646d8f0ec1202233707352a3b88df8f59a36f8e438b97c358aa9ab` |
|  `openjdk-11.0` `openjdk-11.0.22` `openjdk-11`                                     | March 27th   | `sha256:bb7226abee652ec7ad5fcd8e058416aadb5024903900784f0a2dbf8ceec2c695` |
|  `latest-dev` `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.0-dev`             | March 27th   | `sha256:3c18460b19cf1965765a1919cbdc8c017acb7033ca79ea5279cd965fb4dd4953` |
|  `openjdk-8.392-dev` `openjdk-8.392.08-dev` `openjdk-8-dev`                        | March 27th   | `sha256:d97bdeda8ce8ccdb2cab0894ad21c3a24da634af582cde035d26d30a53ad1d95` |
|  `openjdk-17` `openjdk-17.0.10` `openjdk-17.0`                                     | March 27th   | `sha256:6e8cf60bf45304a4531db3418a12842c5948feec0aa32d731a8fdc9e8637fab0` |
|  `openjdk-22.0` `openjdk-22` `latest` `openjdk-22.0.0`                             | March 27th   | `sha256:f37ca466631ed95d91e605147d58a134b6d420cdfff8d378da392b008eb51a65` |
|  `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | March 27th   | `sha256:56b07356b30dac0dbac422b8e91b60f0c69aa99537f767410983ff0a4c568e9c` |
|  `openjdk-17.0.10-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | March 27th   | `sha256:4e445142631f254f0072db8cae5b8957b57a06b4f450c804091e7f5efcde4379` |

