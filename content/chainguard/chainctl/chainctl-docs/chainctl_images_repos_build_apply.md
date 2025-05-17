---
date: 2025-05-16T19:28:17Z
title: "chainctl images repos build apply"
slug: chainctl_images_repos_build_apply
url: /chainguard/chainctl/chainctl-docs/chainctl_images_repos_build_apply/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images repos build apply

Apply a build config

```
chainctl images repos build apply [flags]
```

### Options

```
  -f, --file string     The name of the file containing the build config.
  -h, --help            help for apply
      --parent string   The name or id of the parent location to apply build config.
      --repo string     The name or id of the repo to apply build config.
  -y, --yes             Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

