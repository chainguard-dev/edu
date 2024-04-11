---
title: "Image Overview: pulumi"
linktitle: "pulumi"
type: "article"
layout: "single"
description: "Overview: pulumi Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/pulumi/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/pulumi/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/pulumi/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/pulumi/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Pulumi Image
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/pulumi:latest
```


<!--body:start-->
## Usage

### Kubernetes Pod Example

In this directory, check the `examples/` folder.
You should find an example app for the following support Pulumi languages/runtimes:

- dotnet
- go
- java
- nodejs
- python
- yaml

This will show an example of using Pulumi SDKs to create an Nginx pod in
a kind cluster.

Try running these commands from this directory in the repo.

Set the desired language to the env var `TEST_LANG`:

```
export TEST_LANG=go
```

Start a kind cluster:

```
kind create cluster
```

Extract the kubeconfig, and modify it to use an internal IP:

```
KIND_IP="$(docker ps | grep 'control-plane' | awk '{print $1}' | xargs docker inspect | jq -r '.[0].NetworkSettings.Networks["kind"].IPAddress')"

mkdir .kube
kind get kubeconfig | yq '.clusters[].cluster.server = "https://'${KIND_IP}':6443"' \
    > ".kube/config"
```

Create a temporary Pulumi home directory, and do a local login:

```
mkdir .pulumi
docker run --rm --network kind \
    -w "/work/examples/smoketest-${TEST_LANG}" \
    -v "${PWD}:/work" \
    -e PULUMI_HOME=/work/.pulumi \
    cgr.dev/chainguard/pulumi:latest \
    login file://.
```

Decide a unique stack name:
```
export STACK_NAME="${TEST_LANG}-$(date +%s)"
```

Next, init a stack (for you decided language):

```
docker run --rm --network kind \
    -w "/work/examples/smoketest-${TEST_LANG}" \
    -v "${PWD}:/work" \
    -e PULUMI_HOME=/work/.pulumi \
    -e PULUMI_CONFIG_PASSPHRASE="${STACK_NAME}" \
    cgr.dev/chainguard/pulumi:latest \
    stack init --non-interactive --stack ${STACK_NAME}
```

Note: for some runtimes, you may need to install language-specific dependencies ahead of time.
Here is an example of preinstalling Node.js dpendencies using `npm install`:

```
docker run --rm -w /work/smoketest-${lang} \
    -v "${TMPDIR}:/work" \
    --entrypoint npm \
    cgr.dev/chainguard/pulumi:latest \
    install
```

Finally, create the stack:

```
docker run --rm --network kind \
    -w "/work/examples/smoketest-${TEST_LANG}" \
    -v "${PWD}:/work" \
    -e PULUMI_HOME=/work/.pulumi \
    -e PULUMI_CONFIG_PASSPHRASE="${STACK_NAME}" \
    -e KUBECONFIG=/work/.kube/config \
    cgr.dev/chainguard/pulumi:latest \
    up --yes --config name=${STACK_NAME}
```

You should notice a pod in the default namespace has been created:

```
$ kubectl get pods
NAME            READY   STATUS    RESTARTS   AGE
go-1683319492   1/1     Running   0          24s
```

To teardown the stack, run the following:
```
docker run --rm --network kind \
    -w "/work/examples/smoketest-${TEST_LANG}" \
    -v "${PWD}:/work" \
    -e PULUMI_HOME=/work/.pulumi \
    -e PULUMI_CONFIG_PASSPHRASE="${STACK_NAME}" \
    -e KUBECONFIG=/work/.kube/config \
    cgr.dev/chainguard/pulumi:latest \
    destroy --yes
```

Now check for pods, there should not be any:
```
$ kubectl get pods
No resources found in default namespace.
```
<!--body:end-->

