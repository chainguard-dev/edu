---
title: "Managing tag-based Custom Assembly with chainctl"
linktitle: "Tag-based customization with chainctl"
type: "article"
description: "How to use chainctl to create overlays and bind them to specific tags of a Custom Assembly repository."
date: 2026-09-28T16:33:22+00:00
lastmod: 2026-09-28T16:33:22+00:00
draft: false
tags: ["Chainguard Containers", "Procedural", "Custom Assembly", "chainctl"]
images: []
menu:
  docs:
    parent: "features"
weight: 35
toc: true
---

{{< beta feature="Tag-based Custom Assembly" enroll="true" >}}

This guide shows how to use `chainctl` to apply Custom Assembly customizations to a subset of a repository's tags. You create an overlay that holds the customizations, then bind it to a repository with a tag selector.

For an explanation of overlays, bindings, and tag selectors, see [Customizing specific tags with Custom Assembly](/chainguard/containers/custom-assembly/tag-based-custom-assembly/).

## Prerequisites

Before you start, you need the following:

* Tag-based Custom Assembly enabled for your organization. Contact your Chainguard account team to enable it.
* A recent version of [`chainctl`](/platform/chainctl-usage/how-to-install-chainctl/). Run `chainctl update` to update it.
* A role with the `registry.overlays.edit` capability, such as the built-in `editor` or `owner` role.
* A repository in your organization with no standard Custom Assembly customization. A repository can't use both. To convert one, see [Moving a repository from standard Custom Assembly](#moving-a-repository-from-standard-custom-assembly).

The examples in this guide use the following environment variables. Set them to match your organization and repository:

```shell
export ORGANIZATION=example.com
export REPO=python
```

## Add a package to specific tags

This example adds `py3.13-typer` to the Python 3.13 tags only, so the other Python versions keep building.

1. Create an overlay that adds the package:

    ```shell
    chainctl images overlays create typer --parent $ORGANIZATION --package py3.13-typer
    ```

    ```output
    created overlay: typer (45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/1f4fcff90a5f0a02)
    ```

    To add more than one package, repeat `--package` or separate the names with commas.

1. Bind the overlay to the tags that should receive it. Pass `--tag` once for each tag:

    ```shell
    chainctl images overlays attach \
      --overlay typer \
      --repo $REPO \
      --parent $ORGANIZATION \
      --tag 3.13 --tag 3.13-dev
    ```

    ```output
    attached overlay "typer" to repo 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80 (binding 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80/9b8a7c6d5e4f3a21, selector EXACT [3.13 3.13-dev])
    ```

Chainguard starts rebuilding `3.13` and `3.13-dev` with the overlay applied. Only the tags you list are customized, even if other tags such as `3.13.7` or `latest` point to the same image. To keep those tags identical, list them too.

