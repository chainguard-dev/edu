---
date: 2023-11-21T23:15:25Z
title: "chainctl iam account-associations unset"
slug: chainctl_iam_account-associations_unset
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_unset/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations unset

Remove cloud provider account associations from a group.

### Options

```
  -h, --help   help for unset
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam account-associations](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations/)	 - Configure and manage cloud provider account associations.
* [chainctl iam account-associations unset aws](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_unset_aws/)	 - Remove AWS account configuration for a group.
* [chainctl iam account-associations unset gcp](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_unset_gcp/)	 - Remove GCP account configuration for a group.

