---
date: 2024-02-21T20:43:07Z
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
chainctl iam identity-providers update IDENTITY_PROVIDER_ID [--name=NAME] [--description=DESCRIPTION] [--oidc-issuer=ISSUER] [--oidc-client-id=CLIENTID] [--oidc-client-secret=CLIENTSECRET] [--oidc-additional-scopes=SCOPE,...] [--default-role=ROLE] [--output table|json|id]
```

### Examples

```
  # Update name and description of an identity provider by ID
  chainctl iam identity-provider update fb694596eb1678321f94eec283e1e0be690f655c/a2973bac66ebfde3 --name=new-name --description=new-description
  
  # Update the default role for an identity provider by name
  chainctl iam identity-provider update my-idp --default=role=viewer
```

### Options

```
      --configuration-type string            Type of identity provider. Only OIDC supported currently (default "OIDC")
      --default-role string                  Optional role to grant users on first login
      --description string                   Description of identity provider
  -h, --help                                 help for update
      --name string                          Name of identity provider
      --oidc-additional-scopes stringArray   additional scopes to request for OIDC type identity provider
      --oidc-client-id string                client id for OIDC type identity provider
      --oidc-client-secret string            client secret for OIDC type identity provider
      --oidc-issuer string                   Issuer URL for OIDC type identity provider
  -y, --yes                                  Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identity-providers](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

