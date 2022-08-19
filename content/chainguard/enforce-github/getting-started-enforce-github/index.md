---
title : "Getting Started with Chainguard Enforce for GitHub"
description: "Enforcing commit signatures with GitHub"
type: "article"
date: 2022-08-11T13:41:00+00:00
lastmod: 2022-08-11T13:41:00+00:00
draft: false
images: []
menu:
  docs:
    parent: "enforce-github"
weight: 620
toc: true
---

Chainguard Enforce for GitHub currently supports Gitsign signatures from the public Sigstore instance.

**Note**: This app is currently in alpha, so permissions may change, and features may be added or removed without notice during this time.

## Installation

To get started, you'll need to [install the app on GitHub](../install-enforce-github/) to either your personal accoun or your organization.

Additionally, you will need to [install and configure Gitsign](https://docs.sigstore.dev/gitsign/installation) on your development machine. You may also wish to consulst the [Gitsign repo README](https://github.com/sigstore/gitsign/blob/main/README.md).

Once this is done, the Enforce for GitHub app will automatically respond to new pull requests events.

![Review that checks have passed](check.png)

Note that the app will only respond to existing pull requests if there is new commit activity/

## Require Enforce for submission

To require the Enforce for GitHub app to succeed before pull request submission, enable the **[Require status checks before merging](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#require-status-checks-before-merging)** feature on the desired branch for the `Enforce - Commit Signing` check.

![Protect branches with Chainguard Enforce](protected-branch.png)

You can find this page by navigating to a given repository's **Settings** and then clicking on **Branches** (under **Code and automation**).

### Enable or disable repositories

If you wish to add or remove repositories that Enforce for GitHub responds to in an organization, you can do so via the installation settings page. This page can be found by:

- From a repository page: **Settings** > **Integrations** > **GitHub apps** > **Installed GitHub Apps** > **Chainguard Enforce** > **Configure**
- From an organization page: **Settings** > **Integrations** > **Applications** > **Installed GitHub Apps** > **Chainguard Enforce** > **Configure**

From here, the **Repository Access** configuration can be used to add or remove repos from the app installation.

![Set Chainguard Enforce repository access](repo-access.png)

This page may also be used to completely uninstall the Enforce app from your organization.

Note that if you want to add a new organization or repo, return to the [Installation section](#installation) for relevant instructions.

## Roadmap

Chainguard Enforce for GitHub has a number of features on its roadmap.

- Bring your own Sigstore instance
- Policies — define policies for what identities can or must sign your code.
- Supply chain security insights

And there's more to come!

Want to learn more about Chainguard Enforce? Have a feature request? Let us know at [https://www.chainguard.dev/contact](https://www.chainguard.dev/contact).