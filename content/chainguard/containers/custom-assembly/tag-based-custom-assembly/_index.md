---
title: "Overview of tag-based Custom Assembly"
linktitle: "Tag-based Custom Assembly"
type: "article"
description: "How tag-based Custom Assembly uses overlays and bindings to apply customizations to a subset of a repository's tags."
date: 2026-09-28T16:33:22+00:00
lastmod: 2026-09-28T16:33:22+00:00
draft: false
tags: ["Chainguard Containers", "Conceptual", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
    identifier: "tag-based-custom-assembly"
weight: 33
toc: true
---

{{< beta feature="Tag-based Custom Assembly" enroll="true" >}}

Standard [Custom Assembly](/chainguard/containers/custom-assembly/overview/) applies one customization to every tag in a repository. This fails for images that ship several language or runtime versions side by side, because a package built for one version can't install on the others.

For example, the `python` image publishes tags for Python 3.11, 3.12, 3.13, and 3.14. The `py3.13-typer` package depends on Python 3.13. If you add it with standard Custom Assembly, every tag tries to install it, and the 3.11, 3.12, and 3.14 builds fail.

Tag-based Custom Assembly lets you choose which tags receive a customization. For example, you can do the following:

* Add a package to specific tags, such as `3.13` and `3.13-dev`.
* Add debugging tools to every `-dev` tag and keep the other tags minimal.
* Add a package to every tag, with the package name matched to each tag's Python version.
* Reuse one customization, such as your organization's internal certificates, across many repositories.

This page explains the concepts. To create and manage customizations, see [Managing tag-based Custom Assembly with chainctl](/chainguard/containers/custom-assembly/tag-based-custom-assembly/chainctl/) or [Managing tag-based Custom Assembly with Terraform](/chainguard/containers/custom-assembly/tag-based-custom-assembly/terraform/).

## Overlays and bindings

Tag-based Custom Assembly splits a customization into two resources:

* An **overlay** is a named, reusable set of customizations, such as packages, environment variables, annotations, user accounts, certificates, and runtime repositories. An overlay belongs to your organization, not to a repository, and on its own it changes nothing.
* A **binding** attaches one overlay to one repository and selects which of that repository's tags the overlay applies to.

To apply an overlay to several repositories, create one binding for each repository.

When you create, update, or delete a binding, or update an overlay, Chainguard rebuilds the affected tags without waiting for a new upstream release. An overlay update rebuilds the matching tags in every repository the overlay is bound to. As with standard Custom Assembly, a build normally takes less than 20 minutes, and Chainguard rebuilds the customized tags whenever their packages are updated.

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

## Version templates in package names

Many packages include a language version in their name, such as `py3.12-cryptography` and `py3.14-cryptography`. To add the right package to every tag with one overlay, use the `{{major}}` and `{{minor}}` placeholders in the package name:

```yaml
contents:
  packages:
    - py{{major}}.{{minor}}-cryptography
```

When Chainguard builds each tag, it replaces the placeholders with the major and minor version of the image's main package. The `3.12` tags of the `python` image receive `py3.12-cryptography`, and the `3.14` tags receive `py3.14-cryptography`. When a tag moves to a new version, the package follows it.

Chainguard reads each image's main package from its `dev.chainguard.package.main` label. To check the label, run the following [crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane) command:

```shell
crane config cgr.dev/$ORGANIZATION/python:3.12 | jq -r '.config.Labels["dev.chainguard.package.main"]'
```

```output
python-3.12
```

In this example, the main package is Python 3.12, so `{{major}}` becomes `3` and `{{minor}}` becomes `12`.

`{{major}}` and `{{minor}}` are the only supported placeholders. If you create or update an overlay with any other `{{...}}` placeholder, Chainguard rejects it.

If an image has no main package, or its version has no major and minor components, Chainguard can't fill in the placeholders. That tag's build fails, and the build logs name the package.

## Supported customizations

An overlay supports the same customizations as standard Custom Assembly, with the same validation rules:

* Packages (`contents.packages`)
* [Custom runtime repositories](/chainguard/containers/custom-assembly/overview/#custom-runtime-repositories) (`contents.runtime_repositories`)
* [Custom runtime keys](/chainguard/containers/custom-assembly/overview/#custom-runtime-keys) (`contents.runtime_keyring`)
* [Environment variables and annotations](/chainguard/containers/custom-assembly/custom-assembly-chainctl/#adding-custom-annotations-and-environment-variables) (`environment` and `annotations`)
* [User accounts and groups](/platform/chainctl/chainctl-docs/chainctl_images_repos_build_apply/) (`accounts`)
* [Custom certificates](/chainguard/containers/custom-assembly/custom-assembly-certs/) (`certificates.additional`)

Overlays don't support Chainguard-managed certificate bundles (`certificates.providers`). If an overlay contains a field that overlays don't support, Chainguard rejects the whole overlay instead of ignoring the field.

## Limitations

Tag-based Custom Assembly has the following limitations:

* **One model per repository.** A repository can use standard or tag-based Custom Assembly, but not both. If a repository has one kind of customization, adding the other kind fails with the error `repository custom overlay and overlay binding not allowed`. To move a repository from standard to tag-based Custom Assembly, contact your Chainguard account team.
* **No Chainguard Console support.** Manage overlays and bindings with `chainctl`, Terraform, or the Chainguard API. The Console's Custom Assembly editor manages standard Custom Assembly only.
* **A missing package fails the build.** If a package in an overlay can't be installed on a tag, that tag's build fails. Chainguard doesn't skip the package. The build logs name the package that failed.
* **No removing base packages.** As with standard Custom Assembly, an overlay can add to an image but can't remove packages from the source image.

## Permissions

Overlays and bindings use their own capabilities:

* `registry.overlays.list` lets you view overlays and bindings. The built-in `viewer`, `editor`, and `owner` roles include it.
* `registry.overlays.edit` lets you create, update, and delete overlays and bindings. The built-in `editor` and `owner` roles include it.

To create a custom role with these capabilities, see [Overview of roles and role-bindings in Chainguard](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

## Learn more

* [Managing tag-based Custom Assembly with chainctl](/chainguard/containers/custom-assembly/tag-based-custom-assembly/chainctl/)
* [Managing tag-based Custom Assembly with Terraform](/chainguard/containers/custom-assembly/tag-based-custom-assembly/terraform/)
* [Overview of Chainguard Custom Assembly](/chainguard/containers/custom-assembly/overview/)
* [Custom Assembly FAQs](/chainguard/containers/custom-assembly/faq/)
