---
title: "cg-apk: the Chainguard APK registry MCP server"
linktitle: "cg-apk"
description: "Connect an MCP client to cg-apk to look up Wolfi APK packages and read the SPDX SBOM and melange build recipe embedded in each one."
type: "article"
date: 2026-09-16T00:00:00+00:00
lastmod: 2026-09-16T00:00:00+00:00
draft: false
tags: ["MCP", "Wolfi"]
images: []
menu:
  docs:
    parent: "mcp-servers"
    identifier: "cg-apk"
toc: true
weight: 030
---

`cg-apk` gives an AI tool read-only access to the Chainguard APK registry — the Wolfi package index that Chainguard container images are built from. This lets a client look up a package by name to find its current version, license, and origin, then read the SPDX SBOM and the melange build recipe embedded in the APK itself. That combination answers questions the package index alone cannot: not just which version of `openssl` ships today, but which upstream commit it was built from and what build definition produced it.

The server uses the Streamable HTTP transport, at this endpoint:

```
https://apk.cgr.dev/mcp
```

## Prerequisites

- An MCP-compatible client such as Claude Code, Claude Desktop, or Cursor
- A [Chainguard account](https://console.chainguard.dev/)

## Connect to the server

### Claude Code

Add the server with `claude mcp add`, using the HTTP transport:

```shell
claude mcp add --transport http cg-apk https://apk.cgr.dev/mcp
```

Pick the scope that fits how you want to use it: `local` (the default — only you, in the current directory), `project` (writes a shared `.mcp.json` at the repository root, checked in for teammates), or `user` (only you, across every project). Package lookups are useful in any repository, so `--scope user` is usually the right choice:

```shell
claude mcp add --transport http --scope user cg-apk https://apk.cgr.dev/mcp
```

The server is added unauthenticated. To complete OAuth, start a session and run the `/mcp` command:

```Prompt
/mcp
```

Select **cg-apk**, choose **Authenticate**, and approve the connection in the browser window that opens. Check the status any time with:

```shell
claude mcp list
```

```output
cg-apk: https://apk.cgr.dev/mcp (HTTP) - ✓ Connected
```

### Cursor

Cursor supports HTTP transport natively. Add the server to your MCP configuration:

```json
{
  "mcpServers": {
    "cg-apk": {
      "url": "https://apk.cgr.dev/mcp"
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
    "cg-apk": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://apk.cgr.dev/mcp"
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

Any client that supports a remote Streamable HTTP MCP server with OAuth can connect to the same endpoint. Point it at `https://apk.cgr.dev/mcp` and complete the browser sign-in when prompted.

## Authentication

Authentication is OAuth 2.0 against the Chainguard issuer. Results are scoped to the APK repositories your account can read.

{{< alert context="warning" >}}
**Each Chainguard MCP server requires its own login.** Authenticating to `cg-apk` does not authenticate you to `cg-oci`, `cg-versions`, or `cg-api`. Connecting all four means completing the browser sign-in four times. As of this writing, there is no unified sign-in across the four servers.
{{< /alert >}}

On a remote or headless workstation, you can supply a token from `chainctl` instead of completing the browser flow. Refer to [Authenticate with chainctl instead of a browser](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser) for the full recipe; `cg-apk`'s audience is `https://apk.cgr.dev/mcp`.

## Tool reference

The server exposes three tools. `search_packages` is the entry point, and its results include the four values the other two tools require, so a session normally starts with a search.

| Tool | Parameters | Returns | Example prompt |
| ----- | ----- | ----- | ----- |
| `search_packages` | `name`, `exact`, `origin`, `all_versions`, `arch`, `page_size`, `cursor` | `{name, count, matches, page_size, next_cursor}` | "What version of openssl is in Wolfi?" |
| `get_sbom` | `package_name`, `version`, `architecture`, `scope` | `{sbom}` — raw SPDX JSON | "What upstream source was the jq package built from?" |
| `get_melange_config` | `package_name`, `version`, `architecture`, `scope` | `{melange_configuration}` — raw YAML | "Show me the melange build recipe for jq" |

### search_packages

Looks up APK packages by name, one bounded page at a time.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | yes | Package name to search for. A case-insensitive substring match by default. |
| `exact` | boolean | no | Require an exact name match (`-e`/`--exact`). Uses an indexed lookup; prefer it whenever you know the name. |
| `origin` | boolean | no | Treat `name` as an origin (`-o`/`--origin`), returning the main package and all its subpackages |
| `all_versions` | boolean | no | Return every version rather than only the latest (`-a`/`--all`) |
| `arch` | string | no | Filter by architecture, such as `x86_64` or `aarch64` (default `x86_64`) |
| `page_size` | integer | no | Results per page (default 50, max 200) |
| `cursor` | string | no | The `next_cursor` from a previous call |

Each match returns `package_name`, `version`, `architectures`, `description`, `license`, `origin`, and `scope`.

Keep the following in mind when you search:

- **Substring matching is the default, and it is the expensive path.** A search with only `name` set scans the whole index, like `apk search`. When you already know the package name, pass `exact=true` for an indexed lookup instead. Searching `libxml` returns every package whose name contains that string; searching `libxml2` with `exact=true` returns only that package.
- **In exact and substring searches, the same package appears once per repository scope you can read.** `scope` is the UIDP of the APK repository a given copy lives in, and a package built into several repositories returns one match per repository. An exact search for `openssl` can return several identical rows that differ only in `scope`. This is not duplication in the index; it reflects the repositories your token reaches.

`origin` is the most useful flag for migration work. Given `origin=true` and the name of a source package, it returns the main package and every subpackage built from it, such as `-dev`, `-doc`, and `-static`, which helps when you replace a Debian development package such as `libssl-dev` with its Wolfi equivalent. An `origin=true` search also collapses the per-scope duplicates, returning one row per package with a combined architecture list.

### get_sbom

Fetches the SPDX SBOM document embedded in an APK's filesystem, at `var/lib/db/sbom/<pkg>-<ver>.spdx.json`. The response is `{sbom}`, the raw SPDX JSON as a string.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `package_name` | string | yes | The APK package name, matching `package_name` from a search result |
| `version` | string | yes | The package version, matching `version` from a search result |
| `architecture` | string | yes | A single architecture, such as `x86_64`. Search results return `architectures` as a comma-joined list; pick one. |
| `scope` | string | yes | The repository UIDP, matching `scope` from a search result |

All four values come from `search_packages`, so this chains directly off a search. The document records the upstream source the package was generated from — for `jq` 1.8.2-r2, a `GENERATED_FROM` relationship pointing at the exact `github.com/jqlang/jq` commit — alongside the melange definition that built it and the APK's own metadata.

### get_melange_config

Fetches the `.melange.yaml` build recipe embedded in an APK's control section. The response is `{melange_configuration}`, the raw YAML as a string.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `package_name` | string | yes | The APK package name, matching `package_name` from a search result |
| `version` | string | yes | The package version, matching `version` from a search result |
| `architecture` | string | yes | A single architecture, such as `x86_64` |
| `scope` | string | yes | The repository UIDP, matching `scope` from a search result |

APKs built before melange configs were embedded return an error rather than an empty result. Some recipes are very large — `openssl`'s runs past 60,000 characters — so expect a client to truncate or summarize rather than print one in full.

## Example usage

Sample exchanges from a Claude Code session with `cg-apk` connected. Package versions change often, so your answers will differ.

```Prompt
What version of openssl is in Wolfi right now?
```

```output
  Called cg-apk (ctrl+o to expand)

● Wolfi currently ships openssl 3.6.4 for x86_64, licensed Apache-2.0. It
  appears in five repository scopes your account can read, all at the
  same version.
```

```Prompt
I need the Wolfi equivalents of libxml2-dev. What's available?
```

```output
  Called cg-apk (ctrl+o to expand)

● The libxml2 origin builds seven packages for aarch64 and x86_64:
  libxml2, libxml2-16, libxml2-dev, libxml2-doc, libxml2-py3,
  libxml2-static, and libxml2-utils. libxml2-dev is the direct equivalent.
```

```Prompt
What upstream commit was the jq package built from?
```

```output
  Called cg-apk (ctrl+o to expand)

● jq 1.8.2 was generated from jqlang/jq at commit 34f7186b, fetched as the
  jq-1.8.2 archive. The package is licensed MIT.
```

## Troubleshooting

| Symptom | What it means | What to do |
| ----- | ----- | ----- |
| A search returns nothing | The substring matched no package name. Names in Wolfi often differ from their Debian or Fedora equivalents. | Try a shorter substring, or look up the mapping with the [AI Docs MCP server](/mcp-server-ai-docs/)'s `find_package_equivalent` tool, or the [package comparison tool](https://images.chainguard.dev/). |
| A search is slow | A bare `name` runs a wildcard scan of the whole index. | Pass `exact=true` when you know the name. |
| The same package appears several times | One match per repository scope your token can read. | Use whichever `scope` you intend to pull from; if you only consume the public index, any of them resolves to the same content. |
| `get_sbom` or `get_melange_config` returns HTTP 401 or 403 | The `scope` you passed names a repository your token cannot read. | Re-run `search_packages` and use a `scope` from its results rather than one carried over from another session or account. |
| `get_melange_config` returns an error for a package that exists | The APK predates embedded melange configs. | Call `get_sbom` instead. The SBOM still records the upstream source the package was built from. |
| Server shows as not connected in `claude mcp list` | OAuth was never completed, or the token expired. Claude Code's tokens against the Chainguard issuer last about an hour and carry no refresh token. | Run `/mcp`, select **cg-apk**, and authenticate again, or switch to the [`chainctl` helper](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser). |
| `401 invalid token` when using the `chainctl` helper | The audience was registered as a bare hostname. MCP audiences must include the `/mcp` path. | Run `chainctl auth login --audience=https://apk.cgr.dev/mcp` and try again. |

## Next steps

- [`cg-oci`](/platform/mcp-servers/cg-oci/) — read manifests, SBOMs, and provenance for container images
- [`cg-versions`](/platform/mcp-servers/cg-versions/) — check upstream releases and end-of-life dates
- [`cg-api`](/platform/mcp-servers/cg-api/) — query organizations, IAM, and registry metadata through the platform API
- [Chainguard MCP servers overview](/platform/mcp-servers/overview/) — the full set, and the `chainctl` authentication recipe
