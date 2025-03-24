---
title: "Getting Started with the Python Chainguard Image"
type: "article"
linktitle: "Python"
aliases: 
- /chainguard/chainguard-images/getting-started/getting-started-python
description: "Tutorial on the distroless Python Chainguard Image"
date: 2023-02-28T11:07:52+02:00
lastmod: 2025-02-21T13:46:53+00:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 055
toc: true
---

The Python images based on Wolfi and maintained by Chainguard provide distroless images that are suitable for building and running Python workloads.

Chainguard offers both a minimal runtime image containing just Python, and a development image that contains a package manager and a shell. Because Python applications typically require the installation of third-party dependencies via the Python package installer pip, you may need to implement a [multi-stage Docker build](https://docs.docker.com/build/building/multi-stage/) that uses the Python `-dev` image to set up the application.

In this guide, we'll cover two examples to showcase Python container images based on Wolfi as a runtime. In the first, we'll use the minimal image containing just Python (which has access to the [Python standard library](https://docs.python.org/3/library/)), and in the second we'll demonstrate a multi-stage build.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Example 1 — Minimal Python Chainguard Image

In this example, we'll build and run a distroless Python Chainguard Image in a single-stage build process. We'll first make a demonstration app and then build and run it.

### Step 1: Setting up a Demo Application

We'll start by creating a basic command-line Python application to serve as a demo. This app will generate random octopus facts based on a list in a text file. This app will use the `random` module from the Python standard library.

First, create a directory for your app. You can use any meaningful name and path for you, our example will use `octo-facts/`.

```shell
mkdir ~/octo-facts/ && cd $_
```

Create a new file to serve as the application entry point. We’ll use `main.py`. You can edit this file in whatever code editor you would like. We'll use Nano as an example.

```shell
nano main.py
```

The following Python script defines a light CLI app that takes in a text file, `octo-facts.txt`, and returns a random line from that file.

```python
'''Import random module to implement random.choice() function'''
import random


def random_line(text):
    '''Opens and reads lines of a UTF-8 encoded file, returning a random line'''
    with open(text, 'r', encoding='UTF-8') as file:
        line = file.readlines()
        return random.choice(line)

def main():
    '''Prints random line from facts.txt; verify your path'''
    print(random_line('facts.txt'))

if __name__ == "__main__":
    main()

```

Copy this code to your `main.py` script, save and close the file.

Next, pull down the `facts.txt` file with `curl`. [Inspect the URL](https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/python/octo-facts/facts.txt) before downloading it to ensure it is safe to do so. Make sure you are still in the same directory where your `main.py` script is.

```shell
curl -O https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/python/octo-facts/facts.txt
```

At this point, you can run the script and be sure you are satisfied with the functionality. It is recommended that you use a Python programming environment. Ensure whether you will be using the `python` or `python3` command.

```shell
python main.py
```

You should receive the output of a randomized octopus fact.

```
The wolfi octopus was discovered in 1913.
```

The demo application is now ready. In the next step, you’ll create a Dockerfile to run your app.

### Step 2: Creating the Dockerfile

For this single-stage build, we'll only use one `FROM` line in our Dockerfile. Our resulting image will be based on the distroless Python Wolfi image, which means it doesn’t come with a package manager or even a shell.

We'll begin by creating a Dockerfile. Again, you can use any code editor of your choice, we'll use Nano for demonstration purposes.

```shell
nano Dockerfile
```

The following Dockerfile will:

1. Start a build stage based on the `python:latest` image;
2. Declare the working directory;
3. Copy the script and the text file that's being read;
4. Set up the application as entry point for this image.

```Dockerfile
FROM cgr.dev/chainguard/python:latest

WORKDIR /octo-facts

COPY main.py facts.txt ./

ENTRYPOINT [ "python", "/octo-facts/main.py" ]
```

Save the file when you're finished.

You can now build the image. If you receive an error, try again with `sudo`.

```shell
docker build . --pull -t octo-facts
```

Once the build is finished, run the image.

```shell
docker run --rm octo-facts
```

And you should get output similar to what you got before, with a random octopus fact.

```
Octopuses can breathe and see through their skin.
```

You have successfully completed the single-stage Python Chainguard Image. At this point, you can continue to the [multi-stage example](#example-2-multi-stage-build-for-python-chainguard-image) or [advanced usage](#advanced-usage).

## Example 2 — Multi-Stage Build for Python Chainguard Image

In this example, we'll build and run a multi-stage Python Chainguard Image. We'll have a build image
that includes pip and a shell before creating a final distroless image without these development
tools for production.

### Step 1: Setting up a Demo Application

We'll start by creating a Python application that will take in an image file and convert it to ANSI escape sequences on the CLI to render an image.

To begin, create a directory for your app. You can use any meaningful name and path that resonates with you, our example will use `linky/`.

```shell
mkdir ~/linky/ && cd $_
```

We'll first write out the requirements for our app in a new file, for example we named our file `requirements.txt`. You can edit this file in your preferred code editor, in our case we will use Nano.

```shell
nano requirements.txt
```

We'll use version 68.2.2 of Python [setuptools](https://pypi.org/project/setuptools/) and also install [climage](https://pypi.org/project/climage/). We need to use a slightly older version of setuptools for compatibility with climage. Add the following text to the file:

```shell
setuptools==70.0.0
climage==0.2.0
```

Save the file and we will next create a new file with our python code called `linky.py`. You can edit this file in whatever code editor you would like. We’ll use Nano as an example.

```shell
nano linky.py
```

Add the following Python code which defines a CLI app that takes in an image file, `linky.png`, and
prints a representation of that file to the terminal:

```python
'''import climage module to display images on terminal'''
from climage import convert


def main():
    '''Take in PNG and output as ANSI to terminal'''
    output = convert('linky.png', is_unicode=True)
    print(output)

if __name__ == "__main__":
    main()
```

Next, pull down the `linky.png` image file with `curl`. [Inspect the URL](https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/python/linky/linky.png) before downloading it to ensure it is safe to do so. Make sure you are still in the same directory where your `linky.py` script is.

```shell
curl -O https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/python/linky/linky.png
```

If you have python and pip installed in your local environment, you can now install the dependencies with `pip` and run our program. Don't worry if you don't have python installed, you can simply skip this step and move onto the Dockerfile.

```shell
pip install -r requirements.txt
python linky.py
```

You'll receive a representation of the Chainguard Linky logo on the command line. With your demo application ready, you're ready to move onto the container stage.

### Step 2: Creating the Dockerfile

To make sure our final image is distroless while still being able to install dependencies with pip,
our build will consist of two stages: first, we’ll build the application using the
`python:latest-dev` image variant, a Wolfi-based image that includes pip and other useful tools for
development. Then, we’ll create a separate stage for the final image. The resulting image will be
based on the distroless Python Wolfi image, which means it doesn’t come with pip or even a shell.

Begin by editing a Dockerfile, with Nano for instance.

```shell
nano Dockerfile
```

The following Dockerfile will:

1. Start a new build stage based on the `python:latest-dev` image and call it `builder`;
2. Create a new virtual environment to cleanly hold the application's dependencies;
2. Copy `requirements.txt` from the current directory to the `/linky` location in the container;
3. Run `pip install --no-cache-dir -r requirements.txt` to install dependencies;
4. Start a new build stage based on the `python:latest` image;
5. Copy the dependencies in the virtual environment from the builder stage, and the source code from
   the current directory;
6. Set up the application as the entry point for this image.

Copy this configuration to your own Dockerfile:

```Dockerfile
FROM cgr.dev/chainguard/python:latest-dev AS builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/linky/venv/bin:$PATH"

WORKDIR /linky

RUN python -m venv /linky/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest

WORKDIR /linky

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

COPY linky.py linky.png ./
COPY --from=builder /linky/venv /venv

ENTRYPOINT [ "python", "/linky/linky.py" ]
```

Save the file when you’re finished.

You can now build the image. If you receive a permission error, try running under `sudo`.

```shell
docker build . --pull -t linky 
```

Once the build is finished, run the image with:

```shell
docker run --rm linky
```

And you should get output similar to what you got before, with a printed Linky on the command line.

## Advanced Usage

{{< blurb/images-advanced image="Python" >}}
