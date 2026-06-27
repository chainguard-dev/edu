---
date: 2026-06-26T20:33:43Z
title: "chainctl libraries policy binding list"
slug: chainctl_libraries_policy_binding_list
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_binding_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy binding list

List Libraries policy bindings.

### Synopsis

List active Libraries policy bindings to see which policies are enabled and in which mode.

```
chainctl libraries policy binding list [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json|table] [flags]
```

### Options

```
      --parent string   The name or id of the organization to list bindings for.
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

* [chainctl libraries policy binding](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_binding/)	 - Manage Libraries policy bindings.

