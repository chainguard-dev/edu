---
date: 2026-11-02T19:27:54Z
title: "chainctl plans"
slug: chainctl_plans
url: /platform/chainctl/chainctl-docs/chainctl_plans/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl plans

Show your organization's plan, limits, and usage.

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

* [chainctl](/platform/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl plans describe](/platform/chainctl/chainctl-docs/chainctl_plans_describe/)	 - Show the plan, product access, and quotas near their limits.
* [chainctl plans quotas](/platform/chainctl/chainctl-docs/chainctl_plans_quotas/)	 - Show plan limits and current usage.

