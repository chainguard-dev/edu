---
title: "Image Overview: pytorch-cuda12"
linktitle: "pytorch-cuda12"
type: "article"
layout: "single"
description: "Overview: pytorch-cuda12 Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-06-11 00:42:18
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/pytorch-cuda12/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/pytorch-cuda12/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/pytorch-cuda12/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/pytorch-cuda12/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal, [wolfi](https://github.com/wolfi-dev)-based image for pytorch, a Python package that provides two high-level features: Tensor computation with strong GPU acceleration and Deep neural networks built on a tape-based autograd system.

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/pytorch-cuda12:latest
```


<!--body:start-->

## Running pytorch-cuda12

PyTorch has some prerequisites which need to be configured in the environment
prior to running with GPUs. For examples, please refer to [TESTING.md](https://github.com/chainguard-images/images/blob/main/images/pytorch-cuda12/TESTING.md).

Additionally, please refer to the [upstream documentation](https://github.com/pytorch/pytorch)
for more information on configuring and using PyTorch.

Assuming the environment prerequisites have been met, below demonstrates how
to launch the container:

```bash
docker run --rm -i -t \
    --privileged \
    --gpus all \
    cgr.dev/chainguard/pytorch:latest
```

## Testing GPU Access

If your environment has connected GPUs, you can check that PyTorch has access with the following:

```bash
docker run --rm -it --gpus all cgr.dev/chainguard/pytorch-cuda12:latest
bash-5.2$ python
Python 3.11.9 (main, Apr  2 2024, 15:40:32) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True
>>> torch.cuda.device_count()
1
>>> torch.cuda.get_device_name(0)
'Tesla V100-SXM2-16GB'
```

## Testing PyTorch

As a quick intro, we will use PyTorch to create a very simple deep learning model with two linear layers and an activation function. We’ll create an instance of it and ask it to report on its parameters. Running the below will fetch a [model_builder.py](https://github.com/chainguard-images/images/blob/main/images/pytorch-cuda12/model_builder.py) script from the Chainguard Images repository, place it in a folder on your host machine, and run the script in a pytorch-cuda12 container from a volume.

```bash
mkdir pytorch-test &&\
 curl https://raw.githubusercontent.com/chainguard-images/images/main/images/pytorch-cuda12/model_builder.py > pytorch-test/model_builder.py &&\
 docker run --rm -it -v "$PWD/pytorch-test:/tmp/pytorch-test" --gpus all cgr.dev/chainguard/pytorch-cuda12:latest -c "python /tmp/pytorch-test/model_builder.py"
```

You may also consider running this [quickstart script](https://github.com/chainguard-images/images/blob/main/images/pytorch-cuda12/tests/quickstart.py) based on the [official PyTorch quickstart tutorial](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) using the same approach as above.

### Using Helm charts

As a place to get started, you may also use this Helm chart to get PyTorch running
```bash
  helm install pytorch \
  --namespace pytorch-space --create-namespace  \
  --set image.registry="cgr.dev" \
  --set image.repository="chainguard/pytorch-cuda12" \
  --set image.tag=latest \
  --set containerSecurityContext.runAsUser=0 \
  --set containerSecurityContext.runAsNonRoot=false \
  --set containerSecurityContext.allowPrivilegeEscalation=true \
  --wait oci://registry-1.docker.io/bitnamicharts/pytorch
```
<!--body:end-->

