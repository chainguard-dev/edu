---
title: "apko YAML Reference"
type: "article"
description: "A reference guide for writing YAML for apko"
date: 2022-10-10T11:07:52+02:00
lastmod: 2023-03-15T11:07:52+02:00
draft: false
tags: ["apko", "Reference",]
images: []
menu:
  docs:
    parent: "apko"
weight: 150
toc: true
---

Apko files are a YAML based declarative definition of an image to be built by apko. Unlike Dockerfiles, there is no support for running arbitrary Unix commands (i.e. there is no equivalent of `RUN` statements). This means apko can guarantee the contents and reproducibility of the final image, as well as produce extra metadata such as SBOMs.

This page provides a reference for apko's YAML specification.

## contents
This section defines sources and packages you want to include in your image.

| Directive      | Description                                                                                                                                                                                |
|----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `repositories` | Defines a list of repositories to look in for packages. These can be either URLs or file paths. File paths should start with a label like @local e.g: `@local /github/workspace/packages`. |
| `packages`     | A list containing all packages that should be installed as part of a given image's requirements.                                                                                           |
| `keyring`      | PGP keys to add to the keyring for verifying packages.                                                                                                                                     |


### Example

```yaml
contents:
  keyring:
    - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
  repositories:
    - https://packages.wolfi.dev/os
  packages:
    - wolfi-base
    - nginx
```

## entrypoint
This section defines the default commands and/or services to be executed by the container at runtime.

| Directive        | Description                                                                                                                                                                            |
|------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`           | When this is set to `service-bundle`, the s6 supervisor will be used to start commands listed in `services`.                                                                           |
| `command`        | Specifies a command to run when the container starts. Note that this sets the image _entrypoint_, not the _cmd_ top level element. Only valid when `type` is **not** `service-bundle`. |
| `shell-fragment` | Behaves like `command`, except that the command is a shell fragment. Only valid when `type` is **not** `service-bundle`.                                                               |
| `services`       | Maps **service names** to **commands** that should be started by the s6 supervisor when the container starts. This option is only valid when `type` is set to `service-bundle`.        |

Services are monitored with the [s6 supervisor](https://skarnet.org/software/s6/index.html).

### Examples

#### Example 1: Command entrypoint
```yaml
entrypoint:
  command: /usr/bin/php81
```

#### Example 2: Service entrypoint
```yaml
entrypoint:
  type: service-bundle
  services:
    php-fpm: /usr/sbin/php-fpm
```

## cmd
Defines a command to run when the container starts up. If `entrypoint.command` is not set, it will be executed with `/bin/sh -c`. If `entrypoint.command` is set, `cmd` will be passed as arguments to `entrypoint.command`. This sets the "cmd" value on OCI images.

### Example

```yaml
cmd: help
```

## stop-signal
Configures the shutdown signal sent to the main process in the container by the runtime. By default, this is `SIGTERM`. Be mindful when using this alongside a `service-bundle` entrypoint, which will intercept and potentially reinterpret the signal.

### Example

```yaml
stop-signal: SIGQUIT
```

## work-dir
Sets the working directory for the image. Commands defined within the image `entrypoint` are taken as relative to this path. Equivalent to [WORKDIR](https://docs.docker.com/engine/reference/builder/#workdir) in Dockerfile syntax.

### Example

```yaml
work-dir: /app
```
## archs
The architectures to build. This top-level directive expects a list with all architectures that should be a target for the build. By default, apko will try to build for all architectures that are currently supported.

### Example

```yaml
archs:
  - x86_64
```

## environment
This section defines environment variables that will be set for this image.

### Example

```yaml
environment:
  PATH: /usr/sbin:/sbin:/usr/bin:/bin
  myVAR: "test"
```

## accounts
This section defines users and groups that should be added to this image.

| Directive | Description                                                         |
|-----------|:--------------------------------------------------------------------|
| groups    | A list with the groups that should be present in this image.        |
| users     | A list with the user accounts that should be present in this image. |
| run-as    | The default user to run the entrypoint command.                     |


### Example

```yaml
  users:
    - username: php
      uid: 65532
      gid: 65532
    - username: laravel
      uid: 1000
      gid: 1000
  run-as: 65532
```
## Paths

Defines filesystem operations that can be applied to the image. This includes setting permissions on files or directories as well as creating empty files, directories, and links.

| Directive     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `path`        | Filesystem path to handle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `type`        | The type of file operation to perform. This can be one of the following:<br/> - `directory`: create an empty directory at the path<br/>  - `empty-file`: create an empty file at the path<br/>  - `hardlink`: create a hardlink (`ln`) at the path, linking to the value specified in `source`<br/> - `symlink`: create a symbolic link (`ln -s`) at the path, linking to the value specified in `source`<br/> - `permissions`: sets file permissions on the file or directory at the path. |
| `run-as`      | The default user to run the entrypoint command.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `uid`         | UID to associate with the file                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `gid`         | GID to associate with the file                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `permissions` | File permissions to set. Permissions should be specified in octal e.g. 0o755 (see `man chmod` for details).                                                                                                                                                                                                                                                                                                                                                                                 |
| `source`      | Used in `hardlink` and `symlink`, this represents the path to link to.                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Example

```yaml
paths:
  - path: /app
    type: directory
    permissions: 0o777
    uid: 65532
    gid: 65532
```

## Includes

Defines a path to a configuration file which should be used as the base config. By default, there is no
base config used.

The path can be either a local file, or a file in a remote git repository, in the same style as Go package names and GitHub Actions.

### Example

```yaml
include: github.com/chainguard-dev/apko/examples/alpine-base.yaml@main
```
This would reference the file `examples/alpine-base.yaml` in the `main` branch of the apko git repository.

At present, the path structure assumes that the git repository lives on a site similar to
GitHub, GitLab, or Gitea. In other words, given an include path like the above, it will
parse as:

```
host: github.com
repository: chainguard-dev/apko
path: examples/alpine-base.yaml
reference: main
```


## Annotations

`annotations` defines the set of annotations that should be applied to images and indexes.

### Example

```yaml
annotations:
  image-author: Chainguard
  image-source: http://gihub.com/chainguard-images/images
```
