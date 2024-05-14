---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
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
|  `latest-dev` | April 29th   | `sha256:238928355c3151b097caf2a4876fbb2658cec13734577afe028bea038edbeb69` |
|  `latest`     | April 29th   | `sha256:80129b934cf075a05019f138794990b45509d9589e17a4c92feb02c44e200429` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.456-dev` `2-dev` | May 13th     | `sha256:6219feb811a8dc5bfb88ae771a1bbce781761e25c0bfacd279576d9a707ea743` |
|  `latest` `2.456` `2`             | May 13th     | `sha256:f09ede8c004bb845b34d7aec9e1a3f83daa9e231a1208627bf3f8c6f0ef95b2e` |
|  `2.455-dev`                      | April 30th   | `sha256:c6c70361a2cc0bf7f3b801ca93281127280a1c7559105f7959bd825706ae763d` |
|  `2.455`                          | April 30th   | `sha256:003a795dbe4a264d127bd667bd2fdfe0397e336c1125b76d927ee701f7c5c4ab` |
|  `2.454-dev`                      | April 20th   | `sha256:f4bc0160f5c72dd1ee78c6c017fefa5b2f6c8fa211fdc4cd17d9b848923e09ee` |
|  `2.454`                          | April 19th   | `sha256:752e073a71752fe1b05aa614ae6ead697e9002f8c3147e18a72008f2c795c2f1` |
|  `2.400`                          | April 18th   | `sha256:bd8d42b081d23f5d2ebc04bea7272c42858b40b37c9c4a2dacd89a184373056a` |

