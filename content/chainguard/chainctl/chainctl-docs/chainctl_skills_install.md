---
date: 2026-05-22T22:52:04Z
title: "chainctl skills install"
slug: chainctl_skills_install
url: /chainguard/chainctl/chainctl-docs/chainctl_skills_install/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills install

Download a skill and install it into agent directories.

### Synopsis

Download a skill and place it into the skills directories of detected agents.

By default, a shared canonical copy is written to .agents/skills/<name>/ and
agent-specific symlinks are created. Use --copy to write independent copies.

```
chainctl skills install <ref> [flags]
```

### Options

```
  -a, --agent stringArray   Target specific agents by ID (repeatable). Use --agent '*' for all known agents.
      --copy                Copy files per agent instead of using a shared canonical copy + symlinks.
      --global              Install to global (~/) directories instead of project-local.
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

