---
date: 2025-04-14T14:32:57Z
title: "chainctl iam identity-providers"
slug: chainctl_iam_identity-providers
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers

customer managed identity provider management

### Options

```
  -h, --help   help for identity-providers
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

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam identity-providers create](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_create/)	 - Create an identity provider
* [chainctl iam identity-providers delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_delete/)	 - Delete an identity provider.
* [chainctl iam identity-providers list](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_list/)	 - List identity providers.
* [chainctl iam identity-providers update](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_update/)	 - Update an identity provider

