---
date: 2026-11-24T18:17:18Z
title: "chainctl auth pull-token create"
slug: chainctl_auth_pull-token_create
url: /platform/chainctl/chainctl-docs/chainctl_auth_pull-token_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl auth pull-token create

Create a pull token.

### Synopsis

Create a pull token, a long-lived credential for pulling from Chainguard
in environments that cannot sign in.

--repository is the kind of registry the token pulls from: oci, apk, or a
library ecosystem such as javascript or java. --parent is where the token
belongs. A token for an organization pulls from the organization's default
Libraries repository and from every named repository in it. A token for one
Libraries repository, created with --parent ORG/REPO, pulls only from that
repository's URL, never from the default repository or another repository,
and grants no right to change the repository.

```
chainctl auth pull-token create [--save=true|false] [--name=NAME] [--description=DESC] [--ttl=NUM_HOURS_ACTIVE] [--parent=PARENT] [--repository={oci|apk|java|javascript_athena|ruby|ruby_athena|java_athena|dotnet|javascript|dotnet_athena|go|go_athena|rust|python|python_athena|rust_athena}[,...] | --repository=all] [flags]
```

### Examples

```
  # Create a pull token for container registry pull access.
  chainctl auth pull-token create
  
  # Create a pull token for pull access to a library ecosystem.
  chainctl auth pull-token create --repository=java
  
  # Create one pull token for both the container registry and APK packages.
  chainctl auth pull-token create --repository=oci,apk
  
  # Create one pull token for every repository type "all" covers (oci and apk).
  chainctl auth pull-token create --repository=all
  
  # Create a pull token that lasts for 24 hours.
  chainctl auth pull-token create --ttl=24h
  
  # Create a pull token for a particular organization.
  chainctl auth pull-token create --parent=example.com
  
  # Create a pull token that pulls JavaScript packages only from the repository prod.
  chainctl auth pull-token create --repository=javascript --parent=example.com/prod
  
  # Create a pull token with a description.
  chainctl auth pull-token create --description="CI builds for service-foo"
```

### Options

```
      --description string   Optional description for the pull token.
      --name string          Optional name for the pull token. (default "pull-token")
      --parent string        Name or UIDP of the organization or folder the pull token belongs to. Pass ORG/REPO, such as example.com/prod, for a token that pulls only from one Libraries repository.
      --repository string    Comma-separated repository types to create one pull token for, each one of: oci, apk, java, javascript_athena, ruby, ruby_athena, java_athena, dotnet, javascript, dotnet_athena, go, go_athena, rust, python, python_athena, rust_athena. "all" selects oci and apk. The token gets one role binding per repository type. This names the kind of registry, not a Libraries repository: pass that in --parent as ORG/REPO. (default "oci")
      --save                 Save the OCI registry pull token to the Docker configuration.
      --ttl ns               Time To Live for the validity of the pull token. Valid unit strings range from nanoseconds to hours and are ns, `us`, `ms`, `s`, `m`, and `h`. The maximum depends on the organization's plan: 720h (30 days) for Starter, 168h (7 days) for Team and 8760h (one year) for other plans. (default 720h0m0s)
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

* [chainctl auth pull-token](/platform/chainctl/chainctl-docs/chainctl_auth_pull-token/)	 - Create a pull token.

