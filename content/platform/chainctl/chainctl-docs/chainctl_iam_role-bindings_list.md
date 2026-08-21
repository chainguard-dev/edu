---
date: 2026-08-20T20:16:23Z
title: "chainctl iam role-bindings list"
slug: chainctl_iam_role-bindings_list
url: /platform/chainctl/chainctl-docs/chainctl_iam_role-bindings_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam role-bindings list

List role-bindings.

```
chainctl iam role-bindings list [--parent ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID] [--recursive] [--output=json|table|tree]
```

### Examples

```
  # List role-bindings
  chainctl iam role-bindings list
  
  # Filter role-bindings by organization
  chainctl iam role-bindings list --parent=my-org
  
  # List only role-bindings directly in an organization, excluding nested locations
  chainctl iam role-bindings list --parent=my-org --recursive=false
```

### Options

```
      --parent string   List role-bindings from this location. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --recursive       List role-bindings from the parent location and all nested locations. Set to false to list only the parent location. (default true)
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

* [chainctl iam role-bindings](/platform/chainctl/chainctl-docs/chainctl_iam_role-bindings/)	 - IAM role-bindings resource interactions.

