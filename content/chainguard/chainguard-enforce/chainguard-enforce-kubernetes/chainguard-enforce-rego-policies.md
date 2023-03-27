---
title: "Rego Policies"
type: "article"
description: "Writing Rego-based policies for Chainguard Enforce"
date: 2023-01-12T15:56:52-07:00
lastmod: 2023-01-12T15:56:52-07:00
draft: false
tags: ["Enforce", "Product", "Procedural", "Policy", "Reference", "SBOM"]
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

In this policy, you should change the `name` to be meaningful to you. The `spec` fields are defined at [ClusterImagePolicySpec](https://github.com/sigstore/policy-controller/blob/main/docs/api-types/index.md#clusterimagepolicyspec). By default, this policy will apply to all images, as noted with the `glob: '**'` parameter. If we keep this as is, this means that we are evaluating everything running in our cluster.

The `authorities` field is used in evaluating image signatures. Since we aren’t using signatures in this policy, we will set it to pass. This will be a common setting in Rego-based policies unless you are also evaluating signatures simultaneously.

The policy is being implemented in `warn` mode, which can generate an alert through `CloudEvents` to notify administrators of violations without blocking deployments. You can alternatively use `mode: enforce` to block deployments that violate the policy.

The Rego policy itself is definied within the `policy` section. The first requirement is to include the input data that is to be evaluated. By default, the image in the registry is available. To include additional metadata, one of more of the following should be set:

* `includeSpec:` allows you to access the fields in the `spec` portion of the Kubernetes manifest, including the container configuration, image names, replicas, resources, and more.
* `includeObjectMeta:` allows you to access the fields in the `metadata:` portion of the manifest, including the object’s name and labels.
* `includeTypeMeta:` allows access to the top level fields in the manifest, such as the `kind` and `apiVersion`.
* `fetchConfigFile:` fetches the OCI config file from the registry, which contains metadata about the image in the registry.

Rego policies in Enforce must specify `type: rego` and the `data` field must contain `package sigstore`. 

For the policy to pass, the `isCompliant` field must evaluate to `true` within the curly braces. The `isCompliant` Boolean is set to `false` by default, and the logic in the braces must flip the boolean to `true` for the policy to pass. 

If you define multiple conditions within the `isCompliant` braces, these can be combined using the `AND` keyword to the Boolean logic, meaning that each condition must pass for `isCompliant` to resolve to `true`. You can also define multiple evaluations (meaning, multiple sets of `isCompliant` braces) in the same policy. You would combine these in your policy with the `OR` keyword, meaning that if _any_ of the stated conditions evaluate to `true`, then the `isCompliant` Boolean will _also_ be `true`.

This same structure must be present in all Rego-based policies in Enforce.

## Rego Policy to Check Metadata Labels

You can set a Rego policy in Chainguard Enforce to ensure that it is compliant with certain labels within your metadata. 

For example, within the production environment (with the "production" label) you can ensure that the compliance team is the approver.

```sh
      isCompliant {

        input.metadata.labels.env == "production"
        input.metadata.labels.approved-by == "compliance-team"
      }
```

Here, the policy is requiring and checking that the labels exist in the `ObjectMeta` data. This policy will evaluate to true only if both labels exist in the metadata portion of the manifest.

## Rego Policy to Check Kubernetes Pod Security

As a cluster-level resource, a Kubernetes Pod Security Policy allows a cluster administrator to control security-sensitive aspects of a Pod's specification. This defines a set of conditions that a Pod must meet so that it can be allowed into the cluster. You can think of it as a built-in admission controller which enforces security policies on Pods across a cluster.

This policy checks to make sure our Pod security specifications are properly set.

 ```sh
       isCompliant {

        input.spec.hostNetwork == "false"
        input.spec.hostPID == "false"
        input.spec.hostIPC == "false"
      }
```

Here, `hostNetwork` refers to the host's networking namespace, `hostPID` refers to the host process ID namespace, and `hostPIC` refers to the IPC (interprocess communication) namespace.

This policy will pass if all the restricted values are set to `false`.

## Rego Policy that Disallows Specified Images

In some cases, you may want to evaluate an item elsewhere in the manifest, such as an image source that is included within the container specs of the same manifest. For example, a manifest may have a snippet with a disallowed NGINX image from Docker Hub:

```sh
spec:
  containers:
  - name: "your-container-name"
    image: nginx:latest
  - name: "another-container-name"
    image: nginx
```

In this case, within the `policy` section of your Rego policy, you’ll need to iterate over the image array and check all the relevant fields for the restricted value. You can use the `[_]` syntax to iterate through the array. You can use the `not` keyword in conjunction with the `contains()` built-in function to evaluate all the items within the array.

```sh
      isCompliant {

        result:= input.spec.containers.image[_]
        not contains(result,"docker.io")

      }
```

This policy will not admit Pods that come from docker.io.

## Rego Policy that Disallows Privilege Escalation in Pods

This example Rego policy will disallow privilege escalation in Pods following the [Kubernetes Pod Security Baseline](https://kubernetes.io/docs/concepts/security/pod-security-standards/) Standard. The Baseline Standard is a minimally restrictive policy which prevents known privilege escalations and allows the default and minimally specified Pod configuration.

```sh
      isCompliant {

        filteredContainers = [c | c := input.spec.containers[_]; c.securityContext.allowPrivilegeEscalation == true ]
        filteredInitContainers = [c | c := input.spec.initContainers[_]; c.securityContext.allowPrivilegeEscalation == true ]
        filteredEphemeralContainers = [c | c := input.spec.ephemeralContainers[_]; c.securityContext.allowPrivilegeEscalation == true ]
        (count(filteredContainers) + count(filteredInitContainers) + count(filteredEphemeralContainers)) == 0

      }
```

Setting the `allowPrivilegeEscalation` Boolean controls whether a process can gain more privileges than its parent process. This value will evaluate to `true` when the container is run as privileged. You can review more information about [how to configure a security context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) on the Kubernetes docs. 

This Rego policy shows a method of declaring a variable and using it to count up all the instances of privilege escalation across Pod types, and evaluate that the final count is `0` in order for the policy to pass.

## Rego Policy that Checks Maximum Age of Images

This example Rego policy checks the maximum age (in days) allowed for an image running in your cluster. Enforce measures this through the `created` field of a container image's configuration. This ensures that your images are regularly updated and maintained.

Note that some build tools may fail this check due to using a fixed time (like the Unix epoch) for creation in their reproducible builds. However, many of these tools support specifying `SOURCE_DATE_EPOCH`, which aligns creation time with the date of the source commit.

```sh
  policy:
    fetchConfigFile: true
    type: "rego"
    data: |
      package sigstore

      nanosecs_per_second = 1000 * 1000 * 1000
      nanosecs_per_day = 24 * 60 * 60 * nanosecs_per_second

      # Change this to the maximum number of days you would like to allow
      maximum_age = 30 * nanosecs_per_day

      default isCompliant = false
      isCompliant {
        created := time.parse_rfc3339_ns(input.config[_].created)
        time.now_ns() < created + maximum_age
      }
```

Here, the policy defines a variable for the `maximum_age`, in this case set to `30`, which you can change to the number of days old you would permit an image to be. 

Within the `isCompliant` braces, the Rego policy leverages `time` to evaluate whether the current time is less than the maximum allowed age. To review the different methods of implementing `time` within Rego, review the [Time reference documentation](https://www.openpolicyagent.org/docs/latest/policy-reference/#time).


## Rego Policies that Define Custom Error and Warning Messages

Rego policies have the added benefit of allowing you to define custom error and warning messages. 

This example `attestations` block requires clusters to have a vulnerability report in order to be deemed compliant. Notice, though, that it also defines an `errorMsg` string.

```
  attestations:
    - name: must-have-vuln-report
      predicateType: vuln
      policy:
        type: rego
        data: |
          package sigstore
          isCompliant[response] {
            result = (input.predicateType == "chainguard.dev/attestation/vuln/v1")
            errorMsg = "Not found expected predicate type 'chainguard.dev/attestation/vuln/v1'"
            warnMsg = ""
            response := {
              "result" : result,
              "error" : errorMsg,
              "warning" : warnMsg
            }
          }
```

Here, the custom error message reads `Not found expected predicate type 'chainguard.dev/attestation/vuln/v1'`. Rather than returning the default error, Chainguard Enforce will return this string as a custom error message.

Notice, too, that the previous example defines a `warnMsg` variable. Enforce will only return a warning message to the caller if the policy in question is in `warn` mode, so in that case it was left as an empty string.

The following `attestations` block is similar to the previous one, but this time it defines the `warnMsg` variable to be used as a custom warning message.

```
  attestations:
    - name: must-have-vuln-report
      predicateType: vuln
      policy:
        type: rego
        data: |
          package sigstore
          isCompliant[response] {
            result = (input.predicateType == "cosign.sigstore.dev/attestation/vuln/v1")
            errorMsg = ""
            warnMsg = "WARNING: Found an attestation with predicate type 'cosign.sigstore.dev/attestation/vuln/v1'"
            response := {
              "result" : result,
              "error" : errorMsg,
              "warning" : warnMsg
            }
          }
```

Defining custom error and warning messages with Rego can help with troubleshooting, as they can explain specific policy issues that otherwise may not be clearly understandable.


## Learn More

Within the [Chainguard Enforce Policy Catalog](https://console.enforce.dev/policies/catalog), you have access to more Rego policy templates that you can use directly or modify. These include enforcing SBOM attestation, enforcing a signed vulnerability attestation, and disallowing host namespaces.  

To understand more about the Rego policy format, you can review the [Rego Policy Reference](https://www.openpolicyagent.org/docs/latest/policy-reference/) which includes details on assignment and equality, arrays, objects, sets, and rules. 

Request access to Chainguard Enforce by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs).
