---
date: 2026-05-26T19:38:09Z
title: "chainctl policy-gate check"
slug: chainctl_policy-gate_check
url: /chainguard/chainctl/chainctl-docs/chainctl_policy-gate_check/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policy-gate check

Check an image against active policy gates.

### Synopsis

Evaluate an image against any active policy gates and print the
result for each.

Exit status is non-zero if any policy returned DENIED or ERROR, regardless
of the policy's mode, so this command is suitable for use in CI.

```
chainctl policy-gate check IMAGE_REF [flags]
```

### Examples

```

# Check an image by tag
chainctl policy-gate check cgr.dev/example.com/python:latest

# Check an image by digest
chainctl policy-gate check cgr.dev/example.com/python@sha256:abc...

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

* [chainctl policy-gate](/chainguard/chainctl/chainctl-docs/chainctl_policy-gate/)	 - Manage policy gates.

