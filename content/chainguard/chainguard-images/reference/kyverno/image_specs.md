---
title: "kyverno Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kyverno Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kyverno/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kyverno/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kyverno/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kyverno/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kyverno** Image.

## Variants Compared
The **kyverno** Chainguard Image currently has 6 public variants: 

- `background-controller-latest`
- `cleanup-controller-latest`
- `cli-latest`
- `latest`
- `reports-controller-latest`
- `kyvernopre-latest`

The table has detailed information about each of these variants.

|              | background-controller-latest     | cleanup-controller-latest     | cli-latest                 | latest             | reports-controller-latest     | kyvernopre-latest     |
|--------------|----------------------------------|-------------------------------|----------------------------|--------------------|-------------------------------|-----------------------|
| Default User | `65532`                          | `65532`                       | `65532`                    | `65532`            | `65532`                       | `65532`               |
| Entrypoint   | `/usr/bin/background-controller` | `/usr/bin/cleanup-controller` | `/usr/bin/kubectl-kyverno` | `/usr/bin/kyverno` | `/usr/bin/reports-controller` | `/usr/bin/kyvernopre` |
| CMD          | `help`                           | `help`                        | `help`                     | `help`             | `help`                        | `help`                |
| Workdir      | not specified                    | not specified                 | not specified              | not specified      | not specified                 | not specified         |
| Has apk?     | no                               | no                            | no                         | no                 | no                            | no                    |
| Has a shell? | no                               | no                            | no                         | no                 | no                            | no                    |

Check the [tags history page](/chainguard/chainguard-images/reference/kyverno/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | background-controller-latest | cleanup-controller-latest | cli-latest | latest | reports-controller-latest | kyvernopre-latest |
|---------------------------------|------------------------------|---------------------------|------------|--------|---------------------------|-------------------|
| `ca-certificates-bundle`        | X                            | X                         | X          | X      | X                         | X                 |
| `kubectl-1.28`                  | X                            | X                         | X          | X      | X                         | X                 |
| `kubectl-latest`                | X                            | X                         | X          | X      | X                         | X                 |
| `kyverno-background-controller` | X                            |                           |            |        |                           |                   |
| `wolfi-baselayout`              | X                            | X                         | X          | X      | X                         | X                 |
| `kyverno-cleanup-controller`    |                              | X                         |            |        |                           |                   |
| `kyverno-cli`                   |                              |                           | X          |        |                           |                   |
| `kyverno`                       |                              |                           |            | X      |                           |                   |
| `kyverno-reports-controller`    |                              |                           |            |        | X                         |                   |
| `kyverno-init-container`        |                              |                           |            |        |                           | X                 |

