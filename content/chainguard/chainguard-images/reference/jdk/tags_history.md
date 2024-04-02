---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 1st    | `sha256:d08adf4a79a181b8b7940de9e66e41f8b8650474715587052c9ca601e353033e` |
|  `latest`     | March 28th   | `sha256:ef8da9daa0d134cf659ec642b4409d344bf483592847abdc8d1edcdaf65bd28e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-22.0-dev` `openjdk-22.0.0-dev` `openjdk-22-dev`             | April 1st    | `sha256:2623ef49287fcc27c7ce68d4193af4ba989353190134aff97143247e2059cd22` |
|  `openjdk-8.392.08-dev` `openjdk-8-dev` `openjdk-8.392-dev`                        | April 1st    | `sha256:a956e42282ffc8eb564c603a507e5c0b94d90911e0e3230da46ebfe129d98ef5` |
|  `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` | April 1st    | `sha256:6899c6273c448cad159510a838bd772e2a4d014a9d28882bae8f7680d72e4f7d` |
|  `openjdk-11.0.22-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | April 1st    | `sha256:cedf2e8099e91d83c59160b016a7ed0dcf2b29538b84034af570d642fddb0131` |
|  `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0.2-dev`   | April 1st    | `sha256:4ff90370d2076dc64f1ae7f68e9f60e3f1e83958be6c0d971dc62cf2647cc933` |
|  `openjdk-21.0.2-dev` `openjdk-21.0-dev` `openjdk-21-dev`                          | April 1st    | `sha256:fd3ee3f5a3f247f81dc1950c3516c290f507140a43a9013f3cbdea624641bb03` |
|  `openjdk-17.0-dev` `openjdk-17.0.10-dev` `openjdk-17-dev`                         | April 1st    | `sha256:20bcda8b5a045c2645e073c25d35ce0c9dcd6ffd42a4487bdfdce990dcee59e6` |
|  `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev`  | April 1st    | `sha256:900db13150c25de6cc6a699262da8237aedc541eb4d8c40fe2a0493104ee5b5b` |
|  `openjdk-22` `latest` `openjdk-22.0.0` `openjdk-22.0`                             | March 28th   | `sha256:5d5a5e7b08afaf5b5fafcc50418354cb268de59fcd8b813b686ea84f8d4244cf` |
|  `openjdk-21.0` `openjdk-21.0.2` `openjdk-21`                                      | March 28th   | `sha256:340596e50e609e40fd72ac3b3d47b13e58d44a242db8163911cab6cf7a2e5570` |
|  `openjdk-11.0` `openjdk-11.0.22` `openjdk-11`                                     | March 28th   | `sha256:5d1bca9f4144fed4e17af29e9ff634a65326bb29a3b4f87d3fd952ba80f577a4` |
|  `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15.0`                 | March 28th   | `sha256:f436fbe65269f535938f8677b8d44779429d8a8543a657b8c7f2f25de75be20a` |
|  `openjdk-16.0` `openjdk-16.0.2` `openjdk-16.0.2.7` `openjdk-16`                   | March 28th   | `sha256:74f93f948efbbf5c983da5f404862a4505418ec6403c2cc07668e8d4a3e35883` |
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | March 28th   | `sha256:49799586a61a71b2858626ec9439eb3491399f0ad18ad26bd5169f6dcd74b538` |
|  `openjdk-17.0.10` `openjdk-17` `openjdk-17.0`                                     | March 28th   | `sha256:683cf4788787618a3876b40cfe5f1d444536548032b4bca62171b0767380da3e` |
|  `openjdk-14.0` `openjdk-14.0.2` `openjdk-14` `openjdk-14.0.2.12`                  | March 28th   | `sha256:7e5a903de62fa9e54086e15b03af0b0103ce538666e2fa57466271f5a066ed7b` |

