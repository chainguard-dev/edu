---
title: "cg-api: the Chainguard platform API MCP server"
linktitle: "cg-api"
description: "Connect an MCP client to cg-api to query and manage Chainguard organizations, IAM, registry metadata, and security advisories through the platform API."
type: "article"
date: 2026-09-16T00:00:00+00:00
lastmod: 2026-09-16T00:00:00+00:00
draft: false
tags: ["MCP", "Platform"]
images: []
menu:
  docs:
    parent: "mcp-servers"
    identifier: "cg-api"
toc: true
weight: 020
---

`cg-api` exposes the Chainguard platform API — the same API behind `chainctl` and the Chainguard Console — to an MCP client. Through it, a client can resolve which organizations and folders you belong to, list the image repositories and tags your account holds, inspect roles and role bindings, read security advisories, and manage identity providers and cloud account associations. It is the broadest of Chainguard's four product-data MCP servers, and the only one that reaches organization and IAM data.

The server uses the Streamable HTTP transport, at this endpoint:

```
https://console-api.enforce.dev/mcp
```

{{< alert context="danger" >}}
**`cg-api` is not read-only.** Unlike `cg-oci`, `cg-apk`, and `cg-versions`, this server exposes tools that create, update, and delete real platform resources — including `iam_groups_delete`, `registry_repos_delete`, `iam_role_bindings_delete`, and `iam_identity_providers_update`. An MCP client that decides to "clean up" a group or repository can do so, and the platform API has no undo.

Before connecting it, consider:

