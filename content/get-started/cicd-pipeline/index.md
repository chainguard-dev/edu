---
title: "Set up Chainguard in your CI/CD pipeline"
linktitle: "Chainguard in your CI/CD pipeline"
lead: "A map of where each Chainguard product fits in a CI/CD pipeline, in the order you'd encounter it — from setting up access through keeping your images current. Each stage explains what you configure, why it's worth doing, and where the detailed guide lives."
description: "Where each Chainguard product fits in a CI/CD pipeline: hardening the repository, authenticating without long-lived secrets, pulling trusted inputs, building, verifying, gating deploys, and staying current."
type: "article"
date: 2026-09-24T00:00:00+00:00
lastmod: 2026-09-25T13:22:59+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 012
toc: true
---

A CI/CD pipeline touches most of your software supply chain: the code you commit, the credentials your runners hold, the dependencies you pull, the image you build, and the artifact you ship. Chainguard has something to offer at each of those points.

This page walks the whole path in order so you can see how the pieces relate before you start wiring any of them up. It's a map rather than a tutorial. Each stage gives you the one command that anchors it, then links to the guide that covers the details.

You don't have to adopt every stage, and you don't have to adopt them in order. Most organizations start at [Pull trusted inputs](#4-pull-trusted-inputs), because swapping a base image is the smallest change with the largest effect, then work outward from there.

![Vertical flow diagram of a CI/CD pipeline in nine stages, each labeled with the Chainguard products and practices that apply. Stage 0, set up access: Chainguard Console, chainctl, IAM roles. Stage 1, harden the repository: Guardener, Hardened Actions, Commit Verification. Stage 2, authenticate the pipeline: assumable identities, OIDC tokens, setup-chainctl. Stage 3, replace workflow steps: Chainguard Actions, the cg-actions skill, Chainguard Agent Skills. Stage 4, pull trusted inputs: Chainguard Containers, Chainguard Libraries, Chainguard OS packages. Stage 5, build the image: Custom Assembly, Chainguard VMs, Dockerfile migration. Stage 6, verify before shipping: signature verification, SBOMs, SLSA provenance. Stage 7, gate the deploy: admission policies, repository policies. Stage 8, stay current: Digestabot, CloudEvents, security advisories, EOL Grace Period.](cicd-lifecycle.svg)

## 0. Set up access

Before anything else, you need a Chainguard organization, `chainctl` installed and authenticated, and enough permission to create identities and entitlements. Several stages that follow need the `owner` role. Work through [Get started with chainctl](/get-started/getting-started-with-chainctl/) to install the tool, then log in:

```shell
chainctl auth login
```

The [Chainguard Console](/platform/console/) covers the same ground in a browser, and [comparing chainctl to the Console](/platform/chainctl-usage/comparing-chainctl-to-console/) shows which tasks belong to which. To plan who can do what, see [roles and role bindings](/platform/administration/iam-organizations/roles-role-bindings/).

**Why it matters.** Access lives in one place instead of scattered across registry credentials on individual machines. When someone changes teams, you revoke a role binding rather than hunting for keys.

## 1. Harden the repository

Recent supply chain attacks have targeted the workflow file, not the artifact it produces. [Guardener](/chainguard/guardener/) hardens the repository itself through a suite of capabilities you turn on one at a time.

Two of them run through the [Guardener GitHub App](/chainguard/guardener/github/), enabled per repository by a file you commit to `.chainguard/`:

- [Hardened Actions](/chainguard/guardener/github/actions-security/) recommends and migrates your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents, either as non-blocking review comments or as a migration pull request.
- [Commit Verification](/chainguard/guardener/github/commit-verification/) enforces cryptographically signed commits against a policy you control, covering both keyless Sigstore signatures and static keys such as GPG.

A third runs locally rather than through the app:

- [Dockerfile migration](/chainguard/guardener/dockerfile-migration/) converts your Dockerfiles to Chainguard Containers through the `chainctl agent dockerfile` commands.

To install the app and link your Chainguard organization to your GitHub organization, see [getting started with Guardener](/chainguard/guardener/github/getting-started/).

**Why it matters.** An attacker who can edit a workflow already has your secrets. Hardening the repository closes that door before anything reaches your build.

## 2. Authenticate the pipeline

Your pipeline needs credentials to pull from Chainguard, and a long-lived API key stored in repository secrets is the weakest way to supply them. Chainguard uses [assumable identities](/platform/administration/assumable-ids/) instead: your CI job presents the OIDC token its platform already issues, and exchanges it for a short-lived Chainguard token.

On GitHub Actions, the `setup-chainctl` action handles the exchange:

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: chainguard-dev/setup-chainctl@2cddd35a2f120d9973e58094dc6878c93cf58c28 # v0.5.1
    with:
      identity: "<identity-id>"
```

On GitLab, Jenkins, or a shell script, pass the platform's token to `chainctl` directly:

```shell
chainctl auth login \
  --identity="$IDENTITY_ID" \
  --identity-token="$OIDC_TOKEN"
```

[Automating with chainctl](/platform/chainctl-usage/automating-chainctl/) covers non-interactive use, and the [identity examples](/platform/administration/assumable-ids/identity-examples/) include worked setups for GitHub, GitLab, and several cloud providers.

**Why it matters.** There's no long-lived credential to leak, rotate, or track. A token that shows up in a build log has already expired by the time anyone reads it.

## 3. Replace workflow steps

[Chainguard Actions](/chainguard/actions/overview/) are hardened drop-in replacements for popular GitHub Actions. Each one keeps the same inputs and outputs as the upstream version, so migrating a step means changing the `uses:` line and nothing else.

Enable the entitlement for your organization:

```shell
chainctl actions entitlements create
```

Then point each step at its hardened equivalent, pinned to a commit digest:

```yaml
- uses: chainguard-actions/tj-actions-changed-files@<commit-sha> # v47
```

Repository names in `chainguard-actions` carry the upstream organization as a prefix, so `tj-actions/changed-files` becomes `tj-actions-changed-files`. Run `chainctl actions discover` to list every action and container image your workflows reference, which tells you what there is to migrate. If your GitHub organization restricts which actions can run, add `chainguard-actions/*` to the allowed patterns first.

You don't have to make these edits by hand. Two tools do the migration for you, and which one fits depends on how much you're moving at once:

- [Hardened Actions](/chainguard/guardener/github/actions-security/), through the Guardener GitHub App described in stage 1, inventories the actions in use across your organization and opens migration pull requests on a schedule. You can also trigger a run [on demand](/chainguard/guardener/github/actions-security/#run-an-on-demand-migration) with `chainctl guardener github migrate create`. Use this for a centralized, organization-wide rollout.
- [cg-actions](https://github.com/chainguard-dev/cg-skills/tree/main/skills/cg-actions), a Claude Code skill, audits one repository's Actions usage and opens a pull request swapping in the hardened equivalents. Use this for a pilot, or where installing an app across the organization isn't an option.

Separately, if agents run anywhere in your pipeline, [Chainguard Agent Skills](/chainguard/agent-skills/overview/) applies the same hardening idea to the skills those agents load.

**Why it matters.** Migration is a one-line change per step, and it removes whole classes of attack — tag hijacking, `pull_request_target` abuse, and secret exfiltration — without changing what your workflow does.

## 4. Pull trusted inputs

This is where most teams start. Point your builds at Chainguard for the three kinds of input a pipeline pulls:

- **Container images.** Authenticate to `cgr.dev` and pull from your organization's namespace. See [authenticating to the registry](/chainguard/containers/registry/authenticating/).

  ```shell
  chainctl auth configure-docker
  ```

- **Language dependencies.** [Chainguard Libraries](/chainguard/libraries/introduction/overview/) rebuilds Java, Python, and JavaScript packages from source, and they're drop-in replacements for what you'd pull from Maven Central, PyPI, or npm. Configure your package manager with `chainctl auth configure-npm` or the equivalent for your ecosystem, then follow the [quickstart](/chainguard/libraries/introduction/quickstart/).

- **System packages.** [Chainguard OS packages](/chainguard/chainguard-os/chainguard-os-packages/) are the APK packages the container images are assembled from, available when you need to install something at build time.

All of these are served through the [Chainguard Repository](/chainguard/chainguard-repository/overview/), which is also where you set the policies that govern what your organization is allowed to pull.

**Why it matters.** Remediation happens upstream of your build. When a CVE is fixed, your next build inherits the fix instead of your team opening a ticket to chase it.

## 5. Build the image

Build your application on a Chainguard base image, using the `-dev` variant for the build stage and the minimal runtime variant for the final stage. [Migrating to Chainguard Containers](/chainguard/containers/migration/migrations-overview/) covers the patterns, and the [Dockerfile conversion tool](/chainguard/containers/migration/migration-tools/dockerfile-conversion/) does the mechanical part.

When your runtime image needs packages the standard image doesn't carry, [Custom Assembly](/chainguard/containers/custom-assembly/overview/) builds a variant to your specification. You can trigger those builds from CI:

```shell
chainctl images repos build apply --file custom-jre.yaml \
  --parent <organization> \
  --repo <image-name> \
  --yes
```

[Triggering builds in CI/CD workflows](/chainguard/containers/custom-assembly/custom-assembly-gitops/) shows the full GitOps pattern. If you ship virtual-machine images rather than containers, [Chainguard VMs](/chainguard/vms/overview/) applies the same approach to VM base images.

**Why it matters.** You maintain your application layer and Chainguard maintains everything underneath it. That's the difference between patching a distribution's backlog and shipping your own code.

## 6. Verify before you ship

Every Chainguard container image and library ships with a signed SBOM and provenance attestation. Verifying them in CI turns those signatures into a gate rather than a document nobody reads.

Check an image signature with `cosign`:

```shell
cosign verify \
  --certificate-oidc-issuer=https://issuer.enforce.dev \
  --certificate-identity-regexp="https://issuer.enforce.dev/<organization-id>/.*" \
  cgr.dev/<organization>/<image-name>:latest
```

See [verifying signatures with cosign](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/) for what the command proves, and [retrieving image SBOMs](/chainguard/containers/security-and-compliance/retrieve-image-sboms/) for pulling the SBOM itself. For dependencies, `chainctl libraries verify` reports which of your artifacts Chainguard built; [verifying Chainguard Libraries](/chainguard/libraries/policies-and-security/verification/) covers the detail.

**Why it matters.** The evidence an auditor asks for is generated by the pipeline that shipped the artifact, not reconstructed from memory months later.

## 7. Gate the deploy

Verification in CI only covers what went through CI. An admission controller enforces the same rules at the cluster boundary, so an image that skipped your pipeline can't run. Chainguard documents policies for both [Kyverno](/chainguard/containers/security-and-compliance/enforcement/kyverno/) and [OPA Gatekeeper](/chainguard/containers/security-and-compliance/enforcement/opa-gatekeeper/).

Further upstream, [container policies](/chainguard/chainguard-repository/container-policies/) and [library policies](/chainguard/chainguard-repository/library-policies/) in the Chainguard Repository govern what your organization can pull in the first place.

**Why it matters.** The guarantee holds at runtime, not only at build time. Policy catches the deployment that bypassed the pipeline, which is the one you'd otherwise never hear about.

## 8. Stay current

Chainguard rebuilds images continuously, so the value of a low-CVE image depends on how quickly you pick up the new digest. Automate that:

- [Digestabot](/chainguard/containers/security-and-compliance/updating-containers/digestabot/) opens pull requests that bump pinned digests to the current build.
- [Renovate](/chainguard/containers/security-and-compliance/updating-containers/renovate/) and [Dependabot](/chainguard/containers/security-and-compliance/updating-containers/dependabot/) handle the same job if you already run them.
- [CloudEvents](/platform/administration/cloudevents/) notify your systems when a new image is pushed, so you can trigger a rebuild rather than poll for one.

Track what's changing with [security advisories](/chainguard/containers/security-and-compliance/security-advisories/) and the [changelog](/chainguard/changelog/). When an image version approaches end of life, the End-of-Life Grace Period gives you a defined window to migrate; see [considerations for image updates](/chainguard/containers/security-and-compliance/updating-containers/considerations-for-image-updates/).

**Why it matters.** Pinning a digest and walking away turns a current image into a stale one. Automating the bump is what keeps "low CVE" true next quarter instead of only on the day you adopted it.

## Next steps

- Bringing engineers onto an organization that's already adopted Chainguard? See [Onboard your teams](/get-started/onboard-your-teams/).
- Ready to pull your first image? Work through a [language- or service-specific example](/get-started/containers-examples/).
- Moving existing workloads over? Step through the [migration guides](/get-started/migration/).
- Want the background on CI/CD attacks these stages defend against? Watch [Securing CI/CD with Chainguard](/software-security/learning-labs/ll202604/).
