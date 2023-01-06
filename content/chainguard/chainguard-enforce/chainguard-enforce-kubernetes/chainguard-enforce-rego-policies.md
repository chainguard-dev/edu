---
title: "How to Use Rego Policies with Chainguard Enforce"
type: "article"
description: "Writing Rego-based policies for Chainguard Enforce"
date: 2023-01-05T15:56:52-07:00
lastmod: 2022-01-05T15:56:52-07:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 700
toc: true
---

> _This document relates to Chainguard Enforce. In order to follow along, you will need access to Chainguard Enforce. You can request access by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Chainguard Enforce supports the [Rego Policy Language](https://www.openpolicyagent.org/docs/latest/policy-language/), which is a declarative policy language that is used to evaluate structured input data such as Kubernetes manifests and JSON documents. This feature enables users to apply policies that can evaluate Kubernetes admission requests and object metadata to make comprehensive decisions about the workloads that are admitted to their clusters. Rego support also enables users to enhance existing cloud-native policies by adding additional software supply chain security checks all within Chainguard Enforce.

There are several Rego policy templates that you can customize within the [Chainguard Enforce Policy Catalog](https://console.enforce.dev/policies/catalog). If you would like to write one from scratch, or learn more about how to use this format, you can follow this guide. 

## Rego Policy Template

The [Chainguard Enforce Policy Catalog](https://console.enforce.dev/policies/catalog) includes a blank Rego policy template that you can use to build your own policy. 

```bash
# Copyright 2022 Chainguard, Inc.
# SPDX-License-Identifier: Apache-2.0

apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: my-rego-policy

spec:
  images: [glob: '**']
  authorities: [static: {action: pass}]
  mode: warn
  policy:
    includeSpec: true
    type: rego
    data: |
      package sigstore
      default isCompliant = false
      isCompliant {

        # Rego logic goes here; must evaluate to true for policy to pass

      }
```

In this policy, you should change the `name` to be meaningful to you. The `spec` fields are defined at [ClusterImagePolicySpec](https://github.com/sigstore/policy-controller/blob/main/docs/api-types/index.md#clusterimagepolicyspec). By default, this policy will apply to all images, as noted with the `glob: '**'` parameter. If we keep this as is, this means that we are evaluating everything.

The `authorities` field is used in evaluating image signatures. Since we aren’t using signatures in this policy, we will set it to pass. This will be a common setting in Rego-based policies unless you are also evaluating signatures simultaneously.

The policy is being implemented in `warn` mode, which can generate an alert through `CloudEvents` to notify administrators of violations without blocking deployments. You can alternately use `mode: enforce` to block deployments that violate the policy.

Within the `policy` section is where the Rego policy is defined. The first requirement is to include the input data that is to be evaluated. By default, the image in the registry is available. To include additional metadata, one of more of the following should be set:

* `includeSpec:` allows you to access the fields in the `spec` portion of the Kubernetes manifest, including the container configuration, image names, replicas, resources, and more.
* `includeObjectMeta:` allows you to access the fields in the metadata: portion of the manifest, including the object’s name and labels.
* `includeTypeMeta:` allows access to the top level fields in the manifest, such as the `kind` and `apiVersion`.
* `fetchConfigFile:` fetches the OCI config file from the registry, which contains metadata about the image in the registry.

Rego policies in Enforce must specify `type: rego` and the `data` field must contain `package sigstore`. 

For the policy to pass, the `isCompliant` field must evaluate to `true` within the curly braces. The `isCompliant` Boolean is set to false by default, and the logic in the braces must flip the boolean to true for the policy to pass. 

Within the `isCompliant` braces, multiple conditions may exist if they are added together with the `AND` keyword Multiple evaluations within different sets of braces may also exist in the policy, these will be chained together with the `OR` keyword, meaning that if any of them is true, the Boolean evaluate to be true.

This same structure must be present in all Rego-based policies in Enforce.

