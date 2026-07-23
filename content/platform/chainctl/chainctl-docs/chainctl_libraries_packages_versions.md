---
date: 2026-07-22T19:49:10Z
title: "chainctl libraries packages versions"
slug: chainctl_libraries_packages_versions
url: /platform/chainctl/chainctl-docs/chainctl_libraries_packages_versions/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries packages versions

List the versions of a Libraries package.

### Synopsis

List all versions of a single package, identified by the id returned by 'chainctl libraries packages list'.

```
chainctl libraries packages versions PACKAGE_ID [--output=json|table] [flags]
```

### Options

```
      --upstream   Also include upstream-registry versions. By default only Chainguard-built versions are listed.
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

* [chainctl libraries packages](/platform/chainctl/chainctl-docs/chainctl_libraries_packages/)	 - Inspect Libraries packages.

