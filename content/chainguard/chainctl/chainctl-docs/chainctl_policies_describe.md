---
date: 2026-06-26T20:33:43Z
title: "chainctl policies describe"
slug: chainctl_policies_describe
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies describe

Describe a policy and its parameter schema.

### Synopsis

Show the full definition of a policy: its description, type, and the set
of configurable parameters it accepts. The output includes a copyable
example invocation suitable for `chainctl policies enable`.

Use this command to discover what's configurable on a system policy
before enabling it for your organization.

```
chainctl policies describe --policy POLICY [--parent ORG] [--output=json|table] [flags]
```

### Examples

```

# Describe the cooldown policy
chainctl policies describe --policy=cooldown --parent=example.com

# JSON output (useful for scripts that need the full schema)
chainctl policies describe --policy=cooldown --parent=example.com -o json

```

### Options

```
      --parent string   The name or id of the organization to scope the lookup to.
      --policy string   The name or UIDP of the policy to describe.
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

* [chainctl policies](/chainguard/chainctl/chainctl-docs/chainctl_policies/)	 - Manage policies.

