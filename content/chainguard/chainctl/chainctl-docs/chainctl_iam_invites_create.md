---
date: 2023-04-18T22:50:50Z
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

Generate an invite code to identities or register clusters with Chainguard.

```
chainctl iam invites create [GROUP_NAME | GROUP_ID] [--role ROLE_ID|ROLE_NAME | --cluster] [--ttl TTL_DURATION] [--output json|table|id] [flags]
```

### Examples

```

# Create an invite that will be valid for 5 days:
chainctl iam invite create GROUP_ID --role ROLE_ID --ttl 5d

# Create an invite that only Kim can accept:
chainctl iam invite create GROUP_ID --role ROLE_ID --email kim@example.com

# Create an invite for a cluster:
chainctl iam invite create GROUP_ID --cluster

```

### Options

```
      --cluster        Default roles for cluster invites.
      --email string   The email address that is allowed to accept this invite code.
  -h, --help           help for create
      --role string    Role is used to role-bind the invited to the associated group.
      --ttl duration   Duration the invite code will be valid. (default 168h0m0s)
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

* [chainctl iam invites](/chainguard/chainctl/chainctl-docs/chainctl_iam_invites/)	 - Manage invite codes that register identities or clusters with Chainguard.

