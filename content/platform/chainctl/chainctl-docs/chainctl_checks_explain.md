---
date: 2026-10-26T19:49:34Z
title: "chainctl checks explain"
slug: chainctl_checks_explain
url: /platform/chainctl/chainctl-docs/chainctl_checks_explain/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks explain

Print a repository's resolved checks configuration offline.

### Synopsis

Parse a repository's authored checks configuration (.chainguard/ci/, or the v1 .chainguard/*.yaml layout) the way the planner reads a pull request's, and print its resolved form: every check with its expanded steps, its environment and its resource class. No VM, network or API call is made.

DIR is the repository's root; with none, the top-level directory of the checkout the current directory is in.

When the configuration is refused, every problem is printed with its file and position, and the command exits non-zero. With --output json the resolved workflow.v1 Workflow is printed instead, or the problems when it is refused.

Check names, commands and other text come from the repository: on a terminal they are sanitized unless --raw is given.

```
chainctl checks explain [DIR] [--raw] [--output=json]
```

### Examples

```
  # This checkout's resolved checks
  chainctl checks explain

  # Another repository's, as a workflow.v1 Workflow
  chainctl checks explain ../app -o json
```

### Options

```
      --raw   Write the repository's and the guest's text as raw bytes, escape sequences included, even to a terminal. Output that is not a terminal is always raw.
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

* [chainctl checks](/platform/chainctl/chainctl-docs/chainctl_checks/)	 - Inspect and manage a repository's Checks on the Chainguard sandbox plane.

