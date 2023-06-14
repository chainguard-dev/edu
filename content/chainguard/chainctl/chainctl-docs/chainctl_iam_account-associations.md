---
date: 2023-06-13T23:28:25Z
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
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string              The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam account-associations check](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check/)	 - Check the OIDC federation configurations for cloud providers.
* [chainctl iam account-associations describe](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_describe/)	 - Describe cloud provider account associations for a group.
* [chainctl iam account-associations set](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set/)	 - Set cloud provider account associations for a group.
* [chainctl iam account-associations unset](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_unset/)	 - Remove cloud provider account associations from a group.

