---
date: 2023-04-11T16:56:59Z
title: "chainctl auth identities"
slug: chainctl_auth_identities
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_identities/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth identities

Identity management.

### Options

```
  -h, --help   help for identities
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

* [chainctl auth](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.
* [chainctl auth identities create](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_identities_create/)	 - Create a new identity.
* [chainctl auth identities delete](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_identities_delete/)	 - Delete an identity.
* [chainctl auth identities list](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_identities_list/)	 - List identities.
* [chainctl auth identities update](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_identities_update/)	 - Update an identity
* [chainctl auth identities view](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_identities_view/)	 - View the details of an identity.

