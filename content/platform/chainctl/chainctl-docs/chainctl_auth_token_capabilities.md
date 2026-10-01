---
date: 2026-09-30T19:15:34Z
title: "chainctl auth token capabilities"
slug: chainctl_auth_token_capabilities
url: /platform/chainctl/chainctl-docs/chainctl_auth_token_capabilities/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth token capabilities

Print the capabilities of the local Chainguard Token.

### Synopsis

Print the capabilities of the local Chainguard Token.

With --token -, decode the token read from standard input instead. This
shows what a grant minted with "chainctl auth token --delegate" carries:

  chainctl auth token --delegate=my-delegate --role=viewer --scope=my-org | chainctl auth token capabilities --token -

Prefer "--token -" to passing a token as the flag's value: a token on the
command line is visible to other local users in the process list and is kept
in shell history.

The token is decoded, not verified.

```
chainctl auth token capabilities [--token=TOKEN|-] [flags]
```

### Options

```
      --token string   Decode another token instead of the local one. Use "-" to read it from standard input; a token given as the value is visible in the process list and shell history.
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

* [chainctl auth token](/platform/chainctl/chainctl-docs/chainctl_auth_token/)	 - Print the local Chainguard Token.

