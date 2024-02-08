---
date: 2024-02-08T16:54:31Z
title: "chainctl iam organizations update"
slug: chainctl_iam_organizations_update
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_organizations_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam organizations update

Update an organization.

```
chainctl iam organizations update ORGANIZATION_NAME | ORGANIZATION_ID [--name ORGANIZATION_NAME] [--description ORGANIZATION_DESCRIPTION]
```

### Examples

```

# Update an organization's name
chainctl iam organizations update my-org --name new-org-name

# Update an organization's description
chainctl iam organizations update 19d3a64f20c64ba3ccf1bc86ce59d03e705959ad --description "A description of the organization."

# Remove an organizations's description
chainctl iam organizations update my-org --description ""
```

### Options

```
  -d, --description string   The updated description for the organization.
  -h, --help                 help for update
  -n, --name string          The updated name for the organization.
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

* [chainctl iam organizations](/chainguard/chainctl/chainctl-docs/chainctl_iam_organizations/)	 - IAM organization interactions.

