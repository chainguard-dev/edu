---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc`          | May 23rd     | `sha256:19dfea2c21fd55e08bda886e77b1f00075064f45a751b72f624daba48d85ccb9` |
|  `latest-glibc-root`     | May 23rd     | `sha256:a8369fc160c85ce337e239d4e102e5322dcc71f9218deaf98e9c3ff160b411dc` |
|  `latest-glibc-root-dev` | May 23rd     | `sha256:c108a1595e36a967682ced21167eac0ef12a91d5ac5d6f36d4a3eabe9cf3155b` |
|  `latest-glibc-dev`      | May 23rd     | `sha256:dd4bb108b8a8f2f957aadbe0224be1306bf0a8acf9455812d610c0fb85b9704d` |
|  `latest-dev`            | May 22nd     | `sha256:aab18a96fa32d77892406d8dca2d94c3ad882693eb2b670a45ecc893e1daf02d` |
|  `latest`                | May 22nd     | `sha256:f06036ea97419c784339638cf4a21b52d39df8dfd8aa0e0e73307fc1082c6043` |
|  `latest-root-dev`       | May 22nd     | `sha256:51c7c0164a6b4db491284ad755a0530df11c98d3081a5a05478656c34c9f991f` |
|  `latest-root`           | May 22nd     | `sha256:fa7a03c2cbfa3b961931f0fc0a3489e19fb06ae085f4c2dfd980347ed012c796` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2-dev` `root-2-dev` `glibc-root-2.45.1-dev` `root-2.45-dev` `latest-glibc-root-dev` `latest-root-dev` `glibc-root-2.45-dev` `root-2.45.1-dev` | May 29th     | `sha256:11aac32bc3a64b6ccced4efe38847acf526c670dd35b21dd8746b9e0fa2462eb` |
|  `2` `glibc-2.45` `latest-glibc` `2.45` `glibc-2` `glibc-2.45.1` `2.45.1` `latest`                                                                         | May 29th     | `sha256:59115fbb9e5627a15bf46cced1705832d904009f114d0b5ff7b88b13bc346d87` |
|  `latest-glibc-dev` `latest-dev` `glibc-2.45.1-dev` `glibc-2.45-dev` `2.45-dev` `glibc-2-dev` `2-dev` `2.45.1-dev`                                         | May 29th     | `sha256:edbac0650450b4f3f8b81462bfbd44305435f1e723c863fc3f504b6dfec0f80f` |
|  `root-2` `root-2.45.1` `root-2.45` `glibc-root-2.45.1` `glibc-root-2.45` `latest-root` `latest-glibc-root` `glibc-root-2`                                 | May 29th     | `sha256:b68c97c2677b690cb359aa13cd71fe29b10ec11007bf070259fe8d180ef3d2cc` |
|  `2.45.0-dev` `glibc-2.45.0-dev`                                                                                                                           | May 14th     | `sha256:042068e25cbad28a8e3b127e8db212d9c4fa1aa5cc84751c262b3c83006cd1b2` |
|  `glibc-root-2.45.0` `root-2.45.0`                                                                                                                         | May 14th     | `sha256:f2ff396551bfe42e62401b04a65df65bf43f04d3aff283d0c42454d97d70d7d8` |
|  `2.45.0` `glibc-2.45.0`                                                                                                                                   | May 14th     | `sha256:827fbc62d3e475394599edbf9095a353b4ec964a64797b62b143ef100a464027` |
|  `glibc-root-2.45.0-dev` `root-2.45.0-dev`                                                                                                                 | May 14th     | `sha256:48efe16835214c405ce9131641af0e51f342d50b5e98f05dff415afb65ceb469` |

