---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-10 00:53:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest`            | April 9th    | `sha256:09284fac69c6f1ac1192c23d64fcb4ee12bcc6e6c86f5e0b5e1d0b748c3e2692` |
|  `latest-dev`        | April 9th    | `sha256:52b2b5ba261bff6434ad5ece960dc6561bc1718c1cf7b7ec6c1f97a079457cb3` |
|  `latest-splunk-dev` | April 9th    | `sha256:757f3dd86adefbd920c57f2f235bed147e1b1ad8ffc57b293c588f76dbfef9cf` |
|  `latest-splunk`     | April 9th    | `sha256:4c41a8a95a109730d1d804e52c455faea3a6ada0293d12c4530627c77ca7643c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-splunk-dev` `1-splunk-dev` `1.16.5-r0-splunk-dev` `1.16-splunk-dev` | April 9th    | `sha256:dc8f37393e8a29e9187d673f8e8c3a24a8e187752ac73f5fa4930f85250777be` |
|  `1.16.5-splunk` `1.16.5-r0-splunk` `1-splunk` `1.16-splunk`                 | April 9th    | `sha256:1d2235b8f313322de79e9f08d2f259d850f6a1849eaa64dbeaabd8556cb59e1c` |
|  `1.16-dev` `1.16.5-dev` `latest-dev` `1-dev`                                | April 9th    | `sha256:d4d26768fb224befa3fccb7369b5fb8451317baf24c467c21635d84a242783f2` |
|  `latest` `1` `1.16.5` `1.16`                                                | April 9th    | `sha256:6d4d46ccebb4c551a865318fb84e7296d2040172d52e44bc465b7e12eee6bd49` |
|  `1.16.4-splunk-dev` `1.16.4-r0-splunk-dev`                                  | March 27th   | `sha256:3b27787033b3648c3de96fcd0654098ce79a13f43b2ad6d7dc4f80f2d2db32ba` |
|  `1.16.4-dev`                                                                | March 27th   | `sha256:11600998fec349115f2dce10d0676de2604ee2cfe9e5d9af79d99dd0d19a1a1a` |
|  `1.16.4-splunk` `1.16.4-r0-splunk`                                          | March 22nd   | `sha256:c18d359ef44a76b99ed6695ce4b231bc621b56f19d8659c49ae9f46218fb18ad` |
|  `1.16.4`                                                                    | March 22nd   | `sha256:1eb2f9c7c9b9a0fc95f8e2eb516614490790b30dbb8c1b5fc78699386cb7851a` |
|  `1.16.3-r1-splunk-dev` `1.16.3-splunk-dev`                                  | March 14th   | `sha256:0fef6f7c2cd7b2050db62430cfcbda1321040a445611bd45912694c722feb2ba` |
|  `1.16.3-r1-splunk` `1.16.3-splunk`                                          | March 14th   | `sha256:7c8e444a1bd10fe1b2ff2420375ac5a307d06b9063555dc20522cc6725758e6c` |
|  `1.16.3`                                                                    | March 14th   | `sha256:a73b93df29394adca0c321d669efec4d21b1d50ab3e4f19728196a8023b66e2b` |
|  `1.16.3-dev`                                                                | March 14th   | `sha256:12cb8789fef98f45bd4be9de57f7e2974dd2109ae39dbbfe0fe00c7a2a8d447a` |

