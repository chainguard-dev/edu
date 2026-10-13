---
aliases:
- /chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/
title: "Built-in roles and capabilities reference"
linktitle: "Built-in roles and capabilities"
lead: "Reference for Chainguard's built-in roles and their specific capabilities"
description: "A resource documenting the capabilities and permissions of Chainguard's built-in IAM roles."
type: "article"
date: 2025-08-14T00:00:00Z
lastmod: 2026-10-13T13:55:57+00:00
draft: false
tags: ["IAM", "Reference", "Product"]
images: []
weight: 20
---

Chainguard provides customers with a set of built-in roles as part of its Identity and Access Management (IAM) system. These roles have different permissions and capabilities that allow them to serve specialized purposes, from general administrative access to access for specific resources like registries, APK packages, and programming language libraries.

This reference provides an overview of all Chainguard IAM capabilities and shows which built-in roles include each capability. Each capability represents a specific permission or action that can be performed within the Chainguard platform.

For more information on roles and role-bindings within Chainguard's IAM model, please refer to our [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

## Built-in roles summary

This guide outlines the built-in Chainguard IAM roles available to most customer organizations. You can find more info about specific roles in your organization with the following `chainctl` command:

```shell
chainctl iam roles list
```

Every role grants actions on at least one Chainguard resource. Most actions are `create`, `list`, `update`, or `delete`, and a few resources use others, such as `get`, `accept`, or `call`. For example, the `owner` role can create, delete, list, and update custom roles within Chainguard, while the `viewer` role can only list them.

This guide outlines the following built-in roles provided by Chainguard:

* **Administrative Roles:**
    * `owner`: Full administrative access with all capabilities
    * `editor`: `viewer` access plus creating, updating, and deleting container repositories, editing Custom Assembly overlays, drafting library build requests, and managing event subscriptions
    * `viewer`: Read-only access across all resources, **can** pull images, and can run Guardener sessions
    * `limited_owner`: Owner of a Starter organization, with `viewer` access plus pull tokens, invites limited to the organization's email domain, removing members, billing, and turning on Chainguard Checks and Chainguard Workspaces
    * `console_viewer`: Read-only access across all resources and **cannot** pull images or APK packages, run Guardener sessions, or view legal terms
* **Registry and Container Roles:**
    * `registry.pull`: Container image access
    * `registry.pull_token_creator`: Chainguard registry token management with additional repository capabilities
    * `registry.push`: `registry.pull` access plus pushing images, and creating, updating, and deleting repositories and tags
    * `registry.editor`: `registry.pull` access plus creating, updating, and deleting repositories, and editing Custom Assembly overlays
    * `apk.pull`: Access to the organization's APK packages, including the private APK repository
    * `apk.push`: `apk.pull` access plus uploading and deleting APK packages
* **Library Roles:**
    * `libraries.java.pull`: Java library access
    * `libraries.java.pull_token_creator`: Java token management
    * `libraries.java.push`: `libraries.java.pull` access plus Java library uploads
    * `libraries.python.pull`: Python library access
    * `libraries.python.pull_token_creator`: Python library token management
    * `libraries.python.push`: `libraries.python.pull` access plus Python library uploads
    * `libraries.javascript.pull`: JavaScript library access
    * `libraries.javascript.pull_token_creator`: JavaScript library token management
    * `libraries.javascript.push`: `libraries.javascript.pull` access plus JavaScript library uploads
* **Guardener Roles**:
    * `guardener.user`: Minimum role for running Guardener sessions, including Guardener conversion, terms lookup, and registry pull access
    * `guardener.admin`: Extends `guardener.user` with permission to accept the legal terms required before Guardener sessions can start
* **Checks and Workspaces Roles**:
    * `sandbox.user`: Start, view, and cancel Chainguard Checks runs, and open Chainguard Workspaces sessions
    * `sandbox.identity.user`: Use shared identities in Chainguard Workspaces sessions
* **MCP Roles**:
    * `mcp.tool_user`: Call tools on Chainguard MCP servers
* **Actions Roles**:
    * `actions.viewer`: View the Chainguard Actions catalog

