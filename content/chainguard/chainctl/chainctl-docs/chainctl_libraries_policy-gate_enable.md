---
date: 2026-06-10T18:28:08Z
title: "chainctl libraries policy-gate enable"
slug: chainctl_libraries_policy-gate_enable
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate_enable/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy-gate enable

Enable a Libraries policy for an organization.

### Synopsis

Enable a Libraries policy by creating a binding. If a binding already exists
for the (organization, ecosystem, mode), its mode is updated. The default mode
is ENFORCED.

```
chainctl libraries policy-gate enable --policy POLICY [--parent ORG] [--ecosystem ECOSYSTEM] [--mode ENFORCED|LOG] [flags]
```

### Options

```
      --ecosystem string   The ecosystem the binding applies to (JAVA, PYTHON, JAVASCRIPT).
      --mode string        The binding mode (ENFORCED or LOG).
      --parent string      The name or id of the organization to scope the binding to.
      --policy string      The name or UIDP of the policy.
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

* [chainctl libraries policy-gate](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy-gate/)	 - Manage Libraries policy gates.

