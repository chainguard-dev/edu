---
date: 2026-10-26T19:49:34Z
title: "chainctl develop check"
slug: chainctl_develop_check
url: /platform/chainctl/chainctl-docs/chainctl_develop_check/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop check

Run the repository's checks inside a development session.

### Synopsis

Run the checks of the session's working tree — the .chainguard/ documents as they are in the session right now, uncommitted edits included — inside the session's guest, streaming each step's output as it happens, and exit 0 when they pass or 1 when a step fails.

The result is advisory. The checks run against the dirty tree in the session as it is (packages installed since it opened count), where the gate runs the committed ref in a fresh guest and mints the verdict on push. A pass here is a strong predictor of the gate's, never a guarantee, and nothing here signs.

--check names one check; without it every check with steps runs in document order, stopping at the first failure. A parked session is resumed first. A directory session whose tree has not synced yet is refused: attach to it once to sync it. The same runner is the guest's own run-ci command.

```
chainctl develop check SESSION [--check CHECK] [--output=json]
```

### Examples

```
  # Run every check of the session's tree
  chainctl develop check mono/quiet-harbor

  # One check, by short id
  chainctl develop check 3f9a1c2e --check test
```

### Options

```
      --check string   Run this check (default: all checks with steps, in document order).
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

