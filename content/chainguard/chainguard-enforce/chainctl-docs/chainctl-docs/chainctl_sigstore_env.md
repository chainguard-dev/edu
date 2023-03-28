---
date: 2023-03-28T14:50:08Z
title: "chainctl sigstore env"
slug: chainctl_sigstore_env
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_sigstore_env/
draft: false
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
      --group string   The name or id of the parent group to list sigstore instances from.
  -h, --help           help for env
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl sigstore](/chainguard/chainguard-enforce/chainctl-docs/chainctl_sigstore/)	 - Sigstore related commands for the Chainguard platform.

