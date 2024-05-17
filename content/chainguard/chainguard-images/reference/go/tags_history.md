---
title: "go Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the go Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/go/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/go/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/go/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/go/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 16th     | `sha256:10e075d69ae7d3914578ba057bb13420249a21b2cc2f72abe19131e469e31ed5` |
|  `latest`     | May 16th     | `sha256:9bb4a05365c3384c0a0ae925f1a86bd9bddbaed035a899ed7bcf9d7b2dc747ae` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.19-dev` `1.19.13-dev`                     | May 16th     | `sha256:45913711f23c48b74e4cec5b4c74c1f08dae0affd96a4fb4a2f7d949443aa57d` |
|  `1.21.10` `1.21`                             | May 16th     | `sha256:963372e025a7e4c249b9eba404713d0155d882690f7ea2cb7745e1253806acf4` |
|  `1.20.14-dev` `1.20-dev`                     | May 16th     | `sha256:c5d59672f8ac043cb187f96e4ecc8c20d7215d43010fab39ecda16df6c05518d` |
|  `1.21.10-dev` `1.21-dev`                     | May 16th     | `sha256:7dec323c0e357fe01fcaca515bef6a09591027aec33f47d1afbb74c823c2ab3c` |
|  `1` `1.22.3` `1.22` `latest`                 | May 16th     | `sha256:a5904bc7be322338342644bd4105fc573168c4109824f4310de5e11a5b0513fb` |
|  `1.17` `1.17.13`                             | May 16th     | `sha256:77b2c9567cbdc78dd8a06b0cc3164e27e0532910bdcc6a7fea941453ec60a1d0` |
|  `1.17.13-dev` `1.17-dev`                     | May 16th     | `sha256:4292b9fc6fd6e33950a555199eda97164b5fd28a77b510c5d4955c320ef2ee52` |
|  `1.18` `1.18.10`                             | May 16th     | `sha256:9e39fb821fe33ac4e76f734709cfb168a475086d9b8e7dc1921a045078521726` |
|  `1.18.10-dev` `1.18-dev`                     | May 16th     | `sha256:8481b0602f17cac65c1eeec8c4e6106411f7a5f7790db5ef51212b5d1bfaa8d8` |
|  `1.20` `1.20.14`                             | May 16th     | `sha256:3adf554f4f83573e86000c9cd271b671e8e0cebc22bfe2f468432390f6f23626` |
|  `1.22-dev` `latest-dev` `1-dev` `1.22.3-dev` | May 16th     | `sha256:a8bc199b342ed8f5dd7409e34bed75cd9f53eca1006adb50c32849ad8db080e6` |
|  `1.19.13` `1.19`                             | May 16th     | `sha256:4a772ec889382c787fa3bcd80e00c6dd87f19370c2ffabd43c50152e66179615` |
|  `1.21.9`                                     | May 2nd      | `sha256:5d9d7e9964c94a6e9c3ee76aec4c7ee8241270a84b6aa0117bc9f36eea1c1c5f` |
|  `1.22.2`                                     | May 2nd      | `sha256:5664b8cd131b8d8002ab658debb989e74504a0a63cc6c8b5e5b634612d61df84` |
|  `1.22.2-dev`                                 | May 2nd      | `sha256:7803a5c3307994c91c1a32e36cd01b32b82c32babb952599aefdd0ed827c3e89` |
|  `1.21.9-dev`                                 | May 2nd      | `sha256:adf5aa4cb4542297930f03c44e0539ae89acdc8e565c26fffee6dca569e5891b` |
|  `1.19.8`                                     | May 2nd      | `sha256:06838d22698818b0efe3dfaae3734464070be3061e379266f6c710728b22cb54` |
|  `1.20.3-dev`                                 | May 2nd      | `sha256:7723d919c3839a569d534c74f719cd02232ad13e4a1185a381909422f2e87c8c` |
|  `1.19.8-dev`                                 | May 2nd      | `sha256:eb613f6a2cdfb70c5d50be5d9183b575754ec83fee35e8f62d7cb02b7875bbb2` |
|  `1.20.3`                                     | May 2nd      | `sha256:47a6d2a9faeaa739803fa495ef0721055a24142ebd1f0ab4e2306b6cebf860d1` |

