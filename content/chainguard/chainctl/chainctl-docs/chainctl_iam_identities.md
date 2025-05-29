---
date: 2025-05-28T21:10:51Z
title: "chainctl iam identities"
slug: chainctl_iam_identities
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities

Identity management.

### Options

```
  -h, --help   help for identities
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
* [chainctl iam identities create](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/)	 - Create a new identity.
* [chainctl iam identities delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_delete/)	 - Delete one or more identities.
* [chainctl iam identities describe](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_describe/)	 - View the details of an identity.
* [chainctl iam identities list](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_list/)	 - List identities.
* [chainctl iam identities update](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_update/)	 - Update an identity

