---
date: 2024-02-06T20:43:38Z
title: "chainctl iam identities list"
slug: chainctl_iam_identities_list
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities list

List identities.

```
chainctl iam identities list [--group=GROUP_NAME|GROUP_ID] [--name=NAME] [--relationship={aws|claim_match|pull_token|service_principal|static}] [--expired] [--output id|table|json]
```

### Examples

```
  # List all identities.
  chainctl iam identities list
  
  # List all static identities.
  chainctl iam identities list --relationship=static
  
  # Filter identities by name.
  chainctl iam identities list --name=my-identity
  
  # List expired identities
  chainctl iam identities list --expired
```

### Options

```
      --expired               Return only expired static identities.
      --group string          The name or id of the parent group to list identities from.
  -h, --help                  help for list
      --name string           Filter identities by name.
      --relationship string   Filter identities by relationship type (aws, claim_match, pull_token, service_principal, static).
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/)	 - Identity management.

