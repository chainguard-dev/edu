---
title: "Image Overview: skaffold"
type: "article"
description: "Overview: skaffold Chainguard Image"
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

[cgr.dev/chainguard/skaffold](https://github.com/chainguard-images/images/tree/main/images/skaffold)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 29th    | `sha256:1c35fd32ac80fd63fc47cf3221e06b57fca27ad72fd4c0bfcd1c51d0c81b71a3` |
|  `latest`     | July 29th    | `sha256:badd9f003d74fdf1310663e74b7c553fd9463f5b2b3de79531036d1e051bb1f0` |



Minimal container image for running skaffold apps

The image specifies a default non-root `skaffold` user (UID 65532), and a working directory at `/app`, owned by that `skaffold` user, and accessible to all users.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/skaffold:latest
```

This image includes `skaffold`, `helm`, `kubectl`, `kpt`, `kustomize`, and the `google-cloud-sdk.`

## Usage

This image should be a drop-in replacement for the upstream `skaffold-slim` image.
See the [full documentation](https://skaffold.dev/docs/install/#standalone-binary) for usage.


```
% docker run cgr.dev/chainguard/skaffold:latest
A tool that facilitates continuous development for Kubernetes applications.

  Find more information at: https://skaffold.dev/docs/getting-started/

End-to-end Pipelines:
  run               Run a pipeline
  dev               Run a pipeline in development mode
  debug             Run a pipeline in debug mode

Pipeline Building Blocks:
  build             Build the artifacts
  test              Run tests against your built application images
  deploy            Deploy pre-built artifacts
  delete            Delete any resources deployed by Skaffold
  render            Generate rendered Kubernetes manifests
  apply             Apply hydrated manifests to a cluster
  verify            Run verification tests against skaffold deployments

Getting Started With a New Project:
  init              Generate configuration for deploying an application

Other Commands:
  completion        Output shell completion for the given shell (bash, fish or zsh)
  config            Interact with the global Skaffold config file (defaults to `$HOME/.skaffold/config`)
  diagnose          Run a diagnostic on Skaffold
  fix               Update old configuration to a newer schema version
  schema            List JSON schemas used to validate skaffold.yaml configuration
  survey            Opens a web browser to fill out the Skaffold survey
  version           Print the version information

Usage:
  skaffold [flags] [options]

Use "skaffold <command> --help" for more information about a given command.
Use "skaffold options" for a list of global command-line options (applies to all commands).
```

