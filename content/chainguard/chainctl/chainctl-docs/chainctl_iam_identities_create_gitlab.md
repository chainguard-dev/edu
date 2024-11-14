---
date: 2024-11-13T00:36:09Z
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
chainctl iam identities create gitlab NAME --project-path=GITLAB-GROUP/GITLAB-PROJECT --ref-type={tag|branch} [--ref=REF] [--parent=PARENT] [--description=DESC] [--role=ROLE,ROLE,...] [--output=id|json|table]
```

### Examples

```
  # Create a Gitlab CI identity for any branch in a given Gitlab project
  chainctl iam identities create gitlab my-gitlab-identity --project-path=my-group/my-project --ref-type=branch --parent=eng-org
  
  # Create a Gitlab CI identity for a given branch in a Gitlab project and bind to a role
  chainctl iam identities create gitlab my-gitlab-identity --project-path=my-group/my-project --ref-type=branch --ref=main --role=owner
```

### Options

```
  -d, --description string    The description of the resource.
  -h, --help                  help for gitlab
  -n, --name string           Given name of the resource.
      --parent string         The name or id of the parent location to create this identity under.
      --project-path string   The name of a Gitlab project where the action executes in the form "group-name/project-name[/foo/bar]". You can use a "*" for project-name (or sub-projects) to match any project in the group.
      --ref string            The reference for the executing action. If left empty or "*", all references will match.
      --ref-type string       The type of reference for the executing action, must be either "tag" or "branch".
      --role strings          A comma separated list of names or IDs of roles to bind this identity to (optional).
  -y, --yes                   Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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
  -o, --output string      Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam identities create](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/)	 - Create a new identity.

