---
date: 2023-02-17T21:22:59Z
title: "chainctl policies delete"
slug: chainctl_policies_delete
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_delete/
draft: false
images: []
type: "article"
toc: true
---
## chainctl policies delete

Delete a policy.

```
chainctl policies delete [POLICY_NAME | POLICY_ID] [--yes] [--output id] [flags]
```

### Options

```
  -h, --help   help for delete
  -y, --yes    Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string              The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
```

### SEE ALSO

* [chainctl policies](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

