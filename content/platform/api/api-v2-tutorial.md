---
aliases:
- /chainguard/api/api-v2-tutorial/
title: "Chainguard API v2 Tutorial"
linktitle: "API v2 Tutorial"
type: "article"
description: "Tutorial with examples showing how you can use the Chainguard API v2."
date: 2026-03-30T08:49:31+00:00
lastmod: 2026-08-07T13:02:36+00:00
draft: false
tags: ["Chainguard Console", "Procedural"]
images: []
toc: true
weight: 030
---

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
| **IAM** | Groups, Identities, Roles, RoleBindings, IdentityProviders, AccountAssociations, GroupInvites, Terms, ExternalGroupRoleMappings | List, Get, Create, Update, Delete |
| **Registry** | Repos, Tags, Images | List, Get, Create, Update, Delete |
| **Vulnerabilities** | Advisories | List, Get |
| **Ecosystems (Libraries)** | Artifacts | List, Get (read-only) |
| **Integrations (Advisory)** | SecurityAdvisory (documents, metadata, resolved-vuln reports) | List (read-only) |
| **Events** | Subscriptions | List, Get, Create, Delete |

All endpoints live under a versioned path per domain: `/iam/v2/`, `/registry/v2/`, `/vulnerabilities/v2/`, `/libraries/v2/`, `/advisory/v2/`, or `/events/v2/`.

The worked examples in this guide focus on IAM, Registry, and Vulnerabilities. The other domains follow the same request and response conventions.

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
- **gRPC** — all endpoints are also available via gRPC at the same host. Proto definitions are at `chainguard.dev/sdk/proto/chainguard/platform/`, and the Go SDK clients live under `chainguard.dev/sdk/proto/chainguard/platform/clients/v2`.

---

## 1. Your first v2 request

List the first 3 repos in your organization:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&page_size=3&order_by=name" | jq .
```

```json
{
  "repos": [
    {
      "uid": "d9e2f1a0.../06626efd8c6b3fb7",
      "name": "nginx",
      "createTime": "2026-01-28T12:54:21.189Z",
      "updateTime": "2026-01-28T12:54:21.189Z"
    },
    {
      "uid": "d9e2f1a0.../0ed18f0f929f4c60",
      "name": "python",
      "createTime": "2026-01-23T14:54:42.774Z",
      "updateTime": "2026-01-23T14:54:42.774Z"
    },
    {
      "uid": "d9e2f1a0.../12b4208b23740c37",
      "name": "static",
      "createTime": "2026-01-23T14:54:39.021Z",
      "updateTime": "2026-01-23T14:54:39.021Z"
    }
  ],
  "nextPageToken": "CqQBV3lK...",
  "totalCount": "12",
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

Use direct UID lookups when you already know the resource identifier — they are faster than a List call with an ID filter.

### Filter by name

Find a specific repo without knowing its UID:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&name=nginx" \
  | jq '[.repos[] | {uid, name, createTime}]'
```

```json
[
  {
    "uid": "d9e2f1a0.../06626efd8c6b3fb7",
    "name": "nginx",
    "createTime": "2026-01-28T12:54:21.189Z"
  }
]
```

Name filtering returns exact matches. Combine with `uidp.descendants_of` to scope the search to your organization.

---

## 2. Set up access for a new team

A common workflow: create a CI identity at your organization and bind a role to it.

> **Note:** Create identities under your root organization group (`$ORG_ID`) so they can reach the resources that live there, including your registry. An identity created under a subgroup is scoped to that subgroup and won't see your registry — so it can't pull images.

### Create an identity

```shell
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2/identities/$ORG_ID" \
  -d '{
    "name": "ci-bot",
    "description": "CI/CD pipeline identity",
    "claimMatch": {
      "issuer": "https://token.actions.githubusercontent.com",
      "subject": "repo:my-org@123456/my-repo@654321:ref:refs/heads/main"
    }
  }' | jq .
```

```json
{
  "uid": "d9e2f1a0.../f462d354ca32ca9f",
  "name": "ci-bot",
  "description": "CI/CD pipeline identity",
  "lastSeenTime": "2026-03-27T13:55:00.783Z",
  "createTime": "2026-03-27T13:55:00.785Z",
  "updateTime": "2026-03-27T13:55:00.785Z",
  "claimMatch": {
    "issuer": "https://token.actions.githubusercontent.com",
    "subject": "repo:my-org@123456/my-repo@654321:ref:refs/heads/main"
  }
}
```

{{< note >}}
The `subject` shown here uses GitHub's immutable format, which embeds the numeric owner ID (`123456`) and repository ID (`654321`). Match the exact subject your repository's token carries. For how to find these IDs and when the format applies, see [Create an Assumable Identity for a GitHub Actions Workflow](/platform/administration/assumable-ids/identity-examples/github-identity/#finding-your-repositorys-numeric-identifiers).
{{< /note >}}

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
  "$API/iam/v2/roleBindings/$ORG_ID" \
  -d "{\"identityUid\": \"$IDENTITY_UID\", \"roleUid\": \"$ROLE_UID\"}" | jq .
```

