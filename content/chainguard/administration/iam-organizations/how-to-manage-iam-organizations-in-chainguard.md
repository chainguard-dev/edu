---
title: "How to Manage Chainguard IAM Organizations"
linktitle: "Manage IAM Organizations"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/how-to-manage-iam-groups-in-chainguard-enforce/
- /chainguard/administration/iam-groups/how-to-manage-iam-groups-in-chainguard-enforce/
- /chainguard/administration/iam-groups/how-to-manage-iam-groups-in-chainguard/
type: "article"
description: "Using Identity and Access Management in Chainguard"
date: 2022-07-15T15:22:20+01:00
lastmod: 2024-04-03T15:22:20+01:00
draft: false
tags: ["Product", "Procedural"]
images: []
menu:
  docs:
    parent: "iam-organizations"
weight: 010
toc: true
---

Chainguard provides a rich Identity and Access Management (IAM) model similar to those used by AWS and GCP. This guide outlines how to manage Chainguard's IAM structures with the [`chainctl` command line tool](/chainguard/chainctl/). 

> **Note**: You should work with Chainguard's Customer Success team to create or delete organizations. This will help to ensure that no users lose access to resources and that your IAM structure is configured correctly.

## Logging in

To authenticate into the Chainguard platform, run the following login command.

```sh
chainctl auth login
```

A web browser window will open to prompt you to log in via your chosen OIDC flow. Select an account with which you wish to register. Once authenticated, you can set up an organization.


## Listing Organizations

At any time, you can list the organizations your account has access to by using the `list` subcommand. To make it more human readable, you can output the information as a table by passing `-o table` to the end of the command.

```sh
chainctl iam organizations list
```

You’ll get output regarding each of the organizations the user you're logged in as belongs to, including a description of each organization, if available.

```sh
[demo-org] This is a shared IAM organization for running demos
[tutorial-org] This is a shared IAM organization for tutorials.
```

You can retrieve your organizations' UIDPs by adding the `-o table` option to the previous `list` command.

```sh
chainctl iam organizations list -o table
```
```
          ID          |     NAME     |  	DESCRIPTION
----------------------+--------------+---------------------------------
  <Organization UIDP> | tutorial-org | This is a shared IAM
                      |              | organization for tutorials.
  <Organization UIDP> | demo-org     | This is a shared IAM
                      |              | organization for running demos
```

Some other `chainctl` functions require you to know an organization's UIDP, making this a useful option to remember.


## Inviting Others to an Organization

You can use `chainctl` to generate invite codes in order to invite others to a specific organization.

To do so, run the following command, making sure to replace `$ORGANIZATION` with the name of your chosen organization.

```sh
chainctl iam invite create $ORGANIZATION
```

You will be prompted for the scope that the invite code will be granted. After selecting the [role-bindings](/chainguard/administration/iam-groups/roles-role-bindings), this command will generate both an invite code and an invite link.  If you ever lose the invite code, you can retrieve a list of active invite codes with the following `chainctl` command:

```sh
chainctl iam invite list
```

This will provide output in the form of a table with the organization ID, a timestamp indicating when the invitation to the organization will expire, the invite code's key ID, and the selected role.

```
          ID          |        EXPIRATION        |     KEYID     |          	ROLE          	 
----------------------+--------------------------+---------------+---------------------------------
  <Organization UIDP> | 2024-03-23T00:55:04.813Z | <Invite code> | [editor] Editor            	 
```

Note that this invite code found under the `KEYID` column will be shorter than the one returned in the output of the `chainctl iam invite create` command, but they are effectively the same.

To invite team members, auditors, or others to your desired organizations, securely distribute the invite code and have them log in with chainctl as follows.

```sh
chainctl auth login --invite-code $INVITE_CODE
```

You can also securely distribute the invite link and have users open it in their web browser to log in and join the organization.

Note that you can tighten the scope of an invite code by including the `--email` and `--ttl` flags when creating the invite.

```sh
chainctl iam invite create $ORGANIZATION --email inky@example.com --ttl 24h
```

In this example, the invitation is scoped to a user with the email address `inky@example.com`. If someone with a different email address tries to use the code it will not work. The `--ttl` option in this example means that the code will expire in 24 hours.


## Learn more

In addition to inviting other users to your organization, you can set up [assumable identities]() to allow automation systems — like Buildkite or GitHub Actions — to perform certain administrative tasks for your organization. To learn more, we encourage you to check out our [Overview of Assumable Identities](/chainguard/administration/iam-groups/assumable-ids/) as well as our collection of [Assumable Identity Examples](/chainguard/administration/iam-groups/identity-examples/).

You may also be interested in setting up a [Custom Identity Provider](/chainguard/administration/custom-idps/custom-idps/) for your organization. By default, users can log in with GitHub GitLab, and Google, but a Custom IDP can allow members of your organization to log in to Chainguard with a corporate identity provider like [Okta](/chainguard/administration/custom-idps/okta/), [Azure Active Directory](/chainguard/administration/custom-idps/azure-ad/), or [Ping Identity](/chainguard/administration/custom-idps/ping-id/).
