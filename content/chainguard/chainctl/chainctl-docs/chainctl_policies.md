---
date: 2023-04-19T23:22:15Z
title: "chainctl policies"
slug: chainctl_policies
url: /chainguard/chainctl/chainctl-docs/chainctl_policies/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies

Policy related commands for the Chainguard platform.

### Options

```
  -h, --help   help for policies
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

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl policies apply](/chainguard/chainctl/chainctl-docs/chainctl_policies_apply/)	 - Create or update a policy described by file or stdin.
* [chainctl policies delete](/chainguard/chainctl/chainctl-docs/chainctl_policies_delete/)	 - Delete a policy.
* [chainctl policies edit](/chainguard/chainctl/chainctl-docs/chainctl_policies_edit/)	 - Edit a policy document.
* [chainctl policies list](/chainguard/chainctl/chainctl-docs/chainctl_policies_list/)	 - List policies.
* [chainctl policies update](/chainguard/chainctl/chainctl-docs/chainctl_policies_update/)	 - Update the description of a policy.
* [chainctl policies versions](/chainguard/chainctl/chainctl-docs/chainctl_policies_versions/)	 - Commands for interacting with policy versions on the Chainguard platform.
* [chainctl policies view](/chainguard/chainctl/chainctl-docs/chainctl_policies_view/)	 - View a policy.

