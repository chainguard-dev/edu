---
date: 2026-10-26T19:49:34Z
title: "chainctl develop delete"
slug: chainctl_develop_delete
url: /platform/chainctl/chainctl-docs/chainctl_develop_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop delete

Delete a development session.

### Synopsis

Delete a session named by name, short id, or (when unambiguous) repository: a live guest is torn down and its snapshot discarded; a reaped tombstone is removed. This is the only destroy. Confirms on a terminal unless --yes.

```
chainctl develop delete SESSION [--yes] [--output=json]
```

### Options

```
  -y, --yes   Delete without confirmation.
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
      --non-interactive    Disable prompts; fail if a session or group choice is ambiguous.
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
      --parent string      Organization or folder name/ID (defaults to $CHAINCTL_SANDBOX_GROUP, then default.group).
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl develop](/platform/chainctl/chainctl-docs/chainctl_develop/)	 - Open or resume a cloud development session.

