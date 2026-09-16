---
title: "Getting started with the Python Chainguard Container"
type: "article"
linktitle: "Python"
aliases:
- /chainguard/chainguard-images/getting-started/getting-started-python
- /chainguard/chainguard-images/getting-started/python/
- /chainguard/containers/getting-started/getting-started-python
- /chainguard/containers/getting-started/python/
description: "Learn how to use Chainguard's Python container images for secure Python applications with minimal CVEs, distroless design, and comprehensive supply chain security features"
date: 2023-02-28T11:07:52+02:00
lastmod: 2025-07-23T15:09:59+00:00
tags: ["Chainguard Containers"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 060
toc: true
---

Chainguard's Python container images provide a more secure foundation for Python applications through distroless design, containing significantly fewer CVEs compared to traditional Python images. These production-ready images are optimized for building and running Python workloads.

Two variants of Chainguard Python images are available: a minimal runtime image containing only Python and its standard library, and a `-dev` variant that includes pip and a shell for development purposes. Since most Python applications require third-party packages, the recommended approach is using a [multi-stage Docker build](https://docs.docker.com/build/building/multi-stage/) with the `-dev` image for dependency installation and the minimal image for runtime.

This guide covers two examples of Python container images based on Wolfi as a runtime. The first uses the minimal image containing just Python, which has access to the [Python standard library](https://docs.python.org/3/library/). The second demonstrates a multi-stage build.

{{< details "What is distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "What are multi-stage builds?" >}}
{{< blurb/multistage >}}
{{< /details >}}

{{< details "Chainguard Containers" >}}
{{< blurb/images >}}
{{< /details >}}

## Example 1 — Minimal Python Chainguard Container

In this example, you'll build and run a distroless Python Chainguard Container in a single-stage build process. You'll first make a demonstration app, then build and run it.

### Step 1: Setting up a demo application

Start by creating a basic command-line Python application to serve as a demo. This app generates random octopus facts based on a list in a text file, using the `random` module from the Python standard library.

First, create a directory for your app. You can use any meaningful name and path; this example uses `octo-facts/`.

```shell
mkdir ~/octo-facts/ && cd $_
```

Create a new file named `main.py` to serve as the application entry point. The following Python script defines a light CLI app that takes in a text file, `facts.txt`, and returns a random line from that file.

```shell
cat > main.py <<'EOF'
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
EOF
```

Next, pull down the `facts.txt` file with `curl`. [Inspect the URL](https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/python/octo-facts/facts.txt) before downloading it to ensure it is safe to do so. Make sure you are still in the same directory where your `main.py` script is.

```shell
curl -O https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/python/octo-facts/facts.txt
```

At this point, you can run the script and be sure you are satisfied with the functionality. We recommend that you use a Python programming environment. Determine whether your system uses the `python` or `python3` command.

```shell
python main.py
```

You should receive the output of a randomized octopus fact.

```
The wolfi octopus was discovered in 1913.
```

The demo application is now ready. In the next step, you’ll create a Dockerfile to run your app.

### Step 2: Creating the Dockerfile

For this single-stage build, you'll only need one `FROM` line in your Dockerfile. The resulting container is based on the distroless Python Wolfi container image, which means it doesn’t come with a package manager or even a shell.

Begin by creating a Dockerfile. The following Dockerfile:

1. Starts a build stage based on the `python:latest` image;
2. Declares the working directory;
3. Copies the script and the text file that's being read;
4. Sets up the application as entry point for this container.

```shell
cat > Dockerfile <<'EOF'
FROM cgr.dev/chainguard/python:latest

WORKDIR /octo-facts

COPY main.py facts.txt ./

ENTRYPOINT [ "python", "/octo-facts/main.py" ]
EOF
```

You can now build the container image. If you receive an error, try again with `sudo`.

```shell
docker build . --pull -t octo-facts
```

Once the build is finished, run the container.

```shell
docker run --rm octo-facts
```

And you should get output similar to what you got before, with a random octopus fact.

```
Octopuses can breathe and see through their skin.
```

You have successfully completed the single-stage Python Chainguard Container. At this point, you can continue to the [multi-stage example](#example-2-multi-stage-build-for-python-chainguard-container) or [advanced usage](#advanced-usage).

## Example 2 — Multi-stage build for Python Chainguard Container

In this example, you'll build and run a multi-stage Python Chainguard Container. The build image
includes pip and a shell, and the final distroless image leaves out these development
tools for production.

### Step 1: Setting up a demo application

Start by creating a Python application that takes in an image file and converts it to ANSI escape sequences on the CLI to render an image.

To begin, create a directory for your app. You can use any meaningful name and path that resonates with you; this example uses `linky/`.

```shell
mkdir ~/linky/ && cd $_
```

First, write out the requirements for your app in a file named `requirements.txt`. This installs version 0.2.2 of [climage](https://pypi.org/project/climage/), which converts images into ANSI escape sequences:

```shell
cat > requirements.txt <<'EOF'
climage==0.2.2
EOF
```

Create a file named `linky.py` to hold your Python code. It defines a CLI app that takes in an
image file, `linky.png`, and prints a representation of that file to the terminal:

```shell
cat > linky.py <<'EOF'
'''import climage module to display images on terminal'''
from climage import convert


def main():
    '''Take in PNG and output as ANSI to terminal'''
    output = convert('linky.png', is_unicode=True)
    print(output)

if __name__ == "__main__":
    main()
EOF
```

Next, pull down the `linky.png` image file with `curl`. [Inspect the URL](https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/python/linky/linky.png) before downloading it to ensure it is safe to do so. Make sure you are still in the same directory where your `linky.py` script is.

```shell
curl -O https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/main/python/linky/linky.png
```

With your demo application ready, you can move on to the container stage.

### Step 2: Creating the Dockerfile

To keep the final container distroless while still being able to install dependencies with pip,
the build consists of two stages: first, you’ll build the application using the
`python:latest-dev` image variant, a Wolfi-based image that includes pip and other useful tools for
development. Then, you’ll create a separate stage for the final image. The resulting container is
based on the distroless Python Wolfi container image, which means it doesn’t come with pip or even a shell.

Begin by creating a Dockerfile. The following Dockerfile:

1. Starts a new build stage based on the `python:latest-dev` container image and calls it `builder`;
2. Creates a new virtual environment to cleanly hold the application's dependencies, using
   `--without-pip` to keep pip out of the environment and therefore out of the final image;
3. Copies `requirements.txt` from the current directory to the `/linky` location in the container;
4. Runs `pip --python /linky/venv/bin/python install --no-cache-dir -r requirements.txt` to install
   dependencies, where `--python` points the builder's own pip at the virtual environment;
5. Starts a new build stage based on the `python:latest` image;
6. Copies the dependencies in the virtual environment from the builder stage, and the source code from
   the current directory;
7. Sets up the application as the entry point for this container.

Write this configuration to your own Dockerfile:

```shell
cat > Dockerfile <<'EOF'
FROM cgr.dev/chainguard/python:latest-dev AS builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/linky/venv/bin:$PATH"

WORKDIR /linky

RUN python -m venv --without-pip /linky/venv
COPY requirements.txt .

RUN pip --python /linky/venv/bin/python install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest

WORKDIR /linky

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

COPY linky.py linky.png ./
COPY --from=builder /linky/venv /venv

ENTRYPOINT [ "python", "/linky/linky.py" ]
EOF
```

You can now build the container image. If you receive a permission error, try running under `sudo`.

```shell
docker build . --pull -t linky
```

Once the build is finished, run the image with:

```shell
docker run --rm linky
```

And you should get output similar to what you got before, with a printed Linky on the command line.

## Advanced usage

{{< blurb/images-advanced image="Python" >}}
