---
date: 2026-10-08T18:22:10Z
title: "chainctl skills registry"
slug: chainctl_skills_registry
url: /platform/chainctl/chainctl-docs/chainctl_skills_registry/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills registry

Publish and install skills in any OCI registry by reference.

### Synopsis

Publish and install skills in any OCI registry by reference.

These commands address skills by full OCI reference
(e.g. cgr.dev/my-org/my-skill:v1) rather than by Chainguard org path.
Skills are packed in the same artifact format as "chainctl skills push".

Registries authenticate with your docker credentials (~/.docker/config.json).
For Chainguard registries, run "chainctl auth configure-docker" first.

A skill is an ordinary OCI artifact, so crane handles everything else: list
tags, copy, tag, or read the manifest and config. A skill's files are a single
tar layer, which "crane export" writes as-is.

### Examples

```

# Install a Chainguard skill (its signature is verified):
chainctl skills registry install \
  skills.cgr.dev/chainguard/my-folder/my-skill

# Publish the skill in the current directory, then install it. Your own
# skills aren't Chainguard-signed, so installing them needs --no-verify:
chainctl skills registry publish cgr.dev/my-org/my-skill:v1
chainctl skills registry install --no-verify cgr.dev/my-org/my-skill:v1

# Inspect a skill's files without installing it:
crane export cgr.dev/my-org/my-skill:v1 - | tar -tf -
crane export cgr.dev/my-org/my-skill:v1 - | tar -xOf - SKILL.md
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

* [chainctl skills](/platform/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.
* [chainctl skills registry install](/platform/chainctl/chainctl-docs/chainctl_skills_registry_install/)	 - Install the skill at an OCI reference into agent directories.
* [chainctl skills registry publish](/platform/chainctl/chainctl-docs/chainctl_skills_registry_publish/)	 - Package a skill directory and publish it to an OCI reference.

