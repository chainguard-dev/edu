---
title: "Workload identities and trust in Chainguard Checks"
linktitle: "Identities and trust"
description: "Learn how a Chainguard Checks check gets short-lived Google Cloud or Chainguard credentials through a workload identity, how to limit which pull requests get one, and how to revoke access."
type: "article"
date: 2026-10-12T00:00:00+00:00
lastmod: 2026-10-20T18:30:00+00:00
draft: false
tags: ["Chainguard Checks", "Configuration", "Security"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 35
---

A check that must authenticate to Google Cloud or to Chainguard, such as to read a Cloud Storage bucket or to pull private images from `cgr.dev`, can use a *workload identity*: short-lived credentials that Chainguard Checks gives the check while it runs. This page explains how workload identities work, how to declare and set one up, how to limit which pull requests get one, and how to revoke access.

## How workload identities work

A check's VM holds no long-lived credentials. When a check uses a workload identity, Chainguard Checks issues the check an OpenID Connect (OIDC) token that lasts five minutes, renews the token while the check runs, and keeps the real credentials outside the VM:

| Provider | What the check's VM holds |
| --- | --- |
| Google Cloud | `GOOGLE_APPLICATION_CREDENTIALS`, set to `/run/chainguard/identities/<identity>/adc.json`, a credential configuration that Google Cloud client libraries use without further setup. The tokens that code in the VM can read are sealed stand-ins. Chainguard Checks swaps in the real tokens only on requests to `sts.googleapis.com` and other `googleapis.com` subdomains, such as `storage.googleapis.com`. |
| Chainguard | Nothing. Chainguard Checks adds a credential to the check's requests to each Chainguard host the identity lists, so the check doesn't sign in or need a credential file. |

Code in the check can't read the real tokens, but it can use them: each request it sends to those hosts carries the identity's access. If that access lets the code create a credential, such as a Google Cloud service account key, that credential works outside the check until you delete it. Grant each identity only the access its checks need.

What code can use depends on where it runs:

| Where code runs | Credentials it can use |
| --- | --- |
| A check on a pull request | The identity the check names, if `identities.yaml` on the pull request's base branch allows it for that check and branch. If your default branch has a [`trust` section](#limit-which-pull-requests-get-an-identity), the pull request must also reach the identity's ring. |
| A check after a change merges | The identity the check names, if `identities.yaml` on your default branch allows it for that check and branch. |
| A Chainguard Workspaces session, including the checks that `run-ci` runs in it | The session's own credentials, as described in [Manage Chainguard Workspaces session credentials](/chainguard/workspaces/credentials/). Sessions don't get workload identities, so [`run-ci`](/chainguard/checks/run-checks/) skips checks that use one. |

## Declare an identity

You declare workload identities in `.chainguard/ci/identities.yaml`, which works with either [file layout](/chainguard/checks/configuration/#file-layouts). The file has the following top-level keys:

| Key | Required | Description |
| --- | --- | --- |
| `version` | Yes | The format version. Must be `1`. |
| `identities` | Yes | A map from each identity's name to its definition. Refer to [Identity keys](#identity-keys). |
| `trust` | No | Which pull requests get identities, decided by who opened them. Refer to [Limit which pull requests get an identity](#limit-which-pull-requests-get-an-identity). |

Chainguard Checks refuses keys it doesn't recognize. To check the file before you merge it, run `chainctl checks validate .`, as described in [Validate your configuration offline](/chainguard/checks/run-checks/#validate-your-configuration-offline).

The following file declares an identity named `gcs-read` that the `integration` check in `.chainguard/ci.yaml` can use on pull requests into `main`:

```yaml {title=".chainguard/ci/identities.yaml"}
version: 1
identities:
  gcs-read:
    description: Read test fixtures from Cloud Storage.
    checks:
      - ci.checks.integration
    audiences:
      - https://iam.googleapis.com/projects/123456789012/locations/global/workloadIdentityPools/checks/providers/checks
    gcp:
      provider: projects/123456789012/locations/global/workloadIdentityPools/checks/providers/checks
      audience: https://iam.googleapis.com/projects/123456789012/locations/global/workloadIdentityPools/checks/providers/checks
    allow:
      - run: presubmit
        target_ref: refs/heads/main
```

A check uses an identity by naming it with `identity`. For a Google Cloud identity, the check's `network.egress` must list `sts.googleapis.com`, where client libraries exchange the identity's token, and each Google API host the check calls:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [go]
checks:
  integration:
    cmd: go test -tags=integration ./...
    identity: gcs-read
    network:
      egress:
        - proxy.golang.org
        - sum.golang.org
        - sts.googleapis.com
        - storage.googleapis.com
```

Merge an identity's definition before you use it. Chainguard Checks reads definitions from the base branch, so on the pull request that adds `gcs-read`, the `integration` check can't get the identity and fails.

A check that uses an identity can't set `GOOGLE_APPLICATION_CREDENTIALS` in its `vars` or in its environment's `vars`. If it does, the whole run fails.

### Identity keys

Each identity has the following keys:

| Key | Required | Description |
| --- | --- | --- |
| `description` | No | A description of the identity. |
| `checks` | Yes | A list of selectors for the checks that can use the identity. |
| `audiences` | Yes | A list of the audiences that the identity's tokens can carry. It must include `gcp.audience` and each Chainguard host's `exchange_audience`. |
| `allow` | Yes | A list of the runs that can get the identity. |
| `gcp` | No | Google Cloud settings, both required: `provider`, the workload identity pool provider's resource name, in the form `projects/<project-number>/locations/global/workloadIdentityPools/<pool>/providers/<provider>`, and `audience`, an audience that the provider accepts. |
| `chainguard` | No | A map from each Chainguard host to its settings. Refer to [Chainguard hosts](#chainguard-hosts). |
| `ring` | With a `trust` section | Which pull requests get the identity. Refer to [Limit which pull requests get an identity](#limit-which-pull-requests-get-an-identity). |

An identity needs `gcp`, `chainguard`, or both to give a check any credentials. Identity names are 1 to 48 lowercase letters, digits, and `-`, and start with a letter.

Each `checks` entry has the form `<file>.checks.<check>`. `<file>` is a check file's name without `.yaml`, such as `go` for `.chainguard/ci/go.yaml` or `ci` for `.chainguard/ci.yaml`. `<check>` is a check's name in that file. Either part can be `*` to match any file or any check, but only as the whole part, so `go.checks.test-*` is an error. Quote a selector that starts with `*`, such as `"*.checks.lint"`, because YAML reads a leading `*` as an alias.

Each `allow` entry names a kind of run and its branch:

| `run` | Ref key | Runs it allows |
| --- | --- | --- |
| `presubmit` | `target_ref`, such as `refs/heads/main` | Pull requests whose base branch is that branch. |
| `postsubmit` | `ref`, such as `refs/heads/main` | Runs after a change merges to that branch. Chainguard Checks runs these only on your default branch. |

Each ref must be a full ref that starts with `refs/`.

### Chainguard hosts {#chainguard-hosts}

Each key under `chainguard` is a Chainguard host, and its value has the following keys, all required:

| Key | Description |
| --- | ----------- |
| `identity` | The ID of an assumable identity in your Chainguard organization that trusts this workload identity's tokens. Refer to [Set up the provider](#set-up-the-provider). |
| `exchange_audience` | The audience that the assumable identity accepts. It must also be in the identity's `audiences`. |
| `role` | The most access the check gets on the host, from the following table. The assumable identity's role bindings must also grant that access. |
| `scopes` | A list of group IDs, such as your organization's ID. Only the assumable identity's role bindings on these groups, or on the groups that contain them, apply. |

Each host accepts the following roles:

| Host | `role` | What the check can do |
| ---- | ------ | --------------------- |
| `cgr.dev` | `registry.pull` | Pull container images. |
| `cgr.dev` | `registry.push` | Pull and push container images. |
| `apk.cgr.dev` | `apk.pull` | Download packages. |
| `libraries.cgr.dev` | `libraries.javascript.pull` | Download JavaScript libraries from Chainguard Libraries. |
| `libraries.cgr.dev` | `libraries.python.pull` | Download Python libraries from Chainguard Libraries. |
| `libraries.cgr.dev` | `libraries.java.pull` | Download Java libraries from Chainguard Libraries. |
| `console-api.enforce.dev` | `console.viewer` | List groups, identities, roles, role bindings, and identity providers in the Chainguard API. |

A check that uses a Chainguard host must list it in `network.egress`, along with any host that the service redirects downloads to.

## Set up the provider

A definition in `identities.yaml` grants no access by itself. The provider must also trust the identity's tokens and grant them access. Chainguard Checks issues each token with the following claims:

| Claim | Value |
| ----- | ----- |
| `iss` | `https://issuer.enforce.dev` |
| `sub` | `chainguard:<repository-id>:<identity>`, where `<repository-id>` is a 32-character hexadecimal ID that Chainguard assigns to your GitHub repository, and `<identity>` is the identity's name. |
| `aud` | The identity's `gcp.audience`, or a Chainguard host's `exchange_audience`. |
| `ref` | For a run after merging, the ref it runs on, such as `refs/heads/main`. Tokens for pull requests have no `ref` claim. |

Every Chainguard Checks customer's tokens come from the same issuer, and any repository can ask for any audience, so the subject is what sets your identities apart from everyone else's. Match the exact subject on the provider:

- For Google Cloud, add an OIDC provider to a workload identity pool, with the issuer `https://issuer.enforce.dev` and the attribute mapping `google.subject=assertion.sub`. Grant IAM roles to the principal `principal://iam.googleapis.com/projects/<project-number>/locations/global/workloadIdentityPools/<pool>/subject/chainguard:<repository-id>:<identity>`, never to the whole pool. To refuse other repositories' tokens outright, also give the provider an attribute condition such as `assertion.sub.startsWith('chainguard:<repository-id>:')`.
- For Chainguard, create an [assumable identity](/platform/administration/assumable-ids/assumable-ids/) in your organization that matches the issuer, the exact subject, and the `exchange_audience`, and bind it to a role that grants the access the check needs.

To find your repository's ID, run `chainctl checks status` with one of its pull requests, such as `acme/app#123`, or with the full SHA of a commit that ran checks after merging. The ID is on the `Repo ID:` line, and in the `repository_id` field of the JSON output. Replace `$ORGANIZATION` with the name of your Chainguard organization:

```sh
chainctl checks status acme/app#123 -o json --parent $ORGANIZATION | jq -r .repository_id
```

Chainguard Checks assigns the ID when it first runs checks on the repository, so open a pull request or push to your default branch before you set up the provider. The ID doesn't change when you rename or transfer the repository. A repository you delete and create again gets a new ID.

## Which runs get an identity {#which-runs-get-an-identity}

Chainguard Checks reads each part of an identity's use from a different place:

| Part | Where Chainguard Checks reads it |
| ---- | -------------------------------- |
| The identity's definition in `identities.yaml` | For a pull request, its base branch, at the commit GitHub merges the pull request into. For a run after merging, your default branch's latest commit. |
| The `trust` section and each identity's `ring` | Your default branch's latest commit, for every pull request. |
| The check's `identity` key, its commands, and its `network.egress` | The commit Chainguard Checks runs, which for a pull request includes the pull request's changes. |
| The check's `when` conditions and its `foreach` entries | The commit Chainguard Checks runs, within the limits in [Change checks in a pull request](/chainguard/checks/github/#change-checks-in-a-pull-request). If the base branch's version of the check uses an identity and has a [`when.expr` condition](/chainguard/checks/configuration/#run-when-an-expression-is-true), on the check or on one of its `foreach` entries, Chainguard Checks reads the check's conditions from the base branch until the pull request merges, and `foreach` entries that the pull request adds don't run. |

A pull request can't add an identity, or widen which checks, branches, or people get one, until it merges. It can change what a check that already gets an identity runs, and which hosts that check can reach. If `identities.yaml` is invalid on the base branch or on your default branch, no check gets an identity until you fix it.

Without a `trust` section on your default branch, a check that requests an identity gets it on every open pull request whose base branch matches the identity's `allow` rule, including drafts and pull requests from forks, whoever opened them. Those pull requests' commands run with the identity's access. Grant a presubmit identity only what an untrusted pull request may do, such as read-only access, or limit which pull requests get it with a `trust` section.

## Limit which pull requests get an identity {#limit-which-pull-requests-get-an-identity}

To give identities only to pull requests opened by people you trust, add a `trust` section to `.chainguard/ci/identities.yaml` on your default branch, and give each identity a `ring`:

```yaml {title=".chainguard/ci/identities.yaml"}
version: 1
trust:
  groups:
    maintainers:
      github:
        user: {octocat: 583231}
    bots:
      github:
        app: {dependabot: 49699333}
  subrings:
    trusted:
      authors: [maintainers, bots]
  github_token: 1.trusted
identities:
  gcs-read:
    ring: 1.trusted
    # ...the rest of the identity's definition
```

With this file, the `gcs-read` identity goes only to pull requests opened by `octocat` or by Dependabot, and to runs after merging.

The `trust` section has the following keys:

| Key | Required | Description |
| --- | -------- | ----------- |
| `groups` | Yes | A map from each group's name to the GitHub accounts in it. Refer to [Groups](#groups). |
| `subrings` | Yes | A map from each subring's name to its `authors`, a list of groups. A pull request meets a subring when the account that opened it is in one of those groups. |
| `github_token` | Yes | The ring for a read-only GitHub token, in the same form as `ring`. During the beta, checks don't get this token, but the key is still required. |
| `cache` | No | Which rings share build caches. Refer to [Set up cache pools](/chainguard/checks/variations-services-caches/#set-up-cache-pools). |

### Rings {#rings}

Chainguard Checks places each run in a *ring*, based on the `trust` section on your default branch:

| Ring | Runs in the ring |
| ---- | ---------------- |
| `2` | Runs after merging, on your default branch. |
| `1.<subring>` | Pull requests opened by an account in one of the subring's `authors` groups, such as `1.trusted` for pull requests that `octocat` or Dependabot opens in the earlier example. |
| `0` | Every other pull request. |

Ring `2` is above every subring, and every subring is above ring `0`. The `trust` section uses rings in the following ways:

- An identity's `ring` is the lowest ring that gets the identity. With `ring: 1.trusted`, pull requests in ring `1.trusted` and runs after merging get it. With `ring: 2`, only runs after merging get it, and with `ring: 0`, every run does, the same as without a `trust` section.
- `github_token` sets the lowest ring that gets a GitHub token, in the same way.
- A [cache pool](/chainguard/checks/variations-services-caches/#set-up-cache-pools) lists the exact rings whose runs share it. A run whose ring isn't in any pool gets no cache.

A ring only narrows an identity's `allow` rules, so a run still needs a matching `allow` rule to get the identity.

Only the account that opened the pull request counts. Who pushed its commits, who reviewed it, and whether its branch is in a fork don't change the result.

Because Chainguard Checks reads the `trust` section and every `ring` from your default branch, a pull request can't change its own trust, even a pull request into another branch. When your default branch has a `trust` section, an identity that its `identities.yaml` doesn't define gets ring `2`, so a pull request into another branch never gets an identity that only that branch defines. Without a `trust` section on your default branch, a pull request into another branch can get an identity that only that branch defines.

When the file has a `trust` section, every identity in it needs a `ring`, and every group must be in at least one subring's `authors`. Without a `trust` section, `ring` is an error. Group and subring names follow the same rules as identity names.

### Groups

Each group has exactly one source under `github`:

| Source | Example | Matches |
| ------ | ------- | ------- |
| `org` | `{github: {org: acme}}` | Members of the GitHub organization. |
| `team` | `{github: {team: acme/maintainers}}` | Members of the team, including members of its child teams. |
| `user` | `{github: {user: {octocat: 583231}}}` | The listed GitHub users. |
| `app` | `{github: {app: {dependabot: 49699333}}}` | Pull requests that the listed GitHub Apps open. |

To trust specific people, list them in a `user` group and pin each one's ID, as in the earlier example. Chainguard Checks reads organization and team members from GitHub through the Chainguard App, and can take up to three minutes to see a change to them.

For `user` and `app`, map each login to its numeric GitHub account ID. Chainguard Checks matches the ID, and the login is only a label. To find a user's ID, run the following command, replacing `$LOGIN` with the user's GitHub login:

```shell
gh api "/users/$LOGIN" --jq .id
```

An app opens pull requests as its bot account, `<slug>[bot]`. To find that account's ID, replace `$SLUG` with the app's slug, such as `dependabot`:

```shell
gh api "/users/$SLUG%5Bbot%5D" --jq .id
```

You can also list logins without IDs, such as `user: [octocat]`. Chainguard Checks then trusts whoever holds each login when it decides, so pin IDs instead.

### When a pull request doesn't get an identity {#when-a-pull-request-doesnt-get-an-identity}

On a pull request that doesn't reach an identity's ring, a check that requests the identity fails before its commands run, and Chainguard Checks doesn't retry it. The check's result on GitHub shows **Could not be executed**, and its output includes the reason, such as the following:

```
trust policy places gcs-read at ring 1.trusted, which this pull request does not reach: its opener is in none of subring trusted's authors groups
```

If the check is blocking, the summary check fails too, with a title such as **1 check(s) could not be executed**.

To keep these failures from blocking pull requests opened by people outside your `trust` section, make the check [advisory](/chainguard/checks/configuration/#advisory-checks), or skip it on those pull requests with a [condition](/chainguard/checks/configuration/#run-when-an-expression-is-true). Once that condition is on the base branch, a pull request's edits to it apply only after the pull request merges, as described in [Which runs get an identity](#which-runs-get-an-identity). A condition still doesn't replace the `trust` section, because a pull request can add a check that an identity's `checks` selectors match, or set `identity` on a check whose base branch version doesn't use one, and give that check conditions of its own. A condition on `context.github.pull_request.head_repository` also skips pull requests that people you trust open from their own forks.

## Revoke access

To take access back, change the place that grants it:

| To stop | Change | When it takes effect |
| ------- | ------ | -------------------- |
| A check from getting an identity | Remove the identity, the check's selector, or the `allow` rule from `identities.yaml` on the base branch, or on your default branch for runs after merging. | New runs, once the change merges. A running check loses the identity within about 10 minutes. |
| Pull requests from some people from getting identities | In the `trust` section on your default branch, remove them from a group, or move identities to a higher ring. | New runs, once the change merges. A running check loses the identity within about 18 minutes. That includes up to three minutes for Chainguard Checks to see a change to an organization's or team's members on GitHub. |
| Every use of an identity, including runs after merging | On the provider, remove the roles granted to the identity's subject, or remove the provider's trust in it, such as by disabling the Google Cloud workload identity pool provider or deleting the Chainguard assumable identity. | The provider refuses new token exchanges. A Google Cloud access token that a running check already has can keep working inside that check until it expires, for up to an hour. |

When a change to `identities.yaml` or to the `trust` section takes an identity from a running check, and the identity has Google Cloud settings, Chainguard Checks stops the check and doesn't retry it. The check's result on GitHub shows **Could not be executed**. A Google Cloud access token that the check already has works only inside the check, so it stops working when the check stops. If the identity has only `chainguard` settings, the check keeps running, but its requests to those Chainguard hosts fail.

Chainguard Workspaces sessions don't use workload identities. To revoke what a session can reach, refer to [Review and revoke a session's credentials](/chainguard/workspaces/credentials/#review-and-revoke-a-sessions-credentials) and [Your Chainguard identity in a session](/chainguard/workspaces/credentials/#your-chainguard-identity-in-a-session).
