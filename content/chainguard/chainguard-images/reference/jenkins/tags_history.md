---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 17th     | `sha256:caf4e39bad2a31b4be55dc08508c70999151999d01ac840b05116b9125faa13a` |
|  `latest-dev` | May 17th     | `sha256:a1b0ead142fa81673e43599783287fda025b5ca92b954608cd5ed29124cc01e3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.458-dev` `2-dev` | May 19th     | `sha256:eae5c972db624d2932f1797e9f664b2337ba34d4a477b7a4a88dd325fb07dab0` |
|  `2` `latest` `2.458`             | May 17th     | `sha256:9eb32bd9d27ab5ff73dabfbb0a3a7dafc8222a4cbbb5b493f5200bdeebeed181` |
|  `2.456-dev`                      | May 14th     | `sha256:78d93481a2abc64cb0d85b70664998503253d03ed0284d1b2b6b702d63daea7d` |
|  `2.456`                          | May 13th     | `sha256:f09ede8c004bb845b34d7aec9e1a3f83daa9e231a1208627bf3f8c6f0ef95b2e` |
|  `2.455-dev`                      | April 30th   | `sha256:c6c70361a2cc0bf7f3b801ca93281127280a1c7559105f7959bd825706ae763d` |
|  `2.455`                          | April 30th   | `sha256:003a795dbe4a264d127bd667bd2fdfe0397e336c1125b76d927ee701f7c5c4ab` |
|  `2.454-dev`                      | April 20th   | `sha256:f4bc0160f5c72dd1ee78c6c017fefa5b2f6c8fa211fdc4cd17d9b848923e09ee` |

