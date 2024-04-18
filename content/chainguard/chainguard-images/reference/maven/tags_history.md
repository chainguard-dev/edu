---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-18 00:43:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed | Digest                                                                    |
|--------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-21-dev` | April 17th   | `sha256:9e67ba1cf3ba2afcdb5e5d9b6336b16d37301062f94543c3697476318d2bd45f` |
|  `latest` `openjdk-21`         | April 17th   | `sha256:3c0e7ca99ef5f1f8473328c711884eacbdee87fc1adab6d14ee7d42c0ab448d9` |
|  `openjdk-11`                  | April 17th   | `sha256:f060dda1205baece2f31e0e2d61018b78aefcda950a51571726956b5612ae2af` |
|  `openjdk-17`                  | April 17th   | `sha256:068be81a074f98947a962efb5735f45dd175a0b6f03e67372857fbbe969ba8b9` |
|  `openjdk-11-dev`              | April 17th   | `sha256:4bd019a5633c5950de7093d6abdf8f153e49dcd441fbfecb483eff28a4f79df7` |
|  `openjdk-17-dev`              | April 17th   | `sha256:8c778bdab3c3899c14488befe2cfba973aa5b6a4af62e456b56073e371829436` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-3.9-dev` `latest-dev` `openjdk-21-dev` `openjdk-21-3-dev` `openjdk-21-3.9.6-dev` | April 17th   | `sha256:781047ae2a0158e431e81dd10429159ee4cd86e68e22b2c68687063019cba56c` |
|  `openjdk-21-3.9` `openjdk-21-3.9.6` `openjdk-21` `latest` `openjdk-21-3`                     | April 17th   | `sha256:60203acd90c90c4fd829173e565e92226e2dc9a9d7d15c61815b79d21f4eea21` |
|  `openjdk-11-3` `openjdk-11-3.9` `openjdk-11-3.9.6` `openjdk-11`                              | April 17th   | `sha256:cda14fb4f2ad3a82cd286016c26aa7fdb8cb0f308424a4b626244fa9fed194fa` |
|  `openjdk-11-3.9.6-dev` `openjdk-11-3-dev` `openjdk-11-dev` `openjdk-11-3.9-dev`              | April 17th   | `sha256:6613e7047b4726cc8a8d46c4990092151220560086c7f7f75f26d4cb4fb93380` |
|  `openjdk-17-3-dev` `openjdk-17-dev` `openjdk-17-3.9.6-dev` `openjdk-17-3.9-dev`              | April 17th   | `sha256:6ee5f853ddeb34fffde14077c1c6758beba51de68f6421956b6e876ede8dcdf4` |
|  `openjdk-17-3.9.6` `openjdk-17-3.9` `openjdk-17-3` `openjdk-17`                              | April 17th   | `sha256:8fcaced212aed37b90254c12dbe790c284103f76d1f0623995713ecf7ecde1e1` |

