---
title: "Overview of the Chainguard IAM Model"
linktitle: "IAM Overview"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/overview-of-enforce-iam-model/
- /chainguard/administration/iam-organizations/overview-of-enforce-iam-model/
type: "article"
description: "Overview of Chainguard Identity and Access Management"
lead: "Chainguard Identity and Access Management"
date: 2022-07-15T15:22:20+01:00
lastmod: 2024-04-03T15:22:20+01:00
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

Organizations have a unique domain as their identifier and a user can belong to more than one organization. It's possible for organizations to become [verified organizations](/chainguard/administration/iam-organizations/verified-orgs/). Verification modifies some aspects of the Chainguard platform user experience to help large organizations guide their user base to the correct resource. This optional process is performed manually by Chainguard, so if you're interested in verifying your organization, please reach out to your customer support contact. 

## Identities

In the context of Chainguard, an identity represents an individual user within an organization. Users typically join an organization after [being sent an invitation](https://edu.chainguard.dev/chainguard/administration/iam-organizations/how-to-manage-iam-organizations-in-chainguard/#inviting-others-to-an-organization). After receiving an invitation, the user can sign up with a Google, GitHub, or Gitlab account. In cases like this, the user's identity is the email address associated with the account they used to log in. 

> Note: If their organization has configured one, a user can sign up with a [custom identity provider](/chainguard/administration/custom-idps/custom-idps/).

In order to create an invitation for a new user, you must choose a role for that user and then create a role-binding to tie that user to the chosen role. Our [overview of roles and role-bindings](/chainguard/administration/iam-organizations/roles-role-bindings/) has more information.

You can also create assumable identities. These are typically used to allow automation tools like GitHub Actions or Amazon Lambda to connect to and manage Chainguard resources. Refer to our [guide on assumable identities](/chainguard/administration/iam-organizations/assumable-ids/) to learn more.


## Logging in to the Chainguard Platform

To authenticate into the Chainguard platform, run the following login command.

```sh
chainctl auth login
```

A web browser window will open to prompt you to log in via your chosen OIDC flow. Select the account which you wish to log in as, and you can then begin managing your Chainguard resources.

### Using the headless login flow

Note that you can also use `chainctl`'s `--headless` option to log in. This option allows you to log in to the Chainguard platform from a device that doesn't have a browser installed, such as a container or remote server.

The headless login flow is when you invoke `chainctl auth login --headless` in the terminal. 

```sh
chainctl auth login --headless
```

By including this option, `chainctl` will output an eight-character code as well as a URL ([`https://auth.chainguard.dev/activate`](https://auth.chainguard.dev/activate)). You can then navigate to the URL on another device's browser and enter the code, and then you can log in to Chainguard from that device.

Be aware that the `--headless` login code will only be valid for 900 seconds. 

