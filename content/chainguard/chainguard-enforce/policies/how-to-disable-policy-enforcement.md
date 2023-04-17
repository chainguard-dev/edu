---
title: "Disable Policy Enforcement"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/how-to-disable-policy-enforcement/
type: "article"
description: "Quickly handle incident responses in Chainguard Enforce"
date: 2022-11-29T08:49:31+00:00
lastmod: 2023-03-22T08:49:31+00:00
draft: false
tags: ["Enforce", "Product", "Reference"]
images: []
menu:
  docs:
    parent: "policies"
weight: 040
toc: true
---

> _This document relates to Chainguard Enforce. In order to follow along, you will need access to Chainguard Enforce. You can request access through selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)._

In the event of an incident response or another situation where you may need to modify Chainguard Enforce to _warn_ about instead of _fail_ a given policy, you can modify the policy configuration.

In an Enforce policy, images that fail to meet requirements will cause the image not to be admitted by default. To instead allow these through and warn the user that this operation did not meet the criteria, you can use the `mode` configuration option under `ClusterImagePolicy`. When set to `warn`, the policy will not block the admission, but instead will allow it through and emit a warning.

## Example Warning Policies 

The following sets the `mode` configuration to `warn`.

```yaml
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: image-policy-keyless-warn
spec:
  mode: warn
  images:
  - glob: registry.local:5000/policy-controller/demo*
  authorities:
  - keyless:
      url: http://fulcio.fulcio-system.svc
    ctlog:
      url: http://rekor.rekor-system.svc
```

By specifying the `spec.mode` as `warn`, even if an image is found to be non-compliant it will be allowed through. At the same time, a warning is issued to the caller informing them that this is not a compliant image.

In the Chainguard Enforce Policy Catalog, review also the CUE "Disallow privilege escalation" policy, which prevents privilege escalation (such as via `set-user-ID` or `set-group-ID` file mode). This is Linux only policy in v1.25+.

```yaml
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: disallow-privilege-escalation-cue
  annotations:
    catalog.chainguard.dev/title: Disallow privilege escalation
    catalog.chainguard.dev/labels: cue,workloads
    catalog.chainguard.dev/description: |
      Privilege escalation (such as via set-user-ID or set-group-ID file mode) should
      not be allowed. This is Linux only policy in v1.25+ (spec.os.name != windows)

    catalog.chainguard.dev/learnMoreLink: https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline
spec:
  match:
  - version: "v1"
    resource: "pods"
  images: [glob: '**']
  authorities: [static: {action: pass}]
  mode: warn
  policy:
    includeSpec: true
    type: "cue"
    data: |
      // Create a schema for SecurityContext where allowPrivilegeEscalation
      // is a bool that defaults to true
      #SecurityContext: {
        allowPrivilegeEscalation: bool | *true
        ...
      }
      spec: {
        initContainers: [...{
          // Apply the schema to the security context in each container.
          securityContext: #SecurityContext
          // When allowPrivilegeEscalation is true (either specified, or by default)
          // then surface our error by "validating" name against our error string.
          if securityContext.allowPrivilegeEscalation {
            name: "securityContext.allowPrivilegeEscalation must be false"
          }
        }]
        containers: [...{
          // Apply the schema to the security context in each container.
          securityContext: #SecurityContext
          // When allowPrivilegeEscalation is true (either specified, or by default)
          // then surface our error by "validating" name against our error string.
          if securityContext.allowPrivilegeEscalation {
            name: "securityContext.allowPrivilegeEscalation must be false"
          }
        }]
        ephemeralContainers: [...{
          // Apply the schema to the security context in each container.
          securityContext: #SecurityContext
          // When allowPrivilegeEscalation is true (either specified, or by default)
          // then surface our error by "validating" name against our error string.
          if securityContext.allowPrivilegeEscalation {
            name: "securityContext.allowPrivilegeEscalation must be false"
          }
        }]
      }
```

Again, the `mode` configuration is set to `warn`. If you are logged into the Enforce Console, you can access the [Disallow privilege escalation policy](https://console.enforce.dev/policies/catalog/create/disallow-privilege-escalation-cue) from the Policy Catalog from the **Create policy** button.

## Review Warning Policies

You can review which policies are in **Enforce** or **Warn** mode by reviewing the policy table in your Enforce Console.

![Warn or Enforce mode indicated in policy table](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-policies-ui/enforce-console-warn-enforce-mode_hu3b0eaea9ffe2caf7848b0a93077fa970_51901_900x0_resize_box_3.png)

From your Enforce Console policy table, you can further edit each enforcing policy to a warning policy and vice versa. 