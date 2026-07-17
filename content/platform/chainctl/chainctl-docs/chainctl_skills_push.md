---
date: 2026-07-01T03:32:22Z
title: "chainctl skills push"
slug: chainctl_skills_push
url: /platform/chainctl/chainctl-docs/chainctl_skills_push/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills push

Package a skill directory and publish it to skills.cgr.dev.

### Synopsis

Package a skill directory and publish it to skills.cgr.dev.

Reads SKILL.md from the specified directory (default: current directory),
validates the skill, and pushes an OCI artifact to skills.cgr.dev/<org>/<name>:<tag>.

```
chainctl skills push [<path>] [flags]
```

### Options

```
      --dry-run        Build and validate without pushing.
  -g, --group string   Org or folder to publish under, e.g. "chainguard" or "chainguard/github" (default: current chainctl context).
  -t, --tag string     Version tag to apply. (default "latest")
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

* [chainctl skills](/chainguard/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.

