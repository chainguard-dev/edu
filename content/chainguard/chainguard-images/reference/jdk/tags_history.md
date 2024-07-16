---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest`     | July 8th     | `sha256:6fa19fd4bd3a94c5b1530a9a40f1f4bf3a9442bd64655f3f7995468d71352edf` |
|  `latest-dev` | July 8th     | `sha256:37d1774d14a607b426c21548aad6db0777360ec0e8f7cf23d42f0647d555b4d7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15` `openjdk-15.0.10`                 | July 8th     | `sha256:dc6e00506a45ee484182d04d729521824da04aaedf3f6e2c8a253799fb9bf4c4` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | July 8th     | `sha256:01d3fec7358344b0e7d13e8cf6ab83fae09b299a5a7b4d501a536d2c6c2a7939` |
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | July 8th     | `sha256:1c86cb051e6383b6e1addfbb66dbc0f1f5b73e9c54ed4b7efd0ad33582856d80` |
|  `openjdk-17.0` `openjdk-17` `openjdk-17.0.11`                                     | July 8th     | `sha256:89d27d2b730563d7ffbaf60267c92357416bbfdb2ca32bdf69fb605fac95bfce` |
|  `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | July 8th     | `sha256:5c3e57ef1e5c871ded76ef8513104de05a131c0155634fd750db5bd14c52c925` |
|  `openjdk-8.412` `openjdk-8` `openjdk-8.412.08`                                    | July 8th     | `sha256:d19618c32b81847913e0816d76568170ca837e2964a9f85df2d75367bbc57758` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.11-dev`                         | July 8th     | `sha256:c9c43f4b1c8f856a34b98b0e677dc49fa8d288bff07f529d082ae8bb1439bbff` |
|  `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16-dev`   | July 8th     | `sha256:b205916f87d6ba21d6dfd904ce2950a062b3975cc6d107f8dcd511cc0d7b5357` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14` `openjdk-14.0.2`                  | July 8th     | `sha256:8e6e79c24a329b14b85bc74d6079d13d950c88441f1b55f4b8449af9c5165b57` |
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | July 8th     | `sha256:f6d923c4077ca79516d52e02ce9733296861934a03117657ffd640bb0fdb96dc` |
|  `openjdk-22.0.1-dev` `latest-dev` `openjdk-22.0-dev` `openjdk-22-dev`             | July 8th     | `sha256:f197e225e02a3b62b3ddc6dc7619b6f227818bf381531cdab83b04fd7cc48206` |
|  `openjdk-22.0` `openjdk-22.0.1` `latest` `openjdk-22`                             | July 8th     | `sha256:a40b8dfcd94fe1fb1729034e03d3c7fbc21706a600d9db9b9b7860bdc9e067b3` |
|  `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | July 8th     | `sha256:72d4b0404d117d6a419c0c5dc34ef122f68aa8976266e27c594a2d32a608c6ad` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | July 8th     | `sha256:e1d43ccfd8ef7332957c3393ff9e0870f69d3f1ec2ced7af03aa1ffc89caea6e` |
|  `openjdk-16.0.2` `openjdk-16.0` `openjdk-16` `openjdk-16.0.2.7`                   | July 8th     | `sha256:8333a28d4160e44a427b50d02c93638e100e36d08bd3366e01b1ea6ee24bbda8` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | July 8th     | `sha256:6e21fab074d10de49c2c4d18c2dfded0a404ee2b61e58ba9f973d179b38077dc` |

