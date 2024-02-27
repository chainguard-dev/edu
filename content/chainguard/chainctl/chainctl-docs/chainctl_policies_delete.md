---
date: 2024-02-26T20:38:15Z
title: "chainctl policies delete"
slug: chainctl_policies_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies delete

Delete a policy.

```
chainctl policies delete [POLICY,... | --parent=PARENT [--recursive]] [--yes] [--output id]
```

### Examples

```
  # Delete a policy by name
  chainctl policy delete my-policy
  
  # Delete a policy by ID
  chainctl policy delete fb694596eb...
  
  # Delete multiple policies by name
  chainctl policy delete my-policy,other-policy
  
  # Delete all policies in an organization
  chainctl policy delete --parent=my-org
  
  # Delete all policies in an organization and its descendants
  chainctl policy delete --parent=my-org --recursive
```

### Options

```
  -h, --help            help for delete
      --parent string   Delete all policies from this location.
  -R, --recursive       Delete policies from all descendants of --parent.
  -y, --yes             Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

