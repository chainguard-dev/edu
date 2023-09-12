---
date: 2023-09-12T13:04:57Z
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
chainctl policies delete [POLICY,... | --group=GROUP [--recursive]] [--yes] [--output id] [flags]
```

### Examples

```
  # Delete a policy by name
  chainctl policy delete my-policy
  
  # Delete a policy by ID
  chainctl policy delete fb694596eb...
  
  # Delete multiple policies by name
  chainctl policy delete my-policy,other-policy
  
  # Delete all policies in a group
  chainctl policy delete --group=my-group
  
  # Delete all policies in a group and its descendants
  chainctl policy delete --group=my-group --recursive
```

### Options

```
      --group string   Delete all policies from this group.
  -h, --help           help for delete
  -R, --recursive      Delete policies from all descendants of --group.
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl policies](/chainguard/chainctl/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

