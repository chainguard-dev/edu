---
title: "Image Overview: aws-ebs-csi-driver"
type: "article"
description: "Overview: aws-ebs-csi-driver Chainguard Image"
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

[cgr.dev/chainguard/aws-ebs-csi-driver](https://github.com/chainguard-images/images/tree/main/images/aws-ebs-csi-driver)

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 7th | `sha256:4c74258f2a6ba3cd39a71b70352bde50c02d91bd0b8f0195b782b2b95ac18f4e` |
|  `latest`     | September 4th | `sha256:0093e0df6a2d3cbfb9fa802187b496e8d04cb62d9c6a6969151d7e3f165352d0` |



Minimal images for aws-ebs-csi-driver.

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/aws-ebs-csi-driver:latest
```

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

