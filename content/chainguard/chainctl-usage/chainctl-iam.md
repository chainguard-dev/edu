---
title: "Manage Identity and Access with chainctl"
lead: "Chainguard's chainctl iam commands provide enterprise-grade identity and access management for container registries and security resources."
description: "Learn how to use chainctl iam commands to manage identity, access controls, and role-based permissions for Chainguard's container security platform"
type: "article"
date: 2025-03-06T08:49:15+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["chainctl", "iam"]
images: []
weight: 060
---

Chainguard's identity and access management (IAM) system provides fine-grained control over container registries, security resources, and organizational permissions. The `chainctl iam` commands enable you to manage users, roles, identities, and access policies programmatically for enhanced security and compliance.

For the following, assume that returned information only includes that which your account has permissions to view. Also, actions such as `create` and `delete` are similarly limited.

This page is intended as an introductory overview of IAM with chainctl. For a full reference of all commands with details and switches, see [chainctl Reference](/chainguard/chainctl/).


## List Folders

Folders contain the catalogs of things your organization has access to.

Find out what folders are available to your organization with:

```Shell
chainctl iam folders list $ORGANIZATION_NAME
```

For example, for our Developer Enablement team, which uses the `chainguard.edu` organization, the interaction looks like this:

```Shell
$ chainctl iam folders list chainguard.edu
[chainguard.edu] Developer Enablement images catalog
```

This command can also delete, describe, and update folders by replacing `list` with `delete`, `describe`, or `update`. See the reference guide for more details.


## List and Describe Identities

To list all of the existing identities along with roles, types, and more, use:

```Shell
chainctl iam identities list
```

Because this command requests a large amount of information, you may find it useful to direct the output into a file or pipe it into a filter. If you know the specific `IDENTITY_NAME` or `IDENTITY_ID` that you want to know more about, use:

```Shell
chainctl iam identities describe {IDENTITY_NAME | IDENTITY_ID}
```

This command can also create, delete, describe, and update identities by replacing `list` with `create`, `delete`, `describe`, or `update`. See the reference guide for more details.


## List and Create Identity Providers

This command enables you to manage your own identity management provider, such as a custom OIDC provider. To list all currently configured identity management providers, use:

```Shell
chainctl iam identity-providers list
```

This command can also create, delete, and update your organization's identity providers by replacing `list` with `create`, `delete`, or `update`. See the reference guide for more details.

To tell chainctl about your OIDC provider and enable users to start using it, use create:

```Shell
chainctl iam identity-provider create --name=google --parent=example \
--oidc-issuer=https://accounts.google.com \
--oidc-client-id=foo \
--oidc-client-secret=bar \
--default-role=viewer
```


## List and Create Invites

This command lets you manage invite codes that register identities with Chainguard. To list current invites, use:

```Shell
chainctl iam invites list
```

This will return a list of invites by ID with information about the invite's expiration date, associated roles, and keyID.

This command can also create and delete invites by replacing `list` with `create` or `delete`. See the reference guide for more details.

To create a new invite, use create, like in this example that defines a role, an email address to tie the invite to, the valid length of the invitation, and that it can only be used once:

```Shell
chainctl iam invite create ORGANIZATION_NAME
--role=viewer
--email=sandra@organization.dev
--ttl=7d
--single-use
```


## List organizations

To list all of the organizations your account is associated with, use:

```Shell
chainctl iam organizations list
```

Most users will only be associated with one organization, but admin and support users may find using this command especially useful to determine whether they have needed permissions to interact with specific organizations when help is needed.

This command can also delete and describe organizations by replacing `list` with `delete` or `describe`. See the reference guide for more details.


## List roles

To list all of the roles your account is associated with, use:

```Shell
chainctl iam roles list
```

This command can also create, delete, and update identities by replacing `list` with `create`, `delete` or `update`.

It is possible to define role details during creation or create a role interactively. To create a role interactively, use:

```Shell
chainctl iam roles create ROLE_NAME
```


To find out what actions can be done by each role, use:

```Shell
chainctl iam roles capabilities list
```

This returns a list like this sample:

```Shell
$ chainctl iam roles capabilities list
         RESOURCE        |                 ACTION                  
-------------------------+-----------------------------------------
  account_associations   | create, delete, list, update            
  attestations           | list                                    
  build_report           | list                                    
  clusters               | create, delete, discover, list, update  
  group_invites          | create, delete, list                    
  groups                 | create, delete, list, update            
  identity               | create, delete, list, update            
  identity_providers     | create, delete, list, update            
  libraries.entitlements | create, delete, list                    
  libraries.java         | list                                    
  libraries.python       | list                                    
  manifest               | create, delete, list, update            
  manifest.metadata      | list                                    
  namespaces             | list                                    
  nodes                  | list                                    
  policy                 | create, delete, list, update            
  record_contexts        | list                                    
  record_policy_results  | list                                    
  record_signatures      | list                                    
  records                | list                                    
  registry.entitlements  | list                                    
  repo                   | create, delete, list, update            
  risks                  | list                                    
  role_bindings          | create, delete, list, update            
  roles                  | create, delete, list, update            
  sboms                  | list                                    
  sigstore               | create, delete, list, update            
  sigstore.certificate   | create                                  
  subscriptions          | create, delete, list, update            
  tag                    | create, delete, list, update            
  version                | list                                    
  vuln                   | create                                  
  vuln_report            | create, list                            
  vuln_reports           | list                                    
  workloads              | list 
  ```

To find out about role bindings, use:

```Shell
chainctl iam role-bindings list
```

The `chainctl iam role-bindings` command can also create, delete, and update identities by replacing `list` with `create`, `delete` or `update`.

