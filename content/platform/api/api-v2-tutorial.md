---
aliases:
- /chainguard/api/api-v2-tutorial/
title: "Chainguard API v2 Tutorial"
linktitle: "API v2 Tutorial"
type: "article"
description: "Tutorial with examples showing how you can use the Chainguard API v2."
date: 2026-03-30T08:49:31+00:00
lastmod: 2026-07-20T00:00:00+00:00
draft: false
tags: ["Chainguard Console", "Procedural"]
images: []
toc: true
weight: 030
---

> **Draft status:** This page has several items marked `CONFIRM WITH ENGINEERING`. Do not publish externally until those are resolved.

The v2 API is now Generally Available (GA) and introduces cursor-based pagination, server-side ordering, consistent resource patterns, and structured error responses across all endpoints.

This guide walks through the v2 API using real `curl` commands. If you're migrating an existing v1 or beta (`v2beta1`) integration, see [Migrating from API v1 to API v2](/platform/api/api-v2-migration/) instead.

> **Note:** The example output in this guide was captured from a development environment. Your organization's resource names, UIDs, timestamps, and counts will differ. The response structure and field names are the same across all environments.

## What's the same

- **Authentication** — same OIDC token model as v1
- **Authorization** — same identity-based access control
- **Scoping** — same `uidp.descendants_of` / `uidp.children_of` hierarchy filters

## What's new in v2

- **Cursor-based pagination** with `page_size`, `page_token`, `total_count`
- **Server-side ordering** with `order_by` (ascending/descending on any sortable field)
- **Random-access pagination** with `skip` for UI page jumping
- **Structured errors** with typed detail payloads (AIP-193)
- **Consistent resource patterns** — every resource has `uid`, `createTime`, `updateTime`
- **Hydrated references** — role binding responses include full identity, group, and role objects
- **FieldMask updates** — partial updates via `updateMask` instead of sending the full resource

## Available endpoints

| Domain | Resources | Operations |
| -------- | ----------- | ------------ |
| **IAM** | Groups, Identities, Roles, RoleBindings, IdentityProviders, AccountAssociations, GroupInvites | List, Get, Create, Update, Delete |
| **Registry** | Repos, Tags | List, Get |
| **Vulnerabilities** | Advisories | List, Get |
| **Ecosystems (Libraries)** | — | — |
| **Integrations (Advisory)** | — | — |

All endpoints live under a versioned path per domain: `/iam/v2/`, `/registry/v2/`, `/vulnerabilities/v2/`, `/libraries/v2/`, or `/advisory/v2/`.

> **CONFIRM WITH ENGINEERING:** Ecosystems and Integrations are new domains at GA (beta only covered IAM, Registry, and Vulnerabilities). Get the specific resource names and supported operations for these two domains before publishing — the worked examples in this guide only cover the three domains available during beta.

## Prerequisites

Get an API token and set your organization ID:

```shell
export TOKEN=$(chainctl auth token)
export API=https://console-api.enforce.dev
# ORG_ID is the UID of your root organization group
export ORG_ID=YOUR_ORG_ID
```

The following examples use `$TOKEN`, `$API`, and `$ORG_ID` for brevity.

## Operational notes

Keep the following in mind as you work through this guide.

