---
date: 2023-04-17T18:12:16Z
title: "chainctl sigstore ca list"
slug: chainctl_sigstore_ca_list
url: /chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl sigstore ca list

List certificate authority instances.

```
chainctl sigstore ca list [--group GROUP_NAME | GROUP_ID] [--output table|json|id] [flags]
```

### Options

```
      --group string   The name or id of the parent group to list sigstore instances from.
  -h, --help           help for list
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
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl sigstore ca](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca/)	 - Sigstore commands related to certificate authorities

