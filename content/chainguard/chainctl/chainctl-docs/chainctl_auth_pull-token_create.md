---
date: 2026-02-25T21:19:09Z
title: "chainctl auth pull-token create"
slug: chainctl_auth_pull-token_create
url: /chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth pull-token create

Create a pull token.

```
chainctl auth pull-token create [--save=true|false] [--name=NAME] [--ttl=NUM_HOURS_ACTIVE] [--parent=PARENT] [--repository={oci|apk|javascript|java|python}] [flags]
```

### Examples

```
  # Create a pull token for container registry pull access.
  chainctl auth pull-token create
  
  # Create a pull token for pull access to a library ecosystem.
  chainctl auth pull-token create --repository=java
  
  # Create a pull token that lasts for 24 hours.
  chainctl auth pull-token create --ttl=24h
  
  # Create a pull token for a particular organization.
  chainctl auth pull-token create --parent=my-org
```

### Options

```
      --name string         Optional name for the pull token. (default "pull-token")
      --parent string       The IAM organization or folder with which the pull token identity is associated.
      --repository string   The repository type to create a pull token for. Must be one of: oci, apk, javascript, java, python. (default "oci")
      --save                Save the OCI registry pull token to the Docker configuration.
      --ttl ns              Time To Live for the validity of the pull token. Valid unit strings range from nanoseconds to hours and are ns, `us`, `ms`, `s`, `m`, and `h`. Maximum value is 8760h or one year. (default 720h0m0s)
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

* [chainctl auth pull-token](/chainguard/chainctl/chainctl-docs/chainctl_auth_pull-token/)	 - Create a pull token.

