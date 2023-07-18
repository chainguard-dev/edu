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
|  `latest`     | July 18th    | `sha256:afe386c80c6e60b4686ef2a80bc7ad8a40b6a6bd09d865944684864e85882c65` |
|  `latest-dev` | July 18th    | `sha256:8b0d4a22fc735a48a0726252ed2f3d2bd3e93ff153b4a83ac2863878ae8344d4` |
|               | July 12th    | `sha256:0755b41aa9c452c854474d3a9d99780fc9454ff0c9a05704029aadb8b0ab9dca` |
|               | July 4th     | `sha256:435e79e90dba4a0ae34f3cc04c542a6603729cfc8d74b8c5aaad27383dea3e41` |
|               | June 28th    | `sha256:3592d4c7a38b7798e7bbe185dd123a5890d88f9f40ba7bea4213738589173445` |
|               | June 26th    | `sha256:ab33d352337c6140d5055a6bca00c7a6d07773ee559fd1fc97d0409eb22761af` |
|               | June 26th    | `sha256:8bb713402fd849bf0700467cb2c142ac91e25ffc51f7d8517d02fc5de74857f8` |



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

