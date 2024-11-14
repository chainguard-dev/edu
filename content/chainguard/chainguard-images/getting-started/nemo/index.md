---
title: "Getting Started with the NeMo Chainguard Image"
type: "article"
linktitle: "NeMo"
aliases:
- /chainguard/chainguard-images/getting-started/nemo
description: "Get started with the NeMo Chainguard Image for generative deep learning"
date: 2024-05-16T08:00:00+02:00
lastmod: 2024-05-16T08:00:00+02:00
tags: ["CHAINGUARD IMAGES", "PRODUCTS"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 030
toc: true
---

[NeMo](https://github.com/NVIDIA/NeMo) is a deep learning framework for building conversational AI models that provides standalone module collections for Automatic Speech Recognition (ASR), Natural Language Processing (NLP), and Text-to-Speech (TTS) tasks. The [NeMo Chainguard Image](https://images.chainguard.dev/directory/image/nemo/overview) is a comparatively lightweight NeMo environment with low to no CVEs, making it ideal for both training and production inference. The NeMo Chainguard Image is designed to work with the [CUDA 12](https://developer.nvidia.com/about-cuda) parallel computing platform, and is suited to workloads that take advantage of connected GPUs.

{{< details "What is Deep Learning?" >}}
{{< blurb/deep-learning >}}
{{< /details >}}

In this getting started guide, we will use the NeMo Chainguard Image to generate speech from plain text using models provided by NeMo's text-to-speech (TTS) and natural language processing (NLP) collections. In doing so, we'll compare the security and footprint of the NeMo Chainguard Image to the official runtime image and consider further approaches and resources for applying the NeMo Chainguard Image to additional tasks in conversational AI.

This guide is primarily designed for use in an environment with access to one or more NVIDIA GPUs. However, NeMo is built on [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/), which supports a wide variety of [accelerators](https://pytorch-lightning.readthedocs.io/en/1.1.8/accelerators.html), or interfaces to categories of processing units (CPU, GPU, TPU) or high-level clustering mechanisms such as [Distributed Data Parallel](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html). Some consideration will be given to alternative computing environments such as CPU in this tutorial.

> **Note**: In November 2024, after this article was first written, Chainguard [made changes to its free tier of Developer Imgages](https://www.chainguard.dev/unchained/changes-to-chainguard-images-developer-tier). In order to access the NeMo image used in this guide, you will need to be part of an organization that has access to it. For a full list of Developer Images that will remain in Chainguard's free tier, please refer to [this support page](https://support.chainguard.dev/hc/en-us/articles/28452542784667-Customer-Notice-Free-Image-Tier-Changes).

## Prerequisites

If Docker Engine (or Docker Desktop) is not already installed, follow the [instructions for installing Docker Engine on your host machine](https://docs.docker.com/engine/install/).

To take advantage of connected GPUs, you'll need to install CUDA Toolkit on your host machine.

{{< details "Installing CUDA Toolkit" >}}
{{< blurb/cuda >}}
{{< /details >}}

This tutorial can be followed without connected GPUs or CUDA Toolkit. To run commands in this tutorial on CPU, omit the `  --gpus all` flag when executing container commands. Keep in mind that some functionality within NeMo (such as training models) will take significantly longer on CPU.

## Testing Access to GPUs

We'll start by running the NeMo Chainguard Image interactively and determine whether the environment has access to connected GPUs.

Use the following command to pull the image, run it with GPU access, and start a Python interpreter inside the running container.

```bash
docker run -it --rm \
  --gpus all \
  --shm-size=8g \
  --ulimit memlock=-1 \
  --ulimit stack=67108864 \
  cgr.dev/$ORGANIZATION/nemo:latest
```

> **Note**: Be aware that you will need to change `$ORGANIZATION` to reflect the name of your organization's repository within the Chainguard Registry.

These options allow access to all available GPUs, allocate a custom amount of shared memory (8 GB) to the container, and set an upper bound on container memory use.

Running this command for the first time may take a few minutes, since it will download  the NeMo Chainguard Image to your host machine. Once the image is pulled and the command runs successfully, you will be interacting with a bash shell in the running container. Enter the following commands at the prompt to check the availability of your GPU.

```
$ python
Python 3.11.9 (main, May  1 2024, 21:48:03) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from nemo.core import pytorch_lightning
>>> len(pytorch_lightning.accelerators.find_usable_cuda_devices())
1
```

The above output shows that one GPU is connected and available. Since PyTorch is also accessible within our NeMo Chainguard Image, you can also use it to access more granular information on CUDA and attached GPUs.

```python
>>> import torch
>>> torch.cuda.is_available()
True
>>> torch.cuda.get_device_name(0)
'Tesla V100-SXM2-16GB'
```

Once you've determined that your environment has access to CUDA and connected GPUs, exit the container by typing `Control-d` or by typing `exit()` and pressing `Enter`. You should be returned to the prompt of your host machine.

## NeMo Overview

NeMo is a generative AI toolkit and framework with a focus on conversational AI tasks such as NLP, ASR, and TTS, as well as large language models (LLM) and multimodal (MM) models. NeMo uses a system of [neural modules](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/neural_modules.html), an abstraction over a variety of common elements in model training and inference such as encoders, decoders, loss functions, layers, or models. NeMo also provides [collections of modules](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/collections.html) targeting specific areas of concern in conversational and generative AI, such as LLMs, speech AI / NLP, and TTS.

NeMo is built on [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/), a high-level interface to PyTorch with a focus on scalability, and uses the [Hydra](https://hydra.cc/) library for configuration management.

Since NeMo is a framework with many collections of modules suitable for a wide variety of projects, we've chosen an example task, generative text to speech, requiring the use of two TTS modules. This is an appropriate example of a task that might be run as part of a larger production application.

## Text to Speech (TTS) Example

In this section, we'll run a script that uses the NeMo Chainguard Image to:

- Start with a message in plain text
- Transform it into a set of phonemes
- Generate a spectrogram (waveform representation) using a NeMo-provided spectrogram model
- Transform the spectrogram values into audio using a NeMo-provided vocoder (human voice) model
- Write the resulting audio to a `.wav` file at a set rate

First, let's create a folder to work in on your host machine:

```bash
mkdir -p ~/nemo-tts && cd ~/nemo-tts
```

Next, let's download our [tts.py](https://github.com/chainguard-dev/nemo-examples/blob/main/tts.py) script:

```bash
curl https://raw.githubusercontent.com/chainguard-dev/nemo-examples/main/tts.py > tts.py
```

You should now be in a working directory containing only one file, `tts.py`.

We'll be mounting this folder in our container as a volume, which will allow us to both pass in our script and extract our output.

We'll now start a container based on our NeMo Chainguard Image, mount the current working directory containing our `tts.py` script inside the container as a volume, and run the script in the container:

```bash
docker run -it --rm \
  --gpus all \
  --user root \
  --shm-size=8g \
  --ulimit memlock=-1 \
 --ulimit stack=67108864 \
  -v $PWD:/home/nonroot/nemo-test \
  cgr.dev/$ORGANIZATION/nemo:latest \
 "/home/nonroot/nemo-test/tts.py"
```
Note that we ran the above script as root. This allows us to share the script and output `.wav` file between the host and container. Remember not to run your image as root in a production environment.

If your host machine does not have attached GPUs and you'd like to run the above on your CPU, omit the `  --gpus all \` line. The script tests for availability of the CUDA platform and sets the accelerator to CPU if CUDA is not detected, so the script will also function on CPU.

Since we're using pretrained models to perform text to speech, this example will only take a few minutes using a CPU only. However, other tasks such as model training and finetuning may take significantly longer without connected GPUs.

Note that NeMo collections are large, and initial imports can take up to a minute depending on your environment. The script may appear to hang during that time.

After imports are complete, you should see a large amount of output as NeMo pulls models and works through the steps in the script (tokenizing, generating a spectrogram, generating audio, and writing audio to disk). On completion, the script outputs a `test.wav` file. Because we mounted a volume, this file should now be present in the working directory of your host machine.

```bash
ls
```

```
test.wav  tts.py
```

The `test.wav` file should contain audio similar to this output:

{{< audio src="tts-example.wav" caption="Output from the TTS script" >}}

## Final Considerations and Next Steps

This section will consider next steps for applying the NeMo Chainguard Image to other tasks in conversational AI.

In the [tts.py](https://github.com/chainguard-dev/nemo-examples/blob/main/tts.py) script run above, we used two models provided by NeMo, both contained within the TTS collection.

- [Tacotron2 speech synthesis model](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/tts_en_tacotron2)
- [HiFi-GAN speech synthesis model](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/speechsynthesis_hifigan)

The former model allows us to convert plain text into a spectrogram, or a representation of a waveform. The second model generates audio from the spectrogram. Note that NVIDIA's model overview pages provide useful background information, tags, and sample code. You can search the [full NGC model catalog](https://catalog.ngc.nvidia.com/models?filters=&orderBy=weightPopularDESC&query=&page=&pageSize=) to find pretrained models for use with NeMo.

In this script, we used pretrained models to create the phonemes and audio output. These models can be finetuned with your own speech data to customize the results. NVIDIA hosts a [tutorial on finetuning TTS models with NeMo](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/tutorials/tts-finetune-nemo.html).

The following resources may give a starting point for further explorations with the NeMo Chainguard Image:

- NVIDIA provides a wide variety of [NeMo Tutorials](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/tutorials.html) that are a strong entry point for working with the framework to accomplish specific tasks.
- NVIDIA's [NeMo Playbooks](https://docs.nvidia.com/nemo-framework/user-guide/latest/playbooks/index.html) provide a basis for more advanced tasks and configurations and address running workloads on different platforms and orchestration tooling.
- The [NeMo Collections](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/collections.html) organizes reference documentation for NeMo collections and modules.
- The [NVIDIA NGC model catalog](https://catalog.ngc.nvidia.com/models?filters=&orderBy=weightPopularDESC&query=&page=&pageSize=) can be searched to find models suitable for specific tasks, and each model's overview page provides a useful reference with sample code.
- This [NVIDIA Conversational AI publications page](https://research.nvidia.com/labs/conv-ai/publications) collects papers that use the NeMo framework, showcasing cutting-edge generative deep learning using NeMo
