---
date: 2026-06-30T03:10:49Z
title: "chainctl policies binding delete"
slug: chainctl_policies_binding_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_binding_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies binding delete

Delete a policy binding.

### Synopsis

Delete a policy binding to deactivate a policy for its bound scope.

Removing a binding disables the policy — image pulls will no longer be
checked against it.

You can pass a binding ID directly as a positional argument, or use
--policy to specify the policy name and --parent to identify the
organization if needed.

```
chainctl policies binding delete [BINDING_ID | --policy POLICY] [--parent ORG] [flags]
```

### Examples

```
  # Delete a binding by ID
  chainctl policies binding delete <binding-id>
  
  # Delete a binding by policy name
  chainctl policies binding delete --policy=no-eol --parent=engineering
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

* [chainctl policies binding](/chainguard/chainctl/chainctl-docs/chainctl_policies_binding/)	 - Manage policy bindings.

