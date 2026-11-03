---
title: "Upgrade to Chainguard Team"
date: 2026-11-03T16:40:38+00:00
lastmod: 2026-11-03T16:40:38+00:00
linktitle: "Upgrade to Team"
description: "Move a Chainguard Starter organization to the paid Chainguard Team plan with chainctl, pay by card, and manage or cancel the plan"
type: "article"
draft: false
weight: 16
toc: true
tags: ["Procedural"]
---

[Chainguard Team](/get-started/self-serve/plans/) is Chainguard's paid self-serve plan. You upgrade a Chainguard Starter organization to Team with `chainctl` and pay by card, and Team limits apply as soon as the first payment succeeds. This page covers upgrading, what changes afterward, how billing works, and how to change your card or cancel.

## Before you begin

You need the following:

* A Chainguard Starter organization. To create one, refer to [Sign up for Chainguard Starter](/get-started/self-serve/sign-up-starter/).
* The `limited_owner` or `owner` role in that organization. The person who created a Starter organization has the `limited_owner` role.
* `chainctl` 0.2.394 or later. To update it, run `sudo chainctl update`, or `brew upgrade chainctl` if you installed it with Homebrew.
* A credit or debit card and its billing address.

## Upgrade your organization

To upgrade to Team, complete the following steps:

1. Run `chainctl plans update` with `--plan team`:

    ```shell
    chainctl plans update --plan team
    ```

    If you belong to more than one organization, add `--parent` with the name of the organization to upgrade.

1. In the checkout page that opens in your browser, enter your card and billing address, then save them. Saving the card doesn't charge it.
1. Wait for the first payment. Chainguard charges the card for the first month, and your organization moves to Team once the charge succeeds. That usually takes less than a minute, but can take up to an hour.
1. Confirm the upgrade:

    ```shell
    chainctl plans describe
    ```

    The output names the Team plan. Until the payment succeeds, it still reads Starter.

If you're working on a machine without a browser, such as over SSH, add `--no-browser`. The command prints the checkout page's URL, which you can open on another device.

## What changes when you upgrade

Your organization keeps its name, members, and images, and gets the following:

* **Team limits.** Refer to [Plan limits](/get-started/self-serve/plans/#plan-limits) for the full list.
* **The `owner` role for you.** The person who completes checkout is made an owner of the organization.
* **Image swaps.** You can replace an image you chose with another one, twice in a rolling 30 days.
* **Invitations outside your email domain.** You can invite anyone, with any role you hold yourself.
* **CVE-remediated Chainguard Libraries versions.**
* **Ticket support** during business hours. Refer to [Get support](/get-started/get-support/).

If you created your organization with a personal email address, its Checks and Workspaces compute stops at the included amount rather than being metered past it. To run more, [buy compute](/get-started/self-serve/usage-and-billing/#buy-checks-and-workspaces-compute) in advance.

## How Team is billed

Team is billed monthly, in advance, to the card you saved. The first month starts on the day you upgrade. Applicable tax is added. For the current price, refer to the [Chainguard pricing page](https://www.chainguard.dev/pricing).

Chainguard meters usage past Team's included amounts, such as storage above 500 GiB, and starts charging for it on January 1, 2027. To check your usage, refer to [Usage, limits, and billing](/get-started/self-serve/usage-and-billing/).

## Change your card

To replace the card your plan is charged to, run `chainctl plans add-card`. It opens a page where you save a new card, without charging anything:

```shell
chainctl plans add-card
```

## Cancel Team

To cancel Team, contact Chainguard support. Refer to [Get support](/get-started/get-support/). Cancellation takes effect at the end of the current billing month, and your organization then moves back to Starter.

To move to an Enterprise plan instead, [contact Chainguard](https://www.chainguard.dev/contact).
