---
title : "Chainguard Enforce Changelog"
description: "Chainguard Enforce Changelog"
type: "article"
date: 2023-04-24 22:04:02 +0000 UTC
draft: false
tags: ["Enforce", "Reference", "Product"]
images: []
weight: 799
---

## Introduction
Any customer facing changes to Chainguard Enforce or [`chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) are highlighted in the following notes. Any new features, bug fixes, or general ease of use improvements will be listed under the corresponding release version.

### v0.1.107
Release date: 2023-04-24

Customer facing changes: N/A

### v0.1.106
Release date: 2023-04-20

Customer facing changes: N/A

### v0.1.105
Release date: 2023-04-20
#### Bug or Regression
- Fix the registry hostname in chainctl


### v0.1.104
Release date: 2023-04-19
#### Other (Cleanup or Flake)
- Drop support for registry.enforce.dev
#### Uncategorized
- chainctl recognizes Buildkite ambient credentials

### v0.1.103
Release date: 2023-04-18
#### Documentation
- Add section to Enforce Events page explaining how UIDPs are generated
- Add section to Enforce Events page explaining how to validate `iss` and `sub` fields in Authorization header tokens


### v0.1.102
Release date: 2023-04-17
#### Feature
- Manage cloud accounts associated with groups with `chainctl iam account-associations`


### v0.1.101
Release date: 2023-04-14

Customer facing changes: N/A

### v0.1.100
Release date: 2023-04-13
#### Feature
- deprecates the `default.identity-provider` configuration in for social login (Github, Gitlab and Google). Users should now set `default.social-login`. `default-identity-provider` now configures default custom identity provider for authentication (i.e to replace using the `--identity-provider` flag with `chainctl auth login`)
#### Bug or Regression
- Management of assumable identities with chainctl has been moved from `chainctl auth identities` to `chainctl iam identities`.
- fix bug in `chainctl auth login` when using the depreciated config `default.identity-provider = "google"`.


### v0.1.99
Release date: 2023-04-11

Customer facing changes: N/A

### v0.1.98
Release date: 2023-04-10

Customer facing changes: N/A

### v0.1.97
Release date: 2023-04-10
#### Feature
- API to support custom claim exact matches in ClaimMatch identity
- Add support to authenticate with customer managed identity providers using `chainctl auth login --identity-provider=foo`
- Cluster registration for agentful installation will now persist agent installation options.
- Introduce a new service principal identity type, which only the named Chainguard service can assume.
- Introduce the ability to create Chainguard account associations to authorize service principal identities to act on user Chainguard resources explicitly.
- chainctl can now manage identity providers via `chainct iam identity-providers {create,list,update,delete}`
#### Bug or Regression
- Fix invite codes with custom identity provider


### v0.1.96
Release date: 2023-04-03

Customer facing changes: N/A

### v0.1.95
Release date: 2023-03-29
#### Other (Cleanup or Flake)
- Add contact link to quota error message so users know how to reach out


### v0.1.94
Release date: 2023-03-28
#### Other (Cleanup or Flake)
- Add contact link to quota error message so users know how to reach out


### v0.1.93
Release date: 2023-03-28
#### Feature
- https://github.com/chainguard-dev/customer-issues/issues/37
#### Bug or Regression
- Specify a custom audience claim when creating a GitHub identity with the `--github-audience` flag.
- chainctl should default to preferring ambient credentials when re-assuming an identity after it's current token expires in long-running workflows.


### v0.1.92
Release date: 2023-03-24
#### Bug or Regression
- Have the cgr credential helper prefer ambient auth when fetching credentials.


### v0.1.91
Release date: 2023-03-23

Customer facing changes: N/A

### v0.1.90
Release date: 2023-03-23

Customer facing changes: N/A

### v0.1.89
Release date: 2023-03-22

Customer facing changes: N/A

### v0.1.88
Release date: 2023-03-21

Customer facing changes: N/A

### v0.1.87
Release date: 2023-03-20
#### Feature
- Registry events will now store the friendly name in Repository and the UIDP in RepoID.


### v0.1.86
Release date: 2023-03-16

Customer facing changes: N/A

### v0.1.85
Release date: 2023-03-15

Customer facing changes: N/A

### v0.1.84
Release date: 2023-03-13
#### Feature
- Manage role-bindings with `chainctl iam role-bindings create` and `chainctl iam role-bindings update`.
- SBOM + Attestation ingestion failures now populate in Record status.


### v0.1.83
Release date: 2023-03-09
#### Feature
- SBOM + Attestation ingestion failures now populate in Record status.
- View gRPC requests and responses by passing `-v=2` or larger.


### v0.1.82
Release date: 2023-03-07

Customer facing changes: N/A

### v0.1.81
Release date: 2023-03-07
#### Other
- make `client_secret` field of identity provider terraform resource sensitive (masked in terraform output)
#### Feature
- Disable color in `chainctl` by setting the `NO_COLOR` environment variable.


### v0.1.80
Release date: 2023-03-01

Customer facing changes: N/A

### v0.1.79
Release date: 2023-02-28
#### Feature
- Automatically bind an identity to a role at creation time with the --role flag.
- Create and manage identities with `chainctl auth identities` commands.
- Introduce a new chainguard_group_invite resource to our terraform provider, which enables the creation and management of invite codes as *sensitive* TF state.
#### Bug or Regression
- Fixes an issue where some workload contexts show up as having an Unknown kind after installation.


### v0.1.78
Release date: 2023-02-23

Customer facing changes: N/A

### v0.1.77
Release date: 2023-02-22
#### Bug or Regression
- fix a bug where continuous verification improperly filtered workloads when no `match` block was specified.


### v0.1.76
Release date: 2023-02-17
#### Feature
- Validate AWS Account ID when setting up Account Assocations and fail early if invalid
- add CV support for evaluating workloads with policies using `include*`
#### Bug or Regression
- surface clearer error messages when assuming an identity fails because of mismatched claims.


### v0.1.75
Release date: 2023-02-15
#### Bug or Regression
- chainctl now properly uses the --identity-token in environments with ambient credentials


### v0.1.74
Release date: 2023-02-14
#### Feature
- chainctl now supports detecting ambient credentials when they are mounted in the path: /var/run/chainguard/chainctl/oidc-token
#### Bug or Regression
- Fix the eksctl command returned by discovery to drop the --account argument
- chainctl now properly uses the --identity-token in environments with ambient credentials


### v0.1.73
Release date: 2023-02-14

Customer facing changes: N/A

### v0.1.72
Release date: 2023-02-13

Customer facing changes: N/A

### v0.1.71
Release date: 2023-02-10
#### Bug or Regression
- Fix our SBOM attestation ingestion to support attestations without the cosign "envelope".

### v0.1.70
Release date: 2023-02-09

Customer facing changes: N/A

### v0.1.69
Release date: 2023-02-09

Customer facing changes: N/A

### v0.1.68
Release date: 2023-02-08
#### API Change
- Expose new customer managed identity provider API
#### Feature
- Now when chainctl refreshes auth it will default to the subject of the pre-existing token when --identity isn't passed.


### v0.1.67
Release date: 2023-02-07
#### Feature
- Filter policies and cluster records to a specific image with the `--image` flag.
- chainctl can now detect when it is running in a github actions environment when assuming an identity via chainctl auth login --identity {ID}
- add support for precreating identities that can be assumed by more than one identity.
#### Other (Cleanup or Flake)
- match upstream workload selector logic and add tests
- TrustRoot support for the definition of certificate and timestamp authorities and TUF remote references.
- Error when policies contain unknown fields
- Support to reference policies via an URL or a ConfigMap. This is especially important when the size of the policy is big.
- Fix private multi-arch fetchConfigFile
- Add support for TSA image verification
- Add support to ignore SCT verification on keyless authorities
- Improve kms key validations and error messages for awskms


### v0.1.66
Release date: 2023-02-06

Customer facing changes: N/A

### v0.1.65
Release date: 2023-02-06
#### Feature
- chainctl: add sigstore ca describe command
- Users can now remove rolebinding using `chainctl iam rolebinding delete`
- chainctl now supports policy versioning! Updating or editing a policy creates a new version. Interact with policy versions using `chainctl policy versions` commands `list`, `view` and `activate`.
- terraform provider now support managing Enforce Signing certificate authorities with the `chainguard_sigstore` resource
- Surface a new Identities API and chainguard_identity terraform rule.
#### Other (Cleanup or Flake)
- RoleBinding deletion is now "hard", which avoids a problem where deleted rolebindings could not be recreated.
- chainctl will no longer detect google credentials automatically unless it is in STS mode for the agent, or assuming an identity.
#### Uncategorized
- Set the User-Agent for webhooks to `Chainguard Enforce {commit}`.


### v0.1.64
Release date: 2023-01-26
#### Uncategorized
- Fix terraform provider bug which set account association to default name "tbd"

### v0.1.63
Release date: 2023-01-25

Customer facing changes: N/A

### v0.1.62
Release date: 2023-01-24

Customer facing changes: N/A

### v0.1.61
Release date: 2023-01-23
#### Feature
- Add `--headless` flag to `chainctl auth` for logins on headless instances, and to bypass cloud provider metadata endpoints.
- Add support for cluster location affinity in the terraform provider.
- New configuration values `default.group` and `default.active-within` are available for commands that offer a `--group` or `--active-within` filter flag, respectively. Explicitly provided flags override any default value. `default.identity-provider` can be used to bypass the identity provider selection screen when logging in to `chainctl`.
#### Bug or Regression
- role binding IDs will now use our standard UIDP path shape like other resources, and be rooted under the Group resource it pertains to.  We will (soon) replace all existing RoleBindings with equivalent versions that adhere to this pattern.  These should not require any user action, or have any user-facing impact other than things getting the new ID shape.


### v0.1.60
Release date: 2023-01-19
#### Feature
- terraform-provider now supports profiles for agentless clusters and updating name and cluster description


### v0.1.59
Release date: 2023-01-18

Customer facing changes: N/A

### v0.1.58
Release date: 2023-01-18

Customer facing changes: N/A

### v0.1.57
Release date: 2023-01-18

Customer facing changes: N/A

### v0.1.56
Release date: 2023-01-18
#### Feature
- Add support for AWS AppRunner services to cluster discovery.
- Agentless discovery will now attempt to create an SQS queue subscribing to the audit log SNS topic in the region the cluster lives within.


### v0.1.55
Release date: 2023-01-17

Customer facing changes: N/A

### v0.1.54
Release date: 2023-01-17
#### Bug or Regression
- fix an issue where cluster discovery for GCP would return 403s when it encounters inactive projects


### v0.1.53
Release date: 2023-01-13
#### Feature
- Set/unset individual configuration properties with `chainctl config set` and `chainctl config unset`.
- Terraform provider now supports cluster discover via the `chainguard_cluster_discovery` data source


### v0.1.52
Release date: 2023-01-11
#### Feature
- OCI file media type of `text/spdx+json` is recognized as SPDX+json SBOM
- SBOMs are ingested by default for all applicable images


### v0.1.51
Release date: 2023-01-10
#### Feature
- We will now observe and model Tekton resources, when they are installed.
- terraform-provider now default's to the enforce.dev production environment instead of the decomissioned guak.dev environment
- non-Kubernetes GCP runtimes can now take advantage of GCP audit logs to react in near real-time to deployment events (similar to Kubernetes informers).  This needs the latest release of https://github.com/chainguard-dev/terraform-google-chainguard-account-association to be applied.


### v0.1.50
Release date: 2023-01-06
#### Feature
- Agent-based cluster installation now surfaces cluster created events (like agentless installs)
- Allow customers coming from gitlab to to authorize with Chainguard APIs until gitlab supports customizing the audience claim.
- `chainctl` notifies the user when there is a an update available.


### v0.1.49
Release date: 2023-01-05

Customer facing changes: N/A

### v0.1.48
Release date: 2023-01-05

Customer facing changes: N/A

### v0.1.47
Release date: 2023-01-03
#### Feature
- Introduce a "chainctl cluster discover" command for automatically discovering (and enrolling) clusters.
- Search for packages within your clusters with `chainctl cluster search`
#### Bug or Regression
- Fix authentication for fetchConfigFile with private images (multi-arch images are still broken pending an upstream fix)
- image references should now use a consistently normalized form with a hostname and no tag.  DockerHub references will always get prefixed with index.docker.io (even if written without a host, or with docker.io), and "official" images will have the prefix: index.docker.io/library.  Tags will be stripped, even if specified alongside a digest.  For example, ubuntu:latest@sha256:deadbeef will become: index.docker.io/library/ubuntu@sha256:deadbeef


### v0.1.46
Release date: 2022-12-16

Customer facing changes: N/A

### v0.1.45
Release date: 2022-12-15

Customer facing changes: N/A

### v0.1.44
Release date: 2022-12-14
#### Feature
- Enforce will now detect Knative resource types, if they are installed, and model them in our resource hierarchy.


### v0.1.43
Release date: 2022-12-13

Customer facing changes: N/A

### v0.1.42
Release date: 2022-12-12

Customer facing changes: N/A

### v0.1.41
Release date: 2022-12-12

Customer facing changes: N/A

### v0.1.40
Release date: 2022-12-12
#### Documentation
- generate a release changelog for Enforce and `chainctl` changes, accessible at [https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/changelog/](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/changelog/)
#### Bug or Regression
- Bugfix: allow rerunning of `chainctl cluster install --private`
#### Other (Cleanup or Flake)
- Activity in chainctl will now show up as monitor -> observer, and policy -> enforcer


### v0.1.39
Release date: 2022-12-05
#### Other (Cleanup or Flake)
- agent-based installations may now specify --name and --description during their initial registration.
- declarative installations may now specify cluster name/description by adding the keys cluster-{name,description} to mcp-creds.

### v0.1.38
Release date: 2022-12-01
#### Feature
- The meta reconciliation processes which are spun up by our agents are now HA with keys distributed evenly across the statefulset's replicas.
#### Other (Cleanup or Flake)
- agentless tenants will no longer create a gulfstream namespace for their UID, preferring instead kube-system for establishing cluster identity.
- chainctl now groups cluster activity by a clearer "profile" descriptor, e.g. "policy" and "monitor" (Caveat: these names may change a bit as we finalize things)


### v0.1.37
Release date: 2022-11-29
#### Feature
- Agentless no longer creates CRDs to program itself.
#### Bug or Regression
- Fix an issue where agentless will overwrite user modifications to configmaps.
- Fixes an issue where some distributed policies were getting starved during Continuous Verification due to re-evaluation and throttling.


### v0.1.36
Release date: 2022-11-22

Customer facing changes: N/A

### v0.1.35
Release date: 2022-11-22
#### Bug or Regression
- Fix a bug in our image discovery where RecordContext LastSeen timestamps were updated without updating the ExistenceRecord's LastSeen timestamp.
#### Other (Cleanup or Flake)
- Agentless no longer installs [Cluster]Role[Binding]s since it authenticates via IAM

### v0.1.34
Release date: 2022-11-19

Customer facing changes: N/A

### v0.1.33
Release date: 2022-11-19

Customer facing changes: N/A

### v0.1.32
Release date: 2022-11-19

Customer facing changes: N/A

### v0.1.31
Release date: 2022-11-18
#### Other (Cleanup or Flake)
- Policy events will now only contain entries for changed results.


### v0.1.30
Release date: 2022-11-17
#### Feature
- Log out of the Chainguard platform with `chainctl auth logout`.
- Policy updates now trigger revalidation in continuous verification
#### Other (Cleanup or Flake)
- Customers on older versions of chainctl will need to upgrade, and possible upgrade their agent for things like Workload to continue to show up properly in chainctl and the UI.
- `chainctl iam groups describe` now supports filtering cluster records with `--active-within`.

### v0.1.28
Release date: 2022-11-17

Customer facing changes: N/A

### v0.1.27
Release date: 2022-11-16
#### Feature
- Document Enforce emitted cloudevents including HTTP headers. Available at https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-enforce-events
- Introduce a new "chainctl cluster workloads ls" command for visualizing the workloads running in a cluster or namespace.


### v0.1.26
Release date: 2022-11-14
#### Other (Cleanup or Flake)
- chainctl cluster records ls now distinguishes "mode: warn" policies from "mode: enforce"
- We no longer embed signatures/attestations in the existence records API, e.g. chainctl cluster records ls -ojson


### v0.1.25
Release date: 2022-11-10
#### Feature
- Get information about the policies, images, and packages running on a cluster with `chainctl cluster describe`.
- (staging-only) chainops.dev issued OIDC tokens will now start returning a new `upstream` claim, which contains an encrypted version of the incoming OIDC for use in downstream components.


### v0.1.24
Release date: 2022-11-08
- Adds new `upstream` claim in Chainguard issued OIDC tokens, which includes encrypted data identifying the upstream user the token is being issued for.


### v0.1.23
Release date: 2022-11-07

Customer facing changes: N/A

### v0.1.22
Release date: 2022-11-04
#### Feature
- "chainctl cluster install" no longer pins to the version of the agent embedded in the CLI, but fetches the latest programming from a new API.


### v0.1.21
Release date: 2022-11-03

Customer facing changes: N/A

### v0.1.20
Release date: 2022-11-03
#### Feature
- Start to emit a new dev.chainguard.admission.namespace.v1 event when the policy status on a namespace changes.
- `chainctl cluster uninstall` asks the user for confirmation before continuing. Bypass interactive mode by passing the `--yes` flag.
#### Other (Cleanup or Flake)
- `chainctl cluster uninstall` now accepts `--yes`


### v0.1.19
Release date: 2022-11-02
#### Other (Cleanup or Flake)
- When choosing from a list of resources (e.g. clusters, groups), chainctl will proceed automatically if only a single resource is available.

### v0.1.18
Release date: 2022-11-01
#### Feature
- Added Chainguard Enforce to the AWS Marketplace
- Remove AWS and GCP account associations with `chainctl iam groups remove-aws` and `remove-gcp`, respectively.
#### Other (Cleanup or Flake)
- `chainctl cluster uninstall` accepts filtering with `--group` when uninstalling active clusters; a cluster is only uninstalled if it belongs to the given group or a descendant.

### v0.1.17
Release date: 2022-10-31

Customer facing changes: N/A

### v0.1.16
Release date: 2022-10-31
#### Feature
- `chainctl cluster records list` accepts cluster names in addition to IDs.
- chainctl attempts to authenticate with OAuth2 device flow in terminals without access to a browser.


### v0.1.15
Release date: 2022-10-24

Customer facing changes: N/A

### v0.1.14
Release date: 2022-10-21

Customer facing changes: N/A

### v0.1.13
Release date: 2022-10-20

Customer facing changes: N/A

### v0.1.12
Release date: 2022-10-18

Customer facing changes: N/A

### v0.1.11
Release date: 2022-10-17

Customer facing changes: N/A

### v0.1.10
Release date: 2022-10-13
#### Feature
- Update chainctl directly with `chainctl update`


### v0.1.9
Release date: 2022-10-12

Customer facing changes: N/A

### v0.1.8
Release date: 2022-10-11

Customer facing changes: N/A

### v0.1.7
Release date: 2022-09-29

Customer facing changes: N/A

### v0.1.6
Release date: 2022-09-28

Customer facing changes: N/A

### v0.1.5
Release date: 2022-09-27

Customer facing changes: N/A

### v0.1.4
Release date: 2022-09-26

Customer facing changes: N/A

### v0.1.3
Release date: 2022-09-23

Customer facing changes: N/A

### v0.1.2
Release date: 2022-09-23

Customer facing changes: N/A

### v0.1.1
Release date: 2022-09-21
#### Feature
- `chainctl iam invites create` will accept a role name or ID with the `--role` flag.


### v0.1.0
Release date: 2022-09-21
#### Feature
- Use `chainctl config reset` to revert configuration values back to defaults, and `chainctl config view` now includes any Chainguard environment variables that are set.
- `chainctl iam invites create` will accept a role name or ID with the `--role` flag.


### v0.0.24
Release date: 2022-09-21

Customer facing changes: N/A

### v0.0.23
Release date: 2022-09-19

Customer facing changes: N/A

### v0.0.22
Release date: 2022-09-18

Customer facing changes: N/A

### v0.0.21
Release date: 2022-09-16

Customer facing changes: N/A

### v0.0.20
Release date: 2022-09-15
#### Feature
- `chainctl iam invite create` prints the invite code and constructed invitation URL by default. To force the previous default JSON output instead, include the `-ojson` flag.


### v0.0.19
Release date: 2022-09-14
#### Feature
- `chainctl iam invite create` prints the invite code and constructed invitation URL by default. To force the previous default JSON output instead, include the `-ojson` flag.


### v0.0.18
Release date: 2022-09-14

Customer facing changes: N/A

### v0.0.17
Release date: 2022-09-13

Customer facing changes: N/A

### v0.0.16
Release date: 2022-09-13

Customer facing changes: N/A

### v0.0.15
Release date: 2022-09-12

Customer facing changes: N/A

### v0.0.14
Release date: 2022-09-10
#### Feature
- Customize some colors used across chainctl with `CHAINGUARD_OUTPUT_COLOR_PASS`, `CHAINGUARD_OUTPUT_COLOR_WARN`, and `CHAINGUARD_OUTPUT_COLOR_FAIL`. Highlight important images when reviewing cluster records with `CHAINGUARD_OUTPUT_RECORDS_NOTABLE` and `CHAINGUARD_OUTPUT_RECORDS_COLOR`.
#### Other (Cleanup or Flake)
- Adds support for features added in policy-controller v0.3.0


### v0.0.13
Release date: 2022-09-07
#### Bug or Regression
- `chainctl config edit` will now create a default config file at `<User's config directory>/chainctl/config.yaml`, if one does not exist.
- Fixes certificate output for Fulcio OIDs


### v0.0.12
Release date: 2022-09-06

Customer facing changes: N/A

### v0.0.11
Release date: 2022-09-02

Customer facing changes: N/A

### v0.0.10
Release date: 2022-08-31

Customer facing changes: N/A

### v0.0.9
Release date: 2022-08-30
#### Feature
- Added new command "chainctl cluster update" to update a cluster's name and/or description.
- Allow filtering clusters by group during uninstallation of inactive clusters with the "--group" flag.
- added support for clusters with private API endpoints using the `--private` flag on `chainctl cluster install`


### v0.0.8
Release date: 2022-08-22

Customer facing changes: N/A

### v0.0.7
Release date: 2022-08-15

Customer facing changes: N/A

### v0.0.6
Release date: 2022-08-11

Customer facing changes: N/A

### v0.0.5
Release date: 2022-08-10

Customer facing changes: N/A

### v0.0.4
Release date: 2022-08-09

Customer facing changes: N/A

### v0.0.3
Release date: 2022-08-05

Customer facing changes: N/A

### v0.0.2
Release date: 2022-07-26

Customer facing changes: N/A

### v0.0.1
Release date: 2022-07-19

Customer facing changes: N/A

### v0.0.0
Release date: 2022-07-15

Customer facing changes: N/A
