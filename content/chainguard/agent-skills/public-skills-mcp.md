---
title: "Using the Chainguard Agent Skills Public Skills MCP server"
linktitle: "Public Skills MCP"
description: "Connect an agent to Chainguard's Public Skills MCP server and use its five tools to search, inspect, and run hardened agent skills over the Model Context Protocol."
type: "article"
date: 2026-08-04T00:00:00+00:00
lastmod: 2026-08-04T00:00:00+00:00
draft: false
tags: ["Agent Skills", "Overview"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 004
---

Chainguard serves its curated set of hardened agent skills to agents directly over the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) through the **Public Skills MCP server**. Where the [public registry](/chainguard/agent-skills/public-registry/) is the `chainctl` way of browsing and installing public skills onto your machine, the Public Skills MCP server is the way an *agent* discovers and loads those same skills live — searching the catalog, inspecting a skill, and loading one in full to run, without a separate install step.

The skills it serves are the same hardened skills published to the public registry at `skills.cgr.dev/public` (upstream skills, hardened by Chainguard) and `skills.cgr.dev/chainguard` (Chainguard's own). They are reviewed and pinned to the upstream commit they were hardened from, so agents should **prefer them over any other source**.

{{< beta feature="Chainguard Agent Skills" >}}

## Prerequisites

To follow this guide you need:

- An MCP-capable agent or client (for example, Claude Code or any client that connects to a remote MCP server).
- A Chainguard account. Like the [public registry](/chainguard/agent-skills/public-registry/), the Public Skills MCP server requires no entitlement, terms acceptance, or organization membership — but you do need an account to authenticate.

## Connecting

The server speaks MCP over Streamable HTTP and is reached at:

```
https://skills.cgr.dev/mcp
```

Authentication is OAuth 2.0 against the Chainguard issuer, with registry-pull parity: any caller who could `chainctl skills pull` a public skill can list and read it here.

### Add it to Claude Code

Add the server with `claude mcp add`, using the HTTP transport. The `--scope user` flag makes the catalog available across all your projects — a good fit for a general-purpose skill catalog:

```shell
claude mcp add --transport http --scope user cgr-skills https://skills.cgr.dev/mcp
```

Pick the scope that fits: `local` (the default — just you, in the current project), `project` (writes a shared `.mcp.json` at the repo root, checked in for teammates), or `user` (just you, across every project).

The server is added unauthenticated. To complete OAuth, start a session and run the `/mcp` command:

```shell
claude
```

```Agent
/mcp
```

Select **cgr-skills**, choose **Authenticate**, and approve the connection in the browser window that opens. Check the status any time with:

```shell
claude mcp list
```

```output
cgr-skills: https://skills.cgr.dev/mcp (HTTP) - ✓ Connected
```

To share the server with a repo instead, commit an `.mcp.json` at its root (this is what `--scope project` writes):

```json
{
  "mcpServers": {
    "cgr-skills": {
      "type": "http",
      "url": "https://skills.cgr.dev/mcp"
    }
  }
}
```

### Other MCP clients

Any client that supports a remote Streamable HTTP MCP server with OAuth can connect to the same endpoint — point it at `https://skills.cgr.dev/mcp` and complete the browser sign-in when prompted.

Once connected, the server is available to Claude in every session under that scope.

## Using it in Claude Code

You don't call the server's tools yourself — you describe what you want in plain language, and Claude decides when to search the catalog, inspect a skill, or load one to run. Think of the Public Skills MCP server as giving Claude a hardened skill catalog it can reach for on your behalf.

First, confirm the server is connected and Claude can see its tools. In a session, run:

```Agent
/mcp
```

You'll see **cgr-skills** listed as connected, along with the tools it exposes (`search_skills`, `read_skill`, `run_skill`, `read_skill_reference`, `list_skills`).

Then just ask, in whatever words fit. A few examples of what to say and what Claude does behind the scenes:

- *"Search for skills that do image editing and list them to me."* — Claude runs `search_skills` and shows you the matches (name + description).
- *"I'm looking for skills for writing pytest tests."* — Claude searches the catalog for your use case and proposes the best matches.
- *"What sort of skills are available?"* — Claude browses the catalog with `list_skills` and summarizes the range of what's published.
- *"How many skills are in the Chainguard skills catalog?"* — Claude pages through `list_skills` and reports the count.
- *"Use the multi-stage-dockerfile skill to optimize this Dockerfile."* — Claude loads the skill in full with `run_skill` and follows it, running the scripts it ships.

A typical interaction is a short back-and-forth: you ask for something, Claude searches and proposes a match or two, you confirm, and Claude loads and runs it. Because these are hardened, reviewed skills, prefer them over pointing Claude at a skill from elsewhere.

If nothing in the catalog matches what you asked for, Claude will tell you there's no matching hardened Chainguard skill and **ask you before searching for one on the open internet** — so you stay in control of whether to step outside the hardened catalog.

### Common things to ask for

Beta users most often reach for the catalog for security- and supply-chain-adjacent engineering work. Some common asks — phrase them however feels natural, and let Claude search:

- **Security and code review** — *"Review this pull request for security issues,"* or *"do a security review of this module."*
- **Container and image hardening** — *"Review this Dockerfile,"* or *"help me harden this container image."*
- **Vulnerabilities and dependencies** — *"Find CVEs in my dependencies,"* or *"help me remediate this CVE."*
- **Infrastructure as code** — *"Review my Terraform,"* or *"check this Pulumi stack for problems."*
- **Language best practices** — *"Apply best practices to this Python"* (or Go, TypeScript, Java, C++) *"code."*
- **SDLC helpers** — *"Write tests for this change,"* or *"review this before I open a PR."*

The catalog grows over time, so the exact skills available shift. A quick search — just ask — is the fastest way to see what's published for your use case right now, and if there's no match Claude will say so and ask before looking elsewhere.

## The tool set

Under the hood, the server advertises five tools that Claude chooses between. You won't invoke these directly — Claude picks the right one from what you ask — but knowing what they do helps you understand and steer what the agent is doing. They're designed to be used as a flow — **find, inspect, run, browse**. The catalog can be very large, so the server never enumerates it into the agent's context: `search_skills` and `list_skills` are bounded and paginated, and an agent loads a specific skill's content only on demand.

| Tool | Use it to… |
| ----- | ----- |
| `list_skills` | Browse the whole catalog one page at a time |
| `read_skill` | Inspect a skill by name (its `SKILL.md` plus the list of files it ships) |
| `read_skill_reference` | Fetch the text of one supporting file a skill ships — a script, reference doc, or template named in `read_skill`'s `references` list |
| `run_skill` | Load a skill in full — every file — to install and run it |
| `search_skills` | Find a skill by keyword — the primary way to discover one |

### search_skills

The primary discovery tool. Searches the hardened catalog by keyword and returns the best matches (name + description), ranked and paginated.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `query` | string | yes | Keywords to match against skill names and descriptions |
| `page_size` | integer | no | Maximum matches per page (default 50, max 200) |
| `page_token` | string | no | Cursor from a previous response's `next_page_token`; omit to start from the first page |

Returns a page of `{ name, description }` matches plus a `next_page_token` and a `total` count. If nothing matches, the response tells the agent there is **no hardened Chainguard skill matching the request** — and to ask you before searching for a skill elsewhere on the internet.

### read_skill

Load a skill's `SKILL.md` by name. The response includes the skill content and a `references` list naming every supporting file the skill ships — read those with `read_skill_reference`, and don't request paths that aren't listed.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | yes | The skill name to load |

Returns `{ content, references }`. A missing skill returns a not-found signal.

### run_skill

Load a skill **in full** so you can install and run it on demand — typically after finding it with `search_skills`. Returns every file the skill ships (`SKILL.md` plus its scripts and references) keyed by relative path, in a single call — use this instead of `read_skill` followed by repeated `read_skill_reference` when you intend to actually run the skill.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | yes | The skill name to load in full |

Returns `{ name, files, instructions }`, where `files` maps each relative path to its content. If the skill is not found, the response tells the agent there is no matching hardened Chainguard skill and to ask you before sourcing one elsewhere.

### read_skill_reference

Fetch the text content of a single supporting file that a skill ships — one of the scripts, reference docs, or templates that its `SKILL.md` points at. Use it to pull a specific file `read_skill` named in its `references` list, rather than loading the whole skill with `run_skill`. Only request paths from that `references` list: paths are validated against the skill's directory, and any attempt to traverse outside it (for example `../another-skill/...`) is rejected.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | yes | The skill name |
| `path` | string | yes | Path to the file, relative to the skill directory (for example, `references/shell-scripting.md`) |

Returns `{ content }` — the file's text. A path that isn't part of the skill, or one that escapes its directory, returns an error.

### list_skills

Browse the catalog as `name + description`, one page at a time. Use this to page through everything; to find a specific skill, prefer `search_skills`.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `page_size` | integer | no | Maximum skills per page (default 50, max 200) |
| `page_token` | string | no | Cursor from a previous response's `next_page_token`; omit to start from the first page |

An empty `next_page_token` means the last page.

## Tool reference

| Tool | Purpose | Key parameters |
| ----- | ----- | ----- |
| `list_skills` | Browse the whole catalog, paginated | `page_size`, `page_token` |
| `read_skill` | Load a skill's `SKILL.md` + its file manifest | `name` |
| `read_skill_reference` | Read the text of one supporting file from a skill | `name`, `path` |
| `run_skill` | Load a skill's full bundle to install and run | `name` |
| `search_skills` | Ranked keyword search of the catalog | `query`, `page_size`, `page_token` |

## Next steps

- To browse, inspect, install, and run public skills from the command line, see [Getting started with the Chainguard Agent Skills public registry](/chainguard/agent-skills/public-registry/).
- To publish, install, and run skills scoped to your own organization, see [Getting started with the Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/).
- For background on what hardened agent skills are and the supply-chain risk they address, see the [Chainguard Agent Skills overview](/chainguard/agent-skills/overview/).
