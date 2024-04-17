---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-17 00:46:08
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
|  `latest-root-dev`       | April 16th   | `sha256:a3c156c8f02735b06755f9f224782e0e364d6a55fe2512153f5e5ba407d11bdf` |
|  `latest-dev`            | April 16th   | `sha256:d1a98efb26599aa190eda66df8c1ab9f171d63b3ef5cdf45a66f8f8b3ac782d4` |
|  `latest`                | April 12th   | `sha256:f8fd9abd68239716cb7c83e69bb07f53613e595e9c6eb05c059de9759878880a` |
|  `latest-root`           | April 12th   | `sha256:91272f86336407508918d164d689a64d5a08e9bf496dd5826c29264ffa9b44ef` |
|  `latest-glibc-root-dev` | April 11th   | `sha256:b325dd9cde58ccc8bf344f6d4b04a221cd27698b876672d49f5a1a58747939e8` |
|  `latest-glibc-root`     | April 11th   | `sha256:dcad719f38fc1cc4e9e21ee4bb6b399b574b5ce95e883005c3f6c98f51aeab01` |
|  `latest-glibc-dev`      | April 11th   | `sha256:19b03b7cdb8093c80b64e774d054b612b8cbbcac9a0564307b0a589dad58ba88` |
|  `latest-glibc`          | April 11th   | `sha256:364b944633cc48bca975e2d25fd2bd8cee545cfd6ec13e773ab499840ae4fa67` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2` `latest-glibc-root` `glibc-root-2.44.0` `glibc-root-2.44`                 | April 11th   | `sha256:8b3b491242f353866d62cbd9270643a796457a7d086709fd3cf5151fbba084d9` |
|  `glibc-2.44` `latest-glibc` `glibc-2` `glibc-2.44.0`                                     | April 11th   | `sha256:b76ddbb76a14dbca79b3b6b3a6b20d861e3c836ee8fd728d8a0e7412e504fded` |
|  `glibc-2.44-dev` `glibc-2.44.0-dev` `glibc-2-dev` `latest-glibc-dev`                     | April 11th   | `sha256:d2113d2bc3a29fee78cba6cf628f882c5a405a89cc6630e560e4f9f8d33f04f8` |
|  `latest-glibc-root-dev` `glibc-root-2.44.0-dev` `glibc-root-2.44-dev` `glibc-root-2-dev` | April 11th   | `sha256:b049f1b815887cc1fbae79465fc88a449e76e8c5fe3b7339ed6bc58875b7a8a3` |

