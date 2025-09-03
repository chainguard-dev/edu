---
date: 2025-09-02T09:39:16Z
title: "chainctl images repos update"
slug: chainctl_images_repos_update
url: /chainguard/chainctl/chainctl-docs/chainctl_images_repos_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images repos update

Update image repositories.

```
chainctl images repos update {REPO_NAME|REPO_ID} --parent ORGANIZATION_NAME | ORGANIZATION_ID
```

### Options

```
  -h, --help            help for update
      --name string     Updated name for the repo.
      --parent string   The name or id of the parent location of the repo to update.
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
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl images repos](/chainguard/chainctl/chainctl-docs/chainctl_images_repos/)	 - Image repo related commands for the Chainguard platform.

