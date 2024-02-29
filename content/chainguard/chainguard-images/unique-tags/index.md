---
title: "Unique Tags for Chainguard Images"
linktitle: "Unique Tags"
type: "article"
description: "Overview of what Chainguard's Unique Tags are and how to access them."
date: 2024-02-29T08:49:31+00:00
lastmod: 2024-02-29T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Product", "Overview"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 735
toc: true
---

Some organizations use image tags as an indication that there is a new container image available in a registry. Oftentimes, these organizations' internal automation and policies expect each new build to have its own distinct tag.

To help with cases like this, Chainguard offers Unique Tags for private registries. Unique Tags are ideal for organizations that require a strict tag per release or update of their images. They benefit teams looking for precise tracking and management of container images. 

This guide provides an overview of what these Unique Tags are, the kinds of problems they aim to solve, and how you can access them in the Chainguard Console.


## Chainguard's Unique Tags

Unique Tags are only available for private registries, as the public Chainguard Registry only has the `:latest` or, in some cases, the `:latest-dev` tags available. Unique Tags feature an opt-in feature, which allows customers the flexibility to enable it based on their specific operational and security requirements.

Chainguard's Unique Tags end in a timestamp, such as `20240229`, which indicates the date when the Image was built. Because Chainguard Images are rebuilt daily, this ensures that the specific tag will always represent that specific Image build and not another.

One benefit of using this timestamp scheme with Unique Tags is that it can help users to quickly identify when a given version of an Image was built. It also helps to make them human-readable, as opposed to the long, unpronounceable strings that make up Image digests.

Unique Tags also allow for individual image repositories within a registry to be included or excluded as needed. For example, if you have an application that requires a specific tagging scheme to be compatible with an existing Helm chart, you can enable Unique Tags for your registry, but exclude that specific repository so that its Images only receive the standard tags.

This granular level of control ensures that organizations can implement unique tagging in a way that best suits their organization's specific needs. It offers a tailored approach to image management, allowing for precise and efficient tracking of image versions and builds across different environments.

Additionally, be aware that the Unique Tags feature is integrated with Chainguard's [Tag History](/chainguard/chainguard-images/using-the-tag-history-api/) and [Diff APIs](/chainguard/chainguard-images/using-the-image-diff-api/), as well as the [`chainctl diff` command](/chainguard/chainguard-images/comparing-images/) and [event notifications](/chainguard/administration/cloudevents/events-reference/). These integrations allow you to track changes, compare different image versions, and understand the differences between various builds. It empowers organizations to maintain a detailed and accessible record of their container images, facilitating easier analysis and decision-making.


## How do I find Unique Tags?

After signing into the Chainguard Console, click on **Organization images** in the left-hand navigation. This will take you to your organization's Images directory where you'll be presented with a list of all the Chainguard Production Images your organization has access to.

To the right of the search box and **Category** drop-down menu is a toggle button labeled **Include unique tags**. 

![Screenshot of the Organization images page, showing four Images in a table. The "Include unique tags" button is highlighted with a yellow box.](unique-tags-1.png)

By toggling this button on, each individual Image's details page will show the Unique Tags available for it.

To illustrate, toggle this button on and then click on any Production Image listed in your organization's directory. This example shows a partial list of available versions of the `busybox` Image from the **Versions** tab on its details page.

![Screenshot of a portion of the busybox Image's Versions tab. This screenshot shows the ten most recently built versions, some of which include unique tags such as "latest-20230610."](unique-tags-2.png)

Here there are a number of Image versions with tags similar to `:latest-20230626`. You can read this as "latest as of June 26, 2023," meaning that this particular version of the Image was last updated on June 26, 2023. You can use this version's **Pull URL** (`cgr.dev/chainguard-private/busybox:latest-20230626`) to download this Image, and you can be confident that this Pull URL will always refer to the same Image.


## Accessing Unique Tags

As mentioned previously, Unique Tags are an opt-in feature that is only available for private registries. If your organization is interested in using Unique Tags, please [contact support](https://support.chainguard.dev/hc/en-us) and we will enable this feature for you.


## Learn More

It should be noted that by their design, container image tags are mutable, meaning that they can change over time. Although Unique Tags are meant to serve as a secure solution for teams whose internal workflows assume tag immutability, we still recommend that users pull Images by their digests whenever possible. Check out the ["Pulling by Digest" section](/chainguard/chainguard-images/how-to-use-chainguard-images/#pulling-by-digest) of our guide on How to Use Chainguard images for more information. You may also find our video on [How to Use Container Image Digests to Improve Reproducibility](/chainguard/chainguard-images/videos/container-image-digests/) to be useful.

Additionally, you may find our three-part blog series on Chainguard's image tagging philosophy to be of interest. 

* [Part 1](https://www.chainguard.dev/unchained/chainguards-image-tagging-philosophy-enabling-high-velocity-updates-pt-1-of-3)
* [Part 2](https://www.chainguard.dev/unchained/chainguards-image-tagging-philosophy-enabling-high-velocity-updates-pt-2-of-3)
* [Part 3](https://www.chainguard.dev/unchained/chainguards-image-tagging-philosophy-enabling-high-velocity-updates-pt-3-of-3)
