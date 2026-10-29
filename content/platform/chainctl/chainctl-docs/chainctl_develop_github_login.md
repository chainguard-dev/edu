---
date: 2026-10-28T16:22:54Z
title: "chainctl develop github login"
slug: chainctl_develop_github_login
url: /platform/chainctl/chainctl-docs/chainctl_develop_github_login/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop github login

Connect your GitHub account to development sessions.

### Synopsis

Open a browser to authorize the sandbox plane's develop GitHub App as your GitHub account, and hand the authorization to the sandbox plane: the sessions you create from then on act on GitHub as you, in every group whose policy does not ban it. Logging in does not depend on any group's policy, and changes no existing session. An earlier connection is replaced. If the App is not installed on your own account, how to install it is printed: sessions reach only repositories where it is installed. An owner of an organization installs it there, and a member can request it; pushing to your own repositories and forks needs it on your own account. An organization that requires SAML single sign-on needs an active single sign-on session in the browser first.

```
chainctl develop github login [--port PORT] [--output=json]
```

### Options

```
      --port int   Local loopback port for the GitHub OAuth callback. (default 8989)
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

