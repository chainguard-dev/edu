---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
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
|  `openjdk-11-3-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev` `openjdk-11-dev`              | May 10th     | `sha256:12bc3057452d4bee3b664e036e835c50d1bf81722d0f4b75029575b3b46cffb6` |
|  `openjdk-11-3` `openjdk-11-3.9` `openjdk-11-3.9.6` `openjdk-11`                              | May 10th     | `sha256:3f61fe8ee7aaa5f7620f2049c333dd3c87b7868550d32f5c7f6780936f0968d3` |
|  `openjdk-17-3.9.6-dev` `openjdk-17-dev` `openjdk-17-3.9-dev` `openjdk-17-3-dev`              | May 10th     | `sha256:ee034e6cc20425891be40bddf8a3a0bdfc92be1b251896cb9cecb05486bb986d` |
|  `openjdk-21-3.9` `latest` `openjdk-21-3.9.6` `openjdk-21` `openjdk-21-3`                     | May 10th     | `sha256:287115e38e55abbb57bc4d6daf4a6225155c5ae15c98ee888fe2400e69dc6470` |
|  `openjdk-21-dev` `latest-dev` `openjdk-21-3-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3.9-dev` | May 10th     | `sha256:35894168faa15ca3c8871a9e0640c49791e02fb7fa1e73c5dea6c05eb73594d3` |
|  `openjdk-17-3` `openjdk-17-3.9` `openjdk-17` `openjdk-17-3.9.6`                              | May 10th     | `sha256:9f66cef298ea94c09fc78c4c62e6fc7fc529afcbf9ac095cd22ab37e53743c72` |

