---
date: 2026-07-23T16:28:18Z
title: "chainctl policies decision"
slug: chainctl_policies_decision
url: /platform/chainctl/chainctl-docs/chainctl_policies_decision/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies decision

Inspect policy decisions.

### Synopsis

A policy decision records the outcome of evaluating one policy
against one image digest at pull time. Decisions are recorded for both
enforced and dry-run policies, so you can review what a policy blocked,
or would have blocked, before promoting it to enforce mode.

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

* [chainctl policies](/platform/chainctl/chainctl-docs/chainctl_policies/)	 - Manage policies.
* [chainctl policies decision list](/platform/chainctl/chainctl-docs/chainctl_policies_decision_list/)	 - List policy decisions.

