---
date: 2023-06-06T19:56:49Z
title: "chainctl sigstore ca delete"
slug: chainctl_sigstore_ca_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl sigstore ca delete

Delete a certificate authority instance.

```
chainctl sigstore ca delete SIGSTORE_ID [--yes] [flags]
```

### Examples

```
  # Delete a sigstore instance by ID
  chainctl sigstore ca delete e533448ca9770c46f99f2d86d60fc7101494e4a3
  
  # Delete a sigstore instance by name
  chainctl sigstore ca delete my-name
  
  # Delete a sigstore instance by interactive selection
  chainctl sigstore ca delete
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
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl sigstore ca](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca/)	 - Sigstore commands related to certificate authorities

