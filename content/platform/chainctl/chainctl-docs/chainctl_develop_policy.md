---
date: 2026-10-28T16:22:54Z
title: "chainctl develop policy"
slug: chainctl_develop_policy
url: /platform/chainctl/chainctl-docs/chainctl_develop_policy/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop policy

Show or change the group's policy for development sessions.

### Synopsis

The group's policy applies to every development session in it. org_github is what the organization's GitHub App may serve a session whose github source is ORG:
  bound (the default): the session's own repository, and any other repository the owner bound (chainctl develop SESSION --with github:OWNER/REPO[+push], or a checkout's other remotes, bound at create) while the group was bound, with a token minted for that repository and operation alone. This laptop's credential is never spent on another repository.
  session: the session's own repository only; other repositories go to the attached laptop.
  off: nothing; an ORG source on github is refused.

org_github_push_beyond_session (on by default) is whether, under bound, the App may push to a repository other than the session's own when a binding grants it; off refuses every such push, leaving the session's own repository the only one the App pushes to.

user_github (allowed by default) is whether sessions may act on GitHub as their owner. A session acts as its owner when the owner has connected a GitHub account (chainctl develop github login) and the group allows it when the session is created: every git and gh request it makes is then served with the owner's own GitHub account, through the sandbox plane's develop GitHub App (chainctl develop github status names it), not the App that runs CI, whatever its github source and bindings say. Set it to false to ban this: new sessions use the github source and bindings, and sessions already acting as their owner have their GitHub requests refused until they are replaced. The policy can only allow or ban; it never makes an owner act on GitHub as themselves, and allowing it again changes no existing session.

Any session owner in the group can read the policy. Changing it takes the permission to list every owner's sessions in the group; sessions see a change at their next request.

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
* [chainctl develop policy describe](/platform/chainctl/chainctl-docs/chainctl_develop_policy_describe/)	 - Show the group's policy for development sessions.
* [chainctl develop policy set](/platform/chainctl/chainctl-docs/chainctl_develop_policy_set/)	 - Change the group's policy for development sessions.

