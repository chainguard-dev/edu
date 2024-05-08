---
title: "Getting Started with the NVIDIA NeMo Chainguard Image"
type: "article"
linktitle: "NeMo"
aliases: 
- /chainguard/chainguard-images/getting-started/getting-started-nemo
description: "Get started with the Chainguard Image for NVIDIA's NeMo framework for generative deep learning"
date: 2024-04-25:08:00+02:00
lastmod: 2024-04-25:08:00+00:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 612
toc: true
---

[NVIDIA NeMo](https://github.com/NVIDIA/NeMo) is a deep learning framework for building conversational AI models, providing standalone module collections for Automatic Speech Recognition (ASR), Natural Language Processing (NLP), and Text-to-Speech (TTS) tasks. The [NeMo Chainguard Image](/chainguard/chainguard-images/reference/nemo/) provides a comparatively lightweight NeMo environment with low to no CVEs, making it ideal for both training and production inference. The NeMo Chainguard Image is designed to work with the [CUDA 12](https://developer.nvidia.com/about-cuda) parallel computing platform, and is suited to training and inference tasks that take advantage of connected GPU.

{{< details "What is Deep Learning?" >}}
{{< blurb/deep-learning >}}
{{< /details >}}

In this getting started guide, we will use the NeMo Chainguard Image to generate speech from plain text using models provided by NeMo's text-to-speech (TTS) and natural language processing (NLP) collections. In doing so, we'll compare the security and footprint of the NeMo Chainguard Image to the official runtime image distributed by NVIDIA and consider further approaches and resources for applying the NeMo Chainguard Image to additional tasks in conversational AI.

This guide is primarily designed for use in an environment with access to one or more NVIDIA GPUs. However, NVIDIA NeMo is built on [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/), which supports a wide variety of [accelerators](https://pytorch-lightning.readthedocs.io/en/1.1.8/accelerators.html), or interfaces to categories of processing units (CPU, GPU, TPU) clustering mechanisms such as [Distributed Data Parallel](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html). Some consideration will be given to alternative computing environments such as CPU in this tutorial.

## Testing Access to GPUs

In our first step, we'll run the NeMo Chainguard Image interactively and determine whether the environment has access to connected GPUs.

If Docker Engine (or Docker Desktop) is not already installed, follow the [instructions for installing Docker Engine on your host machine](https://docs.docker.com/engine/install/). 

Run the below command to pull the image, run it with GPU access, and start a Python interpreter inside the running container.

```bash
docker run -it --rm \
  --gpus all \
  --shm-size=8g \
  --ulimit memlock=-1 \
  --ulimit stack=67108864 \
  cgr.dev/chainguard/nemo:latest
```

These options allow access to connected GPU, allocate more shared memory to the container, and put an upper bound on container memory use. 

Running the above for the first time may take a few minutes to pull the NeMo Chainguard Image, currently 4.05 GB. Once the image runs, you will be interacting with a bash shell in the running container. Enter the following commands at the prompt to check the availability of your GPU.

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
XXX CPU NOTE?

Once you've determined that your environment has access to CUDA and connected GPUs, exit the container by typing `Control-d` or by typing `exit()` and pressing `Enter`. You should be returned to the prompt of your host machine.

## NeMo Overview

NeMo is a generative AI toolkit and framework with a focus on conversational AI tasks such as NLP, ASR, and TTS, as well as large language models (LLM) and multimodal (MM) models. NeMo uses a system of [neural modules](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/neural_modules.html), an abstraction over a variety of common elements in model training and inference such as encoders, decoders, loss functions, layers, or models. NeMo also provides [collections of modules](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/collections.html) targeting specific areas of concern in conversational and generative AI, such as LLMs, speech AI / NLP, and TTS. 

NeMo is built on [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/) a high-level interface to PyTorch with a focus on scalability, and uses the [Hydra](https://hydra.cc/) library for configuration management.

Since NeMo is a framework with many collections of modules suitable for a whide variety of projects, we've chosen an example task, generative text to speech, requiring the use of two TTS modules. This is an appropriate example of a task that might be run as part of a larger production application.

## Text to Speech (TTS) Example

In this section, we'll run a script that uses the NeMo Chainguard Image to:

- Take a message in plain text
- Transform it into a set of phonemes
- Generate a spectrogram (waveform representation) using a NeMo-provided spectrogram model
- Transform the spectrogram values into audio using a NeMo-provided vocoder (human voice) model
- Write the resulting audio to a .wav file at a set rate

First, let's create a folder to work in on your host machine:

```bash
mkdir -p ~/nemo-tts && cd ~/nemo-tts
```

Next, let's download our [tts.py](https://github.com/chainguard-dev/nemo-examples/blob/main/tts.py) script:

```bash
curl https://raw.githubusercontent.com/chainguard-dev/nemo-examples/main/tts.py > tts.py
```

You should now be in a working directory with `tts.py`.

```bash
$ ls
tts.py
```

We'll be mounting this folder in our container as a volume, which will allow us to both pass in our script and extract our output.

We'll now run the script in our NeMo Chainguard Image. 

```bash
docker run -it --rm \
  --gpus all \
  --user root \
  --shm-size=8g \
  --ulimit memlock=-1 \
 --ulimit stack=67108864 \
  -v $PWD:/home/nonroot/nemo-test \
  cgr.dev/chainguard/nemo:latest \
  -c "python /home/nonroot/nemo-test/tts.py"
```

If your host machine does not hav attached GPUs and you'd like to run the above on your CPU, omit the `  --gpus all \` line.

Note that NeMo collections are large, and initial imports can take up to a minute depending on your environment. The script may appear to hang during that time.

After imports are complete, you should see a large amount of output as NeMo pulls models and works through the steps in the script.


{{< audio src="tts-example.wav" caption="Output from the TTS script" >}}


