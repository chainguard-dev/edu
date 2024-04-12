---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
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
|  `latest-glibc-root-dev` | April 11th   | `sha256:b325dd9cde58ccc8bf344f6d4b04a221cd27698b876672d49f5a1a58747939e8` |
|  `latest-glibc-root`     | April 11th   | `sha256:dcad719f38fc1cc4e9e21ee4bb6b399b574b5ce95e883005c3f6c98f51aeab01` |
|  `latest-glibc-dev`      | April 11th   | `sha256:19b03b7cdb8093c80b64e774d054b612b8cbbcac9a0564307b0a589dad58ba88` |
|  `latest-glibc`          | April 11th   | `sha256:364b944633cc48bca975e2d25fd2bd8cee545cfd6ec13e773ab499840ae4fa67` |
|  `latest`                | April 11th   | `sha256:a63f65075e5dfb6b040ace5d7a0982b79ed572f196de9d33b69f2a3c5b9665f9` |
|  `latest-root`           | April 11th   | `sha256:3a67c15f02fe47399e6faf5fbc8025e97eaf0aa832097d3f5bcc71599f07905c` |
|  `latest-root-dev`       | April 11th   | `sha256:1a643f0c1c3189fe9c9ed3f199bc657fac1c4ae2de7873446f2b05e7a4938825` |
|  `latest-dev`            | April 11th   | `sha256:32350f65728dc8bb5e31b9a7f352a36ac08416f896862310410a3c0ad0c2cc91` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-root-2` `latest-glibc-root` `glibc-root-2.44.0` `glibc-root-2.44`                 | April 11th   | `sha256:8b3b491242f353866d62cbd9270643a796457a7d086709fd3cf5151fbba084d9` |
|  `glibc-2.44` `latest-glibc` `glibc-2` `glibc-2.44.0`                                     | April 11th   | `sha256:b76ddbb76a14dbca79b3b6b3a6b20d861e3c836ee8fd728d8a0e7412e504fded` |
|  `glibc-2.44-dev` `glibc-2.44.0-dev` `glibc-2-dev` `latest-glibc-dev`                     | April 11th   | `sha256:d2113d2bc3a29fee78cba6cf628f882c5a405a89cc6630e560e4f9f8d33f04f8` |
|  `latest-glibc-root-dev` `glibc-root-2.44.0-dev` `glibc-root-2.44-dev` `glibc-root-2-dev` | April 11th   | `sha256:b049f1b815887cc1fbae79465fc88a449e76e8c5fe3b7339ed6bc58875b7a8a3` |

