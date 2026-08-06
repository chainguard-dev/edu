---
title: "Quickstart for Chainguard Containers"
linktitle: "Quickstart"
lead: "Pull a Free Chainguard Container, build an application on top of it, and verify what you pulled."
description: "An end-to-end walkthrough of Chainguard Containers: pull a Free container, run a small Node.js application on it, and verify the image's signature and SBOM."
type: "article"
date: 2026-08-05T00:00:00+00:00
lastmod: 2026-08-05T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Getting Started"]
images: []
weight: 012
toc: true
---

This quickstart covers one full cycle of working with a [Chainguard Container](/chainguard/chainguard-images/overview/): pull an image from Chainguard's registry, run your own code on it, and verify where it came from. The example uses the Node container, but the same workflow applies to every image in the [Chainguard Containers Directory](https://images.chainguard.dev/).

These steps link to reference documentation instead of explaining each concept in place. Follow the links whenever you want the full picture.

## Prerequisites

To follow this quickstart, you need:

* [Docker](https://docs.docker.com/engine/install/) or another OCI-compatible container runtime.
* [Cosign](/open-source/sigstore/cosign/how-to-install-cosign/) and [jq](https://jqlang.github.io/jq/download/), which you use in Step 4 to verify a container image.

You don't need a Chainguard account. Every image in this guide is a [Free Container](/chainguard/chainguard-images/about/images-categories/#free-containers): publicly available, with no authentication required. Production Containers, which add version-specific tags and patch SLAs, require [authenticating to the registry](/chainguard/chainguard-images/chainguard-registry/authenticating/).

## Step 1: Pull and run a container

Pull the Node container from `cgr.dev`, Chainguard's registry:

```shell
docker pull cgr.dev/chainguard/node:latest
```

Chainguard publishes two tags for Free Containers — `latest` and `latest-dev` — and both point at the most recent build of the image.

The image's entrypoint is `node`, so any arguments you pass go to the Node binary. Run the container, passing an argument to check the Node version:

```shell
docker run --rm cgr.dev/chainguard/node:latest --version
```

```output
v26.6.0
```

Your output may show a different version. Chainguard rebuilds its containers as upstream releases and package updates land, and the `latest` tag follows the newest build.

## Step 2: Build your application on the container

Create a directory for a demo application:

```shell
mkdir ~/hello-chainguard && cd ~/hello-chainguard
```

Create a file named `server.js` to hold an example JavaScript application. It uses only the Node standard library, so the application has no dependencies to install:

```shell
cat > server.js <<EOF
const http = require("node:http");

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({
    message: "Hello from a Chainguard Container",
    node: process.version,
    uid: process.getuid(),
  }));
});

server.listen(8080, () => console.log("Listening on port 8080"));
EOF
```

Then create a `Dockerfile` in the same directory:

```shell
cat > Dockerfile <<EOF
FROM cgr.dev/chainguard/node:latest

WORKDIR /app
COPY --chown=node:node server.js ./

EXPOSE 8080
CMD ["server.js"]
EOF
```

Chainguard Containers run as a nonroot user by default — `node` in this image — so `COPY --chown=node:node` gives the application access to its own files without switching to root. Because the entrypoint is already `node`, `CMD` only needs to name the script.

Build the image:

```shell
docker build . --pull -t hello-chainguard
```

Using the `hello-chainguard` image, start a container in the background:

```shell
docker run -d --name hello-cg -p 8080:8080 hello-chainguard
```

Then send it a request:

```shell
curl localhost:8080
```

```output
{"message":"Hello from a Chainguard Container","node":"v26.6.0","uid":65532}
```

The `uid` in the response is `65532`, confirming that the application runs unprivileged. Stop the container when you're done:

```shell
docker rm -f hello-cg
```

## Step 3: Use a development variant when you need extra tooling

Chainguard's standard containers follow a [distroless](/chainguard/chainguard-images/about/getting-started-distroless/) philosophy: they carry only what the container needs to function. For example, the Node container has no system package manager:

```shell
docker run --rm --entrypoint sh cgr.dev/chainguard/node:latest -c "apk --version"
```

```output
sh: apk: not found
```

The development variant, tagged `latest-dev`, adds `apk` and other utilities for building, testing, and debugging:

```shell
docker run --rm --entrypoint sh cgr.dev/chainguard/node:latest-dev -c "apk --version"
```

```output
apk-tools 2.14.10, compiled for x86_64.
```

To keep a small attack surface in production, install dependencies and compile artifacts in the development variant, then copy the results into the standard variant with a multi-stage build. Refer to [Development and production container variants](/chainguard/chainguard-images/about/differences-development-production/) for how the variants differ, and to [porting a sample application](/get-started/migration/porting-apps-to-chainguard/) for a multi-stage example.

## Step 4: Verify the container and inspect its SBOM

Chainguard signs every container it builds, along with the attestations that describe it. Check the signature on the image you pulled:

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/node | jq
```

Cosign confirms that the signature exists in the transparency log and that a trusted certificate authority issued the signing certificate, then prints the signature payload.

Every container also ships with a signed SBOM. Download the SPDX document to see each package in the image:

```shell
cosign download attestation \
  --platform linux/amd64 \
  --predicate-type https://spdx.dev/Document \
  cgr.dev/chainguard/node | jq -r '.payload' | base64 -d | jq -r '.predicate'
```

For the rest of the available attestations and the commands that verify them, refer to [verifying containers and metadata signatures](/chainguard/chainguard-images/how-to-use/verifying-chainguard-images-and-metadata-signatures-with-cosign/) and [retrieving SBOMs and attestations](/chainguard/chainguard-images/how-to-use/retrieve-image-sboms/).

## Next steps

* Work through a guide for your own stack: [nginx](/chainguard/chainguard-images/getting-started/nginx/), [PostgreSQL](/chainguard/chainguard-images/getting-started/postgres/), [Python](/chainguard/chainguard-images/getting-started/python/), [Go](/chainguard/chainguard-images/getting-started/go/), or [any other language or service](/chainguard/chainguard-images/getting-started/).
* Move an existing workload over with the [migration guides](/get-started/migration/).
* Learn what a Chainguard Container includes and who patches what in the [shared responsibility model](/chainguard/chainguard-images/about/shared-responsibility-model/) and the [container categories reference](/chainguard/chainguard-images/about/images-categories/).
* Understand why these images carry so few vulnerabilities in [Chainguard's low-to-no CVE commitment](/chainguard/chainguard-images/about/zerocve/).
