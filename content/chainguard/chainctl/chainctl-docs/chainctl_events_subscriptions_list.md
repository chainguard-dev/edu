---
date: 2023-11-15T09:28:36Z
title: "chainctl events subscriptions list"
slug: chainctl_events_subscriptions_list
url: /chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl events subscriptions list

List subscriptions.

```
chainctl events subscriptions list [--group GROUP_NAME | GROUP_ID] [--output table|json|id] [flags]
```

### Options

```
      --group string   The parent group name or id of the subscription.
  -h, --help           help for list
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl events subscriptions](/chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions/)	 - Subscription interactions.