```json
{
  "uid": "d9e2f1a0.../9b822036a7075d75",
  "identity": {
    "uid": "d9e2f1a0.../f462d354ca32ca9f",
    "name": "ci-bot",
    "description": "CI/CD pipeline identity",
    "subject": "repo:my-org@123456/my-repo@654321:ref:refs/heads/main",
    "issuer": "https://token.actions.githubusercontent.com"
  },
  "group": {
    "uid": "d9e2f1a0...",
    "name": "my-org",
    "description": "Root organization group"
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
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&page_size=5" \
  | jq '{totalCount, repos: [.repos[].name], nextPageToken: .nextPageToken[:20]}'
```

```json
{
  "totalCount": "12",
  "repos": ["apko", "busybox", "go", "jdk", "nginx"],
  "nextPageToken": "CqQBV3lKbE16Z3dPVE0y"
}
```

Follow the cursor for the next page:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&page_size=5&page_token=CqQBV3lK..." \
  | jq '{repos: [.repos[].name]}'
```

```json
{
  "repos": ["node", "php", "postgres", "python", "redis"]
}
```

When `nextPageToken` is absent from the response, you have reached the last page.

### Server-side ordering

Sort by name:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name" \
  | jq '[.repos[].name]'
```

```json
["apko", "busybox", "go", "jdk", "nginx"]
```

Reverse the order:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name%20desc" \
  | jq '[.repos[].name]'
```

```json
["static", "ruby", "redis", "python", "postgres"]
```

Sort by creation time (newest first):

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&page_size=5&order_by=created_at%20desc" \
  | jq '[.repos[] | {name, createTime}]'
```

```json
[
  {"name": "redis", "createTime": "2026-02-14T09:11:05.488Z"},
  {"name": "postgres", "createTime": "2026-02-10T17:02:05.135Z"},
  {"name": "node", "createTime": "2026-02-03T11:48:04.814Z"},
  {"name": "nginx", "createTime": "2026-01-28T12:54:21.189Z"},
  {"name": "python", "createTime": "2026-01-23T14:54:42.774Z"}
]
```

Pagination and ordering combine: pages maintain sort order across cursors.

### Random-access with `skip`

Jump directly to page 3 (skip the first 10 results):

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/repos?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name&skip=10" \
  | jq '{skipped: .skipped, repos: [.repos[].name]}'
```

```json
{
  "skipped": 10,
  "repos": ["ruby", "static"]
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

## 4. Tags and end-of-life

Tags live under a repo. List them with the same patterns you used for repos, scoped to a single repo with `uidp.children_of`.

### List tags in a repo

Each tag carries its `digest` and a `deprecated` flag:

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

In v1, a dedicated `ListEolTags` call surfaced end-of-life tags. v2 has no separate end-of-life endpoint or server-side filter. Instead, each tag carries a `deprecated` boolean, which you filter on client-side:

```shell
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2/tags?uidp.children_of=$REPO_UID&page_size=200" \
  | jq '[.tags[] | select(.deprecated) | .name]'
```

> **Note:** Client-side filtering on `deprecated` is the intended approach in v2. A v2 equivalent of `ListEolTags` is on the backlog with no committed date; until it ships, the v1 `ListEolTags` endpoint remains available.

---

## 5. Querying vulnerabilities

The Vulnerabilities domain exposes advisory data. In v2 it covers advisories with List and Get.

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

The v1 `GetVulnReport` and `ListVulnCountReports` calls have no v2 equivalent today, and advisories are not a replacement — they serve a different, advisory-feed purpose. The `ListResolvedVulnsReports` endpoint under `/advisory/v2/` is also advisory-feed oriented, not a vulnerability-report replacement. If your integration reads vulnerability reports, continue using the v1 endpoints, which remain fully supported. v2 coverage arrives with the Vulnerabilities domain's migration.

---

## 6. Structured errors

API v2 returns structured error responses with machine-parseable codes and details.

### Validation error

```shell
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2/identities/$ORG_ID" \
  -d '{}' | jq .
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
  "$API/registry/v2/repos/$REPO_UID" \
  -d '{
    "description": "Updated description — only this field changes"
  }' | jq '{uid, name, description}'
```

```json
{
  "uid": "d9e2f1a0.../06626efd8c6b3fb7",
  "name": "nginx",
  "description": "Updated description — only this field changes"
}
```

The `name` field was not in the request body, so it's unchanged. In v1, updates required sending the entire resource — any omitted field would be reset to its zero value.

To be explicit about which fields to update, pass `updateMask`:

```shell
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/registry/v2/repos/$REPO_UID?updateMask=description" \
  -d '{
    "description": "Only this field is updated",
    "name": "this-is-ignored"
  }' | jq '{uid, name, description}'
```

```json
{
  "uid": "d9e2f1a0.../06626efd8c6b3fb7",
  "name": "nginx",
  "description": "Only this field is updated"
}
```

The `name` in the body is ignored because `updateMask` only includes `description`. This PATCH-with-field-mask pattern applies to every updatable resource.

---

## Migration from v1

v2 is additive — v1 endpoints remain available during a transition period, so you can migrate at your own pace. For the full field-by-field mapping and migration timeline, see [Migrating from API v1 to API v2](/platform/api/api-v2-migration/).

---

## Cleanup

Delete resources you created during this walkthrough:

```shell
# Delete in reverse order: role binding, then identity
# BINDING_UID is the uid value returned in the Bind a role response above
curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "$API/iam/v2/roleBindings/$BINDING_UID"
curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "$API/iam/v2/identities/$IDENTITY_UID"
```

Each DELETE returns an empty response body on success.
