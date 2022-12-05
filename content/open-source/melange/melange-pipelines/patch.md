---
title: "patch"
type: "article"
description: "Reference docs for the patch melange pipeline"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "melange"
weight: 600
toc: true
---


Apply patches

### Dependencies
- patch


### Reference
| Input              | Description                                                                    |
|--------------------|--------------------------------------------------------------------------------|
| `strip-components` | The number of path components to strip while extracting. Default is set to `1` |
| `patches`*         | A list of patches to apply, as a whitespace delimited string.                  |


### Example
```yaml
- uses: patch
    with:
      patches: libtool-fix-cross-compile.patch
```
