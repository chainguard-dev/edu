---
title: "Chainguard Libraries repositories overview"
linktitle: "Repositories overview"
description: "Create named repositories in Chainguard Libraries, each with its own URL and upstream fallback setting"
type: "article"
date: 2026-11-12T09:00:00+00:00
lastmod: 2026-11-12T09:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Overview"]
weight: 10
toc: true
---

{{< beta feature="Repositories in Chainguard Libraries" access="a small group of organizations that Chainguard enrolls" >}}

The commands on this page work only after Chainguard enrolls your
organization. Update `chainctl` to the latest release before you start. If
your organization isn't enrolled, `chainctl` returns the following error:

```text
Libraries repositories are not available for this organization.
```

## How repositories work

Chainguard Libraries gives your organization one URL per ecosystem, such as
`https://libraries.cgr.dev/javascript/` for JavaScript. Each URL serves
packages that Chainguard builds from source. If your organization turned on
[upstream
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls),
it also serves packages from the public registry, such as the npm Registry,
that Chainguard hasn't built.

These URLs are your organization's *default repository*. If you don't create
any other repository, nothing changes: the URLs keep working exactly as they
do today.

A *repository* is an additional, named set of URLs in the same organization.
Each repository has its own upstream fallback setting. In this beta, only
JavaScript serves repository URLs. A common setup uses two repositories:

* A `prod` repository with upstream fallback off, so CI installs only packages
  that Chainguard builds.
* A `dev` repository with upstream fallback on, so engineers can install any
  package.

A JavaScript repository URL has the following form, where `example.com` is the
organization name and `prod` is the repository name:

```text
https://libraries.cgr.dev/javascript/~/example.com/prod/
```

## Plan limits

The number of repositories you can create depends on your plan:

| Plan | Repositories |
| --- | --- |
| Starter | The default repository only |
| Team | The default repository and one named repository |
| Enterprise | The default repository and as many named repositories as you need |

## Create a repository

To create a repository named `prod` in the `example.com` organization, run the
following command:

```shell
chainctl libraries repos create prod --parent example.com
```

The output shows the repository URL:

```text
Repository prod is ready.
URLs:
  JAVASCRIPT  https://libraries.cgr.dev/javascript/~/example.com/prod/
```

Running `create` again with the same name doesn't fail or create a second
repository: `chainctl` prints that the existing repository is ready and shows
its URL.

A repository can't use the name of a folder that already exists in the
organization. `chainctl` refuses the name rather than turn the existing folder
into a repository.

## View repositories

To list the repositories in an organization, run the following command:

```shell
chainctl libraries repos list --parent example.com
```

The output is a table with the `NAME`, `CREATED`, and `STATE` columns. The
list includes the default repository, named `default`, and every named
repository. A repository that's working shows the state `ready`.

To view the details of one repository, pass its name:

```shell
chainctl libraries repos describe prod --parent example.com
```

The output shows the repository's state, its creation time, the URL for each
ecosystem, and its upstream fallback setting: either `Upstream fallback: on`
or `Upstream fallback: off (every upstream registry is disabled)`.

The output also lists URLs for Java, Python, Go, and .NET, marked
`(not serving yet)`. In this beta, only JavaScript serves repository URLs.
A request to a repository URL for another ecosystem returns HTTP `503` with a
message such as `Libraries repositories are not available for java yet.`

To view the default repository, omit the name:

```shell
chainctl libraries repos describe --parent example.com
```

The output shows the default repository's URLs and the following line:

```text
This is the organization's default repository. Its upstream fallback follows the organization's Libraries entitlement.
```

## Turn upstream fallback on or off

Each new repository starts with one upstream registry for JavaScript: the
public npm Registry, listed as `npmjs`, enabled.

To view a repository's upstream registries, run the following command:

```shell
chainctl libraries repos upstreams list --parent example.com/prod --ecosystem javascript
```

To turn upstream fallback off, disable `npmjs`:

```shell
chainctl libraries repos upstreams disable npmjs --parent example.com/prod --ecosystem javascript
```

The command prints `Disabled upstream registry npmjs for JAVASCRIPT in
repository prod.` and a warning that upstream fallback is now off for
JavaScript.

To turn upstream fallback on again, enable `npmjs`:

```shell
chainctl libraries repos upstreams enable npmjs --parent example.com/prod --ecosystem javascript
```

With upstream fallback off, the repository serves packages that Chainguard
builds, and returns HTTP `404` for packages that Chainguard hasn't built. With
upstream fallback on, the repository serves both.

You can enable, disable, and reorder the upstream registries that Chainguard
provides. You can't add your own registries. Starter organizations can't change
the list.

The default repository has no upstream list of its own. Its upstream fallback
follows your organization's Libraries entitlement. If you run `upstreams list`
against the organization, `chainctl` returns the following error:

```text
the default repository has no upstream list; its upstream fallback follows the organization's Libraries entitlement
```

