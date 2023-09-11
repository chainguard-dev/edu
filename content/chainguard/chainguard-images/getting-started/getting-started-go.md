---
title: "Getting Started with the Go Chainguard Image"
type: "article"
description: "Tutorial on the distroless Go Chainguard Image"
date: 2023-02-28T11:07:52+02:00
lastmod: 2023-02-28T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "tutorials"
weight: 610
toc: true
---

The Go images based on Wolfi and maintained by Chainguard provide distroless images that are suitable for building Go workloads.

Chainguard offers a minimal runtime image designed for running Go workloads, and a development image that contains a shell and the standard Go build tooling.

We'll demonstrate two ways that you can build the Go image. The [first example](#example-1-minimal-go-chainguard-image-built-with-ko) will show how to build the Go Chainguard Image with [ko](https://ko.build/). ko enables you to build images from Go programs and push them to container registries without requiring a Dockerfile. The [second example](#example-2--multistage-docker-build-for-go-chainguard-image) will show how to create a [multi-stage Docker build](https://docs.docker.com/build/building/multi-stage/) that uses the [glibc-dynamic runtime image](/chainguard/chainguard-images/reference/glibc-dynamic/overview/) along with the Go Chainguard Image.

If you would like to follow along with both examples, you'll need both ko and Docker installed, which you can achieve by following the official installation guides for your setup:

