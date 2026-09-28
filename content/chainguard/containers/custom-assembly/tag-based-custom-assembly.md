---
title: "Customizing specific tags with Custom Assembly"
linktitle: "Tag-based customization"
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
weight: 33
toc: true
---

{{< beta feature="Tag-based Custom Assembly" enroll="true" >}}

Standard [Custom Assembly](/chainguard/containers/custom-assembly/overview/) applies one customization to every tag in a repository. That works when every tag can accept the same packages, but it breaks down for images that ship several language or runtime versions side by side.

For example, the `python` image publishes tags for Python 3.11, 3.12, 3.13, and 3.14. If you add `py3.13-typer` with standard Custom Assembly, every tag tries to install it. The package depends on Python 3.13, so the 3.11, 3.12, and 3.14 builds fail.

Tag-based Custom Assembly solves this by letting you choose which tags receive a customization. You can:

* Add a package to specific tags only, such as `3.13` and `3.13-dev`.
* Add debugging tools to every `-dev` tag, leaving the runtime tags minimal.
* Add a package to every tag, with the package name adjusted to match each tag's Python version.
* Reuse one customization, such as your organization's internal certificates, across many repositories.

This page explains the concepts. To create and manage customizations, see [Managing tag-based Custom Assembly with chainctl](/chainguard/containers/custom-assembly/tag-based-custom-assembly-chainctl/) or [Managing tag-based Custom Assembly with Terraform](/chainguard/containers/custom-assembly/tag-based-custom-assembly-terraform/).

## Overlays and bindings

Tag-based Custom Assembly splits a customization into two resources:

* An **overlay** is a named, reusable set of customizations, such as packages, environment variables, annotations, user accounts, certificates, and runtime repositories. An overlay belongs to your organization, not to a repository, and on its own it changes nothing.
* A **binding** attaches one overlay to one repository and selects which of that repository's tags the overlay applies to.

To apply an overlay to several repositories, create one binding for each repository. When you update an overlay, Chainguard rebuilds every tag it's bound to, in every repository.

After you create, update, or delete a binding, Chainguard rebuilds the affected tags. You don't need to wait for a new upstream release. As with standard Custom Assembly, a build normally takes less than 20 minutes. Chainguard then maintains the customized tags and rebuilds them when their packages are updated.

## Tag selectors

Each binding has a tag selector, which chooses the tags the overlay applies to. There are three kinds of selector:

| Selector | Matches | Example use |
| --- | --- | --- |
| **Exact** | The tags you list by name, such as `3.13` and `3.13-dev`. | Add a package that only works with one version. |
| **Variant** | Every tag of a variant. Only the `dev` variant is available, which matches every tag ending in `-dev`. | Add debugging tools to development images only. |
| **All** | Every tag in the repository. | Add certificates or packages that work with every tag. |

Tags that no binding matches are left as they are.

Variant and all selectors match tags by pattern, so they also cover tags published after you create the binding. An exact selector only ever matches the tag names you list.

### Exact tags and shared digests

Several tags often point to the same image. For example, `3.13`, `3.13.7`, and `latest` might all share one digest. An exact selector applies the overlay only to the tags you list, even when other tags share their digest. If you bind an overlay to `3.13` only, `3.13` gets a customized image and `3.13.7` and `latest` keep the original image.

If you want several tags to stay identical, list all of them in the selector.

Chainguard doesn't check that an exact tag exists when you create the binding. A tag name with a typo matches nothing, and no build runs for it.

## How overlapping bindings combine

A tag can match more than one binding. For example, `latest-dev` matches an all binding, a dev variant binding, and an exact binding that lists `latest-dev`. When a tag matches several bindings, Chainguard layers them in this order:

1. All bindings.
1. Variant bindings.
1. Exact bindings.

Later layers take precedence. List fields, such as packages and runtime repositories, accumulate across layers. For single-value fields, such as an environment variable or annotation that two layers both set, the more specific layer's value wins.

For example, suppose a repository has these bindings:

* An all binding whose overlay adds `curl`.
* A dev variant binding whose overlay adds `strace`.
* An exact binding on `latest-dev` whose overlay adds `gdb`.

The tags are built as follows:

| Tag | Packages added |
| --- | --- |
| `latest-dev` | `curl`, `strace`, `gdb` |
| Other `-dev` tags | `curl`, `strace` |
| All other tags | `curl` |

### Several bindings of the same kind

You can bind several overlays to one repository with the same kind of selector. For example, you might bind a certificates overlay and a packages overlay to a repository, both with an all selector. Bindings of the same kind are combined in any order, so they can't disagree. Chainguard rejects a binding when it and an existing binding match a tag in common and set the same field to different values. A field conflicts when both overlays set any of the following to different values:

