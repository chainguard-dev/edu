---
title: "Built-in Roles and Capabilities Reference"
linktitle: "Built-in Roles & Capabilities"
lead: "Reference for Chainguard's built-in roles and their specific capabilities"
description: "A resource documenting the capabilities and permissions of Chainguard's built-in IAM roles."
type: "article"
date: 2025-08-14T00:00:00Z
lastmod: 2025-08-14T00:00:00Z
draft: false
tags: ["IAM", "Reference", "Product"]
images: []
weight: 010
---

Chainguard provides customers with a set of built-in roles as part of its Identity and Access Management (IAM) system. These roles have different permissions and capabilities that allow them to serve specialized purposes, from general administrative access to access for specific resources like registries, APK packages, and programming language libraries.

This reference provides an overview of all Chainguard IAM capabilities and shows which built-in roles include each capability. Each capability represents a specific permission or action that can be performed within the Chainguard platform.

For more information on roles and role-bindings within Chainguard's IAM model, please refer to our [Overview of Roles and Role-bindings](/chainguard/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).


## Built-in Roles Summary

This guide outlines the built-in Chainguard IAM roles available to most customer organizations. You can find more info about specific roles in your organization with the following `chainctl` command:

```shell
chainctl iam roles list
```

Every role has at least one of four capabilities (`create`, `list`, `update`, `delete`) in relation to at least one Chainguard resource. For example, the `owner` role can create, delete, list, and update custom roles within Chainguard, while the `viewer` role can only list them. 

This guide outlines the following twelve built-in roles provided by Chainguard:

* **Administrative Roles:**
    * `owner` - Full administrative access with all capabilities
    * `editor` - Limited administrative access with mostly read permissions and event management
    * `viewer` - Read-only access across all resources
* **Registry and Container Roles:**
    * `registry.pull` - Container image access
    * `registry.pull_token_creator` - Chainguard registry token management with additional repository capabilities
    * `apk.pull` - Access to the organization's APK packages, including the private APK repository
* **Library Roles:**
    * `libraries.java.pull` - Java library access
    * `libraries.java.pull_token_creator` - Java token management
    * `libraries.python.pull` - Python library access
    * `libraries.python.pull_token_creator` - Python library token management
    * `libraries.javascript.pull` - JavaScript library access
    * `libraries.javascript.pull_token_creator` - JavaScript library token management

The administrative roles are useful for user profiles that require broad, but clearly defined capabilities. The registry, container, and library roles have limited permissions, allowing them to manage only one specific Chainguard resource. These specialized, resource-specific roles grant minimal required access.

For example, the `apk.pull` role only grants `list` access for APK packages and groups. This means identities with this role can pull the organization's APK packages and retrieve information about the organization, but won't have general access to the organization's [Chainguard registry](/chainguard/chainguard-images/chainguard-registry/overview/) access. 


## Chainguard Role Capabilities

The following table maps Chainguard resources to the built-in roles that have permissions for them. Each row represents a specific resource type (like `apk`, `repo`, `identity`, etc.), describes its purpose, and lists which built-in roles have what capabilities (create, delete, list, update) for that resource.

<div style="overflow-x: auto;">

