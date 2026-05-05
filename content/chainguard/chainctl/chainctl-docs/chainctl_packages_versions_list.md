---
date: 2026-05-04T16:59:58Z
title: "chainctl packages versions list"
slug: chainctl_packages_versions_list
url: /chainguard/chainctl/chainctl-docs/chainctl_packages_versions_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl packages versions list

List version stream data for a managed package.

### Synopsis

List version stream data for a managed package.

PACKAGE_NAME is the name of a Chainguard-managed version stream, not an arbitrary apk
package name. Examples include 'bazel', 'airflow', 'python-3.13', and 'actions-runner'.
For arbitrary apk packages such as 'bash' or 'curl', use 'apk info' or 'apk search'
inside a Chainguard image instead.

```
chainctl packages versions list PACKAGE_NAME [--show-eol] [--show-active] [--show-fips] [--include-inactive] [--output=csv|json|table|wide]
```

### Examples

```
  # List version data for the bazel version stream
  chainctl packages versions list bazel

  # List a specific minor stream
  chainctl packages versions list python-3.13
```

### Options

```
      --include-inactive   Include only packages within the EOL grace period end date. No end date is considered inclusive.
      --show-active        Show only active versions.
      --show-eol           Show only EOL versions.
      --show-fips          Show only FIPS versions.
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

* [chainctl packages versions](/chainguard/chainctl/chainctl-docs/chainctl_packages_versions/)	 - Package version related commands for the Chainguard platform.

