---
date: 2024-02-08T19:39:21Z
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
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl policies](/chainguard/chainctl/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

