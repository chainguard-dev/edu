---
title: "kyverno Image Variants"
type: "article"
description: "Detailed information about the public kyverno Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "kyverno"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **kyverno** Image.

## Variants Compared
The **kyverno** Chainguard Image currently has 5 public variants: 

- `background-controller-latest`
- `cleanup-controller-latest`
- `cli-latest`
- `latest`
- `reports-controller-latest`

The table has detailed information about each of these variants.

|              | background-controller-latest     | cleanup-controller-latest     | cli-latest                 | latest             | reports-controller-latest     |
|--------------|----------------------------------|-------------------------------|----------------------------|--------------------|-------------------------------|
| Default User | `nonroot`                        | `nonroot`                     | `nonroot`                  | `nonroot`          | `nonroot`                     |
| Entrypoint   | `/usr/bin/background-controller` | `/usr/bin/cleanup-controller` | `/usr/bin/kubectl-kyverno` | `/usr/bin/kyverno` | `/usr/bin/reports-controller` |
| CMD          | `help`                           | `help`                        | `help`                     | `help`             | `help`                        |
| Workdir      | not specified                    | not specified                 | not specified              | not specified      | not specified                 |
| Has apk?     | no                               | no                            | no                         | no                 | no                            |
| Has a shell? | no                               | no                            | no                         | no                 | no                            |

Check the [tags history page](/chainguard/chainguard-images/reference/kyverno/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | background-controller-latest | cleanup-controller-latest | cli-latest | latest | reports-controller-latest |
|---------------------------------|------------------------------|---------------------------|------------|--------|---------------------------|
| `ca-certificates-bundle`        | X                            | X                         | X          | X      | X                         |
| `kubectl`                       | X                            | X                         | X          | X      | X                         |
| `kyverno-background-controller` | X                            |                           |            |        |                           |
| `wolfi-baselayout`              | X                            | X                         | X          | X      | X                         |
| `kyverno-cleanup-controller`    |                              | X                         |            |        |                           |
| `kyverno-cli`                   |                              |                           | X          |        |                           |
| `kyverno`                       |                              |                           |            | X      |                           |
| `kyverno-reports-controller`    |                              |                           |            |        | X                         |
