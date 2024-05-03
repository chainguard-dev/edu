---
title: "wazero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wazero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/wazero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/wazero/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/wazero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/wazero/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 2nd      | `sha256:38fdabb1b6eb9b18a2a3a0caf15e83d8890a6c81c45ef7296740d02f4aa2e890` |
|  `latest`     | May 2nd      | `sha256:d355b3e33f374ee7141a2766c30633b2258aa9d8b066691ef66cbcce9bbfc2a4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.7-dev` `latest-dev` `1-dev` `1.7.1-dev` | May 2nd      | `sha256:99b39307461bb633dd7514f3ce19f98eed5fdba7791b0ce7a0ce1cd5e0750ec3` |
|  `1.7.1` `latest` `1.7` `1`                 | May 2nd      | `sha256:6521cc761456d17c221659ea934de7e021067555025f31a4df452f1428bb89b7` |
|  `1.7.0-dev`                                | April 11th   | `sha256:9b2efa0651ddb5d06207f230565fc32cd08dd489e98975891b719811083e790e` |
|  `1.7.0`                                    | April 3rd    | `sha256:0085750aebcf356339c8cf2c77d7ebab067aaae80414dd217c17ae52bb99233f` |

