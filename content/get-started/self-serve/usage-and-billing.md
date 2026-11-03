---
title: "Usage, limits, and billing"
date: 2026-11-03T16:40:38+00:00
lastmod: 2026-11-03T16:40:38+00:00
linktitle: "Usage and billing"
description: "Check your Chainguard Starter or Chainguard Team organization's usage against its plan limits, respond to a refused request, and buy Checks and Workspaces compute"
type: "article"
draft: false
weight: 18
toc: true
tags: ["Procedural"]
---

Every Chainguard Starter and Chainguard Team organization has [plan limits](/get-started/self-serve/plans/#plan-limits). This page covers checking your usage against them, what to do when a request is refused, buying more Chainguard Checks and Chainguard Workspaces compute, and what Chainguard charges you for.

## Check your usage

To see your organization's plan, the products it can use, and any limits it's close to, run `chainctl plans describe`:

```shell
chainctl plans describe
```

To list every limit with its current usage, run `chainctl plans quotas list`:

```shell
chainctl plans quotas list
```

The following options narrow the list:

* `--near` shows only the limits you're close to or have reached.
* `--product` shows only the products you name, separated by commas. The products are `images`, `helm-charts`, `libraries`, `packages`, `skills`, `actions`, `checks`, `workspaces`, and `platform`.
* `--parent` names the organization to check, if you belong to more than one.

Usage figures include anything above an included amount. If Chainguard can't measure a figure yet, the list shows a dash. Both commands accept `--output json`.

## When a request is refused

When a request would go past a plan limit, Chainguard refuses it and returns an error that names your plan, the limit, and what you requested. `chainctl` follows it with the `chainctl plans quotas list` command that shows the related limits. For example, the error message for a cooldown outside Team's range reads as follows:

```output
Team plan allows a library cooldown of 0 to 7 days (14 days requested). Upgrade: https://www.chainguard.dev/pricing
```

To respond to a refusal, do one of the following:

* **Stay within the limit.** For example, choose a cooldown period in your plan's range.
* **Wait for the monthly reset.** Monthly limits, such as image egress and package pulls, reset at the start of each calendar month, in UTC.
* **Buy compute.** If the refusal is for Checks or Workspaces compute, [buy compute](#buy-checks-and-workspaces-compute).
* **Upgrade.** On Starter, [upgrade to Chainguard Team](/get-started/self-serve/upgrade-team/). On Team, [contact Chainguard](https://www.chainguard.dev/contact) about an Enterprise plan.

A refusal stops only the next request. Work that's already running, such as an image pull, finishes.

## Buy Checks and Workspaces compute

Each month, your organization uses its plan's included Checks and Workspaces compute first. To run more, a Team organization can buy a prepaid compute balance with `chainctl plans top-up`. You need the `limited_owner` or `owner` role.

### Make your first purchase

1. Run `chainctl plans top-up`. To buy an amount other than the $100 default, add `--amount` with a whole number of US dollars from 25 to 5,000:

    ```shell
    chainctl plans top-up --amount 200
    ```

1. In the checkout page that opens in your browser, enter your card and billing address, then save them. The first purchase opens this page even if you saved a card earlier.

Chainguard charges the card for the balance, plus applicable tax. When the balance falls below 20% of the amount you bought, Chainguard charges the card again to bring it back to that amount. Unused balance expires one year after you buy it.

### Buy more

After the first purchase, run the same command to add to your balance:

```shell
chainctl plans top-up --amount 200
```

`chainctl` shows what it will charge to your card on file and asks you to confirm. To skip the prompt, such as in a script, add `--yes`.

If the connection drops before you learn whether a purchase went through, `chainctl` prints a request ID. Run the command again with `--request-id` and that ID, so you're charged at most once:

```shell
chainctl plans top-up --amount 200 --request-id $REQUEST_ID
```

## What Chainguard charges for

Chainguard charges the following to the card you save:

* **The Team plan fee**, monthly in advance. Refer to [How Team is billed](/get-started/self-serve/upgrade-team/#how-team-is-billed).
* **Compute balances** that you buy, when you buy them and when they refill.
* **Usage past Team's included amounts**, starting January 1, 2027.

Starter is free. Applicable tax is added to every charge. For prices, refer to the [Chainguard pricing page](https://www.chainguard.dev/pricing).
