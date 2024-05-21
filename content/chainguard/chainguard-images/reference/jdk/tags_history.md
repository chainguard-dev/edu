---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
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
|  `latest-dev` | May 20th     | `sha256:50514930dabd392ba7e4c65bbbc94c178fc6f4b395de8f9c22277ae74903be3f` |
|  `latest`     | May 17th     | `sha256:b0df34994fea235ca4d11ed14efface92ecb71fda7c7d88c2ac880f0a9026006` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14`                  | May 20th     | `sha256:9b3e8ce879aef0067d086c1e5b3f01dc26e784e56ca4ea85cc10eabd3aedf243` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14.0.2-dev` `openjdk-14-dev`  | May 20th     | `sha256:c9a086c0872c902799f47e11db8c1095bb06025770f5193897836d1840a6742b` |
|  `openjdk-15.0` `openjdk-15.0.10` `openjdk-15` `openjdk-15.0.10.5`                 | May 20th     | `sha256:c34539328cd587d53ec96b0928c06fb4dc4e05f6415424b9119d24185760aaee` |
|  `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` | May 20th     | `sha256:7adf487201bdbfb85a30c3eab660f3a3312fa3fa5c4e64b5d51ad765981f1bc5` |
|  `openjdk-16` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0`                   | May 20th     | `sha256:5824745a147606a11ba16f8ce6e2ff30d5172ddeed3801740ef2a6b85bda988d` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev`   | May 20th     | `sha256:d09efa2e1b40ff697d7a4d208cbc9f45b42056ad1958cfbf9c335cb7acbc101b` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `latest-dev`             | May 19th     | `sha256:56de3afbf5402456fbdf6afc9c73ba8e0bd360c02a394db8d778f20ad8456f33` |
|  `openjdk-11-dev` `openjdk-11.0-dev` `openjdk-11.0.23-dev`                         | May 19th     | `sha256:479410bb825b354120e672ffbfe62ab56bc5506245ede3f00032d48422676d12` |
|  `openjdk-17.0.11-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | May 19th     | `sha256:8540f1c61c6fca555eb72cce30f04ad803ff7c1036cd815d6e5e0a01386895fe` |
|  `openjdk-8.392-dev` `openjdk-8.392.08-dev` `openjdk-8-dev`                        | May 19th     | `sha256:29a13e1bfe7b4abcd093fc208424786538c9b96d2112aedb2b98de03d261390e` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | May 19th     | `sha256:ad320171388781952326a0fe2fa9ebb4996396bbc569c789e13da73c942dc517` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | May 17th     | `sha256:c22cd04fd457a815bec0765869088d79faadd0eff39865a8ac22a15719466e2e` |
|  `openjdk-22.0.1` `openjdk-22` `openjdk-22.0` `latest`                             | May 17th     | `sha256:8e51008decf3725c355c15f14116130cf310e42a339dafdfacb029027187c5e6` |
|  `openjdk-8` `openjdk-8.392` `openjdk-8.392.08`                                    | May 17th     | `sha256:833b05c477ecfcfc43f2626ce07cf33336b2f42d0844baa43e31d94592a26775` |
|  `openjdk-17` `openjdk-17.0.11` `openjdk-17.0`                                     | May 17th     | `sha256:e4d95f77e18f544c15bc17c34864816036decd6e96a51f09480e9ab7711486d2` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | May 17th     | `sha256:7265c290917d236e06b1ecd1a807fdd6cf778fd014b60dc8e4cb4a6a274eb14f` |
|  `openjdk-11.0.19.5-dev` `openjdk-11.0.19-dev`                                     | May 16th     | `sha256:892756bac53e2b57c43cd8b92d1790d223a18535e7186167dd65b41a51bdab7d` |
|  `openjdk-11.0.19.5` `openjdk-11.0.19`                                             | May 16th     | `sha256:4f282df7a3ebd9751b2372d077f7525f93f379e037cdf3b0d9cb3eb081fde668` |
|  `openjdk-17.0.7.5`                                                                | April 21st   | `sha256:42f156acccda6a812a7792a6201b040080865c08d8d88602c9ef7a03c1fb291d` |
|  `openjdk-17.0.7.5-dev`                                                            | April 21st   | `sha256:e2436f9e5d2e780ea5809773e14715030fe90c677badba52a4d134e649beb8c3` |

