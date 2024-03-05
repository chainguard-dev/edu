---
date: 2024-03-04T20:32:40Z
title: "chainctl iam account-associations"
slug: chainctl_iam_account-associations
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations

Configure and manage cloud provider account associations.

### Options

```
  -h, --help   help for account-associations
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

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam account-associations check](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check/)	 - Check the OIDC federation configurations for cloud providers.
* [chainctl iam account-associations describe](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_describe/)	 - Describe cloud provider account associations for a location.
* [chainctl iam account-associations set](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set/)	 - Set cloud provider account associations for a location.
* [chainctl iam account-associations unset](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_unset/)	 - Remove cloud provider account associations from a location.

