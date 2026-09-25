---
title: "Migrating a Go project to Chainguard Libraries"
type: "article"
linktitle: "Migrate to Chainguard"
description: "How to migrate an existing Go project to pull dependencies from Chainguard Libraries"
date: 2026-09-25T00:00:00+00:00
lastmod: 2026-09-25T00:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Go"]
menu:
  docs:
    parent: go
    identifier: Go Migration
weight: 056
toc: true
---

Chainguard Libraries for Go provides an authenticated Go module proxy that applies Chainguard security controls to Go dependencies.

Because Chainguard Libraries uses the standard [GOPROXY protocol](https://go.dev/ref/mod#goproxy-protocol), migrating an existing project does not require application-code changes or a new dependency declaration format. You configure the Go toolchain to use Chainguard, refresh any cached modules, and verify the build.

This guide covers two common setups:

- **Direct access**: Your Go toolchain connects directly to `libraries.cgr.dev`. This is useful for an evaluation, a small team, or an isolated CI job.
- **Repository manager**: Your Go toolchain connects to a repository manager that proxies Chainguard Libraries. This is recommended for organization-wide use.

## Prerequisites

Before you begin, you need:

- An existing Go project with a `go.mod file`. A `go.sum` file is recommended.
- A supported Go toolchain. Go 1.21 or later is recommended for the current Go Libraries beta.
- [chainctl installed and authenticated](/platform/chainctl-usage/how-to-install-chainctl/).
- An [entitlement to Chainguard Libraries for Go](#create-an-entitlement)
- A [pull token for Chainguard Libraries for Go](#create-a-pull-token)

### Create an entitlement

To create an entitlement to Chainguard Libraries for Go, run:

```bash
chainctl libraries entitlements create --ecosystems=GO
```

You do not need to manually enable upstream fallback for Go; the entitlement for Go automatically includes Chainguard protections for upstream artifacts.

You can also configure a cooldown policy after you create the entitlement. For example, to create and enforce a policy for a 14-day cooldown:

```bash
chainctl libraries policy create --name=go-cooldown-14d --cooldown-days=14
chainctl libraries policy enable go-cooldown-14d --ecosystem=GO --mode=ENFORCE
```

It can take up to 30 minutes for configured policies to take effect. Learn more about cooldown and other policies in the [Libraries policies documentation](/chainguard/chainguard-repository/library-policies/).

### Create a pull token

Create a pull token for the Go repository:

```bash
chainctl auth pull-token --repository=go --ttl=8670h
```

The command returns a username and password. Use these values to authenticate Go to Chainguard Libraries.

> **Note**: Do not commit the credentials to source control. Keep the configuration file out of the repository when it contains literal credentials, or generate it at build time from secrets stored in your CI/CD system. For shared environments, use a dedicated machine identity or service account instead of a personal token when available.

For local development, you can store the credentials in `~/.netrc`:

```bash
cat >> ~/.netrc <<EOF
machine libraries.cgr.dev
login ${CHAINGUARD_GO_IDENTITY_ID}
password ${CHAINGUARD_GO_TOKEN}
EOF
chmod 600 ~/.netrc
```

Go sends credentials to HTTPS proxies. Make sure the machine entry is exactly `libraries.cgr.dev` and that the token has not expired.

## Step 1: Confirm your baseline build

Run your existing build and tests before changing the module proxy:

```bash
go version
go mod download
go test ./...
```

Resolve any existing build or test failures first. This gives you a baseline to compare against after migration.

## Step 2: Configure Go to use Chainguard Libraries

{{< tabs label="Access method for configuring authentication and registry" >}}

{{% tab title="Direct access" %}}

Set Chainguard as the only Go module proxy:

```bash
go env -w GOPROXY=https://libraries.cgr.dev/go
go env -w GONOSUMDB='*'
```

You can use `GOSUMDB=off` instead of `GONOSUMDB=*`:

```bash
go env -w GOSUMDB=off
```

Do not add `direct`, `https://proxy.golang.org`, or another public proxy to `GOPROXY`. A sole Chainguard entry ensures that module requests remain within your organization’s configured controls.

Do not set `GOPRIVATE`. It also sets `GONOPROXY` and can bypass Chainguard. Do not set `GONOSUMCHECK`; it is not a current Go configuration variable.

Check the effective configuration:

```bash
go env GOPROXY GONOSUMDB GOSUMDB
```

{{% /tab %}}

{{% tab title="Repository manager" %}}

For team and organization-wide deployments, configure your repository manager as the authenticated upstream for Chainguard Libraries for Go.

The repository manager should expose a Go module proxy endpoint to your developers and CI systems. Point Go at that endpoint, for example:

```bash
go env -w GOPROXY=https://<your-repository-manager>/go
```

Use repository-manager credentials in the developer and CI environments. Do not distribute the Chainguard pull token to every developer when your repository manager can centralize access.

Configure Chainguard as the primary upstream for Go modules and avoid adding a separate public Go proxy as a fallback. This preserves Chainguard’s policy, cooldown, and malware controls for requests that are not yet available as Chainguard-built modules.

{{% /tab %}}

{{< /tabs >}}

## Step 3: Verify authentication and proxy access

You can test the endpoint directly with the credentials exported by chainctl:

```bash
curl -fsS -u "${CHAINGUARD_GO_IDENTITY_ID}:${CHAINGUARD_GO_TOKEN}" \
  https://libraries.cgr.dev/go/rsc.io/quote/@v/v1.5.2.info
```

A successful response contains JSON similar to:

```bash
{
  "Version": "v1.5.2",
  "Time": "2021-05-05T15:00:00Z"
}
```

The exact timestamp may differ. If the request returns 401, check the token, `.netrc` hostname, and token expiration. If it returns 404, confirm that your organization has upstream fallback enabled and that the module version is available.

## Step 4: Pull modules and verify the build

Use a clean module cache when first testing the migration so that existing cached modules do not hide proxy configuration problems:

```bash
go clean -modcache
go mod download
go test ./...
go mod verify
```

For a minimal smoke test in a temporary directory:

```bash
workdir=$(mktemp -d)
cd "$workdir"
go mod init example.com/proxy-check
go get rsc.io/quote@v1.5.2
go mod verify
```

After the build succeeds, inspect `go env GOPROXY` and your build logs to confirm that module requests are going through Chainguard. Keep the generated `go.sum` file with the project if it is part of your existing dependency-management workflow.

## Step 5: Adopt remediated versions explicitly

Chainguard-remediated Go versions use the `-cgr.N` prerelease suffix. Go does not select these versions through `@latest` or `go get -u`, so you must request the version explicitly.

For example:

```bash
go get example.com/module@v1.2.5-cgr.1
go mod tidy
go mod verify
```

You can also update the `require` directive in `go.mod` directly:

```bash
require example.com/module v1.2.5-cgr.1
```

Use the module version listed by Chainguard for the CVE remediation you want to adopt. A remediated version is a distinct source archive; it does not replace the upstream bytes for another version.
