---
title: "fetch"
type: "article"
description: "Reference docs for the fetch melange pipeline"
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


Fetch and extract external object into workspace

### Dependencies
- wget


### Reference
| Input              | Description                                                                              |
|--------------------|------------------------------------------------------------------------------------------|
| `strip-components` | The number of path components to strip while extracting. Default is set to `1`           |
| `extract`          | Whether to extract the downloaded artifact as a source tarball. Default is set to `true` |
| `expected-sha256`  | The expected SHA256 of the downloaded artifact.                                          |
| `expected-sha512`  | The expected SHA512 of the downloaded artifact.                                          |
| `uri`*             | The URI to fetch as an artifact.                                                         |


### Example
```yaml
pipeline:
  - uses: fetch
    with:
      uri: https://www.php.net/distributions/php-${{package.version}}.tar.gz
      expected-sha256: 3660e8408321149f5d382bb8eeb9ea7b12ea8dd7ea66069da33f6f7383750ab2

```
