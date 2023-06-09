---
date: 2023-06-09T16:20:16Z
title: "chainctl iam groups describe"
slug: chainctl_iam_groups_describe
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_groups_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam groups describe

Describe a group.

```
chainctl iam groups describe [--active-within DURATION] [--output json] [flags]
```

### Options

```
      --active-within duration   How recently a record must have been active to be listed. Zero will return all records. (default 24h0m0s)
  -h, --help                     help for describe
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

* [chainctl iam groups](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

