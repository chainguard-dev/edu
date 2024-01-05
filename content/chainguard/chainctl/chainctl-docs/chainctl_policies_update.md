---
date: 2024-01-05T19:14:17Z
title: "chainctl policies update"
slug: chainctl_policies_update
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies update

Update the description of a policy.

```
chainctl policies update POLICY_NAME | POLICY_ID [--description=DESCRIPTION] [--output table|json|id] [flags]
```

### Examples

```
  # Update a policy description by name.
  chainctl policy update my-policy --description="A description of my policy."
  
  # Remove a policy description by ID.
  chainctl policy update 617ec5ae5775e22fb52ec2d62398de1e7def7986/e74e9050df769110 --description=""
```

### Options

```
  -d, --description string   New description for this policy.
  -h, --help                 help for update
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

