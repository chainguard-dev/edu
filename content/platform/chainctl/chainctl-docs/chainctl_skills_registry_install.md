---
date: 2026-10-09T15:36:02Z
title: "chainctl skills registry install"
slug: chainctl_skills_registry_install
url: /platform/chainctl/chainctl-docs/chainctl_skills_registry_install/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills registry install

Install the skill at an OCI reference into agent directories.

### Synopsis

Install the skill at an OCI reference into agent directories.

The artifact must be a skill (as published by "chainctl skills push" or
"chainctl skills registry publish"). Like "chainctl skills install", a shared
canonical copy is written under .agents/skills/ and agent-specific symlinks
are created; use --copy to write independent copies.

The installed directory is named for the last segment of the repository path
(e.g. my-skill for skills.cgr.dev/chainguard/my-folder/my-skill); use --name
to choose another.
The install is recorded in the skills CLI lock file (skills-lock.json in the
working directory, or ~/.agents/.skill-lock.json with --global) with the
repository, tag, and image digest it came from. Installing fails if the lock
records that name from a different source.

The skill's signature is checked, as by "chainctl skills verify", before
anything is written; installing fails if it doesn't pass. Only skills on
skills.cgr.dev can be verified, so installing from any other registry requires
--no-verify.

The install locations are shown for confirmation before anything is
downloaded; pass --yes to skip the prompt.

```
chainctl skills registry install <ref> [flags]
```

### Examples

```

# Install into the detected agents' project directories:
chainctl skills registry install \
  skills.cgr.dev/chainguard/my-folder/my-skill

# Install globally for Claude Code only:
chainctl skills registry install --global --agent claude-code \
  skills.cgr.dev/chainguard/my-folder/my-skill

# Install under a different name:
chainctl skills registry install --name team-skill \
  skills.cgr.dev/chainguard/my-folder/my-skill

# Install from a registry chainctl can't verify signatures on:
chainctl skills registry install --no-verify cgr.dev/my-org/my-skill:v1

# Install without confirming the locations:
chainctl skills registry install --yes \
  skills.cgr.dev/chainguard/my-folder/my-skill
```

### Options

```
  -a, --agent stringArray   Target specific agents by ID (repeatable). Use --agent '*' for all known agents.
      --copy                Copy files per agent instead of using a shared canonical copy + symlinks.
      --global              Install to global (~/) directories instead of project-local.
      --name string         Name to install the skill under (default: the last segment of the repository path).
      --no-verify           Install without checking the skill's signature. Required for registries chainctl can't verify, which is any but skills.cgr.dev.
  -y, --yes                 Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl skills registry](/platform/chainctl/chainctl-docs/chainctl_skills_registry/)	 - Publish and install skills in any OCI registry by reference.

