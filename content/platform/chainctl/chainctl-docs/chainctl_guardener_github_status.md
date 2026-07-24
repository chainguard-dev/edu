---
date: 2026-07-23T16:28:17Z
title: "chainctl guardener github status"
slug: chainctl_guardener_github_status
url: /platform/chainctl/chainctl-docs/chainctl_guardener_github_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener github status

List the GitHub organizations linked to a Chainguard group.

### Synopsis

List the GitHub organizations linked to a Chainguard group.

Requires the guardener.association.list capability on the group (read-only; no
GitHub authorization or browser flow is involved). When --group is omitted, you
are prompted to pick from your groups.

```
chainctl guardener github status [flags]
```

### Options

```
      --group string   Name or UIDP of the Chainguard group to list. Prompts interactively if omitted.
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

* [chainctl guardener github](/platform/chainctl/chainctl-docs/chainctl_guardener_github/)	 - Link and unlink a GitHub organization to a Chainguard group.