To check on the builds, see [Check the results](#check-the-results).

## Add a package to every `-dev` tag

To bind an overlay to every tag ending in `-dev`, including `-dev` tags published later, use `--variant dev` instead of `--tag`:

```shell
chainctl images overlays create debug-tools --parent $ORGANIZATION --package strace,gdb

chainctl images overlays attach \
  --overlay debug-tools \
  --repo $REPO \
  --parent $ORGANIZATION \
  --variant dev
```

## Add a package to every tag

To bind an overlay to every tag in a repository, use `--all`. Combined with the `{{major}}` and `{{minor}}` placeholders, one overlay can add the right version of a package to each tag:

```shell
chainctl images overlays create cryptography --parent $ORGANIZATION \
  --package 'py{{major}}.{{minor}}-cryptography'

chainctl images overlays attach \
  --overlay cryptography \
  --repo $REPO \
  --parent $ORGANIZATION \
  --all
```

The `3.12` tags receive `py3.12-cryptography`, the `3.14` tags receive `py3.14-cryptography`, and so on. Quote the package name so that your shell doesn't interpret the braces. For details on how Chainguard fills in the placeholders, see [Version templates in package names](/chainguard/containers/custom-assembly/tag-based-custom-assembly/#version-templates-in-package-names).

## Add other customizations

The `--package` flag only sets packages. To set environment variables, annotations, certificates, user accounts, or runtime repositories, write the overlay as a YAML file and pass it with `-f`. The file uses the same format as [`chainctl images repos build apply`](/chainguard/containers/custom-assembly/custom-assembly-chainctl/#applying-packages-non-interactively):

```shell
cat > internal-ca.yaml <<EOF
certificates:
  additional:
    - name: internal-ca
      content: |
        -----BEGIN CERTIFICATE-----
        <certificate contents>
        -----END CERTIFICATE-----
environment:
  REQUESTS_CA_BUNDLE: /etc/ssl/certs/ca-certificates.crt
EOF

chainctl images overlays create internal-ca --parent $ORGANIZATION -f internal-ca.yaml
```

When you pass both `-f` and `--package`, `chainctl` uses the file and ignores `--package`.

An overlay belongs to your organization, so you can bind the same overlay to many repositories. Run `attach` once for each repository:

```shell
for repo in python node go; do
  chainctl images overlays attach --overlay internal-ca --repo $repo --parent $ORGANIZATION --all
done
```

You can bind several overlays to one repository with the same kind of selector, as long as they don't set the same field to different values. For example, you can bind both `internal-ca` and `cryptography` to the `python` repository with `--all`. If two overlays conflict, `attach` fails and the error names the conflicting binding and field.

## List overlays and bindings

To list your organization's overlays, their customizations, and the bindings for each overlay, run the following command:

```shell
chainctl images overlays list --parent $ORGANIZATION
```

```output
overlay: debug-tools (id: 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/2a3b4c5d6e7f8091)
  packages: strace, gdb
  bindings:
    - repo: python (id: 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80)
      selector: VARIANT(DEV)
      id:   45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80/4d5e6f708192a3b4
overlay: typer (id: 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/1f4fcff90a5f0a02)
  packages: py3.13-typer
  bindings:
    - repo: python (id: 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80)
      selector: EXACT [3.13 3.13-dev]
      id:   45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80/9b8a7c6d5e4f3a21
```

The `id` under each binding is the binding ID, which you need to change or remove the binding. For output you can process with tools such as `jq`, add `-o json`.

## Change an overlay

To change an overlay's customizations, run `update` with the overlay's name or ID. The packages or file you pass replace the overlay's existing customizations completely, so include everything the overlay should contain:

```shell
chainctl images overlays update typer --package py3.13-typer,py3.13-rich
```

To change other customizations, pass a YAML file with `-f`:

```shell
chainctl images overlays update internal-ca -f internal-ca.yaml
```

To rename an overlay, pass `--name`:

```shell
chainctl images overlays update typer --name python-cli-tools
```

Chainguard rebuilds the matching tags in every repository the overlay is bound to.

## Change which tags a binding applies to

To change a binding's tag selector, run `update-binding` with the binding ID from `chainctl images overlays list`. The new selector replaces the old one:

```shell
chainctl images overlays update-binding $BINDING_ID --tag 3.13 --tag 3.13-dev --tag latest
```

Chainguard rebuilds newly matched tags with the overlay. Tags the binding no longer matches return to their uncustomized image.

You can only change a binding's selector. To bind a different overlay, or to move a binding to a different repository, remove the binding and create a new one.

## Remove a customization

To remove an overlay from a repository, run `detach` with the binding ID:

```shell
chainctl images overlays detach $BINDING_ID
```

Chainguard rebuilds the tags the binding matched, and they return to their uncustomized image.

To delete an overlay, first detach all of its bindings, then run `delete` with the overlay ID:

```shell
chainctl images overlays delete $OVERLAY_ID
```

If the overlay is still bound to a repository, `delete` fails and lists the bindings to detach. `delete` accepts only the overlay ID, not its name.

## Check the results

Bindings and overlay updates start builds automatically. To see the builds for a repository and the tags each build produced, run the following command:

```shell
chainctl images repos build list --repo $REPO
```

To see a build's logs, including the configuration it was built with, run the following command and select a build:

```shell
chainctl images repos build logs --repo $REPO
```

If a package can't be installed on a tag, that tag's build fails and the logs name the package. The other tags aren't affected. For more on these commands, see [Retrieving information about Custom Assembly containers](/chainguard/containers/custom-assembly/custom-assembly-chainctl/#retrieving-information-about-custom-assembly-containers).

## Moving a repository from standard Custom Assembly

A repository can't use standard and tag-based Custom Assembly at the same time. If you try to bind an overlay to a repository that has a standard customization, `attach` fails with this error:

```output
repository custom overlay and overlay binding not allowed
```

To move a repository to tag-based Custom Assembly without changing what its tags contain, follow these steps:

1. Save the repository's current customization to a file. Run `chainctl images repos build edit --repo $REPO`, copy the configuration from the editor into a file named `current.yaml`, and then close the editor without saving.
1. Create an overlay from the file:

    ```shell
    chainctl images overlays create $REPO-customization --parent $ORGANIZATION -f current.yaml
    ```

1. Remove the standard customization. Run `chainctl images repos build edit --repo $REPO`, delete every entry from the file, then save and confirm the change.
1. Bind the overlay to every tag:

    ```shell
    chainctl images overlays attach --overlay $REPO-customization --repo $REPO --parent $ORGANIZATION --all
    ```

Between steps 3 and 4, Chainguard might rebuild the repository without its customization. To keep that window short, run step 4 right after step 3.

If `attach` still fails after you remove the standard customization, contact your Chainguard account team.

## Learn more

* [Customizing specific tags with Custom Assembly](/chainguard/containers/custom-assembly/tag-based-custom-assembly/)
* [Managing tag-based Custom Assembly with Terraform](/chainguard/containers/custom-assembly/tag-based-custom-assembly-terraform/)
* [Using chainctl to manage Custom Assembly resources](/chainguard/containers/custom-assembly/custom-assembly-chainctl/)