- Keep your client's tool-approval prompts on for this server rather than granting its tools blanket permission.
- Prefer `--scope local` over `--scope user` so the server is present only in the projects where you need it.
- Connect under a token whose capabilities match what you actually want an AI tool to do. The server filters its tool list by capability, so a read-only token never advertises the write tools at all. Narrowing requires the [`chainctl` authentication path](#narrow-what-an-ai-tool-can-do); the browser OAuth flow issues a token carrying your full permissions.
{{< /alert >}}

## Prerequisites

- An MCP-compatible client such as Claude Code, Claude Desktop, or Cursor
- A [Chainguard account](https://console.chainguard.dev/) and an organization
- [`chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) installed, if you plan to narrow your token's capabilities or use the headless authentication path

## Connect to the server

### Claude Code

Add the server with `claude mcp add`, using the HTTP transport:

```shell
claude mcp add --transport http cg-api https://console-api.enforce.dev/mcp
```

Scope options are `local` (the default — only you, in the current directory), `project` (writes a shared `.mcp.json` at the repository root, checked in for teammates), and `user` (only you, across every project). Given the write tools this server exposes, the default `local` scope is the safer choice; specify `--scope user` only if you want platform administration available in every directory.

The server is added unauthenticated. To complete OAuth, start a session and run the `/mcp` command:

```Prompt
/mcp
```

Select **cg-api**, choose **Authenticate**, and approve the connection in the browser window that opens. Check the status any time with:

```shell
claude mcp list
```

```output
cg-api: https://console-api.enforce.dev/mcp (HTTP) - ✓ Connected
```

### Cursor

Cursor supports HTTP transport natively. Add the server to your MCP configuration:

```json
{
  "mcpServers": {
    "cg-api": {
      "url": "https://console-api.enforce.dev/mcp"
    }
  }
}
```

Restart Cursor, then connect the server from **Tools & MCPs** in settings and complete the browser sign-in.

### Claude Desktop

Claude Desktop reads MCP servers from a JSON file but does not yet support HTTP transport directly. Use [`mcp-remote`](https://github.com/geelen/mcp-remote) to bridge to the hosted server:

```json
{
  "mcpServers": {
    "cg-api": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://console-api.enforce.dev/mcp"
      ]
    }
  }
}
```

The configuration file lives at:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

`npx` downloads and runs `mcp-remote` on demand, so you need Node.js installed on the host. Restart Claude Desktop after saving the file.

### Other MCP clients

Any client that supports a remote Streamable HTTP MCP server with OAuth can connect to the same endpoint. Point it at `https://console-api.enforce.dev/mcp` and complete the browser sign-in when prompted.

## Authentication

Authentication is OAuth 2.0 against the Chainguard issuer, and every call runs with your own platform permissions. The server grants no access beyond what your role already allows.

{{< alert context="warning" >}}
**Each Chainguard MCP server requires its own login.** Authenticating to `cg-api` does not authenticate you to `cg-oci`, `cg-apk`, or `cg-versions`. Connecting all four means completing the browser sign-in four times. As of this writing, there is no unified sign-in across the four servers.
{{< /alert >}}

On a remote or headless workstation, you can supply a token from `chainctl` instead of completing the browser flow. Refer to [Authenticate with chainctl instead of a browser](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser) for the full recipe; `cg-api`'s audience is `https://console-api.enforce.dev/mcp`.

### The tool list depends on your token

`cg-api` filters its advertised tools against the capabilities of the token you connected with. Two people connected to the same endpoint can see different tool lists, and a missing tool means your token can't call it, not that the server doesn't offer it. Run `/mcp` in Claude Code to see what your own token receives.

This makes capability narrowing a useful safety control. In a session that uses a token requested without write capabilities, the destructive tools don't appear at all.

### Narrow what an AI tool can do

`chainctl auth token` accepts two flags that reduce a token's reach:

- `--capabilities` requests a token narrowed to the capabilities you name. List the ones a token currently carries with `chainctl auth token capabilities`.
- `--scope` reduces a token's scope to the groups you name, which confines it to one organization or folder.

The browser OAuth flow offers no equivalent, so narrowing means authenticating through `chainctl`. Add the flags to the `chainctl auth token` call inside the headers helper described in the [overview](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser), and every connection that helper opens inherits the narrowed token. A helper that grants read access to one organization and nothing else produces a `cg-api` session with no write tools in it.

## Common parameters

Most tools share the following conventions.

### UIDPs

Platform resources are addressed by **UIDP**, a slash-delimited path that encodes the resource's position in the group hierarchy. A root organization has a bare UIDP such as `0ac7ff905850c35723a7f376e10d007c958c45c8`; a folder beneath it appends a segment, as in `0ac7ff905850c35723a7f376e10d007c958c45c8/014da1131bcc7f51`. Every `*_get` and `*_delete` tool takes a `uid` of this shape, and you normally obtain it from a `*_list` call rather than constructing it.

### The uidp filter

`list` tools accept a `uidp` object that scopes results to part of the hierarchy:

| Field | Type | Description |
| ----- | ----- | ----- |
| `ids` | array of strings | Restrict to these exact UIDPs |
| `children_of` | string | Direct children of this UIDP |
| `descendants_of` | string | Every descendant of this UIDP, at any depth |
| `ancestors_of` | string | The chain of groups above this UIDP |
| `in_root` | boolean | Restrict to root-level groups |

### Pagination

Every `list` tool returns at most 200 results per page and 50 by default; a larger `page_size` is reduced rather than rejected. Continue by passing the response's `nextPageToken` as the next call's `page_token`. Note the casing difference: the parameter is snake_case, and the response field is camelCase. Responses also carry `totalCount`, so an MCP client can report a total without paging through the results.

Most `list` tools additionally accept `order_by` and `skip`.

## Tool reference

The server advertises 60 tools across 16 services, grouped by the service they belong to. Tools that change state are marked **write**.

Run `api_list` to enumerate the services your own token reaches, and `api_read` to see an individual RPC's metadata.

### API discovery

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `api_list` | `path` | Services at the root, or the RPCs under a service such as `iam.v2beta1.GroupsService` |
| `api_read` | `path` | The metadata payload for one RPC, such as `iam.v2beta1.GroupsService/ListGroups` |
| `api_callers` | `type` | The RPCs you can call that use a given proto message type |

*Example prompt:* "What parts of the Chainguard API can I reach?"

### Organizations and folders

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `iam_groups_list` | `name`, `uidp`, `order_by`, `page_size`, `page_token`, `skip` | Groups you can access |
| `iam_groups_get` | `uid` | One group |
| `iam_groups_create` — **write** | group fields, parent | The created group |
| `iam_groups_update` — **write** | group fields | The updated group |
| `iam_groups_delete` — **write** | `uid` | Deletes a group; fails if it has child resources |

*Example prompt:* "What Chainguard organizations am I a member of?"

### Roles and role bindings

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `iam_roles_list` | `name`, `uidp`, `order_by`, `page_size`, `page_token`, `skip` | Roles available to you |
| `iam_roles_get` | `uid` | One role |
| `iam_roles_create` / `iam_roles_update` / `iam_roles_delete` — **write** | role fields, `uid` | Manage custom roles |
| `iam_role_bindings_get` | `uid` | One role binding |
| `iam_role_bindings_create` / `iam_role_bindings_batch_create` / `iam_role_bindings_update` / `iam_role_bindings_delete` — **write** | binding fields, `uid` | Manage who holds which role where |

*Example prompt:* "What roles exist in my organization?"

### Identities and identity providers

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `iam_identities_get` | `uid` | One identity |
| `iam_identities_create` / `iam_identities_update` / `iam_identities_delete` — **write** | identity fields, `uid` | Manage assumable identities |
| `iam_identity_providers_list` | `name`, `uidp`, pagination | Configured identity providers |
| `iam_identity_providers_get` | `uid` | One identity provider |
| `iam_identity_providers_create` / `iam_identity_providers_update` / `iam_identity_providers_delete` — **write** | provider fields, `uid` | Manage custom IdP configuration |
| `iam_external_group_role_mappings_list` | `uidp`, pagination | Mappings from IdP groups to Chainguard roles |
| `iam_external_group_role_mappings_get` | `uid` | One mapping |
| `iam_external_group_role_mappings_create` / `iam_external_group_role_mappings_delete` / `iam_external_group_role_mappings_batch_delete` — **write** | mapping fields, `uid` | Manage group-to-role mappings |

*Example prompt:* "Which identity providers are configured for my org?"

### Invitations and terms

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `iam_group_invites_get` | `uid` | One invitation |
| `iam_group_invites_create` / `iam_group_invites_delete` — **write** | invite fields, `uid` | Manage organization invitations |
| `iam_terms_accept` — **write** | terms fields | Records acceptance of a product's terms |

### Cloud account associations

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `iam_account_associations_list` | `uidp`, pagination | Configured cloud account associations |
| `iam_account_associations_get` | `uid` | One association |
| `iam_account_associations_check` | `uid`, `provider_type` | Verifies an association by performing a live credential exchange against Google, Amazon, or Azure |
| `iam_account_associations_create` / `iam_account_associations_update` / `iam_account_associations_delete` — **write** | association fields, `uid` | Manage associations |

*Example prompt:* "Is my AWS account association working?"

### Event subscriptions

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `iam_subscriptions_list` | `uidp`, pagination | Event subscriptions you can access |
| `iam_subscriptions_get` | `uid` | One subscription |
| `iam_subscriptions_create` / `iam_subscriptions_delete` — **write** | subscription fields, `uid` | Manage CloudEvents subscriptions |

Despite the `iam_` prefix, these tools address the events service rather than IAM. Refer to the [events reference](/platform/administration/cloudevents/events-reference/) for the event types available.

### Registry metadata

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `registry_repos_list` | `name`, `uidp`, `order_by`, `page_size`, `page_token`, `skip` | Repositories you can access |
| `registry_repos_get` | `uid` | One repository |
| `registry_repos_create` / `registry_repos_update` / `registry_repos_delete` — **write** | repo fields, `parent`, `uid` | Manage repositories, including Custom Assembly configuration |
| `registry_tags_list` | `name`, `digest`, `updated_since`, `include_dates`, `include_epochs`, `include_referrers`, `include_vcs_snapshots`, `uidp`, pagination | Tags you can access |
| `registry_tags_get` | `uid` | One tag |
| `registry_images_get_architectures` | image identifier | The architectures an image provides |
| `registry_images_get_size` | image identifier | An image's size |
| `registry_overlays_list` / `registry_overlays_get` | `uidp`, pagination, `uid` | Custom Assembly overlays |
| `registry_overlay_bindings_list` / `registry_overlay_bindings_get` | `uidp`, pagination, `uid` | Which overlays are bound to which repositories |

*Example prompt:* "Which repositories in my org have been updated this week?"

### Security advisories

| Tool | Parameters | Returns |
| ----- | ----- | ----- |
| `vulnerabilities_advisories_get` | `uid` | One security advisory |

### Tools that are deliberately withheld

Six collection-listing tools are not exposed, because enumerating them wholesale would pull sensitive organization data into a model's context. The per-resource `*_get` form of each remains available, so you can still read a specific record when you have its UIDP:

| Withheld tool | Read one instead with |
| ----- | ----- |
| `iam_scim_users_list` | — |
| `iam_identities_list` | `iam_identities_get` |
| `iam_group_invites_list` | `iam_group_invites_get` |
| `iam_role_bindings_list` | `iam_role_bindings_get` |
| `iam_terms_list_terms_acceptances` | — |
| `vulnerabilities_advisories_list` | `vulnerabilities_advisories_get` |

To enumerate any of these, use `chainctl` or the Console rather than an MCP client.

## Core tools in detail

### iam_groups_list

Lists the groups — organizations and folders — that the caller can access. An AI tool usually calls this first, because it returns the UIDPs that almost every other call needs.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | no | Filter by group name |
| `uidp` | object | no | Scope to part of the hierarchy |
| `order_by` | string | no | Sort order |
| `page_size` | integer | no | Results per page (default 50, max 200) |
| `page_token` | string | no | The `nextPageToken` from a previous call |
| `skip` | integer | no | Skip this many results |

Each group returns `name`, `uid`, `description`, `createTime`, `updateTime`, and `verified`. The response carries `totalCount` and, when more pages remain, `nextPageToken`.

*Example prompt:* "What Chainguard organizations and folders can I see?"

### registry_repos_list

Lists the container image repositories the caller can access, with the same filtering and pagination conventions. The response key is `repos`.

Each repository carries its full `activeTags` list, so pages get large quickly. A page of 50 repositories can exceed an MCP client's result limit; use a smaller `page_size` when listing a large organization.

*Example prompt:* "List the repositories in my organization."

This overlaps with `cg-oci`'s `list_repos` but answers a different question. `registry_repos_list` returns the platform's record of a repository — its UIDP, its parent group, its configuration. `cg-oci`'s `list_repos` returns what the registry serves you over the OCI protocol. Use this one for organization and configuration questions, and `cg-oci` for pulling content.

### registry_tags_list

Lists tags. It has more filters than any other tool on this server.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | no | Filter by tag name |
| `digest` | string | no | Find the tags pointing at a digest |
| `updated_since` | date-time | no | Only tags updated after this timestamp |
| `include_dates` | boolean | no | Include tag timestamps |
| `include_epochs` | boolean | no | Include epoch information |
| `include_referrers` | boolean | no | Include referring artifacts |
| `include_vcs_snapshots` | boolean | no | Include version control snapshot information |
| `uidp` | object | no | Scope to part of the hierarchy |

`include_dates` combined with `updated_since` is how you answer freshness questions across a whole organization, rather than one image at a time.

*Example prompt:* "Which tags in my org have been rebuilt since Monday?"

### api_list, api_read, and api_callers

These three describe the API rather than query it, which makes them the reliable way to find out what your token can do.

`api_list` with an empty `path` returns the services available to you. On a broadly capable token that is 16 services, all at `v2beta1`: the `iam`, `registry`, `vulnerabilities`, and `events` families.

Pass a fully qualified service name to list that service's RPCs. Use the name exactly as the root listing returns it — `iam.v2beta1.GroupsService`, not `iam.Groups`:

```
api_list(path: "iam.v2beta1.GroupsService")
  → CreateGroup, DeleteGroup, GetGroup, ListGroups, UpdateGroup
```

A path that doesn't resolve returns an empty `entries` list rather than an error, so an empty result usually means the name was abbreviated rather than that you lack access.

`api_read` takes a single RPC in `Service/Rpc` form and returns its metadata:

```
api_read(path: "iam.v2beta1.GroupsService/ListGroups")
  → capabilities: ["groups.list"]
    method: GET
    path: /iam/v2beta1/groups
    request:  chainguard.platform.iam.v2beta1.ListGroupsRequest
    response: chainguard.platform.iam.v2beta1.ListGroupsResponse
```

The `capabilities` field names the exact capability an RPC requires, which is what you need when [narrowing a token](#narrow-what-an-ai-tool-can-do) to the smallest useful set.

`api_callers` works backwards from a proto message type, such as `chainguard.platform.iam.Group`, to the RPCs that use it.

*Example prompt:* "What RPCs can I call on the Groups service, and what capability does each need?"

## Example usage

Sample exchanges from a Claude Code session with `cg-api` connected.

```Prompt
What Chainguard organizations can I see?
```

```output
  Called cg-api (ctrl+o to expand)

● Your token reaches 24 groups in total. The root organization is
  acme-corp.com, which holds folders including platform, data-services,
  and a sandbox per team. Want me to page through the rest?
```

```Prompt
Which repositories in my org were updated in the last week?
```

```output
  Called cg-api (ctrl+o to expand)

● 132 of the 142 repositories in your organization have at least one tag
  that moved in the last seven days, including gitlab-base, keycloak,
  python, and most of your Helm charts. The 10 that didn't change are
  mostly untagged test repositories, plus one expired entitlement
  (rabbitmq).
```

```Prompt
What parts of the API can I actually reach?
```

```output
  Called cg-api (ctrl+o to expand)

● Your token reaches 16 services, all at v2beta1: nine under iam (Groups,
  Roles, RoleBindings, Identities, IdentityProviders, GroupInvites, Terms,
  AccountAssociations, ExternalGroupRoleMappings), five under registry
  (Repos, Tags, Images, Overlays, OverlayBindings), plus
  vulnerabilities.Advisories and events.Subscriptions.
```

## Troubleshooting

| Symptom | What it means | What to do |
| ----- | ----- | ----- |
| A tool you expected isn't listed | `cg-api` filters its tool list by your token's capabilities, and six collection-listing tools are withheld from everyone. | Run `/mcp` to see your session's tools, and `api_list` to see the services your token reaches. For a withheld list tool, use `chainctl` or the Console. |
| `PERMISSION_DENIED` on a call | Your role does not carry the capability that RPC requires. The server enforces your existing permissions and adds nothing. | Run `api_read` on the RPC to see the capability it requires, then check your role bindings with `chainctl iam role-bindings list` or ask an organization administrator. |
| A `*_get` call fails on a UIDP you typed by hand | UIDPs are slash-delimited hierarchy paths, not names, and a folder's UIDP includes its parent's. | Get the UIDP from the matching `*_list` call rather than composing it. |
| `iam_groups_delete` fails | The group still has child resources. | Remove or move the children first, or delete a leaf folder instead. |
| A list call returns fewer results than `totalCount` | The response is one page. The default page size is 50 and the maximum is 200. | Pass the response's `nextPageToken` as `page_token` to continue. |
| Results look like another team's data | The API returns everything your token reaches across every organization you belong to, not just your current one. | Scope the call with the `uidp` filter — `children_of` or `descendants_of` your own organization's UIDP. |
| Server shows as not connected in `claude mcp list` | OAuth was never completed, or the token expired. Claude Code's tokens against the Chainguard issuer last about an hour and carry no refresh token. | Run `/mcp`, select **cg-api**, and authenticate again, or switch to the [`chainctl` helper](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser). |
| `401 invalid token` when using the `chainctl` helper | The audience was registered as a bare hostname. MCP audiences must include the `/mcp` path. | Run `chainctl auth login --audience=https://console-api.enforce.dev/mcp` and try again. |

## Next steps

- [`cg-oci`](/platform/mcp-servers/cg-oci/) — read manifests, SBOMs, and provenance from the registry itself
- [`cg-apk`](/platform/mcp-servers/cg-apk/) — search the Wolfi package index
- [`cg-versions`](/platform/mcp-servers/cg-versions/) — check upstream releases and end-of-life dates
- [Chainguard MCP servers overview](/platform/mcp-servers/overview/) — the full set, and the `chainctl` authentication recipe
- [Chainguard API documentation](/platform/api/) — the same API over plain HTTP
