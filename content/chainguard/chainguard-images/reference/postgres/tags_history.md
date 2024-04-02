---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
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
|  `latest-dev` | April 1st    | `sha256:b7e826c662dade6531ff45c720b16ca167dd06b601925c0dad7fbb57d84d4561` |
|  `latest`     | March 28th   | `sha256:9e2c368e3f1ab137b0c5198d5960486722c8233311ca41dee175fdff72524e81` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `13-dev` `13.14-dev`             | April 1st    | `sha256:e1deec46fa25bd2830c579605af98ce77440de6925b5735f4b2d5187f2943ad0` |
|  `12-dev` `12.18-dev`             | April 1st    | `sha256:3c9ff394c885f3d1edd53fab995bbb2d68ba1a9324a3b2f7e4b04709039d6ce0` |
|  `latest-dev` `16.2-dev` `16-dev` | April 1st    | `sha256:946aa016ece8ccf78565a3311658f950bfc8ccd8f6030101b5099ebeb3ab623a` |
|  `14.11-dev` `14-dev`             | April 1st    | `sha256:924a1d747e8aee97d6d611974395b9630ec78b4a3ca0e20f976c0452b7e58fb3` |
|  `15.6-dev` `15-dev`              | April 1st    | `sha256:03f8b894b08cd70e5caef7978fa2710d4380d93d81dbc51612a7ed19616fbfb1` |
|  `12` `12.18`                     | March 28th   | `sha256:f15d87d58d695a584316d315491da541fc868f73e997f7ddc0274ab5af09f20f` |
|  `15.6` `15`                      | March 28th   | `sha256:44ec8b261744146dfe2e8d8a80726c3c6ea0d2225a5661d347083477da22bb4d` |
|  `latest` `16.2` `16`             | March 28th   | `sha256:ed46d3dc6fa2be48a2a03abc8577b9d83542dba582665fd389f28164e0a1a565` |
|  `14` `14.11`                     | March 28th   | `sha256:d3760f8232776872181ab68781835e103e2ac55d4fba838cfea877d25018b8ab` |
|  `13.14` `13`                     | March 28th   | `sha256:285adf862ed472b7d05a08ab978545fee89ad262b3163d194667cdad0816e499` |