* The same environment variable.
* The same annotation.
* The same named certificate, runtime key, user, or group.
* The same single-value setting, such as the user the image runs as.

Packages and runtime repositories never conflict; they're combined. Chainguard runs the same check when you update an overlay, against every repository the overlay is bound to.

You can only bind a given overlay to a repository once.

## Version templates in package names

Many packages include a language version in their name, such as `py3.12-cryptography` and `py3.14-cryptography`. To add the right package to every tag with one overlay, use the `{{major}}` and `{{minor}}` placeholders in the package name:

```yaml
contents:
  packages:
    - py{{major}}.{{minor}}-cryptography
```

When Chainguard builds each tag, it replaces the placeholders with the major and minor version of the image's main package. The `3.12` tags of the `python` image receive `py3.12-cryptography`, and the `3.14` tags receive `py3.14-cryptography`. When a tag moves to a new version, the package follows it.

Chainguard finds each image's main package from its `dev.chainguard.package.main` label. You can check the label with a command like the following:

```shell
crane config cgr.dev/$ORGANIZATION/python:3.12 | jq -r '.config.Labels["dev.chainguard.package.main"]'
```

```output
python-3.12
```

`{{major}}` and `{{minor}}` are the only supported placeholders. Chainguard rejects an overlay that uses any other `{{...}}` placeholder when you create or update it.

If an image has no main package, or its version has no major and minor components, the placeholders stay in the package name. That tag's build then fails because the package can't be found, and the build logs name the package.

## Supported customizations

An overlay supports the same customizations as standard Custom Assembly, with the same validation rules:

* Packages (`contents.packages`)
* [Custom runtime repositories](/chainguard/containers/custom-assembly/overview/#custom-runtime-repositories) (`contents.runtime_repositories`)
* [Custom runtime keys](/chainguard/containers/custom-assembly/overview/#custom-runtime-keys) (`contents.runtime_keyring`)
* [Environment variables and annotations](/chainguard/containers/custom-assembly/custom-assembly-chainctl/#adding-custom-annotations-and-environment-variables) (`environment` and `annotations`)
* [User accounts and groups](/platform/chainctl/chainctl-docs/chainctl_images_repos_build_apply/) (`accounts`)
* [Custom certificates](/chainguard/containers/custom-assembly/custom-assembly-certs/) (`certificates.additional`)

Chainguard-managed certificate bundles (`certificates.providers`) aren't supported in overlays. Chainguard rejects an overlay containing any field it doesn't support rather than ignoring the field.

## Limitations

Tag-based Custom Assembly has the following limitations:

* **No mixing with standard Custom Assembly.** A repository can use standard Custom Assembly or tag-based Custom Assembly, but not both. You can't create a binding on a repository that already has a standard Custom Assembly customization, and you can't add a standard customization to a repository that has bindings. The error is `repository custom overlay and overlay binding not allowed`. To switch a repository to tag-based Custom Assembly, remove its standard customization first, then recreate it as an overlay with an all selector. For the steps, see [Moving a repository from standard Custom Assembly](/chainguard/containers/custom-assembly/tag-based-custom-assembly-chainctl/#moving-a-repository-from-standard-custom-assembly).
* **No Chainguard Console support.** You can't create, view, or manage overlays and bindings in the Console. Use `chainctl`, Terraform, or the Chainguard API. The Console's Custom Assembly editor manages standard Custom Assembly only.
* **Only the `dev` variant.** Variant selectors support `-dev` tags only.
* **Failed builds stay failed.** If a package in an overlay can't be installed on a tag, that tag's build fails. Chainguard doesn't skip the package or build the tag without it. The build logs show which package failed.
* **You can't remove base packages.** As with standard Custom Assembly, overlays can add to an image but can't remove packages from the source image.

## Permissions

Overlays and bindings use their own capabilities:

* `registry.overlays.list` lets you view overlays and bindings. The built-in `viewer`, `editor`, and `owner` roles include it.
* `registry.overlays.edit` lets you create, update, and delete overlays and bindings. The built-in `editor` and `owner` roles include it.

To create a custom role with these capabilities, see [Overview of roles and role-bindings in Chainguard](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

## Learn more

* [Managing tag-based Custom Assembly with chainctl](/chainguard/containers/custom-assembly/tag-based-custom-assembly-chainctl/)
* [Managing tag-based Custom Assembly with Terraform](/chainguard/containers/custom-assembly/tag-based-custom-assembly-terraform/)
* [Overview of Chainguard Custom Assembly](/chainguard/containers/custom-assembly/overview/)
* [Custom Assembly FAQs](/chainguard/containers/custom-assembly/faq/)
