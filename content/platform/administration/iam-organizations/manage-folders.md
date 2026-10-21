---
title: "Organize repositories and access with folders"
linktitle: "Folders"
type: "article"
description: "Create IAM folders in a Chainguard organization, pull images from repositories in a folder, and scope pull tokens and role-bindings to a folder."
lead: "Use folders to group repositories inside your organization and to grant access to a subset of them."
date: 2026-10-21T00:00:00+00:00
lastmod: 2026-10-21T00:00:00+00:00
draft: false
tags: ["chainctl", "Procedural", "Reference"]
images: []
menu:
  docs:
    parent: "iam-organizations"
weight: 15
toc: true
---

A **folder** is a group of resources inside a Chainguard [organization](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/#organizations-and-folders). Folders can contain other folders, so you can build a hierarchy under your organization, for example to separate a team's images, or to stage images for testing before you use them in production.

Folders do two things:

* They **group repositories**. A repository in a folder has the folder's name in its path.
* They **scope access**. A role granted on a folder applies only to that folder and the folders inside it.

> **Note:** Earlier versions of Chainguard called organizations "groups" and folders "subgroups". The [Chainguard Terraform provider](/platform/administration/terraform-provider/) still uses the term "groups".

## Create and manage folders

Use `chainctl iam folders` to work with folders.

Create a folder under your organization. Use `--parent` to choose where it goes; to create a nested folder, name an existing folder as the parent:

```sh
chainctl iam folders create test --parent=example.com
```

List the folders in an organization:

```sh
chainctl iam folders list example.com
```

Describe, rename, or delete a folder:

```sh
chainctl iam folders describe test
chainctl iam folders update test --name=staging
chainctl iam folders delete test
```

Run any of these commands without a folder name to select one interactively.

## How repositories in a folder are addressed

A repository's path is your organization's name, followed by each folder above the repository, followed by the repository name:

```text
cgr.dev/<organization>/<folder>/<repository>:<tag>
cgr.dev/<organization>/<folder>/<nested-folder>/<repository>:<tag>
```

The **last** path segment is always the repository. Everything before it identifies the organization and the folders, from the outermost folder to the innermost one.

For example, with this layout:

```text
example.com
├── python            (repository)
└── test              (folder)
    └── python        (repository)
```

the two repositories are pulled as:

```sh
docker pull cgr.dev/example.com/python:latest        # repository at the organization root
docker pull cgr.dev/example.com/test/python:latest   # repository in the "test" folder
```

These are two separate repositories. An image in `test/python` isn't available at `example.com/python`, or the other way round.

Pulling doesn't create folders. If a path names a folder that doesn't exist, the pull fails.

To see which repositories a folder contains, list them with the folder as the parent:

```sh
chainctl images repos list --parent=test
```

## Grant access to a folder

Roles apply **downward**: a role granted on an organization or folder applies to that location and to every folder inside it. A role never applies upward to a parent, or sideways to another folder.

| Where the role-binding is | It covers |
|---|---|
| The organization (`example.com`) | Every repository in the organization, including every folder |
| A folder (`example.com/test`) | Repositories in `test` and in folders inside `test` only |

### Pull tokens

A pull token can pull from the location it's created in and from every folder below it.

To use **one token for the whole organization**, including all of its folders, create it at the organization:

```sh
chainctl auth pull-token create --parent=example.com
```

To limit a token to **one folder**, create it at that folder:

```sh
chainctl auth pull-token create --parent=test
```

A token created at a folder can't pull repositories at the organization root or in other folders.

### Role-bindings

To give an existing identity pull access to a single folder, bind the `registry.pull` role at that folder:

```sh
chainctl iam role-bindings create --parent=test --identity=<identity-uidp> --role=registry.pull
```

An identity that already has `registry.pull` at the organization doesn't need an extra binding on the folder. The organization binding already covers it.

For more about roles, refer to [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

## Custom Assembly in folders

[Custom Assembly](/chainguard/containers/custom-assembly/) works on repositories in folders, and [overlays](/chainguard/containers/custom-assembly/overlays/overview/) can be bound to every repository in a folder.

Currently, a Custom Assembly build for a repository in a folder can only use packages from images that have been added to that same folder, not every package your organization is entitled to. If a build in a folder fails to resolve a package that's available to your organization, build the customized image at the organization root instead, or contact Chainguard support.

## Troubleshooting

If a pull from a folder fails, check these in order:

1. **The path.** Confirm each folder in the path exists and the repository is in the innermost one: `chainctl iam folders list <organization>`, then `chainctl images repos list --parent=<folder>`.
2. **Where the token or role-binding lives.** List pull tokens with `chainctl auth pull-token list`, and role-bindings with `chainctl iam role-bindings list --parent=<organization>`, which includes bindings in every folder below it. The binding must be at the folder or at a location above it, such as the organization.
3. **Mirrors and proxies.** If you pull through an artifact manager such as Artifactory, include the folder in the upstream path it requests from `cgr.dev`.

## Learn more

* [Overview of the Chainguard IAM model](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/)
* [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/)
* [Authenticating to the Chainguard registry](/chainguard/containers/registry/authenticating/)
* [`chainctl iam folders` reference](/platform/chainctl/chainctl-docs/chainctl_iam_folders/)
