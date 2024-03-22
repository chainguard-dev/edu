---
title: "Overview of the Chainguard IAM Model"
linktitle: "IAM Overview"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/overview-of-enforce-iam-model/
type: "article"
description: "Overview of Chainguard Identity and Access Management"
lead: "Chainguard Identity and Access Management"
date: 2022-07-15T15:22:20+01:00
lastmod: 2024-03-21T15:22:20+01:00
draft: false
tags: ["Product", "Reference"]
images: []
menu:
  docs:
    parent: "iam-organizations"
weight: 005
toc: true
---

Chainguard provides a rich Identity and Access Management (IAM) model similar to those used by AWS and GCP. Once authenticated, you can set up a desired structure for managing and delegating Chainguard assets.

## Organizations and Folders

Chainguard's IAM model consists of two structures: **Organizations** and **Folders**. An organization is a customer or group of customers working with the same Chainguard resources, while a folder is a collection of resources within a Chainguard organization.

Organizations have a unique domain as their identifier and a user can belong to more than one organization. It's possible for organizations to become [verified organizations](/chainguard/administration/iam-groups/verified-orgs/). Verification modifies some aspects of the Chainguard platform user experience to help large organizations guide their user base to the correct resource. This optional process is performed manually by Chainguard, so if you're interested in verifying your organization, please reach out to your customer support contact. 

## Role Bindings

There are three built-in roles in Chainguard's IAM model that customers can assign to users or [assumable identities](/chainguard/administration/iam-organizations/assumable-ids/) in their organization:

* Owner
* Editor
* Viewer

You can review the capabilities of each of these roles by running `chainctl iam role list` in order to review the specific capabilities of each of these roles.

**Owner** is the role with the most privileges. An **owner** can create, delete, view (list), and modify (update) across images, policies, groups, account associations, role bindings, and subscriptions. Additionally, an **owner** can create, delete, and view clusters and group invites. An **owner** has read-only access to roles and records.

**Editor** is the role with read access and limited creation and modification access. An **editor** can create, delete, and view images, clusters, role bindings, and subscriptions. Additionally, an **editor** can modify role bindings and subscriptions. As opposed to the owner role, an **editor** can view images, policies, records, groups (and group invites), roles, and account association; but an **editor** cannot make changes to images, policies, records, groups, roles, and account associations. An editor cannot invite users to groups.

**Viewer** is a role that generally only has read-only access. That is, a **viewer** can list images, policies, groups (and group invites), clusters, records, roles and role bindings, subscriptions, and account associations.

Be aware that the `chainctl iam role list` command will return a few other role bindings besides these three. These are experimental roles or top-level roles managed by Chainguard and customers cannot assign them to users within their organization.
