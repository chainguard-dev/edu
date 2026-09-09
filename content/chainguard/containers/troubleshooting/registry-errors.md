---
title: "Troubleshoot registry authentication errors"
linktitle: "Registry errors"
description: "Map the errors cgr.dev returns during login and pull to their causes, including why the same HTTP status code means different things at the token endpoint and the registry API."
type: "article"
date: 2026-09-09T00:00:00+00:00
lastmod: 2026-09-09T17:21:21+00:00
draft: false
tags: ["Chainguard Containers", "Registry"]
images: []
weight: 015
toc: true
---

A login or pull against `cgr.dev` failed and you have an error string. This page maps the errors Chainguard's registry returns to their causes and tells you what to check for each one.

If your pull fails for a container you can see in the [Chainguard Containers Directory](https://images.chainguard.dev/), the container most likely hasn't been added to your organization yet. That case has its own guide: refer to [Troubleshoot container and version availability](/chainguard/containers/troubleshooting/container-version-troubleshooting/).

## Where registry errors come from

Pulling a container from `cgr.dev` takes two separate requests, and each one fails differently:

1. **Credential exchange.** Your tool sends your credentials to the token endpoint at `https://cgr.dev/token` and gets back a bearer token scoped to the repository you asked for. `docker login`, `helm registry login`, `podman login`, and `chainctl auth configure-docker` all exercise this step.
1. **The pull.** Your tool presents that bearer token to the registry API at `https://cgr.dev/v2/` and requests the tags, manifest, and layers.

The two steps reuse the same HTTP status codes for unrelated problems. A `403` from the token endpoint means something different from a `403` from the registry API, so read the error code and message in the response body rather than the status number on its own:

| Response body | Returned by | Meaning |
| -- | -- | -- |
| `UNAUTHORIZED`, "Authentication required" | Token endpoint | The repository requires credentials and you presented none that worked. |
| `FORBIDDEN`, "Forbidden" | Token endpoint | The endpoint won't issue a token for the repository you named, or it couldn't use the credentials you sent. |
| `BAD_REQUEST`, "InvalidArgument" | Token endpoint | The organization in the image reference didn't resolve. |
| `FORBIDDEN`, "caller does not have the required capabilities" | Registry API | You're authenticated, but you aren't authorized for this repository. |
| `NAME_UNKNOWN`, "repository does not exist" | Registry API | The repository name doesn't exist in that organization. |

A bare `Forbidden` message doesn't tell you which of those two it is. Chainguard's registry returns the same `403` to a caller that sent no credentials, a caller whose credentials it can't use, and a caller naming a repository it won't grant a token for. Treat it as a prompt to work through the possible causes in order rather than as a single diagnosis, and in particular don't read it as confirmation that your credentials were accepted.

## Authentication required from the token endpoint

You'll see a `401` like the following when a build or pull runs with no credentials configured:

```output
failed to fetch anonymous token: unexpected status from GET request to https://cgr.dev/token?scope=repository%3A$ORGANIZATION%2Fpython%3Apull&service=cgr.dev: 401 Unauthorized
```

The word "anonymous" is the signal. Your tool found no credentials for `cgr.dev`, so it asked for a public token, and the repository you named isn't public. Containers in the `cgr.dev/chainguard/` namespace are public and need no authentication. Everything in your organization's own namespace at `cgr.dev/$ORGANIZATION/` requires credentials.

Configure the credential helper, then retry:

```shell
chainctl auth configure-docker
```

You don't need to run `chainctl auth login` first. For headless machines, CI systems, and other login flows, refer to [Authenticate to Chainguard's Registry](/chainguard/containers/registry/authenticating/) and [Authentication options for `chainctl`](/platform/chainctl-usage/authentication-options/).

If the failure happens inside `docker build` rather than `docker pull`, check that the builder can see your Docker configuration. A `FROM` line pointing at your organization's namespace needs the same credentials a direct pull does.

## Forbidden from the token endpoint

A `403` from the token endpoint looks like this, often from `helm registry login` or another tool that logs in without naming a repository:

```output
Error: authenticating to "cgr.dev": GET "https://cgr.dev/token?service=cgr.dev": response status code 403: forbidden
```

This response means the token endpoint rejected the request outright. It doesn't tell you which part of the request it objected to, so check these in order:

