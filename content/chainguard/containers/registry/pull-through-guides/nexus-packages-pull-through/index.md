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
As of Nexus 3.96, the native Alpine repository type doesn't support Chainguard's package repositories. This guide describes a setup that uses raw proxy repositories instead.
{{< /note >}}

This tutorial demonstrates how to set up Alpine package (apk) pull-through caches with [Sonatype Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository) that front a [Chainguard private APK repository](/chainguard/containers/building-and-modifying/packages/private-apk-repos/) or the public Chainguard repositories. It also covers how to build a container image that installs packages through the resulting proxy.

## Prerequisites

To complete this tutorial, you need the following:

* Administrative privileges over a Sonatype Nexus Repository instance running **3.94 or later**. If you'd like to test this configuration, you can either download a trial from [Sonatype's website](https://www.sonatype.com/products/sonatype-nexus-oss-download) or run it as a [Docker container](https://github.com/sonatype/docker-nexus3).
* `chainctl` — Chainguard's command-line interface — installed on your local machine. Follow our guide on [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) to set this up.
* Administrative privileges within your Chainguard organization to create role-bindings (`role_bindings.create`); this capability is available to users with [the `owner` role](/platform/administration/iam-organizations/roles-role-bindings/capabilities-reference/#chainguard-role-capabilities).

## Private repository

[Chainguard private APK repositories](/chainguard/containers/building-and-modifying/packages/private-apk-repos/) hold packages that are exclusive to a specific Chainguard organization. They're served from `apk.cgr.dev/<organization>` and require a pull token for access.

Specific package versions should be immutable and can be cached indefinitely, whereas the upstream updates `APKINDEX.tar.gz` whenever it adds new packages. To give each artifact type its own caching properties, you'll create two raw proxy repositories (one for the packages, one for the `APKINDEX.tar.gz`) and a pair of routing rules that direct traffic to the correct proxy. Both proxies sit behind a raw group repository. Clients point `apk` at the group's URL.

You can name the repositories and rules whatever suits your organization; the examples in this guide use `chainguard-apk-*` throughout.

### Creating a pull token

The Nexus proxies need to authenticate to Chainguard to fetch packages from a private APK repository. Generate a pull token with `chainctl`:

```shell
chainctl auth pull-token --repository=apk
```

The `--repository=apk` flag binds the pull token identity to the `apk.pull` role, so it can download packages from your organization's private APK repository. This command returns output like the following:

```output
Creating new APK registry pull-token in example.org

To use this pull token in another environment, supply the following for Basic authorization:

Username: <identity_id>

Password: <pull_token>
```

Take note of the `Username` and `Password`. You'll need them when you set up the proxies.

### Creating the routing rules

The routing rules split incoming requests between the two proxies. They need to exist first, since each proxy references one by name.

Log in to Nexus as an administrator. Open **Settings** and select **Repository** ⇒ **Routing Rules**.

Click **Create Routing Rule** and enter the following details:

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

This proxy handles `.apk` requests. Because packages don't change, its cache never needs to expire.

From **Settings**, select **Repository** ⇒ **Repositories**. Click **Create repository** and select the **raw (proxy)** recipe. Enter the following details:

* **Name** — `chainguard-apk-packages`
* **Online** — Enabled.
* **Remote storage** — `https://apk.cgr.dev/<organization>`, replacing `<organization>` with your organization's name as it appears in the Chainguard Console.
* **Preserve encoded characters in URLs** — Enabled. `apk.cgr.dev` redirects `.apk` requests to a Cloudflare R2 presigned URL whose signature covers percent-encoded characters (`%2B`, `%2F`, `%3D`). Nexus's default URL normalization would decode them and break the signature.
* **Strict Content Type Validation** — Disabled. Nexus enables this setting on every new proxy, so you have to clear the checkbox. While it's on, Nexus compares each file it fetches against the content type implied by the file's extension and rejects anything that doesn't match. An Alpine package is a gzip archive, but Nexus maps the `.apk` extension to `application/vnd.android.package-archive`, so every package fails the check and clients receive a 404.
* **Maximum component age** — `-1` (never expire).
* **Routing Rule** — `chainguard-apk-block-index`.

In the **HTTP** section, select **Authentication**, choose the `Username` type, and enter the `Username` and `Password` from the pull token you generated earlier. Click **Create repository**.

### Creating the index proxy

This proxy handles `APKINDEX.tar.gz` requests. The upstream regenerates the index whenever it adds a package, so the cache TTL is short.

Repeat the process to create a second raw (proxy) repository with the following details:

* **Name** — `chainguard-apk-index`
* **Remote storage** — `https://apk.cgr.dev/<organization>`, replacing `<organization>` with your organization's name as it appears in the Chainguard Console.
* **Preserve encoded characters in URLs** — Enabled.
* **Strict Content Type Validation** — Leave this enabled. This proxy only ever serves `APKINDEX.tar.gz`, whose extension correctly implies gzip, so it passes the check that `.apk` files fail.
* **Maximum component age** — `15` (minutes). Tune higher to reduce origin fetches, or lower for faster visibility of new packages.
* **Routing Rule** — `chainguard-apk-only-index`.

Populate the **HTTP** authentication fields with the same pull token credentials, then click **Create repository**.

### Creating the group

The group combines both proxies behind a single URL. This is the URL that clients point `apk` at.

Return to **Repositories**, click **Create repository**, and select the **raw (group)** recipe. Enter the following details:

* **Name** — `chainguard-apk`.
* **Online** — Enabled.
* **Member repositories** — Add both `chainguard-apk-packages` and `chainguard-apk-index`. Order doesn't matter here. Nexus queries group members in sequence, but the routing rules make these two proxies mutually exclusive, so only one of them can ever answer a given request.

Click **Create repository**.

### Testing

Your group URL is `<nexus_url>/repository/chainguard-apk`, replacing `<nexus_url>` with the base URL of your Nexus instance, including the scheme (for example, `http://localhost:8081`).

Open a terminal and create a Dockerfile. The single quotes around `'EOF'` stop the shell from expanding `$` variables, so Docker interprets them as build arguments and secret references at build time:

```shell
cat > Dockerfile <<'EOF'
FROM cgr.dev/chainguard/python:latest-dev
USER root
ARG NEXUS_URL
RUN --mount=type=secret,id=http_auth,env=HTTP_AUTH,required=true \
    cp /etc/apk/repositories /etc/apk/repositories.disabled && \
    echo "${NEXUS_URL}/repository/chainguard-apk" > /etc/apk/repositories && \
    apk update && \
    apk add sed
USER nonroot
EOF
```

This Dockerfile uses the `python:latest-dev` image. You don't have to use this particular one, but because you're using `apk` to install a package from Nexus, pick a Chainguard container image that includes this package manager.

Not every package is available in every private APK repository. For example, your organization may not have access to the `sed` package. Refer to our [private APK repository documentation](/chainguard/containers/building-and-modifying/packages/private-apk-repos/#about-private-apk-repositories) for more details.

Before building, export your Nexus credentials and base URL. Include the scheme in `NEXUS_URL`, since the Dockerfile writes this value into `/etc/apk/repositories` as-is. For a Nexus instance running locally over plain HTTP, that's something like `http://localhost:8081`:

```shell
export NEXUS_USER=my-nexus-user
export NEXUS_PASSWORD=my-nexus-password
export NEXUS_URL=https://my-nexus-hostname:8081
export HTTP_AUTH="basic:*:${NEXUS_USER}:${NEXUS_PASSWORD}"
```

{{< note >}}
If your Nexus username is an email address, you must percent-encode the `@` sign, as in `export NEXUS_USER=linky%40example.com`.
{{< /note >}}

Then build the image, passing the credentials as Docker build secrets:

```shell
docker build \
  --secret id=http_auth,env=HTTP_AUTH \
  --build-arg NEXUS_URL=$NEXUS_URL \
  -t nexus-apk-build .
```

The build output confirms the `sed` installation:

```output
. . .
 => [4/4] RUN apk update && apk add sed                                                   3.1s
. . .
```

To confirm Nexus cached the package, open **Browse** in the left-hand navigation menu, select `chainguard-apk-packages`, and expand the architecture directory (for example, `x86_64`). The cached package appears there.

## Public repositories

You also have access to the public `chainguard` and `extra-packages` repositories. The same setup works for these, with two differences: there's no authentication, and the remote URL uses `virtualapk.cgr.dev` instead of `apk.cgr.dev`.

For each public repository you want to cache, follow the [private repository procedure](#private-repository) with the following adjustments:

* Reuse the `chainguard-apk-block-index` and `chainguard-apk-only-index` routing rules from earlier. They match on request paths and aren't tied to a specific upstream.
* Name the repositories after the upstream. For example, use `chainguard-apk-public-packages`, `chainguard-apk-public-index`, and `chainguard-apk-public` for the `chainguard` repository, and the matching `chainguard-apk-extras-*` names for `extra-packages`.
* Set **Remote storage** on each proxy to `https://virtualapk.cgr.dev/<organization_id>/chainguard` or `https://virtualapk.cgr.dev/<organization_id>/extra-packages`, replacing `<organization_id>` with your Chainguard organization's UID. Run `chainctl iam organizations list -o table` to find it, or check the **Settings** ⇒ **General** page in the [Chainguard Console](https://console.chainguard.dev).
* Disable **Strict Content Type Validation** on each packages proxy, as in the private setup. The public repositories serve the same gzip `.apk` files, so they fail the same content type check.
* Leave the **HTTP** authentication section unchecked. The public repositories don't require authentication.

To pull from the public repositories in a container build, add their group URLs to `/etc/apk/repositories` alongside (or in place of) the private one. Since there's no authentication, you don't need to embed credentials in the URLs:

```shell
echo "${NEXUS_URL}/repository/chainguard-apk-public" >> /etc/apk/repositories
echo "${NEXUS_URL}/repository/chainguard-apk-extras" >> /etc/apk/repositories
```

## Debugging

If you run into issues pulling from Chainguard's package repositories through Nexus, check for these common pitfalls:

* If `apk add` returns `package mentioned in index not found` or a 404 right after the index fetches successfully, the packages proxy is fetching the index but failing to serve the package itself. Two settings can cause this.
    * Check **Strict Content Type Validation** on the packages proxy first, since Nexus enables it by default: while it's on, Nexus rejects every Alpine package as a content type mismatch and records an `InvalidContentException` in its log, naming the detected type (`application/gzip`) and the expected one (`application/vnd.android.package-archive`).
    * If **Strict Content Type Validation** is already off and the same error persists, Nexus may be normalizing the R2 presigned URL. Check that **Preserve encoded characters in URLs** is enabled on both proxies. When this setting is off, Nexus decodes `%2B`/`%2F`/`%3D` in the redirect target's query string, which invalidates R2's SigV4 signature and returns a 404.
* If both proxies return `403` for every request, you've probably swapped the routing rules attached to each proxy. The packages proxy should have the `BLOCK` rule attached; the index proxy should have the `ALLOW` rule.
* If `apk update` returns `401` from Nexus itself (not the upstream), `apk` isn't sending credentials that Nexus accepts. Set the `HTTP_AUTH` environment variable as the testing section does, embed the credentials in the repository URL instead, or configure the `nx-anonymous` role to grant read on the group repository. Nexus requires its own credentials unless your instance has anonymous access enabled, so this applies to the public repositories too, even though their upstreams need no authentication.
* If `apk update` returns `401` from the upstream via Nexus, the pull token attached to the proxies has expired. Regenerate one with `chainctl auth pull-token --repository=apk` and update the HTTP authentication settings on both proxies.
* Check that your environment meets all [network requirements](/chainguard/containers/registry/network-requirements/), and that Nexus can reach both `apk.cgr.dev` and `*.r2.cloudflarestorage.com`.
* You may have misconfigured a repository. Delete and recreate the affected proxy or group to test with a clean setup.

## Terraform

If you would prefer to deploy this setup with Terraform, the [`nexus-apk-proxy`](https://github.com/chainguard-demo/cookbook/tree/main/terraform-modules/nexus-apk-proxy) module in the Chainguard [cookbook](https://github.com/chainguard-demo/cookbook) repository provides an example of creating a proxy group in the same configuration described by this guide.

## Learn more

If you haven't already done so, you may find it useful to read through our [Registry overview](/chainguard/containers/registry/overview/) to learn more about Chainguard's registry. You can also learn more about Chainguard Containers by referring to our [documentation](/chainguard/containers/overview/), and learn more about working with the Chainguard platform by reviewing our [Administration documentation](/platform/administration/). For a walkthrough of how to set up Nexus as a pull-through cache for Chainguard Containers, refer to [our Nexus containers guide](/chainguard/containers/registry/pull-through-guides/nexus-pull-through/). If you'd like to learn more about Sonatype Nexus, we encourage you to refer to the [official Nexus documentation](https://help.sonatype.com/en/sonatype-nexus-repository.html).
