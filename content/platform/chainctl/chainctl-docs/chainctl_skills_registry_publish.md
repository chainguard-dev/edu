---
date: 2026-10-08T18:22:10Z
title: "chainctl skills registry publish"
slug: chainctl_skills_registry_publish
url: /platform/chainctl/chainctl-docs/chainctl_skills_registry_publish/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills registry publish

Package a skill directory and publish it to an OCI reference.

### Synopsis

Package a skill directory and publish it to an OCI reference.

Reads and validates SKILL.md from the skill directory (default: current
directory, or --dir), packs it as a skill artifact, and publishes it to <ref>.
Prints the published reference by digest.

```
chainctl skills registry publish <ref> [flags]
```

### Examples

```

# Publish the skill in the current directory:
chainctl skills registry publish cgr.dev/my-org/my-skill:v1

# Publish the skill in another directory:
chainctl skills registry publish --dir ./my-skill cgr.dev/my-org/my-skill:v1
```

### Options

```
      --dir string   Skill directory to package (must contain SKILL.md). (default ".")
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

