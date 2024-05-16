---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
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
|  `latest` `openjdk-21`         | May 9th      | `sha256:accaa4b8537aaddc96d9c935af29f2db51edb4472577cf804a6ba80568c2a056` |
|  `latest-dev` `openjdk-21-dev` | May 9th      | `sha256:033dd64782db129fb615f65fc6e944b931cfd702437a6d66442f4b3ebe2953fd` |
|  `openjdk-11-dev`              | May 9th      | `sha256:7726d29a7cbe7960a34d592ab55d7239103d9c8e4e34dd66064d85c41d19dc11` |
|  `openjdk-11`                  | May 9th      | `sha256:3ae1eef84ccef21304b9e95dfbe42df6f7daaa9f23e1c43d895635c81edc8319` |
|  `openjdk-17-dev`              | May 2nd      | `sha256:2e2f8a84a602d3af53b16aa57b5c2208b29620fd896cdd8164ef740d9ee2677d` |
|  `openjdk-17`                  | May 2nd      | `sha256:0a23b694a720fdd1a9dac54e8e729c20ffb8103f2be8873a700b82001a17f67c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-3` `openjdk-11` `openjdk-11-3.9` `openjdk-11-3.9.6`                              | May 9th      | `sha256:06cf0e7cb08d6f3add28a487f9b8946c081b7af98a2e7eee8f317485664c60dd` |
|  `openjdk-11-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev`              | May 9th      | `sha256:0ba4a6a2ecdc95baa8c4dea9001ac2cd92d85db4efaf0ff56e1042669aaa0acb` |
|  `openjdk-21-3.9-dev` `openjdk-21-3.9.6-dev` `openjdk-21-dev` `latest-dev` `openjdk-21-3-dev` | May 9th      | `sha256:be7506d3e103c6d38444b317e03b9e5dca808c389ea7ff0c507a0c89994ba4a7` |
|  `latest` `openjdk-21` `openjdk-21-3.9.6` `openjdk-21-3` `openjdk-21-3.9`                     | May 9th      | `sha256:a2aa38058849a62a53d75f7b4369c372d6fdb6a020c459b3f4c3c62950de07cd` |
|  `openjdk-17-dev` `openjdk-17-3.9-dev` `openjdk-17-3.9.6-dev` `openjdk-17-3-dev`              | May 2nd      | `sha256:e6726621b063b3d5ad6e8c543b137442d8cb803c0e8149b2ef02948f8f71360a` |
|  `openjdk-17` `openjdk-17-3.9` `openjdk-17-3.9.6` `openjdk-17-3`                              | May 2nd      | `sha256:6ce1c8d97c2090f3a63d428b17545d298f3f290c2d07485339e61e1e5d7ad76b` |

