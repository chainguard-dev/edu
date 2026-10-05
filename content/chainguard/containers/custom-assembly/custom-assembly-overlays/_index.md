---
title: "Overview of Custom Assembly Overlays"
linktitle: "Custom Assembly Overlays"
type: "article"
description: "How Custom Assembly Overlays package customizations into reusable overlays and apply them to repositories with bindings."
date: 2026-09-28T16:33:22+00:00
lastmod: 2026-10-05T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Conceptual", "Custom Assembly"]
images: []
aliases:
- /chainguard/containers/custom-assembly/tag-based-custom-assembly/
menu:
  docs:
    parent: "features"
    identifier: "custom-assembly-overlays"
weight: 33
toc: true
---

{{< beta feature="Tag-based Custom Assembly" enroll="true" >}}

Standard [Custom Assembly](/chainguard/containers/custom-assembly/overview/) stores one customization on one repository and applies it to every tag. Custom Assembly Overlays separate the customization from where it applies. You define the customization once, as an overlay, and attach it to repositories with bindings. This lets you do the following:

* Reuse one customization, such as your organization's internal certificates, across many repositories.
* Apply a customization to a subset of a repository's tags, such as only the `-dev` tags. This is called [tag-based Custom Assembly](/chainguard/containers/custom-assembly/custom-assembly-overlays/tag-based-custom-assembly/).
* Add a package to every tag, with the package name matched to each tag's language version.

This page explains the overlay and binding resources. To scope a customization to specific tags, see [Tag-based Custom Assembly](/chainguard/containers/custom-assembly/custom-assembly-overlays/tag-based-custom-assembly/). To create and manage overlays, see [Managing Custom Assembly Overlays with chainctl](/chainguard/containers/custom-assembly/custom-assembly-overlays/chainctl/) or [Managing Custom Assembly Overlays with Terraform](/chainguard/containers/custom-assembly/custom-assembly-overlays/terraform/).

## Overlays and bindings

Custom Assembly Overlays split a customization into two resources:

* An **overlay** is a named, reusable set of customizations, such as packages, environment variables, annotations, user accounts, certificates, and runtime repositories. An overlay belongs to your organization, not to a repository, and on its own it changes nothing.
* A **binding** attaches one overlay to one repository and selects which of that repository's tags the overlay applies to.

To apply an overlay to several repositories, create one binding for each repository.

Each binding has a [tag selector](/chainguard/containers/custom-assembly/custom-assembly-overlays/tag-based-custom-assembly/#tag-selectors), which chooses the tags the overlay applies to. A selector can match every tag in the repository, every tag of a variant such as `-dev`, or an exact list of tag names. Tags that no binding matches keep their uncustomized image.

When you create, update, or delete a binding, or update an overlay, Chainguard rebuilds the affected tags without waiting for a new upstream release. An overlay update rebuilds the matching tags in every repository the overlay is bound to. As with standard Custom Assembly, a build normally takes less than 20 minutes, and Chainguard rebuilds the customized tags whenever their packages are updated.

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

Custom Assembly Overlays have the following limitations:

* **One model per repository.** A repository can use standard Custom Assembly or overlays, but not both. If a repository has one kind of customization, adding the other kind fails with the error `repository custom overlay and overlay binding not allowed`. To move a repository from standard Custom Assembly to overlays, contact your Chainguard account team.
* **No Chainguard Console support.** Manage overlays and bindings with `chainctl`, Terraform, or the Chainguard API. The Console's Custom Assembly editor manages standard Custom Assembly only.
* **A missing package fails the build.** If a package in an overlay can't be installed on a tag, that tag's build fails. Chainguard doesn't skip the package. The build logs name the package that failed.
* **No removing base packages.** As with standard Custom Assembly, an overlay can add to an image but can't remove packages from the source image.

## Permissions

Overlays and bindings use their own capabilities:

* `registry.overlays.list` lets you view overlays and bindings. The built-in `viewer`, `editor`, and `owner` roles include it.
* `registry.overlays.edit` lets you create, update, and delete overlays and bindings. The built-in `editor` and `owner` roles include it.

To create a custom role with these capabilities, see [Overview of roles and role-bindings in Chainguard](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

## Learn more

* [Tag-based Custom Assembly](/chainguard/containers/custom-assembly/custom-assembly-overlays/tag-based-custom-assembly/)
* [Managing Custom Assembly Overlays with chainctl](/chainguard/containers/custom-assembly/custom-assembly-overlays/chainctl/)
* [Managing Custom Assembly Overlays with Terraform](/chainguard/containers/custom-assembly/custom-assembly-overlays/terraform/)
* [Overview of Chainguard Custom Assembly](/chainguard/containers/custom-assembly/overview/)
* [Custom Assembly FAQs](/chainguard/containers/custom-assembly/faq/)
