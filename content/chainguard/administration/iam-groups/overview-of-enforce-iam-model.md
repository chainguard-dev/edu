---
title: "Overview of the Chainguard IAM Model"
linktitle: "IAM Overview"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/overview-of-enforce-iam-model/
type: "article"
description: "Chainguard Identity and Access Management"
lead: "Chainguard Identity and Access Management"
date: 2022-07-15T15:22:20+01:00
lastmod: 2023-12-07T15:22:20+01:00
draft: false
tags: ["Product", "Reference"]
images: []
menu:
  docs:
    parent: "iam-groups"
weight: 005
toc: true
---

Chainguard provides a rich Identity and Access Management (IAM) model similar to those used by AWS and GCP. Once authenticated, you can set up a desired structure for managing and delegating Chainguard assets.

## Role Bindings

There are four built-in role bindings in Chainguard's IAM model (excluding expiremental roles):

* Owner
* Editor
* Viewer
* Gulfstream

You can review the capabilities of each of these roles by running `chainctl iam role list` in order to review the specific capabilities of each of these roles.

**Owner** is the role with the most privileges. An **owner** can create, delete, view (list), and modify (update) across images, policies, groups, account associations, role bindings, and subscriptions. Additionally, an **owner** can create, delete, and view clusters and group invites. An **owner** has read-only access to roles and records.

**Editor** is the role with read access and limited creation and modification access. An **editor** can create, delete, and view images, clusters, role bindings, and subscriptions. Additionally, an **editor** can modify role bindings and subscriptions. As opposed to the owner role, an **editor** can view images, policies, records, groups (and group invites), roles, and account association; but an **editor** cannot make changes to images, policies, records, groups, roles, and account associations. An editor cannot invite users to groups.

**Viewer** is a role that generally only has read-only access. That is, a **viewer** can list images, policies, groups (and group invites), clusters, records, roles and role bindings, subscriptions, and account associations.

**Gulfstream** is a role used for Chainguard's proprietary controller infrastructure, also known as Gulfstream. You can check out our [Gulfstream Overview](/chainguard/chainguard-enforce/concepts/gulfstream-overview/) to learn more about how Gulfstream works.