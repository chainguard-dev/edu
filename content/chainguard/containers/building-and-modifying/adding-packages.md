---
title: "Adding a package to a Chainguard Container"
linktitle: "Add a package"
description: "Choose how to add a package to a Chainguard Container, find the package name, apply the change, and confirm the package reached the finished image."
type: "article"
date: 2026-09-09T00:00:00+00:00
lastmod: 2026-09-09T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly", "Procedural"]
images: []
weight: 005
toc: true
---

Chainguard Containers ship with only the packages their application needs, so sooner or later you'll want one that isn't there. [Custom Assembly](/chainguard/containers/custom-assembly/overview/) is the supported way to add it. You declare the package you want, Chainguard builds the image on its own infrastructure, and Chainguard rebuilds that image whenever the package is updated. You can drive Custom Assembly from the Chainguard Console, interactively with `chainctl`, or non-interactively with `chainctl` from a pipeline.

This page helps you pick an approach, then covers the three steps that apply whichever one you pick: finding the package name, adding the package, and confirming that it reached the finished image.

## Choose an approach

The following table compares the available approaches:

| Approach | Use it when | What you need |
| --- | --- | --- |
| [Custom Assembly in the Console](#add-the-package-in-the-console) | You want to browse the packages your organization can add and apply the change in a few clicks. | A Console account with a role that has the `repo.update` capability. |
| [Custom Assembly with `chainctl`, interactively](#add-the-package-with-chainctl-interactively) | You work from a terminal and want to review a diff before it applies. | `chainctl`, installed and authenticated. |
| [Custom Assembly with `chainctl`, non-interactively](#add-the-package-with-chainctl-non-interactively) | You keep image configuration in version control or apply it from CI/CD. | `chainctl` and a YAML build configuration file. |
| [Custom Assembly with the Chainguard API](/chainguard/containers/custom-assembly/custom-assembly-api-demo/) | You're building your own tooling around Custom Assembly. | An API client and a Chainguard token. |
| [`apk add` in a Dockerfile](/chainguard/containers/using-and-deploying/using-containers/#extending-chainguard-base-containers) | You build on a `-dev` variant or on `wolfi-base`, and you're prepared to pin package versions and image digests yourself. | A Dockerfile and a container image that includes `apk`. |
| [`apk` with `chroot` in a multi-stage build](/chainguard/containers/building-and-modifying/install-apks-in-distroless-variants/) | You need a package in a distroless image and Custom Assembly doesn't fit your workflow. | A multi-stage Dockerfile. |

Custom Assembly is the recommended approach because Chainguard's build pipeline resolves the packages you add against the packages already in the base image, then rebuilds the image when any of them change. Adding packages with `apk add` in your own Dockerfile moves that work to you: without pinned package versions and image digests, a package update can conflict with an older dependency in the base image and break your build until a new base image is released. For the longer version of this argument, see [Why use Custom Assembly for adding packages](/chainguard/containers/custom-assembly/overview/#why-use-custom-assembly-for-adding-packages).

{{< note >}}
Custom Assembly is available to organizations with access to [production Chainguard Containers](/chainguard/containers/concepts/container-categories/#production-containers). If you use Chainguard's free container images, take one of the Dockerfile approaches.
{{< /note >}}

## Before you begin

The Custom Assembly approaches on this page share these prerequisites:

* Access to production Chainguard Containers.
* A role with the `repo.update` capability, to customize an existing image in place, or the `repo.create` capability, to save the result as a new image. Of Chainguard's three default roles — `viewer`, `editor`, and `owner` — only `owner` has both. For a custom role you can create instead, see [Custom Assembly permissions requirements](/chainguard/containers/custom-assembly/overview/#custom-assembly-permissions-requirements).
* For the `chainctl` approaches, [`chainctl` installed](/platform/chainctl-usage/how-to-install-chainctl/) and [authenticated](/platform/chainctl-usage/authentication-options/).

Custom Assembly adds packages to an image; it can't remove the packages the source image already contains. You can, however, remove packages you added in an earlier build.

## Find the package name

You can add only the packages your organization is entitled to, which are the packages that appear in the Chainguard Containers you already have access to. Package names often carry a version stream — `python-3.14` rather than `python` — so confirm the exact name before you add it.

### Find a package in the Console

Open the image in the [Chainguard Console](https://console.chainguard.dev), click **Customize image**, then use the **Filter packages** box. The list holds every package your organization can add. If the package you want isn't listed, open a Chainguard support ticket.

### Find a package with apk

Container images that include `apk` — a `-dev` variant does — can search the repository from inside a running container. For a free container image, no authentication is needed:

```shell
docker run --rm --entrypoint sh cgr.dev/chainguard/wolfi-base:latest \
  -c 'apk update > /dev/null && apk search -e "mongo*"'
```

```output
mongo-tools-100.18.0-r6
mongodb-kubernetes-operator-0.13.0-r14
mongodb-kubernetes-operator-compat-0.13.0-r14
mongodb-kubernetes-operator-readinessprobe-0.13.0-r14
```

To search the packages your organization is entitled to, start a `-dev` variant of one of your organization's images with an `HTTP_AUTH` variable so that `apk` can reach your [private APK repository](/chainguard/containers/building-and-modifying/packages/private-apk-repos/):

```shell
docker run -it --rm --entrypoint /bin/sh --user root \
  -e "HTTP_AUTH=basic:apk.cgr.dev:user:$(chainctl auth token --audience apk.cgr.dev)" \
  cgr.dev/$ORGANIZATION/$CONTAINER:latest-dev
```

From the container's shell, run `apk update` and then `apk search`.

## Add the package

The three procedures that follow all produce the same result. Pick the one that matches how you work.

### Add the package in the Console

1. In the [Chainguard Console](https://console.chainguard.dev), open the image you want to customize.
2. Click **Customize image**, then select the packages to add.
3. Click **Continue**, then choose **Create a new image** or **Customize current image**.
4. Click **Preview changes** and review the package list.
5. Click **Apply changes**.

For the full walkthrough, including how to edit or remove customizations later, see [Using the Chainguard Console to manage Custom Assembly resources](/chainguard/containers/custom-assembly/custom-assembly-console/).

### Add the package with chainctl interactively

1. Open the image's build configuration:

    ```shell
    chainctl images repos build edit --parent $ORGANIZATION --repo $CONTAINER
    ```

    Replace `$ORGANIZATION` with your organization's name and `$CONTAINER` with the name of the image. If you omit either flag, `chainctl` prompts you to choose.

2. `chainctl` opens the configuration in your default text editor. Add the package under `contents.packages`:

    ```yaml
    contents:
      packages:
      - yarn
      - wget
      - bash
    ```

3. Save and close the file. `chainctl` prints a diff and asks you to confirm:

    ```output
    /tmp/3352123767.yaml (-deletion / +addition):

     contents:
       packages:
       - yarn
       - wget
    +  - bash

    Applying build config to $CONTAINER
    Are you sure?
    Do you want to continue? [y,N]:
    ```

4. Enter `y` to start the build.

To save the result as a new image rather than changing the existing one, add `--save-as $NEW_NAME`. For the rest of what you can set in this file, including environment variables, annotations, and custom user accounts, see [Using chainctl to manage Custom Assembly resources](/chainguard/containers/custom-assembly/custom-assembly-chainctl/).

### Add the package with chainctl non-interactively

Both `apply` and `edit` accept a configuration file, which skips the editor and the prompt. Use this form in CI/CD and anywhere you keep image configuration in version control.

1. Write the build configuration to a file:

    ```shell
    cat > build.yaml <<EOF
    contents:
      packages:
        - bash
        - curl
        - mysql
    EOF
    ```

2. Preview what the file would change, without changing anything:

    ```shell
    chainctl images repos build apply -f build.yaml --parent $ORGANIZATION --repo $CONTAINER --dry-run
    ```

    `--dry-run` prints the diff and exits with a non-zero status if there's anything to apply, which makes it usable as a drift check in a pipeline.

3. Apply the configuration. `--yes` confirms the change without prompting:

    ```shell
    chainctl images repos build apply -f build.yaml --parent $ORGANIZATION --repo $CONTAINER --yes
    ```

To save the result as a new image, add `--save-as $NEW_NAME`. This works when you target a single repository; it isn't available when you target several at once with repeated `--repo` flags or a wildcard.

For a worked GitHub Actions pipeline built around these commands, see [Using GitOps to manage Custom Assembly resources](/chainguard/containers/custom-assembly/custom-assembly-gitops/).

## Confirm the package is in the image

Custom Assembly builds run on Chainguard's infrastructure and normally finish in under 20 minutes, so your change won't reach the registry immediately.

1. Check that the build succeeded:

    ```shell
    chainctl images repos build list --parent $ORGANIZATION --repo $CONTAINER
    ```

    ```output
              START TIME           |        COMPLETION TIME        | RESULT  |             TAGS
    -------------------------------|-------------------------------|---------|-------------------------------
     Wed, 09 Sep 2026 12:46:56 CDT | Wed, 09 Sep 2026 12:47:13 CDT | Success | 26-full, 26.8-full, latest-full
     Wed, 09 Sep 2026 12:45:22 CDT | Wed, 09 Sep 2026 12:46:13 CDT | Success | 26-dev, 26.8-dev, latest-dev
    ```

    The Console shows the same information on the image's **Builds** tab. Builds stay listed for 24 hours.

2. Pull the image:

    ```shell
    docker pull cgr.dev/$ORGANIZATION/$CONTAINER:latest
    ```

3. Check for the package. If the image includes `apk`, query it directly. `apk info -e` prints the package name when the package is installed and exits with a non-zero status when it isn't:

    ```shell
    docker run --rm --entrypoint apk \
      cgr.dev/$ORGANIZATION/$CONTAINER:latest-dev info -e bash
    ```

    ```output
    bash
    ```

    Distroless images have no `apk`, so read the image's SBOM instead. This command lists the apk packages in the image:

    ```shell
    cosign download attestation \
      --platform linux/amd64 \
      --predicate-type https://spdx.dev/Document \
      cgr.dev/$ORGANIZATION/$CONTAINER:latest \
      | jq -r '.payload' | base64 -d \
      | jq -r '.predicate.packages[]
               | select(.externalRefs[]?.referenceLocator? // "" | startswith("pkg:apk/"))
               | .name'
    ```

    ```output
    ca-certificates-bundle
    gdbm
    glibc-2.44
    ld-linux-2.44
    python-3.14
    ```

    The Console shows the same list on the image's **SBOM** tab. For more ways to read this data, see [Retrieving Chainguard Container SBOMs](/chainguard/containers/security-and-compliance/retrieve-image-sboms/).

## If the build fails

A Custom Assembly build reports failure only after it finishes. Retrieve the logs for a build with the `logs` subcommand, which prompts you to pick a build report:

```shell
chainctl images repos build logs --parent $ORGANIZATION --repo $CONTAINER
```

In the Console, click a row on the image's **Builds** tab to open the same logs.

Builds fail for a few recurring reasons:

* Two packages install the same file, and Custom Assembly can't resolve the conflict.
* A package is newer than the base image and was built against a newer version of `glibc`.
* The build ran longer than an hour and timed out.
* The package isn't one your organization is entitled to.

For more on these cases, see [Custom Assembly troubleshooting](/chainguard/containers/custom-assembly/faq/#custom-assembly-troubleshooting). If you can't resolve a failure, [contact Chainguard support](https://www.chainguard.dev/contact?utm=docs).

## Learn more

* [Overview of Chainguard Custom Assembly](/chainguard/containers/custom-assembly/overview/) covers what Custom Assembly can change, its limitations, and how the CVE remediation SLA applies to customized images.
* [Custom Assembly FAQs](/chainguard/containers/custom-assembly/faq/) answers questions about entitlements, FIPS, and support boundaries.
* [Overview of Chainguard's package repositories](/chainguard/containers/building-and-modifying/packages/package-model/) explains where the packages you can add come from.
* [Adding custom certificates with Custom Assembly](/chainguard/containers/custom-assembly/custom-assembly-certs/) covers embedding internal CA certificates in an image.
