---
date: 2025-02-19T23:30:24Z
title: "chainctl iam invites"
slug: chainctl_iam_invites
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_invites/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam invites

Manage invite codes that register identities with Chainguard.

### Options

```
  -h, --help   help for invites
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
  -o, --output string      Output format. One of: [csv, , json, id, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam invites create](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_create/)	 - Generate an invite code to identities with Chainguard.
* [chainctl iam invites delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_delete/)	 - Delete invite codes
* [chainctl iam invites list](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites_list/)	 - List organization and folder invites.

