---
date: 2026-07-23T16:28:18Z
title: "chainctl policies check"
slug: chainctl_policies_check
url: /platform/chainctl/chainctl-docs/chainctl_policies_check/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies check

Check an image against active policies.

### Synopsis

Evaluate an image against any active policies and print the
result for each.

Exit status is non-zero if any policy returned DENIED or ERROR, regardless
of the policy's mode, so this command is suitable for use in CI.

```
chainctl policies check IMAGE_REF [flags]
```

### Examples

```

# Check an image by tag
chainctl policies check cgr.dev/example.com/python:latest

# Check an image by digest
chainctl policies check cgr.dev/example.com/python@sha256:abc...

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

* [chainctl policies](/platform/chainctl/chainctl-docs/chainctl_policies/)	 - Manage policies.

