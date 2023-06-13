---
date: 2023-06-13T17:58:41Z
title: "chainctl iam identity-providers create"
slug: chainctl_iam_identity-providers_create
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers create

Create an identity provider

```
chainctl iam identity-providers create [--group=GROUP] [--name=NAME] [--description=DESCRIPTION] [--configuration-type=TYPE] [--oidc-issuer=ISSUER] [--oidc-client-id=CLIENTID] [--oidc-client-secret=CLIENTSECRET] [--oidc-additional-scopes=SCOPES] [--output table|json|id]
```

### Examples

```
  # Bind a user-created identity as viewer to a group
  chainctl iam identity-provider create --group=example --name=google --oidc-issuer=https://accounts.google.com --oidc-client-id=foo --oidc-client-secret=bar
```

### Options

```
      --configuration-type string            Type of identity provider. Only OIDC supported currently (default "OIDC")
      --description string                   Description of identity provider
      --group string                         The name or ID of the group the identity provider belongs to.
  -h, --help                                 help for create
      --name string                          Name of identity provider
      --oidc-additional-scopes stringArray   additional scopes to request for OIDC type identity provider
      --oidc-client-id string                client id for OIDC type identity provider
      --oidc-client-secret string            client secret for OIDC type identity provider
      --oidc-issuer string                   Issuer URL for OIDC type identity provider
  -y, --yes                                  Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam identity-providers](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

