---
date: 2026-03-09T12:15:11Z
title: "chainctl agent dockerfile"
slug: chainctl_agent_dockerfile
url: /chainguard/chainctl/chainctl-docs/chainctl_agent_dockerfile/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl agent dockerfile

AI-powered Dockerfile migration and optimization.

### Synopsis

Dockerfile provides AI-powered Dockerfile migration commands.

Commands:
  build      Migrate a Dockerfile to use wolfi-base
  optimize   Optimize an existing wolfi-based Dockerfile
  upgrade    Upgrade package versions in a Dockerfile
  validate   Validate a migrated Dockerfile

### Options

```
      --log-file string      Write detailed log output to this file
      --server-addr string   DFC server address (overrides config)
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl agent](/chainguard/chainctl/chainctl-docs/chainctl_agent/)	 - Agent-powered commands.
* [chainctl agent dockerfile build](/chainguard/chainctl/chainctl-docs/chainctl_agent_dockerfile_build/)	 - Migrate a Dockerfile to use wolfi-base.
* [chainctl agent dockerfile optimize](/chainguard/chainctl/chainctl-docs/chainctl_agent_dockerfile_optimize/)	 - Optimize an existing wolfi-based Dockerfile.
* [chainctl agent dockerfile upgrade](/chainguard/chainctl/chainctl-docs/chainctl_agent_dockerfile_upgrade/)	 - Upgrade package versions in a Dockerfile.
* [chainctl agent dockerfile validate](/chainguard/chainctl/chainctl-docs/chainctl_agent_dockerfile_validate/)	 - Validate a migrated Dockerfile.

