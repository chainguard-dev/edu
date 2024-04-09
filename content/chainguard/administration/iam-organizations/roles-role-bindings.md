---
title : "Overview of Roles and Role-bindings in Chainguard"
linktitle: "Roles and Role-Bindings"
lead: ""
description: "An overview of Chainguard's identities, roles, and role-bindings, as well as instructions for how to manage roles and role-bindings with chainctl."
type: "article"
date: 2024-04-03T08:48:45+00:00
lastmod: 2024-04-03T08:48:45+00:00
draft: false
tags: ["chainctl", "Product", "Overview"]
images: []
weight: 012
---

In the context of Chainguard, an *identity* represents an individual user within an organization. Chainguard's IAM model allows administrators to assign identities to specialized *roles* which define the level of access that an identity has to the organization's resources. You assign a role by creating a *role-binding*, which is what ties an identity to a given role. 

This guide serves as an overview of what roles and role-bindings are within the context of Chainguard. It also outlines how you can manage roles and role-bindings with `chainctl`. 


## Prerequisites

This guide includes several examples of how you can manage roles and role-bindings with `chainctl`, the Chainguard command-line tool. To set up `chainctl`, follow our guide on [how to install `chainctl`](/chainguard/administration/how-to-install-chainctl/) if you haven't done so already.


## Roles

There are a number of built-in roles in Chainguard's IAM model that customers can assign to identities within their organization. 

`owner` is the role with the most privileges. An owner can create, delete, view (list), and modify (update) organizations, account associations, role-bindings, organization invitations, custom roles, role-bindings, and subscriptions. 

`editor` is the role with read access and limited creation and modification access. An editor can create, delete, and view images, clusters, role-bindings, and subscriptions. Additionally, an editor can modify role-bindings and subscriptions. As opposed to the owner role, an editor can view images, policies, records, organizations, organization invites, roles, and account associations but cannot create or make changes to these resources.

`viewer` is a role that generally only has read-only access. That is, a viewer can list images, policies, organizations (and organization invites), clusters, records, roles and role-bindings, subscriptions, and account associations.

The remaining roles are for more specialized functions. For example, `registry.pull`, `registry.push`, and `registry.pull_token_creator` relate to administering a Chainguard Registry.

You can run `chainctl iam roles list` to retrieve a list of all the roles available to your organization and review each of their specific capabilities. This command will list all the built-in roles as well as any custom roles created for your organization. The next section outlines how to create and manage such custom roles. 


## Managing custom roles

You can use `chainctl` to create custom roles for teams or individuals in your organization, like in the following example.

```sh
chainctl iam roles create my-role
```

After running this command, an interactive prompt will appear asking you to select what capabilities the new role should have and the organization under which the role should be created.

You can avoid using the interactive prompt by including the `--parent` and `--capabilities` options in this command. 

```sh
chainctl iam roles create new-role --parent=example-org --capabilities=roles.list
```

This example creates a new role named `new-role` under an organization named `example-org`. The new role will only have the ability to list roles in the organization.

You can also use `chainctl` to delete custom roles.

```sh
chainctl iam roles delete new-role
```

Note that you cannot delete any of the built-in roles. Attempting to do so will result in an error.


## Managing Role-bindings

You can assign a role — and all of its capabilities — to a given user by creating a role-binding and tying it to that user's identity. 

You can run a command like the following example to create a role-binding.

```sh
chainctl iam role-bindings create
```

This will start an interactive prompt where you can enter the appropriate details for this new role-binding. Specifically, you'll be prompted to specify the identity to bind, the role you want the identity bound to, and the organization that the role-binding should belong to. 

To avoid using the interactive prompt, you can add these details to the command by including the `--identity`, `--role`, and `--parent` options.

```sh
chainctl iam role-bindings create --identity=example-id --role=viewer --parent=example-org
```

This example creates a role-binding for the identity `example-id` with the built-in `viewer` role in an organization named `example-org`. 

Note that in order to use the `--identity` option like this, you will need to know the given identity's UIDP. You can find a list of all your identities' UIDPs by running `chainctl iam identities ls`. The identities' UIDPs will appear in the resulting `ID` column.


## Learn more

You can create a Chainguard identity for an automation system (such as Buildkite or GitHub Actions) to assume. This process involves choosing a role for the assumable identity and then creating a role-binding for it. Check out our [overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/) — as well as our [collection of assumable identity examples](/chainguard/administration/iam-organizations/identity-examples/) — to learn more.

If you'd like to learn more about Chainguard's IAM model and structures, we encourage you to read our [Overview of the Chainguard IAM Model](/chainguard/administration/iam-organizations/overview-of-enforce-iam-model/).
