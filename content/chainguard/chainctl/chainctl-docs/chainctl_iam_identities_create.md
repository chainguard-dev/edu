---
date: 2025-05-30T20:37:58Z
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
chainctl iam identities create NAME {--filename FILE | {--identity-issuer=ISS | --identity-issuer-pattern=PAT} {--subject=SUB | --subject-pattern=PAT} [--audience=AUD | --audience-pattern=PAT] [--claim-pattern=claim:pattern,claim:pattern...] | --identity-issuer=ISS --issuer-keys=KEYS --subject=SUB [--expiration=yyyy-mm-dd]} [--parent=PARENT] [--description=DESC] [--role=ROLE,ROLE,...] [--output=id|json|table]
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
      --claim-pattern stringArray        A comma-separated list of claim:pattern pairs of custom claims to match for this identity (optional).
  -d, --description string               The description of the resource.
      --expiration string                The time when the issuer_keys will expire. Defaults to / Maximum of 30 days after creation time (yyyy-mm-dd).
  -f, --filename string                  A file that contains the identity definition, in either YAML or JSON.
  -h, --help                             help for create
      --identity-issuer string           The issuer of the identity.
      --identity-issuer-pattern string   A pattern to match the issuer of the identity.
      --issuer-keys string               JWKS-formatted public keys for the issuer.
  -n, --name string                      Given name of the resource.
      --parent string                    The name or id of the parent location to create this identity under.
      --role strings                     A comma separated list of names or IDs of roles to bind this identity to (optional).
      --service-principal string         The service principal that is allowed to assume this identity.
      --subject string                   The subject of the identity.
      --subject-pattern string           A pattern to match the subject of the identity.
  -y, --yes                              Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identities](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/)	 - Identity management.
* [chainctl iam identities create github](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create_github/)	 - 
* [chainctl iam identities create gitlab](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create_gitlab/)	 - 

