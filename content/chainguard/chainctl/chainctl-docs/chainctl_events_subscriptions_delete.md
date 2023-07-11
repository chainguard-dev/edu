---
date: 2023-07-11T15:35:05Z
title: "chainctl events subscriptions delete"
slug: chainctl_events_subscriptions_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl events subscriptions delete

Delete a subscription.

```
chainctl events subscriptions delete SUBSCRIPTION_ID [--yes] [--output id] [flags]
```

### Options

```
  -h, --help   help for delete
  -y, --yes    Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl events subscriptions](/chainguard/chainctl/chainctl-docs/chainctl_events_subscriptions/)	 - Subscription interactions.

