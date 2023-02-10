---
date: 2023-02-10T22:19:42Z
title: "chainctl policies versions view"
slug: chainctl_policies_versions_view
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_versions_view/
draft: false
images: []
type: "article"
toc: true
---
## chainctl policies versions view

View the details of a policy version.

```
chainctl policies versions view [VERSION_ID] [--policy POLICY_NAME | POLICY_ID] [--output json] [flags]
```

### Options

```
  -h, --help            help for view
  -p, --policy string   The policy to view a version of. This flag is ignored if VERSION_ID is given.
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

