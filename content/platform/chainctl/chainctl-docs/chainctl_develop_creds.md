---
date: 2026-11-27T13:55:02Z
title: "chainctl develop creds"
slug: chainctl_develop_creds
url: /platform/chainctl/chainctl-docs/chainctl_develop_creds/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop creds

Show or change a development session's credentials.

### Synopsis

With no flag, show the session's credentials: each one's source ("default" when no one has written it), its bindings, and what this laptop remembers for it; who is serving the laptop's credentials right now; and the latest entries of the audited consent trail. -o json prints all three.

To reach more, use chainctl develop SESSION --with ENTRY. To take something back or change where a credential comes from:
  --revoke ENTRY (claude, cgr.dev, chainguard, mcp, mcp:NAME, connector:NAME, github:OWNER/REPO[+push]; repeatable) removes it from the session, audited, and from this laptop's remembered entries; github:OWNER/REPO+push takes back the push alone. For what this laptop approves without asking — claude, chainguard, the session's own repository, a fetch of a remote of its checkout — it also remembers a deny, which a later --with ENTRY takes back. connector:NAME (a claude.ai connector's name or id) turns that connector off on this laptop for every session and denies it on this session, whichever laptop pushes, and it stops working there now. mcp turns every laptop MCP server off for the session; mcp:NAME (a remote MCP server as claude mcp list names it) turns that server off on this laptop for every session, and it stops working in this one now.
  --connectors (or --mcp) shows the checklist of this laptop's claude.ai connectors and Claude Code remote MCP servers that attaching shows when a new one appears, filled in with your answers: one you uncheck stops working in the session now, and one you check works there now. The answers hold for every session.
  --forget removes everything this laptop remembers for the session's repository, and writes nothing to the session.
  --source HOST=laptop|org|owner|off (repeatable) writes where a credential comes from, audited: laptop is this machine (and remembers claude or cgr.dev allowed here), org the organization's credential, off nothing (and both forget what this laptop remembered allowing), owner your own login held by Chainguard, which the plane serves with no laptop attached (claude, after chainctl develop claude login). chainguard takes off alone here; turn it back on with --with chainguard.

Remembered entries live in this laptop's chainctl config directory (develop/approvals.json, mode 0600) and apply to every session on the same group and repository. Nothing the control plane sends writes them. Names, sources, and scopes only; no credential is ever on the trail or in the file.

```
chainctl develop creds SESSION [--revoke ENTRY]... [--forget] [--source HOST=laptop|org|owner|off]... [--connectors] [--output=json|table]
```

### Options

```
      --connectors           choose which of this laptop's claude.ai connectors and MCP servers sessions use, on a checklist
      --forget               remove everything this laptop remembers for the session's repository; nothing is written to the session
      --revoke stringArray   take back an entry: claude, cgr.dev, chainguard, mcp, mcp:NAME (one laptop MCP server), connector:NAME (one claude.ai connector), github:OWNER/REPO, or github:OWNER/REPO+push (the push alone); repeatable
      --source stringArray   where a credential comes from, HOST=laptop|org|owner|off; repeatable
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

