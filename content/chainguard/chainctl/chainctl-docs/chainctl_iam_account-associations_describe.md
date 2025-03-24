---
date: 2025-03-21T17:51:11Z
title: "chainctl iam account-associations describe"
slug: chainctl_iam_account-associations_describe
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations describe

Describe cloud provider account associations for a location.

```
chainctl iam account-associations describe ORGANIZATION_NAME|ORGANIZATION_ID|FOLDER_NAME|FOLDER_ID [--aws] [--gcp] [--chainguard] [--output=id|json|table] [flags]
```

### Options

```
      --aws          Include the AWS account association.
      --chainguard   Include the Chainguard service principal account association.
      --gcp          Include the GCP account association.
  -h, --help         help for describe
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
  -o, --output string      Output format. One of: [csv, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam account-associations](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations/)	 - Configure and manage cloud provider account associations.

