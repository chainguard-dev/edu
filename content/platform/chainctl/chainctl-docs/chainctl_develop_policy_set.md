---
date: 2026-10-30T14:11:50Z
title: "chainctl develop policy set"
slug: chainctl_develop_policy_set
url: /platform/chainctl/chainctl-docs/chainctl_develop_policy_set/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop policy set

Change the group's policy for development sessions.

### Synopsis

Set org_github, org_github_push_beyond_session, user_github, or any of them together on the group's policy for development sessions; only what is given changes. Requires the permission to list every owner's sessions in the group. The change is logged with you as its actor, and every session in the group sees it at its next request.

```
chainctl develop policy set [--org-github session|bound|off] [--org-github-push-beyond-session=true|false] [--user-github=true|false] [--output=json|table]
```

### Options

```
      --org-github string                what the organization's GitHub App may serve: bound, session, or off
      --org-github-push-beyond-session   under bound, whether the organization's GitHub App may push to a repository other than the session's own that a binding grants (default true)
      --user-github                      whether sessions may act on GitHub as their owner, through the develop GitHub App, for owners who connected a GitHub account (chainctl develop github login); false bans it, true restores the default (default true)
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

* [chainctl develop policy](/platform/chainctl/chainctl-docs/chainctl_develop_policy/)	 - Show or change the group's policy for development sessions.

