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
    parent: "go-guides"
weight: 610
toc: true
---

The Go images based on Wolfi and maintained by Chainguard provide distroless images that are suitable for building Go workloads.

Chainguard offers a minimal runtime image designed for running Go workloads, and a development image that contains a shell and the standard Go build tooling. Because Go applications are compiled and the toolchain is not typically required in a runtime image, we suggest the usage of a [multi-stage Docker build](https://docs.docker.com/build/building/multi-stage/) that uses the [glibc-dynamic runtime image](chainguard/chainguard-images/reference/glibc-dynamic/overview/).
In some cases the [static image](chainguard/chainguard-images/reference/static/overview/) may be used as well for an even smaller image, but extra care must be taken to ensure the Go binary is statically-compiled.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Example 1 — Minimal Go Chainguard Image

In this example, we'll build and run a distroless Go Chainguard Image in a multi-stage build process. We'll first make a demonstration app and then build and run it.

### Step 1: Setting up a Demo Application

We'll start by creating a basic command-line Go application to serve as a demo. This image will use the `go-containerregistry` library to print out the digest of the latest Go container image.

First, create a directory for your app. You can use any meaningful name and path for you, our example will use `octo-facts/`.

```shell
mkdir ~/go-digester/ && cd $_
```

Create a new module and file to serve as the entrypoint. We’ll use `main.go`. You can edit this file in whatever code editor you would like. We'll use Nano as an example.

```shell
go mod init go-digester
go get github.com/google/go-containerregistry
go mod tidy
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

At this point, you can run the code and be sure you are satisfied with the functionality.

```shell
% go run .
The digest of cgr.dev/chainguard/go is sha256:b6fbf550fa85b452510801fc344e44e92037f9b9b98175f1e126b6c6d168624b
```

### Step 2: Creating the Dockerfile 

For this multi-stage build, we'll only two `FROM` lines in our Dockerfile.

We'll begin by creating a Dockerfile. Again, you can use any code editor of your choice, we'll use Nano for demonstation purposes. 

```shell
nano Dockerfile
```

The following Dockerfile will:

1. Start a build stage based on the `python:latest` image;
2. Declare the working directory;
3. Copy the script and the text file that's being read;
4. Set up the application as entry point for this image.

```Dockerfile
FROM cgr.dev/chainguard/go AS builder
COPY . /app
RUN cd /app && go build -o go-digester .

FROM cgr.dev/chainguard/glibc-dynamic
COPY --from=builder /app/go-digester /usr/bin/
CMD ["/usr/bin/go-digester"]
```

Save the file when you're finished.

You can now build the image. If you receive an error, try again with `sudo`.

```shell
docker build . -t digester
```

Once the build is finished, run the image.

```shell
docker run --rm digester
The digest of cgr.dev/chainguard/go is sha256:d4a845840e227b5454b67d00ee6ccdaaf2954eab88f47fa9ecac946011513db0
```

And you should get output similar to what you got before.

You have successfully completed the multi-stage Go Chainguard Image. At this point, you can continue to [advanced usage](#advanced-usage).

## Advanced Usage

{{< blurb/images-advanced image="Go" >}}
