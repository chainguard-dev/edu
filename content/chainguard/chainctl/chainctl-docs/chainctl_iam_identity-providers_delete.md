---
date: 2025-04-08T07:31:16Z
title: "chainctl iam identity-providers delete"
slug: chainctl_iam_identity-providers_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers delete

Delete an identity provider.

```
chainctl iam identity-providers delete IDENTITY_PROVIDER_ID|IDENTITY_PROVIDER_NAME [--yes] [--output=id]
```

### Examples

```
  # Delete an identity provider by ID
  chainctl iam identity-providers delete 9b6da6e64b45129eb4e9f9f3ce9b69ca2a550c6b/034e4afcda8c0b07
  
  # Delete an identity provider by name
  chainctl iam identity-providers delete my-idp
```

### Options

```
  -h, --help   help for delete
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

* [chainctl iam identity-providers](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

