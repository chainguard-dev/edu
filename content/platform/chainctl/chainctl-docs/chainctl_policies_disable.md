---
date: 2026-07-22T19:49:10Z
title: "chainctl policies disable"
slug: chainctl_policies_disable
url: /platform/chainctl/chainctl-docs/chainctl_policies_disable/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies disable

Disable a policy.

### Synopsis

Disable a policy by deleting its binding.

This is a shortcut for "policies binding delete".


```
chainctl policies disable --policy POLICY [--parent ORG] [flags]
```

### Examples

```

# Disable a policy by name
chainctl policies disable --policy=no-eol --parent=example.com

```

### Options

```
      --parent string   The name or id of the organization (required when deleting by policy).
      --policy string   The name or id of the policy to disable.
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

* [chainctl policies](/platform/chainctl/chainctl-docs/chainctl_policies/)	 - Manage policies.

