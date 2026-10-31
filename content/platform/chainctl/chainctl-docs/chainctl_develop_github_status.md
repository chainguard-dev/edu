---
date: 2026-10-30T14:11:50Z
title: "chainctl develop github status"
slug: chainctl_develop_github_status
url: /platform/chainctl/chainctl-docs/chainctl_develop_github_status/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop github status

Show the GitHub account connected to your development sessions.

### Synopsis

Show the GitHub account connected to your development sessions, the GitHub App it is connected through, whether its authorization still works, and whether the group's policy allows sessions to act on GitHub as their owner (user_github), and which accounts the App must be installed on for sessions on the checkout in the working directory: the repository it is a copy of, and the fork its branch pushes to, with where each missing one is installed.

```
chainctl develop github status [--output=json|table]
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

* [chainctl develop github](/platform/chainctl/chainctl-docs/chainctl_develop_github/)	 - Connect your GitHub account to development sessions.