## Configure credentials

Two kinds of pull token work with repositories:

* An organization pull token works on the default repository URL and on every
  repository URL in the organization.
* A pull token bound to a repository works only on that repository's URL. On
  the default repository URL or on another repository's URL, the request
  returns HTTP `403`.

To create a pull token bound to the `prod` repository, run the following
command:

```shell
chainctl auth pull-token create --repository=javascript --parent example.com/prod --name ci-prod
```

For more about pull tokens, see [Chainguard Libraries
access](/chainguard/libraries/introduction/access/).

## Configure JavaScript clients

The following sections show how to point JavaScript clients at a repository
URL.

### npm

To point npm at a repository and write a pull token in one step, run the
following command:

```shell
chainctl auth configure npm --pull-token --parent example.com/prod --repo-name prod
```

The command writes a `.npmrc` file that contains the following lines:

```properties
registry=https://libraries.cgr.dev/javascript/~/example.com/prod/
//libraries.cgr.dev/javascript/:_auth=<base64-encoded-token>
//libraries.cgr.dev/javascript-upstream/:_auth=<base64-encoded-token>
```

npm matches credentials by URL prefix, so the credential keyed to
`//libraries.cgr.dev/javascript/` also covers the repository URL. If you run
the command again, it keeps the repository URL.

### pnpm

In `.npmrc`, set `registry` to the repository URL and key the credential to
either `//libraries.cgr.dev/javascript/` or `//libraries.cgr.dev/`. Both keys
work:

```properties
registry=https://libraries.cgr.dev/javascript/~/example.com/prod/
//libraries.cgr.dev/javascript/:_auth=<base64-encoded-token>
```

### Yarn Classic

In `.npmrc`, set `registry` to the repository URL, key the credential to the
full repository URL, and set `always-auth=true`:

```properties
registry=https://libraries.cgr.dev/javascript/~/example.com/prod/
//libraries.cgr.dev/javascript/~/example.com/prod/:_auth=<base64-encoded-token>
always-auth=true
```

Yarn Classic doesn't send a credential keyed to `//libraries.cgr.dev/javascript/`
to a repository URL. With that key, the request fails with HTTP `401`, which
Yarn Classic reports as `Couldn't find package`.

### Yarn

In `.yarnrc.yml`, set `npmRegistryServer` to the repository URL. Add an
`npmRegistries` entry keyed by the same full URL, with `npmAuthIdent` and
`npmAlwaysAuth: true`:

```yaml
npmRegistryServer: "https://libraries.cgr.dev/javascript/~/example.com/prod/"
npmRegistries:
  "//libraries.cgr.dev/javascript/~/example.com/prod/":
    npmAuthIdent: "<base64-encoded-token>"
    npmAlwaysAuth: true
```

An entry keyed by `//libraries.cgr.dev/javascript` doesn't authenticate
requests to a repository URL. Yarn reports `YN0033: No authentication
configured for request`.

## Responses from a repository URL

The following table shows what a client receives from a repository URL. In the
examples, `prod` has upstream fallback off and `dev` has it on. Chainguard
builds `lodash` but doesn't build `leftpad`.

| Request | Response |
| --- | --- |
| `npm install lodash` on `prod` or `dev` | Installs the package |
| `npm install leftpad` on `prod` | HTTP `404` |
| `npm install leftpad` on `dev` | Installs the package |
| Any request without credentials | HTTP `401` |
| A request to a repository that doesn't exist | HTTP `403` |
| A request from an organization that isn't enrolled | HTTP `403` |
| A repository-bound token used on another repository or on the default repository | HTTP `403` |

## Delete a repository

To delete the `dev` repository, run the following command:

```shell
chainctl libraries repos delete dev --parent example.com
```

The command asks you to confirm. To skip the confirmation, pass `--yes`.

If pull tokens or policy bindings still reference the repository, `chainctl`
refuses to delete it and names them, for example:

```text
Repository dev has 1 pull token (ci-dev). Delete them first or pass --force.
```

To delete the repository together with its pull tokens and policy bindings,
pass `--force`.

If someone deletes the repository's folder through IAM, `describe` shows the
state `folder missing` and tells you to run `chainctl libraries repos delete
NAME` to remove the repository.

## Policies and access

A repository uses its organization's [policies](/chainguard/chainguard-repository/library-policies/),
including malware blocking and cooldown. There are no per-repository policies
in this beta.

An identity bound at a repository can only pull packages from it. To create or
delete repositories, or to change their upstream registries, an identity needs
repository permissions at the organization.

## Lockfiles

Lockfiles that already contain repository URLs keep using those URLs.

## Not available in this beta

The following features aren't available in this beta:

* Per-repository policies.
* Repository URLs for Java, Python, Go, and .NET.
* CUDA Python registries on repository URLs.
* Upstream registries that you add, or that need their own credentials.
* Repositories in the Chainguard Console.
