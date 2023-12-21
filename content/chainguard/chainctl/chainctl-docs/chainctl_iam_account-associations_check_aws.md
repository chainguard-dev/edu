---
date: 2023-12-20T19:55:18Z
title: "chainctl iam account-associations check aws"
slug: chainctl_iam_account-associations_check_aws
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check_aws/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations check aws

Checks that the given group has been properly configured for OIDC federation with AWS

```
chainctl iam account-associations check aws GROUP_NAME|GROUP_ID [flags]
```

### Options

```
  -h, --help   help for aws
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam account-associations check](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_check/)	 - Check the OIDC federation configurations for cloud providers.

