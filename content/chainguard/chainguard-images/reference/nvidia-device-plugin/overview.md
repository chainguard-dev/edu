---
title: "Image Overview: nvidia-device-plugin"
type: "article"
description: "Overview: nvidia-device-plugin Chainguard Image"
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

[cgr.dev/chainguard/nvidia-device-plugin](https://github.com/chainguard-images/images/tree/main/images/nvidia-device-plugin)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:f1865af2c2ccc0ece767a5aa413c95dbb2ef739832ba707f68e08298690d604d` |
|  `latest`     | July 15th    | `sha256:b7e5077531829b92c1862e70486fdc5ab4545d0f556cf1ec43129a6a507413a1` |
|               | July 14th    | `sha256:be0f9073a69cc1c2bcee0aafeca13c3d0e30d3bd9e77abf1790d4b1af9da6863` |
|               | July 14th    | `sha256:ead88aded3096fa5748244ae657b68e76c1de7a10658e8c94d75d3c5aa28f4c7` |
|               | July 12th    | `sha256:ec8cbf3f79aaf805b18620b61118c240814ece8ee1cf6252540380764e7e66b9` |



Minimal [nvidia-device-plugin](https://github.com/NVIDIA/k8s-device-plugin) container image.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/nvidia-device-plugin
```

## Usage

Ensure your environment satisfies the [prerequisites](https://github.com/NVIDIA/k8s-device-plugin#prerequisites).

Jump to [Quick Start](https://github.com/NVIDIA/k8s-device-plugin#quick-start) to learn more.

To test:

```shell
$ docker run --rm cgr.dev/chainguard/nvidia-device-plugin --help

NAME:
   NVIDIA Device Plugin - NVIDIA device plugin for Kubernetes

USAGE:
   nvidia-device-plugin [global options] command [command options] [arguments...]

VERSION:
   v0.14.0
commit: e6c111aff19eab995e8d0f4345169e8c310d2f9c

COMMANDS:
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --mig-strategy value           the desired strategy for exposing MIG devices on GPUs that support it:
                                    [none | single | mixed] (default: "none") [$MIG_STRATEGY]
   --fail-on-init-error           fail the plugin if an error is encountered during initialization, otherwise block indefinitely (default: true) [$FAIL_ON_INIT_ERROR]
   --nvidia-driver-root value     the root path for the NVIDIA driver installation (typical values are '/' or '/run/nvidia/driver') (default: "/") [$NVIDIA_DRIVER_ROOT]
   --pass-device-specs            pass the list of DeviceSpecs to the kubelet on Allocate() (default: false) [$PASS_DEVICE_SPECS]
   --device-list-strategy value   the desired strategy for passing the device list to the underlying runtime:
                                    [envvar | volume-mounts | cdi-annotations] (default: "envvar")  (accepts multiple inputs) [$DEVICE_LIST_STRATEGY]
   --device-id-strategy value     the desired strategy for passing device IDs to the underlying runtime:
                                    [uuid | index] (default: "uuid") [$DEVICE_ID_STRATEGY]
   --gds-enabled                  ensure that containers are started with NVIDIA_GDS=enabled (default: false) [$GDS_ENABLED]
   --mofed-enabled                ensure that containers are started with NVIDIA_MOFED=enabled (default: false) [$MOFED_ENABLED]
   --config-file value            the path to a config file as an alternative to command line options or environment variables [$CONFIG_FILE]
   --cdi-annotation-prefix value  the prefix to use for CDI container annotation keys (default: "cdi.k8s.io/") [$CDI_ANNOTATION_PREFIX]
   --nvidia-ctk-path value        the path to use for the nvidia-ctk in the generated CDI specification (default: "/usr/bin/nvidia-ctk") [$NVIDIA_CTK_PATH]
   --container-driver-root value  the path where the NVIDIA driver root is mounted in the container; used for generating CDI specifications (default: "/driver-root") [$CONTAINER_DRIVER_ROOT]
   --help, -h                     show help (default: false)
   --version, -v                  print the version (default: false)
```

To use the Chainguard Images variant, override the values below in your `values.yaml` to use with [Helm](https://github.com/NVIDIA/k8s-device-plugin#deployment-via-helm):

```yaml
image:
  repository: cgr.dev/chainguard/nvidia-device-plugin
  tag: latest
```

