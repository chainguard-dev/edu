---
title: "Chainguard Libraries for Go overview"
linktitle: "Go overview"
description: "Go modules for your application development"
type: "article"
date: 2026-09-25T00:00:00+00:00
lastmod: 2026-10-14T18:18:18+00:00
draft: false
tags: ["Chainguard Libraries", "Go", "Overview"]
menu:
  docs:
    parent: "go"
weight: 51
toc: true
---

Chainguard Libraries for Go provides enhanced security for the Go module ecosystem through an authenticated, secure-by-default Go module proxy. The proxy applies organization-defined policies, malware and greyware protections, and cooldown controls to Go dependencies before they reach development and build environments.

Go modules support cloud-native infrastructure, high-volume services, fintech, networking, and security applications. Chainguard Libraries for Go helps reduce the risks of consuming modules from public sources, including malicious modules, typosquats, and vulnerabilities in versions your applications still need to use.

{{< beta feature="Chainguard Libraries for Go" enroll="true" >}}

## Runtime requirements

Go modules retrieved from Chainguard have the same module paths, APIs, and Go toolchain requirements as their corresponding upstream projects unless a remediated release explicitly documents otherwise. Your application’s existing go.mod remains the source of truth for module requirements.

## Technical details

You must use the username and password [retrieved with chainctl](/chainguard/libraries/introduction/access/) to access the Chainguard Libraries for Go repository.

The URL for the repository is: `https://libraries.cgr.dev/go/`.

When a Go command requests a module, Chainguard resolves the request through the sources enabled for your organization:

- Chainguard-remediated module versions
- Eligible versions from the upstream Go module proxy, when upstream fallback is enabled

The `/go` endpoint is the endpoint you configure in `GOPROXY`. It uses the standard Go module proxy paths for version lists, metadata, `go.mod` files, and module source archives.
Go builds from source on the customer side. Unlike ecosystems that distribute prebuilt language artifacts, Chainguard Libraries for Go distributes module source archives. A CVE-remediated module is published as a distinct Go version rather than replacing the upstream bytes for the same version.

## Go checksum verification

Chainguard-remediated versions are not recorded in the public Go checksum database because they are not available from public upstream origins. Configure Go to skip public checksum verification for modules retrieved through Chainguard:

```bash
go env -w GONOSUMDB='*'
```

You can alternatively disable checksum database verification globally:

```bash
go env -w GOSUMDB=off
```

The Go module proxy remains authenticated over TLS, and `go.sum` continues to pin the module bytes after the first successful fetch.

Do not set `GOPRIVATE` or `GONOPROXY` to `*` or to broad patterns that match public modules. Go fetches any module path that matches `GONOPROXY` (which `GOPRIVATE` also sets) directly from its source repository, bypassing Chainguard. Scope these variables to your own private module paths only, as described in [Private modules](#private-modules). `GONOSUMCHECK` is not a current Go configuration variable and should not be used.

## Private modules

Chainguard Libraries for Go resolves modules through the public Go module proxy and does not fetch from source repositories. A module that lives in a private repository, such as an internal company package, is not available through Chainguard and returns `404 Not Found`.

To use Chainguard for public modules while continuing to fetch private modules directly from your own repositories, set `GONOPROXY` to the module path prefixes of your private modules:

```bash
go env -w GOPROXY=https://libraries.cgr.dev/go
go env -w GONOSUMDB='*'
go env -w GONOPROXY='github.com/example-org/*'
```

With this configuration, Go fetches modules matching `github.com/example-org/*` directly from the repository using your existing Git credentials, and requests every other module through Chainguard. `GOPRIVATE='github.com/example-org/*'` has the same effect. Keep the pattern as narrow as your private module paths, because matching modules are not subject to Chainguard controls.

To publish private modules into a registry that only your organization can resolve, alongside the shared catalog, use `chainctl libraries go upload`. This feature is in beta; contact your Chainguard account team to enable it.

## Upstream fallback

[Upstream fallback](/chainguard/libraries/introduction/#upstream-fallback-and-controls) is enabled by default for Chainguard Libraries for Go. The Go endpoint serves eligible versions from the upstream Go module proxy under Chainguard security controls.

Upstream fallback does not make Chainguard Libraries a complete mirror of the upstream registry. A module or version may be unavailable because it is inside the cooldown window or is blocked by Chainguard or your organization’s policies.

### View packages blocked due to malware

Chainguard’s source code and maintainer behavior scanning identifies and blocks malicious and greyware packages in Chainguard Libraries via the Chainguard Repository. You can get a list of blocked packages via chainctl or the API. Refer to the [Libraries Overview page](/chainguard/libraries/introduction/overview/#malware-and-greyware-detection) for more information.
