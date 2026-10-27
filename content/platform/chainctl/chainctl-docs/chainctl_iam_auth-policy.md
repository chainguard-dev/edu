---
date: 2026-10-26T19:49:34Z
title: "chainctl iam auth-policy"
slug: chainctl_iam_auth-policy
url: /platform/chainctl/chainctl-docs/chainctl_iam_auth-policy/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam auth-policy

Manage an organization's authentication policy (which sign-in methods its members may use).

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

* [chainctl iam](/platform/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam auth-policy describe](/platform/chainctl/chainctl-docs/chainctl_iam_auth-policy_describe/)	 - Describe an organization's authentication policy.
* [chainctl iam auth-policy update](/platform/chainctl/chainctl-docs/chainctl_iam_auth-policy_update/)	 - Update an organization's authentication policy.

