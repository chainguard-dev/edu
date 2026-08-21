---
date: 2026-08-20T20:16:23Z
title: "chainctl iam identity-providers group-mappings"
slug: chainctl_iam_identity-providers_group-mappings
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_group-mappings/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers group-mappings

Manage IdP group-to-role mappings for an identity provider.

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
* [chainctl iam identity-providers group-mappings create](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_group-mappings_create/)	 - Create an IdP group-to-role mapping.
* [chainctl iam identity-providers group-mappings delete](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_group-mappings_delete/)	 - Delete an identity provider's group-to-role mappings.
* [chainctl iam identity-providers group-mappings list](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_group-mappings_list/)	 - List an identity provider's group-to-role mappings.

