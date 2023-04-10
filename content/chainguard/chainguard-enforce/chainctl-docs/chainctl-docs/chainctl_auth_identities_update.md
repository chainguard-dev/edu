---
date: 2023-04-10T21:58:49Z
title: "chainctl auth identities update"
slug: chainctl_auth_identities_update
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_identities_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth identities update

Update an identity

```
chainctl auth identities update IDENTITY_NAME | IDENTITY_ID [--description=DESC] [--identity-issuer=ISS | --identity-issuer-pattern=PAT] [--subject=SUB | --subject-pattern=PAT] [--audience=AUD | --audience-pattern=PAT] [--issuer-keys=KEYS] [--expiration=yyyy-mm-dd] [--output table|id|json] [flags]
```

### Examples

```
  # Update the issuer of an identity.
  chainctl auth identities update my-identity --identity-issuer=https://new-issuer.mycompany.com
  
  # Update the subject to a pattern and update the audience of an identity.
  chainctl auth identities update my-identity --subject-pattern="^\d{4}$" --audience=some-audience
```

### Options

```
      --audience string                  The audience of the identity (optional).
      --audience-pattern string          A pattern to match the audience of the identity (optional).
      --description string               A description of the identity (optional).
      --expiration string                The time when the issuer_keys will expire. Defaults to / Maximum of 30 days after creation time (yyyy-mm-dd).
  -h, --help                             help for update
      --identity-issuer string           The issuer of the identity.
      --identity-issuer-pattern string   A pattern to match the issuer of the identity.
      --issuer-keys string               JWKS-formatted public keys for the issuer.
      --subject string                   The subject of the identity.
      --subject-pattern string           A pattern to match the subject of the identity.
  -y, --yes                              Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl auth identities](/chainguard/chainguard-enforce/chainctl-docs/chainctl_auth_identities/)	 - Identity management.

