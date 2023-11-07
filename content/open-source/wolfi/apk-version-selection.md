---
title: "Package Version Selection"
type: "article"
draft: false
date: 2023-11-06T08:49:31+00:00
lastmod: 2023-11-06T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Wolfi", "apk", "melange"]
images: []
menu:
  docs:
    parent: "wolfi"
weight: 750
toc: true
---

This document explains how to specify version constraints for packages installed with the apk tool, as well as apko and melange. Understanding version selection will enable you to choose the version you're looking for, determine what updates and vulnerability fixes you receive, and can allow you to reproduce an image's digest through exact version matching. 

## Version selection in apko and melange

All the examples in this document focus on usage with the `apk` tool, but the same semantics apply to `apk add` as well as references in an apko or melange `packages` field:

```yaml
environment:
  packages:
    - go>1.21    # install anything newer than 1.21, excluding 1.21
    - foo=~4.5.6 # install any version with a name starting with "4.5.6" (e.g., 4.5.6-r7)
    - python3    # install the latest stable version of python3.
```

## Basic Usage

```sh
apk add go
```

This will install the latest stable version of Go. This is nearly always what you want, since it gives you stable software, with as many updates and vulnerability fixes as possible.

See below for information on the behavior of pre-release versions.

## Fuzzy Matching

You can also use fuzzy version matching.

For example, if you don't care about the epoch, you can request any version of Go with a version string starting in `1.21.1`:

```sh
apk add go=~1.21.1
```

Or you can add any 1.21:

```sh
apk add go=~1.21
```

If multiple versions match that prefix (e.g., `1.21.1-r0`, `1.21.1-r1`, etc.), then the highest numbered next version segment will be chosen.

Fuzzy matching means you can request Go 1.21 without getting 1.20 or 1.22, like you would with `&lt;` or `>`. Wolfi provides a separate `go-1.21` package that `provides:go=1.21.x` so in Go's case you can request `go-1.21` and get the same behavior as `go~1.21`. But this might not be the same case for all packages.

The operators `~`, `~=` and `=~` are equivalent, and all do the same thing.

You can also use fuzzy matching to request a major version prefix:

```sh
apk add go=~1
```

Go will not have a version 2, but other packages might.

For example, `erlang=~26` will match any release of Erlang in the 26 major version, and not match Erlang 25 and below or 27 and above.

`erlang~2` will _not_ match Erlang 26 or 27. It only fuzzy matches whole segments of a semantic versioning version string.

## Version Constraints

To request a minimum or maximum acceptable version of a package to install, you can use `>`, `<`, `>=` and `<=`:

```sh
apk add go>1.20  # install anything newer than 1.20, excluding 1.20.0, but including 1.20.1
apk add go<1.20  # install anything older than 1.20, excluding 1.20.0, but including 1.19.14
apk add go>=1.20 # install anything newer than 1.20, including 1.20.0
apk add go<=1.20 # install anything older than 1.20, including 1.20.0
```

This comparison logic is aware of semantic versioning semantics, so `1.9.10` is less than `1.10`, and `1.9.9` is less than `1.9.10`, even though they may be alphabetically sorted later.

Version constraints can be useful when you want to ensure a minimum or maximum major or minor version, but still want to receive minor or patch updates. Fuzzy matching can produce the same behavior – `go~1.20` is equivalent to `go>=1.20` for example.

## Installing Future Versions

Using `apk add go` installs the latest _stable_ release of Go. For most packages, there is no distinction between the "latest" and "latest stable" release. Some projects, like Go, Node, Python, etc., produce pre-release versions before, or have more nuanced release maturity and support processes. Please refer to the respective larger project for more information. 

Go versions often have Release Candidates. For example, when Go 1.21 is the latest release, the Go team may prepare for Go 1.22 by releasing a Go `1.22_rc1` to let folks try it out before it's fully released. To install this version, you can specify the pre-release package name, which for go will be `go-1.22`:

```sh
apk add go-1.22
```

Note that this string uses a dash (`-`), which means it's specifying the full name of the package, which Wolfi's convention is `go-1.22`. Since it doesn't include any other version constraint or fuzzy matching, it's requesting "the latest version of a package named `go-1.22`", which may install `go-1.22` with version `1.22_rc3`.

When Go 1.22 is fully released, it will become the latest release of Go and `provides:[go=$version]`, so `apk add go` will install Go 1.22.0.

## Exact Version Matching

You can also specify an exact version and epoch to install:

```sh
apk add go=1.21.1-r0
```

This will install exactly this version and epoch, as long as that is available.

Because package updates or vulnerability fixes won't be picked up, this is not generally useful for day-to-day usage. However, this is useful for reproducing an environment exactly, and it's the form we use in the resolved apko configuration attestation we attach to images. This makes it clear exactly what versions of which packages were installed in an image, so you can reproduce it with `apko` to get exactly the same image digest.
