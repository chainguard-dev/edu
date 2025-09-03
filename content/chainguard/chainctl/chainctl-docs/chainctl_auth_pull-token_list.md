---
date: 2025-09-02T09:39:16Z
title: "chainctl auth pull-token list"
slug: chainctl_auth_pull-token_list
url: /chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth pull-token list

List all pull-tokens

```
chainctl auth pull-token list [--parent=PARENT] [--library-ecosystem=LANGUAGE] [--expired=true|false] [flags]
```

### Examples

```
  # List all pull tokens.
  chainctl auth pull-token list
  
  # List all pull tokens associated with the Java library ecosystem.
  chainctl auth pull-token list --library-ecosystem=java
  
  # List expired pull tokens.
  chainctl auth pull-token list --expired
  
  # List pull tokens associated to a particular organization.
  chainctl auth pull-token list --parent=my-org
  
  # List all expired pull tokens associated with the Python library ecosystem.
  chainctl auth pull-token list --library-ecosystem=python --expired
```

### Options

```
      --expired                    If true return only expired pull tokens.
  -h, --help                       help for list
      --library-ecosystem string   The language ecosystem with which the pull-token identity is associated.
      --parent string              The IAM organization or folder with which the pull-token identity is associated.
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
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl auth pull-token](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/)	 - Create a pull token.

