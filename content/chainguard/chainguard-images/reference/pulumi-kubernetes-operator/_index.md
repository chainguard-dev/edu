---
title: "Image Overview: pulumi-kubernetes-operator"
linktitle: "pulumi-kubernetes-operator"
type: "article"
layout: "single"
description: "Overview: pulumi-kubernetes-operator Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/pulumi-kubernetes-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/pulumi-kubernetes-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/pulumi-kubernetes-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/pulumi-kubernetes-operator/provenance_info/" >}}
{{</ tabs >}}

Minimal Pulumi Kubernetes Operator Image

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/pulumi-kubernetes-operator:latest
```

## Usage

See https://github.com/pulumi/pulumi-kubernetes-operator#using-kubectl

Install the CRDs:
```
VERSION="1.11.5"
curl -LO "https://github.com/pulumi/pulumi-kubernetes-operator/archive/refs/tags/v${VERSION}.tar.gz"
tar -xvf "v${VERSION}.tar.gz"
kubectl apply -f pulumi-kubernetes-operator-${VERSION}/deploy/crds/
```

Inject the Chainguard image into the install
```
IMAGE_NAME="cgr.dev/chainguard-private/pulumi-kubernetes-operator:latest"
cat pulumi-kubernetes-operator-${VERSION}/deploy/yaml/operator.yaml | \
  yq ".spec.template.spec.containers[0].image = \"${IMAGE_NAME}\"" \
  > pulumi-kubernetes-operator-${VERSION}/deploy/yaml/operator.yaml.tmp && \
  mv pulumi-kubernetes-operator-${VERSION}/deploy/yaml/operator.yaml.tmp \
  pulumi-kubernetes-operator-${VERSION}/deploy/yaml/operator.yaml
```

If you've loaded the image in yourself, modify the `imagePullPolicy`
as well to prevent 403 errors:
```
cat pulumi-kubernetes-operator-${VERSION}/deploy/yaml/operator.yaml | \
  yq ".spec.template.spec.containers[0].imagePullPolicy = \"IfNotPresent\"" \
  > pulumi-kubernetes-operator-${VERSION}/deploy/yaml/operator.yaml.tmp && \
  mv pulumi-kubernetes-operator-${VERSION}/deploy/yaml/operator.yaml.tmp \
  pulumi-kubernetes-operator-${VERSION}/deploy/yaml/operator.yaml
```

Deploy the operator:
```
kubectl apply -f pulumi-kubernetes-operator-${VERSION}/deploy/yaml
```

Create a Pulumi stack using
[one of our examples](https://github.com/chainguard-images/images/tree/main/images/pulumi/examples):
```
# Choose one of: "dotnet" "go" "java" "nodejs" "python" "yaml"
TEST_LANG="yaml"
STACK_NAME="smoketest-${TEST_LANG}-$(date +%s)"
kubectl apply -f - <<EOF
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: ${STACK_NAME}
spec:
  stack: ${STACK_NAME}
  projectRepo: https://github.com/chainguard-images/images
  repoDir: images/pulumi/examples/smoketest-${TEST_LANG}
  branch: refs/heads/main
  destroyOnFinalize: true
  backend: file://.
  envRefs:
    PULUMI_CONFIG_PASSPHRASE:
      type: Literal
      literal:
        value: abc123
  config:
    name: ${STACK_NAME}
EOF
```

Delete the stack:
```
kubectl delete stack "${STACK_NAME}"
```
