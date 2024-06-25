---
title: "node Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` | June 24th    | `sha256:793d8ea8ef720ba68a2a788ac659647951d84d20f73ba677243c83ebb07ec83a` |
|  `next`                  | June 24th    | `sha256:b350c40f55a530f848ce3aeb6530ca2878ad8ac619f45086822f7ee5cbdb5a00` |
|  `latest`                | June 24th    | `sha256:8d29b37811434040ce79280247287b028a449cf533c6fe2ce8261ea3d799fafd` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                   | Last Changed | Digest                                                                    |
|-----------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `22.3.0` `22.3` `22`                            | June 24th    | `sha256:39dac74ba807634f1ce79c1497cda4778ef1395cac873767fa41071612cac995` |
|  `22-dev` `22.3.0-dev` `22.3-dev` `next-dev` `latest-dev` | June 24th    | `sha256:47e95b87fede8fed26bbf47d688f1354c0c47f8283c5f0ce9565dbfe48df4921` |
|  `next`                                                   | June 24th    | `sha256:00b2f09746bba1e652b840b980a832b2697e198ffc90ff143a5d974e14c9b356` |
|  `18` `18.20.3` `18.20`                                   | June 24th    | `sha256:14d19facf616ec2eebbc3455f70a50639b9bd180f46aa8109f2008bd8443e2f1` |
|  `18-dev` `18.20.3-dev` `18.20-dev`                       | June 24th    | `sha256:b2e19db334fdfdffd2f6604dd973ec237d2c616bfce1eb947ba002c0ccaab7b8` |
|  `20` `20.15` `20.15.0`                                   | June 24th    | `sha256:55dbfb76786d0ae18e8a6108a074f1baae51f207ec7c54994415fa8361111c37` |
|  `20.15.0-dev` `20-dev` `20.15-dev`                       | June 24th    | `sha256:908ef74b5b3d59e6d64ebb74b94bdd9fe32a0228062571f5c91157092bd33c13` |
|  `20.14` `20.14.0`                                        | June 20th    | `sha256:a9658d9e31051b595495bf663cdfc682cfe9a5f5b1c33fa41d120e1b62c42124` |
|  `20.14.0-dev` `20.14-dev`                                | June 20th    | `sha256:56b6508531e4857962c8b7b8f71b2c14ea4c9e21b508e9e4e80a03bba650733d` |

