---
date: 2024-02-29T21:03:13Z
title: "chainctl iam folders delete"
slug: chainctl_iam_folders_delete
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_folders_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam folders delete

Delete a folder.

```
chainctl iam folders delete [FOLDER_NAME | FOLDER_ID] [--skip-refresh] [--yes]
```

### Examples

```

# Delete a folder by ID
chainctl iam folders delete 19d3a64f20c64ba3ccf1bc86ce59d03e705959ad/efb53f2857d567f2

# Delete a folder by name
chainctl iam folders delete my-folder

# Delete a folder to be selected interactively
chainctl iam folders delete

```

### Options

```
  -h, --help           help for delete
      --skip-refresh   Skips attempting to reauthenticate and refresh the Chainguard auth token if it becomes out of date.
  -y, --yes            Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
```

### Options inherited from parent commands

```
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam folders](/chainguard/chainctl/chainctl-docs/chainctl_iam_folders/)	 - IAM folders interactions.

