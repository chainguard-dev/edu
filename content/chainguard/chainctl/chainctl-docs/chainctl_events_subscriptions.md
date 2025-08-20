---
date: 2025-08-19T19:52:13Z
title: "chainctl events subscriptions"
slug: chainctl_events_subscriptions
url: /chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl events subscriptions

Subscription interactions.

### Options

```
  -h, --help   help for subscriptions
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl events](/chainguard/chainctl/chainctl-docs/chainctl_events/)	 - Events related commands for the Chainguard platform.
* [chainctl events subscriptions create](/chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions_create/)	 - Subscribe to events under an organization or folder.
* [chainctl events subscriptions delete](/chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions_delete/)	 - Delete a subscription.
* [chainctl events subscriptions list](/chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions_list/)	 - List subscriptions.

