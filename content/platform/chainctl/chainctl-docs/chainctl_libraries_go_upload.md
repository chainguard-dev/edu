---
date: 2026-10-06T09:26:34Z
title: "chainctl libraries go upload"
slug: chainctl_libraries_go_upload
url: /platform/chainctl/chainctl-docs/chainctl_libraries_go_upload/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries go upload

Upload a Go module version from a source directory.

### Synopsis

Upload a Go module to Chainguard Libraries for Go.

The command packages the module at --source into a GOPROXY module zip
(the same layout 'go mod download' produces), validates it locally, and
uploads it to <ecosystems-url>/go/<module>/@v/<version>.zip. The version
lands in your organization's own registry, which only your organization
can resolve, alongside the shared catalog. The registry derives the .mod
and .info files from the zip. The source directory must contain a go.mod
whose module directive matches --module-path; VCS metadata (.git and
friends), nested modules, and irregular files are excluded automatically.

Uploads are immutable: once a (module, version) exists it cannot be
replaced, so publish a new version instead. --version must be a canonical
semantic version such as v1.2.3, and its major version must agree with
the module path (a /v2 module publishes v2.x.y). Versions with a -cgr.N
suffix are reserved for Chainguard's remediation pipeline and are refused.

Authentication requires a token minted for the registry host that carries
the Go push capability (CAP_LIBRARIES_GO_CREATE). Within an organization
that is the built-in "owner" role or the dedicated "libraries.go.push"
role. Credentials are resolved in this order:
  1. --token
  2. $CHAINCTL_AUTH_TOKEN, if its audience includes the registry host
  3. the chainctl session for the registry host, as created by
     'chainctl auth login --audience <host>' (a browser login is opened
     when no usable session exists)

If a token was minted before the push capability was granted it still
carries the old capability set; refresh it with
'chainctl auth login --audience <host> --refresh'.

Consumers resolve uploaded versions with GOPROXY=<ecosystems-url>/go.
Versions published this way never appear in sum.golang.org, so consumers
must exclude the module from checksum-database lookups (GONOSUMDB or
GOPRIVATE).

```
chainctl libraries go upload [flags]
```

### Examples

```
  # Publish v1.4.0 of a module from its checkout
  chainctl libraries go upload \
      --module-path example.com/team/lib \
      --version v1.4.0 \
      --source ./lib

  # Build and validate the module zip without uploading
  chainctl libraries go upload --module-path example.com/team/lib --version v1.4.0 --source ./lib --dry-run

  # Publish to a non-production registry with an explicit token
  chainctl libraries go upload \
      --ecosystems-url https://libraries.chainops.dev \
      --token "$(chainctl auth token --audience libraries.chainops.dev)" \
      --module-path example.com/team/lib --version v1.4.0 --source ./lib
```

### Options

```
      --dry-run                 Build and validate the module zip and report its size and go.sum hash without uploading.
      --ecosystems-url string   URL of the Chainguard Libraries registry (defaults to https://libraries.cgr.dev). The /go registry path is appended automatically.
      --module-path string      Module path to publish (the go.mod module directive), e.g. example.com/team/lib. Required.
      --source string           Directory containing the module source, including its go.mod. Required.
      --token string            Bearer token for the registry host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
      --version string          Canonical semantic version to publish, e.g. v1.4.0. Required.
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

* [chainctl libraries go](/platform/chainctl/chainctl-docs/chainctl_libraries_go/)	 - Go module registry commands.

