---
date: 2025-08-01T17:33:38Z
title: "chainctl"
slug: chainctl
url: /chainguard/chainctl/chainctl-docs/chainctl/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl

Chainguard Control

```
chainctl [flags]
```

### Options

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl auth](/chainguard/chainctl/chainctl-docs/chainctl_auth/)	 - Auth related commands for the Chainguard platform.
* [chainctl config](/chainguard/chainctl/chainctl-docs/chainctl_config/)	 - Local config file commands for chainctl.
* [chainctl events](/chainguard/chainctl/chainctl-docs/chainctl_events/)	 - Events related commands for the Chainguard platform.
* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl images](/chainguard/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.
* [chainctl packages](/chainguard/chainctl/chainctl-docs/chainctl_packages/)	 - Interact with Chainguard packages
* [chainctl update](/chainguard/chainctl/chainctl-docs/chainctl_update/)	 - Update chainctl.
* [chainctl version](/chainguard/chainctl/chainctl-docs/chainctl_version/)	 - Prints the version

