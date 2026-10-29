---
date: 2026-10-28T16:22:54Z
title: "chainctl develop policy describe"
slug: chainctl_develop_policy_describe
url: /platform/chainctl/chainctl-docs/chainctl_develop_policy_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop policy describe

Show the group's policy for development sessions.

### Synopsis

Show the group's policy for development sessions: org_github, org_github_push_beyond_session, user_github, its revision, and who last changed it. A group no one has written a policy for shows the defaults at revision 0.

```
chainctl develop policy describe [--output=json|table]
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

