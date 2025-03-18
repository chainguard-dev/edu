---
date: 2025-03-17T21:27:26Z
title: "chainctl iam account-associations unset aws"
slug: chainctl_iam_account-associations_unset_aws
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_unset_aws/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations unset aws

Remove AWS account configuration for a location.

```
chainctl iam account-associations unset aws ORGANIZATION_NAME|ORGANIZATION_ID|FOLDER_NAME|FOLDER_ID [--yes] [flags]
```

### Options

```
  -h, --help   help for aws
  -y, --yes    Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam account-associations unset](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_unset/)	 - Remove cloud provider account associations from a location.

