---
title: "Configure Go build tools"
linktitle: "Configure build tools"
description: "Configuring Chainguard Libraries for Go on your workstation"
type: "article"
date: 2026-09-25T00:00:00+00:00
lastmod: 2026-09-29T19:14:43+00:00
draft: false
tags: ["Chainguard Libraries", "Go"]
menu:
  docs:
    parent: "go"
    identifier: "Go Build Configuration"
weight: 53
toc: true
---

Chainguard Libraries for Go implements the standard [GOPROXY protocol](https://go.dev/ref/mod#goproxy-protocol). To use it, configure Go to retrieve modules through the Chainguard Go module proxy.

This page is a reference for configuring Go projects and CI/CD environments. It covers authentication, proxy configuration, cache clearing, verification, and using Chainguard-remediated module versions. Apply these changes on every workstation and build server that downloads Go modules, including CI/CD systems such as GitHub Actions, Jenkins, and TeamCity.

The Chainguard Go module proxy endpoint, `https://libraries.cgr.dev/go`, is also the [Chainguard Repository](/chainguard/chainguard-repository/overview/) endpoint for Go. It serves requested versions from upstream [under Chainguard security controls](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls).

This guide outlines build tool configuration. If you are looking for something else, refer to the following guides depending on your goals:

| If you want to... | Use this page |
| --- | --- |
| Understand what Chainguard Libraries for Go is and how it works | [Go overview](/chainguard/libraries/go/overview/) |
| Set up organization-wide access through a repository manager | [Global configuration](/chainguard/libraries/go/global-configuration/) |
| Look up how to configure Go for use with Chainguard Libraries | This page |
| Migrate an existing project step by step | [Go migration guide](/chainguard/libraries/go/migration/) |

If a package or version is blocked by a policy or malware scan, your build tool returns an error. Refer to the [Error messages documentation](/chainguard/libraries/troubleshooting/errors/) for more details.

## Direct access

Pulling artifacts directly from Chainguard Libraries for Go requires authentication with username and password for a pull token as detailed in the [Libraries Access documentation](/chainguard/libraries/introduction/access/).

Direct access configures Go to use Chainguard Libraries without a repository manager:

```bash
go env -w GOPROXY=https://libraries.cgr.dev/go
go env -w GONOSUMDB='*'
```

You can use `GOSUMDB=off` instead of `GONOSUMDB=*`:

```bash
go env -w GOSUMDB=off
```

Do not add `,direct`, `https://proxy.golang.org`, or another public proxy to `GOPROXY`. Use the Chainguard endpoint as the only entry so that module requests remain within your organization’s configured controls.

Direct access requires per-project and per-workstation configuration. For organizations with multiple teams, proxying through an artifact manager may be a more suitable approach. Learn more in the [global configuration documentation](/chainguard/libraries/go/global-configuration/).

### Authentication

Go can read HTTP Basic authentication credentials from a `.netrc` file. For local development, add an entry for the Chainguard host:

```bash
cat >> ~/.netrc <<EOF
machine libraries.cgr.dev
login ${CHAINGUARD_GO_IDENTITY_ID}
password ${CHAINGUARD_GO_TOKEN}
EOF
chmod 600 ~/.netrc
```

Make sure the machine entry is exactly `libraries.cgr.dev` and that the token has not expired. Go sends credentials only to HTTPS proxies.

For CI/CD, use the CI system’s secret store to provide the credentials. Avoid embedding credentials in `GOPROXY` URLs or checked-in configuration files.

If you use a repository manager, authenticate Go to the repository manager with that system’s credentials. Chainguard pull-token credentials should not be sent to a third-party repository manager unless your organization has explicitly configured that flow.

## Configure Go

Set the following environment variables for any environment that builds the project:

```bash
go env -w GOPROXY=https://libraries.cgr.dev/go
go env -w GONOSUMDB='*'
```

Use your repository manager URL instead when your organization uses a repository manager:

```bash
go env -w GOPROXY=https://<your-repository-manager>/go
go env -w GONOSUMDB='*'
```

Check the effective configuration:

```bash
go env GOPROXY GONOSUMDB GOSUMDB
```

### Checksum database settings

Chainguard-remediated versions are not available from public upstream origins, so they cannot be verified by the public Go checksum database. `GONOSUMDB=*` tells Go not to use the public checksum database for modules retrieved through the configured proxy. The authenticated HTTPS proxy and the project’s `go.sum` file continue to protect module retrieval.

Do not use `GOPRIVATE` for modules that should be retrieved through Chainguard. `GOPRIVATE` also sets `GONOPROXY` and can cause Go to bypass Chainguard.

Do not use `GONOSUMCHECK`; it is not a current Go configuration variable.

## Verify the configuration

Use a clean module cache when testing the configuration for the first time. This prevents previously cached modules from hiding proxy or authentication problems:

```bash
go clean -modcache
go mod download
go test ./...
go mod verify
```

Inspect `GOPROXY` and your build logs to confirm that module requests are going through Chainguard.

## Minimal example project

Use the following commands to test access in a temporary directory:

```bash
workdir=$(mktemp -d)
cd "$workdir"
go mod init example.com/proxy-check
go get rsc.io/quote@v1.5.2
go mod verify
```

A successful `go mod verify` confirms that the downloaded module content matches the checksums recorded in `go.sum`.

## Use remediated Go versions

Chainguard-remediated Go versions use the `-cgr.N` prerelease suffix. For example: `v1.2.5-cgr.1`.

A remediated version is a distinct module source archive. It does not replace the upstream bytes for another version.

Go does not select `-cgr.N` versions automatically through `@latest`, minimal version selection, or `go get -u`. Adopt a remediated version explicitly:

```bash
go get example.com/module@v1.2.5-cgr.1
go mod tidy
go mod verify
```

Replace the module path and version with the remediated version available for your dependency. You can also update the require directive in `go.mod` directly:

```bash
require example.com/module v1.2.5-cgr.1
```
