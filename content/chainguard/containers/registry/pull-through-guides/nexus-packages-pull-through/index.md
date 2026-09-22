---
title: "How to pull packages from Chainguard package repositories through Nexus"
linktitle: "Nexus — packages"
type: "article"
description: "Tutorial for setting up Sonatype Nexus raw repositories as pull-through caches for apk packages from Chainguard's package repositories."
date: 2026-09-17T00:00:00+00:00
lastmod: 2026-09-17T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
menu:
  docs:
    parent: "pull-through-guides"
toc: true
weight: 080
---

{{< note >}}
At the time of writing (2026-09-17) the native Alpine repository type in Nexus doesn't support Chainguard's package repositories. This guide describes a setup that uses raw proxy repositories instead.
{{< /note >}}

This tutorial shows how to set up Alpine package (apk) pull-through caches with [Sonatype Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository) that front a [Chainguard private APK repository](/chainguard/containers/building-and-modifying/packages/private-apk-repos/) or the public Chainguard repositories. It also covers how to build a container image that installs packages through the resulting proxy.

## Prerequisites

In order to complete this tutorial, you need the following:

* Administrative privileges over a Sonatype Nexus Repository instance running **3.94 or later**. If you'd like to test this configuration, you can either download a trial from [Sonatype's website](https://www.sonatype.com/products/sonatype-nexus-oss-download) or run it as a [Docker container](https://github.com/sonatype/docker-nexus3).
* [`chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/)
* Administrative privileges within your Chainguard organization to create role-bindings (`role_bindings.create`); this capability is available to users with [the `owner` role](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/#chainguard-role-capabilities).

## Private repository

[Chainguard private APK repositories](/chainguard/containers/building-and-modifying/packages/private-apk-repos/) hold packages that are exclusive to a specific Chainguard organization. They're served from `apk.cgr.dev/<organization>` and require a pull token for access.

Specific package versions should be immutable and can be cached indefinitely, whereas the `APKINDEX.tar.gz` is updated as new packages are added upstream. To give each artifact type its own caching properties, you'll create two raw proxy repositories (one for the packages, one for the `APKINDEX.tar.gz`) and a pair of routing rules that direct traffic to the correct proxy. Both proxies sit behind a raw group repository. Clients point `apk` at the group's URL.

You can name the repositories and rules whatever suits your organization; the examples below use `chainguard-apk-*` throughout.

### Creating a pull token

The Nexus proxies need to authenticate to Chainguard to fetch packages from a private APK repository. Generate a pull token with `chainctl`:

```shell
chainctl auth pull-token --repository=apk
```

The `--repository=apk` flag binds the pull token identity to the `apk.pull` role, so it can download packages from your organization's private APK repository. The output looks like this:

```output
Creating new APK registry pull-token in example.org

To use this pull token in another environment, supply the following for Basic authorization:

Username: <identity-id>

Password: <pull-token>
```

Take note of the `Username` and `Password`. You'll need them when setting up the proxies below.

### Creating the routing rules

The routing rules will split incoming requests between the two proxies. They need to exist first, since each proxy references one by name.

Log in to Nexus as an administrator. Open **Settings** and select **Repository** ⇒ **Routing Rules**.

Click the **Create Routing Rule** button and enter the following details:

* **Name** — `chainguard-apk-block-index`
* **Description** — `Block APKINDEX.tar.gz paths from the packages proxy.`
* **Mode** — `Block`
* **Matchers** — `.*APKINDEX\.tar\.gz`

Click **Create Routing Rule** to save. Then repeat the process for the second rule:

* **Name** — `chainguard-apk-only-index`
* **Description** — `Restrict the index proxy to APKINDEX.tar.gz paths only.`
* **Mode** — `Allow`
* **Matchers** — `.*APKINDEX\.tar\.gz`

### Creating the packages proxy

This proxy handles `.apk` requests. Because packages won't change, its cache never needs to expire.

From **Settings**, select **Repository** ⇒ **Repositories**, click the **Create repository** button, and select the **raw (proxy)** recipe. Enter the following details:

* **Name** — `chainguard-apk-packages`
* **Online** — Enabled.
* **Remote storage** — `https://apk.cgr.dev/<organization>`, replacing `<organization>` with your organization's name as it appears in the Chainguard Console.
* **Preserve encoded characters in URLs** — Enabled. `apk.cgr.dev` redirects `.apk` requests to a Cloudflare R2 presigned URL whose signature covers percent-encoded characters (`%2B`, `%2F`, `%3D`). Nexus's default URL normalization would decode them and break the signature.
* **Maximum component age** — `-1` (never expire).
* **Routing Rule** — `chainguard-apk-block-index`.

In the **HTTP** section, check **Authentication**, select the `Username` type, and enter the `Username` and `Password` from the pull token you generated earlier. Click **Create repository**.

### Creating the index proxy

This proxy handles `APKINDEX.tar.gz` requests. The upstream regenerates the index whenever a package is added, so the cache TTL is short.

Repeat the process to create a second raw (proxy) repository with the following details:

* **Name** — `chainguard-apk-index`
* **Remote storage** — Same as the packages proxy.
* **Preserve encoded characters in URLs** — Enabled.
* **Maximum component age** — `15` (minutes). Tune higher to reduce origin fetches, or lower for faster visibility of new packages.
* **Routing Rule** — `chainguard-apk-only-index`.

Populate the **HTTP** authentication fields with the same pull token credentials, then click **Create repository**.

### Creating the group

The group combines both proxies behind a single URL. This is the URL that clients point `apk` at.

Return to **Repositories**, click **Create repository**, and select the **raw (group)** recipe. Enter the following details:

* **Name** — `chainguard-apk`.
* **Online** — Enabled.
* **Member repositories** — Add `chainguard-apk-packages` first, then `chainguard-apk-index`.

Click **Create repository**.

### Testing

Your group URL is `<Nexus URL>/repository/chainguard-apk`, replacing `<Nexus URL>` with the hostname and port of your Nexus instance (e.g. `http://localhost:8081`).

Open a terminal and create a Dockerfile. The single quotes around `'EOF'` stop the shell from expanding `$` variables, so Docker sees them as build arguments and secret references at build time:

```shell
cat > Dockerfile <<'EOF'
FROM cgr.dev/chainguard/python:latest-dev
USER root
ARG NEXUS_URL
RUN --mount=type=secret,id=http_auth,env=HTTP_AUTH,required=true \
    cp /etc/apk/repositories /etc/apk/repositories.disabled && \
    echo "https://${NEXUS_URL}/repository/chainguard-apk" > /etc/apk/repositories && \
    apk update && \
    apk add sed
USER nonroot
EOF
```

This Dockerfile uses the `python:latest-dev` image. You don't have to use this particular image, but because we're using `apk` to install a package from Nexus, you should use a Chainguard container image that has this package manager available.

Not every package is available in every private APK repository. For example, your organization may not have access to the `sed` package. See our [private APK repository documentation](/chainguard/containers/building-and-modifying/packages/private-apk-repos/#about-private-apk-repositories) for more details.

Before building, export your Nexus credentials and hostname. If Nexus is running locally, `NEXUS_URL` will be something like `localhost:8081`:

```shell
export NEXUS_USER=my-nexus-user
export NEXUS_PASSWORD=my-nexus-password
export NEXUS_URL=my-nexus-hostname:8081
export HTTP_AUTH="basic:*:${NEXUS_USER}:${NEXUS_PASSWORD}"
```

> **Note**: If your Nexus username is an email address, you must percent-encode the `@` sign, as in `export NEXUS_USER=linky%40example.com`.

Then build the image, passing the credentials as Docker build secrets:

```shell
docker build \
  --secret id=http_auth,env=HTTP_AUTH \
  --build-arg NEXUS_URL=$NEXUS_URL \
  -t nexus-apk-build .
```

The build output shows `sed` being installed:

```output
. . .
 => [4/4] RUN apk update && apk add sed                                                   3.1s
. . .
```

To confirm Nexus cached the package, open **Browse** in the left-hand navigation menu, select `chainguard-apk-packages`, and expand the architecture directory (e.g. `x86_64`). The cached package will be listed there.

## Public repositories

You also have access to the public `chainguard` and `extra-packages` repositories. The same setup works for these, with two differences: there's no authentication and the remote URL uses `virtualapk.cgr.dev` instead of `apk.cgr.dev`.

For each public repository you want to cache, follow the [private repository procedure](#private-repository) with the following adjustments:

* Reuse the `chainguard-apk-block-index` and `chainguard-apk-only-index` routing rules from earlier. They match on request paths and aren't tied to a specific upstream.
* Name the repositories after the upstream, for example `chainguard-apk-public-packages`, `chainguard-apk-public-index`, and `chainguard-apk-public` for the `chainguard` repository (and likewise `chainguard-apk-extras-*` for `extra-packages`).
* Set **Remote storage** on each proxy to `https://virtualapk.cgr.dev/<ORGANIZATION-ID>/chainguard` or `https://virtualapk.cgr.dev/<ORGANIZATION-ID>/extra-packages`, replacing `<ORGANIZATION-ID>` with your Chainguard organization's UID. Run `chainctl iam organizations list -o table` to find it, or check the **Settings** ⇒ **General** page in the [Chainguard Console](https://console.chainguard.dev).
* Leave the **HTTP** authentication section unchecked. The public repositories don't require authentication.

To pull from the public repositories in a container build, add their group URLs to `/etc/apk/repositories` alongside (or in place of) the private one. Since there's no authentication, no credentials need to be embedded in the URLs:

```shell
echo "${NEXUS_URL}/repository/chainguard-apk-public" >> /etc/apk/repositories
echo "${NEXUS_URL}/repository/chainguard-apk-extras" >> /etc/apk/repositories
```

## Debugging

If you run into issues when trying to pull from Chainguard's package repositories through Nexus, you can try checking for these common pitfalls:

* If `apk add` returns `package mentioned in index not found` or a 404 right after the index fetches successfully, Nexus is normalizing the R2 presigned URL. Check that **Preserve encoded characters in URLs** is enabled on both proxies. When this setting is off, Nexus decodes `%2B`/`%2F`/`%3D` in the redirect target's query string, which invalidates R2's SigV4 signature and returns a 404.
* If both proxies return `403` for every request, the routing rules attached to each proxy have probably been swapped. The packages proxy should have the `BLOCK` rule attached; the index proxy should have the `ALLOW` rule.
* If `apk update` returns `401` from Nexus itself (not the upstream), embed the Nexus credentials in the repository URL as shown in the testing section, or configure the `nx-anonymous` role to grant read on the group repository. `apk-tools` doesn't send HTTP basic auth against a repository URL without embedded credentials.
* If `apk update` returns `401` from the upstream via Nexus, the pull token attached to the proxies has expired. Regenerate one with `chainctl auth pull-token --repository=apk` and update the HTTP authentication settings on both proxies.
* Check that all [network requirements](/chainguard/containers/registry/network-requirements/) are met, and that Nexus can reach both `apk.cgr.dev` and `*.r2.cloudflarestorage.com`.
* A repository may have been misconfigured. Delete and recreate the affected proxy or group to test with a clean setup.

## Learn more

If you haven't already done so, you may find it useful to review our [Registry overview](/chainguard/chainguard-registry/overview/) to learn more about Chainguard's registry. You can also learn more about Chainguard Containers by referring to our [documentation](/chainguard/containers/overview/), and learn more about working with the Chainguard platform by reviewing our [Administration documentation](/chainguard/administration/). For a walkthrough of how to set up Nexus as a pull-through cache for Chainguard Containers, refer to [our Nexus containers guide](/chainguard/containers/registry/pull-through-guides/nexus-pull-through/). If you'd like to learn more about Sonatype Nexus, we encourage you to refer to the [official Nexus documentation](https://help.sonatype.com/en/sonatype-nexus-repository.html).
