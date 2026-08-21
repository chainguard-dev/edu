---
title: "Overview of the Chainguard IAM model"
linktitle: "IAM overview"
aliases:
- /chainguard/administration/iam-organizations/overview-of-chainguard-iam-model/
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/overview-of-enforce-iam-model/
- /chainguard/administration/iam-organizations/overview-of-enforce-iam-model/
type: "article"
description: "Learn how Chainguard's identity and access management (IAM) model works with organizations, folders, and role-based access control for more secure resource management"
lead: "Chainguard's identity and access management (IAM) provides enterprise-grade access control for container registries and security resources through organizations, folders, and fine-grained permissions."
date: 2022-07-15T15:22:20+01:00
lastmod: 2026-08-21T16:30:07+00:00
draft: false
tags: ["Console", "Reference"]
images: []
menu:
  docs:
    parent: "iam-organizations"
weight: 005
toc: true
---

Chainguard's identity and access management (IAM) model enables more secure, fine-grained control over container registries and security resources, using familiar concepts from cloud providers like AWS and GCP. This enterprise-grade IAM system allows organizations to implement least-privilege access, delegate permissions, and integrate with existing identity providers for seamless authentication and authorization.

## Organizations and folders

Chainguard's IAM model consists of two structures: **Organizations** and **Folders**. An organization is a customer or group of customers working with the same Chainguard resources, while a folder is a collection of resources within a Chainguard organization.

Organizations have a unique domain as their identifier and a user can belong to more than one organization. It's possible for organizations to become [verified organizations](/platform/administration/iam-organizations/verified-orgs/). Verification modifies some aspects of the Chainguard platform user experience to help large organizations guide their user base to the correct resource. This optional process is performed manually by Chainguard, so if you're interested in verifying your organization, please reach out to your customer support contact.

## Identities

In the context of Chainguard, an identity represents an individual user within an organization. Users typically join an organization after [being sent an invitation](/platform/administration/iam-organizations/how-to-manage-iam-organizations-in-chainguard/#inviting-others-to-an-organization). After receiving an invitation, the user can sign up with a Google, GitHub, or Gitlab account. In cases like this, the user's identity is the email address associated with the account they used to log in.

> Note: If their organization has configured one, a user can sign up with a [custom identity provider](/platform/administration/custom-idps/custom-idps/).

In order to create an invitation for a new user, you must choose a role for that user and then create a role-binding to tie that user to the chosen role. Our [overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/) has more information.

You can also create assumable identities. These are typically used to allow automation tools like GitHub Actions or Amazon Lambda to connect to and manage Chainguard resources. Refer to our [guide on assumable identities](/platform/administration/assumable-ids/assumable-ids/) to learn more.

## Logging in to the Chainguard platform

You can authenticate to the Chainguard platform with `chainctl` in several ways, including interactive browser login, headless device-code login, social login providers, and assumable identities for CI/CD. For the full list of login flows and guidance on when to use each, see [Authentication options](/platform/chainctl-usage/authentication-options/).
