---
date: 2023-05-03T16:19:30Z
title: "chainctl policies edit"
slug: chainctl_policies_edit
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_edit/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies edit

Edit a policy document.

```
chainctl policies edit [POLICY_NAME | POLICY_ID] [--yes] [flags]
```

### Examples

```
  # Edit a policy by name
  chainctl policy edit my-policy
  
  # Edit a policy by ID
  chainctl policy edit bd504b...
```

### Options

```
  -h, --help   help for edit
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

* [chainctl policies](/chainguard/chainctl/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

