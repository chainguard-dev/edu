---
title: "Tag-based Custom Assembly"
linktitle: "Tag-based Custom Assembly"
type: "article"
description: "How to use tag selectors on overlay bindings to apply customizations to a subset of a repository's tags."
date: 2026-10-05T00:00:00+00:00
lastmod: 2026-10-05T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Conceptual", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "custom-assembly-overlays"
    identifier: "tag-based-custom-assembly"
weight: 10
toc: true
---

{{< beta feature="Custom Assembly Overlays" enroll="true" >}}

Standard [Custom Assembly](/chainguard/containers/custom-assembly/overview/) applies one customization to every tag in a repository. This fails for images that ship several language or runtime versions side by side, because a package built for one version can't install on the others.

For example, the `python` image publishes tags for Python 3.11, 3.12, 3.13, and 3.14. The `py3.13-typer` package depends on Python 3.13. If you add it with standard Custom Assembly, every tag tries to install it, and the 3.11, 3.12, and 3.14 builds fail.

Tag-based Custom Assembly uses the tag selector on an [overlay binding](/chainguard/containers/custom-assembly/custom-assembly-overlays/#overlays-and-bindings) to choose which tags receive a customization. For example, you can do the following:

* Add a package to specific tags, such as `3.13` and `3.13-dev`.
* Add debugging tools to every `-dev` tag and keep the other tags minimal.
* Add a package to every tag, with the package name matched to each tag's Python version through [version templates](/chainguard/containers/custom-assembly/custom-assembly-overlays/#version-templates-in-package-names).

This page explains how tag selectors match tags and how bindings combine when their selectors overlap. For the overlay and binding resources themselves, see [Overview of Custom Assembly Overlays](/chainguard/containers/custom-assembly/custom-assembly-overlays/). To create and manage bindings, see [Managing Custom Assembly Overlays with chainctl](/chainguard/containers/custom-assembly/custom-assembly-overlays/chainctl/) or [Managing Custom Assembly Overlays with Terraform](/chainguard/containers/custom-assembly/custom-assembly-overlays/terraform/).

## Tag selectors

Each binding has a tag selector, which chooses the tags the overlay applies to. A selector is one of three kinds:

| Selector | Matches | Example use |
| --- | --- | --- |
| **Exact** | The tags you list by name, such as `3.13` and `3.13-dev`. | Add a package that only works with one version. |
| **Variant** | Every tag of a variant. Only the `dev` variant is available, which matches every tag ending in `-dev`. | Add debugging tools to development images only. |
| **All** | Every tag in the repository. | Add certificates or packages that work with every tag. |

Variant and all selectors also match tags published after you create the binding. An exact selector matches only the tag names you list. Tags that no binding matches keep their uncustomized image.

### Exact tags and shared digests

Several tags often point to the same image. For example, `3.13`, `3.13.7`, and `3.13.7-r0` might share one digest. An exact selector customizes only the tags you list, even when other tags share their digest. If you bind an overlay to `3.13` alone, `3.13` gets a customized image, and `3.13.7` and `3.13.7-r0` keep the original. To keep several tags identical, list all of them.

An exact selector matches tag names, not images. When `3.13` moves to a new release, the binding follows it, so the new `3.13` image is customized too.

Chainguard doesn't check that an exact tag exists when you create the binding. A mistyped tag name matches nothing, so no build runs for it.

## How overlapping bindings combine

A tag can match more than one binding. For example, `latest-dev` matches an all binding, a dev variant binding, and an exact binding that lists `latest-dev`. When a tag matches several bindings, Chainguard layers them in this order:

1. All bindings.
1. Variant bindings.
1. Exact bindings.

Packages and runtime repositories accumulate across layers. When two layers set the same environment variable, annotation, or other single value, the more specific layer wins: exact over variant, and variant over all.

For example, suppose a repository has the following bindings:

* An all binding whose overlay adds `curl`.
* A dev variant binding whose overlay adds `strace`.
* An exact binding on `latest-dev` whose overlay adds `gdb`.

Chainguard adds these packages to each tag:

| Tag | Packages added |
| --- | --- |
| `latest-dev` | `curl`, `strace`, `gdb` |
| Other `-dev` tags | `curl`, `strace` |
| All other tags | `curl` |

### Several bindings of the same kind

You can bind several overlays to one repository with the same kind of selector. For example, you can bind a certificates overlay and a packages overlay to a repository, both with an all selector.

Bindings of the same kind have no precedence order, so their overlays must not contradict each other. Chainguard rejects a binding if it matches a tag that another binding of the same kind also matches, and the two overlays set any of the following to different values:

* An environment variable
* An annotation
* A named certificate, runtime key, user, or group
* Another single value, such as the user the image runs as

Packages and runtime repositories never cause a binding conflict, because Chainguard combines them. Combined packages can still fail a build if the packages themselves are incompatible, for example if two of them install the same file. Chainguard also runs the conflict check when you update an overlay, against every repository the overlay is bound to.

You can bind a given overlay to a repository only once.

## Learn more

* [Overview of Custom Assembly Overlays](/chainguard/containers/custom-assembly/custom-assembly-overlays/)
* [Managing Custom Assembly Overlays with chainctl](/chainguard/containers/custom-assembly/custom-assembly-overlays/chainctl/)
* [Managing Custom Assembly Overlays with Terraform](/chainguard/containers/custom-assembly/custom-assembly-overlays/terraform/)
* [Custom Assembly FAQs](/chainguard/containers/custom-assembly/faq/)
