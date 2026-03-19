---
title: "Authenticating with the Chainguard SDK"
linktitle: "Authentication"
aliases:
- /chainguard/administration/sdk-authentication/
type: "article"
description: "Tutorial with examples showing how you can authenticate with the Chainguard SDK's auth and auth/ggcr packages."
date: 2025-06-04T08:49:31+00:00
lastmod: 2025-06-04T15:22:20+01:00
draft: false
tags: ["Chainguard Console", "Procedural"]
images: []
toc: true
weight: 065
---

There are several ways for users to interact with the Chainguard platform, with [`chainctl`](/chainguard/chainctl/) (Chainguard's command-line tool) and the [Chainguard Console](https://console.chainguard.dev/overview) (Chainguard's web interface) being the two most commonly-used methods. However, both of these require a human user to authenticate, and aren't useful for working with Chainguard resources programmatically.

The [Chainguard SDK](https://github.com/chainguard-dev/sdk) serves to ease programmatic integration with the Chainguard platform. This guide highlights two examples from the SDK repository that show how to authenticate to the [Chainguard registry](/chainguard/chainguard-registry/overview/) using the `chainguard.dev/sdk/auth` and `chainguard.dev/sdk/auth/ggcr` packages. The first has you authenticate as a local user, while the second has you authenticate as an [assumed identity](/chainguard/administration/assumable-ids/assumable-ids/).

This page gives examples in Golang as well as using `curl`. For more information about the Golang examples, refer to the [`examples` folder](https://github.com/chainguard-dev/sdk/tree/main/examples/registry) in the SDK repository.


## Prerequisites

To follow along with this guide you must have [Go installed](https://go.dev/doc/install) to run the  examples provided by the SDK repository, which are written in Golang. Additional examples in `curl` are found just after the discussion of each Golang example.

Additionally, it may help to run these examples from a temporary directory, like `/tmp` so the code is automatically removed from your system the next time it boots:

```shell
cd /tmp
```


## Example 1 — Authenticate using local credentials

The first example from the SDK repository we will go over is the [`chainctl` example](https://github.com/chainguard-dev/sdk/tree/main/examples/registry/chainctl). This example shows how to use a token source backed by `chainctl` — Chainguard's command-line tool — to access the Chainguard registry using local credentials.

### Example 1 in Golang

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
* Using this token, the example makes a call to the Chainguard registry to retrieve some information about the supplied image. The example uses the `cgr.dev/chainguard/static` Free image.

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


### Example 1 using curl

To authenticate using `curl` and the API, first authenticate directly with `chainctl`:

```shell
chainctl auth login
```

This will return output like the following:

```response
Opening browser to https://issuer.enforce.dev/oauth?audience=https%3A%2F%2Fconsole-api.enforce.dev&client_id=auth0&connection=google-oauth2&create_refresh_token=true&exit=redirect&redirect=http%3A%2F%2Flocalhost%3A44723%2Fcallback%3Ftoken%3Dtrue%26error%3Dtrue&skip_registration=true
Opening in existing browser session.
eyJhbGciOiJSUzI1NiIsImtpZCIiwibmFtZSI6SRi0IvgxPIlU8LfgLIk1hdHRoU5NmIxNzM3OGZlNzU51ZjczNTgxNTQ3ODU4OWM2MzNlZTQwZDUyOGMwYTAifQ.eyJhY3QiOnsiYXVkIjoiSHZxeTd5b0VoSThUWTF6WDlyUHJzZGNJbnREejl5aDIiLCJpc3MiOiJodHRwczovL2F1dGguY2hhaW5ndWFyZC5kZXYvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTUzMTIxMjYyNzg5NDAzNzAyMTgifSwiYXVkIjoiaHR0cHM6Ly9jb25zb2xlLWFwaS5lbmZvcmNlLmRldiIsImNhcCI6eyIwYWM3ZmY5MDU4NTBjMzU3MjNhN2YzNzZlMTBkMDA3Yzk1OGM0NWM4IjoiQUFBQUFBQUFBSHhFUWdCQWdJQkVTQWlJR0RCQWlxbGsiLCI0NWEwYzYxZWE2ZmQ5NzdmMDUwYzVmYjlhYzA2YTY5ZWVkNzY0NTk1IjoiQUFBQUFBQUFBSHpfOGdEeDRlRF9fZ25vLURCQl9fdHYiLCI1NWE1OGJjOGU0ZTNkZGNmNWJiZTczYWIwOTA4NzhmYTM1ZDBhNWE5IjoiQUFBQUFBQUFBSHpfOGdEeDRlRF9fZ25vLURCQl9fdHYiLCI3MjA5MDljOWY1Mjc5MDk3ZDg0N2FkMDJhMmYyNGJhOGY1OWRlMzZhIjoiQUFBQUFBQUFBSHhFUWdCQWdJQkVTQWlJR0RCQWlxbGsiLCI4ZDAwODEwYjBhMDI5NTU5ZTUyMzk5ODU1MDMxOTU4ZWY0OGJlNmM4IjoiQUFBQUFBQUFBSHhFUWdCQWdJQkVTQWlJR0RCQWlxbGsiLCI4ZGQwMGJjZmYyMjQzNGQ3YzEwMDdmZWY2Nzg5Mzk0NWU4YmNiNDM1IjoiQUFBQUFBQUFBRndBQUFBQUFBQUFBQUFBQUFBSUFBQUEiLCJhNzBkOTg5ZDgyMWJjMzE1ZmViYTlmYjU4NWQ0ZWNlMzVjODJjMjgyIjoiQUFBQUFBQUFBSHpfOGdEeDRlRF9fZ25vLURCQl9fdHYiLCJiMTkwNGI0MWU1Mzg1Yzk1ZGY3MDlhZjZhY2EzNTMwNTExMzgzZmVmIjoiQUFBQUFBQUFBSHhFUWdCQWdJQkVTQWlJR0RCQWlxbGsiLCJjYTQzOGQ3NmFjYmFkMDI5N2I3NzNkNjgzODkwZmJlNWQ5OWRiOGI1IjoiQUFBQUFBQUFBRzFFQWdBQUlBQVVDQUFBR1lBQmFBbGsiLCJjZTJkMTk4NGEwMTA0NzExNDI1MDMzNDBkNjcwNjEyZDYzZmZiOWY2IjoiQUFBQUFBQUFBSHhFUWdCQWdJQkVTQWlJR0RCQWlxbGsifSwiZW1haWwiOiJtYXR0aGV3LmhlbG1rZUBjaGFZTYwNDRjMDY5N2Y3ZlcmlmaWVkIjp0cnVlLCJleHAiOjE3NzM5MjYzNTcsImlhdCI6MTc3MzkyMjc1NywiaW50ZXJuYWwiOnsiZGVidWciOnRydWV9LCJpc3MiOiJodHRwczovL2lzc3Vlci5lbmZvcmNlLmRldiIsInN1YiI6IjY5MDkxMmNmM2U3Njk3OWVjYTVhYThjOWUyY2VmOTI3MDRhMTEyOTYiLCJ1cHN0cmVhbSI6eyJlbWFpbCI6Im1hdHRoZXcuaGVsbWtlQGNoYWluZ3VhcmQuZGV2ZXcgSGVsbWtlIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0lERmdNeWZ4X2NOR2I0bGtwZ1VTbVA2WjlUSXg0NnZud3JtdDhEQmZYNkZYdmc2R009czk2LWMifX0.GnN8_oJwL3mgutHM3IoX65g8aYoEKmG0-dSHvlxXDYwB6cWpTlfNJKmkJjD5rT8exWnSiP_ibq9SZB7rA23pl17Gn0hdHH42lgKSKzdM6471E_Yz2cThxOKR4KrMDnI9UvIBrZ2cZ270WU21q0soIt5XBcEBTiZ1t2ehfvcVgSi4kq87pNQjF5esmeP71kiCQAtyQuEKKwLB-9ShIVJaSnmgjX3kWtOyXur9fBFXO7XBC6b9DKp3mzsc7JMyNE2UEKN5psHkprfARWa-MFYLsN4MKxo23CEUTOxmRaQzfznOdwDHwZgjN9tfp3RMqG6owvq5x4-H6OAIh6eKfVSadcBsgs2p__WpqPB66rZAt-J6E-NZlNzU51ZjczNTgxNTQ3ODU4tvNyqsxZhnN7rPv1Q0nc18e4JtYzIsBFr-SRi0IvgxPIlU8LfgLKI_CuZ3Uhk503M1lTlin2cPJi3DyDAc3xOeTr3NjSxJ2wOgUErgkZJg70aOoIpSV_4zRC_Qy8-aha-eICEEKs98yVw7GPSrPQpBBcIm0ud0pIM2e-33AVNG-D_mfA2chEZMxoFvZzZaF6xNv7v9r3TlyQ2m2mEJyt9qxkwgsoXaxHhHyjhEkfctP_4cNQ03ytwxqvo4o1SjsCTdo_CxdSOS2JMIvcpq-GDohWUZSAG
```

Then, retrieve an API token and use it to call the API:

```shell
curl -H "Authorization: Bearer $(chainctl auth token)" https://console-api.enforce.dev/iam/v1/groups | jq '.'
```

In our example, [we requested a list of groups the account belongs to](https://edu.chainguard.dev/chainguard/api/spec/#tag/groups/GET/iam/v1/groups). Then we piped the API response, which is in JSON, into `jq` to make it more easily readable by humans for our documentation sample. This will return output like the following, which has been edited for length:

```response
{
  "items": [
    {
      "id": "<removed>",
      "name": "chainguard.edu",
      "description": "Developer Enablement images catalog",
      "resourceLimits": {
        "clusters": 0,
        "idps": 0,
        "repositories": 0
      },
      "verified": true
    },
    {
      "id": "<removed>",
      "name": "chainguard",
      "description": "    This group holds the public Chainguard Images hosted under\n    cgr.dev/chainguard\n",
      "resourceLimits": {},
      "verified": true
    }
  ]
}
```

## Example 2 — Authenticate with an Assumed Identity 

The [`exchange` example](https://github.com/chainguard-dev/sdk/tree/main/examples/registry/exchange) demonstrates how to exchange a token for an assumed identity to access the registry.

### Example 2 in Golang

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

This example is similar to the previous one, but has the following differences:

* It creates a constant named `sub`. In this example, the `sub` constant's value is set to the UIDP of a Chainguard identity named `all-users` which can be assumed by any Chainguard user.
* It takes the token retrieved with the `chainctl` binary and exchanges it for the assumable identity to make a call to the Chainguard registry in order to retrieve some information about the supplied image. The example uses the `cgr.dev/chainguard/static` Free image.

To run this example, first, delete the previous example's `main.go` file if you haven't already. Then save the `exchange` example's `main.go` file to your local machine. Then run the following `go mod init` and `go mod tidy` commands:

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

Again, this example doesn't really reflect a real-world use case. Users will generally access Free container repositories without authenticating, but this example is still useful for understanding how this can be done with the Chainguard SDK.

You can experiment with updating this example to authenticate by assuming an identity you created and retrieve the digest of a container image from your organization's private repository within the Chainguard registry.

To do so, you will need an appropriately-configured assumable identity. You can create an assumable identity with the [`chainctl iam identities create` command](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create/).


### Example 2 using curl

First, login with chainctl using an OIDC token. Where the token comes from will differ by platform. Refer to our [Identity Provider samples](/chainguard/administration/custom-idps/idp-providers/) for some examples.

```shell
chainctl auth login --identity "<identity-id>" --identity-token /var/run/chainguard/oidc/oidc-token
```

Then, retrieve an API token and use it to call the API:

```shell
curl -H "Authorization: Bearer $(chainctl auth token)" https://console-api.enforce.dev/iam/v1/groups | jq '.'
```

In our example, [we requested a list of groups the account belongs to](https://edu.chainguard.dev/chainguard/api/spec/#tag/groups/GET/iam/v1/groups). Then we piped the API response, which is in JSON, into `jq` to make it more easily readable by humans for our documentation sample. This will return output like the following, which has been edited for length:

```response
{
  "items": [
    {
      "id": "<removed>",
      "name": "chainguard.edu",
      "description": "Developer Enablement images catalog",
      "resourceLimits": {
        "clusters": 0,
        "idps": 0,
        "repositories": 0
      },
      "verified": true
    },
    {
      "id": "<removed>",
      "name": "chainguard",
      "description": "    This group holds the public Chainguard Images hosted under\n    cgr.dev/chainguard\n",
      "resourceLimits": {},
      "verified": true
    }
  ]
}
```

While using assumable identities with the API and API tokens, it is useful to use environment variables. Here's a high-level example of what you might do. Refer to your identity provider's documentation and [Assumable Identities](/chainguard/administration/assumable-ids/assumable-ids/) to learn more.

Here are some sample environment variables:

```shell
# This is the UIDP of the assumable identity (refer to documentation)
IDENTITY="<identity-id>"

# Retrieve the OIDC token for your workload. How this is done will differ by platform.
IDENTITY_TOKEN=$(cat /var/run/chainguard/oidc/oidc-token)

# Exchange the OIDC token for a Chainguard API token. The token will be valid for an hour.
API_TOKEN=$(curl -sSf \
  -H "Authorization: Bearer $IDENTITY_TOKEN" \
   "https://issuer.enforce.dev/sts/exchange?aud=https://console-api.enforce.dev&identity=$IDENTITY" \
   | jq -r .token
)

# Use the API token
curl -H "Authorization: Bearer ${API_TOKEN}" https://console-api.enforce.dev/registry/v1/repos
```

Refer to the [Assumable Identities documentation](/chainguard/administration/assumable-ids/assumable-ids/#using-the-chainguard-api) for another example of authentication using an assumed identity.


## Learn More

The Chainguard SDK is a powerful tool for interacting with the Chainguard platform. As mentioned previously, the examples covered in this guide don't represent a practical real-world application, but they are useful for understanding how the Chainguard SDK works and can be used to authenticate to the Chainguard platform.

To learn more, you may be interested in the following resources:

* [Overview of Assumable Identities in Chainguard](/chainguard/administration/assumable-ids/assumable-ids/)
* [Authenticate to Chainguard's Registry](/chainguard/chainguard-registry/authenticating/)
* [Chainguard OpenAPI Specification](/chainguard/api/spec/)