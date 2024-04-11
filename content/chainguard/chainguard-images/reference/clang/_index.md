---
title: "Image Overview: clang"
linktitle: "clang"
type: "article"
layout: "single"
description: "Overview: clang Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/clang/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/clang/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/clang/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/clang/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Clang](https://clang.llvm.org) is a compiler front end for the C, C++, Objective-C, and Objective-C++ programming languages, as well as the OpenMP, OpenCL, RenderScript, CUDA, SYCL, and HIP frameworks
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/clang:latest
```


<!--body:start-->


## Use It!

To illustrate working with the Clang Chainguard Image, this section outlines how you can use it to compile a "Hello World!" program written in C. 

To begin, run the following command to create a file named `hello.c` to hold the C code.

```shell
cat > /tmp/hello.c <<EOF
#include <stdio.h>

int main() {
    printf("Hello World!\n");
    return 0;
}
EOF
```

To simplify cleanup, this command places the file in the `/tmp` temporary directory. 

Next, run the following `docker` command. This will mount the contents of your local `/tmp` directory (including the `hello.c` file) into the container's `work` directory. Once there, Clang will compile the C code into an executable program named `hello`.

```shell
docker run --rm -v /tmp:/work cgr.dev/chainguard/clang:latest hello.c -o /work/hello
```

The `hello` program will be stored back in your local `/tmp` directory. You can test that everything worked correctly by executing this program.

```shell
/tmp/hello
```
```
Hello World!
```

Be aware that, depending on your local machine's operating system, you may not be able to execute this file directly like this. This may be because the program is built with [Wolfi](https://edu.chainguard.dev/open-source/wolfi/overview/). This creates an executable in the Executable and Linkable Format, the standard file format for Linux executables. Other systems might expect a different format; for example, this executable can't run directly on MacOS systems, which instead expect the Mach-O format. It could also be that your machine's `/tmp` directory was mounted with the `noexec` option, preventing anything stored in that directory from being executed.

If you receive an error when trying to run the `hello` program, you can try using another Wolfi-based image to execute it, like so. 

```shell
docker run --rm -v /tmp:/work cgr.dev/chainguard/bash /work/hello
```
```
. . .
Hello World!
```
<!--body:end-->

