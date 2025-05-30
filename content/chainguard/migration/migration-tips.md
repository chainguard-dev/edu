---
title: "Tips for Migrating to Chainguard Containers"
linktitle: "Migration Tips"
type: "article"
description: "This guide outlines a number of tips and strategies to keep in mind for when your organization begins migrating to Chainguard Containers."
date: 2025-05-29T12:56:52-00:00
lastmod: 2025-05-29T12:56:52-00:00
draft: false
tags: ["Chainguard Containers", "Product"]
images: []
menu:
  docs:
    parent: "migration"
weight: 007
toc: true
---

The process of migrating over to Chainguard Containers isn't always straightforward. To help customers become acquainted with Chainguard Containers as they go through the migration process, we've assembled this list of tips and strategies for migrating over their applications.


## Use Development Variants When You Need a Shell

Chainguard provides development (or `-dev`) variants of its containers which include a shell and package manager to allow users to more easily debug and modify the image.

To illustrate, if you try to get a shell in the `cgr.dev/chainguard/nginx:latest` image it will return an error:

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

Although the `-dev` variants have similar security features as their distroless counterparts — such as complete SBOMs and signatures — they feature additional software that is typically not necessary in production environments. The general recommendation is to use the `-dev` variants only to build the application and then copy all application artifacts into a distroless image, which will result in a final container image that has a minimal attack surface and won't allow package installations or logins.

That being said, it's worth noting that `-dev` variants of Chainguard Containers are completely fine to run in production environments. After all, the `-dev` variants are still **more secure** than many popular container images based on fully-featured operating systems such as Debian and Ubuntu since they carry less software, follow a more frequent patch cadence, and offer attestations for what they include.

## Install a Different Shell

The `-dev` variants and `chainguard-base` image use the [ash](https://en.wikipedia.org/wiki/Almquist_shell) shell from BusyBox by default. This is nice from a minimalism perspective, but it's not so great if you need to port a bash and Debian centric entrypoint script to Chainguard Containers.

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

Note that this example uses the `chainguard-base` image, which is only available as a paid Production Container. To follow along with this example, you would need to be part of an organization that has access to this image.


## Use `apk search`

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
  -f, --force               	exit successfully if the group already exists,
                            	and cancel -g if the GID is already used
  -g, --gid GID             	use GID for the new group
  -h, --help                	display this help message and exit
  -K, --key KEY=VALUE       	override /etc/login.defs defaults
  -o, --non-unique          	allow to create groups with duplicate
                            	(non-unique) GID
  -p, --password PASSWORD   	use this encrypted password for the new group
  -r, --system              	create a system account
  -R, --root CHROOT_DIR     	directory to chroot into
  -P, --prefix PREFIX_DIR   	directory prefix
  -U, --users USERS         	list of user members of this group
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

## Watch Out for Entrypoint Differences

In some cases, the entrypoint of Chainguard Containers can have a different behavior from their equivalent images based on other distros. This happens because many popular container images use an entrypoint script that allows running commands on the image through a shell. Since our images typically don't have a shell by default, this can lead to unexpected behavior.

For example, if you run Docker Hub's official Python image, it opens the Python interpreter by default:

```bash
docker run -it python
Python 3.12.3 (main, Apr 10 2024, 11:26:46) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

And the Chainguard Container works in the same way:

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

Other images, such as our [WordPress container images](https://images.chainguard.dev/directory/image/wordpress/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrations-overview), will have a different entrypoint behavior in their `-dev` variant to allow for customization and to facilitate migration from other base images. It's important to always read the image's documentation to understand how the entrypoint works, and if there are any major differences from other images you may be used to work with.

## Containers Don't Run As root By Default

Although there are exceptions, Chainguard Containers typically don’t run as the root user. The reason for this is that distroless containers should have no privileged capabilities, and containers that run as a non-root user and use a minimal seccomp profile are ideal from a security perspective.

Because they don't run as the root user, you may need to include a `USER root` statement in your Dockerfile before installing software on a Chainguard Container.

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


## Packages Not Found

Container images are usually meant to support every possible use case. Because of this, they often contain packages that aren't always necessary, which increases the container image's attack surface and makes it more likely to contain CVEs.

Chainguard Containers are built with minimalism in mind, and thus contain the bare minimum packages needed for an image to function. However, this also means that Chainguard Containers may not contain the packages that you'd expect to find in third-party alternatives.

If a Chainguard Container is missing certain packages that are required for your application, we recommend using a base image and installing the required dependencies on top of it, preferably in a multi-stage Docker build. Our guides on [How to Use Chainguard Containers](/chainguard/chainguard-images/how-to-use-chainguard-images/#extending-chainguard-base-images) and [Getting Started with Distroless](/chainguard/migration/migrations-overview/) include guidance on how you can extend Chainguard base images.

Alternatively, you can take advantage of Chainguard's [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/) and [Private APK Repositories](/chainguard/chainguard-images/features/private-apk-repos/) features to extend your container images. Custom Assembly allows users to create customers container images with extra packages added. This reduces their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs.

Private APK Repositories, meanwhile, allow customers to pull secure apk packages from Chainguard. The list of packages available in an organization’s private repository is based on the apk repositories that the organization already has access to. For example, say your organization has access to the [Chainguard MySQL container image](https://images.chainguard.dev/directory/image/mysql/versions). Along with `mysql`, this image comes with other apk packages, including `bash`, `openssl`, and `pwgen`. This means that you'll have access to these apk packages through your organization's private APK repository, along with any others that appear in Chainguard container images that your organization has access to. 

In some cases you may have Docker builds that copy in binaries to run agents or similar tooling. You may find these binaries don’t work as expected as they are designed to run on a different Linux distribution. Be aware that Chainguard Containers may not have the dependencies required by third-party binaries, or they may be stored at a different path.


## Learn More

For more resources on migrating ot Chainguard Containers, please refer to our [Containers MIgration documentation](/chainguard/migration/). In particular, our [Migration Overview](/chainguard/migration/migrations-overview/) may be of interest. Chainguard Academy also hosts a number of [Compatibility Resources](/chainguard/migration/compatibility/) and [Migration Guides](/chainguard/migration/migration-guides/) for specific platforms and tools.
