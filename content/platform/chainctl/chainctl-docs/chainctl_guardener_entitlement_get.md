---
date: 2026-09-04T19:05:48Z
title: "chainctl guardener entitlement get"
slug: chainctl_guardener_entitlement_get
url: /platform/chainctl/chainctl-docs/chainctl_guardener_entitlement_get/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl guardener entitlement get

Show the guardener entitlement for a group.

### Synopsis

Show the guardener entitlement for a group.

The entitlement records the configured repository visibility scope for the
group. This administrative setting does not determine current repository
coverage, which is controlled by the guardener GitHub App's repository
selection. A group with no configured entitlement shows the default public
scope.

Requires the guardener.entitlement.list capability on the group.

```
chainctl guardener entitlement get [flags]
```

### Options

```
      --parent string   Name or UIDP of the Chainguard group. Prompts interactively if omitted.
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

* [chainctl guardener entitlement](/platform/chainctl/chainctl-docs/chainctl_guardener_entitlement/)	 - Manage a group's guardener entitlement.

