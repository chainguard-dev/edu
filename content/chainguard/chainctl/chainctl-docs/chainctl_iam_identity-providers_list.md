---
date: 2025-02-19T23:30:24Z
title: "chainctl iam identity-providers list"
slug: chainctl_iam_identity-providers_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers list

List identity providers.

```
chainctl iam identity-providers list [--parent ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID] [--output=json|table|tree]
```

### Examples

```
  # List identity providers
  chainctl iam identity-providers list
  
  # Filter list by location
  chainctl iam identity-providers list --parent=my-org
```

### Options

```
  -h, --help            help for list
      --parent string   List identity providers in this location and its descendants.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, , json, id, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identity-providers](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