1. **The credential format.** The username for a pull token is the Chainguard identity ID that owns the token, not your email address. Refer to [Check your credential format](#check-your-credential-format).
1. **The credential's age.** Pull tokens expire 30 days after creation by default. Create a replacement with `chainctl auth configure-docker --pull-token`.
1. **The repository name.** A scope the endpoint won't grant returns this `403` rather than a `404`, whether the repository doesn't exist or isn't in your organization's catalog. Confirm the name against `chainctl images repos list`.

## The organization didn't resolve

A `400` means the organization portion of the image reference didn't match any Chainguard organization:

```output
{"errors":[{"code":"BAD_REQUEST","message":"rpc error: code = InvalidArgument desc = unable to resolve ..."}]}
```

Unlike the other errors on this page, this one has nothing to do with your credentials. The organization name is wrong. List the organizations you belong to and compare:

```shell
chainctl iam organizations list
```

Organization names are usually domain names, such as `example.com`, and the full image reference is `cgr.dev/$ORGANIZATION/$IMAGE:$TAG`. Omitting the organization, or using your organization's display name instead of its registry name, can produce this error.

## Missing capabilities from the registry API

This `403` is the one that means your login worked and your authorization didn't:

```output
{"errors":[{"code":"FORBIDDEN","message":"caller does not have the required capabilities at \"...\""}]}
```

It also surfaces through the tool you're running. A Helm install that logged in successfully and then failed reports it against the API path:

```output
Error: INSTALLATION FAILED: ... /$ORGANIZATION/postgresql/tags/list ... response status code 403
```

Two different problems produce this error, and the fix differs:

- **The repository isn't in your organization's catalog.** This is the more common cause. Your credentials are valid, but the container hasn't been added to your organization. Refer to [Troubleshoot container and version availability](/chainguard/containers/troubleshooting/container-version-troubleshooting/) for how to add it or request it, along with the roles that each path requires.
- **Your identity lacks a role that grants pull access.** Check which capabilities your current credentials carry:

    ```shell
    chainctl auth status
    ```

    Read the `Capabilities` field in the output. Pulling containers needs a role with the `manifest (list)` capability; `registry.pull` is the least privileged built-in role that has it. To grant it, refer to [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/). Pulling APK packages needs `apk (list)` instead, which [Private APK repositories](/chainguard/containers/building-and-modifying/packages/private-apk-repos/#troubleshooting) covers.

An identity federated from a CI system carries only the role you assigned when you created it. An identity created with `--role=registry.pull` can pull containers and do nothing else, which is intentional, but it means the same credentials fail if your workflow later tries to list repositories or read entitlements.

## Repository does not exist

Once you hold a valid token, a name that isn't in the organization returns a `404` rather than a `403`:

```output
{"errors":[{"code":"NAME_UNKNOWN","message":"repository does not exist \"...\""}]}
```

Check the spelling against `chainctl images repos list`, then against the [Chainguard Containers Directory](https://images.chainguard.dev/). If the Directory doesn't list the container either, Chainguard doesn't build it yet and you can ask for it through [Requesting new Chainguard resources](/chainguard/containers/reference/request-resources/). To work out which of those situations you're in, refer to [Troubleshoot container and version availability](/chainguard/containers/troubleshooting/container-version-troubleshooting/).

## Check your credential format

When you authenticate with a pull token, the username is the Chainguard identity ID associated with that token, and the password is the token itself:

```shell
docker login "cgr.dev" \
  --username "<identity-id>" \
  --password "<pull-token>"
```

The email address you use to sign in to the Chainguard Console is not a valid registry username. Neither is your organization name. `chainctl auth configure-docker --pull-token` prints the correct pair, and `chainctl auth pull-token create --output=env` writes them to `CHAINGUARD_IDENTITY_ID` and `CHAINGUARD_TOKEN` for use in scripts.

The same pair works with any tool that logs in to an OCI registry:

```shell
helm registry login cgr.dev \
  --username "$CHAINGUARD_IDENTITY_ID" \
  --password "$CHAINGUARD_TOKEN"
```

Helm and Podman need `chainctl` installed only to create the token. Once you have the identity ID and token, the login itself doesn't call `chainctl`, so you can run it on a machine that doesn't have `chainctl` at all. Refer to [pull token output formats and credential names](/platform/chainctl-usage/pull-token-output/) for the other output formats.

## Errors from a pull-through cache or mirror

A registry mirror reports Chainguard's errors in its own wording, which can obscure which of the preceding cases you're in. Artifactory, for example, reports a rejected credential as a configuration problem:

```output
Invalid username/password configured for Remote Docker repository: $REPOSITORY_NAME ... Can't fetch token for repo ... realm: https://cgr.dev/token
```

The `realm: https://cgr.dev/token` fragment tells you the failure happened during credential exchange, so work through [Forbidden from the token endpoint](#forbidden-from-the-token-endpoint) and [Check your credential format](#check-your-credential-format). Mirrors are a common place for the username to be wrong, because their configuration forms label the field "username" and invite an email address.

Pull tokens expire, so a mirror that worked for a month and then stopped is likely holding an expired token. For the tool-specific settings each platform needs, refer to the [pull-through guides](/chainguard/containers/registry/pull-through-guides/).

## Isolate the failing step

To find out which of the two requests is failing, ask the token endpoint directly. This returns the HTTP status for a credential exchange with no credentials attached:

```shell
curl -s -o /dev/null -w '%{http_code}\n' \
  "https://cgr.dev/token?scope=repository%3A$ORGANIZATION%2F$IMAGE%3Apull&service=cgr.dev"
```

A `401` means the reference resolved and the endpoint wants credentials, so your tool's configuration is the problem rather than the name you used. Drop the `-o /dev/null` to read the error code and message in the response body.

To check the second request, compare `chainctl auth status` against the capabilities listed in [Missing capabilities from the registry API](#missing-capabilities-from-the-registry-api).

## Can't create a pull token

If the Console won't let you create a pull token, or `chainctl auth pull-token create` fails, the problem is your role rather than the registry. Creating a pull token creates a Chainguard identity and a role-binding for it, so it needs a role carrying the `identity (create)` and `role_bindings (create)` capabilities.

`registry.pull_token_creator` is the least privileged built-in role with both. Ask an administrator in your organization to bind it to your account, or refer to [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) to do it yourself. The [capabilities reference](/platform/administration/iam-organizations/roles-role-bindings/capabilities-reference/) lists every capability each built-in role carries.

## Learn more

- [Authenticate to Chainguard's Registry](/chainguard/containers/registry/authenticating/)
- [Troubleshoot container and version availability](/chainguard/containers/troubleshooting/container-version-troubleshooting/)
- [Onboard your teams](/get-started/onboard-your-teams/#what-your-organization-can-pull)
- [Network requirements](/chainguard/containers/registry/network-requirements/)
- [Get support](/get-started/get-support/)
