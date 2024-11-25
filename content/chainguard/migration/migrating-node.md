---
title: "Migrating to Node.js Chainguard Images"
linktitle: "Node Migration"
type: "article"
description: "Guidance on how to migrate Node.js Dockerfile workloads to use Chainguard Images"
date: 2024-05-09T15:56:52-07:00
lastmod: 2024-05-09T15:56:52-07:00
draft: false
tags: ["Images", "Product", "Conceptual"]
images: []
weight: 703
toc: true
---

Chainguard Images are built on top of [Wolfi](/open-source/wolfi/), a Linux _undistro_ designed
specifically for containers. Our Node.js images have a minimal design (sometimes known as
_distroless_) that ensures a smaller attack surface, which results in smaller images [with few to
zero](/chainguard/chainguard-images/vuln-comparison/node/) CVEs. Nightly builds deliver fresh images
whenever updated packages are available, which also helps to reduce the toil of manually patching
CVEs.

{{< details "What is Distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi OS?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

This article is intended as a guide to porting existing Dockerfiles for Node.js applications to a
Chainguard Images base.

## Chainguard Node.js Images

The [Node.js](https://images.chainguard.dev/directory/image/node/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=chainguard/migration/migrating-node) images come in two main
flavours; runtime images intended for production usage and builder images intended for use in the
build-step of multi-stage builds. The builder images are distinguished by the `-dev` suffix (e.g.,
`latest-dev`).

The production images are intentionally as minimal as possible. They have enough dependencies to run
a Node.js application but no more. There is no package manager or shell, which reduces the attack
surface of the image, but can also make it difficult to extend the image. The builder images have
more build tooling as well as a shell and package manager, allowing them to be easily extended. We
still aim to keep CVE counts as low as possible in the builder images and they can be used in
production if necessary (such as when the application requires extra system dependencies at
runtime), but we recommend using the builder image as the first step in a multi-stage build with the
production image as the base for the final image.

This extremely minimal approach to the runtime image is sometimes known as "distroless". For a
deeper exploration of distroless images and their differences from standard base images, refer to
the guide on [Getting Started with Distroless
images](/chainguard/chainguard-images/getting-started-distroless/).

## Migrating From Other Distributions

Dockerfiles will often contain commands specific to the Linux Distribution they are based on. Most
commonly this will be package installation instructions (e.g. `apt` vs `yum` vs `apk`) but also
differences in default shell (e.g. `bash` vs `ash`) and default utilities (e.g. `groupadd` vs `addgroup`).
Our high-level guide on [Migrating to Chainguard Images](/chainguard/migration/migrating-to-chainguard-images/)
contains details about distro-based migration and package compatibility when migrating from Debian,
Alpine, Ubuntu and Red Hat UBI base images.

## Installing Further Dependencies

Sometimes your applications will require further dependencies, either at build-time, runtime or
both. Wolfi has large number of software packages available, so you are likely to be able to
install common packages via `apk add`, but be aware that packages may be named differently than in
other distributions.

The easiest way to search for packages is via apk tools. For example:

```shell
docker run -it --rm cgr.dev/chainguard/wolfi-base
f273a9aa3242:/# apk update
fetch https://packages.wolfi.dev/os/aarch64/APKINDEX.tar.gz
 [https://packages.wolfi.dev/os]
OK: 53914 distinct packages available
f273a9aa3242:/# apk search cairo
cairo-1.18.0-r1
cairo-dev-1.18.0-r1
cairo-gobject-1.18.0-r1
cairo-static-1.18.0-r1
cairo-tools-1.18.0-r1
harfbuzz-8.4.0-r1
harfbuzz-dev-8.4.0-r1
pango-1.52.2-r1
pango-dev-1.52.2-r1
py3-cairo-1.26.0-r0
py3-cairo-dev-1.26.0-r0
```

These packages can then be easily added to your Dockerfile.
For more searching tips, check the [Searching for
Packages](/chainguard/migration/migrating-to-chainguard-images/#searching-for-packages)
section of our base migration guide.

## Differences to Docker Official Image

If you are migrating from the [Docker Official Image](https://hub.docker.com/_/node) there are a
few differences that are important to be aware of.

 - Our images run as the `node` user with UID 65532 by default. If you need elevated privileges
   for a task, such as installing a dependency, you will need to change to the root user. For
   example add a `USER root` statement into a Dockerfile. For security reasons you should make
   sure that the production application runs with a lower privilege user such as `node`.
 - `WORKDIR` is set to `/app` which is owned by the `node` user.
 - The Docker Official images have a "smart" entrypoint that interprets the CMD setting. So `docker
   run -it node` will launch the Node.js interpreter but `docker run -it node /bin/sh` will launch a
   shell. The latter does not work with Chainguard Images. In the non `-dev` images, there is no
   shell to launch, and in the `-dev` images you will need to change the entrypoint e.g. `docker run
   --entrypoint /bin/sh -it cgr.dev/chainguard/node`.
 - The image has a defined `NODE_PORT=3000` environment variable which can be used by applications
 - Our Node.js images include [dumb-init](https://github.com/Yelp/dumb-init) which can be used to
   wrap the Node process in order to handle signals properly and allow for graceful shutdown. You
   can use dumb-init by setting an entrypoint such as: `ENTRYPOINT ["/usr/bin/dumb-init", "--"]`
 - In general there are many fewer libraries and utilities in the Chainguard Image. You may find that
   your application has an unexpected dependency which needs to be added into the Chainguard Image.


## Migration Example

This section has a short example of migrating a Node.js application with a Dockerfile building on
`node:latest` to use the Chainguard Node.js Images. The code for [this example can be found on
GitHub](https://github.com/chainguard-dev/cg-images-node-migration).

Our starting Dockerfile uses the `node:latest` image from Docker Hub in a single-stage build:

```Docker
FROM node:latest

ENV NODE_ENV production

WORKDIR /usr/src/app

COPY package.json .
RUN npm install
USER node
COPY . .

EXPOSE 3000

CMD npm start
```

If you've cloned the GitHub repository, you can build this image with:

```
docker build -t node-classic-image -f Dockerfile-classic .
```

Directly porting to Chainguard Images with the least number of changes results in this Dockerfile:

```Docker
FROM cgr.dev/chainguard/node:latest-dev

ENV NODE_ENV production

WORKDIR /usr/src/app

COPY package.json .
RUN npm install
USER node
COPY . .

EXPOSE 3000

ENTRYPOINT npm start
```

Here we've changed the image to `cgr.dev/chainguard/latest-dev` and the `CMD` command became
`ENTRYPOINT`.

We can still do better in terms of size and security. A multi-stage Dockerfile would look like:


```Docker
FROM cgr.dev/chainguard/node:latest-dev as builder

ENV NODE_ENV production

WORKDIR /usr/src/app

COPY package.json .
RUN npm install
USER node
COPY . .

FROM cgr.dev/chainguard/node:latest

COPY --from=builder --chown=node:node /usr/src/app /app
EXPOSE 3000
ENV NODE_ENV=production
ENV PATH=/app/node_modules/.bin:$PATH
WORKDIR /app
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["node", "app.js"]
```

If you've cloned the GitHub repository, you can build this image with:

```
docker build -t node-multi-image -f Dockerfile-multi .
```

The advantages of this build are:

 - we are using `dumb-init` so the container shuts down cleanly in response to `docker stop`.
 - we do not have all the build tooling in the final image, resulting in a smaller and more secure
   production image

Note that in a production app you may want to use a `Package.lock` file and the `npm ci` command
instead of `npm install` to ensure the correct version of all dependencies is used.

## Additional Resources

 - The [Node.js image documentation](https://images.chainguard.dev/directory/image/node/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=chainguard/migration/migrating-node)
contains full details on our images, including usage documentation, provenance and security
advisories.

 - The [How to Port a Sample Application to Chainguard
Images](/chainguard/migration/porting-apps-to-chainguard/) article contains an example of porting a
Node.js Dockerfile for a legacy application.

 - The [How to Migrate a Node.js Application to Chainguard Images](https://edu.chainguard.dev/chainguard/chainguard-images/videos/node-images/) video works through an example of porting a Node.js Dockerfile.

 - Bret Fisher has an excellent [guide to creating Node.js container
images](https://github.com/BretFisher/nodejs-rocks-in-docker/), including advice for using
distroless.

 - The [Debugging Distroless](/chainguard/chainguard-images/debugging-distroless-images/) guide contains important information for debugging issues with distroless images. You can also refer to the [Verifying Images](/chainguard/chainguard-images/verifying-chainguard-images-and-metadata-signatures-with-cosign/) resource for details around provenance, SBOMs, and image signatures.

