---
title: "Image Overview: timoni"
linktitle: "timoni"
type: "article"
layout: "single"
description: "Overview: timoni Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/timoni/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/timoni/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/timoni/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/timoni/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with `timoni` binary. `timoni` is a package manager for Kubernetes, powered by `cue` and inspired by `helm`.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/timoni:latest
```


<!--body:start-->
The image contains the `timoni`  binary and a few assorted runtime dependencies.

```
docker run cgr.dev/chainguard/timoni:latest
A package manager for Kubernetes powered by CUE.

Usage:
  timoni [command]

Available Commands:
  apply       Install or upgrade a module instance
  build       Build an instance from a module and print the resulting Kubernetes resources
  bundle      Commands for managing bundles
  completion  Generates completion scripts for various shells
  delete      Uninstall a module instance from the cluster
  help        Help about any command
  inspect     Commands for getting information about installed instances
  list        Prints a table of instances and their module version
  mod         Commands for managing modules
  status      Displays the current status of Kubernetes resources managed by an instance
  version     Print the client and API version information

Flags:
      --as string                      Username to impersonate for the operation. User could be a regular user or a service account in a namespace.
      --as-group stringArray           Group to impersonate for the operation, this flag can be repeated to specify multiple groups.
      --as-uid string                  UID to impersonate for the operation.
      --cache-dir string               Default cache directory (default "/home/nonroot/.kube/cache")
      --certificate-authority string   Path to a cert file for the certificate authority
      --client-certificate string      Path to a client certificate file for TLS
      --client-key string              Path to a client key file for TLS
      --cluster string                 The name of the kubeconfig cluster to use
      --context string                 The name of the kubeconfig context to use
      --disable-compression            If true, opt-out of response compression for all requests to the server
  -h, --help                           help for timoni
      --insecure-skip-tls-verify       If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure
      --kubeconfig string              Path to the kubeconfig file to use for CLI requests.
      --log-color                      Adds colorized output to the logs. (defaults to false when no tty)
      --log-pretty                     Adds timestamps to the logs. (default true)
  -n, --namespace string               The instance namespace. (default "default")
  -s, --server string                  The address and port of the Kubernetes API server
      --timeout duration               The length of time to wait before giving up on the current operation. (default 5m0s)
      --tls-server-name string         Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used
      --token string                   Bearer token for authentication to the API server
      --user string                    The name of the kubeconfig user to use
  -v, --version                        version for timoni

```
<!--body:end-->

