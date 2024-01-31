---
date: 2024-01-30T18:15:44Z
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

Subscribe to events under a group.

```
chainctl events subscriptions create SINK_URL [--group GROUP_NAME | GROUP_ID] [--yes] [--output table|json|id] [flags]
```

### Options

```
      --group string   The parent group name or id of the subscription.
  -h, --help           help for create
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl events subscriptions](/chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions/)	 - Subscription interactions.

