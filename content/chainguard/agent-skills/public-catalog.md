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

Chainguard publishes a curated set of hardened agent skills in a public catalog at `skills.cgr.dev/chainguard`. Anyone with `chainctl` can browse and install them — no entitlement and no legal terms required. The Chainguard Agent Skills public catalog is pull-only: you can install skills from the catalog, but you can't push your own skills to it.

This guide walks through the full workflow: listing the available skills, inspecting one, installing it, and running it with an agent.

> **Note**: As of this writing, Chainguard Agent Skills are in beta. You can sign up for the beta program by visiting the [Chainguard Agent Skills product page](https://www.chainguard.dev/agent-skills) and clicking **Join the beta**.

## Prerequisites

To follow this guide, you need `chainctl` **v0.2.275** or later, installed. Refer to our guide on [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.

Unlike a [private Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/), the public catalog requires no entitlement, terms acceptance, or organization membership.

## List available skills

You can browse the skills published in the public Chainguard catalog with the `list` subcommand:

```shell
chainctl skills list --group chainguard
```
```output
    NAME      | LATEST TAG | UPDATED
--------------|------------|----------
 hello-world  | v1.0.0     | 2 days ago
```

## Inspect a skill

To retrieve a skill's reference, digest, tags, and metadata, use the `describe` subcommand:

```shell
chainctl skills describe skills.cgr.dev/chainguard/hello-world:v1.0.0
```
```output
    FIELD    |                                              VALUE                                               
-------------|--------------------------------------------------------------------------------------------------
 Name        | hello-world                                                                                      
 Description | A simple hello world skill. Use this to verify your skills registry setup is working end to end. 
 Tag         | v1.0.0                                                                                           
 Digest      | sha256:393c0a2556c626010dfacaa402508122cbb4218be786882b7c74d9d61b38d19e                          
 Size        | 709 B                                                                                            
 Published   | 2 days ago  
```

## Install a skill

Download and install the skill to make it available to agents on your machine with the `install` subcommand:

```shell
chainctl skills install skills.cgr.dev/chainguard/hello-world:v1.0.0
```

This command automatically detects any agents on your machine and places the skill into their relevant directories. The following example output shows the results on a machine where Claude Code is present:

```output
Installing hello-world
    AGENT    |          LOCATION          |                    MODE                    
-------------|----------------------------|--------------------------------------------
 Claude Code | .claude/skills/hello-world | symlink → ../../.agents/skills/hello-world 
```

## Run the skill from an agent

Load `hello-world` into Claude Code or any MCP-compatible agent. In Claude Code, invoke it by name:

```Agent
/hello-world
```

The agent responds:

```output
Hello from Chainguard Agent Skills! Your skill installed and loaded successfully.
```

This confirms the skill installed and loaded correctly end to end.

## Command reference

| Action | Command |
| ----- | ----- |
| List skills | `chainctl skills list --group chainguard` |
| Describe a skill | `chainctl skills describe skills.cgr.dev/chainguard/<name>:<tag>` |
| Install a skill | `chainctl skills install skills.cgr.dev/chainguard/<name>:<tag>` |

## Next steps

To publish, install, and run skills scoped to your own organization, see [Getting started with the Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/).
