---
title : "Disabling Default Social Logins"
linktitle: "Disable Social Logins"
lead: ""
description: "How to stop users from authenticating to Chainguard with social logins by blocking the Chainguard app in your identity provider, using Google Workspace as an example"
type: "article"
date: 2026-07-02T08:48:45+00:00
lastmod: 2026-07-02T08:48:45+00:00
draft: true
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 007
---

By default, users can authenticate to the Chainguard platform using one of the built-in social login providers — GitHub, GitLab, or Google — as described in our guide on [authenticating with custom identity providers](/chainguard/administration/custom-idps/custom-idps/). After you [configure a custom identity provider](/chainguard/administration/custom-idps/custom-idps/#setup-and-administration) for Single Sign-on (SSO), you may want to require that everyone in your organization authenticate through that provider instead.

A common problem for SSO customers is that users click **Login with Google** (or another social provider) out of habit. Because a personal or non-federated Google account isn't tied to your organization, this creates an account *outside* your organization, which an organization owner then has to clean up and re-provision after the fact. Preventing social logins ensures account lifecycle, group membership, and security policies (such as multi-factor authentication) are enforced centrally through your identity provider.

> **Note**: A native, organization-level setting to hide or disable the default social login providers on the Chainguard login screen is on the Chainguard roadmap. In the meantime, if your identity provider is Google Workspace, you can achieve the same result today by blocking the Chainguard application in the Google Workspace Admin console, as described below. If you'd like to help shape the native feature, reach out to your customer success manager about the early access program.

## How this works

Google Workspace administrators can control which third-party applications are allowed to access Google Workspace data and sign in with a Google account. By setting the Chainguard application's access to **Blocked**, the **Login with Google** button on the Chainguard login screen will fail for users in your Google Workspace organization. Those users must then authenticate through your custom identity provider (or another allowed method) instead, which stops the stray, out-of-org accounts from being created.

This is configured entirely on the Google Workspace side — no changes to your Chainguard configuration are required.

## Before you begin

Before blocking social logins, make sure you have a working custom identity provider and a recovery path in place. Some organizations intentionally keep a social login (or an email and password account) as a [backup, break-glass account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) in case they are ever locked out of their identity provider. If you block Google sign-in without another recovery mechanism, an identity provider outage or misconfiguration could lock every user out of your organization.

We recommend confirming both of the following before proceeding:

* Your custom identity provider is configured and working. You can verify this by listing your identity providers and authenticating with one:

    ```sh
    chainctl iam identity-providers list
    ```

    ```sh
    chainctl auth login --identity-provider <IDP_ID>
    ```

* You have a [backup account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) that does not rely on Google sign-in — for example, an [assumable identity](/chainguard/administration/iam-organizations/assumable-ids/) — so you retain a recovery path.

You will also need administrator access to your organization's [Google Workspace Admin console](https://admin.google.com).

## Blocking the Chainguard app in Google Workspace

The following steps block the Chainguard application for your entire Google Workspace organization. For full details and the latest instructions, refer to Google's documentation on [controlling which third-party and internal apps access Google Workspace data](https://knowledge.workspace.google.com/admin/apps/control-which-apps-access-google-workspace-data).

1. Sign in to the [Google Workspace Admin console](https://admin.google.com) with an administrator account.
2. Navigate to **Security** > **Access and data control** > **API controls**.
3. Find the **App access control** section. The list of accessed apps may be hidden behind a ribbon-style scroll pane — scroll through the tiles until you reach the one labelled **_N_ Accessed Apps**, then click **View list**. This displays the apps that have accessed your organization's Google Workspace data.
4. Click **Add filter**, type `Chainguard`, and apply the filter to narrow the list to apps with "Chainguard" in the name.
5. Hover over the **Chainguard** app row. A **Change access** button appears on the right; click it.
6. Select which users the policy applies to — either **all** organizational units or **specific** organizational units — and then select the policy to **Block** access.
7. Save your changes to activate the policy.

<!--
  TODO (screenshots): Add cropped screenshots of the Google Workspace Admin
  console for steps 3-6 (the "N Accessed Apps" tile / View list, the Chainguard
  filter, and the Change access > Block dialog). Reference images were shared in
  the internal thread but contain personal account data and must be re-captured /
  cropped before publishing. Save them in this directory as e.g.
  google-app-access-1.png and reference with:
  <center><img src="google-app-access-1.png" alt="..." style="width:600px;"></center>
-->

Once the policy is activated, attempts to sign in to the Chainguard Console using a Google account linked to your organization will show a Google **Access blocked: Authorisation error** pop-up with the message `Error 400: admin_policy_enforced`. Affected users must then authenticate through your custom identity provider instead.

> **Tip**: Because you can scope the block to specific organizational units, you can retain break-glass access via Google social login for a chosen organizational unit — for example, a small unit containing only your recovery accounts — while blocking it for everyone else.

## After blocking social logins

Direct your users to authenticate with your custom identity provider. If your organization is [verified](/chainguard/administration/iam-organizations/verified-orgs/), users can log in with your organization name:

```sh
chainctl auth login --org-name example.com
```

Otherwise, users authenticate by passing the identity provider's ID:

```sh
chainctl auth login --identity-provider <IDP_ID>
```

To avoid specifying this on every login, users can set a default identity provider or organization name in their `chainctl` configuration, as described in the [custom identity providers guide](/chainguard/administration/custom-idps/custom-idps/#setting-a-default-identity-provider). In the Chainguard Console, users on a verified organization can enter their organization name or email address to be routed to your identity provider.

If you need to restore Google sign-in — for example, during a recovery scenario — follow the same steps to locate the Chainguard app, but instead of blocking it, change the access policy for the relevant organizational units to grant access. Select at least **Limited** access so that the login scopes are permitted.

The exact console layout and terminology are managed by Google and may change over time. If you require additional assistance configuring app access control or organizational units, refer to [Google Workspace support](https://support.google.com/a).
