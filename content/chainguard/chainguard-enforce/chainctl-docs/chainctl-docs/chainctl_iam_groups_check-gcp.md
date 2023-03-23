---
date: 2023-03-23T19:47:43Z
title: "chainctl iam groups check-gcp"
slug: chainctl_iam_groups_check-gcp
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_iam_groups_check-gcp/
draft: false
images: []
type: "article"
toc: true
---
## chainctl iam groups check-gcp

Checks that the given group has been properly configured for OIDC federation with GCP.

```
chainctl iam groups check-gcp [GROUP_NAME | GROUP_ID] [--output TODO] [flags]
```

### Options

```
  -h, --help   help for check-gcp
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

