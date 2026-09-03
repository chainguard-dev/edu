---
title: "Using Digestabot with Chainguard Containers"
linktitle: "Using Digestabot"
aliases:
- /chainguard/chainguard-images/videos/digestabot/
- /chainguard/chainguard-images/troubleshooting/updating-images/digestabot/
- /chainguard/chainguard-images/staying-secure/updating-images/digestabot/
- /chainguard/containers/videos/digestabot/
- /chainguard/containers/troubleshooting/updating-images/digestabot/
- /chainguard/containers/staying-secure/updating-images/digestabot/
type: "article"
description: "How to configure Digestabot to keep digest-pinned references to Chainguard Containers current, including authenticating to a private cgr.dev registry"
date: 2024-02-07T15:21:01+00:00
lastmod: 2026-09-03T00:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 21
toc: true
---

[Digestabot](https://github.com/chainguard-dev/digestabot) is a GitHub Action that keeps digest-pinned container image references current. It reads the references in your repository, looks up the current digest for each tag in the registry, and opens a pull request when a digest has changed.

Chainguard rebuilds container images daily, so the digest behind a tag such as `latest` or `3.14` changes often. Digestabot lets you pin a reference to an exact digest for reproducibility and still pick up each rebuild, with a pull request as the place to test the change before it ships.

This guide explains how Digestabot matches references, how to authenticate it to your organization's private registry at `cgr.dev`, and how to control which files it scans.

## Choosing between Digestabot, Dependabot, and Renovate

These three tools solve different parts of the same problem:

* **Digestabot** opens a pull request when the digest behind a fixed tag changes. Use it to pick up Chainguard's daily rebuilds without changing the tag you depend on.
* **[Dependabot](/chainguard/containers/staying-secure/updating-images/dependabot/)** opens a pull request when a newer *tag* is available, moving a reference from `go:1.22` to `go:1.26`. Use it to move between version streams.
* **[Renovate](/chainguard/containers/staying-secure/updating-images/renovate/)** does both, and it runs outside GitHub as well as inside it.

Many teams run Digestabot alongside one of the others: Dependabot or Renovate moves the tag when a new version stream appears, and Digestabot keeps the digest current in between. Digestabot is also the better fit for a reference pinned to a mutable tag, where the tag string never changes and Dependabot has nothing to act on.

## How Digestabot matches references

Digestabot updates a reference only when it contains both a tag and a digest:

```
cgr.dev/example.com/go:1.22@sha256:0d0e0f5e9b7f8ee0dbcbb6d1c40ad1bbd0da5b2bb56de2b26dfd8ceb8ed69dbb
```

Both parts are required:

* Digestabot never matches a reference with a tag and no digest. It updates a digest that's already there; it doesn't add one.
* Digestabot skips a reference with a digest and no tag, because it has no tag to look up. The job log records `Image <name> in file <file> does not have a tag, ignoring...`.

This is the most common reason a Digestabot run reports nothing to do.

To add digests to references that carry only a tag, use [Frizbee](https://github.com/stacklok/frizbee), as shown in [Reproducible Dockerfiles with Frizbee and Digestabot](/chainguard/containers/how-to-use/digestabot_frizbee/). Renovate's `pinDigests` option does the same job; refer to [Pin digests](/chainguard/containers/staying-secure/updating-images/renovate/#pin-digests).

Digestabot also skips two categories of reference regardless of their form:

* Any reference in a file whose path contains `testdata`.
* Any reference whose registry address contains `.local:`, such as `registry.local:5000/example`.

## Prerequisites

To follow this guide, you need:

* A GitHub repository with at least one reference to a Chainguard container image pinned in the `tag@digest` form described in the previous section.
* Access to a Chainguard organization, with permission to create identities, if the images come from a private repository in `cgr.dev`.
* `chainctl` installed on your local machine. Refer to [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) if you haven't set this up.

Digestabot opens its pull requests with the workflow's `GITHUB_TOKEN`. For that to work, go to **Settings > Actions > General** in your repository and confirm that **Allow GitHub Actions to create and approve pull requests** is selected. If your organization turns this setting off, pass a token from a GitHub App or a `repo`-scoped personal access token through the `token` input instead.

## Authenticate to a private registry

Digestabot reads digests with [crane](https://github.com/google/go-containerregistry), which uses the Docker credential store on the runner. Digestabot has no registry credential input of its own, so it inherits whatever credentials an earlier step configured.

For a private repository in `cgr.dev`, add a [`setup-chainctl`](https://github.com/chainguard-dev/setup-chainctl) step before the Digestabot step. That action authenticates as a [Chainguard assumable identity](/platform/administration/assumable-ids/assumable-ids/) and registers a Docker credential helper for `cgr.dev`, which crane then uses without further configuration.

Digestabot needs no static pull token, which is where it differs most from Dependabot. The identity mints a short-lived token for each run, so there is no credential to store or rotate.

Create an identity for your repository. The `--github-repo` value embeds GitHub's immutable numeric owner and repository IDs; refer to [Finding your repository's numeric identifiers](/platform/administration/assumable-ids/identity-examples/github-identity/#finding-your-repositorys-numeric-identifiers) for how to retrieve them and when the format applies.

```shell
chainctl iam identities create github digestabot \
  --github-repo=<github-org>@<owner-id>/<github-repo-name>@<repo-id> \
  --github-ref=refs/heads/main \
  --role=registry.pull
```

The command returns an identity ID. Record it for the workflow in the next section.

Digestabot only reads image digests, so the `registry.pull` role covers everything it does on its own. [Annotating pull requests with `chainctl images diff`](#annotate-pull-requests-with-chainctl-images-diff) needs a broader role.

## Create the workflow

Create a file named `.github/workflows/digestabot.yaml` with the following content, replacing `<identity-id>` with the ID from the previous section:

```yaml
name: Digestabot

on:
  workflow_dispatch:
  schedule:
    - cron: "0 1 * * *"

permissions:
  contents: read

jobs:
  digestabot:
    name: Digestabot
    runs-on: ubuntu-latest

    permissions:
      contents: write      # Push the branch holding the digest updates
      pull-requests: write # Open the pull request
      id-token: write      # Assume the Chainguard identity and sign commits

    steps:
    - uses: step-security/harden-runner@e14015d583714f6e62063499dc959a02595150a1 # v2.21.1
      with:
        egress-policy: audit

    - uses: chainguard-dev/setup-chainctl@2cddd35a2f120d9973e58094dc6878c93cf58c28 # v0.5.1
      with:
        identity: "<identity-id>"

    - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1

    - uses: chainguard-dev/digestabot@33d0b78e580aa0c83fe188eb3dfad6611b662479 # v1.3.2
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        labels-for-pr: ''
```

Commit this file to your repository's default branch.

This workflow runs at 1:00 a.m. every day and on demand from **Actions > Digestabot > Run workflow**. Each run authenticates to `cgr.dev` as the identity you created, scans the repository, and opens a pull request titled `Update images digests` on a branch named `update-digests` if any digest has changed.

The example clears `labels-for-pr`, because the default value applies Chainguard's own repository labels — `automated pr`, `kind/cleanup`, and `release-note-none` — which probably don't exist in your repository. Set it to labels you use, or leave it empty.

If your images come from a public repository such as `cgr.dev/chainguard`, drop the `setup-chainctl` step. Digestabot reads public digests without credentials.

### How Digestabot handles repeat runs

Digestabot maintains one pull request rather than opening a new one per run. Each run resets the `update-digests` branch to the base branch, applies the current set of updates, and force-pushes, so an open pull request always reflects the latest digests. If you merge or close that pull request, the next run with pending updates opens a fresh one.

This is worth knowing if you also use Dependabot, which [leaves an open pull request in place](/chainguard/containers/staying-secure/updating-images/dependabot/#update-digest-pinned-references) as newer digests are published.

### Commit signing

Digestabot signs its commits with [gitsign](https://github.com/sigstore/gitsign) by default, which is why the job needs the `id-token: write` permission. GitHub labels these commits as unverified. Refer to [Digestabot's commits show as unverified](#digestabots-commits-show-as-unverified) if a branch protection rule in your repository requires signed commits.

## Choose which files to scan

By default, Digestabot scans files matching `*.yaml`, `*.yml`, `Dockerfile*`, `Makefile*`, `*.sh`, `*.tf`, and `*.tfvars`. It updates digests in Terraform configurations, Makefiles, shell scripts, `ko` configurations, and Kubernetes manifests, not only in Dockerfiles. Any file in the repository that holds a `tag@digest` reference and matches one of these patterns is in scope.

Patterns match file names rather than paths. Digestabot passes each pattern to `find -name`, which compares against the base name of each file, so a pattern such as `manifests/*.yaml` matches nothing. To narrow Digestabot to part of a repository, set `working-dir` to a path relative to the repository root:

```yaml
    - uses: chainguard-dev/digestabot@33d0b78e580aa0c83fe188eb3dfad6611b662479 # v1.3.2
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        working-dir: manifests
        include-files: '*.yaml,Dockerfile*'
```

## Resolve digests through a registry proxy

If you pull Chainguard Containers through a registry proxy, such as a remote repository in Artifact Registry, the proxy can return a stale digest for a tag. The `registry-map` input maps a proxy prefix to the registry behind it, so Digestabot resolves digests against `cgr.dev` while leaving the proxy address in your files:

```yaml
    - uses: chainguard-dev/digestabot@33d0b78e580aa0c83fe188eb3dfad6611b662479 # v1.3.2
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        registry-map: 'us-docker.pkg.dev/my-project/cgr/=cgr.dev/'
```

Provide mappings as comma-separated `proxy=upstream` pairs. Digestabot rewrites the address it looks up, not the reference it writes back, so your files keep pulling through the proxy.

Because the lookups go to `cgr.dev`, the credentials on the runner must grant access there. Keep the `setup-chainctl` step in the workflow even when every reference in your files points at the proxy.

## Extend Digestabot with its outputs

Digestabot reports what it changed in two outputs: `json` describes each update, and `changed_files` lists the files it modified. Combined with `create-pr: false`, which applies the changes in the workspace without opening a pull request, these let you act on an update before it reaches a reviewer:

```yaml
    - uses: chainguard-dev/digestabot@33d0b78e580aa0c83fe188eb3dfad6611b662479 # v1.3.2
      id: digestabot
      with:
        token: ${{ secrets.GITHUB_TOKEN }}

    - shell: bash
      run: |
        while read -r update; do
          updated_image=$(jq -r '.image + "@" + .updated_digest' <<<"${update}")

          echo "Do something with ${updated_image} here."
        done < <(jq -c '.updates // [] | .[]' <<<'${{ steps.digestabot.outputs.json }}')
```

### Annotate pull requests with `chainctl images diff`

[`chainctl images diff`](/platform/chainctl-usage/comparing-images/) compares two container images and reports the packages and vulnerabilities that differ between them. Running it over Digestabot's `json` output turns "test the update before merging" into a summary in the pull request itself: which vulnerabilities the rebuild resolves, which packages changed, and whether the update is worth merging at all.

The [`digestabot-examples`](https://github.com/chainguard-demo/digestabot-examples) repository holds a complete workflow for this in `.github/workflows/chainctl-image-diff.yaml`. It runs Digestabot with `create-pr: false`, verifies that each image is signed by Chainguard, diffs the old and new digests, and discards updates that resolve no vulnerabilities. The same repository has a second workflow that scans each updated image with [Grype](https://github.com/anchore/grype) and comments the results on the pull request.

`chainctl images diff` needs `grype` available on the runner and an identity with a broader role than `registry.pull`; the example workflow uses `viewer`.

## Configuration reference

### Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `working-dir` | Directory to scan, relative to the repository root. | `.` |
| `include-files` | Comma-separated file name patterns to scan. Patterns match base names, not paths. | `*.yaml,*.yml,Dockerfile*,Makefile*,*.sh,*.tf,*.tfvars` |
| `token` | Token used to push the branch and open the pull request. | `${{ github.token }}` |
| `registry-map` | Comma-separated `proxy=upstream` prefix mappings for digest lookups. | None |
| `create-pr` | Whether to open a pull request. Set to `false` to leave the changes in the workspace. | `true` |
| `use-gitsign` | Whether to sign commits with gitsign. | `true` |
| `signoff` | Whether to add a `Signed-off-by` line to the commit message. | `false` |
| `author` | Commit author, in the form `Display Name <email@address.com>`. | The user who triggered the run |
| `committer` | Committer, in the form `Display Name <email@address.com>`. | `github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>` |
| `branch-for-pr` | Branch that carries the updates. | `update-digests` |
| `title-for-pr` | Pull request title. | `Update images digests` |
| `description-for-pr` | Pull request body. Digestabot appends the diff to whatever you set. | `Update images digests` |
| `labels-for-pr` | Comma- or newline-separated labels to apply to the pull request. | `automated pr, kind/cleanup, release-note-none` |
| `commit-message` | Commit message. | `Update images digests` |

### Outputs

| Output | Description |
|--------|-------------|
| `json` | The updates Digestabot made. Each entry in `updates` has a `file`, `image`, `digest`, and `updated_digest`. |
| `changed_files` | Newline-separated list of the files Digestabot modified. |
| `pull_request_number` | Number of the pull request Digestabot opened or updated. |

## Troubleshooting

### Digestabot's commits show as unverified

Digestabot signs its commits with gitsign, which uses Sigstore's certificate authority. GitHub doesn't recognize that authority, so it marks the commits **Unverified**. The signature is valid; the badge reflects GitHub's trust configuration rather than a problem with the commit.

This matters when a branch protection rule requires signed commits, because the rule then blocks Digestabot's pull requests from merging. You have two options:

* Sign the commits with a GPG key that GitHub recognizes. Set `create-pr: false` so that Digestabot only edits the files, then import a key and create the pull request in later steps. Chainguard recommends [keyless signing](/open-source/sigstore/cosign/an-introduction-to-cosign/) where you have the choice, so treat this as a way to satisfy the branch protection rule rather than an improvement.
* Set `use-gitsign: false` to leave the commits unsigned, if your repository doesn't require signed commits and you'd rather not carry signatures GitHub can't verify.

### Digestabot opens no pull requests

If the job succeeds but no pull request appears, check the following:

* **The form of the reference.** Digestabot updates only references carrying both a tag and a digest. Refer to [How Digestabot matches references](#how-digestabot-matches-references).
* **The file name.** `include-files` patterns match base names, so Digestabot never reads a reference in a file the patterns don't cover. Refer to [Choose which files to scan](#choose-which-files-to-scan).
* **The repository setting.** Confirm that **Allow GitHub Actions to create and approve pull requests** is selected, as described in [Prerequisites](#prerequisites).
* **An existing pull request.** Digestabot updates an open `update-digests` pull request in place instead of opening a second one.

### Digest lookups fail

The job summary records `Failed to retrieve digest info for <image>` for each reference Digestabot couldn't resolve, followed by the error from the registry. Check the following, in order:

1. Confirm that the `setup-chainctl` step runs before the Digestabot step and completes successfully.
2. Confirm the identity has the `registry.pull` role and access to the repository holding the image. Run `chainctl iam identities list` to review the identities in your organization.
3. Test the reference outside the workflow. Run `chainctl auth configure-docker`, then `crane digest <reference>` or `docker pull <reference>`.
4. If you pull through a registry proxy, confirm whether the lookups need [`registry-map`](#resolve-digests-through-a-registry-proxy).

## Video overview

This 2024 video introduces the problem Digestabot solves, using a digest-pinned multi-stage Python build as the example. The configuration in this guide has moved on since the recording, but the reasoning holds.

{{< youtube 7WvzkwS9yms >}}

{{< details "Transcript" >}}
Today, I'd like to talk about a common question I get asked.

How can you keep images up to date while avoiding breaking changes?

The basic issue is that we'd like to make sure we're getting the latest security updates and features for our software.

But we really don't want our applications and infrastructure to break unexpectedly.

So there's a tension between updating all the time, which gives you the latest code and limits unexpected breakages.

In this example, we have a multi-stage Python build using Chainguard Container which are pinned to Digest.

Now, Digests are content-based hashes of images.

So if you reference an image by Digest, you will always get exactly the same image every time.

Now, this is fantastic for reproducibility.

As I know, if anybody uses this Dockerfile, they will get exactly the same images that I was using.

And this is especially important in Python, where if the version changes, so we go from Python 3.12 to Python 3.13, you might find that various libraries don't work until they're updated.

Now, how do you do updates then?

Well, you could manually go in and change, bump this Digest yourself.

But we've got a better solution for you that I want to talk about briefly today, and it's called Digestabot.

Digestabot is a GitHub action that can be set to run on a cron job and will open a PR when it detects there's a newer version of the image available.

You can then test the image to make sure it works with your application before merging the PR.

So for my example, it would check the Chainguard registry for the current digest of the latest tag and open a PR if it doesn't match the digest in the file.

We use Digestabot internally at Chainguard, and this pattern nicely balances the tension between keeping images up to date and vulnerability-free with the need to test and verify changes before shipping to production.

So please try it out and let me know if you have any questions.
{{< /details >}}

## Learn more

* [Using Dependabot with Chainguard Containers](/chainguard/containers/staying-secure/updating-images/dependabot/) covers the tool to pair with Digestabot for moving between version streams.
* [Using Renovate with Chainguard Containers](/chainguard/containers/staying-secure/updating-images/renovate/) covers the equivalent setup for teams outside GitHub.
* [Strategies and tooling for updating containers](/chainguard/containers/staying-secure/updating-images/strategies-tools-updating-images/) compares the wider range of update tools.
* [Considerations for keeping containers up to date](/chainguard/containers/staying-secure/updating-images/considerations-for-image-updates/) covers the tradeoffs behind an update policy.
* [Container image digests](/chainguard/containers/how-to-use/container-image-digests/) explains what a digest is and why pinning to one matters.
