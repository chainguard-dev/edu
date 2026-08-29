---
date: 2026-08-28T20:13:14Z
title: "chainctl iam identity-providers list"
slug: chainctl_iam_identity-providers_list
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers list

List identity providers.

```
chainctl iam identity-providers list [--parent ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID] [--recursive] [--output=json|table|tree]
```

### Examples

```
  # List identity providers
  chainctl iam identity-providers list
  
  # Filter list by location
  chainctl iam identity-providers list --parent=my-org
  
  # List only identity providers directly in an organization, excluding nested locations
  chainctl iam identity-providers list --parent=my-org --recursive=false
```

### Options

```
      --parent string   List identity providers from this location. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --recursive       List identity providers from the parent location and all nested locations. Set to false to list only the parent location. (default true)
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

* [chainctl iam identity-providers](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

