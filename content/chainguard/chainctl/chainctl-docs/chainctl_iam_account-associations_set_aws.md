---
date: 2024-03-15T22:44:21Z
title: "chainctl iam account-associations set aws"
slug: chainctl_iam_account-associations_set_aws
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set_aws/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations set aws

Set AWS account association for a location.

```
chainctl iam account-associations set aws ORGANIZATION_NAME|ORGANIZATION_ID|FOLDER_NAME|FOLDER_ID --account=ACCOUNT [--name=NAME] [--description=DESCRIPTION] [--yes] [--output table|json|id] [flags]
```

### Options

```
      --account string       The AWS account ID.
  -d, --description string   The description of the resource.
  -h, --help                 help for aws
  -n, --name string          Given name of the resource.
  -y, --yes                  Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam account-associations set](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set/)	 - Set cloud provider account associations for a location.

