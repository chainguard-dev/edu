---
date: 2023-04-19T23:22:15Z
title: "chainctl iam identities create"
slug: chainctl_iam_identities_create
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities create

Create a new identity.

```
chainctl iam identities create NAME {--filename FILE | {--identity-issuer=ISS | --identity-issuer-pattern=PAT} {--subject=SUB | --subject-pattern=PAT} [--audience=AUD | --audience-pattern=PAT] | --identity-issuer=ISS --issuer-keys=KEYS --subject=SUB [--expiration=yyyy-mm-dd]} [--group=GROUP] [--description=DESC] [--role=ROLE] [--output id|table|json]
```

### Examples

```
  # Create a static identity using the default expiration.
  chainctl iam identities create my-identity --identity-issuer=https://issuer.mycompany.com --issuer-keys=deadbeef --subject=1234
  
  # Create an identity with literal values to match from claims.
  chainctl iam identities create my-identity --identity-issuer=https://issuer.mycompany.com --subject=1234
  
  # Create an identity using patterns to match claims
  chainctl iam identities create my-identity --identity-issuer-pattern="https://*.mycompany\.com" --subject-pattern="^\d{4}$"
  
  # Create an identity from a JSON file definition and bind to a role
  chainctl iam identities create my-identity -f path/to/identity-definition.json --role=viewer
```

### Options

```
      --audience string                  The audience of the identity (optional).
      --audience-pattern string          A pattern to match the audience of the identity (optional).
      --claim_pattern stringArray        A comma-separated list of claim:pattern pairs of custom claims to match for this identity (optional).
  -d, --description string               The description of the resource.
      --expiration string                The time when the issuer_keys will expire. Defaults to / Maximum of 30 days after creation time (yyyy-mm-dd).
  -f, --filename string                  A file that contains the identity definition, in either YAML or JSON.
      --group string                     The name or id of the parent group to create this identity under.
  -h, --help                             help for create
      --identity-issuer string           The issuer of the identity.
      --identity-issuer-pattern string   A pattern to match the issuer of the identity.
      --issuer-keys string               JWKS-formatted public keys for the issuer.
  -n, --name string                      Given name of the resource.
      --role string                      The name or ID of a role to bind this identity to (optional).
      --service-principal string         The service principal that is allowed to assume this identity.
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

* [chainctl iam identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/)	 - Identity management.
* [chainctl iam identities create github](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create_github/)	 - 
* [chainctl iam identities create gitlab](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create_gitlab/)	 - 

