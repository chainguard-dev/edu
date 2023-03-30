---
title: "Creating Wolfi Images with Dockerfiles"
type: "article"
description: "This tutorial demonstrates how to build a Wolfi Python image from scratch, using a Dockerfile workflow."
date: 2022-12-19T08:49:31+00:00
lastmod: 2022-12-19T08:49:31+00:00
draft: false
tags: ["Wolfi", "Procedural"]
images: []
menu:
  docs:
    parent: "wolfi"
weight: 500
toc: true
---

## Introduction

[Wolfi](https://edu.chainguard.dev/open-source/wolfi/overview/) is a minimal open source Linux distribution created specifically for cloud workloads, with an emphasis on software supply chain security. Using [apk](https://wiki.alpinelinux.org/wiki/Package_management) for package management, Wolfi differs from Alpine in a few important aspects, most notably the use of glibc instead of musl and the fact that Wolfi doesn't have a kernel of its own since it is built to run on containers. The minimal footprint makes Wolfi an ideal base for both _distroless_ runtimes and fully-featured builder images.

A _distroless_ image is typically a very minimal container image that doesn't have shells or package managers. The extra tightness improves security in several aspects, but it requires a more sophisticated strategy for image composition since you can't install packages so easily.

There are currently two main strategies for building distroless images with Wolfi:

- **With a Dockerfile:** Use `-dev` variants **or** the `wolfi-base` image from [Chainguard Images](https://edu.chainguard.dev/chainguard/chainguard-images/overview/) to build the application, and copy the artifacts to a distroless runtime image. This option is typically more accessible for people who are already used to a Dockerfile workflow.
- **With apko:** Use [apko](https://edu.chainguard.dev/open-source/apko/overview/) to build a distroless image with only the packages you need, fully customized. This option requires a bigger learning curve to get used to how apko works, but it will give you smaller images with better SBOM coverage. The [Getting Started with apko](https://edu.chainguard.dev/open-source/apko/getting-started-with-apko/) tutorial explains how that works in practice.

The [wolfi-base](https://github.com/chainguard-images/images/tree/main/images/wolfi-base) image, which we'll be using in this tutorial, is not distroless, because it includes `apk-tools` and `bash`. It can still be used to build a final distroless image, when combined with a distroless runtime in a [Docker multi-stage build](https://docs.docker.com/build/building/multi-stage/).

In this article, we'll learn how to leverage Wolfi to create safer runtime environments based on containers. To demonstrate Wolfi usage in a Dockerfile workflow (using a Dockerfile to build your image), we'll create an image based on the [wolfi-base](https://github.com/chainguard-images/images/tree/main/images/wolfi-base) image maintained by Chainguard. The goal is to have a final runtime image able to execute a Python command-line script. The [Step 4](#step-4-optional-composing-distroless-images-in-a-docker-multi-stage-build) of this guide, which is optional, demonstrates how to turn that into a distroless image by combining it with a Python distroless runtime.

## Requirements

You'll need Docker to build and run the application.

## Step 1: Obtaining the Demo Application
We'll use the same demo application from the [Getting Started with the Python Chainguard Image](/chainguard/chainguard-images/reference/python/getting-started-python/) tutorial to demonstrate how to build a Wolfi Python image with a Dockerfile. The application files are available in the [edu-images-demos](https://github.com/chainguard-dev/edu-images-demos) repository. We'll start by cloning that repository in a temporary folder so that we can obtain the relevant application files to run the **second** demo from that tutorial.

The following command will clone the demos repository in your `/tmp` folder:

```shell
mkdir /tmp/images-demos &&  \
  git clone https://github.com/chainguard-dev/edu-images-demos.git \
  /tmp/images-demos
```

We'll now copy the demo application to a location inside your home folder.

```shell
mkdir ~/inky && cp -R /tmp/images-demos/python/inky/* ~/inky/
```

You can now enter the newly created directory in your home folder and inspect its contents:

```shell
cd ~/inky && ls -la
```

This application will take in an image (`inky.png`) file and convert it to ANSI escape sequences to render it on the CLI. The code is on the `inky.py` file, while the `requirements.txt` file has the dependencies required by the application: [setuptools](https://pypi.org/project/setuptools/) and [climage](https://pypi.org/project/climage/).

For your reference, here is the complete `inky.py` script:

```python
'''import climage module to display images on terminal'''
import climage


def main():
    '''Take in PNG and output as ANSI to temrinal'''
    output = climage.convert('inky.png', is_unicode=True)
    print(output)

if __name__ == "__main__":
    main()
```

You'll notice that there's already a Dockerfile in that directory, but it uses the [Python Chainguard image](https://edu.chainguard.dev/chainguard/chainguard-images/reference/python/overview/) in a multi-stage build. In the next step, we'll replace that with a new Dockerfile that uses the [Wolfi-base](https://edu.chainguard.dev/chainguard/chainguard-images/reference/wolfi-base/image_specs/) image to build a Python image from scratch, using Wolfi apks.

## Step 2: Creating the Dockerfile

Now we'll create the Dockerfile to run the application. This Dockerfile will set up a new user and WORKDIR, copy relevant files, and install dependencies with Pip. It will also define the entry point that will be executed when we run this image with `docker run`.

You can rename the old Dockerfile if you want to keep it for tests later.

```shell
mv Dockerfile _DockerfileBkp
```

Then, create a new Dockerfile:

```shell
nano Dockerfile
```

Copy the following content to it:

```
FROM cgr.dev/chainguard/wolfi-base

ARG version=3.11
RUN adduser -D nonroot
WORKDIR /app

RUN apk add python-${version} py${version}-pip && \
	chown -R nonroot.nonroot /app/

USER nonroot
COPY requirements.txt inky.png inky.py /app/
RUN  pip3 install -r requirements.txt --user

ENTRYPOINT [ "python", "/app/inky.py" ]

```

This Dockerfile uses a variable called `version` to define which Python version is going to be installed on the resulting image. You can change this to one of the available Python versions on the [wolfi-dev/os](https://github.com/wolfi-dev/os) repository.

Save the file when you're done. In the next step, we'll build and run the image with `docker`.


## Step 3: Building and Running the Image

With the Dockerfile ready, you can now build your application runtime. If you're on macOS, make sure Docker is running.

Build your image with:

```shell
docker build . -t inky-demo
```

If you run into issues, try using `sudo`.

Finally, run the image with:

```shell
docker run --rm inky-demo
```

You’ll receive a representation of the Chainguard Inky logo on the command line.

## Step 4 (Optional): Composing Distroless Images in a Docker Multi-Stage Build

As discussed in the introduction, it is possible to combine your fully-featured image with a distroless runtime in a Docker multistage build, and this will give you a final image that is also distroless. The [Getting Started with Python](/chainguard/chainguard-images/reference/python/getting-started-python/) tutorial shows in detail how to accomplish that using a `-dev` variant as **builder**, and the distroless Chainguard Python image as runtime. You can also accomplish the same results by using your newly built image based on `wolfi-base` in place of the `-dev` variant of the Python image. The only difference is that you'll need a few more steps to set up your builder image.

The following Dockerfile uses a multi-stage build to obtain a final distroless image that contains everything the application needs to run. The build requires additional software that is not carried along to the final image.

Open a new file and call it `DockerfileDistroless`:

```shell
nano DockerfileDistroless
```

Copy the following code into your new file:

```
FROM cgr.dev/chainguard/wolfi-base as builder

ARG version=3.11
RUN adduser -D nonroot
WORKDIR /app

RUN apk add python-$version py${version}-pip && \
	chown -R nonroot.nonroot /app/

USER nonroot
COPY requirements.txt /app/
RUN  pip3 install -r requirements.txt --user

FROM cgr.dev/chainguard/python:3.11

ARG version=3.11
WORKDIR /app

COPY --from=builder /home/nonroot/.local/lib/python${version}/site-packages /home/nonroot/.local/lib/python${version}/site-packages

COPY inky.py inky.png /app/

ENTRYPOINT [ "python", "/app/inky.py" ]
```

Save and close the file when you're finished.

Now, build this image using a custom tag so that you can compare the previously built `inky-demo` image with its distroless version:

```shell
docker build . -f DockerfileDistroless -t inky-demo:distroless
```

If you run the new image, it should give you the same result as before.

```shell
docker run --rm inky-demo:distroless
```

But these images are not the same. The following command will give you a glimpse of their differences:

```shell
docker images inky-demo
```

```
REPOSITORY   TAG          IMAGE ID       CREATED         SIZE
inky-demo    distroless   619ef9b6c52d   6 seconds ago   66.6MB
inky-demo    latest       4832e9093348   4 minutes ago   99.6MB
```

And you'll notice that the `:distroless` version is significantly smaller, because it doesn't carry along all the software necessary to build the application. More important than size, however, is the smaller attack surface that results in less CVEs.

## Final Considerations

If your build requires dependencies that are not yet available on Wolfi, you can build your own apks using [melange](/open-source/melange/overview/). Check the [Getting started with melange](https://edu.chainguard.dev/open-source/melange/tutorials/getting-started-with-melange/) guide for more details on how to go about that.

Check also the public catalog of [Chainguard Images](/chainguard/chainguard-images/reference/) for application environments including `-dev` variants that can be used as builders for your specific application runtime.
