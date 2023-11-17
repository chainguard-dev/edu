---
date: 2023-11-17T10:11:36Z
title: "chainctl iam account-associations check"
slug: chainctl_iam_account-associations_check
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations check

Check the OIDC federation configurations for cloud providers.

### Options

```
  -h, --help   help for check
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
* [chainctl iam account-associations check aws](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check_aws/)	 - Checks that the given group has been properly configured for OIDC federation with AWS
* [chainctl iam account-associations check gcp](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check_gcp/)	 - Checks that the given group has been properly configured for OIDC federation with GCP

