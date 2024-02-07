---
date: 2024-02-07T16:33:23Z
title: "chainctl policies versions"
slug: chainctl_policies_versions
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_versions/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies versions

Commands for interacting with policy versions on the Chainguard platform.

### Options

```
  -h, --help   help for versions
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
* [chainctl policies versions activate](/chainguard/chainctl/chainctl-docs/chainctl_policies_versions_activate/)	 - Select a version of a policy to enforce.
* [chainctl policies versions diff](/chainguard/chainctl/chainctl-docs/chainctl_policies_versions_diff/)	 - View the differences between two versions of a policy.
* [chainctl policies versions list](/chainguard/chainctl/chainctl-docs/chainctl_policies_versions_list/)	 - List versions of a policy.
* [chainctl policies versions view](/chainguard/chainctl/chainctl-docs/chainctl_policies_versions_view/)	 - View the details of a policy version.

