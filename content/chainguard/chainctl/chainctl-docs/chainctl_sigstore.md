---
date: 2024-01-02T20:38:26Z
title: "chainctl sigstore"
slug: chainctl_sigstore
url: /chainguard/chainctl/chainctl-docs/chainctl_sigstore/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl sigstore

Sigstore related commands for the Chainguard platform.

### Options

```
  -h, --help   help for sigstore
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl sigstore ca](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca/)	 - Sigstore commands related to certificate authorities
* [chainctl sigstore env](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_env/)	 - Print Sigstore related environment variables to configure your environment.