- **Page tokens expire after 3 days** ([AIP-158](https://google.aip.dev/158)). If a token expires, the query restarts from the beginning — no error is returned.
- **Rate limits** are enforced starting at GA.
- **gRPC** — all endpoints are also available via gRPC at the same host. Proto definitions are at `chainguard.dev/sdk/proto/chainguard/platform/`.

> **CONFIRM WITH ENGINEERING:** specific rate limits and response headers, and whether the Go SDK client library moves from `chainguard.dev/sdk/proto/platform/clients/v2beta1` to a `v2` path at GA. Don't publish this section externally until both are confirmed.

---

## 1. Your first v2 request

List the first 3 groups in your organization:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=3&order_by=name" | jq .
```

```json
{
  "groups": [
    {
      "uid": "d9e2f1a0.../9f1c889071ceb6bf",
      "name": "api",
      "description": "API services and backend",
      "resourceLimits": {},
      "verified": false,
      "createTime": "2026-03-27T13:20:03.456Z",
      "updateTime": "2026-03-27T13:20:03.456Z"
    },
    {
      "uid": "d9e2f1a0.../822b6e789e77ebb9",
      "name": "base-images",
      "description": "Base image maintenance",
      "resourceLimits": {},
      "verified": false,
      "createTime": "2026-03-27T13:20:03.123Z",
      "updateTime": "2026-03-27T13:20:03.123Z"
    },
    {
      "uid": "d9e2f1a0.../251da0851a321620",
      "name": "ci-cd",
      "description": "CI/CD pipelines and automation",
      "resourceLimits": {},
      "verified": false,
      "createTime": "2026-03-27T13:20:03.789Z",
      "updateTime": "2026-03-27T13:20:03.789Z"
    }
  ],
  "nextPageToken": "CqQBV3lK...",
  "totalCount": "14",
  "skipped": 0
}
```

Every v2 response follows the same shape:

- **`uid`** — unique resource identifier (replaces `id` in v1)
- **`createTime` / `updateTime`** — timestamps on every resource
- **`nextPageToken`** — cursor for the next page (empty when no more results)
- **`totalCount`** — total matching results across all pages

### Get a single resource

New in v2: fetch a resource directly by UID. In v1, this required a List call with an ID filter.

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups/$GROUP_UID" | jq '{uid, name, description}'
```

```json
{
  "uid": "d9e2f1a0.../04b8bc5bcb561945",
  "name": "engineering",
  "description": "Engineering department"
}
```

Use direct UID lookups when you already know the resource identifier — they are faster than a List call with an ID filter.

### Filter by name

Find a specific group without knowing its UID:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&name=platform" \
  | jq '[.groups[] | {uid, name, description}]'
```

```json
[
  {
    "uid": "d9e2f1a0.../04b8bc5bcb561945/3af5754ef8e5dd4d",
    "name": "platform",
    "description": "Platform team — infrastructure and developer tools"
  }
]
```

Name filtering returns exact matches. Combine with `uidp.descendants_of` to scope the search to your organization.

---

## 2. Set up access for a new team

A real workflow: create an org folder, add an identity, and bind a role.

### Create a group

```shell
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2/groups" \
  -d '{"parent": "'"$ORG_ID"'", "group": {"name": "backend-team", "description": "Backend engineering team"}}' | jq .
```

```json
{
  "uid": "d9e2f1a0.../fb139588d99c8efe",
  "name": "backend-team",
  "description": "Backend engineering team",
  "resourceLimits": {},
  "verified": false,
  "createTime": "2026-03-27T13:55:00.423Z",
  "updateTime": "2026-03-27T13:55:00.423Z"
}
```

> **Note:** The parent group goes in the request body, not the URL path — a change from beta. See [Migrating from API v1 to API v2](/platform/api/api-v2-migration/#step-3-move-create-calls-to-parent-in-body) for details.
>
> **CONFIRM WITH ENGINEERING:** this request body shape, including the `"group"` wrapper field name, is illustrative. Confirm the exact schema before publishing.

### Create an identity

```shell
# GROUP_UID is the uid value returned in the Create a group response above
export GROUP_UID=YOUR_GROUP_UID

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2/identities" \
  -d '{
    "parent": "'"$GROUP_UID"'",
    "identity": {
      "name": "ci-bot",
      "description": "CI/CD pipeline identity",
      "claimMatch": {
        "issuer": "https://token.actions.githubusercontent.com",
        "subject": "repo:my-org/my-repo:ref:refs/heads/main"
      }
    }
  }' | jq .
```

> **CONFIRM WITH ENGINEERING:** this request body shape, including the `"identity"` wrapper field name, is illustrative. Confirm the exact schema before publishing.

```json
{
  "uid": "d9e2f1a0.../fb139588d99c8efe/f462d354ca32ca9f",
  "name": "ci-bot",
  "description": "CI/CD pipeline identity",
  "lastSeenTime": "2026-03-27T13:55:00.783Z",
  "createTime": "2026-03-27T13:55:00.785Z",
  "updateTime": "2026-03-27T13:55:00.785Z",
  "claimMatch": {
    "issuer": "https://token.actions.githubusercontent.com",
    "subject": "repo:my-org/my-repo:ref:refs/heads/main"
  }
}
```

Note the identity `uid` in the response — you will use it in the next step when binding a role.

### Bind a role

First, find the viewer role:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/roles" | jq '.roles[] | select(.name == "viewer") | {uid, name, description}'
```

```json
{
  "uid": "63921b2c44617e3f2603851537be0123af4a57d7",
  "name": "viewer",
  "description": "Viewer Role (built-in)"
}
```

Then bind it:

```shell
# ROLE_UID is the uid of the viewer role, retrieved above
ROLE_UID="63921b2c44617e3f2603851537be0123af4a57d7"
# IDENTITY_UID is the uid value returned in the Create an identity response above
export IDENTITY_UID=YOUR_IDENTITY_UID

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2/roleBindings" \
  -d "{\"parent\": \"$GROUP_UID\", \"roleBinding\": {\"identityUid\": \"$IDENTITY_UID\", \"roleUid\": \"$ROLE_UID\"}}" | jq .
```

> **CONFIRM WITH ENGINEERING:** this request body shape, including the `"roleBinding"` wrapper field name, is illustrative. Confirm the exact schema before publishing.

```json
{
  "uid": "d9e2f1a0.../fb139588.../9b822036a7075d75",
  "identity": {
    "uid": "d9e2f1a0.../fb139588.../f462d354ca32ca9f",
    "name": "ci-bot",
    "description": "CI/CD pipeline identity",
    "subject": "repo:my-org/my-repo:ref:refs/heads/main",
    "issuer": "https://token.actions.githubusercontent.com"
  },
  "group": {
    "uid": "d9e2f1a0.../fb139588d99c8efe",
    "name": "backend-team",
    "description": "Backend engineering team"
  },
  "role": {
    "uid": "63921b2c44617e3f2603851537be0123af4a57d7",
    "name": "viewer",
    "description": "Viewer Role (built-in)"
  },
  "createTime": "2026-03-27T13:55:01.475Z"
}
```

The response includes fully hydrated identity, group, and role objects — no need for follow-up lookups.

---

## 3. Pagination

Every List endpoint supports cursor-based pagination with consistent parameters.

### Basic pagination

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=5" \
  | jq '{totalCount, groups: [.groups[].name], nextPageToken: .nextPageToken[:20]}'
```

```json
{
  "totalCount": "14",
  "groups": ["api", "base-images", "ci-cd", "containers", "engineering"],
  "nextPageToken": "CqQBV3lKbE16Z3dPVE0y"
}
```

Follow the cursor for the next page:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=5&page_token=CqQBV3lK..." \
  | jq '{groups: [.groups[].name]}'
```

```json
{
  "groups": ["incident-response", "platform", "production", "registry-ops", "root"]
}
```

When `nextPageToken` is absent from the response, you have reached the last page.

### Server-side ordering

Sort by name:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name" \
  | jq '[.groups[].name]'
```

```json
["api", "base-images", "ci-cd", "containers", "engineering"]
```

Reverse the order:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name%20desc" \
  | jq '[.groups[].name]'
```

```json
["vuln-scanning", "staging", "security", "sandbox", "root"]
```

Sort by creation time (newest first):

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=5&order_by=created_at%20desc" \
  | jq '[.groups[] | {name, createTime}]'
```

```json
[
  {"name": "sandbox", "createTime": "2026-03-27T13:20:05.488Z"},
  {"name": "production", "createTime": "2026-03-27T13:20:05.135Z"},
  {"name": "staging", "createTime": "2026-03-27T13:20:04.814Z"},
  {"name": "incident-response", "createTime": "2026-03-27T13:20:04.257Z"},
  {"name": "vuln-scanning", "createTime": "2026-03-27T13:20:03.915Z"}
]
```

Pagination and ordering combine: pages maintain sort order across cursors.

### Random-access with `skip`

Jump directly to page 3 (skip the first 10 results):

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2/groups?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name&skip=10" \
  | jq '{skipped: .skipped, groups: [.groups[].name]}'
```

```json
{
  "skipped": 10,
  "groups": ["sandbox", "security", "staging", "vuln-scanning"]
}
```

The `skipped` field in the response confirms how many results were skipped, useful for building UI page controls.

### Pagination parameters

| Parameter | Description |
| ----------- | ------------- |
| `page_size` | Number of results per page (default 50, max 200) |
| `page_token` | Opaque cursor from previous response's `nextPageToken` |
| `order_by` | Sort field and direction, for example `name` or `created_at desc` |
| `skip` | Number of results to skip (for random-access / UI page jumping) |

---

## 4. Querying the registry

Registry endpoints follow the same List, Get, and pagination patterns as the IAM examples earlier, applied to repos and tags. If your integration reads image metadata — listing repos, walking tags, or checking end-of-life status — these are the endpoints you call most.

### List repos

List repos scoped to your organization:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&page_size=3" \
  | jq '[.repos[] | {uid, name, createTime}]'
```

```json
[
  {"uid": "d9e2f1a0.../06626efd8c6b3fb7", "name": "nginx", "createTime": "2026-01-28T12:54:21.189Z"},
  {"uid": "d9e2f1a0.../0ed18f0f929f4c60", "name": "python", "createTime": "2026-01-23T14:54:42.774Z"},
  {"uid": "d9e2f1a0.../12b4208b23740c37", "name": "static", "createTime": "2026-01-23T14:54:39.021Z"}
]
```

The same pagination and ordering parameters work on every List endpoint.

### Get a single repo

Fetch one repo directly by UID, the same way you fetch a group:

```shell
# REPO_UID is a uid value from the List repos response above
export REPO_UID=YOUR_REPO_UID

curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos/$REPO_UID" | jq '{uid, name, createTime}'
```

```json
{
  "uid": "d9e2f1a0.../06626efd8c6b3fb7",
  "name": "nginx",
  "createTime": "2026-01-28T12:54:21.189Z"
}
```

### List tags in a repo

Scope a tag listing to a single repo with `uidp.children_of`. Each tag carries its `digest` and a `deprecated` flag:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/tags?uidp.children_of=$REPO_UID&page_size=3" \
  | jq '[.tags[] | {name, digest, deprecated, updateTime}]'
```

```json
[
  {"name": "latest", "digest": "sha256:6b3f...", "deprecated": false, "updateTime": "2026-07-14T09:12:44.501Z"},
  {"name": "1.27", "digest": "sha256:8c1a...", "deprecated": false, "updateTime": "2026-07-14T09:12:44.502Z"},
  {"name": "1.26", "digest": "sha256:a90d...", "deprecated": true, "updateTime": "2026-05-02T18:30:10.114Z"}
]
```

### Check for deprecated tags

In v1, a dedicated `ListEolTags` call surfaced end-of-life tags. v2beta1 has no separate end-of-life endpoint or server-side filter. Instead, each tag carries a `deprecated` boolean, which you filter on client-side:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/tags?uidp.children_of=$REPO_UID&page_size=200" \
  | jq '[.tags[] | select(.deprecated) | .name]'
```

> **CONFIRM WITH ENGINEERING:** v2beta1 exposes tag deprecation only as a per-tag `deprecated` field, with no server-side end-of-life filter. Confirm whether GA adds a dedicated filter or endpoint, since v1's `ListEolTags` was a common direct-API call.

---

## 5. Querying vulnerabilities

The Vulnerabilities domain exposes advisory data. In v2beta1 it covers advisories with List and Get.

### List advisories

Advisories are scoped and paginated like every other List endpoint, with extra filters such as `artifactNames` and `advisoryIds`:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/vulnerabilities/v2/advisories?uidp.descendants_of=$ORG_ID&page_size=3" \
  | jq '[.advisories[] | {uid, advisoryId, artifactName, updateTime}]'
```

```json
[
  {"uid": "d9e2f1a0.../3b1c", "advisoryId": "CGA-abcd-1234-wxyz", "artifactName": "nginx", "updateTime": "2026-07-18T21:04:11.220Z"},
  {"uid": "d9e2f1a0.../7f2a", "advisoryId": "CGA-efgh-5678-stuv", "artifactName": "python", "updateTime": "2026-07-18T21:04:11.221Z"},
  {"uid": "d9e2f1a0.../a1b2", "advisoryId": "CGA-ijkl-9012-mnop", "artifactName": "openssl", "updateTime": "2026-07-18T21:04:11.222Z"}
]
```

Fetch a single advisory by UID at `/vulnerabilities/v2/advisories/{uid}`.

### Vulnerability reports

> **CONFIRM WITH ENGINEERING:** the v1 `GetVulnReport` and `ListVulnCountReports` calls — used heavily by direct HTTP integrations — have no equivalent in the v2beta1 spec, which exposes only advisories. Confirm whether GA adds vulnerability-report endpoints, or whether advisory data is meant to replace them. This is a real migration gap for the CI/CD audience that reads scan results programmatically.

---

## 6. Structured errors

API v2 returns structured error responses with machine-parseable codes and details.

### Validation error

```shell
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2/groups" \
  -d '{"parent": "'"$ORG_ID"'", "group": {}}' | jq .
```

```json
{
  "code": 3,
  "message": "Invalid argument: name: name must match \"^[a-z0-9 ._-]{1,}$\"",
  "details": [
    {
      "@type": "type.googleapis.com/google.rpc.ErrorInfo",
      "reason": "INVALID_ARGUMENT",
      "domain": "iam.chainguard.dev"
    },
    {
      "@type": "type.googleapis.com/google.rpc.BadRequest",
      "fieldViolations": [
        {
          "field": "name",
          "description": "name must match \"^[a-z0-9 ._-]{1,}$\""
        }
      ]
    }
  ]
}
```

The `fieldViolations` array identifies exactly which fields failed validation and why.

### Precondition failure

Attempting to delete a group that still contains child resources returns a precondition failure:

```json
{
  "code": 9,
  "message": "Precondition failed: cannot delete group with child repos",
  "details": [
    {
      "@type": "type.googleapis.com/google.rpc.ErrorInfo",
      "reason": "FAILED_PRECONDITION",
      "domain": "iam.chainguard.dev"
    },
    {
      "@type": "type.googleapis.com/google.rpc.PreconditionFailure",
      "violations": [
        {
          "type": "RESOURCE_NOT_EMPTY",
          "description": "cannot delete group with child repos"
        }
      ]
    }
  ]
}
```

Error responses follow [Google AIP-193](https://google.aip.dev/193) with typed detail payloads you can switch on programmatically.

---

## 7. Partial updates with FieldMask

Update specific fields without sending the full resource. Only the fields listed in `updateMask` are changed:

```shell
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2/groups/$GROUP_UID" \
  -d '{
    "description": "Updated description — only this field changes"
  }' | jq '{uid, name, description}'
```

```json
{
  "uid": "d9e2f1a0.../fb139588d99c8efe",
  "name": "backend-team",
  "description": "Updated description — only this field changes"
}
```

The `name` field was not in the request body, so it's unchanged. In v1, updates required sending the entire resource — any omitted field would be reset to its zero value.

To be explicit about which fields to update, pass `updateMask`:

```shell
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2/groups/$GROUP_UID?updateMask=description" \
  -d '{
    "description": "Only this field is updated",
    "name": "this-is-ignored"
  }' | jq '{uid, name, description}'
```

```json
{
  "uid": "d9e2f1a0.../fb139588d99c8efe",
  "name": "backend-team",
  "description": "Only this field is updated"
}
```

The `name` in the body is ignored because `updateMask` only includes `description`.

### Update a repo

The same PATCH-with-field-mask pattern applies to every updatable resource. Repository updates are a common case to migrate from v1, where changing one field meant sending the full resource:

```shell
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/registry/v2/repos/$REPO_UID?updateMask=description" \
  -d '{"description": "Updated repo description"}' | jq '{uid, name, description}'
```

```json
{
  "uid": "d9e2f1a0.../06626efd8c6b3fb7",
  "name": "nginx",
  "description": "Updated repo description"
}
```

> **Note:** The repo update path (`/registry/v2/repos/{repo.uid}`) and request body are confirmed against the published v2beta1 spec, where `name` and `description` are writable. As with the group example, `updateMask` is accepted by the live API but isn't restated in the spec, so reconfirm it holds at GA.

---

## Migration from v1

v2 is additive — v1 endpoints remain available during a transition period, so you can migrate at your own pace. For the full field-by-field mapping and migration timeline, see [Migrating from API v1 to API v2](/platform/api/api-v2-migration/).

---

## Cleanup

Delete resources you created during this walkthrough:

```shell
# Delete in reverse order: role binding, identity, group
# BINDING_UID is the uid value returned in the Bind a role response above
curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "$API/iam/v2/roleBindings/$BINDING_UID"
curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "$API/iam/v2/identities/$IDENTITY_UID"
curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "$API/iam/v2/groups/$GROUP_UID"
```

Each DELETE returns an empty response body on success.
