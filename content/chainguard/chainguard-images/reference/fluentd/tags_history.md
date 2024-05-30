---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-splunk`     | May 24th     | `sha256:794be8f9196a1964ebdec0c5084525764d2628fb14d939bbc8760f2da289cc71` |
|  `latest-dev`        | May 23rd     | `sha256:e4613899ffd122f558e9335c0989a1d5406b9d481aaa84644573653e24c9e752` |
|  `latest-splunk-dev` | May 23rd     | `sha256:c34640f12dfe1fe4c1cd9a6ca294abf6520fc2f0b067f1a3c8642fcf1eee6a91` |
|  `latest`            | May 23rd     | `sha256:4d491071d7f99abe37cb1bdc3abcfab9b12339be0a19b316b3132bb100d6d513` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1` `1.16.5` `1.16` `latest`                                                | May 29th     | `sha256:261760059d90591d356e42b56edbb91dceaa90ce2fce293ff217731e737a7757` |
|  `1.16.5-r1-splunk-dev` `1.16-splunk-dev` `1.16.5-splunk-dev` `1-splunk-dev` | May 29th     | `sha256:76604958498de15fe3304db7e00ae930df2f06f6e8ea1f60f736554ccaeac2ef` |
|  `1.16.5-splunk` `1.16-splunk` `1-splunk` `1.16.5-r1-splunk`                 | May 29th     | `sha256:85c414062674e033ee5a74fe240fb666c2ac2ef4d11882a7e682a2ca9bd03691` |
|  `1.16.5-dev` `latest-dev` `1.16-dev` `1-dev`                                | May 29th     | `sha256:147b870cd672f7963b65d4c0c72c13339ce7bf92a1eb537490161d91e26d21db` |
|  `1.16.5-r0-splunk`                                                          | May 23rd     | `sha256:741677b3870ced9463d436491c9168ba3861acc2f66fb6e4d469418bde6e670a` |
|  `1.16.5-r0-splunk-dev`                                                      | May 23rd     | `sha256:124507aed6595fc380269d13f107009ad72fe0fc20ad31dad9b531a7da1f157f` |

