---
date: 2026-11-12T21:48:09Z
title: "chainctl develop cp"
slug: chainctl_develop_cp
url: /platform/chainctl/chainctl-docs/chainctl_develop_cp/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop cp

Copy a file into or out of a development session.

### Synopsis

Copy one file between this machine and a session's guest, byte for byte, up to 16 MiB.

Exactly one of SRC and DEST names a session, as SESSION:PATH, where SESSION is a session name or short id as the other develop verbs take it. A guest PATH is absolute or relative to /work. A local path with a colon in it must start with / or ./ so it is not read as a session. A DEST that ends in /, or a local DEST that is a directory, gets SRC's file name. A local - is stdin as SRC and stdout as DEST.

An existing DEST file is replaced. A file copied in gets the guest's default mode, and one it replaces keeps its own; a file copied out gets 0644 less the umask, and one it replaces keeps its own. The guest side is the session's live root, where 'chainctl develop mcp' reads and writes. Directories are refused: copy one with tar through 'chainctl develop exec'.

```
chainctl develop cp [SESSION:]SRC [SESSION:]DEST
```

### Examples

```
  # Copy notes into a session's workspace
  chainctl develop cp notes.md mono/quiet-harbor:docs/

  # Copy a file the session wrote back to this machine
  chainctl develop cp 3f9a2c1e:/tmp/report.txt ./report.txt
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

