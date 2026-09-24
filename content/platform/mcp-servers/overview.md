---
title: "Chainguard MCP servers overview"
linktitle: "Overview"
description: "The four Chainguard MCP servers that expose live product data — images, packages, version history, and platform APIs — to any MCP-compatible client."
type: "article"
date: 2026-09-16T00:00:00+00:00
lastmod: 2026-09-16T00:00:00+00:00
draft: false
tags: ["MCP", "Overview"]
images: []
menu:
  docs:
    parent: "mcp-servers"
    identifier: "MCP Servers Overview"
toc: true
weight: 010
---

Chainguard runs four MCP servers that give an AI tool direct access to live product data: the container images in `cgr.dev`, the Wolfi package index, upstream version and end-of-life history, and the Chainguard platform API. An MCP client connected to them can answer questions such as what a given image's SBOM contains, which Wolfi package replaces a Debian one, or whether an upstream release is still supported, using data from the product itself rather than from a model's training data.

These servers back the [Chainguard Power for Kiro](/platform/integrations/kiro/) and the [Chainguard plugin for Cursor](/platform/integrations/cursor/), but you don't need either one. Any MCP-compatible client can connect to them directly.

## What is MCP?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open protocol that standardizes how AI applications access external data and tools. An MCP server exposes structured data and tools that AI clients can call to ground their responses in real information.

## The four servers

| Server | Endpoint | What it gives you |
| ----- | ----- | ----- |
| [`cg-oci`](/platform/mcp-servers/cg-oci/) | `https://cgr.dev/mcp` | Manifests, image configs, SBOMs, apko configs, and provenance for a specific image reference |
| [`cg-apk`](/platform/mcp-servers/cg-apk/) | `https://apk.cgr.dev/mcp` | Wolfi package lookup by name, plus package SBOMs and melange build configs |
| [`cg-versions`](/platform/mcp-servers/cg-versions/) | `https://versions.cgr.dev/mcp` | Upstream release and end-of-life history for tracked projects, and upgrade paths between versions |
| [`cg-api`](/platform/mcp-servers/cg-api/) | `https://console-api.enforce.dev/mcp` | The Chainguard platform API: organizations, IAM, policies, registry metadata, and attestation verification |

All four use the Streamable HTTP transport and authenticate with OAuth 2.0 against the Chainguard issuer.

## How these differ from the other Chainguard MCP servers

Chainguard also runs the [AI Docs MCP server](/mcp-server-ai-docs/), which serves documentation, and the [Public Skills MCP server](/chainguard/agent-skills/public-skills-mcp/), which serves agent skills. The four servers in this section are separate: they return live product data, such as an image tag's manifest and SBOM as it exists in the registry right now, rather than documentation about it.

## Authentication

Each server authenticates separately with OAuth 2.0 against the Chainguard issuer. On first use, your client opens a browser window for sign-in.

{{< alert context="warning" >}}
**Each server requires its own login.** Connecting all four means completing the browser sign-in four times, once per endpoint. As of this writing, there is no unified sign-in across the four servers.
{{< /alert >}}

Every tool call is scoped to the token it runs under. The servers return what your Chainguard account can already read and nothing more, so two people connected to the same endpoint can see different repositories, packages, and organizations. `cg-api` goes further and varies its *tool list* by token: tools your capabilities don't cover never appear in the client.

### Authenticate with chainctl instead of a browser

On a remote or headless workstation, the browser redirect can't complete. Claude Code's OAuth path against `issuer.enforce.dev` also issues access tokens that last about an hour and carry no refresh token, so the browser flow repeats often. To avoid both problems, reuse your existing `chainctl` session.

First, register an audience for each MCP server you plan to use. An OAuth audience names the resource a token is valid for, and for MCP servers it must be the full URL including the `/mcp` path — a bare hostname is rejected with `401 invalid token`. Repeat `--audience` to request several tokens at once, and add `--headless` to log in with a device code rather than a browser redirect:

```sh
chainctl auth login \
  --headless \
  --audience=https://cgr.dev/mcp \
  --audience=https://apk.cgr.dev/mcp \
  --audience=https://versions.cgr.dev/mcp \
  --audience=https://console-api.enforce.dev/mcp
```

Once an audience is logged in, `chainctl auth token --audience=<url>` returns from cache without prompting, and `chainctl` refreshes the underlying token as it nears expiry.

Next, point your client at `chainctl` rather than at OAuth. Claude Code's MCP configuration accepts a `headersHelper` field naming a script that Claude Code runs (through `sh -c`, with a roughly 10-second budget) each time it opens a connection. The script reads `CLAUDE_CODE_MCP_SERVER_URL` from its environment and prints a JSON object of HTTP headers on stdout, which Claude Code merges into the connection in place of the OAuth flow.

