---
date: 2026-05-19T23:19:53Z
title: "chainctl skills pull"
slug: chainctl_skills_pull
url: /chainguard/chainctl/chainctl-docs/chainctl_skills_pull/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills pull

Download a published skill to a local directory.

### Synopsis

Download a published skill to a local directory.

<ref> is a skill reference of the form org/name[:tag].
<dir> is the output directory (default: ./<name>).

```
chainctl skills pull <ref> [<dir>] [flags]
```

### Options

```
      --force   Overwrite destination directory if it already exists.
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

* [chainctl skills](/chainguard/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.

