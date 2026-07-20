---
aliases:
- /chainguard/administration/api-v2-migration/
title: "Migrating from API v1 to API v2"
linktitle: "API v1 to v2 Migration"
type: "article"
description: "How to migrate a direct integration with the Chainguard API from v1 to the GA API v2."
date: 2026-07-20T00:00:00+00:00
lastmod: 2026-07-20T00:00:00+00:00
draft: false
tags: ["Chainguard Console", "Procedural"]
images: []
toc: true
weight: 040
---

> **Draft status:** This page has several items marked `CONFIRM WITH ENGINEERING`. Do not publish externally until those are resolved.

Chainguard's API v2 is now Generally Available (GA) across every product domain: Customer Platform (IAM), Containers, Ecosystems, and Integrations. At GA, the "beta" designation is dropped: endpoints move from `/v2beta1/` to `/v2/`. This guide covers what changed from v1, and the steps to migrate an existing direct integration.

If you only use `chainctl`, the Chainguard Console, or the Terraform provider, you don't need this guide — those clients handle versioning for you, and nothing changes on your end. This guide is for anyone calling the API directly: `curl`, gRPC, or a custom SDK integration.

v1 continues to work during a transition period, so nothing breaks today. Migrate at your own pace; see [Timeline](#timeline) for what happens next.

## Prerequisites

You'll need:

- A valid Chainguard identity with access to the resources you're calling.
- `chainctl` installed, to mint a token for testing (`chainctl auth token`).

Set up your environment for the following examples:

```shell
export TOKEN=$(chainctl auth token)
export API=https://console-api.enforce.dev
# ORG_ID is the UID of your root organization group
export ORG_ID=YOUR_ORG_ID
```

## What's not changing

- **Authentication** — same OIDC token model as v1.
- **Authorization** — same identity-based access control.
- **Scoping** — same `uidp.descendants_of` / `uidp.children_of` hierarchy filters.
- **Host** — same API host (`console-api.enforce.dev` in production).

If your integration already authenticates against v1 successfully, no credential or auth-flow changes are needed to call v2.

## Quick reference

| Operation | v1 pattern | v2 pattern |
| --- | --- | --- |
| Path versioning | Unversioned (`/iam/...`, `/registry/...`, `/vulnerabilities/...`, `/libraries/...`, `/advisory/...`) | Versioned: `/v2/...` for every domain |
| Field naming | Inconsistent (`id`, `created_at`, `group_id`) | Consistent camelCase (`uid`, `createTime`/`updateTime`) |
| CREATE | Parent resource identified in the URL path | Parent identified in the request body |
| GET (single resource) | No dedicated endpoint; filter a List call | Dedicated Get endpoint, fetch by `uid` |
| LIST | Offset/page-number params, full result set, no total count | `page_size`, `page_token`, `skip`, `order_by`, `total_count` |
| UPDATE | PUT, full-resource replacement | PATCH, partial update via a field mask |
| DELETE | Same path pattern, ambiguous failure on blocked deletes | Same path pattern, returns a `PreconditionFailure` detail when blocked |
| Errors | Ambiguous — a missing resource can return an empty HTTP 200 result | Structured: `ErrorInfo`, `BadRequest`, `ResourceInfo`, `PreconditionFailure`, with proper status codes |
| Rate limiting | Not enforced | Enforced |

### Path prefixes by domain

| Domain | v1 path prefix | v2 path prefix (GA) |
| --- | --- | --- |
| IAM (Customer Platform: groups, roles, identities, role bindings) | `/iam/` | `/iam/v2/` |
| Registry (Containers) | `/registry/` | `/registry/v2/` |
| Vulnerabilities | `/vulnerabilities/` | `/vulnerabilities/v2/` |
| Libraries (Ecosystems) | `/libraries/` | `/libraries/v2/` |
| Advisory (Integrations) | `/advisory/` | `/advisory/v2/` |

If you built against the beta endpoints, updating the version segment from `v2beta1` to `v2` is the only path change — the request and response shapes don't change as part of that rename.

## Migration steps

### Step 1: Update your endpoint paths

Add the `v2` version segment for each domain you call, using the [path prefix table](#path-prefixes-by-domain). If you were already on `/v2beta1/`, rename it to `/v2/`.

### Step 2: Update field references

v2 standardizes field naming across every service:

- Resource identifiers are always `uid`, never `id`.
- Timestamps are `createTime` / `updateTime`, not `created_at` / `updated_at`.
- All fields use camelCase.

Update any code that reads specific field names out of API responses — these differ from v1 even for the same resource.

### Step 3: Move CREATE calls to parent-in-body

v1 identifies the parent resource in the URL path (for example, `/groups/{parent}`). v2 moves the parent identifier into the request body instead, alongside the fields of the resource being created.

**v1 (illustrative):**

```shell
curl -X POST -H "Authorization: Bearer $TOKEN" \
  "$API/iam/groups/$PARENT_UID" \
  -d '{"name": "my-group"}'
```

**v2 (illustrative):**

```shell
curl -X POST -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups" \
  -d '{"parent": "'"$PARENT_UID"'", "group": {"name": "my-group"}}'
```

> **CONFIRM WITH ENGINEERING:** this request body is illustrative. Get the exact body schema — including the `"group"` wrapper field name — from engineering before publishing.

Stop building create-call URLs with the parent embedded in the path. Build a request body that includes both the parent identifier and the new resource's fields instead.

### Step 4: Switch updates to PATCH with a field mask

v1 uses PUT semantics: changing one field means sending the entire resource back, which forces a fetch-before-write pattern and creates race conditions on concurrent updates. v2 uses PATCH with a field mask, so you specify only the fields you're changing.

```shell
curl -X PATCH -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups/$GROUP_UID?updateMask=description" \
  -d '{"description": "updated description"}'
```

Testing against the live beta API confirmed this `updateMask` parameter name works. It's presumed unchanged at GA, but worth a final confirmation since none of the GA source docs restate it.

Replace fetch-modify-write update logic with a PATCH call that sets only the fields you're changing. A wildcard `*` is available if you genuinely want full replacement.

### Step 5: Switch pagination to cursor-based

v1 pagination relies on page numbers or offsets, and loads the full result set into memory. v2 List endpoints add:

- `page_size` — how many items to return per page.
- `page_token` — the opaque cursor from the previous response's `next_page_token`, used to fetch the next page. Omit it for the first page.
- `skip` — number of items to skip, for jumping directly to a specific page without walking the cursor sequentially.
- `order_by` — server-side ordering, instead of sorting client-side after fetching.
- `total_count` — total matching items, so you don't have to infer it from page math.

```shell
curl -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=3&order_by=name" | jq .
```

Replace any page-number or offset logic with a loop that follows `page_token` until the response stops returning one. Use `skip` instead if you need to jump to an arbitrary page. Adopt `order_by` and drop any client-side sort you were doing to compensate.

### Step 6: Use dedicated Get endpoints

v1 typically requires filtering a List call to fetch a single resource. v2 adds a dedicated Get endpoint per resource, fetched by `uid` directly.

```shell
curl -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups/$GROUP_UID"
```

Replace any "list and filter to one item" pattern with the dedicated Get endpoint for that resource.

### Step 7: Update your error handling

In v1, an empty or ambiguous result can mean several different things — no matches, no permission, or a missing parent resource — with no way for a client to tell them apart. For example, requesting a resource that doesn't exist in v1 returns an empty result with HTTP 200.

v2 returns proper status codes (for example, `NOT_FOUND` / HTTP 404) with structured error details, following the same error model used across Google Cloud APIs:

- **ErrorInfo** — a machine-readable reason code and error domain.
- **BadRequest** — per-field validation errors.
- **ResourceInfo** — which specific resource type and name wasn't found.
- **PreconditionFailure** — why a request was blocked (for example, a delete blocked by a dependent resource).

If your integration currently treats an empty v1 result as ambiguous, or works around that ambiguity with extra calls, update it to branch on the v2 status code and structured error details instead. Re-test your error-handling paths, not just the happy path.

### Step 8: Review rate limits

Rate limits were not enforced during beta. They are enforced starting at GA.

> **CONFIRM WITH ENGINEERING:** specific rate limits and response headers (for example, remaining-quota headers). Add them here once confirmed, and link out to a rate-limits reference page if one exists.

Review your call patterns — polling frequency, batch sizes — against the confirmed limits before cutting production traffic over.

### Step 9: Update gRPC and SDK clients

All v2 endpoints are also available directly via gRPC, at the same host. Proto definitions are at `chainguard.dev/sdk/proto/chainguard/platform/`. If you call the API via generated gRPC clients, regenerate them against the GA `v2` proto packages, renamed from `v2beta1`.

> **CONFIRM WITH ENGINEERING:** whether the Go SDK client library actually moves from `chainguard.dev/sdk/proto/platform/clients/v2beta1` to an equivalent `v2` path at GA, or keeps the `v2beta1` package name internally even after the REST paths rename.

## Full example: listing and deleting groups

**Before (v1):**

```shell
curl -H "Authorization: Bearer $TOKEN" \
  "$API/iam/groups?uidp.descendants_of=$ORG_ID"
```

**After (v2):**

```shell
curl -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=3&order_by=name" | jq .
```

Delete calls follow the same path-prefix change, with no other behavior change:

```shell
curl -X DELETE -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/roleBindings/$BINDING_UID"
curl -X DELETE -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/identities/$IDENTITY_UID"
curl -X DELETE -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups/$GROUP_UID"
```

Each `DELETE` returns an empty response body on success, same as v1. A delete blocked by a dependent resource now returns a `PreconditionFailure` error detail explaining why, instead of an ambiguous failure.

## Timeline

| Phase | When | What it means for you |
| --- | --- | --- |
| Parallel availability | GA onward | Both v1 and v2 serve traffic. v1 responses include deprecation headers noting the eventual sunset date. Migrate at your own pace. |
| Warning escalation | `CONFIRM WITH ENGINEERING` | v1 responses add an additional warning header. If you have meaningful v1 traffic, your Chainguard account team may reach out directly. |
| Soft shutdown | `CONFIRM WITH ENGINEERING` | v1 requests return an error with migration guidance, for a short grace period. |
| Hard removal | `CONFIRM WITH ENGINEERING` | v1 is fully removed. Requests to v1 endpoints fail. |

> **CONFIRM WITH ENGINEERING:** every date in this timeline is a placeholder. Don't ship this table as-is.

Don't wait for a hard deadline to start testing v2 — both versions are available today, and migration can happen incrementally.

## Troubleshooting

**Will my existing integration stop working today?**
No. v1 keeps working during the parallel availability period. Nothing changes for existing integrations until the sunset date, which will be communicated well in advance.

**Do I need new credentials for v2?**
No. Authentication and authorization are unchanged — the same tokens and identities that work with v1 work with v2.

**Why did an API call that used to return an empty list now return an error?**
This is expected, and it's an improvement. In v1, a missing resource and an empty result look the same, so there was no way to tell "nothing matched" apart from "that resource doesn't exist" or "you don't have permission." v2 returns a specific, structured error in those cases instead.

**Why did my create call stop working?**
Check whether you're building the request URL with the parent resource in the path — that's the v1 pattern. In v2, the parent goes in the request body instead. See [Step 3](#step-3-move-create-calls-to-parent-in-body).

**Where do I send a customer who asks about migrating?**
This guide. If you're on the account or support team, reach out to Engineering for anything marked `CONFIRM WITH ENGINEERING` in this guide rather than guessing at specifics.

## Next steps

- [Chainguard API v2 Tutorial](/platform/api/api-v2-tutorial/) — worked examples of the v2 endpoints you'll be migrating to.
- [Chainguard API v2 Specification](/platform/api/spec-api-v2/) — full OpenAPI reference.
- Reach out to your Chainguard account team or [Chainguard Support](https://support.chainguard.dev/) if you run into issues migrating.
