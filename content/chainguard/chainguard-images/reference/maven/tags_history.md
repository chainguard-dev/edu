---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
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
|  `openjdk-21` `latest`         | April 11th   | `sha256:698b02b794492eb8f5d017836c9672a99c4a06d4a18c9a5115c5272f8356c901` |
|  `latest-dev` `openjdk-21-dev` | April 11th   | `sha256:f9bf3ccfa4634a75a3522f75f6249416851ad03d10b318ed13ead0ad69a8ec50` |
|  `openjdk-17`                  | April 11th   | `sha256:7f83961b92323f677aef902de4fcbffe4bdf987df610e0abe90f2add2b0e5bf1` |
|  `openjdk-11-dev`              | April 11th   | `sha256:ce7bccc09340083aa9130d869a23a818134cf4220fe4e3181e507c369a894fe2` |
|  `openjdk-17-dev`              | April 11th   | `sha256:7744138aac163174462f2310b66aa6d7b0ed0cd32a26cb13d17200bfcc4f340d` |
|  `openjdk-11`                  | April 11th   | `sha256:2b236d5a2f144439b3ae90f7e5d88a9e98c83556b76d87f4afb031ab3a146023` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-3.9.6` `openjdk-17-3.9` `openjdk-17` `openjdk-17-3`                              | April 11th   | `sha256:62d975d6ebf903771607aba3d7d472728dc4410ec601c9b9be3405fe5ad70f57` |
|  `openjdk-11-3.9` `openjdk-11-3` `openjdk-11-3.9.6` `openjdk-11`                              | April 11th   | `sha256:e07b3338ec5a4be6c1f876636376fbc377f7b5f7d50ca079436697937383fe9c` |
|  `openjdk-21` `openjdk-21-3` `latest` `openjdk-21-3.9` `openjdk-21-3.9.6`                     | April 11th   | `sha256:218baa0adcbda6d26038e1d129539efd31847556256baafb4379c213266a29b8` |
|  `openjdk-17-3.9.6-dev` `openjdk-17-3.9-dev` `openjdk-17-dev` `openjdk-17-3-dev`              | April 11th   | `sha256:71722bf29431f4f9426eee896bd2c77fca73473b86a021b73c6a019ead70eed9` |
|  `openjdk-21-3.9.6-dev` `openjdk-21-dev` `openjdk-21-3.9-dev` `latest-dev` `openjdk-21-3-dev` | April 11th   | `sha256:4ec54b379262b6a13263c865dc320f8f6859a8392ee017ed5733ec949207e938` |
|  `openjdk-11-3.9.6-dev` `openjdk-11-3-dev` `openjdk-11-dev` `openjdk-11-3.9-dev`              | April 11th   | `sha256:de18f775e2d5e02fd89d71e0c17584fda8072e28814fcc6e752d14b2a11006d9` |

