---
title: "How to Manage IAM Groups in Chainguard Enforce"
type: "article"
description: "Understanding Identity and Access Management in Chainguard Enforce"
date: 2022-15-07T15:22:20+01:00
lastmod: 2022-13-09T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 100
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Chainguard Enforce provides a rich Identity and Access Management (IAM) model similar to those used by AWS and GCP. Once authenticated, you can set up a desired structure for managing and delegating policies.

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