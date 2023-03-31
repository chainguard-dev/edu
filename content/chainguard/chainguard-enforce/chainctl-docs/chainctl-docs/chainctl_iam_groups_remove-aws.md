---
date: 2023-03-29T13:31:37Z
title: "chainctl iam groups remove-aws"
slug: chainctl_iam_groups_remove-aws
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_groups_remove-aws/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam groups remove-aws

Remove any configured AWS account association for this IAM Group.

```
chainctl iam groups remove-aws [GROUP_NAME | GROUP_ID][--output |json|table] [flags]
```

### Options

```
      --account string       The AWS account ID.
  -d, --description string   The description of the association.
  -h, --help                 help for remove-aws
  -n, --name string          The name of the association. (default: the group name)
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

* [chainctl iam groups](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

