---
title: "Getting Started with the C/C++ Chainguard Images"
type: "article"
linktitle: "C/C++"
aliases: 
- /chainguard/chainguard-images/getting-started/getting-started-c
- /chainguard/chainguard-images/getting-started/getting-started-c++
description: "Tutorial on how to get started with the C/C++ Chainguard Images"
date: 2024-07-30T15:54:33+00:00
lastmod: 2024-08-05T16:08:38+00:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 002
toc: true
---

C and its derivative, C++, are two widely adopted compiled languages. Chainguard offers a variety of minimal, low-CVE container images built on the [Wolfi un-distro](/open-source/wolfi/overview/) which are suitable for deploying C-based compiled programs. In this guide, we will explore three ways you can use Chainguard Images to compile and run a C-based binary.

The image with which you choose to run your compiled program depends on the nature of your binaries. Static binaries can be executed in the minimal `static` Chainguard Image, while dynamically linked binaries can be run in the `glibc-dynamic` Image. For our demonstration, we will first compile a C binary using the `gcc-glibc` Chainguard Image, and then learn how to use a multi-stage build to run the resulting binary in the `glibc-dynamic` image. We'll also cover an example showing the multi-stage build process for the C++ programming language. To learn more about the differences between these images, read our article on [Choosing an Image for your Compiled Programs](/chainguard/chainguard-images/working-with-images/compiled-programs/). 

