---
title: "Authenticating with the Chainguard SDK"
linktitle: "SDK Authentication"
type: "article"
description: "Tutorial with examples showing how you can authenticate with the Chainguard SDK's auth and auth/ggcr packages."
date: 2025-06-04T08:49:31+00:00
lastmod: 2025-06-04T15:22:20+01:00
draft: false
tags: ["Chainguard Console", "Procedural"]
images: []
toc: true
weight: 065
contentType: "product-docs"
---

There are several ways for users to interact with the Chainguard platform, with [`chainctl`](/chainguard/chainctl/) (Chainguard's command-line tool) and the [Chainguard Console](https://console.chainguard.dev/overview) (Chainguard's web interface) being the two most commonly-used methods. However, both of these require a human user to authenticate, and aren't useful for working with Chainguard resources programmatically.

The [Chainguard SDK](https://github.com/chainguard-dev/sdk) serves to ease programmatic integration with the Chainguard platform. This guide highlights two examples from the SDK repository that show how to authenticate to the [Chainguard registry](/chainguard/chainguard-registry/overview/) using the `chainguard.dev/sdk/auth` and `chainguard.dev/sdk/auth/ggcr` packages. The first has you authenticate as a local user, while the second has you authenticate as an [assumed identity](/chainguard/administration/assumable-ids/assumable-ids/). 

For more information about the examples highlighted in this guide, refer to the [`examples` folder](https://github.com/chainguard-dev/sdk/tree/main/examples/registry) in the SDK repository.


## Prerequisites

To follow along with this guide you must have [Go installed](https://go.dev/doc/install) to run the provided examples, which are written in Golang.

Additionally, it may help to run these examples from a temporary directory, like `/tmp` so the code is automatically removed from your system the next time it boots:

```shell
cd /tmp
```


## Example 1 — Authenticate Using Local Credentials 

The first example from the SDK repository we will go over is the [`chainctl` example](https://github.com/chainguard-dev/sdk/tree/main/examples/registry/chainctl). This example shows how to use a token source backed by `chainctl` — Chainguard's command-line tool — to access the Chainguard registry using local credentials.

The `chainctl` example consists of the following Go code in a `main.go` file (with comments removed):

```go
package main

import (
	"context"
	"encoding/json"
	"log"
	"os"

	"chainguard.dev/sdk/auth"
	"chainguard.dev/sdk/auth/ggcr"
	"github.com/google/go-containerregistry/pkg/name"
	"github.com/google/go-containerregistry/pkg/v1/remote"
)

func main() {
	ctx := context.Background()
	ts := auth.NewChainctlTokenSource(ctx, auth.WithAudience("cgr.dev"))

	desc, err := remote.Get(name.MustParseReference("cgr.dev/chainguard/static"), remote.WithAuthFromKeychain(ggcr.TokenSourceKeychain(ts)))
	if err != nil {
    	log.Fatalf("error getting reference: %v", err)
	}
	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	_ = enc.Encode(desc)
}
```

This code works by executing the `chainctl` binary to retrieve a token and making a call directly to the registry. Specifically, it does the following things:

* It imports some packages, including the Chainguard SDK's [auth](https://github.com/chainguard-dev/sdk/tree/main/auth) and [auth/ggcr](https://github.com/chainguard-dev/sdk/tree/main/auth/ggcr) packages. These are what allow the program to interact with the Chainguard registry.
* The example uses the `auth` package to execute the `chainctl` CLI binary to retrieve a token based on the local user's credentials.
* Using this token, the example makes a call to the Chainguard registry to retrieve some information about the supplied image. The example uses the `cgr.dev/chainguard/static` Starter image.

To run this example, save the `main.go` file to your local machine. Then run the following commands:

```shell
go mod init github.com/chainguard-dev/sdk && go mod tidy
```

The `go mod init` command will initialize a new `go.mod` file in the current directory. Including the `github.com/chainguard-dev/sdk` URL tells Go to use that as the module path. The `go mod tidy` command ensures that the new `go.mod` file matches the source code in the module.

Following that, execute the program with `go run`:

```shell
go run main.go
```

This will return output like the following:

```
{
  "mediaType": "application/vnd.oci.image.index.v1+json",
  "size": 925,
  "digest": "sha256:633aabd19a2d1b9d4ccc1f4b704eb5e9d34ce6ad231a4f5b7f7a3af1307fdba8",
  "Manifest": "eyJzY2hlbWFWZXJzaW9uIjoyLCJtZWRpYVR5cGUiOiJhcHBsaWNhdGlvbi92bmQub2NpLmltYWdlLmluZGV4LnYxK2pzb24iLCJtYW5pZmVzdHMiOlt7Im1lZGlhVHlwZSI6ImFwcGxpY2F0aW9uL3ZuZC5vY2kuaW1hZ2UubWFuaWZlc3QudjEranNvbiIsInNpemUiOjgzOCwiZGlnZXN0Ijoic2hhMjU2OmJiMmRlMjU3MjFlMTE3Zjg4MDYwYjgyZGQ2YWQ1M2Y4ODdlZTgwOWU1MzE1Y2Y0MWEwMGNkOGExM2ZhMjMwNzciLCJwbGF0Zm9ybSI6eyJhcmNoaXRlY3R1cmUiOiJhbWQ2NCIsIm9zIjoibGludXgifX0seyJtZWRpYVR5cGUiOiJhcHBsaWNhdGlvbi92bmQub2NpLmltYWdlLm1hbmlmZXN0LnYxK2pzb24iLCJzaXplIjo4MzgsImRpZ2VzdCI6InNoYTI1NjoxMmVjMWU3NDg0NmVhNDM1OTNkNmExMzMwZGEyOGVkNGQzNmRmNThhMTg2NGQwOTE1MjRlM2IwYTk5MDY4Y2QzIiwicGxhdGZvcm0iOnsiYXJjaGl0ZWN0dXJlIjoiYXJtNjQiLCJvcyI6ImxpbnV4In19XSwiYW5ub3RhdGlvbnMiOnsiZGV2LmNoYWluZ3VhcmQucGFja2FnZS5tYWluIjoiIiwib3JnLm9wZW5jb250YWluZXJzLmltYWdlLmF1dGhvcnMiOiJDaGFpbmd1YXJkIFRlYW0gaHR0cHM6Ly93d3cuY2hhaW5ndWFyZC5kZXYvIiwib3JnLm9wZW5jb250YWluZXJzLmltYWdlLmNyZWF0ZWQiOiIyMDI1LTA1LTI4VDEzOjM1OjQ4WiIsIm9yZy5vcGVuY29udGFpbmVycy5pbWFnZS5zb3VyY2UiOiJodHRwczovL2dpdGh1Yi5jb20vY2hhaW5ndWFyZC1pbWFnZXMvaW1hZ2VzL3RyZWUvbWFpbi9pbWFnZXMvc3RhdGljIiwib3JnLm9wZW5jb250YWluZXJzLmltYWdlLnVybCI6Imh0dHBzOi8vaW1hZ2VzLmNoYWluZ3VhcmQuZGV2L2RpcmVjdG9yeS9pbWFnZS9zdGF0aWMvb3ZlcnZpZXciLCJvcmcub3BlbmNvbnRhaW5lcnMuaW1hZ2UudmVuZG9yIjoiQ2hhaW5ndWFyZCJ9fQ=="
}
```

The example returns the image's digest and the OCI manifest data. This proves that you've gotten a response back from the registry and that authentication worked as expected.

This example doesn't really reflect a real-world use case, as users will generally access `cgr.dev/chainguard` container repositories without authenticating. However, by presenting a token it will trigger the authentication checks, making this example useful for illustrating how this can be done with the Chainguard SDK.

You can experiment with updating this example to retrieve information about a different Chainguard container image by changing the `cgr.dev/chainguard/static` value in the `main()` function. You could replace this with any Chainguard repository you have access to, and the example will return information about that image.


## Example 2 — Authenticate with an Assumed Identity 

The [`exchange` example](https://github.com/chainguard-dev/sdk/tree/main/examples/registry/exchange) demonstrates how to exchange a token for an assumed identity to access the registry.

This example consists of the following Go code in a `main.go` file (with comments removed):

```go
package main

import (
	"context"
	"encoding/json"
	"log"
	"os"

	"chainguard.dev/sdk/auth"
	"chainguard.dev/sdk/auth/ggcr"
	"github.com/google/go-containerregistry/pkg/name"
	"github.com/google/go-containerregistry/pkg/v1/remote"
)

const (
	sub = "720909c9f5279097d847ad02a2f24ba8f59de36a/a033a6fabe0bfa0d"
)

func main() {
	ctx := context.Background()
	ts := auth.NewChainctlTokenSource(ctx)

	desc, err := remote.Get(name.MustParseReference("cgr.dev/chainguard/static"), remote.WithAuthFromKeychain(ggcr.Keychain(sub, ts)))
	if err != nil {
    	log.Fatalf("error getting reference: %v", err)
	}
	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	_ = enc.Encode(desc)
}
```

This example is similar to the previus one, but has the following differences:

* It creates a constant named `sub`. In this example, the `sub` constant's value is set to the UIDP of a Chainguard identity named `all-users` which can be assumed by any Chainguard user.
* It takes the token retrieved with the `chainctl` binary and exchanges it for the assumable identity to make a call to the Chainguard registry in order retrieve some information about the supplied image. The example uses the `cgr.dev/chainguard/static` Starter image.

To run this example, First, delete the previous example's `main.go` file if you haven't alraedy. Then save the `exchange` example's `main.go` file to your local machine. Then run the following `go mod init` and `go mod tidy` commands:

```shell
go mod init github.com/chainguard-dev/sdk && go mod tidy
```

Following that, execute the program:

```shell
go run main.go
```

This will return output like the following:

```
{
  "mediaType": "application/vnd.oci.image.index.v1+json",
  "size": 925,
  "digest": "sha256:633aabd19a2d1b9d4ccc1f4b704eb5e9d34ce6ad231a4f5b7f7a3af1307fdba8",
  "Manifest": "eyJzY2hlbWFWZXJzaW9uIjoyLCJtZWRpYVR5cGUiOiJhcHBsaWNhdGlvbi92bmQub2NpLmltYWdlLmluZGV4LnYxK2pzb24iLCJtYW5pZmVzdHMiOlt7Im1lZGlhVHlwZSI6ImFwcGxpY2F0aW9uL3ZuZC5vY2kuaW1hZ2UubWFuaWZlc3QudjEranNvbiIsInNpemUiOjgzOCwiZGlnZXN0Ijoic2hhMjU2OmJiMmRlMjU3MjFlMTE3Zjg4MDYwYjgyZGQ2YWQ1M2Y4ODdlZTgwOWU1MzE1Y2Y0MWEwMGNkOGExM2ZhMjMwNzciLCJwbGF0Zm9ybSI6eyJhcmNoaXRlY3R1cmUiOiJhbWQ2NCIsIm9zIjoibGludXgifX0seyJtZWRpYVR5cGUiOiJhcHBsaWNhdGlvbi92bmQub2NpLmltYWdlLm1hbmlmZXN0LnYxK2pzb24iLCJzaXplIjo4MzgsImRpZ2VzdCI6InNoYTI1NjoxMmVjMWU3NDg0NmVhNDM1OTNkNmExMzMwZGEyOGVkNGQzNmRmNThhMTg2NGQwOTE1MjRlM2IwYTk5MDY4Y2QzIiwicGxhdGZvcm0iOnsiYXJjaGl0ZWN0dXJlIjoiYXJtNjQiLCJvcyI6ImxpbnV4In19XSwiYW5ub3RhdGlvbnMiOnsiZGV2LmNoYWluZ3VhcmQucGFja2FnZS5tYWluIjoiIiwib3JnLm9wZW5jb250YWluZXJzLmltYWdlLmF1dGhvcnMiOiJDaGFpbmd1YXJkIFRlYW0gaHR0cHM6Ly93d3cuY2hhaW5ndWFyZC5kZXYvIiwib3JnLm9wZW5jb250YWluZXJzLmltYWdlLmNyZWF0ZWQiOiIyMDI1LTA1LTI4VDEzOjM1OjQ4WiIsIm9yZy5vcGVuY29udGFpbmVycy5pbWFnZS5zb3VyY2UiOiJodHRwczovL2dpdGh1Yi5jb20vY2hhaW5ndWFyZC1pbWFnZXMvaW1hZ2VzL3RyZWUvbWFpbi9pbWFnZXMvc3RhdGljIiwib3JnLm9wZW5jb250YWluZXJzLmltYWdlLnVybCI6Imh0dHBzOi8vaW1hZ2VzLmNoYWluZ3VhcmQuZGV2L2RpcmVjdG9yeS9pbWFnZS9zdGF0aWMvb3ZlcnZpZXciLCJvcmcub3BlbmNvbnRhaW5lcnMuaW1hZ2UudmVuZG9yIjoiQ2hhaW5ndWFyZCJ9fQ=="
}
```

As with the `chainctl` example, the `exchange` example returns the image's digest and the OCI manifest data. This proves that you've gotten a response back from the registry and that authentication worked as expected.

Again, this example doesn't really reflect a real-world use case. Users will generally access Starter container repositories without authenticating, but this example is still useful for understanding how this can be done with the Chainguard SDK.

You can experiment with updating this example to authenticate by assuming an identity you created and retrieve the digest of a container image from your organization's private repository within the Chainguard registry.

To do so, you will need an appropriately-configured assumable identity. You can create an assumable identity with the [`chainctl iam identities create` command](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/).


## Learn More

The Chainguard SDK is a powerful tool for interacting with the Chainguard platform. As mentioned previously, the examples covered in this guide don't represent a practical real-world application, but they are useful for understanding how the Chainguard SDK works and can be used to authenticate to the Chainguard platform.

To learn more, you may be interested in the following resources:

* [Overview of Assumable Identities in Chainguard](/chainguard/administration/assumable-ids/assumable-ids/)
* [Authenticate to Chainguard's Registry](/chainguard/chainguard-registry/authenticating/)
* [Chainguard OpenAPI Specification](/chainguard/administration/api/)
