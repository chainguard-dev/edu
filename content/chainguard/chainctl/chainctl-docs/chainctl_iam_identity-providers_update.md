---
date: 2023-04-24T22:08:04Z
title: "chainctl iam identity-providers update"
slug: chainctl_iam_identity-providers_update
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identity-providers update

Update an identity provider

```
chainctl iam identity-providers update IDENTITY_PROVIDER_ID [--name=NAME] [--description=DESCRIPTION] [--configuration-type=TYPE] [--oidc-issuer=ISSUER] [--oidc-client-id=CLIENTID] [--oidc-client-secret=CLIENTSECRET] [--oidc-additional-scopes=SCOPES] [--output table|json|id]
```

### Examples

```
  # Update name and description of an identity provider
  chainctl iam identity-provider update fb694596eb1678321f94eec283e1e0be690f655c/a2973bac66ebfde3 --name=new-name --description=new-description
```

### Options

```
      --configuration-type string            Type of identity provider. Only OIDC supported currently (default "OIDC")
      --description string                   Description of identity provider
  -h, --help                                 help for update
      --name string                          Name of identity provider
      --oidc-additional-scopes stringArray   additional scopes to request for OIDC type identity provider
      --oidc-client-id string                client id for OIDC type identity provider
      --oidc-client-secret string            client secret for OIDC type identity provider
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

