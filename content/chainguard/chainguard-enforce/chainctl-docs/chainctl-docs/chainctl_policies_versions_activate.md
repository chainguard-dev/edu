---
date: 2023-02-10T22:19:42Z
title: "chainctl policies versions activate"
slug: chainctl_policies_versions_activate
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_versions_activate/
draft: false
images: []
type: "article"
toc: true
---
## chainctl policies versions activate

Select a version of a policy to enforce.

```
chainctl policies versions activate {VERSION_ID | --policy POLICY} [--output table|json]
```

### Options

```
  -h, --help            help for activate
  -p, --policy string   The policy to activate a version of. This flag is ignored if VERSION_ID is given.
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

