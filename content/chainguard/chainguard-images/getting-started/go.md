---
title: "Getting Started with the Go Chainguard Container"
type: "article"
linktitle: "Go"
aliases:
- /chainguard/chainguard-images/getting-started/getting-started-go
description: "Tutorial on the distroless Go Chainguard Container"
date: 2023-02-28T11:07:52+02:00
lastmod: 2025-03-24T11:07:52+02:00
tags: ["Chainguard Containers", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 010
toc: true
---

The [Go Chainguard Container](https://images.chainguard.dev/directory/image/go/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-getting-started-go) is a container image suitable for building Go applications. The `latest` variant is a distroless image without a package manager, while the `latest-dev` variant offers additional building tools and the apk package manager.

In this guide, we'll demonstrate how to build and execute Go applications using Chainguard Containers, using three examples from our [demos repository](https://github.com/chainguard-dev/edu-images-demos). In the first example, we'll build a CLI application using a Docker multi-stage build. In the second example, we'll build an application that's accessible by HTTP server, also using a Docker multi-stage build to obtain an optimized runtime. The third example shows how to build an image using [ko](https://ko.build/), a tool that enables you to build container images from Go programs and push them to container registries without requiring a Dockerfile.

The examples in this guide recommend executing Go binaries from one of our runtime Chainguard Containers, such as the [`glibc-dynamic`](https://images.chainguard.dev/directory/image/glibc-dynamic/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-getting-started-go) or [`static`](https://images.chainguard.dev/directory/image/static/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-getting-started-go) Chainguard Containers. That is possible because Go applications are compiled and the toolchain is not typically required in a runtime container image.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Preparation
This tutorial requires Docker to be installed on your local machine. If you don't have Docker installed, you can download and install it from the [official Docker website](https://docs.docker.com/get-docker/). The third and optional example requires the installation of [ko](https://ko.build/), which you can install by following the instructions on the official site.

### Cloning the Demos Repository
Start by cloning the demos repository to your local machine:

```shell
git clone git@github.com:chainguard-dev/edu-images-demos.git
```
Access the `go` folder in the repository:

```shell
cd edu-images-demos/go
```

Here you will find three folders, each with a different demo that we'll cover in this guide.

## Example 1: CLI Application in Multi-Stage Build
The following example demonstrates a command line application with support for flags and positional arguments. The application prints a modifiable greeting message and provides usage information if the wrong number of arguments are passed by a user or the user passes an unrecognized flag.

Start by accessing the `go-greeter` folder in the demos repository:

```shell
cd go-greeter
```

For reference, here is the content of the `Dockerfile` for this demo:

```Dockerfile
FROM cgr.dev/chainguard/go AS builder
COPY . /app
RUN cd /app && go build -o go-greeter .

FROM cgr.dev/chainguard/static
COPY --from=builder /app/go-greeter /usr/bin/
ENTRYPOINT ["/usr/bin/go-greeter"]
```

This Dockerfile will:

1. Start a build stage based on the `go:latest` container image and name it `builder`;
2. Copy the application files to the `/app` directory in the image;
3. Build the application in the `/app` directory;
4. Start a new build stage based on the `static:latest` image;
5. Copy the built application from the `builder` stage to the `/usr/bin` directory in the new image;
6. Set the entrypoint to the built application.

Run the following command to build the container image, tagging it `go-greeter`:

```shell
docker build . --pull -t go-greeter
```

You can now run the container image with:

```shell
docker run go-greeter
```
You should get output similar to the following:

```
Hello, Linky 🐙!
```

You can also pass in arguments that will be parsed by the Go CLI application:

```shell
docker run go-greeter -g Greetings "Chainguard user"
```
This will produce the following output:

```
Greetings, Chainguard user!
```
The application will also share usage instructions when prompted with the `--help` flag or when invalid flags are passed.

Because we used the `static` Chainguard Container as our runtime, the final container image only requires a few megabytes on disk:

```shell
docker inspect go-greeter | jq -c 'first' | jq .Size | numfmt --to iec --format "%8.4f"
```
```
 3.3009M
```
The final size, `3.309M`, is orders of magnitude smaller than it would be running the application using a Go image. However, if your application is dynamically linked to shared objects, consider using the `glibc-dynamic` Chainguard Container for your runtime or take extra steps to build your Go binary statically. In the next example, we'll build a web application and use the `glibc-dynamic` Chainguard Container as runtime.

## Example 2: Web Application

The second example demonstrates an application that's accessible by HTTP server. The application renders a simple message that changes based on the URI.

Start by accessing the `greet-server` folder in the Go demos repository:

```shell
cd greet-server
```

For reference, here is the content of the `Dockerfile` for this demo:

```Dockerfile
FROM cgr.dev/chainguard/go AS builder
COPY . /app
RUN cd /app && go build

FROM cgr.dev/chainguard/glibc-dynamic
COPY --from=builder /app/greet-server /usr/bin/

EXPOSE 8080

ENTRYPOINT ["/usr/bin/greet-server"]
```

Use the following command to build the container image, tagging it `greet-server`:

```shell
docker build . --pull -t greet-server
```

Now you can run the container image with the following command:

```shell
docker run -p 8080:8080 greet-server
```

Visit `http://0.0.0.0:8080/` using a web browser on your host machine. You should get a greeting message:

```
Hello, Linky 🐙!
```

Changes to the URI will be routed to the application. Try visiting [http://0.0.0.0:8080/Chainguard%20Customer](http://0.0.0.0:8080/Chainguard%20Customer). You should see the following output:

```
Hello, Chainguard Customer!
```

The application will also share version information at [http://0.0.0.0:8080/version](http://0.0.0.0:8080/version).

## Example 3: Minimal Go Chainguard Container Built with ko

In this example, we'll build a distroless Go Chainguard Container with [ko](https://ko.build/). ko offers fast container image builds for Go applications without requiring a Dockerfile. Additionally, ko produces [SBOMs](/open-source/sbom/what-is-an-sbom/) by default, supporting a holistic approach to software security.

Start by accessing the `go-digester` folder in the Go demos repository:

```shell
cd go-digester
```

The `go-digester` demo uses the `go-containerregistry` library to print out the digest of the latest build of a Chainguard Container, using `go` as the default image to pull the digest from, and with an optional parameter to specify a different container image name. If you have Go installed locally, you can run the application with:

```shell
go run main.go
```
You should obtain output similar to this:

```
The latest digest of the go Chainguard Container is sha256:86178b42db2e32763304e37f4cf3c6ec25b7bb83660dcb985ab603e3726a65a6
```
We'll now use ko to build an image that is suitable to run the application defined in `main.go`. By default, ko uses the `cgr.dev/chainguard/static` image as the base image for the build. You can override this by setting the `KO_DEFAULTBASEIMAGE` environment variable to a different base image.

Before building the container image, you'll need to set up the environment variable `KO_DOCKER_REPO`. This environment variable identifies where ko should push images that it builds. This is usually a remote registry like the GitHub Container registry or Docker Hub, but you can publish to your local machine for testing and demonstration purposes.

Run the following command to set the `KO_DOCKER_REPO` environment variable to your local machine:

```shell
export KO_DOCKER_REPO=ko.local
```

Next, ensuring that you are in the same directory as your `main.go` file, run the following command to build the container with ko:

```shell
ko build .
```

Once you run this command, you'll receive output similar to the following.

```
2024/12/06 13:03:14 Using base cgr.dev/chainguard/static:latest@sha256:5ff428f8a48241b93a4174dbbc135a4ffb2381a9e10bdbbc5b9db145645886d5 for go-digester
2024/12/06 13:03:15 git doesn't contain any tags. Tag info will not be available
2024/12/06 13:03:15 Building go-digester for linux/amd64
2024/12/06 13:03:20 Loading ko.local/go-digester-edc0ed689c7fb820a565f76425bed013:0914a85d803988ab10964323c0cd7b4bf89aed2603f6e8e276f798491c731336
2024/12/06 13:03:20 Loaded ko.local/go-digester-edc0ed689c7fb820a565f76425bed013:0914a85d803988ab10964323c0cd7b4bf89aed2603f6e8e276f798491c731336
2024/12/06 13:03:20 Adding tag latest
2024/12/06 13:03:20 Added tag latest
ko.local/go-digester-edc0ed689c7fb820a565f76425bed013:0914a85d803988ab10964323c0cd7b4bf89aed2603f6e8e276f798491c731336
```

At this point, your container is built. Because the output of `ko build` is an image reference, you can pass it to other tools like Docker. You can learn more about [deployment with ko](https://ko.build/deployment/) and [Kubernetes integration](https://ko.build/features/k8s/) by reading the respective documentation on the official site.

We'll demonstrate running the above built container with Docker.

> **Note**: To follow along, be sure that you copy and paste the last line of output from your last command that begins `ko.local/go-digester-...`

```shell
docker run --rm ko.local/go-digester-edc0ed689c7fb820a565f76425bed013:0914a85d803988ab10964323c0cd7b4bf89aed2603f6e8e276f798491c731336
```
Here, you'll expect to receive the same output as before that shows the digest of the Go container.

```
The latest digest of the go Chainguard Container is sha256:86178b42db2e32763304e37f4cf3c6ec25b7bb83660dcb985ab603e3726a65a6
```

You can also pass in an optional argument to specify which Chainguard Container to pull the latest digest from:

```shell
docker run --rm ko.local/go-digester-edc0ed689c7fb820a565f76425bed013:0914a85d803988ab10964323c0cd7b4bf89aed2603f6e8e276f798491c731336 mariadb
```

```
The latest digest of the mariadb Chainguard Container is sha256:6ba5d792d463b69f93e8d99541384d11b0f9b274e93efdeb91497f8f0aae03d1
```

## Advanced Usage

{{< blurb/images-advanced image="Go" >}}
