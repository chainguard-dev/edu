---
date: 2026-10-28T16:22:54Z
title: "chainctl develop mcp"
slug: chainctl_develop_mcp
url: /platform/chainctl/chainctl-docs/chainctl_develop_mcp/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop mcp

Serve tools for development sessions to an MCP client over stdio.

### Synopsis

Serve the develop session tools over the Model Context Protocol on stdin and stdout, for an agent such as Claude Code to read, edit and run commands in your sessions:

  claude mcp add develop -- chainctl develop mcp

The tools are exec, wait, kill, read, write and edit. Each takes a session parameter, a session name or short id, resolved in --parent as the other develop verbs resolve it. Paths are absolute in the guest or relative to /work. write and edit refuse a file that changed since this server last read it. Sessions are created, listed and deleted with the other develop verbs.

Run long builds and tests with the exec tool's run_in_background, then wait for them: the command runs detached in the guest, so the server's other calls go on beside it. A 'chainctl develop exec' from Bash instead holds the guest for the whole command, and another API replica's calls queue behind it.

```
chainctl develop mcp [--parent GROUP]
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

