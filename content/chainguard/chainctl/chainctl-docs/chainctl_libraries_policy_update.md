---
date: 2026-06-19T17:44:19Z
title: "chainctl libraries policy update"
slug: chainctl_libraries_policy_update
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy update

Update a custom Libraries policy.

```
chainctl libraries policy update POLICY [--cooldown-days N] [--block ...] [--allow ...] [flags]
```

### Options

```
      --allow stringArray     An allow-list entry, formatted as comma-separated key=value pairs. Repeatable.
      --block stringArray     A block-list entry, formatted as comma-separated key=value pairs. Repeatable.
      --cooldown-days int32   The cooldown window in days (0 disables, 1-30 explicit, omit to inherit the default). (default -1)
      --description string    The updated description of the policy.
      --parent string         The name or id of the organization that owns the policy.
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

* [chainctl libraries policy](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy/)	 - Manage Libraries policies.

