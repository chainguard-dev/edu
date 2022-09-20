---
date: 2022-08-29T10:58:14-04:00
title: "chainctl iam groups describe"
slug: chainctl_iam_groups_describe
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_groups_describe/
draft: false
images: []
type: "article"
toc: true
---
## chainctl iam groups describe

Describe a group. (Experimental)

```
chainctl iam groups describe [--output json] [flags]
```

### Options

```
  -h, --help   help for describe
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string   The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string     A specific chainctl config file.
      --console string    The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string     The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string     Output format. One of: ["", "table", "tree", "json", "id", "wide"]
```

### SEE ALSO

* [chainctl iam groups](/chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_groups/)	 - IAM Group resource interactions.

