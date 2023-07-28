---
title: "Image Overview: conda"
type: "article"
description: "Overview: conda Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/conda](https://github.com/chainguard-images/images/tree/main/images/conda)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 27th    | `sha256:bd1efe8cedf54548c15911af9e86b5aa4c46b0948d55af762f0fbd483834b75f` |
|  `latest-dev` | July 27th    | `sha256:8b1cb9bc6e4a4792f4668fe3a2c70cd29aec901a155e3509e76a6c9579a3ee3b` |



This image contains the CLI for the [Conda](https://docs.conda.io/en/latest/) programming environment.

This image contains the `conda` command, which can be used to create and manage conda environments, as well
as other assorted conda utilities.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/conda:latest
```

## Use It!

The image can be run directly and sets the conda binary as the entrypoint:

```
docker run cgr.dev/chainguard/conda:latest
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean             Remove unused packages and caches.
    compare           Compare packages between conda environments.
    config            Modify configuration values in .condarc. This is modeled after the git config command. Writes to the user .condarc file (/root/.condarc) by default. Use the --show-sources flag to display all identified configuration locations on your computer.
    create            Create a new conda environment from a list of specified packages.
    info              Display information about current conda install.
    init              Initialize conda for shell interaction.
    install           Installs a list of packages into a specified conda environment.
    list              List installed packages in a conda environment.
    package           Low-level conda package utility. (EXPERIMENTAL)
    remove (uninstall)
                      Remove a list of packages from a specified conda environment. Use `--all` flag to remove all packages and the environment itself.
    rename            Renames an existing environment.
    run               Run an executable in a conda environment.
    search            Search for packages and display associated information.The input is a MatchSpec, a query language for conda packages. See examples below.
    update (upgrade)  Updates conda packages to the latest compatible version.
    notices           Retrieves latest channel notifications.

options:
  -h, --help          Show this help message and exit.
  -V, --version       Show the conda version number and exit.

conda commands available from other packages (legacy):
  content-trust
  env
```

The `conda` binary and tools are in the `/opt/conda/bin` directory.

