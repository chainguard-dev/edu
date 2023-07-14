---
title: "Image Overview: kubernetes-csi-livenessprobe"
type: "article"
description: "Overview: kubernetes-csi-livenessprobe Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-csi-livenessprobe](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-livenessprobe)

| Tag      | Last Updated | Digest                                                                    |
|----------|--------------|---------------------------------------------------------------------------|
| `latest` | July 11th    | `sha256:bd74e638ffe80dadfd016eeb77188af0768cf4e460f74bd819b8195009d3fb2e` |



## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-livenessprobe
```

## Run it

Generally speaking, the `kubernetes-csi-livenessprobe` is a low level Kubernetes component not meant to be managed directly. However, all the steps outlined in the [upstream repo](https://github.com/kubernetes-csi/livenessprobe) apply just as well to the Chainguard Image version.

## Test it

A simple smoke test is provided below that leverages `docker` to spin up the liveness probe attached to a csi driver and ensure basic functionality is met:

```bash
#!/usr/bin/env bash

set -o errexit -o nounset -o errtrace -o pipefail -x

if [[ "${IMAGE_NAME}" == "" ]]; then
	echo "Must set IMAGE_NAME environment variable. Exiting."
	exit 1
fi

UDS="/csi/csi.sock"
CSI_ENDPOINT="unix:/$UDS"

# Start hostpathplugin in the background
docker run -d --name csi-driver -v $(pwd)/csi:/csi quay.io/k8scsi/hostpathplugin:v1.6.0 --endpoint=$CSI_ENDPOINT -nodeid 1 --v=5
trap "docker rm -f csi-driver" EXIT

docker run -d --name probe -p 9808:9808 -v $(pwd)/csi:/csi "$IMAGE_NAME" --v=5 --csi-address=$UDS
trap "docker rm -f probe" EXIT

# Give time to CSI hostpathplugin and livenessprobe to initialize
sleep 3

# Requesting health
health=$(curl -I http://localhost:9808/healthz | grep HTTP | awk '{print $2}')
if [[ "x$health" != "x200" ]]; then
	echo "Health check failed, but it was not supposed to, exiting..."
	exit 1
fi

# Killing hostpathplugin
docker stop csi-driver
sleep 3

# Requesting health, should fail since hostpathplugin is gone
health=$(curl -I http://localhost:9808/healthz | grep HTTP | awk '{print $2}')
if [[ "x$health" != "x500" ]]; then
	echo "Health check did not detect driver failure, returned code: $health, exiting..."
	exit 1
fi

exit 0
```
