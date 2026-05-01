---
date: 2026-04-30T18:48:24Z
title: "chainctl agent accept-terms"
slug: chainctl_agent_accept-terms
url: /chainguard/chainctl/chainctl-docs/chainctl_agent_accept-terms/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl agent accept-terms

Accept required legal terms.

### Synopsis

Presents the legal agreement prompt for the given group.

```
chainctl agent accept-terms [flags]
```

### Options

```
      --group string   UIDP of the group to accept terms for
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

* [chainctl agent](/chainguard/chainctl/chainctl-docs/chainctl_agent/)	 - Agent-powered commands.

