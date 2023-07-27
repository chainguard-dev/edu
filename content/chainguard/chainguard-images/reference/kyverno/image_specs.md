---
title: "Kyverno Image Variants"
type: "article"
description: "Detailed information about the Kyverno Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kyverno"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kyverno** Image.

## Variants Compared
The **kyverno** Chainguard Image currently has 12 public variants: 

- `latest.reports`
- `latest.reports-dev`
- `latest.init`
- `latest.init-dev`
- `latest.cli`
- `latest.cli-dev`
- `latest.cleanup`
- `latest.cleanup-dev`
- `latest.background`
- `latest.background-dev`
- `latest.admission`
- `latest.admission-dev`

The table has detailed information about each of these variants.

|              | latest.reports                | latest.reports-dev            | latest.init           | latest.init-dev       | latest.cli                 | latest.cli-dev             | latest.cleanup                | latest.cleanup-dev            | latest.background                | latest.background-dev            | latest.admission   | latest.admission-dev |
|--------------|-------------------------------|-------------------------------|-----------------------|-----------------------|----------------------------|----------------------------|-------------------------------|-------------------------------|----------------------------------|----------------------------------|--------------------|----------------------|
| Default User | `nonroot`                     | `nonroot`                     | `nonroot`             | `nonroot`             | `nonroot`                  | `nonroot`                  | `nonroot`                     | `nonroot`                     | `nonroot`                        | `nonroot`                        | `nonroot`          | `nonroot`            |
| Entrypoint   | `/usr/bin/reports-controller` | `/usr/bin/reports-controller` | `/usr/bin/kyvernopre` | `/usr/bin/kyvernopre` | `/usr/bin/kubectl-kyverno` | `/usr/bin/kubectl-kyverno` | `/usr/bin/cleanup-controller` | `/usr/bin/cleanup-controller` | `/usr/bin/background-controller` | `/usr/bin/background-controller` | `/usr/bin/kyverno` | `/usr/bin/kyverno`   |
| CMD          | `help`                        | `help`                        | `help`                | `help`                | `help`                     | `help`                     | `help`                        | `help`                        | `help`                           | `help`                           | `help`             | `help`               |
| Workdir      | not specified                 | not specified                 | not specified         | not specified         | not specified              | not specified              | not specified                 | not specified                 | not specified                    | not specified                    | not specified      | not specified        |
| Has apk?     | no                            | yes                           | no                    | yes                   | no                         | yes                        | no                            | yes                           | no                               | yes                              | no                 | yes                  |
| Has a shell? | no                            | yes                           | no                    | yes                   | no                         | yes                        | no                            | yes                           | no                               | yes                              | no                 | yes                  |

Check the [tags history page](/chainguard/chainguard-images/reference/kyverno/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                 | latest.reports | latest.reports-dev | latest.init | latest.init-dev | latest.cli | latest.cli-dev | latest.cleanup | latest.cleanup-dev | latest.background | latest.background-dev | latest.admission | latest.admission-dev |
|---------------------------------|----------------|--------------------|-------------|-----------------|------------|----------------|----------------|--------------------|-------------------|-----------------------|------------------|----------------------|
| `kyverno-reports-controller`    | X              | X                  |             |                 |            |                |                |                    |                   |                       |                  |                      |
| `kubectl`                       | X              | X                  | X           | X               | X          | X              | X              | X                  | X                 | X                     | X                | X                    |
| `kyverno-init-container`        |                |                    | X           | X               |            |                |                |                    |                   |                       |                  |                      |
| `kyverno-cli`                   |                |                    |             |                 | X          | X              |                |                    |                   |                       |                  |                      |
| `kyverno-cleanup-controller`    |                |                    |             |                 |            |                | X              | X                  |                   |                       |                  |                      |
| `kyverno-background-controller` |                |                    |             |                 |            |                |                |                    | X                 | X                     |                  |                      |
| `kyverno`                       |                |                    |             |                 |            |                |                |                    |                   |                       | X                | X                    |
