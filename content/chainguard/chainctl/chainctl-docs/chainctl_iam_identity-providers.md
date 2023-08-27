---
date: 2023-08-26T00:42:30Z
title: "chainctl iam identity-providers"
slug: chainctl_iam_identity-providers
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers

customer managed identity provider management

### Options

```
  -h, --help   help for identity-providers
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam identity-providers create](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_create/)	 - Create an identity provider
* [chainctl iam identity-providers delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_delete/)	 - Delete an identity provider.
* [chainctl iam identity-providers list](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_list/)	 - List identity providers.
* [chainctl iam identity-providers update](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_update/)	 - Update an identity provider

