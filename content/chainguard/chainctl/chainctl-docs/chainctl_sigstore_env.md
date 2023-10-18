---
date: 2023-10-18T20:04:31Z
title: "chainctl sigstore env"
slug: chainctl_sigstore_env
url: /chainguard/chainctl/chainctl-docs/chainctl_sigstore_env/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl sigstore env

Print Sigstore related environment variables to configure your environment.

```
chainctl sigstore env [SIGSTORE_ID | SIGSTORE_NAME] [flags]
```

### Examples

```
  eval $(chainctl sigstore env)
```

### Options

```
      --group string               The name or id of the parent group to list sigstore instances from.
  -h, --help                       help for env
      --identity string            The unique ID of the identity to assume when logging in.
      --identity-provider string   The unique ID of the customer managed identity provider to authenticate with
      --org-name string            Organization to use for authentication. If configured the organization's custom identity provider will be used
  -y, --yes                        Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

