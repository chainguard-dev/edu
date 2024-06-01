---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubectl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubectl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubectl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubectl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:02de9f708823e5be6eb6511a0ab9171bbcf7049b9251af3aec65e6afe1db23b7` |
|  `latest`     | May 23rd     | `sha256:5cc071db52aa5815363f9dfa2cbc890e8defdeabd5370ca5be3f5a394d563e4e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.30.1-dev` `1-dev` `latest-dev` `1.30-dev` | May 30th     | `sha256:bd1260817ec66a5e6e26a14d718747766023ef1b749e08680f0f794972cf5781` |
|  `1.29-dev` `1.29.5-dev`                      | May 30th     | `sha256:613659e94ab8e625908c7cbf0b144930b3c676071489f4c2379d4cc2de2b5866` |
|  `1.27-dev` `1.27.14-dev`                     | May 30th     | `sha256:cebc76f35b0b21f7677ae2f1980c26586006cc24be1151214aece4904693ae92` |
|  `1.28.10-dev` `1.28-dev`                     | May 30th     | `sha256:829a88ab30478489b0a9f2bd98cbc716719cf9c3bac1d6fbc1ed255d73ec365a` |
|  `1.28` `1.28.10`                             | May 23rd     | `sha256:7ca636789cd47f113e1428e179b69ef797e4f3da8b505415375fee0fce9ca686` |
|  `1` `1.30` `latest` `1.30.1`                 | May 23rd     | `sha256:51e0713bde4ef6a3a9a96c6fc3ad4c7147156d87e36e8770be3a18e234c63898` |
|  `1.29` `1.29.5`                              | May 23rd     | `sha256:29e8ce93a7344bfa96d0bc770da8b497c8ff13734085e8b244440c0ad487b15a` |
|  `1.27` `1.27.14`                             | May 23rd     | `sha256:f64ac8847ad65a73553270c5c0e4f55925dbdb0bc552adbb47323e1b6c035a7f` |
|  `1.29.4`                                     | May 15th     | `sha256:ed3a78b7598f7bbc30b7f7409e3c908440c5cc9d85ac9aa286c33099cc3ef840` |
|  `1.30.0-dev`                                 | May 15th     | `sha256:1d3df70b95a12c53735c6fdd1d97c99a5dbfcee1862fcc4714f7f737f56ca650` |
|  `1.30.0`                                     | May 15th     | `sha256:b9cc3719a088d386d3ad87a831d7fc04dcf7416b8d04cee64926acc6707b0d13` |
|  `1.27.13`                                    | May 15th     | `sha256:8f75c099125fea0773715aded35592ff7fd8d8db59395ab3d3bb66d4f9aea275` |
|  `1.29.4-dev`                                 | May 15th     | `sha256:66ef3edc9137a991ea2a60aa8d5de8fe0ff1131dea2a0db8c7d7e61fff46c4f5` |
|  `1.27.13-dev`                                | May 15th     | `sha256:d37490676d071751b105967f6615d33f34aa27176e5b049e7112d59c2f1c3108` |
|  `1.28.9`                                     | May 15th     | `sha256:1731b37f5f760b29f540f0e013a97446baab1e12e832c7410ccfc1703517905c` |
|  `1.28.9-dev`                                 | May 15th     | `sha256:8e01bcda0bbefff414e5ea8888a9e8425704ddd00c5e14ec3cf4df1b6543147a` |
|  `1.26-dev` `1.26.15-dev`                     | May 13th     | `sha256:1e011aa667c8cc7a41eedaf1f38220b03a0f0d4277f3c0393c5ed47b24ad53a0` |
|  `1.25-dev` `1.25.16-dev`                     | May 13th     | `sha256:9ec0ad21540014026dacbef923fb5aeb9ed0b1636a505fad0522fe061df8a57c` |
|  `1.26` `1.26.15`                             | May 2nd      | `sha256:93a765a0c47c74985b04b152b7d573fd43252dc4e9f4f451ed62f5fffd5bd6b8` |
|  `1.25` `1.25.16`                             | May 2nd      | `sha256:51c66711b8efb6cb3ce2c2d9d8f5af35899e25636c3a98a82da98a102184b183` |
|  `1.27.1`                                     | May 18th     | `sha256:cb0c5c3863e0a4c8b3a45e1248fc2e8761d241beac8b7b49abdc3822005bdc23` |

