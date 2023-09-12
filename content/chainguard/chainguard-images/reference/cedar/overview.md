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

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:0afe6688ca5800ac43dbc70410f41ffed5957d4d039aa646ad42e386565f91a6` |
|  `latest`     | September 11th | `sha256:c3b50d6b89ddf9f2ac3be4d0c1ca05988765d0e98764cf754a3030afb4a9a9a1` |



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

