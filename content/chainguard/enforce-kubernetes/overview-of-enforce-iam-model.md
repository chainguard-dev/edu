---
title: "Overview of Enforce IAM model"
type: "article"
description: "Chainguard Enforce Identity and Access Management"
lead: "Chainguard Enforce Identity and Access Management"
date: 2022-15-07T15:22:20+01:00
lastmod: 2022-15-07T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "enforce-kubernets"
weight: 620
toc: true
---

Chainguard Enforce provides a rich Identity and Access Management (IAM) model similar to the likes of AWS and GCP. Once authenticated, you can set up a desired structure for managing and delegating policies.

Each Chainguard Policy needs to be associated with a **group**, and will be effective for that Group as well as all the groups descending from it. Each Cluster needs to be associated with a Group and will be enforced based on that group’s policies.

To authenticate into the Chainguard Enforce platform, use the following login command.

```sh
chainctl auth login
```

A web browser window will open to prompt you to login via Google’s OIDC flow (more methods to authenticate are coming soon). Select an account with which you wish to register. Once authenticated, you can set up a desired group structure for managing and delegating policies.

Begin by creating a root group for your desired organization tied to the account you just used to authenticate to Chainguard Enforce.

```sh
chainctl iam groups create $NAME --no-parent
```

After creating the root group, you can create your desired group hierarchy. Keep in mind that policies roll down, meaning that any policy created at the root level will be inherited by its children.

```sh
chainctl iam group create $CHILD_NAME -parent $ROOT_ID
```

We recommend creating a group structure that outlines how your team organizes and delegates permissions.  A sample starting point can include dev, staging, and prod.

```sh
|- root
    |- dev
    |- staging
    |- prod
```

At any time, you can list the group hierarchy your account has access to by using `list`. To make it more human readable, you can output the information as a table by passing `-o table` to the end of the command.

```sh
chainctl iam groups list
```

You’ll get output regarding each of the groups you belong to, providing you with some information about each group.

```sh
 <Group ID> [tutorial-group] This is a shared IAM group for tutorials.
 <Group ID> [demo-group] This is a shared IAM group for running demos.
```

To invite others to a specific group, you can generate invite codes by creating invites to the group.

```sh
chainctl iam invite create $GROUP
```

You will be prompted for the scope that the invite code will be granted. After selecting the role bindings, the invite code will be generated.  If you ever lose the invite code, a list of active invite codes can be found by listing them with chainctl:

```sh
chainctl iam invite list
```

This will provide output in the form of a table with group ID, when the invitation to the group will expire, the group key ID, and the role.

```sh
ID  |        EXPIRATION        |    KEYID       |              ROLE
------------------------------------------------------------+--------------------------+--------------------------------------+---------------------------------
<Group ID> | 2022-10-15T17:16:39.449Z | xxxxx | [demo] Demo role
```

To invite team members, auditors, or others to your desired groups, securely distribute the invite code and have them log in with chainctl as follows.

```sh
chainctl auth login --invite-code $INVITE_CODE
```

Chainguard Enforce’s IAM ensures that you can set up policies specific to certain groups, and also allows you to manage your users and what access they have.

## Role Bindings

There are four role bindings in the Chainguard Enforce IAM model:
* Gulfstream
* Viewer
* Editor
* Owner

You can review the capabilities of each of these roles by running `chainctl iam role list` in order to review the specific capabilities of each of these roles.

**Gulfstream** is a cluster role that a tenant cluster needs to have in place so that it can subscribe to the SaaS Chainguard Enforce product.

**Owner** is the role with the most privileges. An **owner** can create, delete, view (list), and modify (update) across policies, groups, account associations, role bindings, and subscriptions. Additionally, an **owner** can create, delete, and view clusters and group invites. An **owner** has read-only access to roles and records.

**Editor** is the role with read access and limited creation and modification access. An **editor** can create, delete, and view clusters, role bindings, and subscriptions. Additionally, an **editor** can modify role bindings and subscriptions. As opposed to the owner role, an **editor** can view policies, records, groups (and group invites), roles, and account association; but an **editor** cannot make changes to policies, records, groups, roles, and account associations. An editor cannot invite users to groups.

**Viewer** is a role that generally only has read-only access. That is, a **viewer** can list policies, groups (and group invites), clusters, records, roles and role bindings, subscriptions, and account associations.


