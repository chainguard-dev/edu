---
title : "Overview of Roles and Role-bindings in Chainguard"
linktitle: "Roles and Role-bindings Overview"
lead: ""
description: "An overview of Chainguard's identities, roles, and role-bindings, as well as instructions for how to manage roles and role-bindings with chainctl."
type: "article"
date: 2024-04-03T08:48:45+00:00
lastmod: 2024-04-03T08:48:45+00:00
draft: false
tags: ["chainctl", "Overview"]
images: []
weight: 005
---

In the context of Chainguard, an *identity* represents an individual user within an organization. Chainguard's IAM model allows administrators to assign identities to specialized *roles* which define the level of access that an identity has to the organization's resources. You assign a role by creating a *role-binding*, which is what ties an identity to a given role. 

This guide serves as an overview of what roles and role-bindings are within the context of Chainguard. It also outlines how you can manage roles and role-bindings with `chainctl`. 


## Prerequisites

This guide includes several examples of how you can manage roles and role-bindings with `chainctl`, the Chainguard command-line tool. To set up `chainctl`, follow our guide on [how to install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you haven't done so already.


## Roles

There are a number of built-in roles in Chainguard's IAM model that customers can assign to identities within their organization. Most users within your organization will likely have one of the following roles with broadly-defined privileges: `owner`, `editor`, `viewer`, or `console_viewer`.

`owner` is the role with the most privileges. An owner can create, delete, view (list), and modify (update) organizations, account associations, role-bindings, organization invitations, custom roles, role-bindings, and subscriptions. 

`editor` is the role with read access and limited creation and modification access. As opposed to the owner role, an editor can view images, policies, records, organizations, organization invites, roles, and account associations but cannot create or make changes to these resources. It can modify the state of event subscriptions, but cannot grant roles or permissions. Editors can also push and pull images, libraries, and APKs.

`viewer` is a role that generally only has read-only access. That is, a viewer can list images, policies, organizations (and organization invites), records, roles and role-bindings, subscriptions, and account associations.

`console_viewer` is a role designed for teams that need visibility into the Chainguard Console without any image pull access. A console viewer can browse the Console — viewing organizations, roles, and group information — but has no `registry.pull` or `apk.pull` permissions. This makes it a safe option for inviting developers, auditors, or stakeholders who need awareness of your organization's setup without the ability to pull images or APK packages.

The remaining roles are for more specialized functions. For example, `registry.pull`, `registry.push`, and `registry.pull_token_creator` relate to administering a registry of Chainguard products.

The `owner`, `editor`, and `viewer` roles are useful for user profiles that require broad, but clearly defined capabilities. The registry, container, and library roles have limited permissions, allowing them to manage only one specific Chainguard resource. These specialized, resource-specific roles grant minimal required access.

Every role has at least one of four capabilities (`create`, `list`, `update`, `delete`) in relation to at least one Chainguard resource. For example, the `apk.pull` role only grants `list` access for APK packages and groups. This means identities with this role can pull the organization's APK packages and retrieve information about the organization, but won't have general access to the organization's [Chainguard registry](/chainguard/chainguard-images/chainguard-registry/overview/) access. 

Chainguard's built-in default roles serve as building blocks and can be complemented with custom roles for specific use cases. Custom roles can extend or restrict default role capabilities, and offer or your organization greater flexibility, allowing you to mix default and custom roles based on your team's structure and needs.

When assigning a role, do so based on the principle of least privilege; assign only the role needed for the indentity's function. For example, CI systems should have a role like `registry.pull`, not `editor`.

You can run `chainctl iam roles list` to retrieve a list of all the roles available to your organization and review each of their specific capabilities. This command will list all the built-in roles as well as any custom roles created for your organization. The next section outlines how to create and manage such custom roles. 


## Managing custom roles

There are two options for managing custom roles:
- with [`chainctl`](#manage-custom-roles-with-chainctl), or
- directly [in the Chainguard Console](#manage-custom-roles-in-the-chainguard-console). 

### Manage custom roles with chainctl

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

You can also grant multiple capabilities to a custom role with one command, as in this example:

```sh
chainctl iam roles create puller-role --parent=example-org --capabilities=apk.list,groups.list,manifest.list,manifest.metadata.list,record_signatures.list,repo.list,sboms.list,tag.list,vuln.list
```

This example command creates a role named `puller-role` that has the following capabilities:

* `apk.list`
* `groups.list`
* `manifest.list`
* `manifest.metadata.list`
* `record_signatures.list`
* `repo.list`
* `sboms.list`
* `tag.list`
* `vuln.list`

This essentially combines the capabilities of the `registry.pull` and `apk.pull` roles, allowing any identities bound to this role to be able to pull both Chainguard Containers and APKs.

You can also use `chainctl` to delete custom roles.

```sh
chainctl iam roles delete new-role
```

Note that you cannot delete any of the built-in roles. Attempting to do so will result in an error.

### Manage custom roles in the Chainguard Console

In addition to using `chainctl` to manage roles, you can also create, view, and edit custom roles directly in the [Chainguard Console](https://console.chainguard.dev). 

#### Create  a custom role

1. In the Chainguard Console, navigate to **Settings** > **Roles**.
1. Click **Create Role**.
1. Enter a name and optional description for the new role.
1. Select the capabilities you want the role to include.
1. Click **Create**.

After creating a role, you can attach it to a user. Learn more under [Managing role-bindings](#managing-role-bindings).

#### Edit an existing custom role

1. Navigate to **Settings** > **Roles**.
2. Find the role you want to modify and click **Edit**.
3. Add or remove capabilities as needed.
4. Click **Save Changes**.

> **Note:** Changes to a custom role take effect immediately for all identities currently bound to that role. Built-in roles cannot be edited.

Both the Console and `chainctl` operate on the same underlying roles and role-bindings; changes made in either place are immediately reflected everywhere.


## Managing role-bindings

### Manage role bindings with chainctl

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

### Manage role bindings in the Chainguard Console

1. In the Chainguard Console, navigate to **Settings** > **Users**.
1. Click **Create role binding**.
1. Select a user and the role you want to attach to the user.
1. Click **Create**.

## Learn more

You can create a Chainguard identity for an automation system (such as Buildkite or GitHub Actions) to assume. This process involves choosing a role for the assumable identity and then creating a role-binding for it. Check out our [overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/) — as well as our [collection of assumable identity examples](/chainguard/administration/iam-organizations/identity-examples/) — to learn more.

If you'd like to learn more about Chainguard's IAM model and structures, we encourage you to read our [Overview of the Chainguard IAM Model](/chainguard/administration/iam-organizations/overview-of-enforce-iam-model/).
