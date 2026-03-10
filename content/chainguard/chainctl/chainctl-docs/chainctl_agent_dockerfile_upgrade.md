---
date: 2026-03-09T12:15:11Z
title: "chainctl agent dockerfile upgrade"
slug: chainctl_agent_dockerfile_upgrade
url: /chainguard/chainctl/chainctl-docs/chainctl_agent_dockerfile_upgrade/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl agent dockerfile upgrade

Upgrade package versions in a Dockerfile.

```
chainctl agent dockerfile upgrade [flags]
```

### Options

```
  -f, --dockerfile string   Path to the Dockerfile (default "Dockerfile")
      --dry-run             Show upgrade plan without applying
      --group string        Chainguard group ID for authorization
      --non-interactive     Run without user prompts
  -o, --output string       Output path for upgraded Dockerfile (use '-' for stdout)
```

### Options inherited from parent commands

```
      --api string           The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string      The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string        A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string       The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color          Force color output even when stdout is not a TTY.
  -h, --help                 Help for chainctl
      --issuer string        The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-file string      Write detailed log output to this file
      --log-level string     Set the log level (debug, info) (default "ERROR")
      --server-addr string   DFC server address (overrides config)
  -v, --v int                Set the log verbosity level.
```

### SEE ALSO

* [chainctl agent dockerfile](/chainguard/chainctl/chainctl-docs/chainctl_agent_dockerfile/)	 - AI-powered Dockerfile migration and optimization.

