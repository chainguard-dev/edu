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

Sign in, then browse the skills published in the public Chainguard catalog with the `list` subcommand. The `--recursive` flag lists skills across every source in the catalog. Public skills are namespaced by their upstream source (`public/<host>/<owner>/<repo>/<name>`), so the recursive listing shows each skill's full path:

```shell
chainctl auth login
chainctl skills list --group public --recursive
```

```output
                        NAME                        | LATEST TAG |  UPDATED
----------------------------------------------------|------------|------------
 github.com/anthropics/skills/brand-guidelines      | latest     | 5 days ago
 github.com/anthropics/skills/internal-comms        | latest     | 5 days ago

 . . .
```

The public catalog is large, so a full `--recursive` listing can take a while to return. To browse a single source, scope the `--group` to its path instead (shown next).

To list the skills under a single upstream repository, name its path in the `--group` value. Public skills are namespaced by their source, so an owner's repo lives at `public/<host>/<owner>/<repo>`:

```shell
chainctl skills list --group public/github.com/anthropics/skills
```

```output
 TYPE  |       NAME       | LATEST TAG |  UPDATED
-------|------------------|------------|------------
 skill | brand-guidelines | latest     | 5 days ago
 skill | internal-comms   | latest     | 5 days ago
```

## Describe a skill

To retrieve a skill's reference, digest, tags, and metadata, use the `describe` subcommand. The output records the upstream source and the exact commit Chainguard hardened from:

```shell
chainctl skills describe skills.cgr.dev/public/github.com/anthropics/skills/brand-guidelines:latest
```

```output
      FIELD      |                                                                     VALUE
-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------
 Display Name    | brand-guidelines
 Reference       | public/github.com/anthropics/skills/brand-guidelines
 Install Name    | public-github.com-anthropics-skills-brand-guidelines
 OCI URL         | skills.cgr.dev/public/github.com/anthropics/skills/brand-guidelines:latest
 Description     | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel.
 License         | Apache-2.0
 Upstream        | github.com/anthropics/skills/skills/brand-guidelines
 Upstream Commit | ef740771ac901e03fbca3ce4e1c453a96010f30a
 License Source  | skills/brand-guidelines/LICENSE.txt
 Tag             | ef740771ac901e03fbca3ce4e1c453a96010f30a
 Digest          | sha256:78b0910c0d349f4d0ca14b4f8545e52d7aceaaf1a567b8cccd1f49e11cf329c8
 Size            | 1.2 KB
 Published       | 6 days ago
```

## Pull a skill to inspect it

Where `install` drops a skill straight into your agent's skills directory, `pull` writes the skill's files to a directory you choose so you can inspect them first:

```shell
chainctl skills pull skills.cgr.dev/public/github.com/anthropics/skills/brand-guidelines:latest ./brand-guidelines
```

```output
Skill written to: /home/linky/brand-guidelines
```

Every hardened skill ships with a `HARDENING.md` that records the upstream source, the exact commit Chainguard hardened from, and the outcome of each hardening run:

```shell
cat brand-guidelines/HARDENING.md
```

```output
# Hardening report

- skill: brand-guidelines
- sha: ef740771ac901e03fbca3ce4e1c453a96010f30a
- harden run: 1 (outcome: completed)

The per-model transcripts and any findings for this run are recorded under
`notes/harden/run_1/`.
```

The report pins the exact upstream `sha` Chainguard hardened from and the outcome of the run. The full per-model hardening transcripts and any findings are written alongside the skill under `notes/harden/run_1/`, so you can audit exactly what the hardening engine inspected and changed.

## Install a skill

Download and install the skill to make it available to agents on your machine with the `install` subcommand:

```shell
chainctl skills install skills.cgr.dev/public/github.com/anthropics/skills/brand-guidelines:latest
```

This command automatically detects any agents on your machine and places the skill into their relevant directories. The following example output shows the results on a machine where Claude Code is present:

```output
Installing github.com/anthropics/skills/brand-guidelines
    AGENT    |                              LOCATION                              |                                        MODE
-------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------
 Claude Code | .claude/skills/public-github.com-anthropics-skills-brand-guidelines | symlink → ../../.agents/skills/public-github.com-anthropics-skills-brand-guidelines
```

## Run the skill from an agent

Load the skill into Claude Code or any MCP-compatible agent. In Claude Code, invoke it by name:

```Agent
/brand-guidelines
```

The agent loads the skill and runs it, confirming it installed and loaded correctly end to end.

## Uninstall the skill

To remove a skill from your machine, pass its name to the `uninstall` subcommand. Use the skill's install name, which `describe` reports as the `Install Name` field — for this skill, `public-github.com-anthropics-skills-brand-guidelines`:

```shell
chainctl skills uninstall public-github.com-anthropics-skills-brand-guidelines
```

The command prompts for confirmation before removing any files:

```output
This will remove skill "public-github.com-anthropics-skills-brand-guidelines" from local agent directories.
Proceed?
Do you want to continue? [y,N]:
Uninstalled skill "public-github.com-anthropics-skills-brand-guidelines".
```

By default, `uninstall` removes the skill from every agent directory where it's installed. Use the `--agent` flag to remove it from specific agents only, or the `--global` flag to remove it from global directories instead of the current project. Add the `-y` flag to skip the confirmation prompt.

## Command reference

| Action | Command |
| ----- | ----- |
| List skills | `chainctl skills list --group public --recursive` |
| Describe a skill | `chainctl skills describe skills.cgr.dev/public/<host>/<owner>/<repo>/<name>:<tag>` |
| Pull a skill | `chainctl skills pull skills.cgr.dev/public/<host>/<owner>/<repo>/<name>:<tag> <dir>` |
| Install a skill | `chainctl skills install skills.cgr.dev/public/<host>/<owner>/<repo>/<name>:<tag>` |
| Uninstall a skill | `chainctl skills uninstall <install-name>` |

## Next steps

To publish, install, and run skills scoped to your own organization, see [Getting started with the Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/).
