---
date: 2026-06-10T18:28:08Z
title: "chainctl skills uninstall"
slug: chainctl_skills_uninstall
url: /chainguard/chainctl/chainctl-docs/chainctl_skills_uninstall/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills uninstall

Remove a skill from agent directories on the local machine.

### Synopsis

Remove a skill from agent directories on the local machine.

<name> is the skill name (no org or tag needed — operates on local files only).

uninstall is a local-only operation and does not modify the registry.

```
chainctl skills uninstall <name> [flags]
```

### Options

```
  -a, --agent stringArray   Remove from specific agents only (default: all installed locations).
      --global              Remove from global directories instead of project-local.
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

* [chainctl skills](/chainguard/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.

