---
title: "meson/configure"
type: "article"
description: "Reference docs for the meson/configure melange pipeline"
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


Configure project with meson

### Dependencies
- meson


### Reference
| Input        | Description                                                          |
|--------------|----------------------------------------------------------------------|
| `output-dir` | The output directory for the Meson build. Default is set to `output` |
| `opts`       | Compile options for the Meson build.                                 |


### Example
```yaml
uses: meson/configure

```
