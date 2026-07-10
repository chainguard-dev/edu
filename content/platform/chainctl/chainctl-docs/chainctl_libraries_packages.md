---
date: 2026-07-01T03:32:22Z
title: "chainctl libraries packages"
slug: chainctl_libraries_packages
url: /platform/chainctl/chainctl-docs/chainctl_libraries_packages/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries packages

Inspect Libraries packages.

### Synopsis

Browse the Chainguard Libraries package catalog. Packages are served by
Chainguard Libraries across language ecosystems; these commands list packages,
their versions, and per-ecosystem counts, and report packages withheld by
active Libraries policy.

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

* [chainctl libraries](/platform/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.
* [chainctl libraries packages blocked](/platform/chainctl/chainctl-docs/chainctl_libraries_packages_blocked/)	 - List blocked Libraries packages.
* [chainctl libraries packages count](/platform/chainctl/chainctl-docs/chainctl_libraries_packages_count/)	 - Count Libraries packages per ecosystem.
* [chainctl libraries packages list](/platform/chainctl/chainctl-docs/chainctl_libraries_packages_list/)	 - List Libraries packages.
* [chainctl libraries packages versions](/platform/chainctl/chainctl-docs/chainctl_libraries_packages_versions/)	 - List the versions of a Libraries package.

