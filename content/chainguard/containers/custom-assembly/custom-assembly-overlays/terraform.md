---
title: "Managing Custom Assembly Overlays with Terraform"
linktitle: "Manage overlays with Terraform"
type: "article"
description: "How to use the Chainguard Terraform provider to create Custom Assembly overlays and bind them to repositories and tags."
date: 2026-09-28T16:33:22+00:00
lastmod: 2026-10-05T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Procedural", "Custom Assembly", "Automation"]
images: []
aliases:
- /chainguard/containers/custom-assembly/tag-based-custom-assembly-terraform/
- /chainguard/containers/custom-assembly/tag-based-custom-assembly/terraform/
menu:
  docs:
    parent: "custom-assembly-overlays"
weight: 20
toc: true
---

{{< beta feature="Custom Assembly Overlays" enroll="true" >}}

This guide shows how to manage Custom Assembly Overlays with the [Chainguard Terraform provider](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest). You define overlays with the `chainguard_image_overlay` resource and bind them to repositories with the `chainguard_image_overlay_binding` resource.

For an explanation of overlays, bindings, and tag selectors, see [Overview of Custom Assembly Overlays](/chainguard/containers/custom-assembly/custom-assembly-overlays/).

## Prerequisites

Before you start, you need the following:

* Tag-based Custom Assembly enabled for your organization. Contact your Chainguard account team to enable it.
* Terraform and the Chainguard Terraform provider, version 0.5.0 or later. To configure the provider, see [Introduction to the Chainguard Terraform provider](/platform/administration/terraform-provider/).
* An identity with the `registry.overlays.edit` capability, such as one bound to the built-in `editor` or `owner` role.
* A repository in your organization with no standard Custom Assembly customization. A repository can't use both.

## Look up your organization and repository

Overlays belong to your organization, and bindings belong to a repository, so you need the IDs of both. The following configuration requires the Chainguard provider and uses data sources to look up the `example.com` organization and its `python` repository:

```hcl
terraform {
  required_providers {
    chainguard = {
      source  = "chainguard-dev/chainguard"
      version = ">= 0.5.0"
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

The `chainguard_image_repo` data source returns a list of matching repositories. The `python_repo_id` local value holds the ID of the first match, which the binding examples later in this guide use.

## Create overlays

Each `chainguard_image_overlay` resource defines a named set of customizations. For an overlay that only adds packages, set the `packages` attribute. The following example defines two overlays that add packages:

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

Package names can use the `{{major}}` and `{{minor}}` placeholders, as in `py{{major}}.{{minor}}-cryptography`. For details, see [Version templates in package names](/chainguard/containers/custom-assembly/custom-assembly-overlays/#version-templates-in-package-names).

To add other customizations, such as certificates, environment variables, or annotations, set the `config` attribute instead of `packages`. An overlay can set one of the two, but not both. The `config` attribute takes a JSON-encoded configuration. Its field names follow the Chainguard API, not the YAML file that `chainctl` accepts, and some names differ. For example, the user an image runs as is `accounts.run_as` in `config` but `accounts.run-as` in a `chainctl` file. For the field names, see the [`chainguard_image_overlay` schema](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/resources/image_overlay).

The following example uses `jsonencode` to build an overlay that adds an internal certificate authority, an environment variable, and a package:

```hcl
resource "chainguard_image_overlay" "internal_ca" {
  parent_id = data.chainguard_group.org.id
  name      = "internal-ca"
  config = jsonencode({
    contents = {
      packages = ["curl"]
    }
    environment = {
      REQUESTS_CA_BUNDLE = "/etc/ssl/certs/ca-certificates.crt"
    }
    certificates = {
      additional = [{
        name    = "internal-ca"
        content = file("${path.module}/internal-ca.pem")
      }]
    }
  })
}
```

The `file` function reads the certificate from `internal-ca.pem` in the same directory as your configuration, so the certificate text doesn't need to appear in the configuration itself. For the full list of supported fields, see [Supported customizations](/chainguard/containers/custom-assembly/custom-assembly-overlays/#supported-customizations).

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

To create the overlays and bindings, apply the configuration:

```shell
terraform apply
```

After Terraform creates the bindings, Chainguard rebuilds the matching tags. To check on the builds, run `chainctl images repos build list --repo python --parent example.com`.

## Change or remove customizations

The overlay and binding resources don't support in-place updates. When you change an overlay's name, packages, or configuration, or a binding's selector, Terraform deletes the resource and creates a new one. Replacing an overlay gives it a new ID, so Terraform also replaces the bindings that refer to it.

Each replacement removes the customization before adding it back, so Chainguard might rebuild the affected tags twice: once without the customization and once with it. Review the plan before you apply changes to repositories that serve production traffic.

To remove a customization, delete the binding resource from your configuration and apply. Chainguard rebuilds the tags that the binding matched without the removed overlay. Any other matching overlays still apply. You can't delete an overlay while a binding still refers to it. Terraform removes the binding first when you delete both in one change.

## Learn more

* [Overview of Custom Assembly Overlays](/chainguard/containers/custom-assembly/custom-assembly-overlays/)
* [Managing Custom Assembly Overlays with chainctl](/chainguard/containers/custom-assembly/custom-assembly-overlays/chainctl/)
* [`chainguard_image_overlay` in the Terraform Registry](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/resources/image_overlay)
* [`chainguard_image_overlay_binding` in the Terraform Registry](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/resources/image_overlay_binding)
