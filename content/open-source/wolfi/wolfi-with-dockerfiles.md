---
title: "Creating Wolfi Images with Dockerfiles"
type: "article"
description: "This tutorial demonstrates how to build a Wolfi Python image from scratch, using a Dockerfile workflow."
date: 2022-12-19T08:49:31+00:00
lastmod: 2022-12-19T08:49:31+00:00
draft: false
images: []
menu:
  docs:
    parent: "wolfi"
weight: 500
toc: true
---

## Introduction

[Wolfi](https://edu.chainguard.dev/open-source/wolfi/overview/) is a minimal open source Linux distribution created specifically for cloud workloads, with emphasis on software supply chain security. Using [apk](https://wiki.alpinelinux.org/wiki/Package_management) for package management, Wolfi differs from Alpine in a few important aspects, most notably the use of glib-c instead of Musl and the fact that Wolfi doesn't have a kernel of its own since it is built to run on containers.

In this article, we'll see how to leverage Wolfi to create safer runtime environments based on containers. To demonstrate Wolfi usage in a Dockerfile workflow (using a Dockerfile to build your image), we'll create an image based on the [wolfi-base](https://github.com/chainguard-images/images/tree/main/images/wolfi-base) image maintained by Chainguard. The goal is to have a final runtime image able to execute a Python command-line script.

### Requirements

You'll need a local development environment with Python in order to test the demo, and Docker to build and run the application.

## Obtaining the Demo App
We'll use the same demo application from the [Getting Started with the Python Chainguard Image](/chainguard/chainguard-images/reference/python/getting-started-python/) tutorial to demonstrate how to build a Wolfi Python image with a Dockerfile. The application files are available on the [edu-images-demos](https://github.com/chainguard-dev/edu-images-demos) repository. We'll start by cloning that repository in a temporary folder so that we can obtain the relevant application files to run the **second** demo from that tutorial.

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

For your reference, here is the full content from the `inky.py` script:

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

To test that the application works as expected, first install the dependencies using Pip.

```shell
pip3 install -r requirements.txt
```

Then, run the application with:

```shell
python3 inky.py
```

You’ll receive a representation of the Chainguard Inky logo on the command line. With the demo application ready, you can now move on to building the Wolfi container image.

## Creating the Dockerfile

Now we'll create the Dockerfile to run the application. This Dockerfile will set up a new WORKDIR, copy relevant files, and install dependencies with Pip. It will also define the entry point that will be executed when we run this image with `docker run`.

You can rename the old Dockerfile if you want to keep it for tests later.

```shell
mv Dockerfile _DockerfileBkp
```

Then, create a new Dockerfile and copy the following content to it:

```
FROM cgr.dev/chainguard/wolfi-base

WORKDIR /app
COPY requirements.txt inky.py inky.png /app/
RUN apk add python-3.11 py3.11-pip && \
    pip3 install -r requirements.txt --user

ENTRYPOINT ["python", "/app/inky.py"]

```

After saving the file, you can build your application runtime image with:

```shell
docker build . -t inky-demo
```

Finally, run the image with:

```shell
docker run --rm inky-demo
```

And you should get a similar result as the previous time you run the script.

## Building distroless Wolfi Images

A _distroless_ image is typically a very minimal container image that doesn't have shells or package managers. The extra tightness improves security in several aspects, but it requires a more sophisticated strategy for image composition since you can't install packages so easily. There are currently two main strategies for building distroless images with Wolfi:

- **With a Dockerfile:** Use `-dev` variants from [Chainguard Images](https://edu.chainguard.dev/chainguard/chainguard-images/overview/) to build the application, and copy the artifacts to a pure distroless image in a [Docker multi-stage build](https://docs.docker.com/build/building/multi-stage/). This option is typically more accessible for people who are already used to a Dockerfile workflow. Check the [Getting Started with the Python Chainguard Image](https://edu.chainguard.dev/chainguard/chainguard-images/reference/python/getting-started-python/) guide for practical examples.
- **With apko:** Use [apko](https://edu.chainguard.dev/open-source/apko/overview/) to build a distroless image with only the packages you need, fully customized. This option requires a bigger learning curve to get used to how apko works, but it will give you smaller images with a better SBOM coverage. Check the [Getting Started with apko](https://edu.chainguard.dev/open-source/apko/getting-started-with-apko/) tutorial to see how that works in practice.
