---
date: 2024-03-14T15:41:40Z
title: "chainctl iam organizations describe"
slug: chainctl_iam_organizations_describe
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_organizations_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam organizations describe

Describe an organization.

```
chainctl iam organizations describe [ORGANIZATION_NAME | ORGANIZATION_ID] [--active-within=DURATION] [--output json]
```

### Options

```
      --active-within duration   How recently a record must have been active to be listed. Zero will return all records. (default 24h0m0s)
  -h, --help                     help for describe
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

