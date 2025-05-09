---
date: 2025-05-08T22:32:31Z
title: "chainctl iam invites create"
slug: chainctl_iam_invites_create
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_invites_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam invites create

Generate an invite code to identities with Chainguard.

```
chainctl iam invites create [ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID] [--role=ROLE_ID|ROLE_NAME] [--ttl=TTL_DURATION] [--email=EMAIL] [--single-use] [--output=id|json|table]
```

### Examples

```

# Create an invite that will be valid for 5 days:
chainctl iam invite create my-org-name --role=viewer --ttl=5d

# Create an invite that only Kim can accept:
chainctl iam invite create my-org-name --email=kim@example.com

# Create an invite code that can only be used once.
chainctl iam invite create my-org-name --single-use

```

### Options

```
      --email string   The email address that is allowed to accept this invite code.
  -h, --help           help for create
      --role string    Role is used to role-bind the invited to the associated location.
      --single-use     The invite can only be used once before it is invalidated.
      --ttl duration   Duration the invite code will be valid. (default 168h0m0s)
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

* [chainctl iam invites](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites/)	 - Manage invite codes that register identities with Chainguard.

