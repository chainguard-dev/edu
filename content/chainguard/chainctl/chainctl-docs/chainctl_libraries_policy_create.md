---
date: 2026-06-16T00:04:16Z
title: "chainctl libraries policy create"
slug: chainctl_libraries_policy_create
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy create

Create a custom Libraries policy.

```
chainctl libraries policy create --name NAME [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--cooldown-days N] [--block ...] [--allow ...] [flags]
```

### Examples

```
  # Create a policy with a cooldown window and a blocked package
  chainctl libraries policy create --name=trusted --parent=example.com \
  --cooldown-days=14 --block=purl=pkg:pypi/evil
  
  # Allow a package to bypass the malware gate (justification required)
  chainctl libraries policy create --name=trusted --parent=example.com \
  --allow=purl=pkg:pypi/requests,bypass-malware=true,justification="vetted internally"
```

### Options

```
      --allow stringArray     An allow-list entry, formatted as comma-separated key=value pairs (e.g. purl=pkg:pypi/requests,bypass-cooldown=true,bypass-malware=true,justification="..."). Repeatable.
      --block stringArray     A block-list entry, formatted as comma-separated key=value pairs (e.g. purl=pkg:pypi/requests). Repeatable.
      --cooldown-days int32   The cooldown window in days (0 disables, 1-30 explicit, omit to inherit the default). (default -1)
      --description string    The description of the policy.
      --name string           The name of the policy.
      --parent string         The name or id of the organization to scope the policy to.
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

