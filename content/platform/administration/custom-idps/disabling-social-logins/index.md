---
title: "Disabling Default Social Logins"
linktitle: "Disable Social Logins"
lead: ""
description: "How to stop users from authenticating to Chainguard with social logins by blocking the Chainguard app in your identity provider, using Google Workspace as an example"
type: "article"
date: 2026-07-02T08:48:45+00:00
lastmod: 2026-07-02T08:48:45+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 7
---

By default, users can authenticate to the Chainguard platform with a built-in social login provider: GitHub, GitLab, or Google. After you [configure a custom identity provider](/chainguard/administration/custom-idps/custom-idps/#setup-and-administration) for single sign-on (SSO), you may want to require that everyone in your organization authenticate through that provider instead.

A common problem for SSO customers is that users click **Login with Google** (or another social provider) out of habit. Because a personal or non-federated Google account isn't tied to your organization, this creates an account *outside* it that an owner then has to clean up and re-provision. Preventing social logins keeps account lifecycle, group membership, and security policies (such as multi-factor authentication) enforced centrally through your identity provider.

Chainguard doesn't currently offer a native setting to disable social logins. However, if your identity provider is Google Workspace, you can achieve a similar result by blocking the Chainguard application in the Google Workspace Admin console. This guide outlines how to block the application and how to redirect users afterward.

> **Note**: If a native setting would be valuable to your organization, let your customer success manager know.


## Prerequisites

Before blocking social logins, make sure you have a working custom identity provider and a recovery path in place. Some organizations intentionally keep a social login (or an email and password account) as a [backup, break-glass account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) in case they are ever locked out of their identity provider. If you block Google login without another recovery mechanism, an identity provider outage or misconfiguration could lock every user out of your organization.

We recommend confirming both of the following before proceeding:

* Your custom identity provider is configured and working. You can verify this by listing your identity providers and authenticating with one:

    ```sh
    chainctl iam identity-providers list
    ```

    ```sh
    chainctl auth login --identity-provider <IDP_ID>
    ```

* You have a [backup account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) that does not rely on Google login (for example, an [assumable identity](/chainguard/administration/iam-organizations/assumable-ids/)), so you retain a recovery path.

You also need administrator access to your organization's [Google Workspace Admin console](https://admin.google.com).


## How this works

Google Workspace administrators control which third-party applications can access Google Workspace data and log in with a Google account.

When you set the Chainguard application's access to **Blocked**, the **Login with Google** button on the Chainguard login screen fails for users in your Google Workspace organization. Those users must then authenticate through your custom identity provider (or another allowed method) instead, which prevents stray accounts from being created outside your organization.

You do all of this configuration on the Google Workspace side — Chainguard requires no configuration changes.


## Blocking the Chainguard app in Google Workspace

The following steps block the Chainguard application for your entire Google Workspace organization.

Note that navigation paths and setting names in these steps may change over time. For full details and the latest instructions, refer to Google's documentation on [controlling which third-party and internal apps access Google Workspace data](https://knowledge.workspace.google.com/admin/apps/control-which-apps-access-google-workspace-data).

1. Log in to the [Google Workspace Admin console](https://admin.google.com) with an administrator account.
2. Navigate to **Security** > **Access and data control** > **API controls**.
3. Find the **App access control** section. The list of accessed apps may be hidden behind a ribbon-style scroll pane. Scroll through the tiles until you reach the one labeled **_N_ Accessed Apps**, then click **View list**. This displays the apps that have accessed your organization's Google Workspace data.
4. Click **Add filter**, type `Chainguard`, and apply the filter to narrow the list to apps with "Chainguard" in the name.
5. Hover over the **Chainguard** app row. A **Change access** button appears on the right; click it.
6. Select which users the policy applies to — either **all** organizational units or **specific** ones, and then select the policy to **Block** access.
7. Save your changes to activate the policy.

After you activate the policy, attempts to log in to the Chainguard Console using a Google account linked to your organization show a Google **Access blocked: Authorization error** pop-up with the message `Error 400: admin_policy_enforced`. Affected users must then authenticate through your custom identity provider instead.

> **Tip**: Because you can scope the block to specific organizational units, you can retain break-glass access via Google social login for a chosen organizational unit (for example, a small unit containing only your recovery accounts) while blocking it for everyone else.


## After blocking social logins

Direct your users to authenticate with your custom identity provider. If your organization is [verified](/chainguard/administration/iam-organizations/verified-orgs/), users can log in with your organization name:

```sh
chainctl auth login --org-name example.com
```

Otherwise, users authenticate by passing the identity provider's ID:

```sh
chainctl auth login --identity-provider <IDP_ID>
```

To avoid specifying this on every login, users can set a default identity provider or organization name in their `chainctl` configuration, as described in the [custom identity providers guide](/chainguard/administration/custom-idps/custom-idps/#setting-a-default-identity-provider). In the Chainguard Console, users in a verified organization can enter their organization name or email address to be routed to your identity provider.

If you need to restore Google login (for example, during a recovery scenario), follow the same steps to locate the Chainguard app, but instead of blocking it, change the access policy for the relevant organizational units to grant access. Select at least **Limited** access so that Google permits the login scopes.

Google manages the exact console layout and terminology, which may change over time. If you require additional assistance configuring app access control or organizational units, refer to [Google Workspace support](https://support.google.com/a).

