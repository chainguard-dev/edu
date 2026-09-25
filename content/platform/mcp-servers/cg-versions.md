---
title: "cg-versions: the upstream version history MCP server"
linktitle: "cg-versions"
description: "Connect an MCP client to cg-versions to look up upstream release history, version streams, and end-of-life dates for the projects Chainguard tracks."
type: "article"
date: 2026-09-16T00:00:00+00:00
lastmod: 2026-09-16T00:00:00+00:00
draft: false
tags: ["MCP", "Containers"]
images: []
menu:
  docs:
    parent: "mcp-servers"
    identifier: "cg-versions"
toc: true
weight: 050
---

`cg-versions` gives an AI tool a read-only catalog of the upstream projects Chainguard tracks version information for. Through it, a client can find a tracked project, list its version streams with their end-of-life dates, and read the full release history of one stream with attribution back to the upstream tag and commit each release came from. It answers questions about what upstream projects have published and what is still supported: whether Python 3.9 is past end of life, which streams of a project are still receiving releases, and which upstream commit a given version corresponds to.

The server uses the Streamable HTTP transport, at this endpoint:

```
https://versions.cgr.dev/mcp
```

## What this server does not tell you

`cg-versions` tracks upstream releases, not what Chainguard builds. A version listed here means the upstream project published it. It doesn't mean Chainguard has built a package or image for that version. A stream that has reached end of life upstream may also still be one Chainguard supports for customers.

To find out what Chainguard actually builds, use a different server:

- [`cg-apk`](/platform/mcp-servers/cg-apk/) reads the APK index, so it shows whether a package exists at a given version.
- [`cg-oci`](/platform/mcp-servers/cg-oci/) reads the registry, so it shows whether an image tag exists at a given version.

If you ask an AI tool "Can I get Python 3.9 from Chainguard?", it may answer from this server's upstream end-of-life data, which can't answer that question. The [Chainguard Containers product release lifecycle](/chainguard/containers/concepts/lifecycle-and-eol/versions/) covers Chainguard's support for versions that upstream has dropped.

### Not to be confused with Chainguard Libraries versions

"Versions" also names an unrelated concept in [Chainguard Libraries](/chainguard/libraries/introduction/overview/): the `+cgr.N` and `-0.cgr.N` suffixes that mark a remediated build of a library package. Those suffixes are Chainguard's own rebuild counters for Java, JavaScript, and Python artifacts, and they have nothing to do with this server. `cg-versions` serves upstream version history for the projects behind Chainguard's images and packages. It does not serve library remediation versions, and no tool here returns a `cgr.N` suffix.

## Prerequisites

