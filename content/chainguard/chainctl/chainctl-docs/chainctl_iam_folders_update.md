---
date: 2025-04-03T19:10:23Z
title: "chainctl iam folders update"
slug: chainctl_iam_folders_update
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_folders_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam folders update

Update a folder.

```
chainctl iam folders update FOLDER_NAME | FOLDER_ID [--name FOLDER_NAME] [--description FOLDER_DESCRIPTION]
```

### Examples

```

# Update a folder's name
chainctl iam folders update my-folder --name new-folder-name

# Update a folder's description
chainctl iam folders update 19d3a64f20c64ba3ccf1bc86ce59d03e705959ad/efb53f2857d567f2 --description "A description of the folder."

# Remove a folder's description
chainctl iam folders update my-folder --description ""
```

### Options

```
  -d, --description string   The updated description for the folder.
  -h, --help                 help for update
  -n, --name string          The updated name for the folder.
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
  -o, --output string      Output format. One of: [csv, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam folders](/chainguard/chainctl/chainctl-docs/chainctl_iam_folders/)	 - IAM folders interactions.

