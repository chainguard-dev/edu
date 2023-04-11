---
title: "Overview of the Enforce IAM Model"
type: "article"
description: "Chainguard Enforce Identity and Access Management"
lead: "Chainguard Enforce Identity and Access Management"
date: 2022-15-07T15:22:20+01:00
lastmod: 2022-15-07T15:22:20+01:00
draft: false
tags: ["Enforce", "Product", "Reference"]
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 620
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product by selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)._

Chainguard Enforce provides a rich Identity and Access Management (IAM) model similar to those used by AWS and GCP. Once authenticated, you can set up a desired structure for managing and delegating policies.

## Role Bindings

There are four role bindings in the Chainguard Enforce IAM model:
* Agentless
* Viewer
* Editor
* Owner

You can review the capabilities of each of these roles by running `chainctl iam role list` in order to review the specific capabilities of each of these roles.

**Agentless** is a cluster role that a tenant cluster needs to have in place so that it can subscribe to the SaaS Chainguard Enforce product.

**Owner** is the role with the most privileges. An **owner** can create, delete, view (list), and modify (update) across policies, groups, account associations, role bindings, and subscriptions. Additionally, an **owner** can create, delete, and view clusters and group invites. An **owner** has read-only access to roles and records.

**Editor** is the role with read access and limited creation and modification access. An **editor** can create, delete, and view clusters, role bindings, and subscriptions. Additionally, an **editor** can modify role bindings and subscriptions. As opposed to the owner role, an **editor** can view policies, records, groups (and group invites), roles, and account association; but an **editor** cannot make changes to policies, records, groups, roles, and account associations. An editor cannot invite users to groups.

**Viewer** is a role that generally only has read-only access. That is, a **viewer** can list policies, groups (and group invites), clusters, records, roles and role bindings, subscriptions, and account associations.