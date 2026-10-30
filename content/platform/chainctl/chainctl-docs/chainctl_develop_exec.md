---
date: 2026-10-28T16:22:54Z
title: "chainctl develop exec"
slug: chainctl_develop_exec
url: /platform/chainctl/chainctl-docs/chainctl_develop_exec/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop exec

Run a command in a development session.

### Synopsis

Run one command in a session's guest without a terminal and exit with its exit code.

CMD and its arguments run as given, with no shell; pass sh -c '...' for one. The command runs in --cwd, /work by default. With -i (--stdin) this process's stdin, read to its end (at most 16 MiB), is the command's stdin; without it the command's stdin is empty, so a shell loop's input is never consumed. The command's stdout and stderr arrive on this process's stdout and stderr, byte for byte.

The exit code is the command's, 124 when --timeout killed it, and 255 when the command's outcome is unknown: the session could not be found or reached, or the call was refused or cut off. Interrupting this process, or --timeout passing, kills the command's process group; anything it started with setsid keeps running. A parked session is resumed first, and a session busy with another client's call on another API replica is waited for, up to 10 minutes. A directory session whose tree has not synced yet is refused: attach to it once to sync it. The command holds the session's guest until it exits, so a long one delays other clients' calls; for a long build an agent drives, prefer 'chainctl develop mcp' and its exec tool's run_in_background. The command's output is the guest's, byte for byte, terminal escapes included, as with ssh.

```
chainctl develop exec SESSION [-i] [--cwd DIR] [--timeout D] -- CMD [ARGS...]
```

### Examples

```
  # Run the tests in a session
  chainctl develop exec mono/quiet-harbor -- go test ./...

  # A shell pipeline, with a time limit
  chainctl develop exec 3f9a2c1e --timeout 10m -- sh -c 'make 2>&1 | tail -n 50'

  # Copy a file in, and back out
  chainctl develop exec 3f9a2c1e -i -- sh -c 'cat > notes.md' < notes.md
  chainctl develop exec 3f9a2c1e -- cat notes.md > notes.md
```

### Options

```
      --cwd string         Working directory in the session (absolute or relative to /work). (default "/work")
  -i, --stdin              Pass stdin to the command (up to 16 MiB; otherwise empty).
      --timeout duration   Stop the command after this duration and exit 124 (0: no timeout).
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

