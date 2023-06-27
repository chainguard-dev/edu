---
date: 2023-06-27T18:22:50Z
title: "chainctl iam identities"
slug: chainctl_iam_identities
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities

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

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam identities create](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/)	 - Create a new identity.
* [chainctl iam identities delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_delete/)	 - Delete an identity.
* [chainctl iam identities list](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_list/)	 - List identities.
* [chainctl iam identities update](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_update/)	 - Update an identity
* [chainctl iam identities view](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_view/)	 - View the details of an identity.

