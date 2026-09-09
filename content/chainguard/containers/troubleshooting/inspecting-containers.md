---
title: "Inspecting Chainguard Containers"
linktitle: "Inspecting containers"
description: "How to identify exactly which container build you have with a digest, and how to read the software versions inside it from the container's SBOM"
type: "article"
date: 2023-07-07T15:21:01+00:00
lastmod: 2026-09-08T00:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
weight: 020
toc: true
aliases:
- /chainguard/chainguard-images/videos/container-image-digests/
- /chainguard/chainguard-images/how-to-use/container-image-digests/
- /chainguard/containers/videos/container-image-digests/
- /chainguard/containers/how-to-use/container-image-digests/
- /chainguard/containers/troubleshooting/container-image-digests/
- /chainguard/chainguard-images/videos/version-info-chainguard-images/
- /chainguard/chainguard-images/how-to-use/version-info-chainguard-images/
- /chainguard/containers/videos/version-info-chainguard-images/
- /chainguard/containers/how-to-use/version-info-chainguard-images/
- /chainguard/containers/troubleshooting/version-info-chainguard-images/
---

Two questions come up repeatedly once you're running Chainguard Containers: which exact build is this, and what software versions are inside it? A digest answers the first. The container's SBOM answers the second.

The following examples pull from `cgr.dev/chainguard/`, the namespace that holds Chainguard's Free containers, so they run as written. If you pull from your organization's own registry, substitute `cgr.dev/<organization>/`.

## Identify a build by its digest

A digest is a content-based hash of a container image. No two images share one, so pulling by digest returns the same image every time.

Tags don't behave that way. A tag such as `latest`, or a version tag like `3.0`, points at the newest build in its version stream, and Chainguard moves it as it publishes rebuilds. If you pull the same tag twice on two different days, you may end up pulling two different images, making it difficult to reproduce a build later. [Chainguard Containers product release lifecycle](/chainguard/containers/concepts/lifecycle-and-eol/versions/) explains how those tags float.

### Retrieve the digest of a container

`docker pull` reports the digest of whatever it pulled:

```sh
docker pull cgr.dev/chainguard/node
```

```output
. . .

Digest: sha256:ede7ef4ca485553f5313f7a02ad3537db1fe337079fc7cfb879f44cf709326db
Status: Downloaded newer image for cgr.dev/chainguard/node:latest
cgr.dev/chainguard/node:latest
```

That digest refers to the image *index*, which lists one image per platform rather than pointing at a single image. In most cases the index is what you want to reference, since it lets the same digest work on every architecture you deploy to.

To find out what the index holds, inspect it:

```sh
docker manifest inspect cgr.dev/chainguard/node@sha256:ede7ef4ca485553f5313f7a02ad3537db1fe337079fc7cfb879f44cf709326db | jq
```

The output lists a digest for each platform in the index, typically `linux/amd64` and `linux/arm64`. You can reference one of those directly, but an image pinned to a platform-specific digest only runs on that platform, so be deliberate about it.

[`crane`](https://github.com/google/go-containerregistry/tree/main/cmd/crane) prints the digest alone with nothing to parse, making it useful for scripts:

```sh
crane digest --full-ref cgr.dev/chainguard/node:latest
```

Add `--platform` to get the digest for one platform:

```sh
crane digest --full-ref --platform linux/arm64 cgr.dev/chainguard/node:latest
```

### Pin a reference to a digest

Append the digest to the reference to pull one specific build:

```sh
docker pull cgr.dev/chainguard/node:latest@sha256:ede7ef4ca485553f5313f7a02ad3537db1fe337079fc7cfb879f44cf709326db
```

Registries ignore the tag when a reference carries a digest, which frees the tag to carry a version hint for whoever reads the file next:

```
cgr.dev/chainguard/go:1.22@sha256:7e60584b9ae1eec6ddc6bc72161f4712bcca066d5b1f511d740bcc0f65b05949
```

Chainguard recommends that form, and both [Dependabot](/chainguard/containers/security-and-compliance/updating-containers/dependabot/) and [Renovate](/chainguard/containers/security-and-compliance/updating-containers/renovate/) update the tag and the digest together when they find it.

While you *can* use digests on the command line, they're much more commonly found in configuration files, such as a Dockerfile, a Compose file, or a Kubernetes manifest:

```Dockerfile
FROM cgr.dev/chainguard/go:latest@sha256:7e60584b9ae1eec6ddc6bc72161f4712bcca066d5b1f511d740bcc0f65b05949 AS build

WORKDIR /src
RUN CGO_ENABLED=0 go build -o /bin/server ./src


FROM cgr.dev/chainguard/static:latest AS prod

COPY --from=build /bin/server /bin/
EXPOSE 8000
ENTRYPOINT [ "/bin/server" ]
```

Every run of this Dockerfile build uses the same Go compiler, so a build that works today works the same way next month, even if Chainguard has since rebuilt the container image.

Note the tradeoff: a pinned digest stops receiving patches, because the whole point is that it never changes. Pair digest pinning with something that updates the pin, such as [Digestabot](/chainguard/containers/security-and-compliance/updating-containers/digestabot/), and refer to [Considerations for image updates](/chainguard/containers/security-and-compliance/updating-containers/considerations-for-image-updates/) for how to think about the schedule.

The following video covers the same ground, including what the index looks like from the inside:

{{< youtube xYlLfjgG64E >}}

## Read software versions from a container

Every Chainguard Container records the version of each package it installs.

One way to find this is to list `/var/lib/db/sbom` inside the container. It holds one SPDX document per installed package, and the filenames carry the versions:

```sh
docker run cgr.dev/chainguard/wolfi-base ls /var/lib/db/sbom
```

```output
apk-tools-2.14.10-r14.spdx.json
busybox-1.38.0-r2.spdx.json
ca-certificates-bundle-20260611-r1.spdx.json
glibc-2.44-2.44-r5.spdx.json
. . .
```

That works because `wolfi-base` includes a shell, and with it `ls`. Most Chainguard Containers are distroless and include neither. For those, run the `-dev` variant, which does have a shell:

```sh
docker run --entrypoint /bin/sh cgr.dev/chainguard/python:latest-dev -c "ls /var/lib/db/sbom"
```

Or copy the directory out of the distroless container without running anything in it:

```sh
id=$(docker create cgr.dev/chainguard/python)
docker cp "$id":/var/lib/db/sbom ./sbom
docker rm "$id"
```

Chainguard also publishes a signed, image-level SBOM for every build, which you can retrieve without pulling the container. Refer to [How to retrieve SBOMs and attestations for Chainguard Containers](/chainguard/containers/security-and-compliance/retrieve-image-sboms/) for details.

The following video walks through both routes:

{{< youtube K60-jhVf2I4 >}}

## Related reading

* [Troubleshoot container and version availability](/chainguard/containers/troubleshooting/container-version-troubleshooting/) — when the container or version you need isn't there to inspect.
* [Unique tags](/chainguard/containers/reference/unique-tags/) — an alternative to digests for teams whose workflows require a stable tag.
* [Debugging distroless container images](/chainguard/containers/troubleshooting/debugging-distroless-images/) — further techniques for looking inside a container with no shell.
