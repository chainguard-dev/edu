---
title: "chainctl images"
lead: ""
description: "chainctl images basics"
type: "article"
date: 2025-03-0620T08:49:15+00:00
lastmod: 2025-03-0620T08:49:15+00:00
draft: false
tags: ["chainctl", "images", "Product"]
images: []
weight: 70
---

This page presents some of the more commonly used `chainctl images` commands. For a full reference of all commands with details and switches, see [chainctl Reference](/chainguard/chainctl/).


## `chainctl images list`

To see which Chainguard Images are available to your account, use:

```shell
chainctl images list
```

Be warned, that list may take a while to generate and is likely to scroll past quickly in your command line terminal. You may prefer to direct the output into a file.


## `chainctl images repos list`

For a list of image repositories available to your account, use:

```shell
chainctl images repos list
```


## `chainctl images diff`

This useful command enables you to compare two Chainguard images. To use it, enter:

```shell
chainctl images diff $FROM_IMAGE $TO_IMAGE
```

There is a full docs page on this command. See <ins>[How To Compare Chainguard Images with chainctl](/chainguard/chainguard-images/how-to-use/comparing-images/)</ins> to learn more.