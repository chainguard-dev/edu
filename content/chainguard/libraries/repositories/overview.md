---
title: "Chainguard Libraries repositories overview"
linktitle: "Repositories overview"
description: "Create named repositories in Chainguard Libraries, each with its own URL and upstream fallback setting"
type: "article"
date: 2026-11-12T09:00:00+00:00
lastmod: 2026-11-25T09:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Overview"]
weight: 10
toc: true
---

{{< beta feature="Repositories in Chainguard Libraries" >}}

## How repositories work

Chainguard Libraries gives your organization one URL per ecosystem, such as
`https://libraries.cgr.dev/javascript/` for JavaScript. Each URL serves
packages that Chainguard builds from source. If your organization turned on
[upstream
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls),
it also serves packages from the public registry, such as the public npm
registry, that Chainguard hasn't built.

These URLs are your organization's *default repository*. If you don't create
any other repository, nothing changes: the URLs keep working as before.

A *repository* is an additional, named set of URLs in the same organization.
Each repository has its own upstream fallback setting and can have its own
policy. In this beta, Chainguard Libraries serves repository URLs for
JavaScript and Java. A common setup uses two repositories:

* A `prod` repository with upstream fallback off, so CI installs only packages
  that Chainguard builds.
* A `dev` repository with upstream fallback on, so engineers can install any
  package.

Repository URLs have the following form, where `example.com` is the
organization name and `prod` is the repository name:

| Ecosystem | Repository URL |
| --- | --- |
| JavaScript | `https://libraries.cgr.dev/javascript/~/example.com/prod/` |
| Java | `https://libraries.cgr.dev/java/~/example.com/prod/` |
| Java remediated builds | `https://libraries.cgr.dev/java-remediated/~/example.com/prod/` |

To manage repositories, update `chainctl` to the latest release. Java
repositories need `chainctl` v0.2.408 or later. For instructions, refer to
[How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/).

## Plan limits

The number of repositories you can create depends on your plan:

| Plan | Repositories |
| --- | --- |
| Starter | The default repository only |
| Team | The default repository and one named repository |
| Enterprise | The default repository and as many named repositories as you need |

If you run `chainctl libraries repos create` in a Starter organization,
`chainctl` returns the following message:

```text
Starter plans include only the default repository; upgrade to Team for more.
```

## Create a repository

To create a repository named `prod`, run the following command:

```shell
chainctl libraries repos create prod
```

The output shows the repository URL for each ecosystem your organization is
entitled to, for example:

```text
Repository prod is ready.
URLs:
  JAVASCRIPT  https://libraries.cgr.dev/javascript/~/example.com/prod/
  JAVA        https://libraries.cgr.dev/java/~/example.com/prod/
```

Running `create` again with the same name doesn't fail or create a second
repository: `chainctl` prints that the existing repository is ready and shows
its URL.

A repository can't use the name of a folder that already exists in the
organization. `chainctl` returns an error instead of turning the existing folder
into a repository.

## View repositories

To list the repositories in an organization, run the following command:

```shell
chainctl libraries repos list
```

The output is a table with the `NAME`, `CREATED`, and `STATE` columns. The
list includes the default repository, named `default`, and every named
repository. A repository that's working shows the state `ready`.

To view the details of one repository, pass its name:

```shell
chainctl libraries repos describe prod
```

The output shows the repository's state, its creation time, the URL for each
ecosystem, and its upstream fallback setting: either `Upstream fallback: on`
or `Upstream fallback: off (every upstream registry is disabled)`.

A URL marked `(not serving yet)` belongs to an ecosystem that doesn't serve
repository URLs in this beta. Chainguard Libraries refuses requests to it.

To view the default repository, omit the name:

```shell
chainctl libraries repos describe
```

The output shows the default repository's URLs and the following line:

```text
This is the organization's default repository. Its upstream fallback follows the organization's Libraries entitlement.
```

## Turn upstream fallback on or off

Every repository lists the public npm registry as `npmjs`. A new repository
starts with `npmjs` enabled if your organization's Libraries entitlement
includes upstream fallback, and disabled if it doesn't.

Without that entitlement, upstream fallback stays off even if you enable
`npmjs`, and `describe` says so.

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

A change to upstream fallback takes effect within about a minute. Chainguard
Libraries caches resolved package versions for one minute, so a pull right
after you disable `npmjs` can still return the upstream version.

To turn upstream fallback on again, enable `npmjs`:

