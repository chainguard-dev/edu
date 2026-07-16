---
title: "Getting started with the Chainguard Agent Skills public catalog"
linktitle: "Public Catalog"
description: "Browse, inspect, install, and run hardened agent skills from Chainguard's public catalog with chainctl."
type: "article"
date: 2026-06-08T08:48:45+00:00
lastmod: 2026-06-08T08:48:45+00:00
draft: false
tags: ["Agent Skills", "Overview"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 003
---

Chainguard publishes a curated set of hardened agent skills in a public catalog at `skills.cgr.dev/public`. Anyone with `chainctl` can browse and install them — no entitlement and no legal terms required. The Chainguard Agent Skills public catalog is pull-only: you can install skills from the catalog, but you can't push your own skills to it.

This guide walks through the full workflow: listing the available skills, inspecting one, pulling it to audit how Chainguard hardened it, installing it, and running it with an agent.

{{< beta feature="Chainguard Agent Skills" >}}

## Prerequisites

To follow this guide, you need `chainctl` **v0.2.282** or later, installed. Refer to our guide on [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.

Unlike a [private Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/), the public catalog requires no entitlement, terms acceptance, or organization membership. You do need a Chainguard account to list and pull skills, but you don't need to be a customer.

## List available skills

Sign in, then browse the skills published in the public Chainguard catalog with the `list` subcommand. The `--recursive` flag lists skills across every owner in the catalog:

```shell
chainctl auth login
chainctl skills list --group public --recursive
```

```output
              NAME              | LATEST TAG |   UPDATED
--------------------------------|------------|--------------
 agentspace-so/agentspace       | latest     | 21 hours ago
 antfu/antfu                    | latest     | 21 hours ago
 antfu/nuxt                     | latest     | 21 hours ago
 antfu/vitest                   | latest     | 21 hours ago
 antfu/vue                      | latest     | 21 hours ago
 anthropics/doc-coauthoring     | latest     | 21 hours ago
 anthropics/frontend-design     | latest     | 21 hours ago
 apollographql/apollo-client    | latest     | 21 hours ago

 . . .
```

To list the skills from a single upstream owner, name it in the `--group` value:

```shell
chainctl skills list --group public/anthropics
```

```output
 TYPE  |      NAME       | LATEST TAG | UPDATED
-------|-----------------|------------|------------
 skill | doc-coauthoring | latest     | 1 hour ago
 skill | frontend-design | latest     | 1 hour ago
```

## Describe a skill

To retrieve a skill's reference, digest, tags, and metadata, use the `describe` subcommand. The output records the upstream source and the exact commit Chainguard hardened from:

```shell
chainctl skills describe skills.cgr.dev/public/github/add-educational-comments:latest
```

```output
      FIELD      |                                                    VALUE
-----------------|--------------------------------------------------------------------------------------------------------------
 Display Name    | add-educational-comments
 Reference       | public/github/add-educational-comments
 Install Name    | public-github-add-educational-comments
 OCI URL         | skills.cgr.dev/public/github/add-educational-comments:latest
 Description     | Add educational comments to the file specified, or prompt asking for file to comment if one is not provided.
 License         | MIT
 Upstream        | github.com/github/awesome-copilot/skills/add-educational-comments
 Upstream Commit | cf4347e88c2e40a9aabe5801748ec6bf924c09be
 License Source  | LICENSE
 Tag             | cf4347e88c2e40a9aabe5801748ec6bf924c09be
 Digest          | sha256:59b781f87f82aba08ccf622b60a31ee5b8fbb27fa447ed5910850d4320505735
 Size            | 1.1 KB
 Published       | 1 day ago
```

## Pull a skill to inspect it

Where `install` drops a skill straight into your agent's skills directory, `pull` writes the skill's files to a directory you choose so you can inspect them first:

```shell
chainctl skills pull skills.cgr.dev/public/github/add-educational-comments:latest ./add-educational-comments
```

```output
Skill written to: /home/linky/add-educational-comments
```

Every hardened skill ships with a `HARDENING.md` that records the upstream source, the exact commit Chainguard hardened from, and every change the hardening engine made:

```shell
cat add-educational-comments/HARDENING.md
```

```output
# Hardening Report: github.com/github/awesome-copilot/skills/add-educational-comments

| Field | Value |
|---|---|
| Upstream SHA | `cf4347e88c2e40a9aabe5801748ec6bf924c09be` |
| Hardened at | 2026-06-09T23:14:22Z |
| Files processed | 2 |
| .md files (clean after harden) | 1 |
| .md files (attempts exhausted) | 0 |
| Non-.md files (copied verbatim) | 1 |

## Markdown files

### `SKILL.md`

- Status: **clean**
- Attempts used: 2
- Findings + fixes applied:

  | Attempt | Rule | Severity | Finding |
  |---|---|---|---|
  | 1 | `minimal-permissions` | high | The skill's purpose is to statically analyze and add comments to code files. It does not require the ability to execute the code to fulfill its objectives. The prompt's rules about not 'breaking execution' are constraints on the output, not a requirement to test the code by running it in a live environment. |

## Verbatim files

- `LICENSE`
```

Here, the engine flagged `minimal-permissions`: the skill only needs to read and comment on files, so the hardened version drops the implied permission to execute them.

## Install a skill

Download and install the skill to make it available to agents on your machine with the `install` subcommand:

```shell
chainctl skills install skills.cgr.dev/public/github/add-educational-comments:latest
```

This command automatically detects any agents on your machine and places the skill into their relevant directories. The following example output shows the results on a machine where Claude Code is present:

```output
Installing github/add-educational-comments
    AGENT    |                         LOCATION                          |                                   MODE
-------------|-----------------------------------------------------------|---------------------------------------------------------------------------
 Claude Code | .claude/skills/public-github-add-educational-comments | symlink → ../../.agents/skills/public-github-add-educational-comments
```

## Run the skill from an agent

Load the skill into Claude Code or any MCP-compatible agent. In Claude Code, invoke it by name:

```Agent
/add-educational-comments
```

The agent loads the skill and runs it, confirming it installed and loaded correctly end to end.

## Uninstall the skill

To remove a skill from your machine, pass its name to the `uninstall` subcommand. Use the skill's install name, which `describe` reports as the `Install Name` field — for this skill, `public-github-add-educational-comments`:

```shell
chainctl skills uninstall public-github-add-educational-comments
```

The command prompts for confirmation before removing any files:

```output
This will remove skill "public-github-add-educational-comments" from local agent directories.
Proceed?
Do you want to continue? [y,N]:
Uninstalled skill "public-github-add-educational-comments".
```

By default, `uninstall` removes the skill from every agent directory where it's installed. Use the `--agent` flag to remove it from specific agents only, or the `--global` flag to remove it from global directories instead of the current project. Add the `-y` flag to skip the confirmation prompt.

## Command reference

| Action | Command |
| ----- | ----- |
| List skills | `chainctl skills list --group public --recursive` |
| Describe a skill | `chainctl skills describe skills.cgr.dev/public/<owner>/<name>:<tag>` |
| Pull a skill | `chainctl skills pull skills.cgr.dev/public/<owner>/<name>:<tag> <dir>` |
| Install a skill | `chainctl skills install skills.cgr.dev/public/<owner>/<name>:<tag>` |
| Uninstall a skill | `chainctl skills uninstall <install-name>` |

## Next steps

To publish, install, and run skills scoped to your own organization, see [Getting started with the Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/).
