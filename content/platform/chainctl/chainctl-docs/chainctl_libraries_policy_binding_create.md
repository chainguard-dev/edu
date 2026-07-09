---
date: 2026-07-01T03:32:22Z
title: "chainctl libraries policy binding create"
slug: chainctl_libraries_policy_binding_create
url: /platform/chainctl/chainctl-docs/chainctl_libraries_policy_binding_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy binding create

Create a Libraries policy binding.

### Synopsis

Create a binding to activate a Libraries policy for an (organization, ecosystem) pair. The default mode is ENFORCE.

```
chainctl libraries policy binding create --policy POLICY [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--ecosystem ECOSYSTEM] [--mode ENFORCE|PREVIEW] [flags]
```

### Options

```
      --ecosystem string   The ecosystem the binding applies to (JAVA, PYTHON, JAVASCRIPT).
      --mode string        The binding mode (ENFORCE or PREVIEW). Defaults to ENFORCE.
      --parent string      The name or id of the organization to scope the binding to.
      --policy string      The name or UIDP of the policy to bind.
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

* [chainctl libraries policy binding](/platform/chainctl/chainctl-docs/chainctl_libraries_policy_binding/)	 - Manage Libraries policy bindings.

