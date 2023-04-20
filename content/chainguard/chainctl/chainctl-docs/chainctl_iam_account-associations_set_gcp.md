---
date: 2023-04-20T17:34:48Z
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

Set GCP account association for a group.

```
chainctl iam account-associations set gcp GROUP_NAME|GROUP_ID --project-id=PROJECT_ID --project-number=PROJECT_NUMBER [--name=NAME] [--description=DESCRIPTION] [--yes] [--output table|json|id] [flags]
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

* [chainctl iam account-associations set](/chainguard/chainctl/chainctl-docs/chainctl_iam_account-associations_set/)	 - Set cloud provider account associations for a group.

