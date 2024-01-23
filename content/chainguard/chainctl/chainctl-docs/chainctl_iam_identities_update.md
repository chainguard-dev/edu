---
date: 2024-01-23T17:19:55Z
title: "chainctl iam identities update"
slug: chainctl_iam_identities_update
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities update

Update an identity

```
chainctl iam identities update IDENTITY_NAME | IDENTITY_ID [--description=DESC] [--identity-issuer=ISS | --identity-issuer-pattern=PAT] [--subject=SUB | --subject-pattern=PAT] [--audience=AUD | --audience-pattern=PAT] [--claim-pattern=claim:pattern,claim:pattern...] [--issuer-keys=KEYS] [--expiration=yyyy-mm-dd] [--output table|id|json] [flags]
```

### Examples

```
  # Update the issuer of an identity.
  chainctl iam identities update my-identity --identity-issuer=https://new-issuer.mycompany.com
  
  # Update the subject to a pattern and update the audience of an identity.
  chainctl iam identities update my-identity --subject-pattern="^\d{4}$" --audience=some-audience
```

### Options

```
      --audience string                  The audience of the identity (optional).
      --audience-pattern string          A pattern to match the audience of the identity (optional).
      --claim-pattern stringArray        A comma-separated list of claim:pattern pairs of custom claims to match for this identity.
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
      --api string       The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --config string    A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string   The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string    The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string    Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int            Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/)	 - Identity management.

