---
date: 2026-06-10T18:28:08Z
title: "chainctl policies list"
slug: chainctl_policies_list
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies list

List policies.

### Synopsis

List the policies available for an organization.

Each available policy is shown with its name and description.

```
chainctl policies list [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json|table] [flags]
```

### Examples

```

# List all policies for an organization
chainctl policies list --parent=example.com

# List policies using interactive organization selection
chainctl policies list

# List policies in JSON format
chainctl policies list --parent=example.com -o json

```

### Options

```
      --parent string   The name or id of the organization.
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

