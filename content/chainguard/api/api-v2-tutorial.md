<!--
Copyright 2026 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
-->

# Chainguard API v2 Beta Preview

The Chainguard API v2 introduces cursor-based pagination, server-side ordering, consistent resource patterns, and structured error responses across all endpoints.

This guide walks through the v2 API using real `curl` commands.

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
- **FieldMask updates** — partial updates via `update_mask` instead of sending the full resource

## Available endpoints

| Domain | Resources | Operations |
|--------|-----------|------------|
| **IAM** | Groups, Identities, Roles, RoleBindings, IdentityProviders, AccountAssociations, GroupInvites | List, Get, Create, Update, Delete |
| **Registry** | Repos, Tags | List, Get |
| **Vulnerabilities** | Advisories | List, Get |

All endpoints live under `/iam/v2beta1/`, `/registry/v2beta1/`, or `/vulnerabilities/v2beta1/`.

## Prerequisites

Get an API token:

```bash
export TOKEN=$(chainctl auth token)
export API=https://console-api.enforce.dev
```

All examples below use `$TOKEN` and `$API` for brevity.

---

## 1. Your first v2 request

List the first 3 groups in your organization:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups?uidp.descendants_of=$ORG_ID&page_size=3&order_by=name" | jq .
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

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups/$GROUP_UID" | jq '{uid, name, description}'
```

```json
{
  "uid": "d9e2f1a0.../04b8bc5bcb561945",
  "name": "engineering",
  "description": "Engineering department"
}
```

### Filter by name

Find a specific group without knowing its UID:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups?uidp.descendants_of=$ORG_ID&name=platform" \
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

```bash
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2beta1/groups/$ORG_ID" \
  -d '{"name": "backend-team", "description": "Backend engineering team"}' | jq .
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

Note: the parent group goes in the URL path. The request body contains only the resource fields.

### Create an identity

```bash
GROUP_UID="<uid from previous step>"

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2beta1/identities/$GROUP_UID" \
  -d '{
    "name": "ci-bot",
    "description": "CI/CD pipeline identity",
    "claimMatch": {
      "issuer": "https://token.actions.githubusercontent.com",
      "subject": "repo:my-org/my-repo:ref:refs/heads/main"
    }
  }' | jq .
```

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

### Bind a role

First, find the viewer role:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/roles?name=viewer" | jq '.roles[0] | {uid, name, description}'
```

```json
{
  "uid": "63921b2c44617e3f2603851537be0123af4a57d7",
  "name": "viewer",
  "description": "Viewer Role (built-in)"
}
```

Then bind it:

```bash
ROLE_UID="63921b2c44617e3f2603851537be0123af4a57d7"
IDENTITY_UID="<uid from identity creation>"

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2beta1/roleBindings/$GROUP_UID" \
  -d "{\"identityUid\": \"$IDENTITY_UID\", \"roleUid\": \"$ROLE_UID\"}" | jq .
```

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

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups?uidp.descendants_of=$ORG_ID&page_size=5" \
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

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups?uidp.descendants_of=$ORG_ID&page_size=5&page_token=CqQBV3lK..." \
  | jq '{groups: [.groups[].name]}'
```

```json
{
  "groups": ["incident-response", "platform", "production", "registry-ops", "root"]
}
```

### Server-side ordering

Sort by name:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name" \
  | jq '[.groups[].name]'
```

```json
["api", "base-images", "ci-cd", "containers", "engineering"]
```

Reverse the order:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name%20desc" \
  | jq '[.groups[].name]'
```

```json
["vuln-scanning", "staging", "security", "sandbox", "root"]
```

Sort by creation time (newest first):

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups?uidp.descendants_of=$ORG_ID&page_size=5&order_by=created_at%20desc" \
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

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/iam/v2beta1/groups?uidp.descendants_of=$ORG_ID&page_size=5&order_by=name&skip=10" \
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
|-----------|-------------|
| `page_size` | Number of results per page (default 50, max 200) |
| `page_token` | Opaque cursor from previous response's `nextPageToken` |
| `order_by` | Sort field and direction, e.g. `name`, `created_at desc` |
| `skip` | Number of results to skip (for random-access / UI page jumping) |

---

## 4. Querying the registry

List repos scoped to your organization:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API/registry/v2beta1/repos?uidp.descendants_of=$ORG_ID&page_size=3" \
  | jq '[.repos[] | {uid, name, createTime}]'
```

```json
[
  {"uid": "d9e2f1a0.../06626efd8c6b3fb7", "name": "nginx", "createTime": "2026-01-28T12:54:21.189Z"},
  {"uid": "d9e2f1a0.../0ed18f0f929f4c60", "name": "python", "createTime": "2026-01-23T14:54:42.774Z"},
  {"uid": "d9e2f1a0.../12b4208b23740c37", "name": "static", "createTime": "2026-01-23T14:54:39.021Z"}
]
```

Same pagination and ordering parameters work on all List endpoints.

---

## 5. Structured errors

v2 returns structured error responses with machine-parseable codes and details.

### Validation error

```bash
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2beta1/groups/$ORG_ID" \
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

### Precondition failure

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

## 6. Partial updates with FieldMask

Update specific fields without sending the full resource. Only the fields listed in `updateMask` are changed:

```bash
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2beta1/groups/$GROUP_UID" \
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

```bash
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/iam/v2beta1/groups/$GROUP_UID?updateMask=description" \
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

---

## Good to know

- **Page tokens expire after 3 days** ([AIP-158](https://google.aip.dev/158)). If a token expires, the query restarts from the beginning — no error is returned.
- **Rate limits** are not enforced during beta. They will be introduced at GA.
- **gRPC** — all endpoints are also available via gRPC at the same host. Proto definitions are at `chainguard.dev/sdk/proto/chainguard/platform/`.

---

## Migration from v1

v2 is additive — v1 endpoints remain available. You can migrate at your own pace:

- Replace `/iam/v1/` with `/iam/v2beta1/` in your API calls
- Update field names: `id` → `uid`, `createdAt` → `createTime`, `updatedAt` → `updateTime`
- Add pagination handling for List endpoints (or set `page_size` high for small result sets)
- v1 will have a deprecation window after v2 reaches GA

---

## Cleanup

Delete resources you created during this walkthrough:

```bash
# Delete in reverse order: role binding, identity, group
curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "$API/iam/v2beta1/roleBindings/$BINDING_UID"
curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "$API/iam/v2beta1/identities/$IDENTITY_UID"
curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "$API/iam/v2beta1/groups/$GROUP_UID"
```