---
date: 2026-08-27T20:49:25Z
title: "chainctl policies binding list"
slug: chainctl_policies_binding_list
url: /platform/chainctl/chainctl-docs/chainctl_policies_binding_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies binding list

List policy bindings.

### Synopsis

List active policy bindings to see which policies are enabled and
in which mode.

Bindings are scoped to one organization: pass --parent, or omit it to
use your configured default group, or (with no default configured) the
single organization you can access — you are prompted when several are
available. Each binding shows the policy it activates and the
enforcement mode (enforced or dry-run).

Each binding's parameters are cross-checked against the referenced
policy's current parameters. The STATUS column reports OK,
INVALID (parameters no longer satisfy the schema), or UNKNOWN.
Rows flagged INVALID are elaborated below the table with the
concrete reasons; the JSON output carries the same detail when at
least one binding is invalidated.

```
chainctl policies binding list [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json|table] [flags]
```

### Examples

```
  # List bindings for your default (or only) organization
  chainctl policies binding list
  
  # List bindings for a specific organization
  chainctl policies binding list --parent=engineering
```

### Options

```
      --parent string          The name or id of the organization to list bindings for.
      --resource-type string   Only list entries for this resource type (shorthand: Repo, Python, Java, Javascript; or a full type).
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

* [chainctl policies binding](/platform/chainctl/chainctl-docs/chainctl_policies_binding/)	 - Manage policy bindings.

