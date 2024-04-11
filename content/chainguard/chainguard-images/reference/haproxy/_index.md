---
title: "Image Overview: haproxy"
linktitle: "haproxy"
type: "article"
layout: "single"
description: "Overview: haproxy Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/haproxy/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/haproxy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/haproxy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/haproxy/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal [haproxy](https://www.haproxy.org/) base image rebuilt every night from source.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/haproxy:latest
```


<!--body:start-->
## Usage

Similar to the `docker-library/haproxy` image, this image does not come with any default configuration.

Please refer to [upstream's excellent (and comprehensive) documentation](https://docs.haproxy.org/) on the subject of configuring HAProxy for your needs.

Let say you have a `haproxy.cfg` config file is current working directory. To test that configuration file, you can run the following command

```
docker run -it --rm -v "$(pwd):/etc/haproxy" --name haproxy-syntax-check cgr.dev/chainguard/haproxy haproxy -c -f /etc/haproxy/haproxy.cfg
```

In order for the container to work, you need to mount your custom `haproxy.cfg` file in the container. The following example runs HAProxy with a custom configuration file:

```
docker run -it --rm -v "$(pwd):/etc/haproxy" cgr.dev/chainguard/haproxy haproxy -f /etc/haproxy/haproxy.cfg
```

### Helm install

When installing in Kubernetes, `securityContexts` that drop `[ "ALL" ]` capabilities interfere with the `setcap` privileged `haproxy`. In order to support Kubernetes based installs which default to dropping `ALL` capabilities, the necessary modifications must be made to add back `NET_ADMIN` capabilities.

For example, in the `ha-redis` chart used by `argocd`, the `values.yaml` becomes:

```yaml
# values.yaml
haproxy:
  enabled: true
  containerSecurityContext:
    capabilities:
      add:
        - NET_BIND_SERVICE
```
<!--body:end-->

