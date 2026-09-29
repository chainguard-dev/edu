---
title: "Managing tag-based Custom Assembly with chainctl"
linktitle: "Customize tags with chainctl"
type: "article"
description: "How to use chainctl to create overlays and bind them to specific tags of a Custom Assembly repository."
date: 2026-09-28T16:33:22+00:00
lastmod: 2026-09-29T14:47:57+00:00
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

This guide shows how to use `chainctl` to apply Custom Assembly customizations to some of a repository's tags. You create an overlay that holds the customizations, then bind it to a repository with a tag selector.

For an explanation of overlays, bindings, and tag selectors, see [Overview of tag-based Custom Assembly](/chainguard/containers/custom-assembly/tag-based-custom-assembly/).

## Prerequisites

Before you start, you need the following:

* Tag-based Custom Assembly enabled for your organization. Contact your Chainguard account team to enable it.
* A recent version of [`chainctl`](/platform/chainctl-usage/how-to-install-chainctl/). Run `chainctl update` to update it.
* A role with the `registry.overlays.edit` capability, such as the built-in `editor` or `owner` role.
* A repository in your organization with no standard Custom Assembly customization. A repository can't use both. To move a repository from standard Custom Assembly, contact your Chainguard account team.

The examples in this guide use the following environment variables. Set them to match your organization and repository:

```shell
export ORGANIZATION=example.com
export REPO=python
```

The examples add Python packages to the `python` repository, but the same commands work for any repository.

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

Chainguard starts rebuilding `3.13` and `3.13-dev` with the overlay applied. It customizes only the tags you list, even if other tags such as `3.13.7` or `3.13.7-r0` point to the same image. To keep those tags identical, list them too.

