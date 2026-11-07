---
date: 2026-11-06T22:09:37Z
title: "chainctl checks mcp"
slug: chainctl_checks_mcp
url: /platform/chainctl/chainctl-docs/chainctl_checks_mcp/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks mcp

Serve the checks verbs as tools to an MCP client over stdio.

### Synopsis

Serve the "chainctl checks" verbs over the Model Context Protocol on stdin and stdout, for an agent such as Claude Code:

  claude mcp add checks -- chainctl checks mcp

Each tool runs one verb with -o json and returns what it prints: checks_status, checks_failures, checks_logs, checks_trace and checks_validate. With --allow-rerun it also serves checks_rerun, the one tool that changes anything. An output over 64 KiB is cut, with a note naming the parameters that narrow it.

The flags given here (--sandbox-url, --parent, --token) are passed to every verb that takes them. Nothing is asked on the terminal: a missing login is the verb's error.

```
chainctl checks mcp [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--allow-rerun]
```

### Options

```
      --allow-rerun          Also serve checks_rerun, which reruns a Run's checks.
      --parent string        The organization or folder (name or ID) the Runs are in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --token string         Bearer token for the sandbox host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
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

* [chainctl checks](/platform/chainctl/chainctl-docs/chainctl_checks/)	 - Inspect and manage a repository's Checks on the Chainguard sandbox plane.