* [ko installation](https://ko.build/install/)
* [Docker installation](https://docs.docker.com/get-docker/)

Before building the image, follow the [prerequisite step](#prerequisite--setting-up-a-demo-application-in-go) below to set up a demo application.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Prerequisite — Setting up a Demo Application in Go

We'll start by creating a basic command-line Go application to serve as a demo. This image will use the `go-containerregistry` library to print out the digest of the latest Go container image.

First, create a directory for your app. You can use any meaningful name and path for you, our example will use `go-digester/`.

```shell
mkdir ~/go-digester/ && cd $_
```

Next, initialize your app by creating a new module and installing dependencies.

```shell
go mod init go-digester
go mod tidy
go get github.com/google/go-containerregistry
go get github.com/google/go-containerregistry/pkg/v1/remote
go get github.com/google/go-containerregistry/pkg/name
```

With these in place, create a file to serve as the entrypoint. We’ll use `main.go`. You can edit this file in whatever code editor you would like. We'll use Nano as an example.

```shell
nano main.go
```

The following Go code defines a light CLI app that prints the digest of the latest Go Chainguard Image:

```go
package main

import (
	"fmt"

	"github.com/google/go-containerregistry/pkg/name"
	"github.com/google/go-containerregistry/pkg/v1/remote"
)

func main() {
	image := "cgr.dev/chainguard/go"
	ref, err := name.ParseReference(image)
	if err != nil {
		panic(err)
	}
	desc, err := remote.Get(ref)
	if err != nil {
		panic(err)
	}
	fmt.Printf("The digest of %s is %s\n", image, desc.Digest)
}
```

Save and close the file. Then, you can run the code with the `go` command to be sure you are satisfied with the functionality.

```shell
go run .
```

The output should be the printed digest of the latest Go Chainguard Image.

```
The digest of cgr.dev/chainguard/go is sha256:d4a845840e227b5454b67d00ee6ccdaaf2954eab88f47fa9ecac946011513db0
```

With the program running as expected, you're ready to move onto either or both examples of building the image.

## Example 1 — Minimal Go Chainguard Image Built with ko

In this example, we'll build a distroless Go Chainguard Image with ko from the demo app we created in the [prerequisite step](#prerequisite--setting-up-a-demo-application-in-go).

ko offers fast container image builds for Go applications. It builds images by executing `go build` on your local machine, and because of this, you are not required to have Docker installed to build the image. Additionally, ko produces [SBOMs](/open-source/sbom/what-is-an-sbom/) by default, supporting a holistic approach to software security.

First, you'll need to set up the environment variable (`KO_DOCKER_REPO`) that identifies where ko should push images that it builds. This is usually a remote registry like GitHub Container registry or Docker Hub, but you can publish to your local machine for testing and demonstration purposes.

```shell
export KO_DOCKER_REPO=ko.local
```

Next, ensuring that you are in the same directory as your `main.go` file, build the image with ko:

```shell
ko build .
```

Once you run this command, you'll receive output similar to the following.

```
2023/03/05 17:44:03 Using base distroless.dev/static:latest@sha256:4a5fda9b2aa55b49971d220cc4ba3d73998084e37e437f23721836112015c2d4 for go-digester
...
2023/03/05 17:44:05 Added tag latest
ko.local/go-digester-edc0ed689c7fb820a565f76425bed013:33523bfd5a136392f92905ffe5a076681baac3060d48c2b9ff2f787a7cc90dfd
```

At this point, your image is built. Because the output of `ko build` is an image reference, you can pass it to other tools like Docker. You can learn more about [deployment with ko](https://ko.build/deployment/) and [Kubernetes integration](https://ko.build/features/k8s/) by reading the respective documentation on the official site.

We'll demonstrate running the above built image with Docker.

> **Note**: To follow along, be sure that you copy and paste the last line of output from your last command that begins `ko.local/go-digester-...`

```shell
docker run --rm ko.local/go-digester-edc0ed689c7fb820a565f76425bed013:33523bfd5a136392f92905ffe5a076681baac3060d48c2b9ff2f787a7cc90dfd
```

Here, you'll expect to receive the same output as before that shows the digest of the image.

```
The digest of cgr.dev/chainguard/go is sha256:d4a845840e227b5454b67d00ee6ccdaaf2954eab88f47fa9ecac946011513db0
```

Now that you have built the Go Chainguard Image with ko, you can continue onto [advanced usage](#advanced-usage), or you can complete the multistage setup in [Example 2](#example-2--multistage-docker-build-for-go-chainguard-image).

## Example 2 — Multistage Docker Build for Go Chainguard Image

Because Go applications are compiled and the toolchain is not typically required in a runtime image, we suggest the usage of a [multi-stage Docker build](https://docs.docker.com/build/building/multi-stage/) that uses the [glibc-dynamic runtime image](/chainguard/chainguard-images/reference/glibc-dynamic/overview/). In some cases, the [static image](/chainguard/chainguard-images/reference/static/overview/) may be used as well for an even smaller image, but extra care must be taken to ensure the Go binary is statically-compiled.

For this multi-stage build, we'll use two `FROM` lines in our Dockerfile. To create this Dockerfile, you can use any code editor of your choice, we'll use Nano for demonstation purposes.

```shell
nano Dockerfile
```

The following Dockerfile will:

1. Start a build stage based on the `go:latest` image;
2. Declare the working directory;
3. Copy the script and the text file that's being read;
4. Set up the application as entry point for this image.

```Dockerfile
FROM cgr.dev/chainguard/go AS builder
COPY ../reference/go /app
RUN cd /app && go build -o go-digester .

FROM cgr.dev/chainguard/glibc-dynamic
COPY --from=builder /app/go-digester /usr/bin/
CMD ["/usr/bin/go-digester"]
```

Save the file when you're finished.

You can now build the image with Docker. If you receive an error, try again with `sudo`.

```shell
docker build . -t digester
```

Once the build is finished, run the image.

```shell
docker run --rm digester
```

You should get output similar to what you got before.

```
The digest of cgr.dev/chainguard/go is sha256:d4a845840e227b5454b67d00ee6ccdaaf2954eab88f47fa9ecac946011513db0
```

You have successfully completed the multi-stage Go Chainguard Image. At this point, you can continue to [advanced usage](#advanced-usage).

## Advanced Usage

{{< blurb/images-advanced image="Go" >}}
