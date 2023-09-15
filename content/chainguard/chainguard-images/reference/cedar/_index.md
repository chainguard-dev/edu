---
title: "Image Overview: cedar"
linktitle: "cedar"
type: "article"
layout: "single"
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

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cedar/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/cedar/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cedar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cedar/provenance_info/" >}}
{{</ tabs >}}



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

