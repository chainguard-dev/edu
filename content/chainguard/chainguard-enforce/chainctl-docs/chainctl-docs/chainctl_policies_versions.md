---
date: 2023-03-13T22:56:41Z
title: "chainctl policies versions"
slug: chainctl_policies_versions
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_versions/
draft: false
images: []
type: "article"
toc: true
---
## chainctl policies versions

Commands for interacting with policy versions on the Chainguard platform.

### Options

```
  -h, --help   help for versions
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

* [chainctl policies](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.
* [chainctl policies versions activate](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_versions_activate/)	 - Select a version of a policy to enforce.
* [chainctl policies versions list](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_versions_list/)	 - List versions of a policy.
* [chainctl policies versions view](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_versions_view/)	 - View the details of a policy version.

