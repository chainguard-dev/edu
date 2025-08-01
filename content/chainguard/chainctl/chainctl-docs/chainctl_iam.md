---
date: 2025-08-01T17:33:38Z
title: "chainctl iam"
slug: chainctl_iam
url: /chainguard/chainctl/chainctl-docs/chainctl_iam/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam

IAM related commands for the Chainguard platform.

### Options

```
  -h, --help   help for iam
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

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl iam account-associations](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations/)	 - Configure and manage cloud provider account associations.
* [chainctl iam folders](/chainguard/chainctl/chainctl-docs/chainctl_iam_folders/)	 - IAM folders interactions.
* [chainctl iam identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/)	 - Identity management.
* [chainctl iam identity-providers](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management
* [chainctl iam invites](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites/)	 - Manage invite codes that register identities with Chainguard.
* [chainctl iam organizations](/chainguard/chainctl/chainctl-docs/chainctl_iam_organizations/)	 - IAM organization interactions.
* [chainctl iam role-bindings](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings/)	 - IAM role-bindings resource interactions.
* [chainctl iam roles](/chainguard/chainctl/chainctl-docs/chainctl_iam_roles/)	 - IAM role resource interactions.