To check on the builds, see [Check the results](#check-the-results).

## Add packages to every `-dev` tag

To bind an overlay to every tag ending in `-dev`, use `--variant dev` instead of `--tag`. The following commands create an overlay with two debugging tools and bind it to the repository's `-dev` tags:

```shell
chainctl images overlays create debug-tools --parent $ORGANIZATION --package strace,gdb

chainctl images overlays attach \
  --overlay debug-tools \
  --repo $REPO \
  --parent $ORGANIZATION \
  --variant dev
```

The binding also applies to `-dev` tags published after you create it, so new versions get `strace` and `gdb` without any further changes.

## Add a package to every tag

To bind an overlay to every tag in a repository, use `--all`. The following commands create an overlay that adds `curl` and bind it to every tag:

```shell
chainctl images overlays create curl --parent $ORGANIZATION --package curl

chainctl images overlays attach \
  --overlay curl \
  --repo $REPO \
  --parent $ORGANIZATION \
  --all
```

As with a variant binding, an all binding also applies to tags published after you create it.

## Add the matching package version to every tag

Some packages include a language version in their name, so no single package name works on every tag. The `{{major}}` and `{{minor}}` placeholders solve this: Chainguard replaces them with each tag's version when it builds the tag. The following commands add the `cryptography` package that matches each tag's Python version:

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

The `--package` flag sets only packages. To set environment variables, annotations, certificates, user accounts, or runtime repositories, write the overlay as a YAML file and pass it with `-f`. The file uses the same format as [`chainctl images repos build apply`](/chainguard/containers/custom-assembly/custom-assembly-chainctl/#applying-packages-non-interactively).

The following commands write an overlay that adds an internal certificate authority and an environment variable, then create the overlay from the file:

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

If you pass both `-f` and `--package`, `chainctl` uses the file and ignores `--package`.

An overlay belongs to your organization, so you can bind it to many repositories. The following loop binds `internal-ca` to every tag of three repositories:

```shell
for repo in python node go; do
  chainctl images overlays attach --overlay internal-ca --repo $repo --parent $ORGANIZATION --all
done
```

Each repository gets its own binding, and each binding starts a rebuild of that repository.

You can bind several overlays to one repository with the same kind of selector, as long as they don't set the same field to different values. For example, you can bind both `internal-ca` and `cryptography` to the `python` repository with `--all`. If two overlays conflict, `attach` fails. For example, binding a second overlay that sets `REQUESTS_CA_BUNDLE` to a different value returns an error that names the existing binding and the conflicting field:

```output
Error: attaching overlay: rpc error: code = FailedPrecondition desc = Precondition failed: overlay config does not merge commutatively with co-matching binding(s): binding "45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80/b7d24dbd7193c219" (overlay "internal-ca", selector ALL) on fields [environment["REQUESTS_CA_BUNDLE"]]
```

To resolve the conflict, change one of the overlays so that they agree, or bind them with selectors that don't match the same tags.

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

Each binding's `id` is its binding ID. You need it to change or remove the binding. To get output you can process with tools such as `jq`, add `-o json`.

## Change an overlay

To change an overlay's customizations, run `update` with the overlay's name or ID. The packages or file you pass replace the overlay's existing customizations completely, so include everything the overlay should contain.

> **Note**: `--package` replaces the whole overlay, not only its packages. If you created the overlay from a file, for example with certificates or environment variables, running `update` with `--package` removes those customizations. To keep them, update the file and pass it with `-f`.

The following command replaces the packages in the `typer` overlay:

```shell
chainctl images overlays update typer --package py3.13-typer,py3.13-rich
```

```output
updated overlay: typer (45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/1f4fcff90a5f0a02)
```

To change other customizations, pass a YAML file with `-f`:

```shell
chainctl images overlays update internal-ca -f internal-ca.yaml
```

To rename an overlay, pass `--name`:

```shell
chainctl images overlays update debug-tools --name dev-debug-tools
```

Bindings refer to overlays by ID, so renaming an overlay doesn't affect its bindings.

Chainguard rebuilds the matching tags in every repository the overlay is bound to.

## Change which tags a binding applies to

To change a binding's tag selector, run `update-binding` with the binding's ID. Set `BINDING_ID` to the `id` shown for the binding in `chainctl images overlays list`:

```shell
export BINDING_ID=45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80/9b8a7c6d5e4f3a21
```

The following command replaces the binding's selector, adding `3.13.7` to the tags it applies to:

```shell
chainctl images overlays update-binding $BINDING_ID --tag 3.13 --tag 3.13-dev --tag 3.13.7
```

```output
updated overlay binding 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80/9b8a7c6d5e4f3a21 (selector EXACT [3.13 3.13-dev 3.13.7])
```

Chainguard rebuilds the affected tags. Newly matched tags receive the overlay, and tags that no longer match are rebuilt without it. Any other matching overlays still apply.

The selector is the only part of a binding you can change. To bind a different overlay, or to move a binding to another repository, remove the binding and create a new one.

## Remove a customization

To remove an overlay from a repository, run `detach` with the binding ID:

```shell
chainctl images overlays detach $BINDING_ID
```

```output
detached overlay binding 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/7c3e5a1b2d4f6e80/9b8a7c6d5e4f3a21
```

Chainguard rebuilds the tags that the binding matched without the detached overlay. Any other matching overlays still apply.

To delete an overlay, detach all of its bindings first. Then run `delete` with the overlay's name or ID:

```shell
chainctl images overlays delete typer
```

```output
deleted overlay 45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/1f4fcff90a5f0a02
```

If the overlay is still bound to a repository, `delete` fails and lists the bindings to detach. If more than one overlay you can access has the same name, pass the overlay's ID instead, shown next to its name in `chainctl images overlays list`.

## Check the results

Bindings and overlay updates start builds automatically. To see the builds for a repository and the tags each build produced, run the following command:

```shell
chainctl images repos build list --repo $REPO --parent $ORGANIZATION
```

The following command shows a build's logs, including the configuration Chainguard built it with. Select a build when prompted:

```shell
chainctl images repos build logs --repo $REPO --parent $ORGANIZATION
```

If a package can't be installed on a tag, that tag's build fails and the logs name the package. The failure doesn't affect other tags. For more on these commands, see [Retrieving information about Custom Assembly containers](/chainguard/containers/custom-assembly/custom-assembly-chainctl/#retrieving-information-about-custom-assembly-containers).

## Learn more

* [Overview of tag-based Custom Assembly](/chainguard/containers/custom-assembly/tag-based-custom-assembly/)
* [Managing tag-based Custom Assembly with Terraform](/chainguard/containers/custom-assembly/tag-based-custom-assembly-terraform/)
* [Using chainctl to manage Custom Assembly resources](/chainguard/containers/custom-assembly/custom-assembly-chainctl/)