{{< details "What is distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

To follow along with this guide, you will need to have [Docker Engine](https://docs.docker.com/engine/install/) and `gcc`, the [GNU Compiler Collection](https://gcc.gnu.org/) installed on your machine. You can find the code and Dockerfiles used in this repository at our [Demos GitHub repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/c).

## Example 1 --- Minimal C Chainguard Image

### Step 1: Setting up a Demo Application

To start, let's create a simple demonstration application for us to run in our container. First we will create a folder to contain our files. The following command will create a new directory `cguide` and navigate to it.

```sh
mkdir -p cguide && cd cguide
```

Within this directory, we will create a file to hold the code for our first example. Execute the following command in your terminal to begin editing a new file using the text editor of your choice. We will demonstrate using `nano`:

```sh
nano hello.c
```

Inside of our `hello.c` file, copy in the following code. This code will execute a simple "Hello, world!" application.

```C
/* Chainguard Academy (edu.chainguard.dev)
*  Getting Started with the C/C++ Chainguard Images
*  Examples 1 & 2 - C
*/

#include <stdio.h>

// Main Function
int main(){
	printf("Hello, world!\n");
	printf("I am a demo from the Chainguard Academy.\n");
	printf("My code was written in C.\n");
	
	return 0;
}
```

When you are done editing the file, save and close it.

Now, let's compile this file with `gcc`. The command uses the `-Wall` flag to display compiler errors and warnings, if any occur, and uses the `-o` flag to rename our executable to `hello`.

```sh
gcc -Wall -o hello hello.c
```

Once your program is successfuly compiled, you can run it with the following command:

```sh
./hello
```

You should see the "Hello, world!" program output in your terminal if the program executed successfully.

```Output
Hello, world!
I am a demo from the Chainguard Academy.
My code was written in C.
```

### Step 2: Creating the Dockerfile

Now that we have successfully tested our example program locally, next, we will compile and run it inside of an image. An advantage of choosing to run your code inside of containerized environments is portability. In the previous step, `gcc` compiled the binary to run on your machine. However, if you were to run this binary on a different operating system, it likely will fail to execute properly. Using a container ensures that your program will run on any machine as the containerized environment will be consistent across platforms.

Let us begin by creating a Dockerfile called `Dockerfile1` for our image. Execute the following code with the text editor of your choice to begin editing a new file.

```sh
nano Dockerfile1
```

The following Dockerfile will:
1. Use the `gcc-glibc:latest` Chainguard Image as the base image;
2. Set the current working directory to `/usr/bin`;
3. Copy our `hello.c` program code to the current directory;
4. Compile our program and name it `hello`;
5. Execute the compiled binary when the container is started.

```Dockerfile
# Example 1 - Single Stage Build for C

FROM cgr.dev/chainguard/gcc-glibc:latest

WORKDIR /usr/bin

COPY hello.c ./

RUN ["gcc", "-Wall", "-o", "hello", "hello.c"]

ENTRYPOINT ["./hello"]
```

Copy the text in to your Dockerfile, save, and close it.

Next, start Docker Engine on your machine. Execute the following command in your terminal. The `-f` flag specifies the Dockerfile which we are using to build from, and the `-t` flag will tag our image with a meaningful name.

```sh
docker build -f Dockerfile1 -t example1:latest .
```

With your image built, we can now run it with the following command.

```sh
docker run --name example1 example1:latest
```

You should see output in your terminal identical to that of the binary we compiled locally.

```Output
Hello, world!
I am a demo from the Chainguard Academy.
My code was written in C.
```

## Example 2 --- Multi-Stage Build for C Applications

In our first example, we successfully compiled and executed our C binary in the `gcc-glibc` image. To go a step further, we can use a multi-stage build, which allows us to compile our program in one image and execute it in another image. A multi-stage build gives you more control over your final image, as you can transfer your program to an image with a smaller footprint after build time to reduce your program's attack surface. The `glibc-dynamic` image, which we will use as our second stage in the build, does not contain `gcc`. Because of this, a malicious binary could not be compiled by an attacker tampering with the image.

### Step 1: Creating the Dockerfile

Using the text editor of your choice, create a new Dockerfile called `Dockerfile2`.

```sh
nano Dockerfile2
```

The following Dockerfile will:
1. Use the `gcc-glibc` Chainguard Image as the builder stage;
2. Set the current working directory of the image to `/usr/bin`;
3. Copy our `hello.c` program code to the current directory;
4. Compile the program using `gcc` and name it `hello`;
5. Begin a new stage using the `glibc-dynamic` Chainguard Image;
6. Set the current working directory of the new image to `/usr/bin`;
7. Copy the compiled `hello` C binary from our builder stage;
8. Execute our binary from the `glibc-dynamic` image when the container is started.

```Dockerfile2
# Example 2 - Multi-Stage Build for C

FROM cgr.dev/chainguard/gcc-glibc:latest AS builder

WORKDIR /usr/bin

COPY hello.c ./

RUN ["gcc", "-Wall", "-o", "hello", "hello.c"]

FROM cgr.dev/chainguard/glibc-dynamic:latest

WORKDIR /usr/bin

COPY --from=builder /usr/bin/hello ./

ENTRYPOINT ["./hello"]
```

When you are finished editing your Dockerfile, save and close it.

With our new Dockerfile created, we can build the image. Execute the following command in your terminal to build your multi-stage image.

```sh
docker build -f Dockerfile2 -t example2:latest .
```

With your image built, we can now run it with the following command.

```sh
docker run --name example2 example2:latest
```

You should see output in your terminal identical to that of the previous example.

```Output
Hello, world!
I am a demo from the Chainguard Academy.
My code was written in C.
```

Great! Having your program execute from a smaller image with less packages reduces your potential attack surface, making it a more secure approach for production-facing builds.

## Example 3 --- Multi-Stage Build for C++ Applications

So far, our demonstrations have featured a program coded in C. A similar image building process applies to binaries compiled for the C++ programming language. 

### Step 1: Setting up a Demo Application

In your terminal, create a new file called `hello.cpp` with the text editor of your choice.

```sh
nano hello.cpp
```

Copy the following C++ code to the file you just created. This code will display a simple greeting specifying that it was written in C++.

```C++
/* Chainguard Academy (edu.chainguard.dev)
*  Getting Started with the C/C++ Chainguard Images
*  Example 3 - C++
*/

#include <iostream>
using namespace std;

// Main Function
int main(){
    cout << "Hello, world!\n";
    cout << "I am a demo from the Chainguard Academy.\n";
    cout << "My code was written in C++.\n";

    return 0;
}
```

When you are done editing your file, save and close it.

You can now compile your C++ program using `g++`. Execute the following command in your terminal to compile the program. The command will display any compiler warnings or errors and will name the resultant binary `hello`.

```sh
g++ -Wall -o hello hello.cpp
```

Now you can test your compiled binary.

```sh
./hello
```

You should see the following output in your terminal.

```Output
Hello, world!
I am a demo from the Chainguard Academy.
My code was written in C++.
```

### Step 2: Creating the Dockerfile

Now, with a working C++ example, we can compile and run our program using a multi-stage build. With the text editor of your choice, create a new file named `Dockerfile3`.

```sh
nano Dockerfile3
```

The following Dockerfile will:
1. Use the `gcc-glibc` Chainguard Image as the builder stage;
2. Set the current working directory of the image to `/usr/bin`;
3. Copy our `hello.cpp` program code to the current directory;
4. Compile the program using `g++` and name it `hello`;
5. Begin a new stage using the `glibc-dynamic` Chainguard Image;
6. Set the current working directory of the new image to `/usr/bin`;
7. Copy the compiled `hello` C++ binary from our builder stage;
8. Execute our binary from the `glibc-dynamic` image when the container is started.

```Dockerfile3
# Example 3 - Multi-Stage Build for C++

FROM cgr.dev/chainguard/gcc-glibc:latest AS builder

WORKDIR /usr/bin

COPY hello.cpp ./

RUN ["g++", "-Wall", "-o", "hello", "hello.cpp"]

FROM cgr.dev/chainguard/glibc-dynamic:latest

WORKDIR /usr/bin

COPY --from=builder /usr/bin/hello ./

ENTRYPOINT ["./hello"]
```

When you are finished editing your Dockerfile, save and close it.

With our new Dockerfile created, we can build the image. Execute the following command in your terminal to build your multi-stage C++ image.

```sh
docker build -f Dockerfile3 -t example3:latest .
```

With your image built, we can now run it with the following command.

```
docker run --name example3 example3:latest
```

You should see output in your terminal identical to that of the C++ binary you compiled locally.

```Output
Hello, world!
I am a demo from the Chainguard Academy.
My code was written in C++.
```

## Advanced Usage

{{< blurb/images-advanced image="C/C++" >}}