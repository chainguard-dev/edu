---
date: 2023-10-18T20:04:31Z
title: "chainctl iam identities create gitlab"
slug: chainctl_iam_identities_create_gitlab
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create_gitlab/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities create gitlab



```
chainctl iam identities create gitlab NAME --project-path=GITLAB-GROUP/GITLAB-PROJECT [--ref-type=REF-TYPE] [--ref=REF] [--group=GROUP] [--description=DESC] [--role=ROLE] [--output id|table|json]
```

### Examples

```
  # Create a Gitlab CI identity for any branch in a given Gitlab project
  chainctl iam identities create gitlab my-gitlab-identity --project-path=my-group/my-project --ref-type=branch --ref='*' --group=eng-group
  
  # Create a Gitlab CI identity for a given branch in a Gitlab project and bind to a role
  chainctl iam identities create gitlab my-gitlab-identity --project-path=my-group/my-project --ref-type=branch --ref=main --role=owner
```

### Options

```
  -d, --description string    The description of the resource.
      --group string          The name or id of the parent group to create this identity under.
  -h, --help                  help for gitlab
  -n, --name string           Given name of the resource.
      --project-path string   The name of a Gitlab project where the action executes.
      --ref string            The reference for the executing action. (default "*")
      --ref-type string       The type of reference for the executing action (optional).
      --role string           The name or ID of a role to bind this identity to (optional).
  -y, --yes                   Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identities create](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/)	 - Create a new identity.

