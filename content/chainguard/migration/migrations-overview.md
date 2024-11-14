---
title: "Overview of Migrating to Chainguard Images"
linktitle: "Migration Overview"
type: "article"
description: "This overview serves as a collection of information and resources on migrating to Chainguard Images."
date: 2024-07-22T12:56:52-00:00
lastmod: 2024-08-08T14:44:52-00:00
draft: false
tags: ["IMAGES", "PRODUCT", "OVERVIEW"]
images: []
menu:
  docs:
    parent: "migration"
weight: 005
toc: true
---

[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) are a collection of container images designed for security and minimalism. Many Chainguard Images are [distroless](/chainguard/chainguard-images/getting-started-distroless/); they contain only an open-source application and its runtime dependencies. These images do not even contain a shell or package manager, because fewer dependencies reduce the potential attack surface of images.

By minimizing the number of dependencies and thus reducing their potential attack surface, Chainguard Images inherently contain few to zero CVEs. Chainguard Images are rebuilt nightly to ensure they are completely up-to-date and contain all available security patches. With this nightly build approach, our engineering team sometimes [fixes vulnerabilities before they’re detected](https://www.chainguard.dev/unchained/how-chainguard-fixes-vulnerabilities?utm_source=docs).

The main features of Chainguard Images include:

* Minimalist design, with no unnecessary software bloat
* Automated nightly builds to ensure Images are completely up-to-date and contain all available security patches
* [High quality build-time SBOMs](/chainguard/chainguard-images/working-with-images/retrieve-image-sboms/) (software bill of materials) attesting the provenance of all artifacts within the Image
* [Verifiable signatures](/chainguard/chainguard-images/working-with-images/retrieve-image-sboms/) provided by [Sigstore](/open-source/sigstore/cosign/an-introduction-to-cosign/)
* Reproducible builds with Cosign and apko ([read more about reproducibility](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds))

Because of their minimalist design, Chainguard Images sometimes require users to adjust their image workflows. This document is intended to serve as a migration guide for customers transitioning their organizations to use Chainguard Images. It includes general tips and strategies for migrating to Chainguard Images as well as a curated set of migration-related resources.

## Migrating to Chainguard Images

### Porting Key Points

* Chainguard's distroless Images have no shell or package manager by default. This is great for security, but sometimes you need these things, especially in builder images. For those cases we have `-dev` images (such as `cgr.dev/chainguard/python:latest-dev`) which do include a shell and package manager.
* Chainguard Images typically don't run as root, so a `USER root` statement may be required before installing software.
* The `-dev` images and `wolfi-base` / `chainguard-base` use BusyBox by default, so any `groupadd` or `useradd` commands will need to be ported to `addgroup` and `adduser`.
* The free Developer tier of Images provides `:latest` and `:latest-dev` versions. Our paid Production Images offer tags for major and minor versions.
* We use apk tooling, so `apt install` commands will become `apk add`.
* Chainguard Images are based on `glibc` and our packages cannot be mixed with Alpine packages.
* In some cases, the entrypoint in Chainguard Images can be different from equivalent images based on other distros, which can lead to unexpected behavior. You should always check the image's specific documentation to understand how the entrypoint works.
* When needed, Chainguard recommends using a base image like `chainguard-base` or a `-dev` image to install an application's OS-level dependencies.
* Although `-dev` images are still more secure than most popular container images based on other distros, for increased security on production environments we recommend combining them with a distroless variant in a multi-stage build.

Perhaps the best place for most users to get started with migrating to Chainguard Images is by following our guide on [How to Port a Sample Application to Chainguard Images](/chainguard/migration/porting-apps-to-chainguard/). This guide involves updating a sample application made up of three services to use Chainguard Images. Although the application involved is fairly simple, the concepts outlined in the guide can also be useful for migrating more complex applications.

### Tips for migrating to Chainguard Images

#### Use `-dev` Images when you need a shell

Chainguard Images have no shell or package manager by default. Although this is great for security on production environments, you'll eventually need to install additional packages and log into a container or run shell commands, especially for build stages in multi-stage Dockerfiles and for debugging. For these cases there are `-dev` image variants which do include a shell and package manager.

For example, the `-dev` variant of the `nginx:latest` Image is `nginx:latest-dev`. These images typically contain a shell and tools like a package manager to allow users to more easily debug and modify the image.

To illustrate, if you try to get a shell in the `cgr.dev/chainguard/nginx:latest` image:

```bash
docker run -it --entrypoint /bin/sh --user root cgr.dev/chainguard/nginx:latest

docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "/bin/sh": stat /bin/sh: no such file or directory: unknown.
```

But this is possible with the `latest-dev` variant:

```bash
docker run -it --entrypoint /bin/sh --user root cgr.dev/chainguard/nginx:latest-dev

/ # apk add php
fetch https://packages.wolfi.dev/os/aarch64/APKINDEX.tar.gz
(1/6) Installing xz (5.4.6-r0)
(2/6) Installing libxml2 (2.12.6-r0)
(3/6) Installing php-8.2-config (8.2.18-r0)
(4/6) Installing readline (8.2-r3)
(5/6) Installing sqlite-libs (3.45.1-r0)
(6/6) Installing php-8.2 (8.2.18-r0)
OK: 66 MiB in 38 packages

/ #
```

Although the `-dev` image variants have similar security features as their distroless versions, such as complete SBOMs and signatures, they feature additional software that is typically not necessary in production environments. The general recommendation is to use the `-dev` variants only to build the application and then copy all application artifacts into a distroless image, which will result in a final container image that has a minimal attack surface and won't allow package installations or logins.

That being said, it's worth noting that `-dev` variants of Chainguard Images are completely fine to run in production environments. After all, the `-dev` variants are still **more secure** than many popular container images based on fully-featured operating systems such as Debian and Ubuntu since they carry less software, follow a more frequent patch cadence, and offer attestations for what they include.

#### If necessary, install a different shell

The `-dev` images and `chainguard-base` images use the [ash](https://en.wikipedia.org/wiki/Almquist_shell) shell from BusyBox by default. This is nice from a minimalism perspective, but it's not so great if you need to port a bash and Debian centric entrypoint script to Chainguard Images.

In these cases you have a choice — you can update your scripts to work in ash, or you can install the shell that works with your scripts. There's no reason to be stuck on the ash shell if you really need bash or zsh.

For example:

```bash
docker run -it cgr.dev/$ORGANIZATION/chainguard-base

423450e3fd52:/# echo {1..5}
{1..5}

423450e3fd52:/# apk add bash
fetch https://packages.wolfi.dev/os/aarch64/APKINDEX.tar.gz
(1/3) Installing ncurses-terminfo-base (6.4_p20231125-r1)
(2/3) Installing ncurses (6.4_p20231125-r1)
(3/3) Installing bash (5.2.21-r1)
OK: 20 MiB in 17 packages

423450e3fd52:/# bash

423450e3fd52:/# echo {1..5}
1 2 3 4 5

423450e3fd52:/#
```

Note that this example uses the `chainguard-base` image, which is only available as a paid Production Image. To follow along with this example, you would need to be part of an organization that has access to this image and replace `$ORGANIZATION` in the `docker pull` command with the name of your organization's private Chainguard registry.

#### Use `apk search`

Following on from the last point, you'll often need to install extra utilities to provide required dependencies for applications and scripts. These dependencies are likely to have different package names compared to other Linux distributions, so the `apk search` command can be very useful for finding the package you need.

For example, say we are porting a Dockerfile that uses the `groupadd` command. We could convert this to the BusyBox `addgroup` equivalent, but it's also perfectly fine to add the `groupadd` utility. The only issue is that there's no `groupadd` package, so we have to search for it:

```bash
docker run -it cgr.dev/$ORGANIZATION/chainguard-base

ae154854dc6d:/# groupadd
/bin/sh: groupadd: not found

ae154854dc6d:/# apk add groupadd
ERROR: unable to select packages:
  groupadd (no such package):
    required by: world[groupadd]

ae154854dc6d:/# apk search groupadd
shadow-4.15.1-r0

ae154854dc6d:/# apk add shadow
(1/4) Installing libmd (1.1.0-r1)
(2/4) Installing libbsd (0.12.2-r0)
(3/4) Installing linux-pam (1.6.1-r0)
(4/4) Installing shadow (4.15.1-r0)
OK: 20 MiB in 18 packages

ae154854dc6d:/# groupadd
Usage: groupadd [options] GROUP

Options:
  -f, --force                   exit successfully if the group already exists,
                                and cancel -g if the GID is already used
  -g, --gid GID                 use GID for the new group
  -h, --help                    display this help message and exit
  -K, --key KEY=VALUE           override /etc/login.defs defaults
  -o, --non-unique              allow to create groups with duplicate
                                (non-unique) GID
  -p, --password PASSWORD       use this encrypted password for the new group
  -r, --system                  create a system account
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       directory prefix
  -U, --users USERS             list of user members of this group
```

Another useful trick is the `cmd:` syntax for finding packages that provide commands. For example, searching for `ldd` returns multiple results:

```bash
ae154854dc6d:/# apk search ldd
dpkg-dev-1.22.6-r0
nfs-utils-2.6.4-r1
posix-libc-utils-2.39-r1
```

But if we use the `cmd:` syntax we only get a single result:

```bash
ae154854dc6d:/# apk search cmd:ldd
posix-libc-utils-2.39-r1
```

And we can even use the syntax directly in `apk add`:

```bash
ae154854dc6d:/# apk add cmd:ldd
(1/4) Installing ncurses-terminfo-base (6.4_p20231125-r1)
(2/4) Installing ncurses (6.4_p20231125-r1)
(3/4) Installing bash (5.2.21-r1)
(4/4) Installing posix-libc-utils (2.39-r1)
OK: 27 MiB in 22 packages
```

#### Watch out for entrypoint differences

In some cases, the entrypoint of Chainguard Images can have a different behavior from their equivalent images based on other distros. This happens because many popular images use an entrypoint script that allows running commands on the image through a shell. Since our images typically don't have a shell by default, this can lead to unexpected behavior.

For example, if you run Docker Hub's official Python image, it opens the Python interpreter by default:

```bash
docker run -it python
Python 3.12.3 (main, Apr 10 2024, 11:26:46) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

And the Chainguard Image works in the same way:

```bash
docker run -it cgr.dev/chainguard/python
Python 3.12.3 (main, Apr  9 2024, 16:36:34) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

But if you pass a Linux command to the Docker Hub image, it will be run from a shell:

```bash
docker run -it python echo "in a shell"
in a shell
```

The Chainguard Python image doesn't use an entrypoint script. It relies on the Python interpreter as single entrypoint for both the `latest` and the `latest-dev` variants. So instead of executing the command through a shell, it tries to parse the command as an argument to the Python interpreter:

```bash
docker run -it cgr.dev/chainguard/python echo "in a shell"
/usr/bin/python: can't open file '//echo': [Errno 2] No such file or directory
```

The same behavior can be observed in the `latest-dev` variant, which does contain a shell, but uses the Python interpreter as entrypoint to keep consistency with the `latest` variant:

```bash
docker run -it cgr.dev/chainguard/python:latest-dev echo "in a shell"
/usr/bin/python: can't open file '//echo': [Errno 2] No such file or directory
```

Other images, such as our [WordPress Images](https://images.chainguard.dev/directory/image/wordpress/overview), will have a different entrypoint behavior in their `-dev` variant to allow for customization and to facilitate migration from other base images. It's important to always read the image's documentation to understand how the entrypoint works, and if there are any major differences from other images you may be used to work with.

#### Images don't run as root by default

Although there are exceptions, Chainguard Images typically don’t run as the root user. The reason for this is that distroless containers should have no privileged capabilities, and containers that run as a non-root user and use a minimal seccomp profile are ideal from a security perspective.

Because they don't run as the root user, you may need to include a `USER root` statement in your Dockerfile before installing software on a Chainguard Image.

Additionally, be aware that `-dev` images also do not run as root in most cases, which can result in permission errors like the following:

```bash
docker run -it --entrypoint bin/bash chainguard/python:latest-dev

bash-5.2$ mkdir test
mkdir: can't create directory 'test': Permission denied

bash-5.2$ sudo mkdir test
bash: sudo: command not found
```

In cases like this, you can instead run a command like the following to access the container's shell as the root user:

```bash
docker run -it --user root --entrypoint bin/bash chainguard/python:latest-dev
```

Here, the `--user` option tells Docker to assume the root user role.


#### Packages not found

Container images are usually meant to support every possible use case. Because of this, they often contain packages that aren't necessary for many use cases, which increases the container image's attack surface and makes it more likely to contain CVEs.

Chainguard Images are built with minimalism in mind, and thus contain the bare minimum packages needed for an image to function. However, this also means that Chainguard Images may not contain the packages that you'd expect to find in third-party alternatives.

If a Chainguard Image is missing certain packages that are required for your application, we recommend using a base image and installing the required dependencies on top of it, preferably in a multi-stage Docker build. Our guides on [How to Use Chainguard Images](/chainguard/chainguard-images/how-to-use-chainguard-images/#extending-chainguard-base-images) and [Getting Started with Distroless](/chainguard/migration/migrations-overview/) include guidance on how you can extend Chainguard base images.

In some cases you may have Docker builds that copy in binaries to run agents or similar tooling. You may find these binaries don’t work as expected as they are designed to run on a different Linux distribution. Be aware that Chainguard Images may not have the dependencies required by third-party binaries, or they may be stored at a different path.


### Troubleshooting resources

Even with these tips and potential pitfalls in mind, the move to a distroless workflow can lead to confusion. To help with troubleshooting issues that can occur, Chainguard Academy has a guide on [Debugging Distroless Images](/chainguard/chainguard-images/debugging-distroless-images/).

We also have a video on [Debugging Distroless Containers with Docker Debug](/chainguard/chainguard-images/videos/debugging_distroless/).

Lastly, you might also find help in the [Chainguard Images FAQs](/chainguard/chainguard-images/faq/).



## Migration Resources

Chainguard Academy hosts a number of resources that can be useful when migrating to Chainguard Images.

As mentioned previously, most new users of Chainguard Images would benefit from following our guide on [How to Port a Sample Application to Chainguard Images](/chainguard/migration/porting-apps-to-chainguard/#tldr-porting-key-points). In addition to this guide, Chainguard Academy includes several types of resources that can be useful when migrating to Chainguard Images:

* **Compatibility Guides** — These guides highlight the differences between Chainguard Images and Alpine third-party images.
* **Migration Guides** — These provide guidance migrating workloads based on a specific language or platform to use Chainguard Images.
* **Getting Started Guides** — These resources outline how to work with specific Images, with some including a sample application used in examples.


### Language- or Platform-specific resources

We currently offer both Migration and Getting Started Guides for these Images:

| **Image** | **Migration Guide** | **Getting Started Guide** |
|-----------|:-------------------:|:-------------------------:|
| Node   | [✅ (link)](/chainguard/migration/migrating-node/)   | [✅ (link)](/chainguard/chainguard-images/getting-started/node/) |
| Python | [✅ (link)](/chainguard/migration/migrating-python/) | [✅ (link)](/chainguard/chainguard-images/getting-started/python/)
| PHP    | [✅ (link)](/chainguard/migration/migrating-php/)    | [✅ (link)](/chainguard/chainguard-images/getting-started/php/) |


### Migration Guides

* [Node](/chainguard/migration/migrating-node/)
* [PHP](/chainguard/migration/migrating-python/)
* [Python](/chainguard/migration/migrating-php/)

In addition, we have a few migration guides in the form of videos:

* [Go (video)](/chainguard/chainguard-images/videos/migrating_go/)
* [Java (video)](/chainguard/chainguard-images/videos/java-images/)
* [Node (video)](/chainguard/chainguard-images/videos/node-images/)


### Compatibility Guides

* [Alpine](/chainguard/migration/alpine-compatibility/)
* [Debian](/chainguard/migration/debian-compatibility/)
* [Red Hat](/chainguard/migration/red-hat-compatibility/)
* [Ubuntu](/chainguard/migration/ubuntu-compatibility/)


### Getting Started Guides

* [Cilium](/chainguard/chainguard-images/getting-started/cilium/)
* [Go](/chainguard/chainguard-images/getting-started/go/)
* [Istio](/chainguard/chainguard-images/getting-started/istio/)
* [Laravel](/chainguard/chainguard-images/getting-started/laravel/)
* [MariaDB](/chainguard/chainguard-images/getting-started/mariadb/)
* [NeMo](/chainguard/chainguard-images/getting-started/nemo/)
* [nginx](/chainguard/chainguard-images/getting-started/nginx/)
* [Node](/chainguard/chainguard-images/getting-started/node/)
* [PHP](/chainguard/chainguard-images/getting-started/php/)
* [PostgreSQL](/chainguard/chainguard-images/getting-started/postgres/)
* [Python](/chainguard/chainguard-images/getting-started/python/)
* [PyTorch](/chainguard/chainguard-images/getting-started/pytorch/)
* [Ruby](/chainguard/chainguard-images/getting-started/ruby/)
* [WordPress](/chainguard/chainguard-images/getting-started/wordpress/)


## Further Reading

* [Overview of Chainguard Images](/chainguard/chainguard-images/overview/)
* [How to Use Chainguard Images](/chainguard/chainguard-images/how-to-use-chainguard-images/)
* [How to transition to secure container images with new migration guides (Blog)](https://www.chainguard.dev/unchained/how-to-transition-to-secure-container-images-with-new-migration-guides)
* [Getting Started with Distroless Images](/chainguard/chainguard-images/getting-started-distroless/)

