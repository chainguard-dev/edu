---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 3rd     | `sha256:75749da41c0d9bb46fe94500c1a9d002ae4aa574db06f696d67320e85c724de2` |
|  `latest-dev` | July 3rd     | `sha256:449d88a17244b559956b7cfb2b3559325bd452acc2056f05d4dfaf1f8ef651d5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-16.0.2.7-dev` `openjdk-16.0-dev` `openjdk-16-dev` `openjdk-16.0.2-dev`   | July 6th     | `sha256:894becd0ec9bc00217a263490469de4b844978d2a02d7c293b61e40ab99d295e` |
|  `openjdk-14.0-dev` `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14-dev`  | July 6th     | `sha256:521163a1aad0ae5c93d4aafa65a17c223218b53a6448c8b6c8d3926580042f4a` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | July 6th     | `sha256:efecc99bed3e37f1f8a070347d9dbd052929ccb3d4aa9b36a70eefa1fc163a99` |
|  `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` | July 6th     | `sha256:f654239affbd07ab4bb20a0dd26d871e5458137fbc6c2de38d4c200d328c1938` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | July 6th     | `sha256:b02a0cdfe5b476e6c1ad53491061a70b309060b9c9e476319915e943bd5e7f09` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | July 6th     | `sha256:3f9fd1f9a4e1df1db5470bd28c0efa76bae3c18db9abc90fe8c90fee2195b445` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | July 6th     | `sha256:419255dde369643939ccd79e9dfcb3d8c40f626f8d4fd3b7bf40ecd147a5a630` |
|  `openjdk-16.0.2.7` `openjdk-16.0` `openjdk-16.0.2` `openjdk-16`                   | July 6th     | `sha256:4a1685e9758fcdd53c9e89ff9b658d994b6ee8579b8577f651a6f4ed67f5f39f` |
|  `openjdk-8` `openjdk-8.412` `openjdk-8.412.08`                                    | July 6th     | `sha256:a77855b61d56362f00fdd45a92edca62d40e53d77845196ebbe7da777ff1161a` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | July 6th     | `sha256:37d42c846c0099e436a0b063217c5ea2927e5769f8481acbca5911fac7041fbb` |
|  `openjdk-22.0` `openjdk-22.0.1` `openjdk-22` `latest`                             | July 6th     | `sha256:08eb52dd035e41742c3441544c2f36aca14c778634eafa048adf331f00a69f1e` |
|  `openjdk-21` `openjdk-21.0` `openjdk-21.0.3`                                      | July 6th     | `sha256:640cf6dd7ee2ee3599bd528ac7197cf0410d9649442d08d7db9225d433eb9fd3` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14.0.2` `openjdk-14`                  | July 6th     | `sha256:c8226bff4e97b6120c402c5215989444484aa2fdcafb808ac613aa2bb392d66d` |
|  `openjdk-22.0-dev` `openjdk-22.0.1-dev` `latest-dev` `openjdk-22-dev`             | July 6th     | `sha256:874b0ed9840a5cf89c3f2db18595cc3af6ca0a1569e548b0d50d1ffd58f24c0b` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | July 6th     | `sha256:854cf070390440b11dccb5a4a7649261bfeea3995744b57c52cc276628b637ac` |
|  `openjdk-8-dev` `openjdk-8.412-dev` `openjdk-8.412.08-dev`                        | July 6th     | `sha256:a868e3c06c9998fa17c6d322f82117b37ad1720f8bd2b5de2815af6e888429a0` |

