---
date: 2026-06-12T17:28:47Z
title: "chainctl iam external-group-role-mappings delete"
slug: chainctl_iam_external-group-role-mappings_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_external-group-role-mappings_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam external-group-role-mappings delete

Delete an IdP group-to-role mapping.

```
chainctl iam external-group-role-mappings delete MAPPING_ID [--yes] [flags]
```

### Examples

```
  # Delete a group mapping by ID
  chainctl iam external-group-role-mappings delete MAPPING_UIDP
```

### Options

```
  -y, --yes   Skip confirmation prompt
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

* [chainctl iam external-group-role-mappings](/chainguard/chainctl/chainctl-docs/chainctl_iam_external-group-role-mappings/)	 - Manage IdP group-to-role mappings.

