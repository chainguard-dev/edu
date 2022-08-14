---
title : "Chainguard Enforce for GitHub"
description: "Enforcing commit signatures with GitHub"
type: "article"
date: 2022-08-11T13:41:00+00:00
lastmod: 2022-08-11T13:41:00+00:00
draft: false
images: []
---

Chainguard Enforce for GitHub offers git signature verification and enforcement for your GitHub repos. With Enforce for GitHub, you can verify [Sigstore Gitsign](https://docs.sigstore.dev/gitsign/overview) commits and have greater trust in commits by signing commits with ephemeral keys tied to user identities.

Enforce for GitHub currently works with public or private repos on [github.com](https://github.com).

**Note**: This app is currently alpha: permissions may change, and features may be added or removed without notice during this time.

## Installation

This section will walk you through installing and setting up Chainguard Enforce for GitHub. 

### Prerequisites

This app assumes that you have a GitHub account, and that mosty likely you are already connected to a GitHub organization and collaborating on code repositories. 

Before you can install, you'll need to register your organization for early access.

During early access, Chainguard is requiring users to manually register the organizations they wish to use with Enforce for GitHub. While skipping this step will not prevent you from installing the app on GitHub, the app will not respond to repository webhooks until you are registered.

To register, you will need to provide the following information:

- Point of contact for feedback and announcements.
- What orgs and repos you would like to enable.

### Navigate to app on GitHub 

Navigate to the GitHub app installation page available at [https://github.com/apps/chainguard-enforce](https://github.com/apps/chainguard-enforce).

<img src="/chainguard/enforce/configure.png">

From here, select the **Configure** button towards the right of the page. 

### Select user or organization

Once you click on the **Configure** button, you'll be directed to a page where you can select your desired user or orgization.

<img src="/chainguard/enforce/user-select.png">

If you select your user, you will be able to install onto your personal account and will be able to select either the all of your repos or specific ones. If you select an organization, you will install Enforce for GitHub onto your GitHub organization. You will need administative access or approval to do this. Within this workflow you can also select either all of the organization's repos or specific ones. 

### Review and install

At this point, you should review your permissions. You can restrict Enforce for GitHub to only have access to certain repos within your account or organization.

<img src="/chainguard/enforce/permissions.png">

The following table explains the permissions that the app is granted and why each permission is needed. 

| Permission                      | Why it's needed                                                           |
| ------------------------------- | ------------------------------------------------------------------------- |
| Read access to metadata         | Required by GitHub Apps                                                   |
| Read access to code             | Used to fetch commit signatures and receive push events.                  |
| Read access to pull requests    | Used to resolve pull requests to commits and receive pull request events. |
| Read and write access to checks | Used to write pull request status checks.                                 |

Once you are satisfied with the permissions and the location where you want the app installed, you can continue the workflow to install Chainguard Enforce for GitHub.

## Usage

Currently, Enforce for GitHub supports Gitsign signatures from the public Sigstore instance.

### Installation

To get started, you'll need to [install the app on GitHub](#installation) to either your personal accoun or your organization.

Additionally, you will need to [install and configure Gitsign](https://docs.sigstore.dev/gitsign/installation) on your development machine. You may also wish to consulst the [Gitsign repo README](https://github.com/sigstore/gitsign/blob/main/README.md).

Once this is done, the Enforce for GitHub app will automatically respond to new pull requests events.

<img src="/chainguard/enforce/check.png">

Note that the app will only respond to existing pull requests if there is new commit activity/

### Require Enforce for submission

To require the Enforce for GitHub app to succeed before pull request submission, enable the **[Require status checks before merging](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#require-status-checks-before-merging)** feature on the desired branch for the `Enforce - Commit Signing` check.

<img src="/chainguard/enforce/protected-branch.png">

You can find this page by navigating to a given repository's **Settings** and then clicking on **Branches** (under **Code and automation**).

### Enable or disable repositories

If you wish to add or remove repositories that Enforce for GitHub responds to in an organization, you can do so via the installation settings page. This page can be found by:

- From a repository page: **Settings** > **Integrations** > **GitHub apps** > **Installed GitHub Apps** > **Chainguard Enforce** > **Configure**
- From an organization page: **Settings** > **Integrations** > **Applications** > **Installed GitHub Apps** > **Chainguard Enforce** > **Configure**

From here, the **Repository Access** configuration can be used to add or remove repos from the app installation.

<img src="/chainguard/enforce/repo-access.png">

This page may also be used to completely uninstall the Enforce app from your organization.

Note that if you want to add a new organization or repo, return to the [Installation section](#installation) for relevant instructions.

## Roadmap

Chainguard Enforce for GitHub has a number of features on its roadmap.

- Bring your own Sigstore instance
- Policies — define policies for what identities can or must sign your code.
- Supply chain security insights

And there's more to come!

## Support

If you encounter any issues, please reach out to the team via [support@chainguard.dev](mailto:support@chainguard.dev).

Want to learn more about Chainguard Enforce? Have a feature request? Let us know at [https://www.chainguard.dev/contact](https://www.chainguard.dev/contact).
