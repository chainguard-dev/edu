---
date: 2023-02-15T23:07:18Z
title: "chainctl policies versions list"
slug: chainctl_policies_versions_list
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_versions_list/
draft: false
images: []
type: "article"
toc: true
---
## chainctl policies versions list

List versions of a policy.

```
chainctl policies versions list [POLICY_NAME | POLICY_ID] [--output table|json]
```

### Options

```
  -h, --help   help for list
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

* [chainctl policies versions](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_versions/)	 - Commands for interacting with policy versions on the Chainguard platform.

