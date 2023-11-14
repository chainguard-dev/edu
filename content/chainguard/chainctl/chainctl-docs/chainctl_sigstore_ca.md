---
date: 2023-11-14T00:08:02Z
title: "chainctl sigstore ca"
slug: chainctl_sigstore_ca
url: /chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl sigstore ca

Sigstore commands related to certificate authorities

### Options

```
  -h, --help   help for ca
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

* [chainctl sigstore](/chainguard/chainctl/chainctl-docs/chainctl_sigstore/)	 - Sigstore related commands for the Chainguard platform.
* [chainctl sigstore ca create](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca_create/)	 - Create a certificate authority instance.
* [chainctl sigstore ca delete](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca_delete/)	 - Delete a certificate authority instance.
* [chainctl sigstore ca describe](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca_describe/)	 - Describe a certificate authority instance.
* [chainctl sigstore ca list](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca_list/)	 - List certificate authority instances.

