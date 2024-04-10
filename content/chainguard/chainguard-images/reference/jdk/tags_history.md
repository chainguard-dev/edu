---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-10 00:53:55
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
|  `latest-dev` | April 9th    | `sha256:827f18a2e31b06e572efa50f2fb97323f0238374eeb4bf59bc1f2ef712b509e3` |
|  `latest`     | April 9th    | `sha256:d0e3cf389cdaa8acb2eb85dcf318168469c5bd627d9d05045d1677f5af56b504` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8` `openjdk-8.392.08` `openjdk-8.392`                                    | April 9th    | `sha256:b1c3ff82c88703e2a85cba1ecbe61b8b10fca6f5b6acba471fbdadfd37550ede` |
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev` `openjdk-8-dev`                        | April 9th    | `sha256:0d105957246b328486e46f996d0fe46c696cd7cf8cf8e534981c6fbe2a334925` |
|  `openjdk-16.0` `openjdk-16.0.2` `openjdk-16.0.2.7` `openjdk-16`                   | April 9th    | `sha256:61ec68de8e8e833f0cfc7fddacbca5181c7ac6b4ee83fcb5d9dfbd359f1c8fc8` |
|  `openjdk-17.0-dev` `openjdk-17.0.10-dev` `openjdk-17-dev`                         | April 9th    | `sha256:b6d22664e12138d7390a8b7135d8e3f0ad04d602610644c9453a451f4586fb25` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14` `openjdk-14.0.2`                  | April 9th    | `sha256:075149191aaabb8f69405fcf45baa7259c6f37c004704f20b1f5e8efc6d6a250` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14-dev` `openjdk-14.0.2-dev`  | April 9th    | `sha256:8dc6aba997fb203c79f2d86804e1ca259242a8991b645760c60076f1f51567d5` |
|  `openjdk-15` `openjdk-15.0.10` `openjdk-15.0` `openjdk-15.0.10.5`                 | April 9th    | `sha256:607ad302db5d5042b95f4ba49c0a6a1bc40264d3c74c54223e18843ba01c152e` |
|  `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16-dev`   | April 9th    | `sha256:abf0bd7af8f158bbbeeb894e93f47d8eef8b565204e2ae767c92a087a7eed79a` |
|  `openjdk-22.0.0` `openjdk-22.0` `openjdk-22` `latest`                             | April 9th    | `sha256:61e18fd2bdbb6bc46d3b94a8cd9b09d2567dd95e8c572e7b562be59b23297390` |
|  `openjdk-22.0-dev` `openjdk-22.0.0-dev` `openjdk-22-dev` `latest-dev`             | April 9th    | `sha256:1061c9eff85096a0b56b46b8b8237154a6d0cc69b4d780a9d1ea897ed14ba721` |
|  `openjdk-21.0.2-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | April 9th    | `sha256:762189272bab7a2c4f16979f182e61b5556e364c483d1694feaa4c582aac811f` |
|  `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` | April 9th    | `sha256:93bfde3293b075ce6c3194880da02c64bbda87c36a12c1561b243e2a12fcb6cb` |
|  `openjdk-21` `openjdk-21.0.2` `openjdk-21.0`                                      | April 9th    | `sha256:4e7cc3a42df1bf17e6865cf6055a06d70531b3f445028b1674bead10879400a7` |
|  `openjdk-11.0.22` `openjdk-11.0` `openjdk-11`                                     | April 9th    | `sha256:5cf076d073b2eb901ee8686109fcdb3b809be9c168cc9ba25366093de6be3c84` |
|  `openjdk-17.0` `openjdk-17` `openjdk-17.0.10`                                     | April 9th    | `sha256:541e458fd972e15fc490aed47c9b529cb930f502c5bd686766a71643db5ca9e0` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.22-dev`                         | April 9th    | `sha256:fb10ed382b2d45b5f9f4ff4dac75ce19d8c6208b9230b8204522dbfca724d6a8` |