- An MCP-compatible client such as Claude Code, Claude Desktop, or Cursor
- A [Chainguard account](https://console.chainguard.dev/)

## Connect to the server

### Claude Code

Add the server with `claude mcp add`, using the HTTP transport:

```shell
claude mcp add --transport http cg-versions https://versions.cgr.dev/mcp
```

Pick the scope that fits how you want to use it: `local` (the default — only you, in the current directory), `project` (writes a shared `.mcp.json` at the repository root, checked in for teammates), or `user` (only you, across every project):

```shell
claude mcp add --transport http --scope user cg-versions https://versions.cgr.dev/mcp
```

The server is added unauthenticated. To complete OAuth, start a session and run the `/mcp` command:

```Prompt
/mcp
```

Select **cg-versions**, choose **Authenticate**, and approve the connection in the browser window that opens. Check the status any time with:

```shell
claude mcp list
```

```output
cg-versions: https://versions.cgr.dev/mcp (HTTP) - ✓ Connected
```

### Cursor

Cursor supports HTTP transport natively. Add the server to your MCP configuration:

```json
{
  "mcpServers": {
    "cg-versions": {
      "url": "https://versions.cgr.dev/mcp"
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
    "cg-versions": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://versions.cgr.dev/mcp"
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

Any client that supports a remote Streamable HTTP MCP server with OAuth can connect to the same endpoint. Point it at `https://versions.cgr.dev/mcp` and complete the browser sign-in when prompted.

## Authentication

Authentication is OAuth 2.0 against the Chainguard issuer.

{{< alert context="warning" >}}
**Each Chainguard MCP server requires its own login.** Authenticating to `cg-versions` does not authenticate you to `cg-oci`, `cg-apk`, or `cg-api`. Connecting all four means completing the browser sign-in four times. As of this writing, there is no unified sign-in across the four servers.
{{< /alert >}}

On a remote or headless workstation, you can supply a token from `chainctl` instead of completing the browser flow. Refer to [Authenticate with chainctl instead of a browser](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser) for the full recipe; `cg-versions`'s audience is `https://versions.cgr.dev/mcp`.

## Concepts

The catalog has three levels, and each tool works at one of them:

- A **project** is a tracked upstream piece of software, named as the catalog names it. Names follow upstream convention rather than Chainguard image names, so Node.js is `nodejs`, not `node`.
- A **stream** is a release line within a project, such as Python's `3.12`. Each stream carries its own end-of-life date and support status.
- A **version** is a single release within a stream, such as `3.9.25`, with attribution to the upstream tag and commit it was cut from.

## Tool reference

| Tool | Parameters | Returns | Example prompt |
| ----- | ----- | ----- | ----- |
| `search_projects` | `name_pattern`, `page_size`, `page_token` | `{projects, next_page_token}` — names only | "Is there a tracked project for Node?" |
| `get_project` | `project` | `{project: {name, streams}}` with per-stream EOL status | "Which Python versions are still supported upstream?" |
| `get_stream` | `project`, `stream` | `{stream: {project, stream, eol_date, is_eol, versions}}` | "List every Python 3.9 release with its upstream commit" |

### search_projects

Finds tracked projects by name. Results are paginated alphabetically.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name_pattern` | string | yes | A Go regular expression applied to project names, such as `kube.*`, `^go$`, or `.*` to match everything |
| `page_size` | integer | no | Entries per page (default 25, max 200) |
| `page_token` | string | no | The `next_page_token` from a previous call. Reuse the same `name_pattern` when continuing. |

This takes a regular expression rather than a literal string. `^node` returns `node-feature-discovery`, `node-problem-detector`, and `nodejs`, so a partial name usually finds the catalog's name for the project. Anchor the pattern with `^` and `$` when you want one project and nothing else.

Matches come back as names only, with no version data attached. Chain to `get_project` for anything more.

### get_project

Returns a project's identity together with a support-status summary for each of its version streams.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `project` | string | yes | Project name as `search_projects` returns it, such as `python` |

Each stream in the response carries:

| Field | Description |
| ----- | ----- |
| `stream` | The release line, such as `3.12` |
| `eol_date` | The upstream end-of-life date, where known |
| `is_eol` | Whether the stream is past that date |
| `version_count` | How many releases the catalog holds for the stream |

Use this tool to find which streams are still supported. For `python` it returns streams `3.8` through `3.14`, with `3.9` and `3.8` marked `is_eol: true` and `3.14` carrying an `eol_date` of 2030-10-31. A `version_count` of zero means the catalog tracks the stream's support dates but holds no individual releases for it, which is common for streams that reached end of life some time ago.

### get_stream

Returns the release history for one stream of a project, with upstream source attribution for each version.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `project` | string | yes | Project name, such as `python` |
| `stream` | string | yes | Stream name within the project, such as `3.9` |

Both parameters are required, so the call is always scoped to a single release line; there is no way to pull a project's entire history in one request. The response repeats the stream's `eol_date` and `is_eol`, then lists its versions newest first. Each version carries a `sources` array, where each source has a `type` and whatever attribution that source provides:

| Source type | What it contributes |
| ----- | ----- |
| `git` | The upstream tag, a URL for it, the commit hash, and the tag's publication timestamp |
| `endoflife.date` | When the release was recorded in endoflife.date |
| `release_monitor` | The tag as release-monitoring.org saw it |

A single version usually carries all three, which is what makes this tool useful for provenance questions: Python 3.9.25 resolves to tag `v3.9.25` at commit `0bbaf5de` in `python/cpython`, published 2025-10-31.

There is no `page_size` or cursor on this tool. Streams usually hold only a few releases (Python 3.9 has five), but the response has no size limit.

## Example usage

Sample exchanges from a Claude Code session with `cg-versions` connected.

```Prompt
Which Python versions are still supported upstream?
```

```output
  Called cg-versions (ctrl+o to expand)

● Upstream Python currently supports 3.10 through 3.14. End-of-life dates
  run from 2026-10-31 for 3.10 out to 2030-10-31 for 3.14. Python 3.9 went
  end of life on 2025-10-31 and 3.8 on 2024-10-07.

  This is upstream support only. It doesn't tell you what Chainguard
  builds; cg-apk or cg-oci can answer that.
```

```Prompt
Is there a tracked project for Node?
```

```output
  Called cg-versions (ctrl+o to expand)

● Three projects match: nodejs, node-feature-discovery, and
  node-problem-detector. The Node.js runtime is tracked as "nodejs".
```

```Prompt
Show me every Python 3.9 release and where it came from.
```

```output
  Called cg-versions (ctrl+o to expand)

● The catalog doesn't have every Python 3.9 release. Its history starts in
  December 2024 and holds five releases, newest first:

  3.9.25 — tag v3.9.25, commit 0bbaf5de, published 2025-10-31
  3.9.24 — tag v3.9.24, commit 91bdb00d, published 2025-10-09
  3.9.23 — tag v3.9.23, commit 86527026, published 2025-06-03
  3.9.22 — tag v3.9.22, commit 05c55492, published 2025-04-08
  3.9.21 — tag v3.9.21, commit f3994ade, published 2024-12-03

  All five are tagged in python/cpython. Python 3.9 reached end of life
  upstream on 2025-10-31.
```

## Troubleshooting

| Symptom | What it means | What to do |
| ----- | ----- | ----- |
| A project lookup finds nothing | The name doesn't match the catalog's. Names follow upstream convention, not Chainguard image names. | Search with an unanchored pattern first, such as `node`, and use the name the search returns. |
| A search returns far more than you expected | `name_pattern` is a regular expression, so an unanchored pattern matches as a substring anywhere in the name. | Anchor it: `^go$` for the Go project alone, rather than `go`. |
| A stream you expected is missing | The catalog tracks streams the upstream project publishes as distinct release lines. Some projects don't maintain parallel streams. | Call `get_project` to see the streams that exist before asking for one by name. |
| A stream shows `version_count: 0` | The catalog knows the stream's support dates but holds no individual releases for it. | Use `get_project` for the support status; there is no release history to fetch. |
| The AI tool says a version is unavailable from Chainguard | It may be reasoning from upstream end-of-life data, which says nothing about Chainguard's builds. | Ask it to check [`cg-apk`](/platform/mcp-servers/cg-apk/) or [`cg-oci`](/platform/mcp-servers/cg-oci/) instead, and refer to the [product release lifecycle](/chainguard/containers/concepts/lifecycle-and-eol/versions/). |
| Server shows as not connected in `claude mcp list` | OAuth was never completed, or the token expired. Claude Code's tokens against the Chainguard issuer last about an hour and carry no refresh token. | Run `/mcp`, select **cg-versions**, and authenticate again, or switch to the [`chainctl` helper](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser). |
| `401 invalid token` when using the `chainctl` helper | The audience was registered as a bare hostname. MCP audiences must include the `/mcp` path. | Run `chainctl auth login --audience=https://versions.cgr.dev/mcp` and try again. |

## Next steps

- [`cg-apk`](/platform/mcp-servers/cg-apk/) — check whether a package is actually built at a given version
- [`cg-oci`](/platform/mcp-servers/cg-oci/) — check whether an image tag exists at a given version
- [`cg-api`](/platform/mcp-servers/cg-api/) — query organizations, IAM, and registry metadata through the platform API
- [Chainguard MCP servers overview](/platform/mcp-servers/overview/) — the full set, and the `chainctl` authentication recipe
