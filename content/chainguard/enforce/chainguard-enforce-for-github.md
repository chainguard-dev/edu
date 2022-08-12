---
title : "Chainguard Enforce for GitHub"
description: "Enforcing commit signatures with GitHub"
type: "article"
date: 2022-08-11T13:41:00+00:00
lastmod: 2022-08-11T13:41:00+00:00
draft: false
images: []
---

Git signature verification and enforcement for your GitHub repos!

NOTE: This app is currently alpha - Permissions may change, and features may be added/removed without notice during this time.

## Features

- Verify Sigstore Gitsign commits — have greater trust in commit by signing commits with ephemeral keys tied to user identities.
  - Currently works with public or private repos on `github.com`.

## Installation

1. Register your org for early access

   During early access, Chainguard is requiring users to manually register the orgs they wish to use with the app. While skipping this step will not prevent you from installing the app on GitHub, the app will not respond to repository webhooks until this is done.

   - Point of contact for feedback / announcements.
   - What orgs / repos you would like to enable.

2. Navigate to the App installation page -
   https://github.com/apps/chainguard-enforce

   <img src="/chainguard/enforce/configure.png">

   - Select `Configure`

3. Select your desired user/org

   <img src="/chainguard/enforce/user-select.png">

4. Review permissions and install

   <img src="/chainguard/enforce/permissions.png">

   - (optional): Restrict app to certain repos within your organization.

   | Permission                      | Why it's needed                                                           |
   | ------------------------------- | ------------------------------------------------------------------------- |
   | Read access to metadata         | Required by GitHub Apps                                                   |
   | Read access to code             | Used to fetch commit signatures and receive push events.                  |
   | Read access to pull requests    | Used to resolve pull requests to commits and receive pull request events. |
   | Read and write access to checks | Used to write pull request status checks.                                 |

## Usage

Currently the app supports Gitsign signatures from the public Sigstore instance.

To get started:

- [Install the app on your org](#installation).
- On your development machine,
  [install and configure Gitsign](https://github.com/sigstore/gitsign/blob/main/README.md).

Once this is done, the Enforce app will automatically respond to new pull requests events (note: the app will only respond to existing pull requests if there is new commit activity).

<img src="/chainguard/enforce/check.png">

### Require Enforce for submission

To require the Enforce app to succeed before pull request submission, enable the [`Require status checks before merging`](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#require-status-checks-before-merging) feature on the desired branch for the `Enforce - Commit Signing` check.

<img src="/chainguard/enforce/protected-branch.png">

### Enable/disable repositories

If you wish to add or remove repositories that Enforce for GitHub responds to in an organization you can do so via the installation settings page. This page can be found by:

- From a repository page: Settings > Integrations > GitHub apps > Installed GitHub Apps > Chainguard Enforce > Configure
- From an organization page: Settings > Integrations > Applications > Installed GitHub Apps > Chainguard Enforce > Configure

From here, the `Repository Access` configuration can be used to add / remove
repos from the app installation.

<img src="/chainguard/enforce/repo-access.png">

This page may also be used to completely uninstall the Enforce app from your organization.

NOTE: If you want to add a new organization / repo, follow the [Installation instructions](#installation).

## Roadmap

- Bring your own Sigstore instance
- Policies - define policies for what identities can/must sign your code.
- Supply Chain Security Insights
- And more to come!

## Support

If you encounter any issues, please reach out at [support@chainguard.dev](mailto:support@chainguard.dev).

Want to learn more about Chainguard Enforce? Have a feature request? Let us know at [https://www.chainguard.dev/contact](https://www.chainguard.dev/contact).
