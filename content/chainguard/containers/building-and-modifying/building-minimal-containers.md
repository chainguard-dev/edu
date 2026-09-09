---
title: "Building minimal container images"
linktitle: "Building minimal containers"
description: "How to build minimal container images with multi-stage builds: the Chainguard static base for compiled binaries, and runtime images for languages like Java that need one"
type: "article"
date: 2023-08-30T15:21:01+00:00
lastmod: 2026-09-08T00:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
weight: 020
toc: true
aliases:
- /chainguard/chainguard-images/videos/static-base-image/
- /chainguard/chainguard-images/how-to-use/static-base-image/
- /chainguard/containers/videos/static-base-image/
- /chainguard/containers/how-to-use/static-base-image/
- /chainguard/containers/building-and-modifying/static-base-image/
- /chainguard/chainguard-images/videos/minimal-runtime-images/
- /chainguard/chainguard-images/how-to-use/minimal-runtime-images/
- /chainguard/containers/videos/minimal-runtime-images/
- /chainguard/containers/how-to-use/minimal-runtime-images/
- /chainguard/containers/building-and-modifying/minimal-runtime-images/
---

The less software a container image holds, the less there is to transfer, to maintain, and to attack. Chainguard's [distroless](/chainguard/containers/concepts/getting-started-distroless/) container images take that as far as it goes: no shell, no package manager, and only the libraries the application needs.

That raises a practical question: without a shell or a package manager, how do you get your application into the image? The answer is a multi-stage build. One stage compiles or assembles your application with all the tooling that requires, and the final stage copies the result into a minimal base. This page covers both shapes that build takes, depending on whether your application needs a language runtime once it's running.

## Applications that compile to a static binary

Go, Rust, and other toolchains that produce a statically linked binary can use the smallest base Chainguard publishes. Build in the language's own image, then copy the binary into `cgr.dev/chainguard/static`:

```Dockerfile
FROM cgr.dev/chainguard/go:latest AS build

COPY main.go /main.go
RUN CGO_ENABLED=0 go build -o /hello /main.go


FROM cgr.dev/chainguard/static:latest

COPY --from=build /hello /usr/local/bin/
CMD ["hello"]
```

`CGO_ENABLED=0` matters here. The `static` image ships no C library, so the binary must not link against one dynamically.

### Why not `scratch`?

For a binary that needs nothing else, the empty `scratch` image is smaller still, and it works. Most applications need more than that, though: TLS root certificates to make outbound HTTPS calls, time zone data to handle local times, and directories such as `/tmp`, `/etc`, and `/home` that libraries expect to find. The `static` image provides those and close to nothing else, which makes it a better default than `scratch` for a statically compiled application.

The following video walks through this build and compares the result against other minimal base images:

{{< youtube ZT6177U0fUM >}}

## Applications that need a language runtime

Java, Python, and .NET applications can't run on `static` or `scratch`, because the runtime files have to be in the container image. The build keeps the same two stages; only the final base changes, from an empty image to a runtime image.

For a Maven project, the build stage runs Maven against your sources to produce a JAR, and the final stage starts from `cgr.dev/chainguard/jre`, copies in that JAR, and sets an entrypoint that runs it. The build stage is large, since it holds the JDK, Maven, and everything Maven downloaded. The final image holds the JRE and your JAR, and like the `static` image it has no shell and no package manager.

You can find complete, working Dockerfiles for this example — a Spring Pet Clinic application built with the Chainguard Maven and JRE images — in the [minimal_images_for_language_runtimes](https://github.com/chainguard-dev/minimal_images_for_language_runtimes) repository.

### Choosing a runtime version

An untagged build uses the latest Maven and the latest JRE. That suits many projects, but sometimes you need to pin the Java version in both stages. The latest version of each container is free for everyone; tagged major and minor versions come with a subscription, as described in the [Containers overview](/chainguard/containers/overview/#production-and-free-containers).

If a tagged runtime isn't available to you, you can assemble your own runtime layer on `cgr.dev/chainguard/wolfi-base`, installing the JDK and Maven packages you need with `apk` and setting `JAVA_HOME` yourself. The minimal_images_for_language_runtimes repository includes this variant too. However, this method comes with two important tradeoffs:

* `wolfi-base` includes a shell and a package manager, so the image you finish with is no longer distroless.
* The JRE image ships locale data that `wolfi-base` leaves out. Java applications that depend on locale data need that package added back, which increases the image's size.

For a supported way to add packages to a distroless image without giving up its properties, check out [Custom Assembly](/chainguard/containers/custom-assembly/).

This video works through the Maven and JRE build, then the `wolfi-base` variant:

{{< youtube P7pmV-s5ZYY >}}

## Learn more

* Confirm what your finished image contains with [Inspecting Chainguard Containers](/chainguard/containers/troubleshooting/inspecting-containers/).
* If the application fails in the distroless stage but works in the build stage, refer to [Debugging distroless container images](/chainguard/containers/troubleshooting/debugging-distroless-images/).
* To add APK packages to a distroless variant directly, refer to [Installing APK packages in distroless variants](/chainguard/containers/building-and-modifying/install-apks-in-distroless-variants/).
