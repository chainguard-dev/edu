---
title: "chainctl iam"
lead: ""
description: "chainctl iam basics"
type: "article"
date: 2025-03-0620T08:49:15+00:00
lastmod: 2025-03-0620T08:49:15+00:00
draft: false
tags: ["chainctl", "iam", "Product", "authentication", "access", "identity", "management"]
images: []
weight: 60
---

This page presents some of the more commonly used `chainctl iam` commands. These commands all relate to identity and access management (IAM), enabling your organization to control access to various resources and actions.

For a full reference of all commands with details and switches, see [chainctl Reference](/chainguard/chainctl/).

For the following, assume that returned information only includes that which your account has permissions to view. Also, actions such as `create` and `delete` are similarly limited.


## chainguard iam folders

Find out what folders are available to your organization with:

```shell
chainctl iam folders list $ORGANIZATION_NAME
```

For example, for our Developer Enablement team, which uses the `chainguard.edu` organization, the interaction looks like this:

```shell
$ chainctl iam folders list chainguard.edu
[chainguard.edu] Developer Enablement images catalog
```

This command can also delete, describe, and update folders by replacing `list` with `delete`, `describe`, or `update`. See the reference guide for more details.


## chainguard iam identities

To list all of the existing identities along with roles, types, and more, use:

```shell
chainctl iam identities list
```

This command can also create, delete, describe, and update identities by replacing `list` with `create`, `delete`, `describe`, or `update`. See the reference guide for more details.


## chainguard iam identity-providers

This command enables you to manage your own identity management provider, such as a custom OIDC provider. To list all currently configured identity management providers, use:

```shell
chainctl iam identity-providers list
```

This command can also create, delete, and update identity providers by replacing `list` with `create`, `delete`, or `update`. See the reference guide for more details.


## chainguard iam invites

This command lets you manage invite codes that register identities with Chainguard. To list current invites, use:

```shell
chainctl iam invites list
```

This will return a list of invites by ID with information about the invite's expiration date, associated roles, and keyID.


This command can also create and delete invites by replacing `list` with `create` or `delete`. See the reference guide for more details.


## chainctl iam organizations

To list all of the organizations your account is associated with, use:

```shell
chainctl iam organizations list
```

This command can also delete and describe organizations by replacing `list` with `delete` or `describe`. See the reference guide for more details.


## chainctl iam roles

To list all of the roles your account is associated with, use:

```shell
chainctl iam roles list
```

This command can also create, delete, and update identities by replacing `list` with `create`, `delete` or `update`.

To find out what actions can be done by each role, use:

```shell
chainctl iam roles capabilities list
```

To find out about role bindings, use:

```shell
chainctl iam role-bindings list
```

This command can also create, delete, and update identities by replacing `list` with `create`, `delete` or `update`.

See the reference guide for more details on each of these commands.
