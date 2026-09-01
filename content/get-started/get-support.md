---
title: "Get support"
linktitle: "Get support"
lead: "Chainguard offers several ways to get help, and the right one depends on your situation. This guide covers which channel handles your kind of request, what you need in place before you can open a support ticket, and what to include when you do."
description: "Get help from Chainguard: choose the right support channel, meet the prerequisites for the support portal, and open a ticket a support engineer can act on."
type: "article"
date: 2026-09-01T00:00:00+00:00
lastmod: 2026-09-01T00:00:00+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 015
toc: true
---

When the documentation doesn't answer your question, Chainguard offers several ways to get help. This guide covers which channel handles your kind of request, what you need in place before you can open a support ticket, and what to include when you do.

## Where to send your request

The support portal handles most requests, but it isn't the only route, and for some situations it isn't the right one. Find your situation in the following list:

- **You have a problem with a Chainguard product or with your organization's configuration.** Open a ticket in the [support portal](https://support.chainguard.dev/).

- **You can't sign in to the Chainguard Console, and your organization uses single sign-on — for example, you've lost the device running your authenticator app.** Contact the identity provider administrator at your own organization. When you sign in through Google, GitHub, GitLab, or a corporate identity provider, that provider manages your multi-factor authentication, and Chainguard can neither see it nor change it.

- **You can't sign in at all, so you can't reach the portal.** Email [support@chainguard.dev](mailto:support@chainguard.dev).

- **Your organization uses Catalog Starter.** Use the [knowledge base](https://support.chainguard.dev/hc/en-us), the [community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw), and the free [Chainguard courses](https://courses.chainguard.dev/). Catalog Starter doesn't include ticket access.

- **Your request concerns your subscription or what your organization is licensed for — for example, whether a particular image is included in your entitlements.** Contact your account team, meaning the customer success manager or solutions architect assigned to your organization.

## Before you open a ticket

Many questions already have a published answer you can find in seconds:

- **This documentation site.** Search from the box at the top of any page.

- **Ask AI.** Click **Ask AI** in the upper-right corner of any page on this site and ask your question in plain language. The assistant draws on Chainguard's documentation and support content and cites its sources. Review the answer and its sources before you act on it.

- **The [Chainguard knowledge base](https://support.chainguard.dev/hc/en-us).** Chainguard support engineers publish articles there for problems that come up repeatedly.

## Open a ticket

### Confirm that you can reach the portal

The support portal has two prerequisites.

First, your organization needs a paid plan. Catalog Starter doesn't include support tickets, root cause analysis, or phone escalation. For what the free plan does cover, see [Chainguard Catalog Starter](/chainguard/containers/about/catalog-starter/).

Second, your identity has to be linked to an organization. The portal identifies you through your Chainguard Console account, and an unlinked identity produces an error. To check, sign in to the [Chainguard Console](https://console.chainguard.dev) and look for your organization in the left sidebar. If it isn't there, ask an administrator in your organization to invite you, then open the invitation email and complete the setup flow. Signing in without completing that flow leaves your identity unlinked.

{{< note >}}
Administrators can invite users from the Console under **Settings > Users > Invite users**, or from the command line. See [How to manage IAM organizations in Chainguard](/platform/administration/iam-organizations/how-to-manage-iam-organizations-in-chainguard/).
{{< /note >}}

### Submit the request

1. Sign in to the [Chainguard Console](https://console.chainguard.dev).

1. In the left sidebar, click **Support**. You can also go to [support.chainguard.dev](https://support.chainguard.dev/) directly.

1. Fill in the request form. Before you submit, the portal offers relevant documentation and a generated answer. If that resolves your question, you're finished. Otherwise, submit the request as usual.

### If the portal returns an error

Work through the following steps:

1. Open the Console and the support portal in a private browsing window.

1. Clear your browser cache and cookies.

1. Confirm that you're signing in with the same identity you were invited with.

If the error persists, email [support@chainguard.dev](mailto:support@chainguard.dev) with a screenshot of the error, the email address of the account you're trying to use, and the invitation link if you still have it.

## What to include in your request

A support engineer can start on a problem instead of asking you for more information when your request includes:

- Your organization name.

- The image or package name and tag, and the digest if you have it.

- The command you ran and its complete output, including any error message.

- The `chainctl` version, if the problem involves the command-line tool. Run `chainctl version` to get it.

- What you expected to happen instead.
