---
title: "Using Dependabot with Chainguard Containers"
linktitle: "Using Dependabot"
aliases:
- /chainguard/containers/staying-secure/updating-images/dependabot/
- /chainguard/containers/staying-secure/updating-containers/dependabot/
type: "article"
description: "How to configure Dependabot to authenticate to your private cgr.dev registry and open pull requests that update Chainguard Containers"
date: 2026-09-03T00:00:00+00:00
lastmod: 2026-09-04T16:13:45+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
weight: 050
toc: true
---

[Dependabot](https://docs.github.com/en/code-security/dependabot) is GitHub's dependency update tool. It reads the container image references in your Dockerfiles and Kubernetes manifests, checks the registry for newer tags, and opens pull requests to update them.

This guide explains how to configure Dependabot to authenticate to your organization's private registry at `cgr.dev` so it can keep your references to Chainguard Containers current.

## Choosing between Dependabot and Digestabot

Dependabot and [Digestabot](/chainguard/containers/security-and-compliance/updating-containers/digestabot/) solve different halves of the same problem, and many teams run both:

* **Dependabot** opens a pull request when a newer *tag* is available — for example, moving a reference from `go:1.22` to `go:1.26`. Use it to move between version streams.
* **Digestabot** opens a pull request when the *digest* behind a fixed tag changes. Chainguard rebuilds container images daily, so the digest behind a tag such as `latest` or `3.14` changes often. Use Digestabot to pick up those rebuilds.

Dependabot acts on the tag string in your reference. If you pin to a mutable tag and never change that string, Dependabot has nothing to update, and Digestabot is the better fit.

## Prerequisites

To follow this guide, you need:

* A GitHub repository containing at least one reference to a Chainguard container image.
* Access to a Chainguard organization, with permission to create pull tokens.
* `chainctl` installed on your local machine. Refer to [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) if you haven't set this up.

## Create a pull token

Dependabot authenticates to private container registries with a static username and password. It doesn't support [Chainguard assumable identities](/platform/administration/assumable-ids/assumable-ids/), so you need to create a [pull token](/chainguard/containers/registry/authenticating/#authenticating-with-a-pull-token).

Create one with `chainctl`:

```shell
chainctl auth configure-docker --pull-token --ttl 2160h
```

This command responds with output such as the following:

```shell
To use this pull token in another environment, run this command:

    docker login "cgr.dev" --username "<identity-id>" --password "<pull-token>"
```

The username has the form `<organization ID>/<pull token ID>`. Record both values; you'll store them as secrets in the next section.

The `--ttl` flag sets how long the token stays valid. The example uses `2160h`, or 90 days. The default is `720h` (30 days) and the maximum is `8760h` (one year). Dependabot's authentication fails once the token expires, so choose a lifetime you can commit to rotating, and set a reminder to replace the token before it lapses.

One pull token can serve every repository in your GitHub organization. Storing it as an organization-level secret, rather than creating a token for each repository, leaves you with a single credential to rotate.

## Store the credentials as Dependabot secrets

GitHub keeps Dependabot secrets in a separate store from Actions secrets. A token added to Actions secrets is invisible to Dependabot, and the update job fails to authenticate without a clear explanation.

To add the secrets to a single repository:

1. In your repository on GitHub, go to **Settings > Secrets and variables > Dependabot**.
2. Select **New repository secret**.
3. Name the secret `CHAINGUARD_PULL_TOKEN_USERNAME` and enter the username from the previous section.
4. Select **Add secret**.
5. Repeat these steps to create `CHAINGUARD_PULL_TOKEN_PASSWORD` with the password value.

To share one token across every repository in your GitHub organization, add the secrets at **Settings > Secrets and variables > Dependabot** in the organization's settings instead, and grant access to the repositories that need them.

## Configure Dependabot

Create a file named `.github/dependabot.yml` at the root of your repository with the following content:

```yaml
version: 2

registries:
  chainguard:
    type: docker-registry
    url: cgr.dev
    username: ${{secrets.CHAINGUARD_PULL_TOKEN_USERNAME}}
    password: ${{secrets.CHAINGUARD_PULL_TOKEN_PASSWORD}}
    replaces-base: true

updates:
  - package-ecosystem: "docker"
    directory: "/"
    registries:
      - chainguard
    schedule:
      interval: "daily"
```

This configuration defines a registry named `chainguard`, points it at `cgr.dev`, and authenticates with the secrets you created. The `updates` section tells Dependabot to check the Dockerfiles in the repository root once a day, using that registry.

Adjust `directory` to match where your manifests live, and `interval` to match how often you want pull requests. Refer to GitHub's [Dependabot options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference) for the full set of options.

Commit this file to your repository's default branch.

### Understanding `replaces-base`

Setting `replaces-base: true` tells Dependabot to resolve container image references against `cgr.dev` instead of Docker Hub, the default registry for the Docker ecosystem.

This setting doesn't affect fully qualified references such as `cgr.dev/example.com/go:1.22`, which Dependabot matches by hostname either way. It changes how Dependabot resolves *unqualified* references such as `FROM python:3.13`, which it sends to `cgr.dev` rather than Docker Hub.

Keep `replaces-base: true` when every container image in the repository comes from Chainguard. If the repository also pulls images from other registries, omit the setting so Dependabot resolves each reference against the registry that hosts it:

```yaml
registries:
  chainguard:
    type: docker-registry
    url: cgr.dev
    username: ${{secrets.CHAINGUARD_PULL_TOKEN_USERNAME}}
    password: ${{secrets.CHAINGUARD_PULL_TOKEN_PASSWORD}}
```

{{< alert context="warning" >}}
Omitting `replaces-base` keeps Dependabot working across a mix of registries, but the images it resolves elsewhere remain outside Chainguard's hardening and rebuild process. Container images from other registries are not covered by [Chainguard's CVE SLA](https://www.chainguard.dev/legal/cve-policy). Where a Chainguard equivalent exists, replacing those references and keeping `replaces-base: true` gives you broader coverage.
{{< /alert >}}

## Verify the configuration

Dependabot runs on the schedule you set, but you can trigger a run immediately to confirm that authentication works:

1. In your repository on GitHub, go to **Insights > Dependency graph > Dependabot**.
2. Find the entry for the `docker` ecosystem.
3. Select **Check for updates**.

Select **Last checked** to open the job log. A successful run lists the tags Dependabot found for each image, then opens a pull request for any reference it can update, with a title such as `Bump example.com/go from 1.22 to 1.26`.

## Update digest-pinned references

Chainguard recommends pinning image references to a [digest](/chainguard/containers/troubleshooting/container-image-digests/) while keeping the tag as a version hint, in the form `cgr.dev/example.com/go:1.22@sha256:...`. Dependabot updates both parts of a reference that's already in this form, as described in [Unique tags](/chainguard/containers/reference/unique-tags/).

Two limits are worth knowing before you rely on this:

* Dependabot updates a digest that's already present, but it won't add one to a reference that has only a tag. Pin the digest yourself the first time. Adding digests automatically is an [open feature request](https://github.com/dependabot/dependabot-core/issues/14065).
* When a reference carries both a tag and a digest, Dependabot [doesn't supersede an open pull request](https://github.com/dependabot/dependabot-core/issues/7387) as newer digests are published. Because Chainguard rebuilds container images daily, use Digestabot for references pinned to a fixed tag.

## Limitations

* **Assumable identities aren't supported.** Dependabot's OIDC authentication covers a fixed set of registries that doesn't include Chainguard, so a pull token is the only option. Refer to GitHub's documentation on [configuring access to private registries](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-access-to-private-registries) for the current list.
* **GitHub-hosted Dependabot only.** Chainguard tests this configuration against Dependabot as hosted by GitHub. Self-hosted and third-party runners may handle credentials differently.

## Troubleshooting

### Authentication fails with `private_source_authentication_failure`

This error means Dependabot reached `cgr.dev` but couldn't authenticate. Check the following, in order:

1. Confirm the secrets are stored under **Dependabot**, not **Actions**. This is the most common cause.
2. Confirm the pull token is still valid. Run `chainctl auth pull-token list` to see the tokens in your organization and when they expire.
3. Confirm the username is the complete `<organization ID>/<pull token ID>` string, including the slash.
4. Test the credentials outside of Dependabot with `docker login cgr.dev --username <identity-id> --password <pull-token>`, followed by a `docker pull` of one of the images in your repository.

### No pull requests appear

If the job log shows a successful run but no pull requests, check the following:

* Dependabot acts on the tag string. A reference pinned to a mutable tag such as `latest` produces no pull requests, because the tag never changes. Use Digestabot for those references.
* Dependabot opens at most five pull requests per ecosystem by default. Raise the `open-pull-requests-limit` option if existing pull requests are holding the queue.
* Unqualified references such as `FROM python:3.13` reach `cgr.dev` only when `replaces-base: true` is set. Otherwise, fully qualify the reference.

## Learn more

* [Using Renovate with Chainguard Containers](/chainguard/containers/security-and-compliance/updating-containers/renovate/) covers the equivalent setup for teams outside GitHub, or teams that want short-lived credentials through an assumable identity.
* [Strategies and tooling for updating containers](/chainguard/containers/security-and-compliance/updating-containers/strategies-tools-updating-images/) compares the wider range of update tools.
* [Authenticating to the Chainguard registry](/chainguard/containers/registry/authenticating/) documents pull tokens and the other authentication options in full.
