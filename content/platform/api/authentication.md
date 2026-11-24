---
title: "Authenticating with the Chainguard SDK"
linktitle: "Authentication"
aliases:
- /chainguard/api/authentication/
- /chainguard/administration/sdk-authentication/
type: "article"
description: "Tutorial with examples showing how you can authenticate with the Chainguard SDK's auth and auth/ggcr packages."
date: 2025-06-04T08:49:31+00:00
lastmod: 2026-11-24T15:13:28+00:00
draft: false
tags: ["Chainguard Console", "Procedural"]
images: []
toc: true
weight: 40
---

There are several ways for users to interact with the Chainguard platform, with [`chainctl`](/platform/chainctl/) (Chainguard's command-line tool) and the [Chainguard Console](https://console.chainguard.dev/overview) (Chainguard's web interface) being the two most commonly-used methods. However, both of these require a human user to authenticate, and aren't useful for working with Chainguard resources programmatically.

The [Chainguard SDK](https://github.com/chainguard-dev/sdk) serves to ease programmatic integration with the Chainguard platform. This guide highlights two examples from the SDK repository that show how to authenticate to the [Chainguard registry](/chainguard/containers/registry/overview/) using the `chainguard.dev/sdk/auth` and `chainguard.dev/sdk/auth/ggcr` packages. The first has you authenticate as a local user, while the second has you authenticate as an [assumed identity](/platform/administration/assumable-ids/assumable-ids/). A third example shows how a delegate exchanges a delegation grant for an access token, with either the `chainguard.dev/sdk/sts` package or a direct HTTP request.

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
[[ACCESS_TOKEN]]
```

Then, retrieve an API token and use it to call the API:

```shell
curl -H "Authorization: Bearer $(chainctl auth token)" https://console-api.enforce.dev/iam/v1/groups | jq '.'
```

In our example, [we requested a list of groups the account belongs to](/platform/api/spec/#tag/groups/GET/iam/v1/groups). Then we piped the API response, which is in JSON, into `jq` to make it more easily readable by humans for our documentation sample. This will return output like the following, which has been edited for length:

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

## Example 2 — Authenticate with an assumed identity

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

To do so, you will need an appropriately-configured assumable identity. You can create an assumable identity with the [`chainctl iam identities create` command](/platform/chainctl/chainctl-docs/chainctl_iam_identities_create/).

### Example 2 using curl

First, login with chainctl using an OIDC token. Where the token comes from will differ by platform. Refer to our [Identity provider samples](/platform/administration/custom-idps/idp-providers/) for some examples. Replace `[[IDENTITY_ID]]` with the UIDP of your assumable identity:

```shell
chainctl auth login --identity "[[IDENTITY_ID]]" --identity-token /var/run/chainguard/oidc/oidc-token
```

Then, retrieve an API token and use it to call the API:

```shell
curl -H "Authorization: Bearer $(chainctl auth token)" https://console-api.enforce.dev/iam/v1/groups | jq '.'
```

In our example, [we requested a list of groups the account belongs to](/platform/api/spec/#tag/groups/GET/iam/v1/groups). Then we piped the API response, which is in JSON, into `jq` to make it more easily readable by humans for our documentation sample. This will return output like the following, which has been edited for length:

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

Using environment variables is helpful when working with assumable identities through the API and API tokens. Here's a high-level example of what you might do. Refer to your identity provider's documentation and [Assumable identities](/platform/administration/assumable-ids/assumable-ids/) to learn more.

Here are some sample environment variables:

```shell
# This is the UIDP of the assumable identity (refer to documentation)
IDENTITY="[[IDENTITY_ID]]"

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

Refer to the [Assumable identities documentation](/platform/administration/assumable-ids/assumable-ids/#using-the-chainguard-api) for another example of authentication using an assumed identity.

## Example 3 — Exchange a delegation grant as a delegate

<!-- TODO(blocker): Engineering must confirm the audience (aud) for a delegated token used against libraries.cgr.dev, and the capabilities a Libraries pull needs. Until then, [[CONFIRM_LIBRARIES_AUDIENCE_WITH_ENGINEERING]] stays a placeholder and this example isn't ready for Libraries use. Don't merge with the placeholder in place. -->

A *delegate* is an identity that acts only on grants its subject mints for it. You create a delegate with [`chainctl iam identities create delegate`](/platform/chainctl/chainctl-docs/chainctl_iam_identities_create_delegate/), and the subject mints a grant for it with [`chainctl auth token --delegate`](/platform/chainctl/chainctl-docs/chainctl_auth_token/). This example covers the delegate's side: exchanging the grant at the Chainguard STS for an access token.

The grant isn't an access token. No API accepts it, and its only use is as the input to the exchange. Send the token that the exchange returns to the API instead.

{{< note >}}
`chainctl auth login` doesn't perform a delegated exchange, including with `--identity-token`. If you run it as a delegate, it fails with an error like `identity [[DELEGATE_ID]] only accepts delegated exchanges`. This error is expected. Exchange the grant with an HTTP request or the Go SDK instead, as shown in this section.
{{< /note >}}

A delegated exchange has the following constraints:

* You must request both a scope and at least one capability. In an HTTP request, repeat the `cap` field once for each capability.
* The exchanged token carries only a subset of the grant's capabilities. If you request a capability the grant doesn't carry, the whole exchange fails.
* The exchanged token expires no later than the grant, and a grant lasts at most 60 minutes.
* The exchange doesn't issue a refresh token. When the exchanged token expires, the subject mints a new grant and the delegate exchanges it again.

Treat the grant as a secret until it expires. It's a bearer token for the delegated exchange, so move it from the subject to the delegate over a channel you trust, and don't log it or pass it as a command-line argument.

### Example 3 using curl

First, the subject mints a grant. This command grants the viewer role's capabilities in an organization and stores the grant in the `GRANT` variable:

```shell
GRANT=$(chainctl auth token --delegate=my-delegate --role=viewer --scope=[[ORGANIZATION_ID]])
```

Then, with the grant in the `GRANT` variable on the delegate's side, send a `POST` request to the STS exchange endpoint. The grant is the bearer token, and the delegated-exchange fields are form-encoded in the request body:

```shell
API_TOKEN=$(printf 'Authorization: Bearer %s\n' "${GRANT}" | curl -sSf \
  -H @- \
  --data-urlencode "identity=[[DELEGATE_ID]]" \
  --data-urlencode "delegated=true" \
  --data-urlencode "aud=[[CONFIRM_LIBRARIES_AUDIENCE_WITH_ENGINEERING]]" \
  --data-urlencode "scopes=[[ORGANIZATION_ID]]" \
  --data-urlencode "cap=[[CAPABILITY_1]]" \
  --data-urlencode "cap=[[CAPABILITY_2]]" \
  https://issuer.enforce.dev/sts/exchange \
  | jq -r .token
)
```

The request sets the following fields:

* `identity`: The delegate's identity ID. `chainctl iam identities create delegate --output=id` prints it.
* `delegated`: Set to `true` to request a delegated exchange.
* `aud`: The audience of the access token you're requesting. A successful exchange doesn't confirm that a service accepts this audience. To check it, call the service with the access token.
* `scopes`: The UIDP of the organization to scope the access token to.
* `cap`: One capability for the access token. Repeat the field for each capability.

`printf` is a shell built-in, and `curl -H @-` reads the header from standard input, so the grant doesn't appear in the process list. The STS returns JSON, and `jq` extracts the access token from its `token` field. Send `API_TOKEN` as a bearer token to the service that matches the audience you requested.

#### Exchange a grant for a Chainguard API token

This example applies only to the Chainguard API audience, `https://console-api.enforce.dev`, not to Chainguard Libraries. It exchanges a grant for an access token that carries the `repo.list` capability, and then uses that token to list the organization's repositories:

```shell
API_TOKEN=$(printf 'Authorization: Bearer %s\n' "${GRANT}" | curl -sSf \
  -H @- \
  --data-urlencode "identity=[[DELEGATE_ID]]" \
  --data-urlencode "delegated=true" \
  --data-urlencode "aud=https://console-api.enforce.dev" \
  --data-urlencode "scopes=[[ORGANIZATION_ID]]" \
  --data-urlencode "cap=repo.list" \
  https://issuer.enforce.dev/sts/exchange \
  | jq -r .token
)

printf 'Authorization: Bearer %s\n' "${API_TOKEN}" | curl -sSf \
  -H @- \
  "https://console-api.enforce.dev/registry/v1/repos?uidp.descendants_of=[[ORGANIZATION_ID]]" \
  | jq '.items | length'
```

The second command prints the number of repositories in the organization.

### Example 3 in Golang

The `chainguard.dev/sdk/sts` package performs the same exchange. `sts.WithDelegation()` requests the delegated exchange, `sts.WithIdentity()` names the delegate, and `sts.WithScope()` and `sts.WithCapabilities()` select the access the token carries:

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "chainguard.dev/sdk/sts"
)

func main() {
    ctx := context.Background()
    grant := os.Getenv("GRANT")

    exchanger := sts.New(
        "https://issuer.enforce.dev",
        "[[CONFIRM_LIBRARIES_AUDIENCE_WITH_ENGINEERING]]",
        sts.WithDelegation(),
        sts.WithIdentity("[[DELEGATE_ID]]"),
        sts.WithScope("[[ORGANIZATION_ID]]"),
        sts.WithCapabilities("[[CAPABILITY_1]]", "[[CAPABILITY_2]]"),
    )

    pair, err := exchanger.Exchange(ctx, grant)
    if err != nil {
        log.Fatalf("exchanging the grant: %v", err)
    }

    // Send pair.AccessToken as a bearer token. pair.RefreshToken is empty.
    fmt.Printf("Access token expires at %s\n", pair.Expiry)
}
```

The second argument to `sts.New()` is the audience of the access token you're requesting. As with the HTTP request, `Exchange()` returns no refresh token, and the access token expires no later than the grant.

## Learn more

The Chainguard SDK is a powerful tool for interacting with the Chainguard platform. As mentioned previously, the examples covered in this guide don't represent a practical real-world application, but they are useful for understanding how the Chainguard SDK works and can be used to authenticate to the Chainguard platform.

To learn more, you may be interested in the following resources:

* [Overview of assumable identities in Chainguard](/platform/administration/assumable-ids/assumable-ids/)
* [Authenticate to Chainguard's registry](/chainguard/containers/registry/authenticating/)
* [Chainguard OpenAPI specification](/platform/api/spec/)
