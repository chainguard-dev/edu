---
title: "Tutorial: Porting a Sample Application to Chainguard Images"
linktitle: "Tutorial: Porting a Sample Application"
type: "article"
description: "This article works through porting a small but complete application to use Chainguard Images. As
we'll see, this is relatively straightforward, but it is important to be aware of some of the
differences to other common images."
date: 2024-04-10T12:56:52-00:00
lastmod: 2024-04-10T14:44:52-00:00
draft: false
tags: ["IMAGES", "PRODUCT", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "concepts"
weight: 100
toc: true
---

## TL;DR Porting Key Points

* Chainguard Images have no shell or package manager by default. This is great for security, but
  sometimes you need these things, especially in builder images. For those cases we have `-dev`
  images (e.g. `cgr.dev/chainguard/python:latest-dev`) which do include a shell and package manager.
* Chainguard Images typically don't run as root, so a `USER root` statement may be required before
  installing software
* The `-dev` images and `wolfi-base` use busybox by default, so any `groupadd` or `useradd` commands
  will need to be ported to `addgroup` and `adduser`
* The free developer tier of images provides `latest` and `latest-dev` versions. For specific tags
  or older versions please see our production images.
* We use apk tooling, so `apt get` commands will become `apk add`
* Chainguard Images are based on `glibc` and our packages cannot be mixed with Alpine packages
* The entrypoint on Chainguard Images is likely to be different to other common images (due to the
  lack of a shell) which can be confusing -- for example shell commands may get unexpectedly run by
  the Python interpreter

---

The application in question is [identidock](https://github.com/using-docker/identidock). This
application was written for the book [Using
Docker](https://learning.oreilly.com/library/view/using-docker/9781491915752/) about ten years ago,
which shows that we can still migrate software of this age to a new container while realizing the
benefits of a no-to-low CVE count. The application itself will create
[identicons](https://en.wikipedia.org/wiki/Identicon) for a user name, similar to what [GitHub
generates for users with no avatar](https://github.blog/2013-08-14-identicons/). It was designed at
the time to demonstrate a "microservices" approach, and as such it's made up of 3 services:


* The main identidock service, which takes the requests and talks to the
  [dnmonster](https://github.com/amouat/dnmonster) service and the redis cache
* A NodeJS application which creates the identicons
* Redis which is used as a simple cache

The services are put together as shown. The user only talks to the identidock service. The
identidock service will first check the cache to see if it has already created an identicon for the
input and if not requests a new identicon from the dnmonster service. The identicon is then returned
to the user and saved to the cache if required.

![Diagram of Identidock Architecture](arch.png "Diagram of Identidock Architecture")

The book walked through using various orchestrators to deploy the application, some of which have
since fallen out of usage (anyone remember [fleet](https://github.com/coreos/fleet)?). For the sake
of this tutorial, we'll use Docker Compose, which is arguably the simplest surviving orchestrator
covered in the book.

The first task was to get the 10-year-old application building and running again. As it was a simple
example application, this was thankfully straightforward and mainly required bumping versions of
dependencies and a couple of cases of replacing unmaintained libraries. For a larger project this
may well have been a major effort. The original code can be found on the [using-docker GitHub
repository](https://github.com/using-docker/identidock) and the updated working version (prior to
moving to Chainguard Images) can be found on the [v1
branch](https://github.com/chainguard-dev/identidock-cg/tree/v1) of the [repository for this
tutorial](https://github.com/chainguard-dev/identidock-cg/).

In order to follow along with the tutorial, please clone the code and switch to the `v1` branch e.g:


```bash
git clone https://github.com/chainguard-dev/identidock-cg.git
cd identidock-cg
git switch v1
```

# Updating dnmonster

To begin, we'll update the heart of the application – the dnmonster service. dnmonster is based on
[monsterid.js](monsterid.js) by Kevin Gaudin. The dnmonster container hosts an API which returns an
[identicon](https://en.wikipedia.org/wiki/Identicon) based on the input it's given.

```bash
docker run -d -p 8080:8080 amouat/dnmonster
curl --output ./monster.png 'localhost:8080/monster/wolfi?size=100'
```

In this example, we give dnmonster the input "wolfi", for which it will produce the following image:

![Simple "monster" art](monster.png "Monster generated for wolfi input")

The version of the code on the v1 branch already contains a few updates from the original code, as
well as bumping versions the codebase was moved from the old and sporadically maintained
[restify](https://github.com/restify/node-restify) module to the more modern
[express](https://expressjs.com/) module.

The Dockerfile for this version of the dnmonster service can be found in the dnmonster folder and
looks like:


```Dockerfile
FROM node

RUN apt-get update && apt-get install -yy --no-install-recommends \
    libcairo2-dev libjpeg62-turbo-dev libpango1.0-dev libgif-dev \
    librsvg2-dev build-essential g++

#Create non-root user
RUN groupadd -r dnmonster && useradd -r -g dnmonster dnmonster
RUN install -d -o dnmonster -g dnmonster /home/dnmonster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
COPY ./src /usr/src/app

RUN chown -R dnmonster:dnmonster /usr/src/app
USER dnmonster

EXPOSE 8080

CMD [ "npm", "start" ]
```

The image can be built with:

```bash
cd dnmonster
docker build -t dnmonster .
```

Looking at this image:

```bash
docker images dnmonster
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
dnmonster    latest    1eb74ae9d0f0   3 hours ago   1.22GB
```

We can also run Grype to investigate if there any known vulnerabilities present in the image:

```
grype docker:dnmonster
 ✔ Vulnerability DB                [no update available]
 ✔ Loaded image                                                                                                    dnmonster:latest
 ✔ Parsed image                                             sha256:20b235c7f120abdb223516c9c2649aac1e6e3dde8301ae7394c6b4a433537b51
 ✔ Cataloged contents                                              5703441c038c01715db710653b028e4689ec2ad96bf471bad9a06e0c4cf5775e
   ├── ✔ Packages                        [788 packages]
   ├── ✔ File digests                    [18,974 files]
   ├── ✔ File metadata                   [18,974 locations]
   └── ✔ Executables                     [1,343 executables]
 ✔ Scanned for vulnerabilities     [970 vulnerability matches]
   ├── by severity: 5 critical, 70 high, 154 medium, 32 low, 450 negligible (259 unknown)
   └── by status:   11 fixed, 959 not-fixed, 0 ignored
```

This tells us that (at the time of writing) the image is 1.22 GB in size and has **970 known
vulnerabilities**.

The first step in moving to Chainguard Images is to try switching the image name in to check if
anything breaks. In this case, we’ll begin with the developer variant of the Node image. Change the
first line of the Dockerfile from:


```Dockerfile
FROM node
```

To:

```Dockerfile
FROM cgr.dev/chainguard/node:latest-dev
```

Unlike the `cgr.dev/chainguard/node:latest` image, the `latest-dev` version includes a shell and
package manager, which we will need for some of the build steps. In general it's better to use the
more minimal "latest" version where possible in order to keep the size down and reduce the tooling
available to attackers.

If you try building this image, you'll find that it breaks in several places. The image needs to
install various libraries so that it can compile the
<code>[node-canvas](https://github.com/Automattic/node-canvas)</code> dependency, and this looks a
bit different in Debian and [Wolfi](http://wolfi.dev) (the OS powering Chainguard Images). In Wolfi,
we first need to switch to the root user to install software and we use <code>apk add</code> instead
of <code>apt-get</code>. We then need to figure out the Wolfi equivalents of the various Debian
packages, which may not always have a one-to-one correspondence. There are tools to help here – you
can consult our [migration
guides](https://edu.chainguard.dev/chainguard/migration-guides/debian-compatibility/) and use apk
tools (e.g. <code>apk search libjpeg</code>), but searching the [Wolfi
GitHub](https://github.com/wolfi-dev/os) repository for package names will often provide you with
what you’re looking for. Make these changes by replacing the "RUN apt-get … " line with the
following "RUN apk update" and adding a "USER root" line. The start of the Dockerfile should look
like this:


```Dockerfile
FROM cgr.dev/chainguard/node:latest-dev

USER root
RUN apk update && apk add \
    cairo-dev libjpeg-turbo-dev pango-dev giflib-dev \
    librsvg-dev glib-dev harfbuzz-dev fribidi-dev expat-dev libxft-dev
```

The next change we need to make is to the "RUN groupadd …" line. Chainguard images use busybox by
default, which means `groupadd` needs to become `addgroup`. Rewrite the line so that it looks like
this:

```Dockerfile
RUN addgroup dnmonster && adduser -D -G dnmonster dnmonster
```

Finally, the default entrypoint for the Chainguard image is `/usr/bin/node`. If we leave the `CMD`
as it is, it will be interpreted as an argument to node, which isn't what we want. The Docker
official image uses an entrypoint script to interpret commands, but this can't be done in the
`cgr.dev/chainguard/node:latest` image due to the lack of a shell and we want the `latest-dev`
entrypoint to match. The easiest fix is to change the `CMD` command to `ENTRYPOINT` which will
override the `/usr/bin/node` command:

```Dockerfile
ENTRYPOINT [ "npm", "start" ]
```

Once you've made all these changes, you should have a Dockerfile that looks like:

```Dockerfile
FROM cgr.dev/chainguard/node:latest-dev

USER root
RUN apk update && apk add \
    cairo-dev libjpeg-turbo-dev pango-dev giflib-dev \
    librsvg-dev glib-dev harfbuzz-dev fribidi-dev expat-dev libxft-dev

#Create non-root user
RUN addgroup dnmonster && adduser -D -G dnmonster dnmonster
RUN install -d -o dnmonster -g dnmonster /home/dnmonster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
COPY ./src /usr/src/app

RUN chown -R dnmonster:dnmonster /usr/src/app
USER dnmonster

EXPOSE 8080

ENTRYPOINT [ "npm", "start" ]
```


At this point, we have a version of dnmonster that works and is equivalent to the previous version.
We can build this image:

```bash
docker build -t dnmonster-cg .
...
```

And investigate it again:

```bash
docker images dnmonster-cg
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
dnmonster-cg   latest    d4bb3a473a90   36 seconds ago   880MB

grype docker:dnmonster-cg
✔ Vulnerability DB                [no update available]
✔ Loaded image                                                                                                 dnmonster-cg:latest
✔ Parsed image                                             sha256:d4bb3a473a9086d3e3d17e781b3ea0ad84031cb4082cbf433e9561ee349e5e86
✔ Cataloged contents                                              d32762222ca3091f6f6a5009fe407da33f96cecec2d29368b271b2e0d52f8ff0
├── ✔ Packages                        [506 packages]
├── ✔ File digests                    [14,262 files]
├── ✔ File metadata                   [14,262 locations]
└── ✔ Executables                     [714 executables]
✔ Scanned for vulnerabilities     [0 vulnerability matches]
├── by severity: 0 critical, 0 high, 0 medium, 0 low, 0 negligible
└── by status:   0 fixed, 0 not-fixed, 0 ignored
No vulnerabilities found
```

So the image is now significantly smaller at 880MB, but more importantly, we've eliminated all 970
vulnerabilities.

But we can still do more. In particular, although 880MB is significantly smaller than the previous
version, it's still a large image.To get the size down, we can use a multi-stage build where the
built assets are copied into a minimal production image, which doesn't include build tooling or
dependencies required during development.

Ideally, we would use the `cgr.dev/chainguard/node:latest` image for this, but we also need to
install the dependencies for `node-canvas`, which means we need an image with apk tools. Normally
it’s recommended to use a `latest-dev` image for this, but in node's case, the `latest-dev` image is
relatively large due to the inclusion of build tooling, such as C compilers, that can be required by
Node modules. Instead, we're going to use the `wolfi-base` image and install `nodejs` as a package.

To do this, replace the Dockerfile with the following:

```Dockerfile
FROM cgr.dev/chainguard/node:latest-dev as build

USER root
RUN apk update && apk add \
    cairo-dev libjpeg-turbo-dev pango-dev giflib-dev \
    librsvg-dev glib-dev harfbuzz-dev fribidi-dev expat-dev libxft-dev

#Create non-root user
RUN addgroup dnmonster && adduser -D -G dnmonster dnmonster
RUN install -d -o dnmonster -g dnmonster /home/dnmonster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
COPY ./src /usr/src/app

RUN chown -R dnmonster:dnmonster /usr/src/app
USER dnmonster

EXPOSE 8080

ENTRYPOINT [ "npm", "start" ]

FROM cgr.dev/chainguard/wolfi-base

RUN apk update && apk add nodejs \
    cairo-dev libjpeg-turbo-dev pango-dev giflib-dev \
    librsvg-dev glib-dev harfbuzz-dev fribidi-dev expat-dev libxft-dev

WORKDIR /app
COPY --from=build /usr/src/app /app

EXPOSE 8080
ENTRYPOINT [ "node", "server.js" ]
```

We've added an "`as build"` statement to the first "`FROM"` line and added a second build that
starts on the line "`FROM cgr.dev/chainguard/wolfi-base"`. The second build installs the required
dependencies (including nodejs) before copying the build artifacts from the first image. We also
changed the entrypoint to execute node directly, as the image no longer contains npm.

Build and investigate the image:


```bash
docker build -t dnmonster-multi .
…
docker images dnmonster-multi
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
dnmonster-multi   latest    9b2e79c87572   18 minutes ago   336MB
grype docker:dnmonster-multi
✔ Vulnerability DB                [no update available]
✔ Loaded image                                                                                              dnmonster-multi:latest
✔ Parsed image                                             sha256:9b2e79c87572902c3dc1577e55b56b27406b521cae6b231cb15d9b347eb0b94c
✔ Cataloged contents                                              88258c2837dbe88bd4490fc672d170581fbcdbe0dcc34c696d2a14032ad36395
├── ✔ Packages                        [256 packages]
├── ✔ File digests                    [9,357 files]
├── ✔ File metadata                   [9,357 locations]
└── ✔ Executables                     [599 executables]
✔ Scanned for vulnerabilities     [0 vulnerability matches]
├── by severity: 0 critical, 0 high, 0 medium, 0 low, 0 negligible
└── by status:   0 fixed, 0 not-fixed, 0 ignored
No vulnerabilities found
```

This results in an image that is now only 336MB in size and still has 0 CVEs.

We're most of the way now, but there are still a couple of finishing touches to make. The first one
is to remove the dnmonster user. The wolfi-base image already defines a `nonroot` user, so we can
make the build a little less complicated by using that user directly. The second one is to add in a
process manager. We have node running as the root process (PID 1) in the container, which isn't
ideal as it doesn't handle some of the responsibilities that come with running as PID 1, such as
forwarding signals to subprocesses. You can see this most clearly when you try to stop the image –
it takes several seconds as the process doesn't respond to the SIGTERM signal sent by Docker and has
to be hard killed with SIGKILL. To fix this, we can add
<code>[tini](https://github.com/krallin/tini)</code>, a small init for containers.

The `tini` binary will run as PID 1, launch npm as a subprocess and take care of PID 1
responsibilities. Now, the final Dockerfile looks like this:

```Dockerfile
FROM cgr.dev/chainguard/node:latest-dev as build

USER root

RUN apk update && apk add \
    tini cairo-dev libjpeg-turbo-dev pango-dev giflib-dev \
    librsvg-dev glib-dev harfbuzz-dev fribidi-dev expat-dev libxft-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV NODE_ENV production
COPY package.json /usr/src/app/
RUN npm install
COPY ./src /usr/src/app

FROM cgr.dev/chainguard/wolfi-base

RUN apk update && apk add tini nodejs \
    cairo-dev libjpeg-turbo-dev pango-dev giflib-dev \
    librsvg-dev glib-dev harfbuzz-dev fribidi-dev expat-dev libxft-dev

WORKDIR /app
COPY --from=build /usr/src/app /app

EXPOSE 8080
ENTRYPOINT ["tini", "--" ]
CMD [ "node", "server.js" ]
```


This version is also available in the main branch of the repository.

Build it:

```bash
docker  build -t dnmonster-final .
…
```

And run it to prove it still works:

```bash
docker run -d -p 8080:8080 amouat/dnmonster-final
...
curl --output ./monster.png 'localhost:8080/monster/wolfi?size=100'
```

There are still more tweaks that could be made. Bret Fisher has some [excellent resources on
building NodeJS containers in this GitHub
repo](https://github.com/BretFisher/nodejs-rocks-in-docker). But for the purposes of this example
app, we've made excellent progress.

## Updating Identidock

The next service we will look at updating is Identidock, the main entrypoint for the application.
Identidock is responsible for looking up requests in the cache and falling-back to calling the
dnmonster service if they're not present.

Again, the version of the code on the v1 branch already contains a few updates from the original
code, but in this case all that was needed was to bump various libraries to newer versions. The
Dockerfile for the v1 version can be found in the identidock folder and looks like:

```Dockerfile
FROM python

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==3.0.2 uWSGI requests==2.31.0 redis==5.0.3
WORKDIR /app
USER uwsgi
COPY app /app
COPY cmd.sh /

EXPOSE 9090 9191

CMD ["/cmd.sh"]
```

The image can be built with the following, assuming the current directory is the root of repo:

```bash
cd identidock
docker build -t identidock .
…
```

Take a look at the image:

```bash
docker images identidock
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
identidock   latest    46d3857f790b   8 minutes ago   1.05GB
```

Scan for vulnerabilities:

```bash
grype docker:identidock
✔ Vulnerability DB                [no update available]
✔ Loaded image                                                                                                      identidock:latest
✔ Parsed image                                                sha256:46d3857f790b295a14829e709d8483f98bd3c1f304bc1f40f87b16a62300b76b
✔ Cataloged contents                                                 09873b2d93203eb19c56257a597702b060b803851d152c624407f8aca30ab018
├── ✔ Packages                        [455 packages]
├── ✔ File digests                    [19,267 files]
├── ✔ File metadata                   [19,267 locations]
└── ✔ Executables                     [1,437 executables]
✔ Scanned for vulnerabilities     [980 vulnerability matches]
├── by severity: 5 critical, 66 high, 155 medium, 32 low, 463 negligible (259 unknown)
└── by status:   11 fixed, 969 not-fixed, 0 ignored
```

At the time of writing, this image is 1.05GB with 980 vulnerabilities (5 critical) according to Grype.

Again as a first step, we will try to switch out directly to the Chainguard Image. To do this, edit the Dockerfile so the first line reads:

```Dockerfile
FROM cgr.dev/chainguard/python:latest-dev
```

Before building the image we need to also update "groupadd" syntax to use the "addgroup" format. As Chainguard Images don't run as root by default for security reasons, we also need to change to the root user for this command to work. Replace the RUN groupadd line with the lines:


```Dockerfile
USER root
RUN addgroup uwsgi && adduser -D -G uwsgi uwsgi
```


The image now builds, but there are issues due to differences in the image entrypoint. If you run
the image, you will get a confusing error message such as:

```bash
`File "/cmd.sh", line 4`
  if [ "$ENV" = 'DEV' ]; then
         ^^^^^^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

This is caused by the Chainguard Image using `/usr/bin/python` as the entrypoint, which means the
`cmd.sh` entrypoint script is interpreted by Python instead of the shell. Remember, most Chainguard
Images don't come with a shell at all, so this difference from the [Docker Hub
Python](https://hub.docker.com/_/python) images makes sense, but can still be a source of confusion.
Fixing this can be as easy as changing the entrypoint, but let's take a look at the script first.
This is the file `cmd.sh` in the identidock directory:

```bash
#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
   echo "Running Development Server"
   exec python "/app/identidock.py"
elif [ "$ENV" = 'UNIT' ]; then
    echo "Running Unit Tests"
    exec python "tests.py"
else
    echo "Running Production Server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py \
               --callable app --stats 0.0.0.0:9191
fi
```

This script decides how to run the application depending on how the `ENV` environment variable is
set. The idea here is to allow us to use the same image in development, testing and production. This
approach is no longer recommended as it leads to development tooling being present in the production
environment. Even though the development tooling isn't run in production, it is still bloating the
image and is potentially exploitable by attackers. Therefore, we will use a different approach and
break the Dockerfile into separate development and production images.

Let’s skip to the final Dockerfile for our image and walk through the changes made. These changes
address multiple issues, beyond just having multiple images, and are based on the [Chainguard
Academy guide to Python
images](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/python/).

Replace the Dockerfile with this one (this is also available on the "main" branch):

```Dockerfile
FROM cgr.dev/chainguard/python:latest-dev as dev

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app
RUN python -m venv /app/venv
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["identidock.py"]

FROM cgr.dev/chainguard/python

WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

COPY app/identidock.py ./
COPY --from=dev /app/venv /app/venv

EXPOSE 9090
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:9090", "identidock:app" ]
```

And add the file `requirements.txt` to the current directory (`identidock`) with the following contents:

```
Flask==3.0.2
requests==2.31.0
redis==5.0.3
gunicorn==21.2.0
```

The first thing to notice is that we have a multistage build now. If you want the development image
rather than the production one, you can specify it during docker build:

```bash
docker build --target dev -t identidock:dev .
```

Otherwise, you will get the production image only.

There are several more environment variables defined. These prevent the creation of Python bytecode
and buffering of output. The reasons why you want these are normally set are explained in detail in
the blog [PYTHONDONTWRITEBYTECODE and PYTHONUNBUFFERED
Explained](https://blog.mimixtech.com/pythondontwritebytecode-and-pythonunbuffered-explained).

The installation of pip modules has moved to the `requirements.txt` file. The main thinking here is
that we don't need to update the Dockerfile each time a dependency is updated or changed.

The development server runs on port 5000, while the production server runs on port 9090. We could
edit this so they both run on the same port, but this approach reduces the chance of accidentally
running the development server in production. The development server is started directly from the
entrypoint, so we are no longer dependent on an entrypoint script, simplifying our architecture.

To get a minimal, clean production install, we are using a Python virtual environment
([venv](https://docs.python.org/3/library/venv.html)) in the development image to isolate all
dependencies, which are then copied over to the production image. Finally, the production image has
been changed to use [gunicorn](https://gunicorn.org/) as [uwsgi has entered "maintenance
mode"](https://github.com/unbit/uwsgi).

Build the final image:

```bash
docker build -t identidock-cg .
```

And take a look at it:

```bash
docker images identidock-cg
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
identidock-cg   latest    30a424aa8a51   15 seconds ago   93.6MB
```

Run a scan with grype:


```bash
grype docker:identidock-cg
✔ Vulnerability DB                [updated]
✔ Loaded image                                                                                                                                                                    identidock-cg:latest
✔ Parsed image                                                                                                                 sha256:30a424aa8a51548491ea3c152383ce2c16a801859e9e8e252b147162ac0b637e
✔ Cataloged contents                                                                                                                  40024c9c378c73d52c9e62f32fcf6d0d328d8d14a66a328df8d6fc0278a4a2e8
├── ✔ Packages                        [46 packages]
├── ✔ File digests                    [2,020 files]
├── ✔ File metadata                   [2,020 locations]
└── ✔ Executables                     [141 executables]
✔ Scanned for vulnerabilities     [0 vulnerability matches]
├── by severity: 0 critical, 0 high, 0 medium, 0 low, 0 negligible
└── by status:   0 fixed, 0 not-fixed, 0 ignored
```

The result of all these changes is that the production image is only 93.6 MB (down from 1.05GB, so
an enormous saving of just under a GB) and has 0 CVEs (down from 980). This is a huge improvement!

Further information on using Chainguard Images with Python can be found in our
[guide](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/python/).


## Updating Redis

This migration is the most straightforward. We're not making any changes to the application image,
so all we need to do is directly update the reference to `redis:7` in the Docker Compose file to
`cgr.dev/chainguard/redis`. The new image requires no extra configuration but we go from a 139 MB
image with 137 vulnerabilities to a 23MB image with 0 CVEs (again according to Grype).

Full details on the new Docker Compose file are found in the next section.

## Updating Docker Compose

In the top level directory of the repo, replace the `docker-compose.yaml` with the following:


```yaml
name: identidock

services:
  frontend:
    build: identidock
    ports:
      - "9090:9090"

  dnmonster:
    build: dnmonster

  redis:
    image: cgr.dev/chainguard/redis
```

If you now run `docker compose up –build`, you should have a working application that can be reached on port 9090:

![Screenshot of running application](app.png "Screenshot of running application")

There are some differences between this version and the original. The environment variable used for
switching between image variants has been removed and the ports have changed to reflect the default
port used in gunicorn.

This Compose file doesn't contain support for a development workflow currently – ideally we would be
able to quickly iterate on our code without building a new image. The original file used volumes to
achieve this, but this isn't something we want to do with the production image. One solution is to
have a separate development Compose file, which will build the development image and use a volume to
mount code at runtime for immediate feedback. New versions of Docker also support [Compose
Watch](https://docs.docker.com/compose/file-watch/) which can be a more efficient and granular
solution that volume mounts. See [What is Docker Compose Watch and what problem does it
solve?](https://collabnix.com/what-is-docker-compose-watch-and-what-problem-does-it-solve/) for an
introductory tutorial on using Compose Watch.


## Conclusion

Porting our application to Chainguard Images was relatively straightforward. There were some gotchas
around differences to other images, such as different entrypoint settings and names for packages.
The largest part of the puzzle was moving from single image builds to multistage builds that take
advantage of the minimal Chainguard runtime images for Python and NodeJS. Once all this was done, we
ended up with a much smaller set of images and with a drastically reduced number of CVEs.
