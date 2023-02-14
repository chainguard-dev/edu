---
date: 2023-02-14T01:25:23Z
title: "chainctl policies edit"
slug: chainctl_policies_edit
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_edit/
draft: false
images: []
type: "article"
toc: true
---
## chainctl policies edit

Edit a policy document.

```
chainctl policies edit [POLICY_NAME | POLICY_ID] [--label VERSION_LABEL] [--yes] [flags]
```

### Examples

```
  # Edit a policy by name and give it a label
  chainctl policy edit my-policy --label v2"
  
  # Edit a policy by ID
  chainctl policy edit bd504bdfe12e8a7f56c43e8231fd8d57a3dc7a3c/1d570a212972383b
```

### Options

```
  -h, --help           help for edit
  -l, --label string   The label for this version of the policy.
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl policies](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

