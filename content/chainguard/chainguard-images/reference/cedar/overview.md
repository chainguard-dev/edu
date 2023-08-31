---
title: "Image Overview: cedar"
type: "article"
description: "Overview: cedar Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/cedar](https://github.com/chainguard-images/images/tree/main/images/cedar)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 30th  | `sha256:9f0ec10e729edc1c939b0a6e5fc30c8e7f6da9aeff5b2c14ec34f0850a2973f3` |
|  `latest-dev` | August 30th  | `sha256:16c27f6a769e15d178952e1a5c5188070e8982a7014a59e971676e83f3b0074a` |



This image contains the CLI for the [Cedar Policy](https://www.cedarpolicy.com/en) Language.
The binary can be used to run, test, format, or evaluate Cedar policies

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cedar:latest
```

## Use It!

The image can be run directly and sets the cedar image as the entrypoint:

```
docker run cgr.dev/chainguard/cedar:latest
CLI interface for the Cedar Policy language.

Usage: cedar <COMMAND>

Commands:
  authorize    Evaluate an authorization request
  evaluate     Evaluate a Cedar expression
  validate     Validate a policy set against a schema
  check-parse  Check that policies successfully parse
  link         Link a template
  format       Format a policy set
  help         Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help
  -V, --version  Print version
  ```

```

