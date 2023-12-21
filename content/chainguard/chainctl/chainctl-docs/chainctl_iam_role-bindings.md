---
date: 2023-12-21T20:37:17Z
title: "chainctl iam role-bindings"
slug: chainctl_iam_role-bindings
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam role-bindings

IAM role-bindings resource interactions.

### Options

```
  -h, --help   help for role-bindings
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam role-bindings create](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings_create/)	 - Create a role-binding
* [chainctl iam role-bindings delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings_delete/)	 - Delete a role-binding.
* [chainctl iam role-bindings list](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings_list/)	 - List role-bindings.
* [chainctl iam role-bindings update](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings_update/)	 - Update a role-binding.

