---
title: "Usage, limits, and billing"
date: 2026-11-03T16:40:38+00:00
lastmod: 2026-11-09T19:57:25+00:00
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

Usage figures include anything above an included amount. On Team, storage shows as unlimited, because storage past the included 500 GiB is metered, not refused. Image egress is shown in bytes. If Chainguard can't measure a figure yet, the list shows a dash; for a new organization, that's usually the case until Chainguard's next hourly usage count. Both commands accept `--output json`.

On Starter, the rows for application, base, and AI images each show a limit of 5, but those images share one total of 5, which the catalog images row shows.

### Check usage from a script

Chainguard doesn't send you alerts as you approach a limit. To watch for limits from a scheduled job, run `chainctl plans quotas list` with `--near` and `--output json`, and read the JSON:

```shell
chainctl plans quotas list --near --output json
```

Don't rely on the exit status alone. Both `plans` commands exit with status 1 when usage is unavailable, and `quotas list --near` also exits with status 1 when no quota is near its limit.

## When a request is refused

When a request would go past a plan limit, Chainguard refuses it and returns an error that names your plan and the limit, and what you've used or what you asked for. `chainctl` follows it with the `chainctl plans quotas list` command that shows the related limits. For example, the error message for a cooldown outside Team's range reads as follows:

```output
Team plan allows a library cooldown of 0 to 7 days (14 days requested). Upgrade: https://www.chainguard.dev/pricing or run: chainctl plans update --plan enterprise
```

To respond to a refusal, do one of the following:

* **Stay within the limit.** For example, if you're at the pull-token limit, revoke a token you no longer use before you create another one.
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

1. In the checkout page that opens in your browser, enter your card and billing address, then save them. If the page shows **I'm purchasing as a business**, which depends on your billing country, you can select it and enter a business tax ID, such as a VAT number. The first purchase opens this page even if you saved a card earlier.

Chainguard charges the card for the balance, plus applicable tax. When the balance falls below 20% of the amount you bought, Chainguard charges the card again to bring it back to that amount. Unused balance expires one year after you buy it.

Usage that runs past a spent balance, while a refill is being charged or after one fails, is charged at the end of the month. If a refill fails, replacing your card with `chainctl plans add-card` doesn't turn automatic refills back on. To restart them, contact Chainguard support.

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
* **Storage above Team's included 500 GiB**, starting January 1, 2027.

Starter is free. Applicable tax is added to every charge. For prices, refer to the [Chainguard pricing page](https://www.chainguard.dev/pricing).