```shell
chainctl libraries repos upstreams enable npmjs --parent example.com/prod --ecosystem javascript
```

With upstream fallback off, the repository serves packages that Chainguard
builds, and returns HTTP `404` for packages that Chainguard hasn't built. With
upstream fallback on, the repository serves both.

You can enable, disable, and reorder the upstream registries that Chainguard
provides. You can't add your own registries. If your organization downgrades
to Starter and keeps a named repository, you can disable an upstream registry
but not enable or reorder one.

The default repository has no upstream list of its own. Its upstream fallback
follows your organization's Libraries entitlement. If you run `upstreams list`
against the organization, `chainctl` returns the following error:

```text
the default repository has no upstream list; its upstream fallback follows the organization's Libraries entitlement
```

### Java upstream registries

A Java repository lists five upstream registries: `maven-central`,
`google-maven`, `gradle-plugins`, `confluent`, and `jboss-releases`. The
repository tries the enabled registries in the order of the list. With none
enabled, upstream fallback is off for Java.

To view, disable, or enable a Java upstream registry, pass `--ecosystem java`:

```shell
chainctl libraries repos upstreams list --parent example.com/prod --ecosystem java
chainctl libraries repos upstreams disable google-maven --parent example.com/prod --ecosystem java
chainctl libraries repos upstreams enable google-maven --parent example.com/prod --ecosystem java
```

To change the order, list every registry once, the first tried first:

```shell
chainctl libraries repos upstreams reorder maven-central gradle-plugins google-maven confluent jboss-releases \
  --parent example.com/prod --ecosystem java
```

## Configure credentials

Two kinds of pull token work with repositories:

* An organization pull token works on the default repository URL and on every
  repository URL in the organization.
* A pull token bound to a repository works only on that repository's URLs. On
  the default repository URL or on another repository's URL, the request
  returns HTTP `403`. A Java token bound to a repository works on both of its
  Java URLs.

To create a pull token bound to the `prod` repository, run the following
command:

```shell
chainctl auth pull-token create --repository=javascript --parent example.com/prod --name ci-prod
```

For Java, pass `--repository=java`:

```shell
chainctl auth pull-token create --repository=java --parent example.com/prod --name ci-prod-java
```

For more information about pull tokens, refer to [Chainguard Libraries
access](/chainguard/libraries/introduction/access/).

## Configure JavaScript clients

The following sections show how to point JavaScript clients at a repository
URL.

### npm

To point npm at a repository and write a pull token in one step, run the
following command:

```shell
chainctl auth configure npm --pull-token --parent example.com/prod
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

If the project already installed packages from the default repository, its
`package-lock.json` pins every package to the default repository URL, for
example:

```json
"resolved": "https://libraries.cgr.dev/javascript/lodash/-/lodash-4.17.21.tgz"
```

npm ignores `registry` for packages already in the lockfile and fetches each
`resolved` URL as written, so every request still goes to the default
repository. A pull token bound to the repository returns HTTP `403` there. An
organization pull token works, but npm installs from the default repository,
so the repository's upstream fallback setting never applies.

To fix this, regenerate the lockfile once:

```shell
rm package-lock.json && npm install
```

After that, every `resolved` URL is under the repository URL, and `npm ci`
pulls through the repository.

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

Yarn Classic doesn't send a credential keyed to
`//libraries.cgr.dev/javascript/` to a repository URL. With that key, the
request fails with HTTP `401`, which Yarn Classic reports as `Couldn't find
package`.

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

## Configure Java clients

