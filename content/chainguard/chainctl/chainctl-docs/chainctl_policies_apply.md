---
date: 2023-05-25T17:06:13Z
title: "chainctl policies apply"
slug: chainctl_policies_apply
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_apply/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies apply

Create or update a policy described by file or stdin.

```
chainctl policies apply [--group=GROUP_NAME | GROUP_ID] [--description=DESCRIPTION] [--filename=FILENAME]... [--recursive] [--yes] [--output table|json|id] [flags]
```

### Examples

```
  # Apply a policy document from disk to the "eng" group
  chainctl policy apply --filename=images-are-signed.yaml --group=eng
  
  # Apply an updated policy document to an existing policy, automatically respond yes to confirmation prompts
  chainctl policy apply -f images-are-signed-v2.yaml --group=eng --yes
  
  # Apply a policy document from stdin, interactively choose the group to apply the policy to
  chainctl policy apply -f -
```

### Options

```
  -d, --description string   The description of the policy.
  -f, --filename strings     Filename, directory, or URL to files to use to create or update the resource
      --group string         The parent group name or id of the policy.
  -h, --help                 help for apply
  -R, --recursive            Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.
  -y, --yes                  Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl policies](/chainguard/chainctl/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

