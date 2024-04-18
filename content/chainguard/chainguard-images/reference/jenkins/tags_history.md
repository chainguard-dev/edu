---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-18 00:43:55
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
|  `latest-dev` | April 17th   | `sha256:a7e862b714e9b898360ad3d459847ad25f8a620c5fb8f572ae61eb50c2df2dfc` |
|  `latest`     | April 17th   | `sha256:ef0b0b2bde59d6a21dfe5f891459d5b8eb153fd08df3820f725b9a067b8096bb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2` `latest` `2.454`             | April 17th   | `sha256:6dc1b9591fc19ae99c2dd34441566fb5c5b9a04acc3e7f33d12d3d481987fc3f` |
|  `latest-dev` `2.454-dev` `2-dev` | April 17th   | `sha256:4f4508fc77ebf2e569ae49405f6cde3aabc3c9c888080d62b1981510ee4546cb` |
|  `2.453-dev`                      | April 11th   | `sha256:5622376414d7b82bcc18ea801b64e760df1879bf7724ab912b0ec6f5e41ba896` |
|  `2.453`                          | April 11th   | `sha256:5b8dba7e104c6ffdc0e8d0268113d2caeb7373a0d1535e019fcf7ad2855b4cf1` |
|  `2.452-dev`                      | April 5th    | `sha256:0c8638ab11c39310885bc3e975b1aabdb22202ecee4cae9dd548276abdc63dcc` |
|  `2.452`                          | April 2nd    | `sha256:f052ff590f6aaa0c5975a4ca222b405b4edb4f423fbf286a78990254b8f0708c` |
|  `2.451-dev`                      | April 1st    | `sha256:39ccd8c0d6f83a841cc6889c124ca7f73d971cca8235e7314ebe1d0d44228d23` |
|  `2.451`                          | March 28th   | `sha256:6c0ebc567036320aa3956c042e38487f42f5678989a2e33570e8342a2c7dc2d4` |
|  `2.450-dev`                      | March 20th   | `sha256:ffa9168061690d1a11cd602234d62ca4de2ccfc5f7223d69e80af19a70886d0f` |
|  `2.450`                          | March 20th   | `sha256:90c4ac02f6893758fedbee5072779f8f48a5d19e09ea585608940a4506025b77` |
|  `2.449-dev`                      | March 18th   | `sha256:292423b9874e77b2dc9c5366790031fe61fd710c3e674706c9441915fe982db8` |
|  `2.449`                          | March 18th   | `sha256:21a92280f0a73be522e892d8e8e766f250b7787543cb03d256d35b80a4853478` |

