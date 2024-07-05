---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 3rd     | `sha256:75749da41c0d9bb46fe94500c1a9d002ae4aa574db06f696d67320e85c724de2` |
|  `latest-dev` | July 3rd     | `sha256:449d88a17244b559956b7cfb2b3559325bd452acc2056f05d4dfaf1f8ef651d5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev`   | July 4th     | `sha256:cec978d9c98f46eca318e0f2cbefccdd3bca5f864635cd6b5ba7a71f0ade8871` |
|  `openjdk-8.412.08-dev` `openjdk-8-dev` `openjdk-8.412-dev`                        | July 4th     | `sha256:eebb23f228b07119937175b9ce7d34de78256e29f36dbd59e0ae7b2df6607c0d` |
|  `openjdk-16` `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2`                   | July 4th     | `sha256:5827e88b557244a5188173f09704294914433cf7354f8b9d391731a9077ff974` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14.0.2` `openjdk-14`                  | July 4th     | `sha256:2a8ba3f15271461004e4f516bf8eed44b1eba67a8914577da413c87b1f7f817c` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | July 4th     | `sha256:93554e1ffc42e79789557e0f7912e77dca133190d86ff8814c5df712f14f1dc5` |
|  `openjdk-22` `latest` `openjdk-22.0` `openjdk-22.0.1`                             | July 4th     | `sha256:1dcd008d28a1dc9849454087db7a8bcaab1c2afcfa441f342b7cb4de6280e1f9` |
|  `openjdk-11.0.23-dev` `openjdk-11-dev` `openjdk-11.0-dev`                         | July 4th     | `sha256:0215e2de1a3fde8e12c45e55b4244505c0f0328b8ff05b7039f9de3d4bf316b1` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.11-dev`                         | July 4th     | `sha256:efc4fad528b031e658c58219bf6389cc7ebccd3d6c47c3077d137ae6af36d9cc` |
|  `latest-dev` `openjdk-22.0.1-dev` `openjdk-22-dev` `openjdk-22.0-dev`             | July 4th     | `sha256:db82ad57a4135d8232c1ff66ede9d0d0785eec9a7160be1b3179c03910ae3dc0` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | July 4th     | `sha256:b0c9b0abd8d8ff77998594270ad73aff3b8b6192a2277a114df4037c5c9dc82c` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` | July 4th     | `sha256:0b499316b399a1b9fba74e3a1f02126203efd06e42ce07391e93c58487998c63` |
|  `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev`  | July 4th     | `sha256:65e7ff726d52efd7b18d05b8154709f841437baf821b73127d4322e65f12762d` |
|  `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0.10` `openjdk-15.0`                 | July 4th     | `sha256:6336d714bc66ac7c8fc6dce1ca1210004f5ee1ed77133e19919c04f2e3abf676` |
|  `openjdk-17.0` `openjdk-17` `openjdk-17.0.11`                                     | July 4th     | `sha256:20631e7d23d19980472731b05200a99e30c0918f721be0847fc51872d078e032` |
|  `openjdk-8.412.08` `openjdk-8.412` `openjdk-8`                                    | July 4th     | `sha256:ef4fcebcc1483d4df690aa938dddf2e4e0a9c0b4b8f4fe4d43d8213739c57200` |
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | July 4th     | `sha256:93197999b2bd7ac6e7adbfb8f3f42f517ff89e314aef03ee48c93565c3d2f3c1` |

