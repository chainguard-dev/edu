---
date: 2026-11-09T19:57:31Z
title: "chainctl images repos delete-image"
slug: chainctl_images_repos_delete-image
url: /platform/chainctl/chainctl-docs/chainctl_images_repos_delete-image/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images repos delete-image

Delete one image from a customer image repository and release its storage.

### Synopsis

Delete one image from a repository under your organization's images folder. The image's tags, its manifest, and every layer, config, and index entry that no other image in the repository still needs are removed, and the released bytes stop counting toward the organization's image storage immediately. An image a surviving multi-platform index still lists cannot be deleted on its own; delete the index. Durable storage is not erased by this command.

```
chainctl images repos delete-image {REPO_NAME|REPO_ID} [--parent ORGANIZATION_NAME | ORGANIZATION_ID | FOLDER_NAME | FOLDER_ID] (--tag TAG | --digest DIGEST) [--dry-run] [--yes]
```

### Options

```
      --digest string   Manifest digest (sha256:...) of the image to delete.
      --dry-run         Report what would be removed without removing anything.
      --parent string   The name or id of the parent location holding the image repo. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --tag string      Tag of the image to delete. Every tag pointing at the same image is removed with it.
  -y, --yes             Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl images repos](/platform/chainctl/chainctl-docs/chainctl_images_repos/)	 - Image repo related commands for the Chainguard platform.

