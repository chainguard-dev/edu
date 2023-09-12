---
title: "Image Overview: r-base"
type: "article"
description: "Overview: r-base Chainguard Image"
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

[cgr.dev/chainguard/r-base](https://github.com/chainguard-images/images/tree/main/images/r-base)

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest`     | September 11th | `sha256:80f66c9e3a997d165c4f286e8fbccd6076170b463f146f724d503e031a5c4bd7` |
|  `latest-dev` | September 11th | `sha256:87348599a88d53fd79b144206ae432d79f94f95d414a93faa20d784633203621` |



This image contains the R programming language and environment.
It can be used for statistical analysis, machine learning and data visualization.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/r-base:latest
```

## Use It!

The image can be run directly and sets the R wrapper as the entrypoint:

```shell
docker run cgr.dev/chainguard/r-base:latest

Usage: R [options] [< infile] [> outfile]
   or: R CMD command [arguments]

Start R, a system for statistical computation and graphics, with the
specified options, or invoke an R tool via the 'R CMD' interface.

Options:
  -h, --help            Print short help message and exit
  --version             Print version info and exit
  --encoding=ENC        Specify encoding to be used for stdin
  --encoding ENC
  RHOME                 Print path to R home directory and exit
```

The binary also contains the Rscript wrapper:

```shell
docker run --entrypoint=/usr/bin/Rscript cgr.dev/chainguard/r-base:latest

Usage: Rscript [options] file [args]
   or: Rscript [options] -e expr [-e expr2 ...] [args]
A binary front-end to R, for use in scripting applications.

Options:
  --help              Print usage and exit
  --version           Print version and exit
  --verbose           Print information on progress
  --default-packages=LIST  Attach these packages on startup;
                        a comma-separated LIST of package names, or 'NULL'
and options to R (in addition to --no-echo --no-restore), for example:
  --save              Do save workspace at the end of the session
  --no-environ        Don't read the site and user environment files
  --no-site-file      Don't read the site-wide Rprofile
  --no-init-file      Don't read the user R profile
  --restore           Do restore previously saved objects at startup
  --vanilla           Combine --no-save, --no-restore, --no-site-file,
                        --no-init-file and --no-environ

Expressions (one or more '-e <expr>') may be used *instead* of 'file'.
Any additional 'args' can be accessed from R via 'commandArgs(TRUE)'.
See also  ?Rscript  from within R.
```

Note that the standard version of this image requires a shell because R is typically
invoked through built-in shell wrappers.

