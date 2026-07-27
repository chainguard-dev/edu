---
date: 2026-07-23T16:28:17Z
title: "chainctl iam identity-providers scim enable"
slug: chainctl_iam_identity-providers_scim_enable
url: /platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim_enable/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers scim enable

Enable SCIM provisioning for an identity provider.

```
chainctl iam identity-providers scim enable IDENTITY_PROVIDER [flags]
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

* [chainctl iam identity-providers scim](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_scim/)	 - Manage SCIM provisioning for an identity provider.

