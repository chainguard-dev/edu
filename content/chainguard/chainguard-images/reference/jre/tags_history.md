---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
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
|  `latest`     | May 24th     | `sha256:c76802be2d6617236071f474ab6a20dcb560295c6000262473edd674f9dde9d6` |
|  `latest-dev` | May 24th     | `sha256:a9fc4404a3029beefd3c9bbd197f0848da57268ceb8111971093b49bf4493595` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16`                   | May 29th     | `sha256:f284d8c8d57ea527cde4e3ac4d594dd20d2aeac7273d21a7d834ce3f04a72afe` |
|  `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev`  | May 29th     | `sha256:c77c104e6efa190a1c4d95967c2f551648d2d6d5fe710b3d79d93fb03c25fc7b` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2` `openjdk-14`                  | May 29th     | `sha256:5cfd559e2017b430e3477b12c08ab9a269f81714d80798959d6fdabccce0976f` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | May 29th     | `sha256:ff8ee35682ac73dd3ec23e936873126b1b739cda1538dda4103654edeb24b71a` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | May 29th     | `sha256:df91422a62f0aa79379b157918fa503ddaa37b7db3392295f67cab1e287497f2` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 29th     | `sha256:0dfe19dbfcbcc5f3e0337d5ae06f8a0aa29595687a75a37bec649961dd7b9b74` |
|  `openjdk-8` `openjdk-8.412.08` `openjdk-8.412`                                    | May 29th     | `sha256:e5c6275ea89b1cda91c3d4a4465d483e5a5fc9db662bf11044b34704fb8ac5b9` |
|  `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0-dev`   | May 29th     | `sha256:47f0535c0b7406dfe32e2e72500d217ef98073d5c328536a28aa819bab6a9c44` |
|  `latest` `openjdk-22.0` `openjdk-22` `openjdk-22.0.1`                             | May 29th     | `sha256:c246f1f796725566501ec34cf6082528d117268cd9ffe463e66f2afac3240411` |
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | May 29th     | `sha256:f945886729a450e986bca1f36639a9f46d0ff8199125a3c5e5b9501c56f7b5c8` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | May 29th     | `sha256:6d6490894dfd4ac5b3543ef9eb2c201435074d2591a293d30d79c5cfd26ae343` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | May 29th     | `sha256:5840e3891a03b113f1354ab18dbe519d79fcbf0a1a698ec4c38d8dc45279ae5e` |
|  `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | May 29th     | `sha256:b6c06dd541f375395e5c8e7afd13985441b21abf009eeea84a1620a85ea550d6` |
|  `latest-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev`             | May 29th     | `sha256:c4c8532eae2d043028f09ac3459b08cc21c3a0d920fc248a97d771dcfae96c76` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | May 29th     | `sha256:6c7aed81f07b840e44dab9db77793fbf62703eb4a9413e85ebcb7f937091f358` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | May 29th     | `sha256:111699e88221102785f1b6051d3e962368a1c16644e3d09e421faf5cd721030a` |
|  `openjdk-8.392` `openjdk-8.392.08`                                                | May 24th     | `sha256:bee10fb31837f16c5619ab12bd23f4306aca19ccc0b9bcbe56414e409bf4df2c` |
|  `openjdk-8.392-dev` `openjdk-8.392.08-dev`                                        | May 24th     | `sha256:6b4e5dbd3bd694eb6e7e092b52b90a93912a07a68f83949a1f9dbf7f86345aed` |
|  `openjdk17.0.7.7-dev` `openjdk17.0.7-dev`                                         | May 24th     | `sha256:7ae7e3f4fd4d3ed8dc5079df0f2a3d8f5eb7a0bbb299c43b26087d0a0e606491` |
|  `openjdk17.0.7.7` `openjdk17.0.7`                                                 | May 24th     | `sha256:987c691df173a241a4398d60014a6f061e007e4323f19d9c487b95c7623dfeaa` |
|  `openjdk11.0.19.5` `openjdk11.0.19`                                               | May 16th     | `sha256:677dee78db811af812e1bb2bd33c1f247a5a4e0418169c194d965fc618768bba` |
|  `openjdk11.0.19.5-dev` `openjdk11.0.19-dev`                                       | May 16th     | `sha256:30327ab04c691b2d4f2bfa4391531384ea89b4e204cc65b90eee78a5cbc83156` |

