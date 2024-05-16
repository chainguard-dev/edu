---
title: "Image Overview: gpu-feature-discovery"
linktitle: "gpu-feature-discovery"
type: "article"
layout: "single"
description: "Overview: gpu-feature-discovery Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gpu-feature-discovery/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gpu-feature-discovery/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gpu-feature-discovery/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gpu-feature-discovery/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [gpu-feature-discovery](https://github.com/NVIDIA/gpu-feature-discovery) container image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/gpu-feature-discovery:latest
```


<!--body:start-->
## Usage

NVIDIA GPU Feature Discovery for Kubernetes is a software component that allows you to automatically generate labels for the set of GPUs available on a node
For more information, refer to the GFD documentation:
- [GFD Github README](https://github.com/NVIDIA/gpu-feature-discovery/blob/main/README.md#installing-via-helm-install)

```shell
NAME:
   GPU Feature Discovery - generate labels for NVIDIA devices

USAGE:
   GPU Feature Discovery [global options] command [command options] [arguments...]

VERSION:
   0.8.2
commit: 47a1ea6862f69844c5364c98a77aa97fe9ea7b74

COMMANDS:
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --mig-strategy value                           the desired strategy for exposing MIG devices on GPUs that support it:
                                                    [none | single | mixed] (default: "none") [$GFD_MIG_STRATEGY, $MIG_STRATEGY]
   --fail-on-init-error                           fail the plugin if an error is encountered during initialization, otherwise block indefinitely (default: true) [$GFD_FAIL_ON_INIT_ERROR, $FAIL_ON_INIT_ERROR]
   --oneshot                                      Label once and exit (default: false) [$GFD_ONESHOT]
   --no-timestamp                                 Do not add the timestamp to the labels (default: false) [$GFD_NO_TIMESTAMP]
   --sleep-interval value                         Time to sleep between labeling (default: 1m0s) [$GFD_SLEEP_INTERVAL]
   --output-file value, --output value, -o value  (default: "/etc/kubernetes/node-feature-discovery/features.d/gfd") [$GFD_OUTPUT_FILE]
   --machine-type-file value                      a path to a file that contains the DMI (SMBIOS) information for the node (default: "/sys/class/dmi/id/product_name") [$GFD_MACHINE_TYPE_FILE]
   --config-file value                            the path to a config file as an alternative to command line options or environment variables [$GFD_CONFIG_FILE, $CONFIG_FILE]
   --use-node-feature-api                         Use NFD NodeFeature API to publish labels (default: false) [$GFD_USE_NODE_FEATURE_API]
   --help, -h                                     show help
   --version, -v                                  print the version
```

Helm Installation for GPU Feature Discovery

Step 1: Add and Update Helm Repository
Add the NVIDIA GFD Helm repository and update it to ensure you have access to the latest charts.

```shell
$ helm repo add nvgfd https://nvidia.github.io/gpu-feature-discovery
$ helm repo update
```

Step 2: Install GPU Feature Discovery
Install GPU Feature Discovery using Helm with the specified version, namespace, and optional configuration settings.

This command deploys GPU Feature Discovery as a standalone chart in the gpu-feature-discovery namespace.
```shell
$ helm upgrade -i nvgfd nvgfd/gpu-feature-discovery \
  --version 0.8.2 \
  --namespace gpu-feature-discovery \
  --create-namespace
```

Step 3: Verify Installation
Verify that the GPU Feature Discovery DaemonSet is running in the specified namespace.

```shell
$ kubectl get daemonset -n gpu-feature-discovery -l app.kubernetes.io/name=gpu-feature-discovery
```
For more information, refer to the documentation:
- [Helm Installation Guide](https://github.com/NVIDIA/gpu-feature-discovery/blob/main/README.md#installing-via-helm-install)
<!--body:end-->

