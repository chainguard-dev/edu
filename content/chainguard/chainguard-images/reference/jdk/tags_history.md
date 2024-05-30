---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
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
|  `latest-dev` | May 24th     | `sha256:d283e8ca2fc03b562456d2018ec314ec81a0b18d8af44c72dcd9e6b3ab6e3362` |
|  `latest`     | May 24th     | `sha256:885937f5e3c0a97df355fe5a798de76df067ef1010bd409cf0e5e75c6e72efee` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `openjdk-22.0` `openjdk-22` `openjdk-22.0.1`                             | May 29th     | `sha256:94e13d40d7b7b74c4863fab7a05d3850f6233afe86a8599f3680de8c1c81cd37` |
|  `openjdk-22.0.1-dev` `latest-dev` `openjdk-22.0-dev` `openjdk-22-dev`             | May 29th     | `sha256:4be4d33b45e3acdf5cbade990e5b97fd9e7711da725b448b8454220de94a44b3` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16.0` `openjdk-16`                   | May 29th     | `sha256:b5209c7dc2aef3178599d591a4fe2610d2c05efb7f2869d17aac15b7dc65dcb9` |
|  `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0`                 | May 29th     | `sha256:693c7bff0f490e75ea37bdf11cdef71ffc02cc58e9605baa74231fb943ad3e9b` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | May 29th     | `sha256:6a11265536d4ff6eca4a4e7f7f40ccdda502ba38858b179f55b7b367a695df22` |
|  `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev`   | May 29th     | `sha256:d88c8ab51b906ef2e23a7874a87b6d1f013d36aab8c4df0857cb1f46b755b459` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | May 29th     | `sha256:1d1a7301a92ed66def67088d87da785795bbd9a94cfc3a23d5acbe2f49055229` |
|  `openjdk-8.412.08` `openjdk-8.412` `openjdk-8`                                    | May 29th     | `sha256:29dbe957e91c74cf6068c916bc8befee671306e5c6d7cdcc15de6155e0df5e78` |
|  `openjdk-15.0-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` | May 29th     | `sha256:4555b54d71e0bdef48b3864307d60c699e05aea6e6334fca8ce4bd7f76019d46` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | May 29th     | `sha256:2f71f5a29ea76db64872b871d06ad46428454948030baa67d33152c2c13de534` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2` `openjdk-14`                  | May 29th     | `sha256:5763be832e812ddf99812040108e65d97942fffb1350162eeb2309648e5565ad` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | May 29th     | `sha256:a2c306817273c9c9ce15070679b80571c66568f878dc8759eca6579f858bff34` |
|  `openjdk-8.412-dev` `openjdk-8.412.08-dev` `openjdk-8-dev`                        | May 29th     | `sha256:1940ef5edc598baaa117103f61bb81da2abffbf5590c63b11bd56d04df47e98b` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | May 29th     | `sha256:bb33171fd2ce0a67d2d47602ff175ac6c83baa97ccf36bfb761f9c9ee7c9f102` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14-dev` `openjdk-14.0.2-dev`  | May 29th     | `sha256:4c25619b76387aab2bb81a3445df0e98e0154ffb1e8027e66f89d8b38fe0b0f3` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 29th     | `sha256:bf7f201042e69b4ab1dd39a7199a31855cfab343fa3cc60e9fbe38ceed893ef7` |
|  `openjdk-8.392` `openjdk-8.392.08`                                                | May 24th     | `sha256:46923fe97a13048c8f32fe8c3eaef247df1e8d595468bffc7715a094766472cd` |
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev`                                        | May 24th     | `sha256:fbaad341ead88558bba7c9ffc5304d5e8c3c008b1983186039d4cc26cd397adf` |
|  `openjdk-17.0.7.7-dev` `openjdk-17.0.7-dev`                                       | May 24th     | `sha256:4371eadda85a33174d3a7bb8084f7e70e862cb0c032b5b4d38bdd6c6fb168756` |
|  `openjdk-17.0.7.7` `openjdk-17.0.7`                                               | May 24th     | `sha256:d69ada7f17ef4b025c353fae0d02620ebebbf2fa20a615fbc1e2c04bc39a59d5` |
|  `openjdk-11.0.19.5-dev` `openjdk-11.0.19-dev`                                     | May 16th     | `sha256:892756bac53e2b57c43cd8b92d1790d223a18535e7186167dd65b41a51bdab7d` |
|  `openjdk-11.0.19.5` `openjdk-11.0.19`                                             | May 16th     | `sha256:4f282df7a3ebd9751b2372d077f7525f93f379e037cdf3b0d9cb3eb081fde668` |

