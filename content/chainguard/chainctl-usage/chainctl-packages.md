---
title: "chainctl packages"
lead: ""
description: "chainctl packages basics"
type: "article"
date: 2025-03-06T08:49:15+00:00
lastmod: 2025-03-06T08:49:15+00:00
draft: false
tags: ["chainctl", "packages", "Product"]
images: []
weight: 100
---

This page presents the most commonly used `chainctl packages` command. For a full reference of all commands with details and switches, see [chainctl Reference](/chainguard/chainctl/).

## List the package versions available

If you want to get details about the various package versions available that can be used in images, use:

```shell
chainctl packages versions list $PACKAGENAME
```

This will list all the versions that Chainguard has built and the end-of-life date for each version that has one assigned. It will also list older package versions that are no longer available.
