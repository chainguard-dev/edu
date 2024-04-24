---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-24 00:53:13
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
|  `latest`     | April 23rd   | `sha256:04025a387644a28387122848bb25b638183fa838637ee51f8c150859f2244cfa` |
|  `latest-dev` | April 23rd   | `sha256:548e07905f15824bd4c2573b4456eb1de12d2877b1b6e6168caaa30c84c575c3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.454-dev` `2-dev` | April 20th   | `sha256:f4bc0160f5c72dd1ee78c6c017fefa5b2f6c8fa211fdc4cd17d9b848923e09ee` |
|  `2` `latest` `2.454`             | April 19th   | `sha256:752e073a71752fe1b05aa614ae6ead697e9002f8c3147e18a72008f2c795c2f1` |
|  `2.453-dev`                      | April 11th   | `sha256:5622376414d7b82bcc18ea801b64e760df1879bf7724ab912b0ec6f5e41ba896` |
|  `2.453`                          | April 11th   | `sha256:5b8dba7e104c6ffdc0e8d0268113d2caeb7373a0d1535e019fcf7ad2855b4cf1` |
|  `2.452-dev`                      | April 5th    | `sha256:0c8638ab11c39310885bc3e975b1aabdb22202ecee4cae9dd548276abdc63dcc` |
|  `2.452`                          | April 2nd    | `sha256:f052ff590f6aaa0c5975a4ca222b405b4edb4f423fbf286a78990254b8f0708c` |
|  `2.451-dev`                      | April 1st    | `sha256:39ccd8c0d6f83a841cc6889c124ca7f73d971cca8235e7314ebe1d0d44228d23` |
|  `2.451`                          | March 28th   | `sha256:6c0ebc567036320aa3956c042e38487f42f5678989a2e33570e8342a2c7dc2d4` |
|  `2.400`                          | April 18th   | `sha256:bd8d42b081d23f5d2ebc04bea7272c42858b40b37c9c4a2dacd89a184373056a` |

