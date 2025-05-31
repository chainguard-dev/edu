---
date: 2025-05-30T20:37:58Z
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
chainctl images repos list [--repo=REPO_NAME] [--public | --parent=PARENT_NAME|PARENT_ID] [--updated-within=DURATION] [--show-dates] [--show-epochs] [--show-referrers]
```

### Options

```
  -h, --help            help for list
      --parent string   The name or id of the parent location to list image repos.
      --public          List repos from the public Chainguard registry.
      --repo string     Search for a specific repo by name.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl images repos](/chainguard/chainctl/chainctl-docs/chainctl_images_repos/)	 - Image repo related commands for the Chainguard platform.

