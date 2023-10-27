---
title: "How to Manage Chainguard IAM Groups"
linktitle: "Manage IAM Groups"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/how-to-manage-iam-groups-in-chainguard-enforce/
type: "article"
description: "Understanding Identity and Access Management in Chainguard"
date: 2022-07-15T15:22:20+01:00
lastmod: 2023-10-26T15:22:20+01:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
menu:
  docs:
    parent: "iam-groups"
weight: 010
toc: true
---

Chainguard provides a rich Identity and Access Management (IAM) model similar to those used by AWS and GCP. Once authenticated, you can set up a desired structure for managing and delegating policies.

Each Chainguard policy needs to be associated with a **group**, and will be effective for that group as well as all the groups descending from it. Each cluster needs to be associated with a group and will be enforced based on that group’s policies.


## Logging in

To authenticate into the Chainguard platform, use the following login command.

```sh
chainctl auth login
```

A web browser window will open to prompt you to login via Google’s OIDC flow (more methods to authenticate are coming soon). Select an account with which you wish to register. Once authenticated, you can set up a desired group structure for managing and delegating policies.

## Creating a Group

Begin by creating an organization tied to the account you just used to authenticate to Chainguard.

```sh
chainctl iam groups create $NAME --no-parent
```

After creating the organization, you can create your desired group hierarchy. Keep in mind that policies roll down, meaning that any policy created at the root level will be inherited by its children.

```sh
chainctl iam group create $CHILD_NAME --parent $ROOT_ID
```

We recommend creating a group structure that outlines how your team organizes and delegates permissions.  A sample starting point can include dev, staging, and prod.

```sh
|- root
    |- dev
    |- staging
    |- prod
```


## Listing Groups

At any time, you can list the group hierarchy your account has access to by using `list`. To make it more human readable, you can output the information as a table by passing `-o table` to the end of the command.

```sh
chainctl iam groups list
```

You’ll get output regarding each of the groups you belong to, including a description of each group, if available.

```sh
 <Group ID> [tutorial-group] This is a shared IAM group for tutorials.
 <Group ID> [demo-group] This is a shared IAM group for running demos.
```

You can retrieve your groups' UIDPs by adding the `-o table` option to the previous `list` command.

```sh
chainctl iam groups list -o table
```
```
      ID     |      NAME      |    DESCRIPTION      
-------------+----------------+-----------------------------------------------
  <Group ID> | tutorial-group | This is a shared IAM group for tutorials.
  <Group ID> | demo-group     | This is a shared IAM group for running demos.  
```

Some other `chainctl` functions require you to know a group's UIDP, making this a useful option to remember.


## Inviting Others to a Group

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

Chainguard’s IAM ensures that you can set up policies specific to certain groups, and also allows you to manage your users and what access they have.
