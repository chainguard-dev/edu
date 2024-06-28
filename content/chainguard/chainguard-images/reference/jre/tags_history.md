---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-28 00:31:38
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
|  `latest-dev` | June 26th    | `sha256:dbd7f22536633dadfcfa484cad0f93247e7327128ba37f26759379500b756705` |
|  `latest`     | June 26th    | `sha256:6ddc546709a1c43a6549e6008b54a9e982f84a77c64befaf8b11d1520cb41bc3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | June 27th    | `sha256:a54c5079c266f2b2596c9431a1b875d7f82e5815e0a5a2ed2bba83ebfddf2d32` |
|  `openjdk-8.412.08` `openjdk-8.412` `openjdk-8`                                    | June 27th    | `sha256:311e016619e84c6ccaca98316cbec5787700eae4a5e21d0a8d3f7bc956b6bf54` |
|  `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0`                 | June 26th    | `sha256:ab771a1e5f16506de12812b7969a2e0730bdb7f708ccd8eb5821841caad84f36` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | June 26th    | `sha256:86368596b4d3adf1ed9fc6054a81010e6c5e8e693f0b58ce34c3debd145d66ce` |
|  `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` | June 26th    | `sha256:a145c51a2e3afb2a73f42996b6ad0134fcddae13bb84b64faf8383573d60bee4` |
|  `latest` `openjdk-22.0` `openjdk-22` `openjdk-22.0.1`                             | June 26th    | `sha256:9054cee4df166e942cf51db33cc4354f6da12c5717caa2eb3269fdb44e8ef518` |
|  `openjdk-22.0.1-dev` `openjdk-22.0-dev` `openjdk-22-dev` `latest-dev`             | June 26th    | `sha256:6a37651262844616f7eba02f45b52217bad884d66903852657798a9247f6cdd1` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | June 26th    | `sha256:3385d6187f6ca4f0118da1c84f1c33df3bb6bc3458475d46ab8ec6d38bf5c07f` |
|  `openjdk-16.0.2.7` `openjdk-16.0` `openjdk-16.0.2` `openjdk-16`                   | June 26th    | `sha256:77f93e5d5decd73055750e5f35682059a8a72d9940fb9eacd5212114ba40ce04` |
|  `openjdk-14.0.2` `openjdk-14` `openjdk-14.0.2.12` `openjdk-14.0`                  | June 26th    | `sha256:14897354b916b22f641c747156c99d024239a03d2a7f9387b760ef5d1659c83c` |
|  `openjdk-17.0.11-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | June 26th    | `sha256:05dbcf432649bbf31bdeffb81fc7ea45458223cb94e11c0bbd7ccdec458ef62a` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | June 26th    | `sha256:87977f2b2535a1a6b849f72e1ef3611f504b2df3b6b82dce29232d28a36406db` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | June 26th    | `sha256:1165d305bf04ba93c5e8c68bc1900f5876b33587d4ce5f5743efbb35ad68f0be` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | June 26th    | `sha256:d6cdf783b49a40aa45db2958f0fa0fe69f7b14b6a5490a3cefad0b5e20ae0558` |
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | June 26th    | `sha256:9f7daa3e985971f69afbb10db77a2f1cd49ab0c9a9c840340e9e750be6046af1` |
|  `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev`   | June 26th    | `sha256:58d8ca9bd6df2e7de80c842cab5ceb3757ff94fb53600052ef787399f5f8b349` |

