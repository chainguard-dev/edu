---
title: "git-checkout"
type: "article"
description: "Reference docs for the git-checkout melange pipeline"
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


Check out sources from git

### Dependencies
- git


### Reference
| Input         | Description                                                 |
|---------------|-------------------------------------------------------------|
| `repository`* | The repository to check out sources from.                   |
| `destination` | The path to check out the sources to. Default is set to `.` |
| `depth`       | The depth to use when cloning. Default is set to `50`       |
| `branch`      | The branch to check out, otherwise HEAD is checked out.     |


### Example
```yaml
- uses: git-checkout
  with:
    repository: https://github.com/envoyproxy/envoy
    branch: v${{package.version}}
    destination: envoy
```
