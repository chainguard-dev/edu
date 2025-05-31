---
date: 2025-05-30T20:37:58Z
title: "chainctl images repos build"
slug: chainctl_images_repos_build
url: /chainguard/chainctl/chainctl-docs/chainctl_images_repos_build/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images repos build

Manage custom image builds

### Options

```
  -h, --help   help for build
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
* [chainctl images repos build apply](/chainguard/chainctl/chainctl-docs/chainctl_images_repos_build_apply/)	 - Apply a build config
* [chainctl images repos build edit](/chainguard/chainctl/chainctl-docs/chainctl_images_repos_build_edit/)	 - Edit a build config
* [chainctl images repos build list](/chainguard/chainctl/chainctl-docs/chainctl_images_repos_build_list/)	 - List build reports
* [chainctl images repos build logs](/chainguard/chainctl/chainctl-docs/chainctl_images_repos_build_logs/)	 - Get build logs

