---
date: 2025-04-10T09:56:58Z
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
chainctl iam identity-providers create --parent ORGANIZATION_NAME | ORGANIZATION_ID [--name=NAME] [--description=DESCRIPTION] --oidc-issuer=ISSUER --oidc-client-id=CLIENTID --oidc-client-secret=CLIENTSECRET [--oidc-additional-scopes=SCOPE,...] --default-role=ROLE [--output=id|json|table]
```

### Examples

```
  # Setup a custom OIDC provider and bind new users to the viewer role
  chainctl iam identity-provider create --name=google --parent=example \
  --oidc-issuer=https://accounts.google.com \
  --oidc-client-id=foo \
  --oidc-client-secret=bar \
  --default-role=viewer
```

### Options

```
      --configuration-type string            Type of identity provider. Only OIDC supported currently (default "OIDC")
      --default-role string                  Role to grant users on first login
      --description string                   Description of identity provider
  -h, --help                                 help for create
      --name string                          Name of identity provider
      --oidc-additional-scopes stringArray   additional scopes to request for OIDC type identity provider
      --oidc-client-id string                client id for OIDC type identity provider
      --oidc-client-secret string            client secret for OIDC type identity provider
      --oidc-issuer string                   Issuer URL for OIDC type identity provider
      --parent string                        The name or ID of the location the identity provider belongs to.
  -y, --yes                                  Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identity-providers](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/)	 - customer managed identity provider management

