---
date: 2023-12-21T20:37:17Z
title: "chainctl iam identities create github"
slug: chainctl_iam_identities_create_github
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create_github/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities create github



```
chainctl iam identities create github NAME --github-repo=REPO [--github-ref=REF] [--github-audience=AUD] [--group=GROUP] [--description=DESC] [--role=ROLE] [--output id|table|json]
```

### Examples

```
  # Create a GitHub Actions identity for any branch in a repo
  chainctl iam identities create github my-gha-identity --github-repo=my-org/repo-name --group=eng-group
  
  # Create a GitHub Actions identity for a given branch in a repo and bind to a role
  chainctl iam identities create github my-gha-identity --github-repo=my-org/repo-name --github-ref=refs/heads/test-branch --role=owner
```

### Options

```
  -d, --description string       The description of the resource.
      --github-audience string   The audience for the GitHub OIDC token
      --github-ref string        The branch reference for the executing action (optional).
      --github-repo string       The name of a GitHub repo where the action executes.
      --group string             The name or id of the parent group to create this identity under.
  -h, --help                     help for github
  -n, --name string              Given name of the resource.
      --role string              The name or ID of a role to bind this identity to (optional).
  -y, --yes                      Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identities create](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/)	 - Create a new identity.

