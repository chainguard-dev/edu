---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
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
|  `latest-dev` | June 28th    | `sha256:55147ce86108f20e9c63cf2c483904525edc39bfb5d11f6c58d573ec68feabdf` |
|  `latest`     | June 28th    | `sha256:53eff7d5cf0ed838d64a9cf69de7b97f5086f7b0150475c6896e5ec9c5414762` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | June 28th    | `sha256:56adaf407481b55404cf1e0b2762263a41356db21c42b184b839b8666d69a2a0` |
|  `openjdk-22` `openjdk-22.0.1` `latest` `openjdk-22.0`                             | June 28th    | `sha256:2cd7741e96ad56579bac80a80f1937ed91f9657fe77e9bf56d9256cfd75bbe2b` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | June 28th    | `sha256:92e4f9a3300284f79541515f22f8cbf8a99fcff2317a95d172b852c2d03ac18d` |
|  `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | June 28th    | `sha256:e468a47d0de586c20ed5a911759950a8bc051a99f455b490dc5ccc85ba0f1300` |
|  `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev` `openjdk-16-dev`   | June 28th    | `sha256:f8897ec6a8b427b06917e54f3f93696141b7c75113243aa1c96f57705a53df5b` |
|  `openjdk-8` `openjdk-8.412` `openjdk-8.412.08`                                    | June 28th    | `sha256:ef3cca4e10f6ae68468ccb77fdd1cd6c5c45a2d2f67f18e0c1220e4eefce8880` |
|  `openjdk-14` `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14.0`                  | June 28th    | `sha256:a10ba9539c79e4d0729773b0321f4e508d8cc151a05394fddf060dde3598f4cf` |
|  `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | June 28th    | `sha256:3027a229f707c8bd38b6a5adc3740c7cbe3afd9d8d82e23d6d4184346761f058` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | June 28th    | `sha256:b1920d488c79d4833bd3a55c30add0b197ff80d163fe44c8dcc07b717053c97d` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | June 28th    | `sha256:6d85b02b3b53ade87db54ace3e0e8c49b8ff1424d8680dcda88fc465216272db` |
|  `openjdk-22.0-dev` `openjdk-22.0.1-dev` `openjdk-22-dev` `latest-dev`             | June 28th    | `sha256:c0ffe6f8f9e542902ba15d0cfb5effa738ffbd4617468a04b4c7fb41f07f106b` |
|  `openjdk-16` `openjdk-16.0` `openjdk-16.0.2` `openjdk-16.0.2.7`                   | June 28th    | `sha256:2972211f1ae44f294940fb3fa33f8f65c01f3c377b4470a570db214b027d0bb6` |
|  `openjdk-15.0.10` `openjdk-15` `openjdk-15.0` `openjdk-15.0.10.5`                 | June 28th    | `sha256:b8459c4c5a69180bd6eec0ffebafda2e74878fca83e339c80047d5007be4c867` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.11-dev`                         | June 28th    | `sha256:90071b05af3e968d8693bec7aa048a21875b86dd729b1fa5ae9884d488b6c14f` |
|  `openjdk-21.0-dev` `openjdk-21.0.3-dev` `openjdk-21-dev`                          | June 28th    | `sha256:192b6d8b4fc3f7e859c509b297d26be7a61b88da023e99b402e41147f13ecaaf` |
|  `openjdk-11.0.23-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | June 28th    | `sha256:655ac49fdf1307e451b3cf4aa282da330ef09987ca79435a3c09a3157d0c294e` |

