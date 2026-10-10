---
date: 2026-10-09T15:36:02Z
title: "chainctl skills install"
slug: chainctl_skills_install
url: /platform/chainctl/chainctl-docs/chainctl_skills_install/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills install

Download a skill and install it into agent directories.

### Synopsis

Download a skill and place it into the skills directories of detected agents.

<ref> is a skill reference, optionally host-qualified: a bare org/name (or
org/owner/name) resolves to the hardened catalog on skills.cgr.dev, while an
uploads.cgr.dev/org/name reference installs a private skill straight from the
uploads namespace (the same reference `chainctl skills list --source uploads`
prints).

By default, a shared canonical copy is written to .agents/skills/<name>/ and
agent-specific symlinks are created. Use --copy to write independent copies.

With --verify, the fetched digest must pass the same signature check as
`chainctl skills verify` before any file or symlink is written; otherwise
the command exits nonzero and installs nothing. A skill on a registry whose
signatures chainctl cannot verify, such as a staging or development registry,
fails too, unless --allow-unverifiable-host is also given.

```
chainctl skills install <ref> [flags]
```

### Options

```
  -a, --agent stringArray         Target specific agents by ID (repeatable). Use --agent '*' for all known agents.
      --allow-unverifiable-host   With --verify, accept a skill from a registry whose signatures chainctl cannot verify, such as a staging or development registry, with a warning instead of failing.
      --copy                      Copy files per agent instead of using a shared canonical copy + symlinks.
      --global                    Install to global (~/) directories instead of project-local.
      --verify                    Check Chainguard's signature on the fetched skill, as 'chainctl skills verify' does, before writing anything. Fails unless verified, including for a skill on a registry whose signatures chainctl cannot verify.
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

