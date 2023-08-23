---
date: 2023-08-23T00:12:48Z
title: "chainctl sigstore ca describe"
slug: chainctl_sigstore_ca_describe
url: /chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl sigstore ca describe

Describe a certificate authority instance.

```
chainctl sigstore ca describe [SIGSTORE_NAME | SIGSTORE_ID] [--output |json] [flags]
```

### Examples

```
  # Describe a sigstore certiicate authority
  chainctl sigstore ca describe my-ca
```

### Options

```
  -h, --help   help for describe
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

* [chainctl sigstore ca](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca/)	 - Sigstore commands related to certificate authorities

