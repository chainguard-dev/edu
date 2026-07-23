---
date: 2026-07-22T19:49:10Z
title: "chainctl skills delete"
slug: chainctl_skills_delete
url: /platform/chainctl/chainctl-docs/chainctl_skills_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills delete

Remove a published version of a skill.

### Synopsis

Remove a published version of a skill.

Delete a single version:   org/name:tag
A tag is required to prevent accidental deletion of "latest", and deleting the
"latest" tag requires additional confirmation. When you delete a skill's last
remaining version, the now-empty skill entry is removed too, so it no longer
lingers in "skills list" with no pullable content.

Clear an already-empty skill:   org/name
A tagless reference is accepted only for a skill that has no versions left (the
residue of versions deleted before this cleanup existed). A skill that still has
versions requires an explicit tag.

```
chainctl skills delete <ref> [flags]
```

### Options

```
  -y, --yes   Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl skills](/platform/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.

