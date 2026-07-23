---
date: 2026-07-22T19:49:10Z
title: "chainctl policies override delete"
slug: chainctl_policies_override_delete
url: /platform/chainctl/chainctl-docs/chainctl_policies_override_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies override delete

Delete a policy override.

### Synopsis

Delete a policy override to revoke a waiver.

Once deleted, the targeted artifact is again subject to the policy's
result. Pass the override ID as a positional argument; use
"chainctl policies override list" to find it.

```
chainctl policies override delete OVERRIDE_ID [flags]
```

### Examples

```
  # Delete an override by ID
  chainctl policies override delete <override-id>
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

* [chainctl policies override](/platform/chainctl/chainctl-docs/chainctl_policies_override/)	 - Manage policy overrides.

