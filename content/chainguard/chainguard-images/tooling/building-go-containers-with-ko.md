---
title: "Build Go Containers with Ko"
linktitle: "Ko"
type: "article"
description: "In this tutorial, you'll learn how to build minimal Go Containers using Ko and Chainguard base images"
date: 2025-09-11T08:49:31+00:00
lastmod: 2025-09-11T08:49:31+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 001
toc: true
---
[Ko](https://ko.build/) is a tool for building Go applications into container images without using Dockerfiles. When combined with Chainguard's minimal containers, Ko creates smaller and more secure container runtimes with only your application and its essential dependencies.

This tutorial will guide you through installing Ko and using it to containerize Go applications with Chainguard Containers. By the end of this tutorial, you'll understand how to build, configure, and deploy secure, custom containers with your Go-based application using Ko's streamlined workflow.

## Prerequisites

To follow along with this tutorial, you will need:

- A working Go development environment to set up the demo
- Docker or another OCI-compatible container runtime installed and running, so that you can test the resulting image
- Ko installed following the [official installation instructions](https://ko.build/install/)

Once you're finished installing Ko, check that it is functional by running:

```shell
ko version
```

You should get output similar to the following:

```shell
v0.18.0
```

## Step 1 — Creating a Sample Go Application

To demonstrate Ko's capabilities, we'll create a simple Go web server that runs a minimal web application. Later on, you’ll be able to containerize it.

Create a new directory for your project:

```shell
mkdir ko-demo && cd ko-demo
```

Initialize a new Go module:

```shell
go mod init ko-demo
```

Use the following command to create a `main.go` file containing the logic for a basic web server application:

```shell
cat > main.go <<EOF
package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello from Ko! Running on port %s\n", port)
    })

    http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        fmt.Fprint(w, "OK")
    })

    log.Printf("Server starting on port %s", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}
EOF
```

This creates a web server with two endpoints: a root endpoint (`/`) that returns a greeting message and a health check endpoint (`/health`) to check the status of the server. The server listens on port `8080` by default but can be configured using the `PORT` environment variable.

Test that your application works locally:

```shell
go run main.go
```

Your application should start and display output similar to:

```output
2025/08/04 15:35:45 Server starting on port 8080
```

Open another terminal and test the endpoint:

```shell
curl http://localhost:8080
```

You should receive the following response:

```output
Hello from Ko! Running on port 8080
```

Stop the application by pressing `CTRL+C` in the terminal where it's running.

## Step 2 — (Re) Authenticating to the Chainguard Registry

In case you have previously authenticated to the Chainguard registry via `chainctl`, you might need to refresh your token by pulling an image and reauthenticating with your OIDC provider of choice. Run the following command for that:

```shell
docker pull cgr.dev/chainguard/static
```

Once you’re able to pull images without being prompted to authenticate, you can proceed to the next step.

## Step 3 — Building Your First Container with Ko

To get started, you'll build your application locally using Ko’s default configuration. Ko supports cross-compilation to other CPU architectures and operating systems via the `--platform` flag, so it can build container images for any platform that is supported by the base image. Chainguard Containers are available for both `amd64` and `arm64` architectures.

To build the image locally using default settings, run:

```shell
ko build --local .
```

If you're on macOS, you may want to include the `--platform=linux/arm64` flag to your command, or use `--platform=all` to build all supported platforms.

```shell
ko build --local --platform=linux/arm64 .
```

The `--local` flag tells Ko to build the image and load it into your local Docker daemon instead of pushing it to a registry. The output includes information such as the image name and tags added to this build:

```output
...
2025/08/04 15:53:05 Building ko-demo for linux/amd64
2025/08/04 15:53:11 Loading ko.local/ko-demo-f2e1cf7eebaa497931a6a58522f6d83f:2f27fb1252ce004cf29fa713e8c7d3bce1c2e95352f3ddb33fb72690431e73fd
2025/08/04 15:53:12 Loaded ko.local/ko-demo-f2e1cf7eebaa497931a6a58522f6d83f:2f27fb1252ce004cf29fa713e8c7d3bce1c2e95352f3ddb33fb72690431e73fd
2025/08/04 15:53:12 Adding tag latest
2025/08/04 15:53:12 Added tag latest
ko.local/ko-demo-f2e1cf7eebaa497931a6a58522f6d83f:2f27fb1252ce004cf29fa713e8c7d3bce1c2e95352f3ddb33fb72690431e73fd
```

By default, Ko creates a unique image name for the project based on the import path, and a unique tag name that identifies this specific build. If you run the command again multiple times, you’ll get the same combination of image name \+ tag. The tag will only change if there are changes in the build, such as  updates in the base image, or updates to dependencies. This feature facilitates reproducible builds.

You can change this behavior at runtime with the flags `--base-import-paths` to omit the hash appended to the image name, and `--bare` to use only the base registry name. For example, the following command will rebuild the image using only the path information for the image name, while still creating a unique tag in addition to `latest`:

```shell
ko build --local . --base-import-paths
```

```output
...
2025/09/02 12:57:00 Adding tag latest
2025/09/02 12:57:00 Added tag latest
ko.local/ko-demo:d403c3992168125d8dbb960f6c47783dfb7d20f660791d16334310e9dee26b9e
```

You can use the `docker image list` command to check the images and tags you created with Ko:

```shell
docker image list | grep ko
```

```output
ko.local/ko-demo                  d403c3992168125d8dbb960f6c47783dfb7d20f660791d16334310e9dee26b9e   9c710b8a98a2   4 weeks ago     9.07MB
ko.local/ko-demo                  latest                                                             9c710b8a98a2   4 weeks ago     9.07MB
ko.local/ko-demo-f2e1cf7eebaa497931a6a58522f6d83f   d403c3992168125d8dbb960f6c47783dfb7d20f660791d16334310e9dee26b9e   9c710b8a98a2   4 weeks ago     9.07MB
ko.local/ko-demo-f2e1cf7eebaa497931a6a58522f6d83f   latest                                           86528e034ac8   4 weeks ago     9.07MB
```

It’s worth noting that the resulting image is very minimal, with less than 10MB in size.

Now you can test your containerized application. The following command runs the image using a port mapping to redirect requests on port `8080` in the host to the same port inside the container:

```shell
docker run -p 8080:8080 ko.local/ko-demo
```

Your application should start inside the container. Test it with curl in another terminal:

```shell
curl http://localhost:8080
```

You should receive the same response as before. Stop the container by pressing `CTRL+C`.

## Step 4 — Pushing Images to a Remote Registry

Ko can build and push images to a remote registry with a single command. To push images, you’ll need to set up the `KO_DOCKER_REPO` environment variable with your preferred push registry. The value can be either your own registry URL (such as `ghcr.io/my-org/my-repo`) or your Docker username, in case you are using the Docker Hub registry.

For example, the following will set up Ko to push to a Docker Hub registry under the `linky` user:

```shell
export KO_DOCKER_REPO=linky
```

To build the image and push it to the remote registry, run:

```shell
ko build --base-import-paths
```

The image will be built and pushed to the remote registry automatically, which you can confirm from the output:

```output
2025/09/15 13:09:10 Using base cgr.dev/chainguard/static:latest@sha256:b2e1c3d3627093e54f6805823e73edd17ab93d6c7202e672988080c863e0412b for ko-demo
2025/09/15 13:09:11 current folder is not a git repository. Git info will not be available
2025/09/15 13:09:11 Building ko-demo for linux/amd64
2025/09/15 13:09:11 Publishing linky/ko-demo:latest
2025/09/15 13:09:14 pushed blob: sha256:8cf6f1c6fcba0c40fba9e61b39672b1cd91626c7c6fd78d3ce1679dfae2b8b1c
2025/09/15 13:09:14 pushed blob: sha256:8d9d552233adea41e9d0d6b73cf2847b736ac13bd9a4b8df39836193652c6500
2025/09/15 13:09:15 pushed blob: sha256:250c06f7c38e52dc77e5c7586c3e40280dc7ff9bb9007c396e06d96736cf8542
2025/09/15 13:09:15 pushed blob: sha256:7493e3cb9c5dc55615efb3f5298804d5817c43127a5e82bc7d6d6b5edf472912
2025/09/15 13:09:16 pushed blob: sha256:4fcce664a6320a086990883b95e0377ca0e410844c7fa93a8ca02869aac6dd12
2025/09/15 13:09:16 pushed blob: sha256:59b34ce0532f011950c3e51cd19f924aaa4dc9fdb722448610a0e3e47ea1138b
2025/09/15 13:09:17 index.docker.io/linky/ko-demo:sha256-6ce1b8b932e5249ce5aaaee33ceaa491ef5c83ef3a2f44dc51700113806f46c6.sbom: digest: sha256:a5dd8c1ad4a415db5944f848427271a4bb87b475cd04cd31eb17a6bfd4dd0b5b size: 373
2025/09/15 13:09:17 Published SBOM index.docker.io/linky/ko-demo:sha256-6ce1b8b932e5249ce5aaaee33ceaa491ef5c83ef3a2f44dc51700113806f46c6.sbom
2025/09/15 13:09:17 linky/ko-demo:latest: digest: sha256:6ce1b8b932e5249ce5aaaee33ceaa491ef5c83ef3a2f44dc51700113806f46c6 size: 1336
2025/09/15 13:09:17 Published linky/ko-demo@sha256:6ce1b8b932e5249ce5aaaee33ceaa491ef5c83ef3a2f44dc51700113806f46c6
linky/ko-demo@sha256:6ce1b8b932e5249ce5aaaee33ceaa491ef5c83ef3a2f44dc51700113806f46c6
```

You’ll notice that Ko also pushes an SBOM to the remote registry.

To verify that the image is available in the remote registry, you can pull it to your local machine with a command similar to this, using the remote registry’s URL and the image name:

```shell
docker pull linky/ko-demo
```

Remember to replace `linky/ko-demo` with your own unique registry address and image name.

## Next Steps

You now have a foundation for using Ko to build secure, minimal images for your Go applications. To continue learning about Ko and container security, consider exploring:

- [Ko's official documentation](https://ko.build/) for advanced configuration options
- [Chainguard's image catalog](https://images.chainguard.dev/) to discover specialized base images for different use cases
- [Container signing with Cosign](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-install-cosign/) to add cryptographic signatures to your images

Ko's declarative approach to container building combined with Chainguard's security-focused base images provides a powerful toolkit for modern Go application deployment.
