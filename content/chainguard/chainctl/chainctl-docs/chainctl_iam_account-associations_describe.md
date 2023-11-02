---
date: 2023-11-01T20:32:20Z
title: "chainctl iam account-associations describe"
slug: chainctl_iam_account-associations_describe
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations describe

Describe cloud provider account associations for a group.

```
chainctl iam account-associations describe GROUP_NAME|GROUP_ID [--aws] [--gcp] [--output table|id|json] [flags]
```

### Options

```
      --aws    Include the AWS account association.
      --gcp    Include the GCP account association.
  -h, --help   help for describe
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