| Resource | Purpose | Roles with access to this resource |
|------------|---------|---------------------------|
| `account_associations` | Link cloud provider accounts to organization | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li></ul> |
| `apk` | Manage APK packages in the registry | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`apk.pull` (list)</li></ul> |
| `build_report` | Access detailed build and scan reports for images and packages | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li></ul> |
| `group_invites` | Send and manage invitations to join Chainguard organization | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li></ul> |
| `groups` | Manage organization and hierarchical structures | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li></ul> |
| `identity` | Create and manage user identities and service accounts | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull_token_creator` (create)</li><li>`libraries.java.pull_token_creator` (create)</li><li>`libraries.python.pull_token_creator` (create)</li><li>`libraries.javascript.pull_token_creator` (create)</li></ul> |
| `identity_providers` | Configure [custom identity providers](/chainguard/administration/custom-idps/custom-idps/) (OIDC, SAML) for authentication | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li></ul> |
| `libraries.artifacts` | View Chainguard Library artifact metadata and information | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li></ul> |
| `libraries.entitlements` | Manage access permissions for Chainguard Libraries | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`libraries.java.pull` (list)</li><li>`libraries.python.pull` (list)</li><li>`libraries.javascript.pull` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li></ul> |
| `libraries.java` | Access [Chainguard Libraries for Java](/chainguard/libraries/java/overview/) | <ul><li>`owner` (list)</li><li>`libraries.java.pull` (list)</li><li>`libraries.java.pull_token_creator` (list)</li></ul> |
| `libraries.javascript` | Access Chainguard Libraries for JavaScript | <ul><li>`owner` (list)</li><li>`libraries.javascript.pull` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li></ul> |
| `libraries.python` | Access [Chainguard Libraries for Python](/chainguard/libraries/python/overview/) | <ul><li>`owner` (list)</li><li>`libraries.python.pull` (list)</li><li>`libraries.python.pull_token_creator` (list)</li></ul> |
| `manifest` | Access and manage container image manifests | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (create, delete, list, update)</li></ul> |
| `manifest.metadata` | View container image manifest metadata and attestations | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li></ul> |
| `record_signatures` | View cryptographic signature verification records | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li></ul> |
| `registry.entitlements` | View registry access entitlements and permissions | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li></ul> |
| `repo` | Create and manage container repositories (including [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/) resources) | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (create, delete, list, update)</li></ul> |
| `role_bindings` | [Assign roles to identities](/chainguard/administration/iam-organizations/roles-role-bindings/roles-role-bindings/#managing-role-bindings) (users and service accounts) | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull_token_creator` (create)</li><li>`libraries.java.pull_token_creator` (create)</li><li>`libraries.python.pull_token_creator` (create)</li><li>`libraries.javascript.pull_token_creator` (create)</li></ul> |
| `roles` | Create, modify, and manage [custom Chainguard IAM roles](/chainguard/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li></ul> |
| `sboms` | Access Software Bill of Materials for packages and images | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li></ul> |
| `subscriptions` | Manage [CloudEvent](/chainguard/administration/cloudevents/events-reference/) subscriptions for notifications and automation | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (create, delete, list, update)</li><li>`viewer` (list)</li></ul> |
| `tag` | Manage Chainguard container image tags | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li></ul> |
| `version` | View version information across all resources and assets | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li></ul> |
| `vuln` | Create vulnerability reports and assessments | <ul><li>`owner` (create)</li></ul> |
| `vuln_report` | Manage detailed vulnerability assessments for specific resources | <ul><li>`owner` (create, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li></ul> |
| `vuln_reports` | View high-level vulnerability report summaries | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li></ul> |

</div>

## Role Capabilities Comparison

The following table compares the general abilities of the twelve built-in roles described in the [previous summary](#built-in-roles-summary):

<div style="overflow-x: auto;">

| Role | Pull Images | List Tags/Repos | View SBOMs/Diffs | Create IAM Resources | Create Pull Tokens | Libraries Access |
|------|-------------|-----------------|------------------|---------------------|--------------------|-----------------|
| `owner` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `editor` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| `viewer` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| `registry.pull` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| `registry.pull_token_creator` | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| `apk.pull` | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `libraries.java.pull` | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| `libraries.java.pull_token_creator` | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ |
| `libraries.python.pull` | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| `libraries.python.pull_token_creator` | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ |
| `libraries.javascript.pull` | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| `libraries.javascript.pull_token_creator` | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ |

</div>

**Notes:**
- **Pull Images/List Tags/Repos/View SBOMs**: These capabilities refer to container registry operations relating to the `manifest`, `repo`, `tag`, and `sboms` resources
- **Library-specific roles**: `libraries.*.pull` and `libraries.*.pull_token_creator` roles are focused on their respective library ecosystems and don't have container registry access
- **APK Pull**: The `apk.pull` role is specialized for APK package management, not container operations


## Learn More

- [Overview of Roles and Role-bindings in Chainguard](/chainguard/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) - Conceptual overview and basic management
- [Overview of Chainguard IAM Model](/chainguard/administration/iam-organizations/overview-of-enforce-iam-model/) - Complete IAM architecture
