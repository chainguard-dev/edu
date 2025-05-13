---
date: 2025-05-12T21:16:51Z
title: "chainctl iam account-associations set"
slug: chainctl_iam_account-associations_set
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations set

Set cloud provider account associations for a location.

### Options

```
  -h, --help   help for set
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

* [chainctl iam account-associations](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations/)	 - Configure and manage cloud provider account associations.
* [chainctl iam account-associations set aws](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set_aws/)	 - Set AWS account association for a location.
* [chainctl iam account-associations set gcp](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set_gcp/)	 - Set GCP account association for a location.

