---
date: 2022-08-29T10:58:14-04:00
title: "chainctl policies view"
slug: chainctl_policies_view
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_view/
draft: false
images: []
type: "article"
toc: true
---
## chainctl policies view

View a policy.

```
chainctl policies view [POLICY_ID|POLICY_NAME] [flags]
```

### Options

```
  -h, --help   help for view
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

* [chainctl policies](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

