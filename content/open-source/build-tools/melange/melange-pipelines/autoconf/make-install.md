---
title: "autoconf/make-install"
aliases:
- /open-source/melange/melange-pipelines/autoconf/make-install
type: "article"
description: "Reference docs for the autoconf/make-install melange pipeline"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["melange", "Reference"]
images: []
menu:
  docs:
    parent: "melange"
weight: 600
toc: true
---


Run autoconf make install

### Dependencies
- make


### Reference
| Input | Description                                                  |
|-------|--------------------------------------------------------------|
| `dir` | The directory containing the Makefile. Default is set to `.` |


### Example
```yaml
- uses: autoconf/make-install

```
