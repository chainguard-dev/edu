---
date: 2025-04-14T14:32:57Z
title: "chainctl iam account-associations set gcp"
slug: chainctl_iam_account-associations_set_gcp
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set_gcp/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam account-associations set gcp

Set GCP account association for a location.

```
chainctl iam account-associations set gcp ORGANIZATION_NAME|ORGANIZATION_ID|FOLDER_NAME|FOLDER_ID --project-id=PROJECT_ID --project-number=PROJECT_NUMBER [--name=NAME] [--description=DESCRIPTION] [--yes] [--output=id|json|table] [flags]
```

### Options

```
  -d, --description string      The description of the resource.
  -h, --help                    help for gcp
  -n, --name string             Given name of the resource.
      --project-id string       The GCP project ID.
      --project-number string   The GCP project number.
  -y, --yes                     Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam account-associations set](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set/)	 - Set cloud provider account associations for a location.

