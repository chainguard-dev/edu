---
title: "Chainguard plans"
date: 2026-11-03T16:30:40+00:00
lastmod: 2026-11-05T12:46:23+00:00
linktitle: "Plans"
description: "Compare the Chainguard Starter and Chainguard Team self-serve plans, including the limits that apply to each"
type: "article"
draft: false
weight: 12
toc: true
tags: ["Reference"]
---

Chainguard offers two self-serve plans, which you can sign up for, use, and upgrade without talking to anyone at Chainguard:

* **Chainguard Starter** is free. It gives a small team access to Chainguard Containers, Chainguard Libraries, Chainguard Checks, Chainguard Workspaces, and Guardener. To start, refer to [Sign up for Chainguard Starter](/get-started/self-serve/sign-up-starter/).
* **Chainguard Team** is a paid plan for teams that outgrow Starter. It raises most Starter limits, removes the caps on members and CI identities, and includes ticket support. A Starter organization [upgrades to Team](/get-started/self-serve/upgrade-team/) with `chainctl` and pays by card.

Enterprise plans, which cover features such as FIPS images, SSO, and custom policies, are set by contract. To discuss one, [contact Chainguard](https://www.chainguard.dev/contact). For prices, refer to the [Chainguard pricing page](https://www.chainguard.dev/pricing).

## Plan limits

The following table lists what each self-serve plan includes:

| | Chainguard Starter | Chainguard Team |
| --- | --- | --- |
| **Chainguard Containers** | | |
| Catalog images | 5 application, base, or AI images | 5 application, base, or AI images |
| Image swaps | None | 5 per rolling 30 days |
| Helm charts | Charts for your images | Coming soon |
| Image egress | 100 GiB a month | 1 TiB a month |
| Storage | 100 GiB | 500 GiB included, then metered |
| **Chainguard Libraries** | | |
| Ecosystems | Java, Python, JavaScript, .NET, and Go | Java, Python, JavaScript, .NET, and Go |
| CVE-remediated versions | Not included | Included |
| Package pulls | 50,000 a month | 1,000,000 a month |
| Cooldown period | Fixed at 7 days, no per-package override | 0 to 7 days |
| **Chainguard Checks and Chainguard Workspaces** | | |
| Checks compute | 500 vCPU-hours a month | 1,000 vCPU-hours a month included, then metered up to 2,000 |
| Workspaces compute | 500 vCPU-hours a month | 1,000 vCPU-hours a month included, then metered up to 2,000 |
| Workspaces sessions | 3 per organization, 1 per member | 3 per organization, 1 per member |
| **Organization and access** | | |
| Members | Up to 5, from your email domain | Unlimited |
| CI identities | 3 | Unlimited |
| Pull tokens | 5 active, each valid for up to 30 days | 5 active, each valid for up to 7 days |
| [CloudEvents](/platform/administration/cloudevents/) subscriptions | None | 1 |
| SSO and SCIM | Not included | Not included |
| **Support** | Community | Tickets during business hours, with no response-time commitment |

Monthly limits reset at the start of each calendar month, in UTC. GiB and TiB are binary units: 1 GiB is 1,024 MiB, and 1 TiB is 1,024 GiB. Chainguard uses these units when it reports usage and when it refuses a request.

Chainguard counts Starter usage against the limits for image egress, storage, and package pulls now, and starts refusing requests past them on January 1, 2027. To see which limits you're already near, run `chainctl plans quotas list --near`.

FIPS, developer-tool, and commercial images need an Enterprise plan.

On Starter, a newly published package version stays unavailable for 7 days, and you can't override the cooldown for a package. For how the Libraries cooldown limits work, refer to [Cooldown limits by plan](/chainguard/chainguard-repository/library-policies/#cooldown-limits-by-plan).

A Starter organization created with a personal email address can't invite anyone until it upgrades to Team.

Team pull tokens last at most 7 days. To authenticate CI pipelines on Team without replacing a secret every week, use a CI identity, which Team doesn't cap. Refer to [Overview of assumable identities in Chainguard](/platform/administration/assumable-ids/assumable-ids/).

### What the limits count

* **Image egress** counts the image layers you download. Manifests don't count.
* **Package pulls** count one download of one package version, however many files the download includes. A version served from the upstream registry counts the same as one Chainguard built.
* **Storage** counts the images, uploads, and skills your organization pushes, and the Libraries packages it uploads. The Chainguard images you pull don't count.

## What happens at a limit

A plan limit is a cap, an included amount, or a feature the plan doesn't include:

* **A cap** refuses the next request that would go past it. Work that's already running, such as an image pull, finishes.
* **An included amount** keeps serving you past the limit and meters the extra usage. On Team, storage and Checks and Workspaces compute are included amounts. On Team, compute past 2,000 vCPU-hours a month is refused, unless your organization has bought compute.
* **A feature the plan doesn't include**, such as SSO, is refused whenever you try to use it.

A Team organization created with a personal email address, rather than a business email domain, can't go past its included compute. To run more, [buy compute](/get-started/self-serve/usage-and-billing/#buy-checks-and-workspaces-compute) in advance.

A refused request returns an error that names your plan and the limit, and what you've used or what you asked for, followed by a link to the pricing page and a `chainctl plans update` command for the next plan. For example:

```output
Team plan allows a library cooldown of 0 to 7 days (14 days requested). Upgrade: https://www.chainguard.dev/pricing or run: chainctl plans update --plan enterprise
```

To see your organization's plan and the limits it's close to, run `chainctl plans describe`:

```shell
chainctl plans describe
```

To list every limit with its current usage, run `chainctl plans quotas list`. Add `--near` to show only the limits you're close to.

## Mirroring

The self-serve plans' terms don't allow mirroring Chainguard images or packages into a repository manager, such as JFrog Artifactory.
