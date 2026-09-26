---
title: "Getting started with the Chainguard Skills Registry"
linktitle: "Skills Registry"
description: "Enable the Chainguard Skills Registry, then push, install, and run an agent skill scoped to your organization."
type: "article"
date: 2026-06-05T08:48:45+00:00
lastmod: 2026-09-17T00:00:00+00:00
draft: false
tags: ["Agent Skills", "Overview"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 002
---

The Chainguard Skills Registry lets you publish, manage, and distribute skills scoped to your organization. `chainctl` publishes the skills you push as OCI artifacts at `uploads.cgr.dev/<your-org>/<skill-name>:<tag>`.

A skills entitlement provisions two namespaces under your organization, and `chainctl` serves each from its own registry host:

* `uploads.cgr.dev/<your-org>` holds the skills your organization pushes.
* `skills.cgr.dev` serves skills hardened by Chainguard, including the public catalog. You can pull from this namespace, but not push to it.

The commands in this guide reference `uploads.cgr.dev`, because that's where your own skills live. To pull hardened skills instead, refer to [Getting started with the Chainguard Agent Skills public registry](/chainguard/agent-skills/public-registry/).

This guide walks through the full workflow, including how to enable the registry for your org, then push, install, and run a skill.

{{< beta feature="Chainguard Skills Registry" >}}

## Prerequisites

To follow this guide, you need:

* `chainctl` **v0.2.353** or later, installed and authenticated. Refer to [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.
* An active Chainguard organization.
* Owner access on the organization.

The examples in this guide use an `$ORG` environment variable to refer to your organization. Set it to the name of your organization before you begin:

```shell
export ORG=<your-organization>
```

## Enabling the skills entitlement

Before your org can push or install skills, create a skills entitlement.

> **Note**: You must have the `owner` role in your organization to create a skills entitlement and accept the Skills Registry terms of service.

```shell
chainctl skills entitlements create --parent $ORG
```

```output
Created skills entitlement for org example.dev (717b474ac6972745c5706a898aa6e67ffba97dad)
```

The `entitlements` subcommands scope to an org with `--parent`, unlike the other `skills` subcommands, which use `--group`. Omit `--parent` to pick the org from an interactive list.

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

In CI, where no interactive terminal is available, pass `--yes` instead. That flag confirms you have read and agreed to the documents referenced in the [Agent Skills disclosure](https://www.chainguard.dev/legal/agent-skills-disclosure).

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

After running this command, your directory has the following structure:

```
hello-world/
└── SKILL.md
```

The directory name (`hello-world/`) must match the `name` field in the frontmatter (`name: hello-world`). If they don't match, both `validate` and `push` fail.

## Manage skills with `chainctl`

This section outlines some of the `chainctl` commands you can use to manage skills in your organization's private Skills Registry. The following commands use the `hello-world` skill as an example, but you can use any other skills you've created in its place.

Refer to the [`chainctl skills` reference documentation](/platform/chainctl/chainctl-docs/chainctl_skills/) for more information.

### Validate the skill

Before you publish, check that the skill directory meets the spec with the `validate` subcommand. It runs locally and makes no network calls:

```shell
chainctl skills validate hello-world
```

```output
✓  SKILL.md found
✓  Frontmatter valid
✓  name: "hello-world" (matches directory basename)
✓  description: 96 chars
✓  Total size: 387 B / 10 MB
✓  1 file(s) will be published:
     SKILL.md

Validation passed.
```

`validate` confirms that the directory contains a `SKILL.md`, that its frontmatter is valid, that the `name` field matches the directory name, and that the skill is within the size limit. It also lists the files that `push` will publish.

To also flag optional fields that Chainguard recommends, add the `--strict` flag:

```shell
chainctl skills validate hello-world --strict
```

```output
✓  SKILL.md found
✓  Frontmatter valid
✓  name: "hello-world" (matches directory basename)
✓  description: 96 chars
✓  Total size: 387 B / 10 MB
✓  1 file(s) will be published:
     SKILL.md
⚠  license field is recommended

Validation passed.
```

Here, `--strict` warns that the skill omits the recommended `license` field. Warnings don't cause validation to fail, but addressing them produces a more complete skill.

### Push the skill to your organization's registry

From the parent directory of `hello-world/`, push the skill to your org's registry and tag it:

```shell
chainctl skills push hello-world --group $ORG --tag v1.0.0
```

```output
                    REFERENCE                   |     DIGEST
------------------------------------------------|----------------
 uploads.cgr.dev/example.dev/hello-world:v1.0.0 | sha256:393c...
```

`--tag` is repeatable, so you can publish one artifact under several tags at once, such as `--tag v1.0.0 --tag latest`. Omit it and `chainctl` publishes as `latest` and warns that you didn't pin a version. To build and validate the artifact without publishing it, add `--dry-run`.

### List your skills

Confirm the skill was published with the `list` subcommand. `list` reads the hardened catalog by default, so pass `--source uploads` to list the skills your organization pushed:

```shell
chainctl skills list --group $ORG --source uploads
```

```output
     SOURCE      | TYPE  |    NAME     | LATEST TAG | UPDATED
-----------------|-------|-------------|------------|----------
 uploads.cgr.dev | skill | hello-world | v1.0.0     | just now
```

The `SOURCE` column names the registry host to pull each skill from. Pass `--source all` to list both namespaces in one table, or `--recursive` to list every skill in nested folders by its full path.

To view a skill's reference, digest, tags, and metadata, use the `describe` subcommand:

```shell
chainctl skills describe uploads.cgr.dev/$ORG/hello-world:v1.0.0
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
chainctl skills install uploads.cgr.dev/$ORG/hello-world:v1.0.0
```

Qualify the reference with the `uploads.cgr.dev` host to install one of your organization's own skills. A bare `<org>/<name>` reference resolves to the hardened catalog on `skills.cgr.dev` instead.

This command automatically detects any agents on your machine and places the skill into their relevant directories. The following example output shows the results on a machine where Claude Code is present:

```output
Installing hello-world
    AGENT    |          LOCATION          |                    MODE
-------------|----------------------------|--------------------------------------------
 Claude Code | .claude/skills/hello-world | symlink → ../../.agents/skills/hello-world
```

By default, `install` writes one canonical copy to `.agents/skills/` and symlinks each agent's directory to it, so every agent reads the same files. Add `--copy` to give each agent an independent copy, `--global` to install under your home directory instead of the current project, and `--agent` to target specific agents rather than every one detected.

### Run the skill from an agent

`install` places the skill where your agents already read skills from, so no further configuration is required. Start a session in the directory you installed into and invoke the skill. In Claude Code, run:

```Agent
/hello-world
```

The agent responds:

```output
Hello from Chainguard Agent Skills! Your skill installed and loaded successfully.
```

This confirms the skill was published, installed, and loaded correctly end to end.

### Uninstall the skill

To remove a skill from your machine, pass its name to the `uninstall` subcommand. You only need the name, not the full registry reference:

```shell
chainctl skills uninstall hello-world
```

The command prompts for confirmation before removing any files:

```output
This will remove skill "hello-world" from local agent directories.
Proceed?
Do you want to continue? [y,N]:
Uninstalled skill "hello-world".
```

By default, `uninstall` removes the project-local copy from every agent directory where it's installed. If a global copy also exists, `uninstall` leaves it in place and prints a warning; re-run with `--global` to remove that copy too. Use the `--agent` flag to remove the skill from specific agents only, and the `-y` flag to skip the confirmation prompt.

`uninstall` operates only on the local files on your machine. It doesn't modify your organization's registry. To remove a published skill from the registry, use [`chainctl skills delete`](/platform/chainctl/chainctl-docs/chainctl_skills_delete/) instead.

### Delete a skill from the registry

To remove a published version of a skill from your organization's registry, pass its full reference to the `delete` subcommand. The reference must include an explicit tag:

```shell
chainctl skills delete uploads.cgr.dev/$ORG/hello-world:v1.0.0
```

The command prompts for confirmation before removing the version:

```output
Delete uploads.cgr.dev/example.dev/hello-world:v1.0.0?
Do you want to continue? [y,N]:
```

Press <kbd>y</kbd> and <kbd>ENTER</kbd> to confirm. Add the `-y` flag to skip the prompt and delete the version non-interactively.

The command requires a tag so you don't delete the `latest` tag by accident. Deleting `latest` is still possible, but it prompts for an additional confirmation.

When you delete a skill's last remaining version, `chainctl` removes the now-empty skill entry as well, so it doesn't linger in `list` output with nothing to pull. A tagless reference such as `uploads.cgr.dev/$ORG/hello-world` is valid only for a skill that already has no versions left; a skill that still has versions requires an explicit tag.

Unlike `uninstall`, `delete` removes the skill from the registry for your whole organization. It doesn't remove copies already installed on anyone's machine.

## Command reference

| Action | Command |
| ----- | ----- |
| Enable the entitlement | `chainctl skills entitlements create --parent $ORG` |
| Accept the registry terms | `chainctl skills accept-terms --group $ORG` |
| Validate a skill | `chainctl skills validate <name>` |
| Push a skill | `chainctl skills push <name> --group $ORG --tag <version>` |
| List your org's skills | `chainctl skills list --group $ORG --source uploads` |
| List a skill's versions | `chainctl skills versions uploads.cgr.dev/$ORG/<name>` |
| Describe a skill | `chainctl skills describe uploads.cgr.dev/$ORG/<name>:<version>` |
| Pull a skill to a directory | `chainctl skills pull uploads.cgr.dev/$ORG/<name>:<version> <dir>` |
| Install a skill | `chainctl skills install uploads.cgr.dev/$ORG/<name>:<version>` |
| Uninstall a skill | `chainctl skills uninstall <name>` |
| Delete a published skill | `chainctl skills delete uploads.cgr.dev/$ORG/<name>:<version>` |
