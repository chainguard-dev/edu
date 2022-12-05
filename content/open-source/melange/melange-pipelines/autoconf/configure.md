---
title: "autoconf/configure"
type: "article"
description: "Reference docs for the autoconf/configure melange pipeline"
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


Run the autoconf configure script

### Dependencies
None

### Reference
| Input | Description                                                          |
|-------|----------------------------------------------------------------------|
| `dir` | The directory containing the configure script. Default is set to `.` |


### Example
```yaml
- uses: autoconf/configure
  with:
    opts: |
      PYTHON=/usr/bin/python3 \
      --with-lzma \
      --with-zlib

```
