---
aliases:
- /chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/
title: "Built-in roles and capabilities reference"
linktitle: "Built-in roles and capabilities"
lead: "Reference for Chainguard's built-in roles and their specific capabilities"
description: "A resource documenting the capabilities and permissions of Chainguard's built-in IAM roles."
type: "article"
date: 2025-08-14T00:00:00Z
lastmod: 2026-11-12T13:41:48+00:00
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
    * `viewer`: Read-only access across all resources, **can** pull images, can run Guardener sessions, and can call tools on Chainguard MCP servers
    * `limited_owner`: Owner of a Starter organization, with `viewer` access plus pull tokens, library access, adding catalog images and Helm charts to the organization, invites limited to the organization's email domain, removing members, billing, and turning on Chainguard Checks and Chainguard Workspaces
    * `console_viewer`: Read-only access across all resources and **cannot** pull images or APK packages, run Guardener sessions, call tools on Chainguard MCP servers, or view legal terms
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

The following table maps Chainguard capabilities to the built-in roles that hold them. Each row covers one resource, such as `repo` or `identity`. The first column lists the full name of every capability on that resource, and the last column lists the actions each built-in role holds on it.

A capability's name is its resource and its action, joined by a dot. For example, `registry.entitlements.images.add` is the `add` action on the `registry.entitlements.images` resource. Use these full names when you [create a custom role](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/#managing-custom-roles) that grants only the capabilities a task needs, as in [Create a role for managing image entitlements](#create-a-role-for-managing-image-entitlements).

<div style="overflow-x: auto;">

<!-- BEGIN generated by scripts/capabilities-table/generate.py -->

