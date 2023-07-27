---
title: "Flux Image Variants"
type: "article"
description: "Detailed information about the Flux Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Flux"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Flux** Image.

## Variants Compared
The **flux** Chainguard Image currently has 14 public variants: 

- `latest.source-controller`
- `latest.source-controller-dev`
- `latest.notification-controller`
- `latest.notification-controller-dev`
- `latest.kustomize-controller`
- `latest.kustomize-controller-dev`
- `latest.image-reflector-controller`
- `latest.image-reflector-controller-dev`
- `latest.image-automation-controller`
- `latest.image-automation-controller-dev`
- `latest.helm-controller`
- `latest.helm-controller-dev`
- `latest.cli`
- `latest.cli-dev`

The table has detailed information about each of these variants.

|              | latest.source-controller     | latest.source-controller-dev | latest.notification-controller     | latest.notification-controller-dev | latest.kustomize-controller     | latest.kustomize-controller-dev | latest.image-reflector-controller     | latest.image-reflector-controller-dev | latest.image-automation-controller     | latest.image-automation-controller-dev | latest.helm-controller     | latest.helm-controller-dev | latest.cli      | latest.cli-dev  |
|--------------|------------------------------|------------------------------|------------------------------------|------------------------------------|---------------------------------|---------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|----------------------------------------|----------------------------|----------------------------|-----------------|-----------------|
| Default User | `nonroot`                    | `nonroot`                    | `nonroot`                          | `nonroot`                          | `nonroot`                       | `nonroot`                       | `nonroot`                             | `nonroot`                             | `nonroot`                              | `nonroot`                              | `nonroot`                  | `nonroot`                  | `nonroot`       | `nonroot`       |
| Entrypoint   | `/usr/bin/source-controller` | `/usr/bin/source-controller` | `/usr/bin/notification-controller` | `/usr/bin/notification-controller` | `/usr/bin/kustomize-controller` | `/usr/bin/kustomize-controller` | `/usr/bin/image-reflector-controller` | `/usr/bin/image-reflector-controller` | `/usr/bin/image-automation-controller` | `/usr/bin/image-automation-controller` | `/usr/bin/helm-controller` | `/usr/bin/helm-controller` | `/usr/bin/flux` | `/usr/bin/flux` |
| CMD          | not specified                | not specified                | not specified                      | not specified                      | not specified                   | not specified                   | not specified                         | not specified                         | not specified                          | not specified                          | not specified              | not specified              | `help`          | `help`          |
| Workdir      | not specified                | not specified                | not specified                      | not specified                      | not specified                   | not specified                   | not specified                         | not specified                         | not specified                          | not specified                          | not specified              | not specified              | not specified   | not specified   |
| Has apk?     | no                           | yes                          | no                                 | yes                                | no                              | yes                             | no                                    | yes                                   | no                                     | yes                                    | no                         | yes                        | no              | yes             |
| Has a shell? | no                           | yes                          | no                                 | yes                                | no                              | yes                             | no                                    | yes                                   | no                                     | yes                                    | no                         | yes                        | yes             | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/flux/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                    | latest.source-controller | latest.source-controller-dev | latest.notification-controller | latest.notification-controller-dev | latest.kustomize-controller | latest.kustomize-controller-dev | latest.image-reflector-controller | latest.image-reflector-controller-dev | latest.image-automation-controller | latest.image-automation-controller-dev | latest.helm-controller | latest.helm-controller-dev | latest.cli | latest.cli-dev |
|------------------------------------|--------------------------|------------------------------|--------------------------------|------------------------------------|-----------------------------|---------------------------------|-----------------------------------|---------------------------------------|------------------------------------|----------------------------------------|------------------------|----------------------------|------------|----------------|
| `flux-source-controller`           | X                        | X                            |                                |                                    |                             |                                 |                                   |                                       |                                    |                                        |                        |                            |            |                |
| `flux-notification-controller`     |                          |                              | X                              | X                                  |                             |                                 |                                   |                                       |                                    |                                        |                        |                            |            |                |
| `flux-kustomize-controller`        |                          |                              |                                |                                    | X                           | X                               |                                   |                                       |                                    |                                        |                        |                            |            |                |
| `flux-image-reflector-controller`  |                          |                              |                                |                                    |                             |                                 | X                                 | X                                     |                                    |                                        |                        |                            |            |                |
| `flux-image-automation-controller` |                          |                              |                                |                                    |                             |                                 |                                   |                                       | X                                  | X                                      |                        |                            |            |                |
| `flux-helm-controller`             |                          |                              |                                |                                    |                             |                                 |                                   |                                       |                                    |                                        | X                      | X                          |            |                |
| `busybox`                          |                          |                              |                                |                                    |                             |                                 |                                   |                                       |                                    |                                        |                        |                            | X          | X              |
| `flux`                             |                          |                              |                                |                                    |                             |                                 |                                   |                                       |                                    |                                        |                        |                            | X          | X              |
| `flux-compat`                      |                          |                              |                                |                                    |                             |                                 |                                   |                                       |                                    |                                        |                        |                            | X          | X              |
