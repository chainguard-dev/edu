---
title: "Image Overview: aws-ebs-csi-driver"
linktitle: "aws-ebs-csi-driver"
type: "article"
layout: "single"
description: "Overview: aws-ebs-csi-driver Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-28 00:31:13
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/aws-ebs-csi-driver/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/aws-ebs-csi-driver/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aws-ebs-csi-driver/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-ebs-csi-driver/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal images for [aws-ebs-csi-driver](https://aws.amazon.com/ebs/).
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/aws-ebs-csi-driver:latest
```
<!--getting:end-->

<!--body:start-->
## Testing

Since this application requires AWS credentials to be set up, we should create the required permissions before deploying it.

To do that, you can follow up on the official documentation [here](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md#set-up-driver-permissions).

But for the sake of simplicity, we can create the Kubernetes secret resource called `aws-secret` with the proper options `key_id` and `access_key`:

```shell
kubectl create secret generic aws-secret \
    --namespace kube-system \
    --from-literal "key_id=${AWS_ACCESS_KEY_ID}" \
    --from-literal "access_key=${AWS_SECRET_ACCESS_KEY}"
```

There are several methods to deploy the driver, but we will use the `helm` method.

We should add the `aws-ebs-csi-driver` Helm repository to our repositories list:

```shell
helm repo add aws-ebs-csi-driver https://kubernetes-sigs.github.io/aws-ebs-csi-driver
helm repo update
```

Next, we can install the driver with the following command:

```shell
helm upgrade --install aws-ebs-csi-driver \
    --namespace kube-system \
    --set image.repository=cgr.dev/chainguard/aws-ebs-csi-driver \
    --set image.tag=latest \
    aws-ebs-csi-driver/aws-ebs-csi-driver
```

Once the driver has been deployed, verify the pods are running:

```shell
kubectl get pods -n kube-system -l app.kubernetes.io/name=aws-ebs-csi-driver
```
<!--body:end-->

