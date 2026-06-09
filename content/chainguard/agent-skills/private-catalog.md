---
title: "Getting started with the Chainguard Agent Skills private registry"
linktitle: "Private Registry"
description: "Enable Chainguard Agent Skills, then push, install, and run an agent skill scoped to your organization."
type: "article"
date: 2026-06-05T08:48:45+00:00
lastmod: 2026-06-05T08:48:45+00:00
draft: false
tags: ["Agent Skills", "Overview"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 002
---

Chainguard Agent Skills lets you publish, manage, and distribute skills scoped to your organization. Skills are stored as OCI artifacts at `skills.cgr.dev/<your-org>/<skill-name>:<tag>` and managed with `chainctl`.

This guide walks through the full workflow, including how to enable the registry for your org, then push, install, and run a skill.

> **Note**: As of this writing, Chainguard Agent Skills are in beta. You can sign up for the beta program by visiting the [Chainguard Agent Skills product page](https://www.chainguard.dev/agent-skills) and clicking **Join the beta**.

## Prerequisites

To follow this guide, you need:

* `chainctl` **v0.2.275** or later, installed and authenticated. See [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.
* An active Chainguard organization.
* Owner access on the organization.

The examples use an `$ORG` environment variable to refer to your organization. Set it to the name of your organization before you begin:

```shell
export ORG=<your-organization>
```

## Enabling the skills entitlement

Before your org can push or install skills, create a skills entitlement:

```shell
chainctl skills entitlements create --parent $ORG
```

```output
Created skills entitlement for org example.dev (717b474ac6972745c5706a898aa6e67ffba97dad)
```

Next, accept the Skills Registry terms of service for your org:

```shell
chainctl skills accept-terms --group $ORG
```

This opens an interactive prompt:

```output
   Chainguard Legal Agreements
   To continue, please review and accept the following:
   ▶ [] I agree to the Skills Registry Terms of Service
         https://www.chainguard.dev/legal/agent-skills-disclosure

   ↑/↓ navigate  •  space toggle  •  enter confirm  •  q cancel
```

Press <kbd>SPACE</kbd> to accept the terms of service and <kbd>ENTER</kbd> to confirm.


## Creating an example skill

A skill is a directory containing a `SKILL.md` file. The `SKILL.md` frontmatter declares the skill's `name` and a `description` that tells an agent when to use it. The rest of the file contains the instructions the agent follows.

The next section has a few examples that refer to a skill named `hello-world`. You can create a sample `hello-world` skill with the following command:

```shell
mkdir hello-world
cat > hello-world/SKILL.md << 'EOF'
---
name: hello-world
description: A simple hello world skill. Use this to verify your skills registry setup is working end to end.
---

When this skill is invoked, greet the user with:

"Hello from Chainguard Agent Skills! Your skill installed and loaded successfully."

If the user provides their name, greet them by name instead:

"Hello, <name>! Welcome to Chainguard Agent Skills."
EOF
```

Your directory now looks like this:

```
hello-world/
└── SKILL.md
```

The directory name (`hello-world/`) must match the `name` field in the frontmatter (`name: hello-world`). If they don't match, the skill will fail to push.

## Manage skills with `chainctl`

This section outlines some of the `chainctl` commands you can use to manage skills in your organization's private Skills Registry. The following commands use the `hello-world` skill as an example, but you can use any other skills you've created in its place.

Check out the [`chainctl skills` reference documentation](/chainguard/chainctl/chainctl-docs/chainctl_skills/) for more information.

### Push the skill to your organization's registry

From the parent directory of `hello-world/`, push the skill to your org's registry and tag it:

```shell
chainctl skills push hello-world --group $ORG --tag v1.0.0
```
```output
            REFERENCE             |        DIGEST
----------------------------------|------------------------
 skills.cgr.dev/example.dev/hello-world:v1.0.0 | sha256:3196...
```

### List your skills

Confirm the skill was published with the `list` subcommand:

```shell
chainctl skills list --group $ORG
```
```output
    NAME      | LATEST TAG | UPDATED
--------------|------------|----------
 hello-world  | v1.0.0     | just now
```

To view a skill's reference, digest, tags, and metadata, use the `describe` subcommand:

```shell
chainctl skills describe skills.cgr.dev/$ORG/hello-world:v1.0.0
```
```output
    FIELD    |                                              VALUE                                               
-------------|--------------------------------------------------------------------------------------------------
 Name        | hello-world                                                                                      
 Description | A simple hello world skill. Use this to verify your skills registry setup is working end to end. 
 Tag         | v1.0.0                                                                                           
 Digest      | sha256:393c0a2556c626010dfacaa402508122cbb4218be786882b7c74d9d61b38d19e                          
 Size        | 709 B                                                                                            
 Published   | just now  
```


### Install the skill

Download and install the skill to make it available to agents on your machine:

```shell
chainctl skills install skills.cgr.dev/$ORG/hello-world:v1.0.0
```

This command automatically detects any agents on your machine and places the skill into their relevant directories. The following example output shows the results on a machine where Claude Code is present:

```output
Installing hello-world
    AGENT    |          LOCATION          |                    MODE                    
-------------|----------------------------|--------------------------------------------
 Claude Code | .claude/skills/hello-world | symlink → ../../.agents/skills/hello-world 
```

### Run the skill from an agent

Load `hello-world` into Claude or any MCP-compatible agent. In Claude Code, invoke it with:

```Agent
/hello-world
```

The agent responds:

```output
Hello from Chainguard Agent Skills! Your skill installed and loaded successfully.
```

This confirms the skill was published, installed, and loaded correctly end to end.

## Command reference

| Action | Command |
| ----- | ----- |
| Enable the entitlement | `chainctl skills entitlements create --parent $ORG` |
| Accept the registry terms | `chainctl skills accept-terms --group $ORG` |
| Push a skill | `chainctl skills push <name> --group $ORG --tag <version>` |
| List skills | `chainctl skills list --group $ORG` |
| Describe a skill | `chainctl skills describe skills.cgr.dev/$ORG/<name>:<version>` |
| Install a skill | `chainctl skills install skills.cgr.dev/$ORG/<name>:<version>` |