| Capabilities | Purpose | Roles with access to this resource |
|------------|---------|---------------------------|
| `account_associations.create`<br>`account_associations.delete`<br>`account_associations.list`<br>`account_associations.update` | Link cloud provider accounts to organization | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `actions.list` | View the [Chainguard Actions](/chainguard/actions/overview/) catalog | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`actions.viewer` (list)</li></ul> |
| `advisories.list` | View [security advisories](/chainguard/containers/security-and-compliance/security-advisories/) for the packages in Chainguard images | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `apk.create`<br>`apk.delete`<br>`apk.list` | Manage APK packages in the registry | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`apk.pull` (list)</li><li>`apk.push` (create, delete, list)</li><li>`sandbox.user` (list)</li></ul> |
| `apk.blobs.get` | Download APK package binary content | <ul><li>`owner` (get)</li><li>`editor` (get)</li><li>`viewer` (get)</li><li>`limited_owner` (get)</li><li>`registry.pull_token_creator` (get)</li><li>`apk.pull` (get)</li><li>`apk.push` (get)</li></ul> |
| `auth_policies.list`<br>`auth_policies.update` | View and change the organization's [authentication policy](/platform/chainctl/chainctl-docs/chainctl_iam_auth-policy/), which sets how long a sign-in to the organization lasts | <ul><li>`owner` (list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `billing.manage` | Manage the organization's billing and payment method | <ul><li>`owner` (manage)</li><li>`limited_owner` (manage)</li></ul> |
| `build_report.list` | Access detailed build and scan reports for images and packages | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `entitlements.get` | View the organization's plan and its product limits | <ul><li>`owner` (get)</li><li>`editor` (get)</li><li>`viewer` (get)</li><li>`limited_owner` (get)</li><li>`console_viewer` (get)</li></ul> |
| `group_invites.create`<br>`group_invites.delete`<br>`group_invites.list` | Send and manage invitations to join Chainguard organization | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (create, delete, list)</li><li>`console_viewer` (list)</li></ul> |
| `groups.create`<br>`groups.delete`<br>`groups.list`<br>`groups.rename`<br>`groups.update` | Manage organization and hierarchical structures | <ul><li>`owner` (create, delete, list, rename, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list, rename)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (create, list)</li><li>`registry.editor` (list)</li><li>`apk.pull` (list)</li><li>`apk.push` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li><li>`sandbox.user` (list)</li></ul> |
| `guardener.actions.migrate` | Have Guardener migrate a repository's GitHub Actions to Chainguard Actions by opening a pull request | <ul><li>`owner` (migrate)</li><li>`editor` (migrate)</li><li>`viewer` (migrate)</li><li>`limited_owner` (migrate)</li><li>`guardener.user` (migrate)</li><li>`guardener.admin` (migrate)</li></ul> |
| `guardener.association.list`<br>`guardener.association.manage` | View and manage the GitHub organizations connected through [the Chainguard App](/chainguard/guardener/github/app-connections/) | <ul><li>`owner` (list, manage)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list, manage)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list, manage)</li></ul> |
| `guardener.dfc.convert` | Convert Dockerfiles to use Chainguard images with [Guardener](/chainguard/guardener/dockerfile-migration/) | <ul><li>`owner` (convert)</li><li>`editor` (convert)</li><li>`viewer` (convert)</li><li>`limited_owner` (convert)</li><li>`guardener.user` (convert)</li><li>`guardener.admin` (convert)</li></ul> |
| `guardener.entitlement.list` | View the organization's Guardener settings, such as which repositories Guardener can access | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `guardener.images.migrate` | Request and view [container image migrations](/chainguard/guardener/github/image-migration/) for a repository | <ul><li>`owner` (migrate)</li><li>`editor` (migrate)</li><li>`viewer` (migrate)</li><li>`limited_owner` (migrate)</li><li>`guardener.user` (migrate)</li><li>`guardener.admin` (migrate)</li></ul> |
| `guardener.scan.get`<br>`guardener.scan.list` | View the dependency scans Guardener runs on connected repositories | <ul><li>`owner` (get, list)</li><li>`editor` (get, list)</li><li>`viewer` (get, list)</li><li>`limited_owner` (get, list)</li><li>`console_viewer` (get, list)</li><li>`guardener.user` (get, list)</li><li>`guardener.admin` (get, list)</li></ul> |
| `identity.create`<br>`identity.delete`<br>`identity.list`<br>`identity.update` | Create and manage user identities, service accounts, and pull tokens | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (create, list)</li><li>`console_viewer` (list)</li><li>`registry.pull_token_creator` (create)</li><li>`libraries.java.pull_token_creator` (create)</li><li>`libraries.python.pull_token_creator` (create)</li><li>`libraries.javascript.pull_token_creator` (create)</li></ul> |
| `identity_providers.create`<br>`identity_providers.delete`<br>`identity_providers.list`<br>`identity_providers.update` | Configure [custom identity providers](/platform/administration/custom-idps/custom-idps/) (OIDC, SAML) for authentication | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `identity_providers.scim.manage` | Turn on [SCIM provisioning](/platform/administration/custom-idps/scim-provisioning/scim-overview/) for a custom identity provider and manage its tokens | <ul><li>`owner` (manage)</li></ul> |
| `identity_providers.scim.users.list` | View the users a custom identity provider provisioned through SCIM | <ul><li>`owner` (list)</li></ul> |
| `libraries.artifacts.list` | View Chainguard Library artifact metadata and information | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.aws_marketplace.subscriptions.create`<br>`libraries.aws_marketplace.subscriptions.list`<br>`libraries.aws_marketplace.subscriptions.update` | Manage Chainguard Libraries subscriptions bought through AWS Marketplace | <ul><li>`owner` (create, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.cache.invalidate`<br>`libraries.cache.list` | View and clear the organization's Chainguard Libraries resolution cache | <ul><li>`owner` (invalidate, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.entitlements.create`<br>`libraries.entitlements.delete`<br>`libraries.entitlements.list` | Manage access permissions for Chainguard Libraries | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`libraries.java.pull` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.java.push` (list)</li><li>`libraries.python.pull` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.python.push` (list)</li><li>`libraries.javascript.pull` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li><li>`libraries.javascript.push` (list)</li></ul> |
| `libraries.java.create`<br>`libraries.java.list` | Access [Chainguard Libraries for Java](/chainguard/libraries/java/overview/) | <ul><li>`owner` (create, list)</li><li>`limited_owner` (list)</li><li>`libraries.java.pull` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.java.push` (create, list)</li></ul> |
| `libraries.javascript.create`<br>`libraries.javascript.list` | Access Chainguard Libraries for JavaScript | <ul><li>`owner` (create, list)</li><li>`limited_owner` (list)</li><li>`libraries.javascript.pull` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li><li>`libraries.javascript.push` (create, list)</li></ul> |
| `libraries.policy.create`<br>`libraries.policy.delete`<br>`libraries.policy.list`<br>`libraries.policy.update` | Create and manage the cooldown and malware policies applied to upstream library pulls | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.policy.binding.create`<br>`libraries.policy.binding.delete`<br>`libraries.policy.binding.list`<br>`libraries.policy.binding.update` | Apply Chainguard Libraries policies to the organization | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.policy.block_event.list` | View the library pulls a policy blocked | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.python.create`<br>`libraries.python.list` | Access [Chainguard Libraries for Python](/chainguard/libraries/python/overview/) | <ul><li>`owner` (create, list)</li><li>`limited_owner` (list)</li><li>`libraries.python.pull` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.python.push` (create, list)</li></ul> |
| `libraries.request_groups.create`<br>`libraries.request_groups.delete`<br>`libraries.request_groups.list`<br>`libraries.request_groups.submit`<br>`libraries.request_groups.update` | Request library versions for Chainguard to build, and track those requests | <ul><li>`owner` (create, delete, list, submit, update)</li><li>`editor` (create, delete, list, update)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `libraries.request_groups.items.update` | Edit the individual libraries in a draft build request | <ul><li>`owner` (update)</li><li>`editor` (update)</li></ul> |
| `libraries.storage_usage.get` | View how much storage the organization's uploaded libraries use in each ecosystem | <ul><li>`owner` (get)</li></ul> |
| `manifest.create`<br>`manifest.delete`<br>`manifest.list`<br>`manifest.update` | Access and manage container image manifests | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (create, delete, list, update)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `manifest.metadata.list` | View container image manifest metadata and attestations | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `mcp.tool.call` | Call tools on [Chainguard MCP servers](/platform/mcp-servers/overview/) | <ul><li>`owner` (call)</li><li>`editor` (call)</li><li>`viewer` (call)</li><li>`limited_owner` (call)</li><li>`mcp.tool_user` (call)</li></ul> |
| `packages.entitlements.list` | View which tier of Chainguard OS Packages the organization is entitled to, base or FIPS | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `policies.binding.create`<br>`policies.binding.delete`<br>`policies.binding.list`<br>`policies.binding.update` | Turn image pull policies on for the organization | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `policies.decision.list` | View the allow and block decisions image pull policies made | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `policies.override.create`<br>`policies.override.delete`<br>`policies.override.list` | Exempt a specific image from policy enforcement | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `policies.policy.create`<br>`policies.policy.delete`<br>`policies.policy.list`<br>`policies.policy.update` | View and manage image pull policies, such as blocking end-of-life images | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `record_signatures.list` | View cryptographic signature verification records | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `referrers.list` | View the signatures, attestations, and other artifacts attached to an image | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `registry.charts.add` | Add a catalog [Helm chart](/get-started/self-serve/helm-charts/) and the images it needs to the organization | <ul><li>`owner` (add)</li><li>`limited_owner` (add)</li></ul> |
| `registry.deployments.list` | View the Helm charts associated with a container repository | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `registry.entitlements.list` | View registry access entitlements and permissions | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `registry.entitlements.images.add`<br>`registry.entitlements.images.remove`<br>`registry.entitlements.images.swap` | Add, remove, and swap the images in the organization's registry entitlement | <ul><li>`owner` (add, remove, swap)</li><li>`limited_owner` (add)</li></ul> |
| `registry.overlays.edit`<br>`registry.overlays.list` | View and edit [Custom Assembly overlays](/chainguard/containers/custom-assembly/overlays/) | <ul><li>`owner` (edit, list)</li><li>`editor` (edit, list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.editor` (edit, list)</li></ul> |
| `registry.settings.list` | View the organization's registry settings, such as whether unique tags and the End-of-Life Grace Period are on by default | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `repo.check_policies`<br>`repo.create`<br>`repo.delete`<br>`repo.list`<br>`repo.update` | Create and manage container repositories (including [Custom Assembly](/chainguard/containers/custom-assembly/) resources) | <ul><li>`owner` (check_policies, create, delete, list, update)</li><li>`editor` (create, delete, list, update)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (create, delete, list, update)</li><li>`registry.editor` (create, delete, list, update)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `repo.blobs.get` | Download container image binary content | <ul><li>`owner` (get)</li><li>`editor` (get)</li><li>`viewer` (get)</li><li>`limited_owner` (get)</li><li>`registry.pull` (get)</li><li>`registry.pull_token_creator` (get)</li><li>`registry.push` (get)</li><li>`registry.editor` (get)</li><li>`guardener.user` (get)</li><li>`guardener.admin` (get)</li></ul> |
| `role_bindings.create`<br>`role_bindings.delete`<br>`role_bindings.list`<br>`role_bindings.update` | [Assign roles to identities](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/#managing-role-bindings) (users and service accounts) | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (create, delete, list)</li><li>`console_viewer` (list)</li><li>`registry.pull_token_creator` (create)</li><li>`libraries.java.pull_token_creator` (create)</li><li>`libraries.python.pull_token_creator` (create)</li><li>`libraries.javascript.pull_token_creator` (create)</li></ul> |
| `roles.create`<br>`roles.delete`<br>`roles.list`<br>`roles.update` | Create, modify, and manage [custom Chainguard IAM roles](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`libraries.java.pull_token_creator` (list)</li><li>`libraries.python.pull_token_creator` (list)</li><li>`libraries.javascript.pull_token_creator` (list)</li></ul> |
| `sandbox.identity.admin`<br>`sandbox.identity.create`<br>`sandbox.identity.use` | Create the [Chainguard identity a Workspaces session acts through](/chainguard/workspaces/credentials/#your-chainguard-identity-in-a-session), and define and use shared session identities | <ul><li>`owner` (admin, create, use)</li><li>`sandbox.user` (create)</li><li>`sandbox.identity.user` (use)</li></ul> |
| `sandbox.run.cancel`<br>`sandbox.run.create`<br>`sandbox.run.list` | Start, view, and cancel [Chainguard Checks](/chainguard/checks/overview/) runs | <ul><li>`owner` (cancel, create, list)</li><li>`limited_owner` (cancel, create, list)</li><li>`sandbox.user` (cancel, create, list)</li></ul> |
| `sandbox.session.create`<br>`sandbox.session.list` | Open [Chainguard Workspaces](/chainguard/workspaces/overview/) sessions, and list every user's sessions in the organization | <ul><li>`owner` (create, list)</li><li>`limited_owner` (create)</li><li>`sandbox.user` (create)</li></ul> |
| `sboms.list` | Access Software Bill of Materials for packages and images | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `skills.list`<br>`skills.publish` | View the [Chainguard Agent Skills](/chainguard/agent-skills/overview/) catalog and publish skills | <ul><li>`owner` (list, publish)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `skills.entitlements.create`<br>`skills.entitlements.delete`<br>`skills.entitlements.list` | Manage which Chainguard Agent Skills the organization can access | <ul><li>`owner` (create, delete, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `skills.harden.cancel`<br>`skills.harden.read`<br>`skills.harden.write` | Submit, track, and cancel [skill hardening](/chainguard/agent-skills/skill-hardening/) jobs | <ul><li>`owner` (cancel, read, write)</li></ul> |
| `subscriptions.create`<br>`subscriptions.delete`<br>`subscriptions.list`<br>`subscriptions.update` | Manage [CloudEvent](/platform/administration/cloudevents/events-reference/) subscriptions for notifications and automation | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (create, delete, list, update)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `tag.create`<br>`tag.delete`<br>`tag.list`<br>`tag.update` | Manage Chainguard container image tags | <ul><li>`owner` (create, delete, list, update)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (create, delete, list, update)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `telemetry.containers.list` | View the container images that connected repositories use, as Guardener observes them | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |
| `terms.accept`<br>`terms.list` | View and accept the legal terms a Chainguard product requires before you can use it | <ul><li>`owner` (accept, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (accept, list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (accept, list)</li></ul> |
| `version.list` | View version information across all resources and assets | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `vuln.create` | Create vulnerability reports and assessments | <ul><li>`owner` (create)</li></ul> |
| `vuln_report.create`<br>`vuln_report.list` | Manage detailed vulnerability assessments for specific resources | <ul><li>`owner` (create, list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li></ul> |
| `vuln_reports.list` | View high-level vulnerability report summaries | <ul><li>`owner` (list)</li><li>`editor` (list)</li><li>`viewer` (list)</li><li>`limited_owner` (list)</li><li>`console_viewer` (list)</li><li>`registry.pull` (list)</li><li>`registry.pull_token_creator` (list)</li><li>`registry.push` (list)</li><li>`registry.editor` (list)</li><li>`guardener.user` (list)</li><li>`guardener.admin` (list)</li></ul> |

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
| `limited_owner` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
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
* **Console Viewer**: Has the same broad `list` access as `viewer`, but can't pull blobs (`apk.blobs`, `repo.blobs`), view legal terms (`terms`), run Guardener conversions or migrations (`guardener.dfc`, `guardener.actions`, `guardener.images`), call tools on Chainguard MCP servers (`mcp.tool`), or list the GitHub organizations connected through the Chainguard App (`guardener.association`). This makes it a safe role for inviting team members who need Console visibility without the ability to pull images or APKs.

### Pull token creator roles

The following roles are used for managing pull tokens for certain resources:

* `registry.pull_token_creator`
* `libraries.java.pull_token_creator`
* `libraries.python.pull_token_creator`
* `libraries.javascript.pull_token_creator`

For example, the `libraries.*.pull_token_creator` roles are focused on their respective library ecosystems and don't have container registry access.

These roles are able to create pull tokens because of the `identity.create` capability. However, none of these roles have the `identity.list` capability, meaning that they aren't able to view the pull tokens they've created.

The reason for this is that Chainguard doesn't distinguish pull token identities from other [assumable identities](/platform/administration/assumable-ids/assumable-ids/) at the IAM level. If these roles also had the `identity.list` capability, they would be able to view **all** the identities in that scope. By not including `identity.list` among their capabilities, the pull token creator roles have a more limited scope, as intended.

## Create a role for managing image entitlements {#create-a-role-for-managing-image-entitlements}

An organization's registry entitlement lists the Chainguard Containers it can use. Of the built-in roles, only `owner` can add, remove, and swap the images in it, and `limited_owner` can add them. To let someone manage the entitlement without the rest of the `owner` role, create a custom role with only the capabilities the task needs.

Which capabilities you need depends on your organization's plan:

* **Per-image plans:** The entitlement holds each image individually, and the `registry.entitlements.images` capabilities control which images it holds.
* **Catalog Pricing:** The entitlement already covers every image in your catalog, so you don't change it. Adding an image to your organization creates a repository instead, which needs the `repo` capabilities described in [Self-serve catalog experience](/chainguard/containers/reference/pricing/#self-serve-catalog-experience).

On a per-image plan, the following command creates a role that can manage the entitlement with the [`chainctl images entitlements`](/platform/chainctl/chainctl-docs/chainctl_images_entitlements/) commands. Replace `$ORGANIZATION` with the name of your organization. Creating a custom role requires the `owner` role:

```shell
chainctl iam roles create entitlement-manager \
  --parent=$ORGANIZATION \
  --capabilities=groups.list,registry.entitlements.list,registry.entitlements.images.add,registry.entitlements.images.remove,registry.entitlements.images.swap
```

The role includes these capabilities:

* `groups.list`: Lets the commands find your organization when you pass `--parent`.
* `registry.entitlements.list`: Lets `chainctl images entitlements list` show the entitlement and the images it holds.
* `registry.entitlements.images.add`, `registry.entitlements.images.remove`, and `registry.entitlements.images.swap`: Let `add-image`, `remove-image`, and `swap-image` change the images. Each image that `remove-image` or `swap-image` takes out counts against your organization's 30-day swap quota.

To let the role add images but not remove or swap them, leave out `registry.entitlements.images.remove` and `registry.entitlements.images.swap`.

To give the role to a user, create a role-binding, as described in [Managing role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/#managing-role-bindings).

## Learn more

* [Overview of roles and role-bindings in Chainguard](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) - Conceptual overview and basic management
* [Overview of Chainguard IAM model](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/) - Complete IAM architecture
