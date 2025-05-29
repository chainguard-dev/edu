---
date: 2025-05-28T21:10:51Z
title: "chainctl images repos build logs"
slug: chainctl_images_repos_build_logs
url: /chainguard/chainctl/chainctl-docs/chainctl_images_repos_build_logs/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images repos build logs

Get build logs

```
chainctl images repos build logs [flags]
```

### Options

```
      --build-id string   The id of the build to get logs for.
  -h, --help              help for logs
      --parent string     The name or id of the parent location to get build logs.
      --repo string       The name or id of the repo to get build logs.
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

* [chainctl images repos build](/chainguard/chainctl/chainctl-docs/chainctl_images_repos_build/)	 - Manage custom image builds

