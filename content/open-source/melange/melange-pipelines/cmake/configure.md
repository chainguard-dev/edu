---
title: "cmake/configure"
type: "article"
description: "Reference docs for the cmake/configure melange pipeline"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["MELANGE", "REFERENCE"]
images: []
menu:
  docs:
    parent: "melange"
weight: 600
toc: true
---


Configure a CMake project

### Dependencies
- cmake
- ninja


### Reference
| Input        | Description                                                          |
|--------------|----------------------------------------------------------------------|
| `output-dir` | The output directory for the CMake build. Default is set to `output` |
| `opts`       | Compile options for the CMake build.                                 |


### Example
```yaml
uses: cmake/configure

```
