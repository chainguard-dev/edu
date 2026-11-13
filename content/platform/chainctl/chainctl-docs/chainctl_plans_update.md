---
date: 2026-11-12T21:48:09Z
title: "chainctl plans update"
slug: chainctl_plans_update
url: /platform/chainctl/chainctl-docs/chainctl_plans_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl plans update

Move your organization to another plan.

### Synopsis

Move your organization to another plan.

With --plan team, this opens a hosted checkout page where an owner
enters a card. Nothing is charged on the page itself. The organization
moves to Team once the card is charged, which usually follows within a
minute but can take up to an hour. Until then it stays on Starter and
'chainctl plans describe' still reads Starter.

The upgrade makes the purchaser an owner of the organization. The
command waits up to 15 minutes for that, refreshing your local token
until it carries the owner role. With --no-wait or --output json it
exits once the checkout page is shown; run 'chainctl auth login' once
the organization is on Team.

With --plan enterprise or --plan starter, the command tells you how to
ask Chainguard for the change.

To cancel Team, contact Chainguard support.

```
chainctl plans update --plan team|enterprise|starter [--parent ORG] [--no-browser] [--no-wait] [--output=json|table] [flags]
```

### Options

```
      --no-browser      Print the checkout URL instead of opening it in a browser.
      --no-wait         Exit once the checkout page is shown, instead of waiting for the organization to move to Team.
      --parent string   The name or id of the organization whose plan to change.
      --plan string     The plan to move to: team, enterprise, or starter.
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

* [chainctl plans](/platform/chainctl/chainctl-docs/chainctl_plans/)	 - Show your organization's plan, limits, and usage.

