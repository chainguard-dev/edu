---
date: 2023-04-25T23:36:21Z
title: "chainctl iam identity-providers delete"
slug: chainctl_iam_identity-providers_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers delete

Delete an identity provider.

```
chainctl iam identity-providers delete IDENTITY_PROVIDER_ID [--yes] [--output id]
```

### Examples

```
  # Delete an identity provider
  chainctl iam identity-providers delete 9b6da6e64b45129eb4e9f9f3ce9b69ca2a550c6b/034e4afcda8c0b07
```

### Options

```
  -h, --help   help for delete
  -y, --yes    Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam identity-providers](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

