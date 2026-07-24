---
date: 2026-07-23T16:28:18Z
title: "chainctl libraries policy disable"
slug: chainctl_libraries_policy_disable
url: /platform/chainctl/chainctl-docs/chainctl_libraries_policy_disable/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy disable

Disable a Libraries policy for an organization.

### Synopsis

Disable a Libraries policy by deleting its binding. If --mode is omitted, both
the ENFORCE and PREVIEW bindings for the (organization, ecosystem) are deleted.

```
chainctl libraries policy disable [POLICY] [--parent ORG] [--ecosystem ECOSYSTEM] [--mode ENFORCE|PREVIEW] [flags]
```

### Options

```
      --ecosystem string   The ecosystem the binding applies to (JAVA, PYTHON, JAVASCRIPT).
      --mode string        The binding mode (ENFORCE or PREVIEW).
      --parent string      The name or id of the organization to scope the binding to.
      --policy string      The name or UIDP of the policy. Provide this or the positional argument, not both.
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

* [chainctl libraries policy](/platform/chainctl/chainctl-docs/chainctl_libraries_policy/)	 - Manage Libraries policies.

