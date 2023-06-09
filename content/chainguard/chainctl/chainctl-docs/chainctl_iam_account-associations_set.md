---
date: 2023-06-09T16:20:16Z
title: "chainctl iam account-associations set"
slug: chainctl_iam_account-associations_set
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations set

Set cloud provider account associations for a group.

### Options

```
  -h, --help   help for set
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

* [chainctl iam account-associations](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations/)	 - Configure and manage cloud provider account associations.
* [chainctl iam account-associations set aws](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set_aws/)	 - Set AWS account association for a group.
* [chainctl iam account-associations set gcp](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set_gcp/)	 - Set GCP account association for a group.

