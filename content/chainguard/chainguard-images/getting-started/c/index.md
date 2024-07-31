---
title: "Getting Started with the C/C++ Chainguard Images"
type: "article"
linktitle: "C/C++"
aliases: 
- /chainguard/chainguard-images/getting-started/getting-started-c
- /chainguard/chainguard-images/getting-started/getting-started-c++
description: "Tutorial on how to get started with the C/C++ Chainguard Images"
date: 2024-07-30T15:54:33+00:00
lastmod: 2024-07-30T15:54:33+00:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 002
toc: true
---

Chainguard offers a variety of minimal, low-CVE container images which are suitable for running and deploying compiled programs. C and C++ are two examples of widely adopted compiled languages used by developers. Chainguard builds a variety of images for compiled programs. To learn more about the differences between each image, read our article on [Choosing an Image for your Compiled Programs](/chainguard/chainguard-images/working-with-images/compiled-programs/). 

In this guide, we will explore two ways you can use Chainguard Images to run your C and C++ binaries.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

To follow along with this guide, you will need to have [Docker Engine](https://docs.docker.com/engine/install/) and `gcc`, the [GNU Compiler Collection](https://gcc.gnu.org/) installed on your machine. You can find the code used in this repository at our [Demos GitHub repository]().

## Example 1 --- Minimal C/C++ Chainguard Image

### Step 1: Setting up a Demo Application

To start, let's create a simple demonstration application for us to use in our container. First we will create a folder to contain our files. You can create this at a location convenient for you. The following command will create a new directory and navigate to it.

```sh
mkdir -p cguide && $_ cd cguide
```

Within this directory, we will create a file to hold the code for our first example. Execute the following command in your terminal to begin editing a new file. If you prefer a text editor other than `nano`, feel free to use an alternative.

```sh
nano example1.c
```

Inside of our `example1.c` file, copy in the following code. This code will execute a simple "Hello, world!" application to confirm our code is running as intended.
```nano
/* Chainguard Academy (edu.chainguard.dev)
*  Getting Started with the C/C++ Chainguard Images
*  Example 1 --- Minimal C/C++ Chainguard Image
*/

#include <stdio.h>

// Main Function
int main(){
        printf("Hello, world!\n");
        printf("I am a demo from the Chainguard Academy.\n");

        return 0;
}
```

When you are done editing the file, save and close it.

Now, let's compile this file with `gcc`. The command uses the `-Wall` flag to display compiler errors and warnings, if any occur, and uses the `-o` flag to rename our executable to `example1`.

```sh
gcc -Wall example1.c
```

Once your program is successfuly compiled, you can run it with the following command:

```sh
./example1
```

You should see the "Hello, world!" program output in your terminal if the program executed successfully.
```
Hello, world!
I am a demo from the Chainguard Academy.
```

### Step 2: Creating the Dockerfile

Now that we have a working demo, we can use a Dockerfile to run it inside of a Chainguard Image. In the `cguide` folder, create a new `Dockerfile`.

```sh
nano Dockerfile
```

Inside the Dockerfile, copy the following text.

```Dockerfile
FROM cgr.dev/chainguard/static:latest

```

## Example 2 --- Multi-Stage Build for C/C++ Chainguard Images

### Step 1: Setting up a Demo Application

### Step 2: Creating the Dockerfile

## Advanced Usage

{{< blurb/images-advanced image="C/C++" >}}