---
date: 2023-10-24T20:45:57Z
title: "chainctl images repos list"
slug: chainctl_images_repos_list
url: /chainguard/chainctl/chainctl-docs/chainctl_images_repos_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images repos list

List image repositories.

```
chainctl images repos list [--group GROUP_NAME | GROUP_ID] [flags]
```

### Options

```
      --group string     The name or id of the parent group to list image repos.
  -h, --help             help for list
      --show-dates       Whether to show date tags of the form latest-{date}.
      --show-epochs      Whether to show epoch tags of the form 1.2.3-r4.
      --show-referrers   Whether to show referrer tags of the form sha256-deadbeef.{sig,sbom,att}.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl images repos](/chainguard/chainctl/chainctl-docs/chainctl_images_repos/)	 - Image repo related commands for the Chainguard platform.

