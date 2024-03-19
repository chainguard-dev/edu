---
title: "k8s-sidecar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k8s-sidecar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k8s-sidecar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 18th   | `sha256:f31f994a45134c24baa0120f5023e17140649b3d7734a7b9d7de6d0135011f4a` |
|  `latest`     | March 18th   | `sha256:f08bd0be8faad5b6baf99e21b0d9f633e732b1c88e8414758df5af1fa1b2726f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.26` `1.26.1`                 | March 18th    | `sha256:a19b17599ed8dfc760bd77101ae7adfe3b113b89dc372545064c23034224738e` |
|  `1-dev` `latest-dev` `1.26-dev` `1.26.1-dev` | March 18th    | `sha256:444da134c5427e7af2cd22fe8d56fc5b6bdf66e321fa9682497ee4fe2fbf9fd7` |
|  `1.26.0-dev`                                 | March 2nd     | `sha256:fbfacc2f5ca90fbc0933e95b1354a7e397d83b81938181261f498a453c72672d` |
|  `1.26.0`                                     | March 1st     | `sha256:fa244bba955ff2419b401e83fb062f6d2d0e4db5f2955126a71dd866a6847852` |
|  `1.25.6` `1.25`                              | February 26th | `sha256:5122e92c38b77df2933f06cded201ccbeac376adf2e49e3aae8d9d78c289912c` |
|  `1.25-dev` `1.25.6-dev`                      | February 26th | `sha256:44af9bfeecd1695c69475a71a860e7c399f2b65170dd962a2e6d67f0b4f31ce5` |
|  `1.25.4-dev`                                 | February 24th | `sha256:fc502b83eb2a58e1b6c259ced16bcd97fdd68b1964695d01bece450e5996626e` |
|  `1.25.4`                                     | February 24th | `sha256:9cce6c67c785997a2dd1842c08271b93bd0711281b7c91eab8876b5874f5061d` |

