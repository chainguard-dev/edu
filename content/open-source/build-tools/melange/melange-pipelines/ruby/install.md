---
title: "ruby/install"
aliases:
- /open-source/melange/melange-pipelines/autoconf/configure
type: "article"
description: "Reference docs for the ruby/install melange pipeline"
date: 2023-04-06T11:07:52+02:0
lastmod: 2023-04-06T11:07:52+02:0
draft: false
tags: ["melange", "Reference"]
images: []
menu:
  docs:
    parent: "melange"
weight: 600
toc: true
---


Install a ruby gem

### Dependencies
- busybox
- ca-certificates-bundle


### Reference
| Input      | Description                                                     |
|------------|-----------------------------------------------------------------|
| `gem`      | Gem name                                                        |
| `gem-file` | The full filename of the gem to build                           |
| `version`* | Gem version to install. This can be a version tag (1.0.0)       |
| `opts`     | Options to pass to the gem install command Default is set to `` |


### Example
There are no examples available.
