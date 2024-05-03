---
title: "cmake/build"
aliases:
- /open-source/melange/melange-pipelines/cmake/build
type: "article"
description: "Reference docs for the cmake/build melange pipeline"
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


Build a CMake project

### Dependencies
- cmake
- ninja


### Reference
| Input        | Description                                                          |
|--------------|----------------------------------------------------------------------|
| `output-dir` | The output directory for the CMake build. Default is set to `output` |


### Example
```yaml
uses: cmake/build

```
