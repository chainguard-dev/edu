---
date: 2026-10-28T16:22:54Z
title: "chainctl develop github"
slug: chainctl_develop_github
url: /platform/chainctl/chainctl-docs/chainctl_develop_github/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop github

Connect your GitHub account to development sessions.

### Synopsis

Connect your GitHub account once with login, and the sessions you create from then on act on GitHub as you: every git and gh request such a session makes is served with your own GitHub account, through the sandbox plane's develop GitHub App (status names it; it is not the App that runs CI), as far as the App's permissions, its installations, and your own access allow. That holds in every group whose policy does not ban it (user_github, see chainctl develop policy); a group that bans it creates sessions that use their github source and bindings instead. A session keeps the GitHub identity it was created with: logging in or out never changes an existing session's, and a session that acts as you refuses git and gh requests after you log out. The connection refreshes itself until you log out or GitHub revokes it.

No token is written to this machine or shown: the control plane keeps the account's authorization, sealed, and hands it to no one but the requests your own sessions make.

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
* [chainctl develop github login](/platform/chainctl/chainctl-docs/chainctl_develop_github_login/)	 - Connect your GitHub account to development sessions.
* [chainctl develop github logout](/platform/chainctl/chainctl-docs/chainctl_develop_github_logout/)	 - Disconnect your GitHub account from development sessions.
* [chainctl develop github status](/platform/chainctl/chainctl-docs/chainctl_develop_github_status/)	 - Show the GitHub account connected to your development sessions.