The administrative roles are useful for user profiles that require broad, but clearly defined capabilities. The registry, container, and library roles have limited permissions, allowing them to manage only one specific Chainguard resource. These specialized, resource-specific roles grant minimal required access.

For example, the `apk.pull` role grants `list` access for APK packages and groups, and `get` access to APK package content. This means identities with this role can pull the organization's APK packages and retrieve information about the organization, but won't have general access to the organization's [Chainguard registry](/chainguard/containers/registry/overview/) resources.

## Chainguard role capabilities

The following table maps Chainguard resources to the built-in roles that have permissions for them. Each row represents a specific resource type (like `apk`, `repo`, `identity`, etc.), describes its purpose, and lists which actions each built-in role has on that resource.

<div style="overflow-x: auto;">

<!-- BEGIN generated by scripts/capabilities-table/generate.py -->

| Resource | Purpose | Roles with access to this resource |
|------------|---------|---------------------------|
| `account_associations` | Link cloud provider accounts to organization | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `actions` | View the [Chainguard Actions](/chainguard/actions/overview/) catalog | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`actions.viewer` (list)</li></ul> |
| `advisories` | View [security advisories](/chainguard/containers/security-and-compliance/security-advisories/) for the packages in Chainguard images | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `apk` | Manage APK packages in the registry | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`apk.pull` (list)</li><li>`apk.push` (create, delete, list)</li></ul> |
| `apk.blobs` | Download APK package binary content | <ul><li>`owner` (get)</li><li>`editor` (get)</li><li>`viewer` (get)</li><li>`limited_owner` (get)</li><li>`registry.pull_token_creator` (get)</li><li>`apk.pull` (get)</li><li>`apk.push` (get)</li></ul> |
| `billing` | Manage the organization's billing and payment method | <ul><li>`owner` (manage)</li><li>`limited_owner` (manage)</li></ul> |
| `build_report` | Access detailed build and scan reports for images and packages | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `group_invites` | Send and manage invitations to join Chainguard organization | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (create, delete, list)</li><li>`console_viewer` (list)</li></ul> |
| `groups` | Manage organization and hierarchical structures | <ul><li>`owner` (create, delete, list, rename, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list, rename)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (create, list)</li><li>`registry.editor` (list)</li><li>`apk.pull` (list)</li><li>`apk.push` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `guardener.actions` | Have Guardener migrate a repository's GitHub Actions to Chainguard Actions by opening a pull request | <ul><li>`owner` (migrate)</li><li>`editor` (migrate)</li><li>`viewer` (migrate)</li><li>`limited_owner` (migrate)</li><li>`guardener.user` (migrate)</li><li>`guardener.admin` (migrate)</li></ul> |
| `guardener.association` | View and manage the GitHub organizations connected through [the Chainguard App](/chainguard/guardener/github/app-connections/) | <ul><li>`owner` (list, manage)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list, manage)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list, manage)</li></ul> |
| `guardener.dfc` | Convert Dockerfiles to use Chainguard images with [Guardener](/chainguard/guardener/dockerfile-migration/) | <ul><li>`owner` (convert)</li><li>`editor` (convert)</li><li>`viewer` (convert)</li><li>`limited_owner` (convert)</li><li>`guardener.user` (convert)</li><li>`guardener.admin` (convert)</li></ul> |
| `guardener.entitlement` | View the organization's Guardener settings, such as which repositories Guardener can access | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `guardener.images` | Request and view [container image migrations](/chainguard/guardener/github/image-migration/) for a repository | <ul><li>`owner` (migrate)</li><li>`editor` (migrate)</li><li>`viewer` (migrate)</li><li>`limited_owner` (migrate)</li><li>`guardener.user` (migrate)</li><li>`guardener.admin` (migrate)</li></ul> |
| `guardener.scan` | View the dependency scans Guardener runs on connected repositories | <ul><li>`owner` (get, list)</li><li>`editor` (get, list)</li><li>`viewer` (get, list)</li><li>`limited_owner` (get, list)</li><li>`console_viewer` (get, list)</li><li>`guardener.user` (get, list)</li><li>`guardener.admin` (get, list)</li></ul> |
| `identity` | Create and manage user identities, service accounts, and pull tokens | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (create, list)</li><li>`console_viewer` (list)</li><li>`registry.pull_token_creator` (create)</li><li>`libraries.java.pull_token_creator` (create)</li><li>`libraries.python.pull_token_creator` (create)</li><li>`libraries.javascript.pull_token_creator` (create)</li></ul> |
| `identity_providers` | Configure [custom identity providers](/platform/administration/custom-idps/custom-idps/) (OIDC, SAML) for authentication | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `identity_providers.scim` | Turn on [SCIM provisioning](/platform/administration/custom-idps/scim-provisioning/scim-overview/) for a custom identity provider and manage its tokens | <ul><li>`owner` (manage)</li></ul> |
| `identity_providers.scim.users` | View the users a custom identity provider provisioned through SCIM | <ul><li>`owner` (list)</li></ul> |
| `libraries.artifacts` | View Chainguard Library artifact metadata and information | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.aws_marketplace.subscriptions` | Manage Chainguard Libraries subscriptions bought through AWS Marketplace | <ul><li>`owner` (create, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.cache` | View and clear the organization's Chainguard Libraries resolution cache | <ul><li>`owner` (invalidate, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.entitlements` | Manage access permissions for Chainguard Libraries | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`libraries.java.pull` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.java.push` (list)</li><li>`libraries.python.pull` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.python.push` (list)</li><li>`libraries.javascript.pull` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li><li>`libraries.javascript.push` (list)</li></ul> |
| `libraries.java` | Access [Chainguard Libraries for Java](/chainguard/libraries/java/overview/) | <ul><li>`owner` (create, list)</li><li>`libraries.java.pull` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.java.push` (create, list)</li></ul> |
| `libraries.javascript` | Access Chainguard Libraries for JavaScript | <ul><li>`owner` (create, list)</li><li>`libraries.javascript.pull` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li><li>`libraries.javascript.push` (create, list)</li></ul> |
| `libraries.policy` | Create and manage the cooldown and malware policies applied to upstream library pulls | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.policy.binding` | Apply Chainguard Libraries policies to the organization | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.policy.block_event` | View the library pulls a policy blocked | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.python` | Access [Chainguard Libraries for Python](/chainguard/libraries/python/overview/) | <ul><li>`owner` (create, list)</li><li>`libraries.python.pull` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.python.push` (create, list)</li></ul> |
| `libraries.remote_registries` | Configure the upstream registries the organization's virtual repositories pull from | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.request_groups` | Request library versions for Chainguard to build, and track those requests | <ul><li>`owner` (create, delete, list, submit, update)</li><li>`editor` (create, delete, list, update)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.request_groups.items` | Edit the individual libraries in a draft build request | <ul><li>`owner` (update)</li><li>`editor` (update)</li></ul> |
| `libraries.storage_usage` | View how much storage the organization's uploaded libraries use in each ecosystem | <ul><li>`owner` (get)</li></ul> |
| `manifest` | Access and manage container image manifests | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (create, delete, list, update)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `manifest.metadata` | View container image manifest metadata and attestations | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `mcp.tool` | Call tools on [Chainguard MCP servers](/platform/mcp-servers/overview/) | <ul><li>`owner` (call)</li><li>`mcp.tool_user` (call)</li></ul> |
| `packages.entitlements` | View which tier of Chainguard OS Packages the organization is entitled to, base or FIPS | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `policies.binding` | Turn image pull policies on for the organization | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `policies.decision` | View the allow and block decisions image pull policies made | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `policies.override` | Exempt a specific image from policy enforcement | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `policies.policy` | View and manage image pull policies, such as blocking end-of-life images | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `record_signatures` | View cryptographic signature verification records | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `referrers` | View the signatures, attestations, and other artifacts attached to an image | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `registry.deployments` | View the Helm charts associated with a container repository | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `registry.entitlements` | View registry access entitlements and permissions | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `registry.entitlements.images` | Add, remove, and swap the images in the organization's registry entitlement | <ul><li>`owner` (add, remove, swap)</li><li>`limited_owner` (add)</li></ul> |
| `registry.overlays` | View and edit [Custom Assembly overlays](/chainguard/containers/custom-assembly/overlays/) | <ul><li>`owner` (edit, list)</li><li>`editor` (edit, list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.editor` (edit, list)</li></ul> |
| `registry.settings` | View the organization's registry settings, such as whether unique tags and the End-of-Life Grace Period are on by default | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `repo` | Create and manage container repositories (including [Custom Assembly](/chainguard/containers/custom-assembly/) resources) | <ul><li>`owner` (check_policies, create, delete, list, update)</li><li>`editor` (create, delete, list, update)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (create, delete, list, update)</li><li>`registry.editor` (create, delete, list, update)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `repo.blobs` | Download container image binary content | <ul><li>`owner` (get)</li><li>`editor` (get)</li><li>`viewer` (get)</li><li>`limited_owner` (get)</li><li>`registry.pull` (get)</li><li>`registry.pull_token_creator` (get)</li><li>`registry.push` (get)</li><li>`registry.editor` (get)</li><li>`guardener.user` (get)</li><li>`guardener.admin` (get)</li></ul> |
| `role_bindings` | [Assign roles to identities](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/#managing-role-bindings) (users and service accounts) | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (create, delete, list)</li><li>`console_viewer` (list)</li><li>`registry.pull_token_creator` (create)</li><li>`libraries.java.pull_token_creator` (create)</li><li>`libraries.python.pull_token_creator` (create)</li><li>`libraries.javascript.pull_token_creator` (create)</li></ul> |
| `roles` | Create, modify, and manage [custom Chainguard IAM roles](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li></ul> |
| `sandbox.identity` | Create the [Chainguard identity a Workspaces session acts through](/chainguard/workspaces/credentials/#your-chainguard-identity-in-a-session), and define and use shared session identities | <ul><li>`owner` (admin, create, use)</li><li>`sandbox.user` (create)</li><li>`sandbox.identity.user` (use)</li></ul> |
| `sandbox.run` | Start, view, and cancel [Chainguard Checks](/chainguard/checks/overview/) runs | <ul><li>`owner` (cancel, create, list)</li><li>`limited_owner` (cancel, create)</li><li>`sandbox.user` (cancel, create, list)</li></ul> |
| `sandbox.session` | Open [Chainguard Workspaces](/chainguard/workspaces/overview/) sessions, and list every user's sessions in the organization | <ul><li>`owner` (create, list)</li><li>`limited_owner` (create)</li><li>`sandbox.user` (create)</li></ul> |
| `sboms` | Access Software Bill of Materials for packages and images | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `skills` | View the [Chainguard Agent Skills](/chainguard/agent-skills/overview/) catalog and publish skills | <ul><li>`owner` (list, publish)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `skills.entitlements` | Manage which Chainguard Agent Skills the organization can access | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `skills.harden` | Submit, track, and cancel [skill hardening](/chainguard/agent-skills/skill-hardening/) jobs | <ul><li>`owner` (cancel, read, write)</li></ul> |
| `subscriptions` | Manage [CloudEvent](/platform/administration/cloudevents/events-reference/) subscriptions for notifications and automation | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (create, delete, list, update)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `tag` | Manage Chainguard container image tags | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (create, delete, list, update)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `telemetry.containers` | View the container images that connected repositories use, as Guardener observes them | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `terms` | View and accept the legal terms a Chainguard product requires before you can use it | <ul><li>`owner` (accept, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (accept, list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (accept, list)</li></ul> |
| `version` | View version information across all resources and assets | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `vuln` | Create vulnerability reports and assessments | <ul><li>`owner` (create)</li></ul> |
| `vuln_report` | Manage detailed vulnerability assessments for specific resources | <ul><li>`owner` (create, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `vuln_reports` | View high-level vulnerability report summaries | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |

<!-- END generated by scripts/capabilities-table/generate.py -->

</div>

## Role capabilities comparison

The following table compares the general abilities of the built-in roles described in the [previous summary](#built-in-roles-summary):

<div style="overflow-x: auto;">

| Role | Pull Images | List Tags/Repos | View SBOMs/Diffs | Create IAM Resources | Create Pull Tokens | Libraries Access |
|------|-------------|-----------------|------------------|---------------------|--------------------|-----------------|
| `owner` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `editor` | ✅ | ✅ | ✅ | ✕ | ✕ | ✕ |
| `viewer` | ✅ | ✅ | ✅ | ✕ | ✕ | ✕ |
| `limited_owner` | ✅ | ✅ | ✅ | ✅ | ✅ | ✕ |
| `console_viewer` | ✕ | ✅ | ✅ | ✕ | ✕ | ✕ |
| `registry.pull` | ✅ | ✅ | ✅ | ✕ | ✕ | ✕ |
| `registry.pull_token_creator` | ✅ | ✅ | ✅ | ✅ | ✅ | ✕ |
| `registry.push` | ✅ | ✅ | ✅ | ✕ | ✕ | ✕ |
| `registry.editor` | ✅ | ✅ | ✅ | ✕ | ✕ | ✕ |
| `apk.pull` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `apk.push` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `libraries.java.pull` | ✕ | ✕ | ✕ | ✕ | ✕ | ✅ |
| `libraries.java.pull_token_creator` | ✕ | ✕ | ✕ | ✅ | ✅ | ✅ |
| `libraries.java.push` | ✕ | ✕ | ✕ | ✕ | ✕ | ✅ |
| `libraries.python.pull` | ✕ | ✕ | ✕ | ✕ | ✕ | ✅ |
| `libraries.python.pull_token_creator` | ✕ | ✕ | ✕ | ✅ | ✅ | ✅ |
| `libraries.python.push` | ✕ | ✕ | ✕ | ✕ | ✕ | ✅ |
| `libraries.javascript.pull` | ✕ | ✕ | ✕ | ✕ | ✕ | ✅ |
| `libraries.javascript.pull_token_creator` | ✕ | ✕ | ✕ | ✅ | ✅ | ✅ |
| `libraries.javascript.push` | ✕ | ✕ | ✕ | ✕ | ✕ | ✅ |
| `guardener.user` | ✅ | ✅ | ✅ | ✕ | ✕ | ✕ |
| `guardener.admin` | ✅ | ✅ | ✅ | ✕ | ✕ | ✕ |
| `sandbox.user` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `sandbox.identity.user` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `mcp.tool_user` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `actions.viewer` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |

</div>

**Notes**

* **Pull Images/List Tags/Repos/View SBOMs**: These capabilities refer to container registry operations relating to the `manifest`, `repo`, `tag`, and `sboms` resources
* **APK Pull**: The `apk.pull` role is specialized for APK package management, not container operations
* **Console Viewer**: Has the same broad `list` access as `viewer`, but can't pull blobs (`apk.blobs`, `repo.blobs`), view legal terms (`terms`), run Guardener conversions or migrations (`guardener.dfc`, `guardener.actions`, `guardener.images`), or list the GitHub organizations connected through the Chainguard App (`guardener.association`). This makes it a safe role for inviting team members who need Console visibility without the ability to pull images or APKs.

### Pull token creator roles

The following roles are used for managing pull tokens for certain resources:

* `registry.pull_token_creator`
* `libraries.java.pull_token_creator`
* `libraries.python.pull_token_creator`
* `libraries.javascript.pull_token_creator`

For example, the `libraries.*.pull_token_creator` roles are focused on their respective library ecosystems and don't have container registry access.

These roles are able to create pull tokens because of the `identity.create` capability. However, none of these roles have the `identity.list` capability, meaning that they aren't able to view the pull tokens they've created.

The reason for this is that Chainguard doesn't distinguish pull token identities from other [assumable identities](/platform/administration/assumable-ids/assumable-ids/) at the IAM level. If these roles also had the `identity.list` capability, they would be able to view **all** the identities in that scope. By not including `identity.list` among their capabilities, the pull token creator roles have a more limited scope, as intended.

## Learn more

* [Overview of roles and role-bindings in Chainguard](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) - Conceptual overview and basic management
* [Overview of Chainguard IAM model](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/) - Complete IAM architecture
