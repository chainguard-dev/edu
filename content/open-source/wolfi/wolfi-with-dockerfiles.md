---
title: "Creating Wolfi Images with Dockerfiles"
linktitle: "Wolfi Images with Dockerfiles"
type: "article"
description: "This tutorial demonstrates how to build a Wolfi Python image from scratch, using a Dockerfile workflow."
date: 2022-12-19T08:49:31+00:00
lastmod: 2024-08-01T10:00:31+00:00
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

[Wolfi](/open-source/wolfi/overview/) is a minimal open source Linux distribution created specifically for cloud workloads, with an emphasis on software supply chain security. Using [apk](https://wiki.alpinelinux.org/wiki/Package_management) for package management, Wolfi differs from Alpine in a few important aspects, most notably the use of glibc instead of musl and the fact that Wolfi doesn't have a kernel as it is intended to be used with a container runtime. This minimal footprint makes Wolfi an ideal base for both _distroless_ images and fully-featured builder images.

A distroless image is a minimal container image that typically doesn't include a shell or package manager. The extra tightness improves security in several aspects, but it requires a more sophisticated strategy for image composition since you can't install packages so easily. Wolfi-based builder images are still a better and more secure option to use as base images in your Dockerfile than using a full-fledged Linux distribution, as they are smaller and have fewer CVEs. You can learn more about distroless in our [Going Distroless](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started-distroless/) guide.

The [wolfi-base](https://github.com/chainguard-images/images/tree/main/images/wolfi-base) image, which we'll be using in this tutorial, is not distroless because it includes `apk-tools` and `bash`. In some cases, it can still be used to build a final distroless image, when combined with a distroless runtime in a [Docker multi-stage build](https://docs.docker.com/build/building/multi-stage/). That depends on the complexity of the image, the number of dependencies required, and whether these dependencies are system libraries or language ecosystem packages, for example.

In this article, we'll learn how to leverage Wolfi to create safer runtime environments based on containers. To demonstrate Wolfi usage in a Dockerfile workflow (using a Dockerfile to build your image), we'll create an image based on the [wolfi-base](https://github.com/chainguard-images/images/tree/main/images/wolfi-base) image maintained by Chainguard. The goal is to have a final runtime image able to execute a Python application. [Step 4](#step-4-optional-composing-distroless-images-in-a-docker-multi-stage-build) of this guide, which is optional, demonstrates how to turn that into a distroless image by combining it with a Python distroless image, also provided by Chainguard.

## Requirements

You'll need Docker to build and run the application.

## Step 1: Obtaining the Demo Application
We'll use the same demo application from the [Getting Started with the Python Chainguard Image](/chainguard/chainguard-images/getting-started/python//) tutorial to demonstrate how to build a Wolfi Python image with a Dockerfile. The application files are available in the [edu-images-demos](https://github.com/chainguard-dev/edu-images-demos) repository. We'll start by cloning that repository in a temporary folder so that we can obtain the relevant application files to run the **second** demo from that tutorial.

The following command will clone the demos repository in your `/tmp` folder:

```shell
mkdir /tmp/images-demos &&  \
  git clone https://github.com/chainguard-dev/edu-images-demos.git \
  /tmp/images-demos
```

We'll now copy the demo application to a location inside your home folder.

```shell
mkdir ~/linky && cp -R /tmp/images-demos/python/linky/* ~/linky/
```

You can now enter the newly created directory in your home folder and inspect its contents:

```shell
cd ~/linky && ls -la
```

This application will take in an image (`linky.png`) file and convert it to ANSI escape sequences to render it on the CLI. The code is on the `linky.py` file, while the `requirements.txt` file has the dependencies required by the application: [setuptools](https://pypi.org/project/setuptools/) and [climage](https://pypi.org/project/climage/).

For your reference, here is the complete `linky.py` script:

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

You'll notice that there's already a Dockerfile in that directory, but it uses the [Python Chainguard image](https://images.chainguard.dev/directory/image/python/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-open-source-wolfi-wolfi-with-dockerfiles) in a multi-stage build. In the next step, we'll replace that with a new Dockerfile that uses the [Wolfi-base](https://images.chainguard.dev/directory/image/wolfi-base/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-open-source-wolfi-wolfi-with-dockerfiles) image to build a Python image from scratch, using Wolfi apks.

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

```Dockerfile
FROM cgr.dev/chainguard/wolfi-base

ARG version=3.12
WORKDIR /app

RUN apk add python-${version} py${version}-pip && \
	chown -R nonroot:nonroot /app/

USER nonroot
COPY requirements.txt linky.png linky.py /app/
RUN  pip install -r requirements.txt --user

ENTRYPOINT [ "python", "/app/linky.py" ]
```

This Dockerfile uses a variable called `version` to define which Python version is going to be installed in the resulting image. You can change this to one of the Python versions available in Wolfi. To find out which versions are available, please refer to the [Searching for Packages](https://edu.chainguard.dev/chainguard/migration/migrating-to-chainguard-images/#searching-for-packages) section of our migration guide.

Save the file when you're done. In the next step, we'll build and run the image with `docker`.


## Step 3: Building and Running the Image

With the Dockerfile ready, you can now build your application runtime. If you're on macOS, make sure Docker is running.

Build your image with:

```shell
docker build . -t linky-demo
```

If you run into issues, try using `sudo`.

Finally, run the image with:

```shell
docker run --rm linky-demo
```

You’ll receive a representation of the Chainguard Linky logo on the command line.

## Step 4 (Optional): Composing Distroless Images in a Docker Multi-Stage Build

As discussed in the introduction, in some cases it is possible to combine your fully-featured image with a distroless runtime in a Docker multistage build, and this will give you a final image that is also distroless. Keep in mind that this technique for building distroless images is only viable when there aren't additional system dependencies that require installation via `apk`.

The [Getting Started with Python](/chainguard/chainguard-images/getting-started/python/) tutorial shows in detail how to accomplish that using a `-dev` variant as **builder**, and the distroless Chainguard Python image as production image. You can also accomplish the same results by using your newly-built image based on `wolfi-base` in place of the `-dev` variant of the Python image. We'll change the build to use a virtual environment to package the dependencies and add an extra step to create the final image.

The following Dockerfile uses a multi-stage build to obtain a final distroless image that contains everything the application needs to run. The build requires additional software that is not carried along to the final image.

Open a new file and call it `DockerfileDistroless`:

```shell
nano DockerfileDistroless
```

Copy the following code into your new file:

```Dockerfile
FROM cgr.dev/chainguard/wolfi-base as builder

ARG version=3.12

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app

RUN apk update && apk add python-$version py${version}-pip && \
	chown -R nonroot:nonroot /app/
USER nonroot
RUN python -m venv /app/venv

COPY requirements.txt /app/
RUN  pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest

ENV PYTHONUNBUFFERED=1
ENV PATH="/app/bin:$PATH"

WORKDIR /app

COPY --from=builder /app/venv /app

COPY linky.py linky.png /app/

ENTRYPOINT [ "python", "/app/linky.py" ]
```

Save and close the file when you're finished.

Now, build this image using a custom tag so that you can compare the previously built `linky-demo` image with its distroless version:

```shell
docker build . -f DockerfileDistroless -t linky-demo:distroless
```

If you run the new image, it should give you the same result as before.

```shell
docker run --rm linky-demo:distroless
```

But these images are not the same. The following command will give you a glimpse of their differences:

```shell
docker images linky-demo
```

```
REPOSITORY   TAG          IMAGE ID       CREATED         SIZE
linky-demo    distroless   619ef9b6c52d   6 seconds ago   90.3MB
linky-demo    latest       4832e9093348   4 minutes ago   110MB
```

You'll notice that the `:distroless` version is significantly smaller, because it doesn't carry along all the software necessary to build the application. More important than size, however, is the smaller attack surface that results in fewer CVEs.

## Final Considerations

In this tutorial, we've demonstrated how to build a Python image from scratch using the `wolfi-base` image. We've also shown how to compose a distroless image using a multi-stage build. This technique is useful when you need to reduce the attack surface of your application runtime, which is especially important in security-sensitive environments.

If your application runtime requires system dependencies that are not already included within a distroless variant available in our [images directory](https://images.chainguard.dev), you can still use a builder image (identified by the `-dev` suffix) or the `wolfi-base` image in a standard Dockerfile to build a suitable runtime. These images come with `apk` and a shell, allowing for further customization based on your application's requirements.

If you can't find an image that is a good match for your use case, or if your build has dependencies that cannot be met with the regular catalog, [get in touch with us](https://www.chainguard.dev/contact?utm_source=docs) for alternative options.



