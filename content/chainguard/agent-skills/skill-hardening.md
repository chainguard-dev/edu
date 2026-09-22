---
title: "Getting started with skill hardening"
linktitle: "Skill hardening"
description: "Upload an agent skill for hardening, track the job, browse results in user folders, and review the report before installing the skill."
type: "article"
date: 2026-09-22
lastmod: 2026-09-22
draft: false
tags: ["Agent Skills", "Getting Started", "chainctl"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 005
---

Use `chainctl skills harden` to upload an agent skill, submit it for server-side hardening, and download the result with a report of the changes and scanner findings. You can submit a local directory or harden an artifact you have already pushed to your organization's uploads registry.

This guide builds on [Getting started with the Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/), covering hardening and job tracking before you install the skill.

{{< beta feature="Chainguard Agent Skills" >}}

## Prerequisites

You need:

- An [installed and authenticated `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) that includes `skills harden` and `skills status`.
- An organization with a Skills entitlement and accepted Skills terms.
- Permission to upload skills, submit and read hardening jobs, and pull the results.

Check that your version includes the commands:

```shell
chainctl skills harden --help
chainctl skills status --help
```

The `harden` help should show `--folder`, `--digest`, `--wait`, and `--timeout`. If it shows only the generic `skills` help, [update `chainctl`](/platform/chainctl-usage/chainctl-version-update/).

Set the following variables for your organization. The examples use the production registries. `$ORG` can be your organization's name or UIDP (its unique identifier).

```shell
export ORG='your-organization'
export UPLOADS_HOST='uploads.cgr.dev'
```

If onboarding is not already complete, an organization administrator with `skills.entitlements.create` and `terms.accept` permissions runs:

```shell
chainctl skills entitlements create --parent "$ORG"
chainctl skills accept-terms --group "$ORG"
```

Review and accept the terms in the interactive prompt. To check whether the organization already has an entitlement, run:

```shell
chainctl skills entitlements list --parent "$ORG"
```

An entitlement enables access to the service. Its presence does not indicate that a skill has been uploaded or hardened.

## Create and validate an example skill

Create a small skill that produces a release checklist:

```shell
mkdir harden-demo
cat > harden-demo/SKILL.md <<'EOF'
---
name: harden-demo
description: Write a short release checklist when the user asks to prepare a software release.
license: Apache-2.0
---

Ask the user for the project name and intended release version if either is missing.
Return a checklist covering tests, release notes, and the release owner.
Use only information provided by the user. Mark missing details as "to confirm".
EOF

chainctl skills validate ./harden-demo
```

The directory name must match the frontmatter `name`. Keep the directory within the 10 MB limit. Validation checks the skill's structure locally; the hardening pipeline performs the subsequent review and evaluation.

## Harden a local directory

From the directory containing `harden-demo`, run:

```shell
chainctl skills harden ./harden-demo --group "$ORG" --wait --timeout 30m
```

The command packages and uploads the directory, submits a hardening job, prints its ID, and waits for completion. `--folder ./harden-demo` is equivalent to the positional directory argument. A separate `skills push` is unnecessary for this workflow.

On success, the command prints the hardened artifact's reference and digest and downloads it into `./hardened/harden-demo/`. The download includes `SKILL.md`, any supporting files, and `HARDENING.md` with the hardening report and findings.

The hardened artifact is published under the submitting user's namespace:

```text
skills.cgr.dev/<org-uidp>/users/<user-namespace>/harden-demo@sha256:<digest>
```

The service generates the user namespace. Save the exact reference returned by the command, including `users/<user-namespace>/` and the digest, for subsequent pulls or installs.

## Submit now and check later

Omit `--wait` to return after submission. Use `-o id` to capture the job ID:

```shell
JOB_ID=$(chainctl skills harden ./harden-demo --group "$ORG" -o id)
chainctl skills status --group "$ORG" --id "$JOB_ID"
```

To resume waiting and download the result:

```shell
chainctl skills status --group "$ORG" --id "$JOB_ID" --wait --timeout 30m
```

`--id` takes the 64-character job ID, without a `sha256:` prefix or an operation path. Repeating a submission with the same organization, user, skill name, and content digest returns the same job. Use `status` when you only need to check progress.

`--timeout` requires `--wait` and bounds the waiting command, including its other work. A timeout or <kbd>Ctrl-C</kbd> stops the local command; it does not cancel the server-side job. Resume with the saved ID. A pipeline failure exits nonzero and prints its failure reason.

## Harden an existing upload

You can also push a tagged artifact first and then explicitly request hardening:

```shell
chainctl skills push ./harden-demo --group "$ORG" --tag v1.0.0
chainctl skills describe "$UPLOADS_HOST/$ORG/harden-demo:v1.0.0"

chainctl skills harden "$UPLOADS_HOST/$ORG/harden-demo:v1.0.0" \
  --group "$ORG" --wait --timeout 30m
```

`push` stores the original artifact in `uploads.cgr.dev`. Use `harden` to submit it for hardening and `status` to track the job. A successful push does not mean that a hardened result is available in `skills.cgr.dev`.

The upload must be in the same organization passed to `--group`. This command accepts a reference at `<uploads-host>/<org>/<skill-name>`; use the organization root when pushing an artifact you intend to harden this way.

To select the exact artifact from the push output, use its digest instead:

```shell
chainctl skills harden --group "$ORG" --name harden-demo \
  --digest 'sha256:<64-hex-digest-from-push>' --wait --timeout 30m
```

`--digest` requires `--name` and takes only the digest, not a tag or full registry reference. Choose one input form per invocation: a path, `--folder`, an uploads reference, or `--digest` with `--name`.

## Browse results in user folders

### Why do I only see a `users` folder?

By default, `chainctl skills list` reads the hardened registry (`--source skills`) and shows only the immediate folders and skills at the selected level. For example:

```shell
chainctl skills list --group "$ORG"
```

```output
     SOURCE     |  TYPE  | NAME  | LATEST TAG | UPDATED
----------------|--------|-------|------------|---------
 skills.cgr.dev | folder | users | --         | --
```

`users` is a registry folder containing namespaces for users who submit skills for hardening. A row with `TYPE` set to `folder` has no skill tag or update time, so those columns show `--`. The folder row alone does not tell you whether a hardening job has completed or whether your skill is inside it.

Hardened results are organized like this:

```text
skills.cgr.dev/<org-uidp>/
└── users/
    └── <user-namespace>/
        └── harden-demo
```

Each submitting user has a separate namespace, so different users can harden a skill with the same name without sharing a repository path.

### Expand all user folders

Add `--recursive` (or `-r`) to include skills from every nested folder in the listing:

```shell
chainctl skills list --group "$ORG" --source skills --recursive
```

For skills included in the listing, the `NAME` column shows the full path relative to the organization, such as `users/<user-namespace>/harden-demo`. Repeating the default non-recursive command continues to show only the top-level folder.

**Listing limitation:** `skills list` currently includes skill rows only for repositories with a `latest` tag. `--recursive` expands the folders but does not remove this filter. A completed hardening job can be available by its returned digest reference and still be absent from the listing. See [Find a skill that is missing from the listing](#find-a-skill-that-is-missing-from-the-listing).

To browse one level at a time, append the registry folder path to `--group`:

```shell
chainctl skills list --group "$ORG/users"
chainctl skills list --group "$ORG/users/<user-namespace>"
```

Replace `<user-namespace>` with a folder name returned by the first command. These paths select registry folders; they do not refer to directories on your machine.

### Find a skill after pushing it

If `push` returned an `uploads.cgr.dev` reference, select the uploads source to browse that registry:

```shell
chainctl skills list --group "$ORG" --source uploads --recursive
```

To browse uploads and hardened results in one listing:

```shell
chainctl skills list --group "$ORG" --source all --recursive
```

Use the `SOURCE` column to distinguish the registries:

| Source option | Registry | Contents |
| --- | --- | --- |
| `--source skills` (default) | `skills.cgr.dev` | Hardened skills with a `latest` tag, including skills in user namespaces. |
| `--source uploads` | `uploads.cgr.dev` | Original uploads with a `latest` tag. |
| `--source all` | Both registries | Skills with a `latest` tag from either source, labeled by registry. |

If you have only run `push`, follow [Harden an existing upload](#harden-an-existing-upload). If you already submitted a hardening job, use `chainctl skills status --group "$ORG" --id "$JOB_ID"` to check it. An entitlement listing or a `users` folder row is not a job status check.

### Find a skill that is missing from the listing

An upload pushed only with `--tag v0.1.0` or `--tag v1.0.0` has no `latest` tag. A hardened result may also have a digest or generated version tag without `latest`. These artifacts can be pulled by their exact references even though `list` omits them. Changing `--source` does not remove the `latest` filter.

For an upload, inspect the full reference from the `push` output:

```shell
chainctl skills describe "$UPLOADS_HOST/$ORG/harden-demo:v1.0.0"
```

For a hardening job, use `status` and save the returned hardened reference as described in [Review and install the result](#review-and-install-the-result). Use that reference for `describe`, `pull`, or `install`; an empty listing does not mean the job failed.

If you want a tagged upload to appear in `list`, you can publish it with both a version tag and `latest`:

```shell
chainctl skills push ./harden-demo --group "$ORG" --tag v1.0.0 --tag latest
chainctl skills list --group "$ORG" --source uploads
```

Both tags point to the same uploaded artifact. This updates the upload's `latest` tag; it does not add a `latest` tag to the separate hardened result.

## Review and install the result

Read `hardened/harden-demo/HARDENING.md` for the change summary and findings, including findings that remain open. Review the resulting instructions before using the skill. A successful hardening job can still have remaining findings.

Copy the full hardened reference printed by `harden` or `status`:

```shell
export HARDENED_REF='<full-hardened-reference-including-@sha256:digest>'
chainctl skills describe "$HARDENED_REF"
chainctl skills install "$HARDENED_REF"
```

`install` detects your local agents and reports where it placed the skill. Use the installed name and location shown by the command to load it in your agent, then ask it to prepare a release checklist for a test project.

If `./hardened/harden-demo/` already contains a previous download, `--wait` will not overwrite it. Check `status` without `--wait`, then pull the returned reference into a new directory:

```shell
chainctl skills pull "$HARDENED_REF" ./harden-demo-reviewed
```
