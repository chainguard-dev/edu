---
date: 2025-05-15T20:58:46Z
title: "chainctl iam folders describe"
slug: chainctl_iam_folders_describe
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_folders_describe/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam folders describe

Describe a folder.

```
chainctl iam folders describe [FOLDER_NAME | FOLDER_ID] [--active-within=DURATION] [--output=json]
```

### Options

```
      --active-within duration   How recently a record must have been active to be listed. Zero will return all records. (default 24h0m0s)
  -h, --help                     help for describe
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

* [chainctl iam folders](/chainguard/chainctl/chainctl-docs/chainctl_iam_folders/)	 - IAM folders interactions.