`chainctl auth configure` has no Maven or Gradle form. Copy the repository
URLs into your build configuration, and use a pull token bound to the
repository. If your organization's entitlement includes remediated builds,
list the remediated URL first, as for the default repository in [Configure
Java build tools](/chainguard/libraries/java/build-configuration/#direct-access).

### Maven

In `~/.m2/settings.xml`, list the repository URLs in the `chainguard` profile
and give each one a `server` entry with the pull token:

```xml
<settings>
  <activeProfiles>
    <activeProfile>chainguard</activeProfile>
  </activeProfiles>
  <profiles>
    <profile>
      <id>chainguard</id>
      <repositories>
        <repository>
          <id>chainguard-remediated</id>
          <url>https://libraries.cgr.dev/java-remediated/~/example.com/prod/</url>
        </repository>
        <repository>
          <id>chainguard-java</id>
          <url>https://libraries.cgr.dev/java/~/example.com/prod/</url>
        </repository>
      </repositories>
    </profile>
  </profiles>
  <servers>
    <server>
      <id>chainguard-remediated</id>
      <username>${env.CHAINGUARD_JAVA_IDENTITY_ID}</username>
      <password>${env.CHAINGUARD_JAVA_TOKEN}</password>
    </server>
    <server>
      <id>chainguard-java</id>
      <username>${env.CHAINGUARD_JAVA_IDENTITY_ID}</username>
      <password>${env.CHAINGUARD_JAVA_TOKEN}</password>
    </server>
  </servers>
</settings>
```

If your `settings.xml` also has a `mirror` or `pluginRepository` entry for
`https://libraries.cgr.dev/java/`, change its URL to the repository URL too. A
pull token bound to the repository returns HTTP `403` on the default
repository URL.

### Gradle

In `build.gradle`, list the repository URLs in the `repositories` block, above
any other repository:

```groovy
repositories {
    maven {
        url = uri("https://libraries.cgr.dev/java-remediated/~/example.com/prod/")
        credentials {
            username = providers.environmentVariable("CHAINGUARD_JAVA_IDENTITY_ID").orNull
            password = providers.environmentVariable("CHAINGUARD_JAVA_TOKEN").orNull
        }
    }
    maven {
        url = uri("https://libraries.cgr.dev/java/~/example.com/prod/")
        credentials {
            username = providers.environmentVariable("CHAINGUARD_JAVA_IDENTITY_ID").orNull
            password = providers.environmentVariable("CHAINGUARD_JAVA_TOKEN").orNull
        }
    }
}
```

## Responses from a repository URL

The following table shows what a client receives from a repository URL. In the
examples, `prod` has upstream fallback off and `dev` has it on. Chainguard
builds `lodash`. For a package that Chainguard doesn't build but the public npm
registry hosts, the examples use `five`.

| Request | Response |
| --- | --- |
| `npm install lodash` on `prod` or `dev` | Installs the package |
| `npm install five` on `prod` | HTTP `404` |
| `npm install five` on `dev` | Installs the package |
| A Java artifact that Chainguard builds, on `prod` or `dev` | Served |
| A Java artifact that only an upstream registry holds, on `prod` | HTTP `404` |
| A Java artifact that only an upstream registry holds, on `dev` | Served |
| A request without credentials | HTTP `401` |
| A request to a repository that doesn't exist | HTTP `403` |
| A repository-bound token used on another repository or on the default repository | HTTP `403` |

## Delete a repository

To delete the `dev` repository, run the following command:

```shell
chainctl libraries repos delete dev
```

The command asks you to confirm. To skip the confirmation, pass `--yes`.

If pull tokens or policy bindings still reference the repository, `chainctl`
returns an error that names them, for example:

```text
Repository dev has 1 pull token (ci-dev). Delete them first or pass --force.
```

To delete the repository together with its pull tokens, policies, and policy
bindings, pass `--force`.

If someone deletes the repository's folder through IAM, `describe` shows the
state `folder missing` and tells you to run `chainctl libraries repos delete
NAME` to remove the repository.

## Policies and access

A JavaScript or Java repository can have its own
[policy](/chainguard/chainguard-repository/library-policies/), with its own
cooldown, allow list, and block list. A repository without its own policy
uses the organization's. The organization's block list and malware blocking
apply in every repository, and a repository's allow list can't override them.

To give the `prod` repository its own policy, create the policy in the
repository and enable it there:

```shell
chainctl libraries policy create --name=prod-policy --parent=example.com/prod --cooldown-days=3
chainctl libraries policy enable prod-policy --parent=example.com/prod --ecosystem=JAVA --mode=ENFORCE
```

You can enable a policy in a repository only after the organization has an
enforced policy for the same ecosystem.

An identity bound at a repository can pull packages only from that repository.
To manage repositories, an identity needs the following capabilities at the
organization:

| Action | Capability |
| --- | --- |
| Create a repository | `repositories.create` |
| Delete a repository | `repositories.delete` |
| Enable, disable, or reorder upstream registries | `repositories.update` |
| List or describe repositories | `repositories.list` |

Only the `owner` role has the three write capabilities. The `viewer` and
`editor` roles have `repositories.list` only.

## Not available in this beta

The following features aren't available in this beta:

* Repository URLs for Python, Go, and .NET.
* CUDA Python registries on repository URLs.
* Upstream registries that you add, or that need their own credentials.
* Repositories in the Chainguard Console.
