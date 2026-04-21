---
title: "Installing APK packages in distroless variants"
linktitle: "Install APKs in distroless"
description: "Learn how to install APK packages into Chainguard's distroless container images that do not include package managers"
type: "article"
date: 2026-04-21T00:00:01+00:00
lastmod: 2026-04-21T00:00:01+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 080
toc: true
---

This page documents workflows for installing APK packages in [distroless variants](/chainguard/chainguard-images/about/getting-started-distroless/) of Chainguard container images, such as most builds tagged `:latest`. We copy a filesystem from a distroless container image to a build image, install APKs to it using `chroot`, then copy the modified filesystem back to the distroless image in the final step.

## Overview: Installing packages in distroless containers

The distroless variants of Chainguard Containers do not contain shells or package managers by design. This reduces attack surface and exploitability for these images. In cases where additional packages are required, we typically recommend the following:

- If packages for the language runtime (such as those installed with Python’s pip or Node’s npm) are required and no additional system-level (APK) dependencies are needed, we recommend following one of our language-specific multi-stage build tutorials ([Python](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/python/), [Node](https://edu.chainguard.dev/chainguard/migration/migrating-node/), [PHP](https://edu.chainguard.dev/chainguard/migration/migrating-php/)).  
- Use Chainguard's [Custom Assembly](https://edu.chainguard.dev/chainguard/chainguard-images/features/custom-assembly/) tool to create an image with additional packages added.  
- For some use cases, consider running our variant tagged `:latest-dev` in production. These Chainguard Containers are also low-to-zero CVE and are considered production-ready.  
- Consider requesting a custom image from Chainguard.

However, we understand that there are specific use cases that require installation of system-level APK packages in distroless variants, such as maintaining internal build environments requiring application- or team-based packaging. In these cases, you may wish to implement the approach described in this document.

## Comparing workflow options

Why not just directly copy individual APK files to a distroless image? If you’re familiar with the package or packages that need to be installed to the distroless image, this *may* work. However, this approach has a number of disadvantages:

- Scanners will typically not detect the copied files as a system-level package.
- You will also need to know the locations of all relevant files and configurations in order to copy these resources manually.
- This method can be verbose in cases where you need many packages or where packages install many files.

The chroot approach typically registers installed packages correctly, making them visible to scanners—one of the key reasons we recommend it.

Here are three options that you may be considering and our thoughts about them before we focus solely on chroot:

- **Copying** — Copying individual package files to a distroless image has the drawbacks mentioned.
- **Bind mount** — In a multi-stage build, mount APK and other required development resources from a development image, then install needed APKs using these mounted resources. This approach can work for a single point in time but can be difficult to maintain as the APK resources needed to copy over change over time.
- **Chroot (recommended)** — In a multi-stage build, install any build-time dependencies and build any required software artifacts such as binaries. Use a second base image to install runtime dependencies to a directory specified with chroot for later copying. In a final step, copy built software artifacts and the chroot installation directory to scratch and set the desired entrypoint. This method is recommended.


## Using chroot

> **Note**: If you’re working to a deadline, you can skip to this short [appendix with full code example](#appendix-b:-example-code-for-chroot-method-\(c-binary\)).

This workflow allows you to install APKs to a distroless image during a Dockerfile build by generating required software artifacts in a development environment, preparing a directory structure with runtime dependencies installed using chroot, then assembling these components back in the distroless image. The steps are as follows:

1. Pull a distroless base image for use as a filesystem reference image and as the base image for the final step. This image should be as close as possible to your desired runtime environment.
2. Pull an image with package managers and shells (typically tagged `latest-dev`) with the desired environment for building your software artifacts.
3. Install any build time dependencies and build your software artifacts, such as virtual environments or binaries.
4. Copy the entire filesystem from the reference image to a directory on the build image. Install any desired runtime APKs to this directory using chroot.
5. Switch to the original distroless image for the final assembly.
6. Copy the directory with installed runtime dependencies from the build image to root on the distroless image. Copy any built software artifacts from the build image to the distroless image.  
7. Set the desired entrypoint.

In short, we pull a distroless image, replicate its file structure as a folder on the build image, install APKs to that file structure, build our artifacts on the build image, then put the customized file structure and artifacts into the distroless image.

### Considerations

- You should build with the \`--no-cache\` flag enabled to ensure the latest remediated binaries are used and \`–pull\` to pull the most recent images.
- Images built using this approach should be rebuilt periodically, even when reference base & build images did not change, to get updates of custom packages.
- Scanners should correctly register packages in the final image.

### Example A: Preparing a Python virtual environment with APK install and runtime dependencies  

In this example, we prepare a virtual environment that will support the Python module for MariaDB, create a customized distroless file structure with needed APKs, and assemble these components in a distroless image. Creating this virtual environment (installing from pip) requires specific APKs be available at both install time and runtime.

Note that, in this example, the same APKs are installed at install and runtime. In some cases, the packages required at install and runtime will not be the same. Many or most packages in interpreted language ecosystems like Python will only require system-level APKs to be present at runtime, and in these cases you can leave out adding APKs before installation. In the example case, system-level packages are required to install MariaDB using pip as well as at runtime.

Let's get started.

1. Create a `run.py` file that will import the `_mysql` object from the `MySQLdb` module and print the version:

```python
from MySQLdb import _mysql  
print(_mysql.__version__)
```

2. Create a `requirements.txt` file with `mysqlclient` as the only listed Python dependency:

```plaintext
mysqlclient
```

3. Create a Dockerfile. Here's the full file, followed by line-by-line explanations.

```Dockerfile
# syntax=docker/dockerfile:1

FROM cgr.dev/chainguard/python:latest AS base

FROM cgr.dev/chainguard/python:latest-dev AS build

WORKDIR /app

USER root
RUN apk add --no-cache mariadb-connector-c-dev mariadb

USER 65532
RUN python -m venv venv
ENV PATH="/app/venv/bin":$PATH
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

USER root
COPY --from=base / /base-chroot
RUN mkdir -p /base-chroot
RUN apk add --no-cache --root /base-chroot mariadb-connector-c-dev mariadb

FROM cgr.dev/chainguard/python:latest
# Copy over the apks prep'ed at the end of the build stage (no apk-add in this image)
COPY --link --from=build /base-chroot /

WORKDIR /app
COPY --from=build /app/venv /app/venv
COPY run.py run.py
ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python", "run.py"]
```

First, we pull the distroless image we wish to customize. This image will be used both as a reference filesystem we will customize with our chosen APKs and later as the base image for our final assembly.

`FROM cgr.dev/chainguard/python:latest AS base`

Next, we pull our build image. The following steps will run in this environment.

`FROM cgr.dev/chainguard/python:latest-dev AS build`

Create a working directory:

`WORKDIR /app`

Now let’s add dependencies needed to install `mysqlclient` using pip. For many libraries, dependencies are needed only for runtime, so installing APKs at this stage is not needed. Note that we need root access to install APKs.

`USER root`  
`RUN apk add --no-cache mariadb-connector-c-dev mariadb`

We now create a virtual environment, give this environment precedence on the path, and install Python dependencies, in this case only `mysqlclient`. Installation by pip takes place as a nonadministrative user.

`USER 65532`  
`RUN python -m venv venv`  
`ENV PATH="/app/venv/bin":$PATH`  
`COPY requirements.txt /app/`  
`RUN pip install --no-cache-dir -r /app/requirements.txt`

We have now created the software artifact that will be copied into our final distroless image, in this case a Python virtual environment set up to run MariaDB. Now we will create a customized file structure that uses the filesystem from our distroless image as a base and includes required additional APKs needed during runtime.

First, copy the full contents of the distroless image we pulled at the beginning (labeled “base”) to a folder on our build image:

`USER root`  
`COPY --from=base / /base-chroot`  
`RUN mkdir -p /base-chroot`

Now install APKs to this copied folder using chroot:

`RUN apk add --no-cache --root /base-chroot mariadb-connector-c-dev mariadb`

We’ve now prepared two components on our build image: the required software artifacts (a Python virtual environment) and a file structure customized with installed APKs needed for runtime. We will now assemble these components in the distroless image.

Switch to the distroless image:

`FROM cgr.dev/chainguard/python:latest`

Copy the customized folder structure we created on the build image, replacing the root of our distroless image:

`COPY --link --from=build /base-chroot` 

Note here that we have chosen to use the [`--link` flag](https://docs.docker.com/reference/dockerfile/#copy---link). This adds an independent layer with the copied files and replaces the filesystem without reference to existing files, resulting in a more complete replacement. However, use of this flag can increase image size, so you may wish to experiment with disabling this flag in your build.

Next, we copy our virtual environment and run script:

`WORKDIR /app`  
`COPY --from=build /app/venv /app/venv`  
`COPY run.py run.py`

Set the path so that the virtual environment has precedence:

`ENV PATH="/app/venv/bin:$PATH"`

Finally, set the entrypoint:

`ENTRYPOINT ["python", "run.py"]`

4. Once you have your Dockerfile, `run.py`, and `requirements.txt`, build the image:

`docker build . --pull --no-cache -t mariadb-distroless`

Here, `--pull` ensures we receive the latest images, even if one is locally stored, and `--no-cache` ensures that we receive the latest versions of packages.

5. Once the build completes, run the container:

`docker run mariadb-distroless`

The output should be the version of the `MySQLdb` module (from the output of `run.py`).

### Example B: Binary compilation with local build and runtime dependencies

In this example, the work is done in our Dockerfile, which is presented in full here and then annotated below.

```Dockerfile
FROM cgr.dev/chainguard/glibc-dynamic:latest AS base

FROM cgr.dev/chainguard/gcc-glibc:latest-dev AS build


COPY <<EOF ./test.c
#include <stdio.h>
#include <curl/curl.h>
void main(){
    printf("%s\\n", curl_version());
}
EOF

RUN apk add pc:libcurl


RUN gcc test.c `pkg-config --cflags --libs libcurl` -o dynamic-binary

COPY --from=base / /base-chroot

RUN apk add --root /base-chroot so:libcurl.so.4

FROM scratch

COPY --from=build /base-chroot /

COPY --from=build /work/dynamic-binary /usr/bin/dynamic-binary

ENTRYPOINT ["/usr/bin/dynamic-binary"]

```

In this Dockerfile, we start by pulling a reference image as similar as possible to our desired runtime environment. In this case, we pull the distroless `glibc-dynamic` Chainguard Image suitable for running compiled C binaries.

`FROM cgr.dev/chainguard/glibc-dynamic:latest AS base`

Next, pull a build image with shell, APK, and needed toolchains for binary compilation or other build process:

`FROM cgr.dev/chainguard/gcc-glibc:latest-dev AS build`

Copy source file(s) for our desired artifact. This example will use a [here document](https://en.wikipedia.org/wiki/Here_document) with a short example depending on libcurl.

`COPY <<EOF ./test.c`  
`#include <stdio.h>`  
`#include <curl/curl.h>`  
`void main(){`  
   `printf("%s\\n", curl_version());`  
`}`  
`EOF`

Install any needed build-time dependencies using APK:

`RUN apk add pc:libcurl`

Build the binary:

``RUN gcc test.c `pkg-config --cflags --libs libcurl` -o dynamic-binary``

We now have the binary we’ll run in the final image. Next, we take steps to add runtime dependency APKs. We’ll first copy the entire filesystem of our reference distroless runtime image (here labeled “base”) pulled above to a directory on our build image. We will then install APKs to this directory. In the final step, this directory will be used as the filesystem in our assembled output image.

Copy the filesystem of our reference image (“base”)to a directory on our build image:

`COPY --from=base / /base-chroot`

Install APKs to the copied folder using chroot:

`RUN apk add --root /base-chroot so:libcurl.so.4`

We now have our needed components, the compiled software artifact (in this case, a binary depending on libcurl) and a directory structure customized without runtime dependencies. We will now assemble these components in scratch.

First, pull scratch:

`FROM scratch AS custom-production-image`

Copy the customized file structure to root on the scratch image (“custom-production-image”):

 `COPY --from=build /base-chroot /`

Copy the binary:

`COPY --from=build /work/dynamic-binary /usr/bin/dynamic-binary`

In the last line of the Dockerfile, set the entrypoint:

`ENTRYPOINT ["/usr/bin/dynamic-binary"]`

We will now build the image from this Dockerfile:

`docker build . --pull --no-cache -t dynamic-binary`

Finally, run our image:

`docker run dynamic-binary`

You should see output similar to the following:

```
libcurl/8.12.1 OpenSSL/3.4.1 zlib/1.3.1 brotli/1.1.0 libpsl/0.21.5 nghttp2/1.64.0 OpenLDAP/2.6.9
```

You have now created a production image based on a minimal distroless Chainguard Image customized with additional runtime dependencies as installed APKs.

## Appendix A: Example code for chroot method (Python virtualenv)

`Dockerfile`:

```Dockerfile
# syntax=docker/dockerfile:1

FROM cgr.dev/chainguard/python:latest AS base

FROM cgr.dev/chainguard/python:latest-dev AS build

WORKDIR /app

USER root
RUN apk add --no-cache mariadb-connector-c-dev mariadb

USER 65532
RUN python -m venv venv
ENV PATH="/app/venv/bin":$PATH
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

USER root
COPY --from=base / /base-chroot
RUN mkdir -p /base-chroot
RUN apk add --no-cache --root /base-chroot mariadb-connector-c-dev mariadb

FROM cgr.dev/chainguard/python:latest
# Copy over the apks prep'ed at the end of the build stage (no apk-add in this image)
COPY --link --from=build /base-chroot /

WORKDIR /app
COPY --from=build /app/venv /app/venv
COPY run.py run.py
ENV PATH="/app/venv/bin:$PATH"

ENTRYPOINT ["python", "run.py"]
```

---

`run.py`:

```python
from MySQLdb import _mysql
print(_mysql.__version__)
```

---

`Requirements.txt`:

```plaintext
mysqlclient
```

## Appendix B: Example code for chroot method (C binary)

Annotated `Dockerfile`:

```Dockerfile
# SPDX-FileCopyrightText: 2025 Chainguard, Inc.
# SPDX-License-Identifier: Apache-2.0

# Pull unmodified base image
FROM cgr.dev/chainguard/glibc-dynamic:latest AS base

# Pull build container with toolchains and apk
FROM cgr.dev/chainguard/gcc-glibc:latest-dev AS build

# Get workload source code
COPY <<EOF ./test.c
#include <stdio.h>
#include <curl/curl.h>
void main(){
    printf("%s\\n", curl_version());
}
EOF

# Install build-time dependency
RUN apk add pc:libcurl

# Compile workload code
RUN gcc test.c `pkg-config --cflags --libs libcurl` -o dynamic-binary

# Copy base image contents to a subfolder
COPY --from=base / /base-chroot

# Customize base image chroot
RUN apk add --root /base-chroot so:libcurl.so.4

# Create customized production image from scratch
FROM scratch AS custom-production-image
# Copy customized base image
COPY --from=build /base-chroot /
# Copy workload binary
COPY --from=build /work/dynamic-binary /usr/bin/dynamic-binary

ENTRYPOINT ["/usr/bin/dynamic-binary"]
```

Build the image:

`docker build . --no-cache -t dynamic-binary`

Run the image:

`docker run dynamic-binary`

If the build was successful, you should see version information from libcurl as `output.t`.