---
title : "Chainguard Enforce Changelog"
description: "Chainguard Enforce Changelog"
type: "article"
date: 2022-12-07 20:35:46 +0000 UTC
draft: false
images: []
weight: 799
---

## Introduction
Any customer facing changes to Chainguard Enforce or [`chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) are highlighted in the following notes. Any new features, bug fixes, or general ease of use improvements will be listed under the corresponding release version.

### v0.1.39
Release date: 2022-12-07
#### Other (Cleanup or Flake)
- agent-based installations may now specify --name and --description during their initial registration.
- declarative installations may now specify cluster name/description by adding the keys cluster-{name,description} to mcp-creds.

### v0.1.38
Release date: 2022-12-07
#### Feature
- The meta reconciliation processes which are spun up by our agents are now HA with keys distributed evenly across the statefulset's replicas.
#### Other (Cleanup or Flake)
- agentless tenants will no longer create a gulfstream namespace for their UID, preferring instead kube-system for establishing cluster identity.
- chainctl now groups cluster activity by a clearer "profile" descriptor, e.g. "policy" and "monitor" (Caveat: these names may change a bit as we finalize things)


### v0.1.37
Release date: 2022-12-07
#### Feature
- Agentless no longer creates CRDs to program itself.
#### Bug or Regression
- Fix an issue where agentless will overwrite user modifications to configmaps.
- Fixes an issue where some distributed policies were getting starved during Continuous Verification due to re-evaluation and throttling.


### v0.1.36
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.35
Release date: 2022-11-23
#### Bug or Regression
- Fix a bug in our image discovery where RecordContext LastSeen timestamps were updated without updating the ExistenceRecord's LastSeen timestamp.
#### Other (Cleanup or Flake)
- Agentless no longer installs [Cluster]Role[Binding]s since it authenticates via IAM

### v0.1.34
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.33
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.32
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.31
Release date: 2022-11-28
#### Other (Cleanup or Flake)
- Policy events will now only contain entries for changed results.


### v0.1.30
Release date: 2022-11-28
#### Feature
- Log out of the Chainguard platform with `chainctl auth logout`.
- Policy updates now trigger revalidation in continuous verification
#### Other (Cleanup or Flake)
- Customers on older versions of chainctl will need to upgrade, and possible upgrade their agent for things like Workload to continue to show up properly in chainctl and the UI.
- `chainctl iam groups describe` now supports filtering cluster records with `--active-within`.

### v0.1.29
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.28
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.27
Release date: 2022-11-28
#### Feature
- Document Enforce emitted cloudevents including HTTP headers. Available at https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-enforce-events
- Introduce a new "chainctl cluster workloads ls" command for visualizing the workloads running in a cluster or namespace.


### v0.1.26
Release date: 2022-11-28
#### Other (Cleanup or Flake)
- chainctl cluster records ls now distinguishes "mode: warn" policies from "mode: enforce"
- We no longer embed signatures/attestations in the existence records API, e.g. chainctl cluster records ls -ojson


### v0.1.25
Release date: 2022-11-28
#### Feature
- Get information about the policies, images, and packages running on a cluster with `chainctl cluster describe`.
- (staging-only) chainops.dev issued OIDC tokens will now start returning a new `upstream` claim, which contains an encrypted version of the incoming OIDC for use in downstream components.


### v0.1.24
Release date: 2022-11-28
- Adds new `upstream` claim in Chainguard issued OIDC tokens, which includes encrypted data identifying the upstream user the token is being issued for.


### v0.1.23
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.22
Release date: 2022-11-28
#### Feature
- "chainctl cluster install" no longer pins to the version of the agent embedded in the CLI, but fetches the latest programming from a new API.


### v0.1.21
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.20
Release date: 2022-11-28
- This release is an exciting update for Chainguard Enforce. Enforce now emits events when enforcement status on a namespace changes. 
- You can create policies from scratch or choose one from our catalog! 
- <img width="396" alt="image" src="https://user-images.githubusercontent.com/8444505/209160322-343de467-5a0a-45d8-92b1-e5d3456c26f0.png"> 
#### Feature
- Start to emit a new dev.chainguard.admission.namespace.v1 event when the policy status on a namespace changes.
- `chainctl cluster uninstall` asks the user for confirmation before continuing. Bypass interactive mode by passing the `--yes` flag.
#### Other (Cleanup or Flake)
- `chainctl cluster uninstall` now accepts `--yes`


### v0.1.19
Release date: 2022-11-28
#### Other (Cleanup or Flake)
- When choosing from a list of resources (e.g. clusters, groups), chainctl will proceed automatically if only a single resource is available.

### v0.1.18
Release date: 2022-11-28
#### Feature
- Added Chainguard Enforce to the AWS Marketplace
- Remove AWS and GCP account associations with `chainctl iam groups remove-aws` and `remove-gcp`, respectively.
#### Other (Cleanup or Flake)
- `chainctl cluster uninstall` accepts filtering with `--group` when uninstalling active clusters; a cluster is only uninstalled if it belongs to the given group or a descendant.

### v0.1.17
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.16
Release date: 2022-11-28
#### Feature
- `chainctl cluster records list` accepts cluster names in addition to IDs.
- chainctl attempts to authenticate with OAuth2 device flow in terminals without access to a browser.


### v0.1.15
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.14
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.13
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.12
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.11
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.10
Release date: 2022-11-28
#### Feature
- Update chainctl directly with `chainctl update`


### v0.1.9
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.8
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.7
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.6
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.5
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.4
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.3
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.2
Release date: 2022-11-28

Customer facing changes: N/A

### v0.1.1
Release date: 2022-11-28
#### Feature
- `chainctl iam invites create` will accept a role name or ID with the `--role` flag.


### v0.1.0
Release date: 2022-11-28
#### Feature
- Use `chainctl config reset` to revert configuration values back to defaults, and `chainctl config view` now includes any Chainguard environment variables that are set.
- `chainctl iam invites create` will accept a role name or ID with the `--role` flag.


### v0.0.24
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.23
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.22
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.21
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.20
Release date: 2022-11-28
#### Feature
- `chainctl iam invite create` prints the invite code and constructed invitation URL by default. To force the previous default JSON output instead, include the `-ojson` flag.


### v0.0.19
Release date: 2022-11-28
#### Feature
- `chainctl iam invite create` prints the invite code and constructed invitation URL by default. To force the previous default JSON output instead, include the `-ojson` flag.


### v0.0.18
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.17
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.16
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.15
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.14
Release date: 2022-11-28
#### Feature
- Customize some colors used across chainctl with `CHAINGUARD_OUTPUT_COLOR_PASS`, `CHAINGUARD_OUTPUT_COLOR_WARN`, and `CHAINGUARD_OUTPUT_COLOR_FAIL`. Highlight important images when reviewing cluster records with `CHAINGUARD_OUTPUT_RECORDS_NOTABLE` and `CHAINGUARD_OUTPUT_RECORDS_COLOR`.
#### Other (Cleanup or Flake)
- Adds support for features added in policy-controller v0.3.0


### v0.0.13
Release date: 2022-11-28
#### Bug or Regression
- `chainctl config edit` will now create a default config file at `<User's config directory>/chainctl/config.yaml`, if one does not exist.
- Fixes certificate output for Fulcio OIDs


### v0.0.12
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.11
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.10
Release date: 2022-11-28

Customer facing changes: N/A

### v0.0.9
Release date: 2022-11-24
#### Feature
- Added new command "chainctl cluster update" to update a cluster's name and/or description.
- Allow filtering clusters by group during uninstallation of inactive clusters with the "--group" flag.
- added support for clusters with private API endpoints using the `--private` flag on `chainctl cluster install`


### v0.0.8
Release date: 2022-11-24

Customer facing changes: N/A

### v0.0.4
Release date: 2022-11-24

Customer facing changes: N/A

### v0.0.3
Release date: 2022-11-24

Customer facing changes: N/A

### v0.0.2
Release date: 2022-11-24

Customer facing changes: N/A

### v0.0.1
Release date: 2022-11-24

Customer facing changes: N/A

### v0.0.0
Release date: 2022-11-23

Customer facing changes: N/A
