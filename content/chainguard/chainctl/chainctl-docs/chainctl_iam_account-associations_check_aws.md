---
date: 2025-04-15T16:06:39Z
title: "chainctl iam account-associations check aws"
slug: chainctl_iam_account-associations_check_aws
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check_aws/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations check aws

Checks that the given location has been properly configured for OIDC federation with AWS

```
chainctl iam account-associations check aws ORGANIZATION_NAME|ORGANIZATION_ID|FOLDER_NAME|FOLDER_ID [flags]
```

### Options

```
  -h, --help   help for aws
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
  -o, --output string      Output format. One of: [csv, env, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam account-associations check](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check/)	 - Check the OIDC federation configurations for cloud providers.