Save this helper as its own file and make it executable. It works for any Chainguard MCP server, so you need only one copy no matter how many you connect:

```shell
mkdir -p ~/bin
cat > ~/bin/cg-mcp-headers <<'EOF'
#!/bin/sh
set -e
aud=${CLAUDE_CODE_MCP_SERVER_URL:?CLAUDE_CODE_MCP_SERVER_URL not set}
tok=$(timeout -s KILL 8 chainctl auth token --audience="$aud") || {
    echo "no chainctl token for audience $aud; run: chainctl auth login --audience=$aud" >&2
    exit 1
}
printf '{"Authorization":"Bearer %s"}\n' "$tok"
EOF
chmod +x ~/bin/cg-mcp-headers
```

The heredoc delimiter is quoted (`<<'EOF'`) so that the shell writes `$aud`, `$tok`, and `${CLAUDE_CODE_MCP_SERVER_URL}` into the file literally. With an unquoted delimiter, the shell replaces all three with empty strings, and the resulting script sends no credentials.

The file must be executable because Claude Code runs its path as a command through `sh -c`.

The `timeout` keeps the helper from stalling. If you haven't logged in to an audience, `chainctl auth token` starts an interactive login, which runs past Claude Code's time limit for the helper. With the timeout, the helper exits quickly and prints the command that fixes the problem.

Now reference the script from each server entry. The `headersHelper` value must be an absolute path, so write the file from the repository root and let the shell expand `$HOME` for you:

```shell
cat > .mcp.json <<EOF
{
  "mcpServers": {
    "cg-oci": {
      "type": "http",
      "url": "https://cgr.dev/mcp",
      "headersHelper": "$HOME/bin/cg-mcp-headers"
    },
    "cg-apk": {
      "type": "http",
      "url": "https://apk.cgr.dev/mcp",
      "headersHelper": "$HOME/bin/cg-mcp-headers"
    },
    "cg-versions": {
      "type": "http",
      "url": "https://versions.cgr.dev/mcp",
      "headersHelper": "$HOME/bin/cg-mcp-headers"
    },
    "cg-api": {
      "type": "http",
      "url": "https://console-api.enforce.dev/mcp",
      "headersHelper": "$HOME/bin/cg-mcp-headers"
    }
  }
}
EOF
```

This delimiter is deliberately unquoted, unlike the one in the helper script. There are no other shell variables in the JSON, so `$HOME` resolves to your real home directory as the file is written and you avoid hand-editing four paths.

That command replaces any existing `.mcp.json`. If the repository already has one, merge the `mcpServers` entries into it by hand instead.

### Keep your path out of a shared file

A committed `.mcp.json` carries your home directory to everyone who clones the repository, and their username won't match yours. To keep the tracked file generic, leave the plain `type` and `url` entries in `.mcp.json` and put the `headersHelper` override in your own `~/.claude.json`, under the repository's absolute path:

```json
{
  "projects": {
    "/absolute/path/to/repo": {
      "mcpServers": {
        "cg-oci": {
          "type": "http",
          "url": "https://cgr.dev/mcp",
          "headersHelper": "/home/your-user/bin/cg-mcp-headers"
        }
      }
    }
  }
}
```

{{< alert context="danger" >}}
Edit `~/.claude.json` rather than overwriting it. It holds all of your Claude Code configuration, so redirecting a heredoc over it discards everything else you have set up. Open it in an editor and add the `projects` entry alongside what's already there.
{{< /alert >}}

Because this form is keyed by absolute path, a second clone or `git worktree` of the same repository needs its own entry.

## Pagination

Every `list_*` and `search_*` tool across the four servers returns one page at a time and caps the page size. The parameter names differ by server:

| Server | Page size | Request the next page with | Response field to pass back |
| ----- | ----- | ----- | ----- |
| `cg-oci` | 50 default, 200 max | `cursor` | `next_cursor` (or the last item's name, for `list_repos`) |
| `cg-apk` | 50 default, 200 max | `cursor` | `next_cursor` |
| `cg-versions` | 25 default, 200 max | `page_token` | `next_page_token` |
| `cg-api` | 50 default, 200 max | `page_token` | `nextPageToken` |

## Next steps

- [`cg-oci`](/platform/mcp-servers/cg-oci/) — look up manifests, configs, SBOMs, and provenance for a container image
- [`cg-apk`](/platform/mcp-servers/cg-apk/) — find Wolfi packages and read their SBOMs and build configs
- [`cg-versions`](/platform/mcp-servers/cg-versions/) — check upstream releases, end-of-life dates, and upgrade paths
- [`cg-api`](/platform/mcp-servers/cg-api/) — query organizations, IAM, policies, and attestations through the platform API
