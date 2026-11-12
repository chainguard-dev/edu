---
date: 2026-11-11T10:22:55Z
title: "chainctl plans quotas list"
slug: chainctl_plans_quotas_list
url: /platform/chainctl/chainctl-docs/chainctl_plans_quotas_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl plans quotas list

List quotas and usage for each product.

### Synopsis

List plan limits and current usage. Usage figures include amounts above
your plan's included allowance. With --near, show only quotas that are near
or at their limits. Unmeasured usage is shown as a dash.
Exit with status 1 if any requested product's usage is unavailable, including
when --near produces no rows. JSON uses the API's protobuf schema.

```
chainctl plans quotas list [--parent ORG] [--product PRODUCT,...] [--near] [--output=json|table] [flags]
```

### Options

```
      --near              Only show quotas near or at their limits.
      --parent string     Name, path, or UIDP of the organization or one of its folders.
      --product strings   Only show these products: images, helm-charts, libraries, packages, skills, actions, checks, workspaces, platform.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl plans quotas](/platform/chainctl/chainctl-docs/chainctl_plans_quotas/)	 - Show plan limits and current usage.

