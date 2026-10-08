---
date: 2026-10-07T14:01:35Z
title: "chainctl iam identities create delegate"
slug: chainctl_iam_identities_create_delegate
url: /platform/chainctl/chainctl-docs/chainctl_iam_identities_create_delegate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities create delegate

Create a delegate: an identity that acts only on grants you mint for it.

### Synopsis

Create a delegate: an identity that acts only on grants you mint for it.

A delegate holds no role bindings and cannot be assumed directly. Its only
use is the delegated exchange of a grant minted by its subject with
"chainctl auth token --delegate=NAME". The exchanged token's subject is the
delegate, it records you as the actor, and it carries at most the grant's
capabilities within the delegate's organization.

The delegate pins your identity as its subject (or --subject, which requires
permission to create identities), this environment's issuer, and a randomly
generated delegation audience that grants for it are minted for.

Grants are stateless, so there is no per-grant list or revoke. Deleting the
delegate stops every future exchange; grants already minted for it expire
within 60 minutes.

```
chainctl iam identities create delegate NAME [--parent=PARENT] [--description=DESC] [--subject=IDENTITY_ID] [--yes] [--output=id|json|table]
```

### Examples

```
  # Create a delegate in an organization and mint a grant for it.
  chainctl iam identities create delegate my-delegate --parent=my-org
  chainctl auth token --delegate=my-delegate --role=viewer --scope=ORGANIZATION_ID
  
  # As an administrator, create a delegate for another user.
  chainctl iam identities create delegate their-delegate --parent=my-org --subject=IDENTITY_ID
```

### Options

```
  -d, --description string   The description of the resource.
  -n, --name string          Given name of the resource.
      --parent string        The name or id of the parent location to create this identity under. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --subject string       The Chainguard identity ID allowed to mint grants for this delegate (default: your own).
  -y, --yes                  Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identities create](/platform/chainctl/chainctl-docs/chainctl_iam_identities_create/)	 - Create a new identity.

