---
date: 2026-09-25T09:27:27Z
title: "chainctl skills list"
slug: chainctl_skills_list
url: /platform/chainctl/chainctl-docs/chainctl_skills_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills list

List skills published by an org.

### Synopsis

List skills and their tags, including skills without a latest tag.

By default, list the immediate skills and folders in the skills registry. Use --recursive to include skills in nested folders, or --source uploads to list uploads. Referrer tags are hidden by default; use --show-referrers to include them.

```
chainctl skills list [flags]
```

### Options

```
  -g, --group string     Org or folder to list, e.g. "chainguard" or "chainguard/github" (default: current context).
  -r, --recursive        Recurse into nested folders and list every skill by its full path.
      --show-referrers   Whether to show referrer tags of the form sha256-deadbeef.{sig,sbom,att}.
      --source string    Which namespace to list: "skills" (hardened, skills.cgr.dev), "uploads" (user uploads, uploads.cgr.dev), or "all". (default "skills")
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

