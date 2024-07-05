---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/postgres/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/postgres/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/postgres/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 3rd     | `sha256:7615b4f5b64e905cc17c2cca18c21651b2b4214e476ad8dfebf60c97aae2cee7` |
|  `latest-dev` | July 3rd     | `sha256:e78b66ffbb440e1d7f558c985a5672c899b5f638c0b702b023a2f1bbbd78fb6d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `15` `15.7`                      | July 4th     | `sha256:7b31c7d9ea59a1764d2d1ff36d2d03fe0f09507019fcc79399e262b2a8acccd0` |
|  `15.7-dev` `15-dev`              | July 4th     | `sha256:ef0f71aadb2467f360ccffe3925fa2b7d14086e48579dcd9650a42be3d0dde8b` |
|  `12.19` `12`                     | July 4th     | `sha256:31cd1896bb9da48b89ddad2606b672e8fe2a6b6532cf77401736a2d53e09f7bc` |
|  `13.15` `13`                     | July 4th     | `sha256:9bd69eae213e83d868e7d5f30d495e49dc577670f1920bf483990ca6579fce33` |
|  `14` `14.12`                     | July 4th     | `sha256:9d95616b480dae9e92a30dfce33c668f840e4d6ae60fe4bfdbf123161506a3f5` |
|  `16.3` `latest` `16`             | July 4th     | `sha256:8ce027208cdfa1c8f72ef9f3de04c5c48c868141e50794b9b60c03ad67ec7bfc` |
|  `13-dev` `13.15-dev`             | July 4th     | `sha256:696bc7cb86ce260723960f8952f66c3d49eed58cf928b5f22fd1cba0cb664d53` |
|  `12.19-dev` `12-dev`             | July 4th     | `sha256:0e60cfd75c1bde884a60fa18fe05658b4e174d19dc4408f3d3de795912489e70` |
|  `16.3-dev` `latest-dev` `16-dev` | July 4th     | `sha256:b7945c7bc903a8f8306b665ab8ee28a8721c19610e2b5715e2f1baef9753aabb` |
|  `14.12-dev` `14-dev`             | July 4th     | `sha256:e9a38963c64c8b3f6eef40a9cc1928e7cd30d354364b6961459c827c1d6c00d4` |

