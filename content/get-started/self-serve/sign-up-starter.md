---
title: "Sign up for Chainguard Starter"
date: 2026-11-03T16:30:40+00:00
lastmod: 2026-11-09T18:55:19+00:00
linktitle: "Sign up for Starter"
description: "Create a free Chainguard Starter organization with chainctl, add images, and join an existing Starter organization"
type: "article"
draft: false
weight: 14
toc: true
tags: ["Getting Started", "Procedural"]
---

[Chainguard Starter](/get-started/self-serve/plans/) is Chainguard's free self-serve plan. You sign up with `chainctl starter init`, which creates a Starter organization for you and, optionally, adds your first images. This page covers signing up, adding images, joining an organization that already exists, and signing up from a script or a coding agent.

## Before you begin

You need the following:

* `chainctl` 0.2.394 or later. To install it, refer to [How to install chainctl](/platform/chainctl-usage/how-to-install-chainctl/). To update an existing installation, run `sudo chainctl update`, or `brew upgrade chainctl` if you installed it with Homebrew.
* A verified email address on one of these accounts: GitHub, GitLab, Google, or an email-and-password account. For GitHub and GitLab, Chainguard uses the account's primary email address.

Use a business email address if you plan to invite colleagues. With a business address, Chainguard names your organization after your email domain, and you can invite people whose addresses are in that domain. A personal email address, such as a Gmail address, creates an organization that isn't tied to any domain and can't invite anyone until it upgrades to Chainguard Team.

## Sign up

To create a Starter organization, complete the following steps:

1. Run `chainctl starter init`:

    ```shell
    chainctl starter init
    ```

1. Choose an identity provider from the menu. `chainctl` offers to save your choice, so you aren't asked again next time.
1. Sign in using the browser window that opens. You have 5 minutes to finish.
1. Answer the questions about your name, company, job title, and whether you want updates from Chainguard. Before the questions, `chainctl` prints the terms and privacy notice that you agree to by continuing.
1. If you signed in with a personal email address, enter a name for your organization. The name can't look like a domain name.

`chainctl` creates your organization and prints its name and ID. Chainguard then sets up the organization's access to images, which usually takes a few minutes.

To add images as part of signing up, list them with `--images`. For example, the following command signs in with GitHub and adds the `nginx` and `redis` images once the organization is ready:

```shell
chainctl starter init --social-login github --images nginx,redis
```

## Add images

A Starter organization can access up to five images. To find image names, browse the [Chainguard Directory](/chainguard/containers/registry/chainguard-directory/). To add images after you sign up, run `chainctl starter add-images` with one or more image names:

```shell
chainctl starter add-images nginx redis
```

Once you add an image, you can't swap it for another one. When all five slots are used, `chainctl starter status` says so and links to a page for contacting Chainguard about more images. To add a Helm chart, use `chainctl images helm add-chart`. Each image the chart needs that your organization doesn't already have uses one of the five slots. Refer to [Self-serve Helm charts](/get-started/self-serve/helm-charts/#chainguard-starter-and-chainguard-team-organizations).

To check whether your images are ready to pull, run `chainctl starter status`. It shows your organization's registry path, how many images you've added, and each image's state. An image shows `INITIALIZING` until it's ready to pull, then `READY`.

```shell
chainctl starter status
```

When an image is ready, pull it from your organization's registry path. Replace `$ORGANIZATION` with the registry path that `chainctl starter status` shows:

```shell
docker pull cgr.dev/$ORGANIZATION/nginx:latest
```

An organization created with a personal email address has no domain, so its registry path uses the organization's ID instead of a name.

To pull from CI pipelines, create a pull token. Refer to [Authenticate CI pipelines with a pull token](/chainguard/containers/reference/catalog-starter/#authenticate-ci-pipelines-with-a-pull-token).

## Join an existing organization

If your company already has a Starter organization for your email domain, `chainctl starter init` can't create a second one. Ask to join the existing organization instead:

1. Sign in to Chainguard with your business email address:

    ```shell
    chainctl auth login
    ```

1. Request access:

    ```shell
    chainctl starter request-access
    ```

Chainguard emails the request to the organization's owners, who decide whether to invite you. For privacy, the command responds the same way whether or not an organization exists for your domain.

## Sign up from a script or a coding agent

`chainctl starter init` can run without prompts, which lets a script or a coding agent run it for you. You still sign in yourself in the browser.

Pass `--non-interactive` with a flag for each question:

```shell
chainctl starter init --non-interactive --social-login google \
  --given-name Ada --family-name Lovelace --company Acme --job-title Engineer \
  --output json
```

With `--non-interactive`, the command never prompts. If a required flag is missing, it fails and names the flags it needs. A missing `--email-updates` counts as no. If you sign up with a personal email address, also pass `--name`.

With `--output json`, the command writes progress to standard error and writes one JSON object to standard output. The object includes the outcome, the organization's ID and name, the images it added, the next command to run, and the error, if any. If the identity you signed in with already belongs to an organization, the object also includes `organizations`, the organizations it belongs to; `identity`, the email address it signed in with; and `hint`, what to do instead.

The command exits with one of the following codes:

| Code | Meaning |
| ---- | ------- |
| `0` | The organization was created, and any `--images` were added. |
| `1` | Any other failure, such as an invalid or missing flag, or a network error. |
| `3` | The identity you signed in with already belongs to an organization. The browser may have reused an earlier sign-in; sign out in the browser to use another identity. |
| `4` | The identity isn't eligible for a Starter organization. |
| `5` | The organization couldn't be created. One may already exist for your email domain; run `chainctl starter request-access`. |
| `6` | Authentication failed. |
| `7` | The organization was created, but a later step failed, such as adding the `--images`. The JSON's `next` field names the command to run next. Pressing Ctrl-C after the organization was created also exits with `7`. |
| `8` | The browser sign-in wasn't finished within 5 minutes. Run the same command again. |

### Have a person accept the terms

When a coding agent signs up for you, add `--terms-step` so that you, not the agent, accept the terms. This flag needs `chainctl` 0.2.397 or later.

With `--terms-step` and `--output json`, the JSON object also includes the following fields:

* `terms`: the statement to accept and the documents it refers to.
* `plan`: what the Starter plan includes and excludes. The list can include limits that Chainguard doesn't enforce yet. For the current limits, refer to [Chainguard plans](/get-started/self-serve/plans/).

Once the organization exists, the `next` field names the command that accepts the terms. An owner of the organization reads the terms and runs it. Replace `<organization-id>` with the ID from the JSON's `organization` field:

```shell
chainctl starter accept-terms --parent <organization-id>
```

The command prints what the Starter plan includes, then the terms, and asks you to accept them. Without an interactive terminal, add `--yes`; using it means you agree to the terms. Running the command again after the terms are accepted changes nothing.

## Next steps

* Compare what Starter and Team include in [Chainguard plans](/get-started/self-serve/plans/).
* To use Chainguard Checks and Chainguard Workspaces, refer to [Set up Chainguard Checks and Chainguard Workspaces](/get-started/checks-and-workspaces/set-up/).
