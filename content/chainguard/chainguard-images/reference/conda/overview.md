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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 6th | `sha256:d09b34a32c5677931bdaa13b3c59654b074d13d2ab2eedcd65edab00918e1817` |
|  `latest`     | September 4th | `sha256:1e5e88e7b6dea2e7660401200e424a6ed48dae41b25cbbd899dd891c3b6569fa` |



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

