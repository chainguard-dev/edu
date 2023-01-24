---
date: 2023-01-24T12:45:29-05:00
title: "chainctl sigstore ca"
slug: chainctl_sigstore_ca
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_sigstore_ca/
draft: false
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
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string              The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
```

### SEE ALSO

* [chainctl sigstore](/chainguard/chainguard-enforce/chainctl-docs/chainctl_sigstore/)	 - Sigstore related commands for the Chainguard platform.
* [chainctl sigstore ca create](/chainguard/chainguard-enforce/chainctl-docs/chainctl_sigstore_ca_create/)	 - Create a certificate authority instance.
* [chainctl sigstore ca delete](/chainguard/chainguard-enforce/chainctl-docs/chainctl_sigstore_ca_delete/)	 - Delete a certificate authority instance.
* [chainctl sigstore ca list](/chainguard/chainguard-enforce/chainctl-docs/chainctl_sigstore_ca_list/)	 - List certificate authority instances.

