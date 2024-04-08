---
title: "Image Overview: argocd-extension-installer"
linktitle: "argocd-extension-installer"
type: "article"
layout: "single"
description: "Overview: argocd-extension-installer Chainguard Image"
date: 2024-04-08 00:38:35
lastmod: 2024-04-08 00:38:35
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/argocd-extension-installer/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd-extension-installer/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/argocd-extension-installer/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd-extension-installer/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Install Argo CD extensions using init-containers
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/argocd-extension-installer:latest
```
<!--getting:end-->

<!--body:start-->

## Usage

To get more detail about how to use this installer, please refer to the [Install UI Extensions](https://github.com/argoproj-labs/argocd-extension-metrics#install-ui-extension).


The yaml file below is an example of how to define a kustomize patch to install this UI extension:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: argocd-server
spec:
  template:
    spec:
      initContainers:
        - name: extension-metrics
          image: cgr.dev/chainguard/argocd-extension-installer:latest
          env:
          - name: EXTENSION_URL
            value: https://github.com/argoproj-labs/argocd-extension-metrics/releases/download/v1.0.0/extension.tar.gz
          - name: EXTENSION_CHECKSUM_URL
            value: https://github.com/argoproj-labs/argocd-extension-metrics/releases/download/v1.0.0/extension_checksums.txt
          volumeMounts:
            - name: extensions
              mountPath: /tmp/extensions/
          securityContext:
            runAsUser: 1000
            allowPrivilegeEscalation: false
      containers:
        - name: argocd-server
          volumeMounts:
            - name: extensions
              mountPath: /tmp/extensions/
      volumes:
        - name: extensions
          emptyDir: {}

```

or you can use the following settings while installing the ArgoCD server through Helm:

```yaml
...
  ## Argo CD extensions
  ## This function in tech preview stage, do expect instability or breaking changes in newer versions.
  ## Ref: https://github.com/argoproj-labs/argocd-extension-installer
  ## When you enable extensions, you need to configure RBAC of logged in Argo CD user.
  ## Ref: https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/#the-extensions-resource
  extensions:
    # -- Enable support for Argo CD extensions
    enabled: false

    ## Argo CD extension installer image
    image:
      # -- Repository to use for extension installer image
      repository: "quay.io/argoprojlabs/argocd-extension-installer"
      # -- Tag to use for extension installer image
      tag: "v0.0.1"
      # -- Image pull policy for extensions
      # @default -- `""` (defaults to global.image.imagePullPolicy)
      imagePullPolicy: ""

    # -- Extensions for Argo CD
    # @default -- `[]` (See [values.yaml])
    ## Ref: https://github.com/argoproj-labs/argocd-extension-metrics#install-ui-extension
    extensionList: []
    #  - name: extension-metrics
    #    env:
    #      - name: EXTENSION_URL
    #        value: https://github.com/argoproj-labs/argocd-extension-metrics/releases/download/v1.0.0/extension.tar.gz
    #      - name: EXTENSION_CHECKSUM_URL
    #     
...
```

<!--body:end-->

