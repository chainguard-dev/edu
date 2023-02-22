---
date: 2023-02-22T10:33:41Z
title: "chainctl iam groups set-aws"
slug: chainctl_iam_groups_set-aws
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_groups_set-aws/
draft: false
images: []
type: "article"
toc: true
---
## chainctl iam groups set-aws

Set the AWS account association for this IAM Group.

```
chainctl iam groups set-aws [GROUP_NAME | GROUP_ID] [--account ACCOUNT_ID] [--output |json|table] [flags]
```

### Options

```
      --account string       The AWS account ID.
  -d, --description string   The description of the association.
  -h, --help                 help for set-aws
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
```

### SEE ALSO

* [chainctl iam groups](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

