---
title: "Getting started with the Chainguard Skills Registry"
linktitle: "Skills Registry"
description: "Enable the Chainguard Skills Registry, then upload, harden, install, and run an agent skill scoped to your organization."
type: "article"
date: 2026-06-05T08:48:45+00:00
lastmod: 2026-09-22
draft: false
tags: ["Agent Skills", "Overview"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 002
---

The Chainguard Skills Registry lets you publish, manage, and distribute skills scoped to your organization. Use `chainctl` to upload original skills to `uploads.cgr.dev`, submit them for hardening, and install the hardened results from `skills.cgr.dev`.

This guide walks through enabling the registry for your organization, then uploading, hardening, installing, and running a skill. For job tracking, digest-based submissions, and browsing user folders, see [Getting started with skill hardening](/chainguard/agent-skills/skill-hardening/).

{{< beta feature="Chainguard Skills Registry" >}}

## Prerequisites

To follow this guide, you need:

* An installed and authenticated `chainctl` that includes `skills harden` and `skills status`. Check with `chainctl skills harden --help` and `chainctl skills status --help`. Refer to [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.
* An active Chainguard organization.
* Owner access on the organization.

The examples in this guide use an `$ORG` environment variable to refer to your organization. Set it to the name of your organization before you begin:

```shell
export ORG='your-organization'
```

## Enabling the skills entitlement

Before your org can push or install skills, create a skills entitlement.

> **Note**: You must have the `owner` role in your organization to create a skills entitlement and accept the Skills Registry terms of service.

```shell
chainctl skills entitlements create --parent "$ORG"
```

```output
Created skills entitlement for org example.dev (717b474ac6972745c5706a898aa6e67ffba97dad)
```

Next, accept the Skills Registry terms of service for your org:

```shell
chainctl skills accept-terms --group "$ORG"
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

After running this command, your directory will have the following structure:

```
hello-world/
└── SKILL.md
```

The directory name (`hello-world/`) must match the `name` field in the frontmatter (`name: hello-world`). If they don't match, the skill will fail to push.

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

### Push the skill to your organization's uploads registry

From the parent directory of `hello-world/`, push the skill to your organization's uploads registry with a version tag:

```shell
chainctl skills push hello-world --group "$ORG" --tag v1.0.0
```

```output
            REFERENCE             |        DIGEST
----------------------------------|------------------------
 uploads.cgr.dev/example.dev/hello-world:v1.0.0 | sha256:3196...
```

Keep the versioned reference for the hardening submission below.

### List your uploads

Confirm the upload with the `list` subcommand and `--source uploads`:

```shell
chainctl skills list --group "$ORG" --source uploads
```

```output
     SOURCE      | TYPE  |    NAME     |  TAGS  | UPDATED
-----------------|-------|-------------|--------|----------
 uploads.cgr.dev | skill | hello-world | v1.0.0 | just now
```

Without `--source uploads`, `list` shows the hardened registry. A successful push does not mean a hardened result is available there. Submit the upload for hardening in the next step.

The `TAGS` column shows all tags for each skill. A `latest` tag is not required. If your output has a `LATEST TAG` column or omits the upload, see [Find a skill that is missing from the listing](/chainguard/agent-skills/skill-hardening/#find-a-skill-that-is-missing-from-the-listing).

### Harden the skill

Submit the uploaded artifact and wait for the result:

```shell
chainctl skills harden "uploads.cgr.dev/$ORG/hello-world:v1.0.0" \
  --group "$ORG" --wait --timeout 30m
```

The command prints a job ID, waits for hardening, and downloads the result to `./hardened/hello-world/`. Review the instructions and `HARDENING.md` report, including any findings that remain open.

Save the exact hardened reference returned by the command. It includes a user namespace and digest, in the form `skills.cgr.dev/<org-uidp>/users/<user-namespace>/hello-world@sha256:<digest>`:

```shell
export HARDENED_REF='<full-hardened-reference-returned-by-the-command>'
chainctl skills describe "$HARDENED_REF"
```

For submissions directly from a local directory, checking a job later, and resuming after a timeout, see [Getting started with skill hardening](/chainguard/agent-skills/skill-hardening/).

### List hardened skills

Hardened results are nested under `users/<user-namespace>/`. Add `--recursive` to browse skills inside those folders:

```shell
chainctl skills list --group "$ORG" --source skills --recursive
```

Without `--recursive`, the organization-level listing may show only a `users` row with `TYPE` set to `folder`. Expand the folder with `--recursive`, or browse it with `chainctl skills list --group "$ORG/users"`. See [Browse results in user folders](/chainguard/agent-skills/skill-hardening/#browse-results-in-user-folders) for the folder layout and how to show uploads alongside hardened results.

The listing includes skills with generated version tags and skills without tags. Use the exact `$HARDENED_REF` returned by the job to inspect and install the result you reviewed.

### Install the skill

Download and install the skill to make it available to agents on your machine:

```shell
chainctl skills install "$HARDENED_REF"
```

This command automatically detects agents on your machine and reports where it placed the skill. The install name includes the registry namespace to distinguish skills with the same name. Copy the **Install Name** from `chainctl skills describe "$HARDENED_REF"` for use in the following steps:

```shell
export INSTALLED_SKILL='<install-name-from-describe>'
```

### Run the skill from an agent

Load the skill from the location reported by `install`. In Claude Code, invoke it with `/<installed-skill-name>`, replacing `<installed-skill-name>` with the value you saved in `$INSTALLED_SKILL`. Ask the agent to greet you, and check that its response follows the instructions you reviewed in the hardened `SKILL.md`.

### Uninstall the skill

To remove a skill from your machine, pass its install name to the `uninstall` subcommand:

```shell
chainctl skills uninstall "$INSTALLED_SKILL"
```

The command prompts for confirmation before removing any files.

By default, `uninstall` removes the skill from every agent directory where it's installed. Use the `--agent` flag to remove it from specific agents only, or the `--global` flag to remove it from global directories instead of the current project. Add the `-y` flag to skip the confirmation prompt.

`uninstall` operates only on the local files on your machine. It doesn't modify your organization's registry. To remove a published skill from the registry, use [`chainctl skills delete`](/platform/chainctl/chainctl-docs/chainctl_skills_delete/) instead.

### Delete a skill from the registry

To remove a published version of a skill from your organization's hardened registry, first list its tags. Use the repository portion of the hardened reference, preserving its user namespace:

```shell
HARDENED_REPO="${HARDENED_REF%@*}"
chainctl skills versions "$HARDENED_REPO"
```

Select a tag from that output and pass the full tagged reference to `delete`. The upload's `v1.0.0` tag is not a substitute for a tag from the hardened repository. Digest references are not accepted by `delete`:

```shell
export HARDENED_TAG='<tag-from-the-versions-output>'
chainctl skills delete "$HARDENED_REPO:$HARDENED_TAG"
```

The command prompts for confirmation before removing the version. Press <kbd>y</kbd> and <kbd>ENTER</kbd> to confirm. Add the `-y` flag to skip the prompt and delete the version non-interactively.

The command requires a tag so you don't delete the `latest` tag by accident. Deleting `latest` is still possible, but it prompts for an additional confirmation.

Unlike `uninstall`, `delete` removes the skill from the registry for your whole organization. It doesn't remove copies already installed on anyone's machine.

## Command reference

| Action | Command |
| ----- | ----- |
| Enable the entitlement | `chainctl skills entitlements create --parent "$ORG"` |
| Accept the registry terms | `chainctl skills accept-terms --group "$ORG"` |
| Validate a skill | `chainctl skills validate <name>` |
| Upload a skill | `chainctl skills push <name> --group "$ORG" --tag <version>` |
| List uploads | `chainctl skills list --group "$ORG" --source uploads` |
| Harden a local skill | `chainctl skills harden ./<name> --group "$ORG" --wait` |
| Check a hardening job | `chainctl skills status --group "$ORG" --id "$JOB_ID"` |
| List hardened skills in all folders | `chainctl skills list --group "$ORG" --recursive` |
| Describe a hardened skill | `chainctl skills describe "$HARDENED_REF"` |
| Install a hardened skill | `chainctl skills install "$HARDENED_REF"` |
| Uninstall a skill | `chainctl skills uninstall "$INSTALLED_SKILL"` |
| Delete a published version | `chainctl skills delete "$HARDENED_REPO:$HARDENED_TAG"` |
