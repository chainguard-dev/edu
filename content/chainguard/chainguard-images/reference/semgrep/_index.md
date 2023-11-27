---
title: "Image Overview: semgrep"
linktitle: "semgrep"
type: "article"
layout: "single"
description: "Overview: semgrep Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-27 16:34:14
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/semgrep/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/semgrep/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/semgrep/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/semgrep/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
CLI for the [Semgrep](https://semgrep.dev) static analysis tool. Semgrep is a lightweight static analysis tool for many languages. It finds bug variants with patterns that look like source code.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/semgrep:latest
```
<!--getting:end-->

<!--body:start-->
## Use It!

The image can be run directly and sets the semgrep binary as the entrypoint:

```shell
$ docker run cgr.dev/chainguard/semgrep:latest

Usage: semgrep [OPTIONS] COMMAND [ARGS]...

  To get started quickly, run `semgrep scan --config auto`

  Run `semgrep SUBCOMMAND --help` for more information on each subcommand

  If no subcommand is passed, will run `scan` subcommand by default

Options:
  -h, --help  Show this message and exit.

Commands:
  ci                   The recommended way to run semgrep in CI
  install-semgrep-pro  Install the Semgrep Pro Engine
  login                Obtain and save credentials for semgrep.dev
  logout               Remove locally stored credentials to semgrep.dev
  lsp                  [EXPERIMENTAL] Start the Semgrep LSP server
  publish              Upload rule to semgrep.dev
  scan                 Run semgrep rules on files
  shouldafound         Report a false negative in this project.

```
<!--body:end-->

