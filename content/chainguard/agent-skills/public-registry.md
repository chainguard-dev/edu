---
title: "Getting started with the Chainguard Agent Skills public registry"
linktitle: "Public registry"
aliases:
- /chainguard/agent-skills/public-catalog/
description: "Browse, inspect, install, and run hardened agent skills from Chainguard's public registry with chainctl."
type: "article"
date: 2026-06-08T08:48:45+00:00
lastmod: 2026-10-09T23:38:36+00:00
draft: false
tags: ["Agent Skills", "Overview"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 30
---

Chainguard publishes a curated set of hardened agent skills in a public registry at `skills.cgr.dev/public`. Anyone with `chainctl` can browse and install them — no entitlement and no legal terms required. The Chainguard Agent Skills public registry is pull-only: you can install skills from the registry, but you can't push your own skills to it.

This guide walks through the full workflow: listing the available skills, inspecting one, pulling it to audit how Chainguard hardened it, verifying its signature, installing it, and running it with an agent.

{{< beta feature="Chainguard Agent Skills" >}}

## Prerequisites

To follow this guide, you need `chainctl` **v0.2.376** or later, installed. Refer to our guide on [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.

Unlike a [private Chainguard skills registry](/chainguard/agent-skills/skills-registry/), the public registry requires no entitlement, terms acceptance, or organization membership. You do need a Chainguard account to list and pull skills, but you don't need to be a customer.

## List available skills

Sign in, then browse the skills published in Chainguard's public registry with the `list` subcommand. The `--recursive` flag lists skills across every source in the registry. Public skills are namespaced by their upstream source (`public/<host>/<owner>/<repo>/<name>`), so the recursive listing shows each skill's full path:

```shell
chainctl auth login
chainctl skills list --group public --recursive
```

```output
     SOURCE     |                         NAME                         |                       TAGS                       |   UPDATED
----------------|------------------------------------------------------|--------------------------------------------------|--------------
 skills.cgr.dev | github.com/github/awesome-copilot/agent-supply-chain | 2201a49dd6f972ac4f685d03361d58c9c9206690, latest | 2 months ago
 skills.cgr.dev | github.com/github/awesome-copilot/game-engine        | cf4347e88c2e40a9aabe5801748ec6bf924c09be, latest | 2 months ago
 skills.cgr.dev | github.com/github/awesome-copilot/mcp-security-audit | 2201a49dd6f972ac4f685d03361d58c9c9206690, latest | 2 months ago

 . . .
```

The public registry is large, so a full `--recursive` listing can take a while to return. To browse a single source, scope the `--group` to its path instead:

```shell
chainctl skills list --group public/github.com/github/awesome-copilot
```

```output
     SOURCE     | TYPE  |               NAME                |                       TAGS                       |   UPDATED
----------------|-------|-----------------------------------|--------------------------------------------------|--------------
 skills.cgr.dev | skill | acreadiness-generate-instructions | --                                               | --
 skills.cgr.dev | skill | acreadiness-policy                | 2201a49dd6f972ac4f685d03361d58c9c9206690, latest | 2 months ago
 skills.cgr.dev | skill | add-educational-comments          | --                                               | --
 skills.cgr.dev | skill | adobe-illustrator-scripting       | --                                               | --
 skills.cgr.dev | skill | agent-owasp-compliance            | 2201a49dd6f972ac4f685d03361d58c9c9206690, latest | 3 weeks ago
 skills.cgr.dev | skill | agent-supply-chain                | 2201a49dd6f972ac4f685d03361d58c9c9206690, latest | 2 months ago
 skills.cgr.dev | skill | agentic-eval                      | --                                               | --
 skills.cgr.dev | skill | ai-team-orchestration             | --                                               | --

 . . .
```

Each hardened skill is tagged with the upstream commit Chainguard hardened it from, and most also carry `latest`. A skill with `--` in the `TAGS` column has no tags, so you can't pull or install it by tag.

## Describe a skill

To retrieve a skill's reference, digest, tags, and metadata, use the `describe` subcommand. The output records the upstream source and the exact commit Chainguard hardened from:

```shell
chainctl skills describe skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest
```

```output
      FIELD      |                                              VALUE
-----------------|--------------------------------------------------------------------------------------------------
 Display Name    | game-engine
 Reference       | public/github.com/github/awesome-copilot/game-engine
 Install Name    | public-github.com-github-awesome-copilot-game-engine
 OCI URL         | skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest
 Description     | Expert skill for building web-based game engines and games using HTML5, Canvas, WebGL, and ...
 License         | MIT
 Upstream        | github.com/github/awesome-copilot/skills/game-engine
 Upstream Commit | cf4347e88c2e40a9aabe5801748ec6bf924c09be
 License Source  | LICENSE
 Tag             | cf4347e88c2e40a9aabe5801748ec6bf924c09be
 Digest          | sha256:c8a079466ef2eb8de03847f0a96efe0b5131c628d9164bf7edb887bdd5ed668d
 Size            | 1.2 KB
 Published       | 6 days ago
```

## Pull a skill to inspect it

Where `install` drops a skill straight into your agent's skills directory, `pull` writes the skill's files to a directory you choose so you can inspect them first:

```shell
chainctl skills pull skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest ./game-engine
```

```output
Skill written to: /home/linky/game-engine
```

Every hardened skill ships with a `HARDENING.md` that records the upstream source, the exact commit Chainguard hardened from, and the outcome of each hardening run:

```shell
cat game-engine/HARDENING.md
```

```output
# Hardening report

- skill: `github.com/github/awesome-copilot/skills/game-engine`
- sha: `cf4347e88c2e40a9aabe5801748ec6bf924c09be`
- harden run: 1 (outcome: completed)
- SKILL.md modified: true

Hardened by the multi-model harden pipeline. The per-model fix plans, cross-model critiques, and the reconciled synthesis are recorded under `notes/harden/run_1/`. The corrected SKILL.md is this version's hardened overlay.
```

The report pins the exact upstream `sha` Chainguard hardened from, the outcome of the run, and whether the hardened overlay changed the skill's `SKILL.md`. Skills are hardened by a multi-model pipeline whose per-model fix plans and reconciled synthesis are recorded for the run, so you can trace exactly what was inspected and changed.

## Verify a skill's signature

Chainguard signs every skill in the public registry, and the signature covers the skill's files, including `HARDENING.md`. To check that Chainguard signed a skill and that it hasn't changed since, use the `verify` subcommand:

```shell
chainctl skills verify skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest
```

```output
   FIELD   |                                        VALUE
-----------|--------------------------------------------------------------------------------------
 Status    | verified
 Digest    | sha256:ed8ffbbd8ccf13b3230ebc64e924799824a91676d0444896b28810f906a4072f
 Identity  | https://issuer.enforce.dev/85490af34ebd49d9ea1fe9370c4ef1169930fc5f/c478d8a95ab1938a
 Issuer    | https://issuer.enforce.dev
 Log Index | 141100935
```

To verify a skill as you fetch it, add `--verify` to `pull` or `install`. The command then checks the exact digest it fetches and writes nothing unless the skill is `verified`:

```shell
chainctl skills pull --verify skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest ./game-engine
```

For what `verify` checks, its other results, and how to verify a skill with Cosign, refer to [Verifying Chainguard Agent Skills signatures](/chainguard/agent-skills/verifying-skills/).

## Install a skill

Download and install the skill to make it available to agents on your machine with the `install` subcommand:

```shell
chainctl skills install skills.cgr.dev/public/github.com/github/awesome-copilot/game-engine:latest
```

This command automatically detects any agents on your machine and places the skill into their relevant directories. The following example output shows the results on a machine where Claude Code is present:

```output
Installing github.com/github/awesome-copilot/game-engine
    AGENT    |                              LOCATION                              |                                        MODE
-------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------
 Claude Code | .claude/skills/public-github.com-github-awesome-copilot-game-engine | symlink → ../../.agents/skills/public-github.com-github-awesome-copilot-game-engine
```

## Run the skill from an agent

Load the skill into Claude Code or any MCP-compatible agent. In Claude Code, invoke it by name:

```Agent
/game-engine
```

The agent loads the skill and runs it, confirming it installed and loaded correctly end to end.

## Uninstall the skill

To remove a skill from your machine, pass its name to the `uninstall` subcommand. Use the skill's install name, which `describe` reports as the `Install Name` field — for this skill, `public-github.com-github-awesome-copilot-game-engine`:

```shell
chainctl skills uninstall public-github.com-github-awesome-copilot-game-engine
```

The command prompts for confirmation before removing any files:

```output
This will remove skill "public-github.com-github-awesome-copilot-game-engine" from local agent directories.
Proceed?
Do you want to continue? [y,N]:
Uninstalled skill "public-github.com-github-awesome-copilot-game-engine".
```

By default, `uninstall` removes the skill from every agent directory where it's installed. Use the `--agent` flag to remove it from specific agents only, or the `--global` flag to remove it from global directories instead of the current project. Add the `-y` flag to skip the confirmation prompt.

## Command reference

| Action | Command |
| ----- | ----- |
| List skills | `chainctl skills list --group public --recursive` |
| Describe a skill | `chainctl skills describe skills.cgr.dev/public/<host>/<owner>/<repo>/<name>:<tag>` |
| Verify a skill's signature | `chainctl skills verify skills.cgr.dev/public/<host>/<owner>/<repo>/<name>:<tag>` |
| Pull a skill | `chainctl skills pull skills.cgr.dev/public/<host>/<owner>/<repo>/<name>:<tag> <dir>` |
| Pull or install only if the signature verifies | Add `--verify` to `pull` or `install` |
| Install a skill | `chainctl skills install skills.cgr.dev/public/<host>/<owner>/<repo>/<name>:<tag>` |
| Uninstall a skill | `chainctl skills uninstall <install-name>` |

## Next steps

To publish, install, and run skills scoped to your own organization, refer to [Getting started with the Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/).
