---
title: "See who created a pull token or identity"
linktitle: "Identity creators"
type: "article"
description: "Find out who created a pull token or other identity in your Chainguard organization, using the Chainguard Console, chainctl, or the Chainguard API."
lead: "Chainguard records who created each pull token and identity, so you can trace a token back to the person or workload that made it."
date: 2026-11-19T00:00:00+00:00
lastmod: 2026-11-19T00:00:00+00:00
draft: false
tags: ["Console", "chainctl", "IAM", "Procedural", "Reference"]
images: []
menu:
  docs:
    parent: "iam-organizations"
weight: 35
toc: true
---

When you create a pull token or any other [identity](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/) in your organization, Chainguard records who created it. You can see the creator in the Chainguard Console, in `chainctl`, and in the Chainguard API. This helps you answer questions like "who made this pull token, and do they still need it?" without searching your own records.

## What Chainguard records

Each identity has two related values:

* **Created by** is the ID of the identity whose credentials created it. Chainguard sets it when the identity is created and never changes it afterward. You can't set or edit it yourself.
* **Creator email** is the creator's current verified email address. Chainguard looks it up each time you view the identity rather than storing it, so it reflects the creator's email today, not when they created the identity.

The creator is whoever made the request. If a person creates a pull token while signed in, the creator is that person. If a CI workflow creates an identity using an [assumable identity](/platform/administration/assumable-ids/assumable-ids/), the creator is that assumable identity, not the person who set up the workflow.

### When the creator email is empty

Chainguard shows the creator email only while the creator holds a role in your organization, either on the organization itself or on a folder within it. The email is empty when:

* The creator no longer holds a role in your organization.
* The creator doesn't have a verified email address. This is typical for assumable identities and other non-human identities.
* The creator's identity was deleted.

In each case, the **Created by** ID is still available.

### When no creator is recorded

Some identities have no creator recorded:

* **Identities created before this feature was released.** Chainguard didn't record creators before then, and can't add a creator to these identities later.
* **Your own user identity.** The identity Chainguard creates when you first sign in has no creator, because no one else made it.

If you need to know who created an older pull token, check your own records, such as the CI configuration or secret store where the token is used. If no one claims the token, consider [revoking it](/chainguard/containers/registry/authenticating/#revoking-a-pull-token) and creating a new one, which records its creator.

## View the creator in the Chainguard Console

1. In the [Chainguard Console](https://console.chainguard.dev), go to **Settings** and open **Pull tokens**.
2. Find the token in the list. The **Created by** column shows the creator's email, or the creator's ID if the email isn't available.
3. To see more detail, select the token. The details panel shows the creator's email and ID. If no creator was recorded, it shows **Not recorded**.

## View the creator with chainctl

To see the creator of each pull token in an organization, run:

```sh
chainctl auth pull-token list --parent=ORGANIZATION_NAME
```

The output includes a **Created By** column. The column is empty for tokens that have no recorded creator.

To see the creator of a single identity, run:

```sh
chainctl iam identities describe IDENTITY_ID
```

The output includes a `Created by:` line when a creator was recorded, and leaves the line out otherwise.

Both commands, and `chainctl iam identities list`, include the creator in JSON output. Add `--output=json` to get `created_by` and `creator_email` for each identity.

## View the creator with the Chainguard API

The identity resource includes both values as output-only fields:

| Field | API v1 | API v2 |
| --- | --- | --- |
| Created by | `created_by` | `createdBy` |
| Creator email | `creator_email` | `creatorEmail` |

The fields appear when you get, list, create, or update an identity. Because they're output only, the API ignores any value you send for them.

If you subscribe to [Chainguard events](/platform/administration/cloudevents/events-reference/), the `actor.subject` of each `dev.chainguard.api.iam.identity.created.v1` event names the identity that created it. Events never include the creator email, so email addresses aren't sent to your event subscriptions.

## Match a creator ID to a person

If you have a creator ID but no email, you can look it up in your organization's role bindings:

```sh
chainctl iam role-bindings list --parent=ORGANIZATION_NAME
```

Find the creator ID in the **Identity** column to see that identity's name and email. If the ID doesn't appear, the creator no longer holds a role in your organization.
