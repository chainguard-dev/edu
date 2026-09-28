---
title: "Managing tag-based Custom Assembly with Terraform"
linktitle: "Tag-based customization with Terraform"
type: "article"
description: "How to use the Chainguard Terraform provider to create overlays and bind them to specific tags of a Custom Assembly repository."
date: 2026-09-28T16:33:22+00:00
lastmod: 2026-09-28T16:33:22+00:00
draft: false
tags: ["Chainguard Containers", "Procedural", "Custom Assembly", "Automation"]
images: []
menu:
  docs:
    parent: "features"
weight: 37
toc: true
---

{{< beta feature="Tag-based Custom Assembly" enroll="true" >}}

This guide shows how to manage tag-based Custom Assembly with the [Chainguard Terraform provider](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest). You define overlays with the `chainguard_image_overlay` resource and bind them to repositories with the `chainguard_image_overlay_binding` resource.

For an explanation of overlays, bindings, and tag selectors, see [Customizing specific tags with Custom Assembly](/chainguard/containers/custom-assembly/tag-based-custom-assembly/).

## Prerequisites

Before you start, you need the following:

* Tag-based Custom Assembly enabled for your organization. Contact your Chainguard account team to enable it.
* Terraform and the Chainguard Terraform provider, version 0.4.6 or later. To configure the provider, see [Introduction to the Chainguard Terraform provider](/platform/administration/terraform-provider/).
* An identity with the `registry.overlays.edit` capability, such as one bound to the built-in `editor` or `owner` role.
* A repository in your organization with no standard Custom Assembly customization. A repository can't use both.

## Look up your organization and repository

Overlays belong to your organization, and bindings belong to a repository. Use data sources to look up their IDs:

```hcl
terraform {
  required_providers {
    chainguard = {
      source  = "chainguard-dev/chainguard"
      version = ">= 0.4.6"
    }
  }
}

data "chainguard_group" "org" {
  name = "example.com"
}

data "chainguard_image_repo" "python" {
  parent_id = data.chainguard_group.org.id
  name      = "python"
}

locals {
  python_repo_id = data.chainguard_image_repo.python.items[0].id
}
```

## Create overlays

Each `chainguard_image_overlay` resource defines a named set of packages. The following example defines two overlays:

```hcl
resource "chainguard_image_overlay" "typer" {
  parent_id = data.chainguard_group.org.id
  name      = "typer"
  packages  = ["py3.13-typer"]
}

resource "chainguard_image_overlay" "debug_tools" {
  parent_id = data.chainguard_group.org.id
  name      = "debug-tools"
  packages  = ["strace", "gdb"]
}
```

Package names can use the `{{major}}` and `{{minor}}` placeholders, as in `py{{major}}.{{minor}}-cryptography`. For details, see [Version templates in package names](/chainguard/containers/custom-assembly/tag-based-custom-assembly/#version-templates-in-package-names).

The `chainguard_image_overlay` resource supports packages only. To create an overlay with other customizations, such as certificates or environment variables, use [`chainctl`](/chainguard/containers/custom-assembly/tag-based-custom-assembly-chainctl/#add-other-customizations).

## Bind overlays to tags

Each `chainguard_image_overlay_binding` resource attaches one overlay to one repository. The `tag_selector` block chooses which tags the overlay applies to.

To apply an overlay to specific tags, set `kind` to `EXACT` and list the tags:

```hcl
resource "chainguard_image_overlay_binding" "typer" {
  repo_id    = local.python_repo_id
  overlay_id = chainguard_image_overlay.typer.id

  tag_selector {
    kind = "EXACT"
    tags = ["3.13", "3.13-dev"]
  }
}
```

To apply an overlay to every `-dev` tag, set `kind` to `VARIANT` and `variant_type` to `DEV`:

```hcl
resource "chainguard_image_overlay_binding" "debug_tools" {
  repo_id    = local.python_repo_id
  overlay_id = chainguard_image_overlay.debug_tools.id

  tag_selector {
    kind         = "VARIANT"
    variant_type = "DEV"
  }
}
```

To apply an overlay to every tag, set `kind` to `ALL`:

```hcl
tag_selector {
  kind = "ALL"
}
```

You can bind a given overlay to a repository only once. To apply an overlay to more tags, change its binding's selector instead of adding a second binding.

Run `terraform apply` to create the resources. Chainguard then rebuilds the matching tags. To check on the builds, run `chainctl images repos build list --repo python`.

## Change or remove customizations

The overlay and binding resources don't support in-place updates. When you change an overlay's name or packages, or a binding's selector, Terraform deletes the resource and creates a new one. Replacing an overlay also replaces its bindings.

Each replacement removes the customization before adding it back, so Chainguard might rebuild the affected tags twice: once without the customization and once with it. Review the plan before you apply changes to repositories that serve production traffic.

To remove a customization, delete the binding resource from your configuration and apply. Chainguard rebuilds the tags the binding matched, and they return to their uncustomized image. You can't delete an overlay while a binding still refers to it. Terraform removes the binding first when you delete both in one change.

## Learn more

* [Customizing specific tags with Custom Assembly](/chainguard/containers/custom-assembly/tag-based-custom-assembly/)
* [Managing tag-based Custom Assembly with chainctl](/chainguard/containers/custom-assembly/tag-based-custom-assembly-chainctl/)
* [`chainguard_image_overlay` in the Terraform Registry](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/resources/image_overlay)
* [`chainguard_image_overlay_binding` in the Terraform Registry](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/resources/image_overlay_binding)
