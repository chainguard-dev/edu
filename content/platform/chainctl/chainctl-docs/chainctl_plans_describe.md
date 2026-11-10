---
date: 2026-11-09T19:57:31Z
title: "chainctl plans describe"
slug: chainctl_plans_describe
url: /platform/chainctl/chainctl-docs/chainctl_plans_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl plans describe

Show the plan, product access, and quotas near their limits.

### Synopsis

Show the plan, product access, and quotas near their limits.

Exits with status 1 if any product's usage is unavailable.

```
chainctl plans describe [--parent ORG] [--output=json|table] [flags]
```

### Options

```
      --parent string   Name, path, or UIDP of the organization or one of its folders.
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

* [chainctl plans](/platform/chainctl/chainctl-docs/chainctl_plans/)	 - Show your organization's plan, limits, and usage.

