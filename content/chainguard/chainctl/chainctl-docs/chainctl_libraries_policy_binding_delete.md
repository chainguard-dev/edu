---
date: 2026-06-23T17:19:36Z
title: "chainctl libraries policy binding delete"
slug: chainctl_libraries_policy_binding_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_binding_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy binding delete

Delete a Libraries policy binding.

### Synopsis

Delete a Libraries policy binding to deactivate the policy for its bound (organization, ecosystem) pair.

```
chainctl libraries policy binding delete BINDING_ID [flags]
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

