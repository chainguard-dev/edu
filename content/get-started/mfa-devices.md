---
title: "Change or reset your MFA device"
linktitle: "Change your MFA device"
lead: "Moving your authenticator to a new phone, switching authenticator apps, or replacing a lost device all depend on the same thing: how you sign in to the Chainguard Console. This guide explains how to tell which sign-in path you use and where to change your MFA for each one."
description: "Change or reset the multi-factor authentication device you use with the Chainguard Console, whether your MFA is managed by your identity provider or by Chainguard."
type: "article"
date: 2026-09-11T00:00:00+00:00
lastmod: 2026-09-11T00:00:00+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 020
toc: true
---

You might need to move your multi-factor authentication (MFA, also called 2FA) to a new device because you replaced your phone, changed authenticator apps, or lost the device that generates your codes. Where you make that change depends on how you sign in to the Chainguard Console, because Chainguard manages MFA for only one of the sign-in paths.

## Find out which sign-in path you use

The Console login screen has buttons for Google, GitHub, and GitLab, along with a single field that accepts either your email address or your organization name. What you click or enter there determines your path:

- **You click Google, GitHub, or GitLab.** That provider signs you in.

- **You enter your organization name.** The Console sends you to the identity provider your organization registered.

- **You enter an email address whose domain your organization registered with a custom identity provider.** The Console sends you to that provider.

- **You enter any other email address.** The Console sends you to Chainguard's email and password sign-in, which always asks for a one-time code from an authenticator app.

Your path determines who holds your MFA enrollment:

| How you sign in | Who manages your MFA | Where to change it |
| --- | --- | --- |
| Google, GitHub, or GitLab | That provider | Your account settings with that provider |
| Your organization's identity provider, such as Okta, Microsoft Entra ID, Ping Identity, or Keycloak | Your own organization | Your internal IT or identity provider administrator |
| Your email address and a password | Chainguard | A support ticket opened by an Owner in your organization |

## Change MFA managed by an identity provider

When you sign in through Google, GitHub, GitLab, or your organization's own identity provider, that provider holds your MFA enrollment. Chainguard can neither see it nor change it, so Chainguard support can't reset it for you. Change it where you manage the rest of that account:

- **Google.** See [Turn on 2-Step Verification](https://support.google.com/accounts/answer/185839) in Google Account Help.

- **GitHub.** See [Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication).

- **GitLab.** See [Two-factor authentication](https://docs.gitlab.com/user/profile/account/two_factor_authentication/).

- **A corporate identity provider.** Contact your internal IT helpdesk or the administrator who manages the provider.

After you change MFA with your provider, sign in to the Console as usual. Nothing needs to change on the Chainguard side.

## Change MFA for email and password sign-in

Chainguard manages this path through Auth0, which hosts the sign-in screen at `auth.chainguard.dev` and holds your MFA enrollment. MFA is required here, so this path always asks for a code. You can't change or reset your own device: the Console has no MFA settings page, and Chainguard's sign-in configuration includes no self-service reset.

If you still have your old device, check whether your authenticator app can move the entry for you. Some apps can transfer an existing entry to a new device, though whether yours can, and how, depends on the app. If it can't, or if you no longer have the old device, ask Chainguard to reset your enrollment.

### Ask for a reset

Chainguard doesn't act on an MFA reset requested from the account's own email address. Anyone who controlled your mailbox could already request a password reset, so treating an emailed request as proof of identity would defeat the purpose of the second factor.

Instead, ask an Owner in your Chainguard organization to open a support ticket on your behalf. [Resetting your MFA device for the Chainguard Console](https://support.chainguard.dev/hc/en-us/articles/52523310297115-Resetting-your-MFA-device-for-the-Chainguard-Console) in the Chainguard knowledge base describes the process.

Once support clears your enrollment, sign in to the Console again. The sign-in flow prompts you to enroll and displays a new QR code, which you scan with your authenticator app to finish. You won't receive an automatic notification when the reset happens, so watch your support ticket for the update.

## One email address, two identities

If your organization registered a custom identity provider after you had already created an email and password account, you might hold two separate Chainguard identities that share one email address. Chainguard identifies you by the provider that issued your login together with your ID at that provider, not by your email address, so the platform treats the two as distinct accounts. Each carries its own MFA, in a different place.

When the Console asks for a code from an authenticator app and you expected to sign in through your organization's provider, you're on the email and password path. Enter your organization name in the login field instead of your email address to reach your provider.

## Get more help

If you can't sign in at all and therefore can't reach the support portal, see [Get support](/get-started/get-support/) for the right channel.
