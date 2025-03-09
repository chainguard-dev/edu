---
date: 2025-03-07T00:03:07Z
title: "chainctl events subscriptions create"
slug: chainctl_events_subscriptions_create
url: /chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl events subscriptions create

Subscribe to events under an organization or folder.

```
chainctl events subscriptions create SINK_URL [--parent ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID] [--yes] [--output=id|json|table]
```

### Options

```
  -h, --help            help for create
      --parent string   The parent location name or id of the subscription.
  -y, --yes             Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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
  -o, --output string      Output format. One of: [csv, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl events subscriptions](/chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions/)	 - Subscription interactions.

