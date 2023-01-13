---
date: 2022-12-15T19:03:53-05:00
title: "chainctl policies apply"
slug: chainctl_policies_apply
url: /chainguard/chainguard-enforce/chainctl-docs/chainctl_policies_apply/
draft: false
images: []
type: "article"
toc: true
---
## chainctl policies apply

Create or update a policy described by file or stdin.

```
chainctl policies apply [--group GROUP_NAME|GROUP_ID] [--description DESCRIPTION] [--filename FILENAME]... [--recursive] [--yes] [--output table|json|id] [flags]
```

### Options

```
  -d, --description string   The description of the policy.
  -f, --filename strings     Filename, directory, or URL to files to use to create or update the resource
      --group string         The parent group id of the policy.
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
      --timestamp_authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
```

### SEE ALSO

* [chainctl policies](/chainguard/chainguard-enforce/chainctl-docs/chainctl_policies/)	 - Policy related commands for the Chainguard platform.

