---
title: "Disallowing Non-Default Capabilities"
type: "article"
description: "Using Policy Controller to prevent running pods with extra capabilities"
date: 2023-03-02T13:11:29+08:29
lastmod: 2023-03-02T13:11:29+08:29
draft: false
tags: ["policy-controller", "Procedural", "Policy"]
images: []
menu:
  docs:
    parent: "policy-controller"
weight: 006
toc: true
terminalImage: policy-controller-base:latest
---

This guide demonstrates how to use the [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) to prevent running containers with extra capabilities. You will create a `ClusterImagePolicy` that uses the [CUE](https://cuelang.org/) language to examine a pod spec, and only allow admission into a cluster if the pod is running with one or many [Linux capabilities](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container) from defined set of safe capabilities flags.

## Prerequisites

To follow along with this guide outside of the terminal that is embedded on this page, you will need the following:

* A Kubernetes cluster with administrative access. You can set up a local cluster using [**kind**](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) or use an existing cluster.
* **kubectl** — to work with your cluster. Install `kubectl` for your operating system by following the official [Kubernetes kubectl documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).
* [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) installed in your cluster. Follow our [How To Install Sigstore Policy Controller](https://edu.chainguard.dev/open-source/sigstore/policy-controller/how-to-install-policy-controller/) guide if you do not have it installed, and be sure to label any namespace that you intend to use with the `policy.sigstore.dev/include=true` label.

If you are using the terminal that is embedded on this page, then all the prerequsites are installed for you. Note that it make take a minute or two for the Kubernetes cluster to finish provisioning. If you receive any errors while running commands, retry them after waiting a few seconds.

Once you have everything in place you can continue to the first step and confirm that the Policy Controller is working as expected.

## Step 1 - Checking the Policy Controller is Denying Admission

Before creating a `ClusterImagePolicy`, check that the Policy Controller is deployed and that your `default` namespace is labeled correctly. Run the following to check that the deployment is complete:

```bash
kubectl -n cosign-system wait --for=condition=Available deployment/policy-controller-webhook && \
kubectl -n cosign-system wait --for=condition=Available deployment/policy-controller-policy-webhook
```

When both deployments are finished, verify the `default` namespace is using the Policy Controller:

```
kubectl get ns -l policy.sigstore.dev/include=true
```

You should receive output like the following:

```
NAME      STATUS   AGE
default   Active   24s
```

Once you are sure that the Policy Controller is deployed and your `default` namespace is configured to use it, run a pod to make sure admission requests are handled and denied by default:

```bash
kubectl run --image cgr.dev/chainguard/nginx:latest nginx
```

Since there is no `ClusterImagePolicy` defined yet, the Policy Controller will deny the admission request with a message like the following:

```
Error from server (BadRequest): admission webhook "policy.sigstore.dev" denied the request: validation failed: no matching policies: spec.containers[0].image
cgr.dev/chainguard/nginx@sha256:628a01724b84d7db2dc3866f645708c25fab8cce30b98d3e5b76696291d65c4a
```

In the next step, you will define a policy that ensures pods only run with safe capabilities and apply it to your cluster.

## Step 2 — Creating a `ClusterImagePolicy`

Now that you have the Policy Controller running in your cluster, and have the `default` namespace configured to use it, you can now define a `ClusterImagePolicy` to admit images.

Open a new file with `nano` or your preferred editor:

```shell
nano /tmp/cip.yaml
```

Copy the following policy to the `/tmp/cip.yaml` file:

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: non-default-capabilities-cue
spec:
  match:
  - version: "v1"
    resource: "pods"
  images: [glob: '**']
  authorities: [static: {action: pass}]
  mode: enforce
  policy:
    includeSpec: true
    type: "cue"
    data: |
      #Allowed: "AUDIT_WRITE" |
                "CHOWN" |
                "DAC_OVERRIDE" |
                "FOWNER" |
                "FSETID" |
                "KILL" |
                "MKNOD" |
                "NET_BIND_SERVICE" |
                "SETFCAP" |
                "SETGID" |
                "SETPCAP" |
                "SETUID" |
                "SYS_CHROOT"
      spec: {
        initContainers: [...{
          securityContext: {
            capabilities: {
              add: [...#Allowed]
            }
          }
        }]
        containers: [...{
          securityContext: {
            capabilities: {
              add: [...#Allowed]
            }
          }
        }]
        ephemeralContainers: [...{
          securityContext: {
            capabilities: {
              add: [...#Allowed]
            }
          }
        }]
      }
```

The Policy Controller will check each type of container's definition (`initContainers`, `containers`, and `ephemeralContainers`) in a pod spec for any added capabilities. The controller will only admit a pod if the added capabilities are in the `#Allowed` set.

The set of allowed capabilities is defined in this portion of the CUE policy and can be added to or changed to match your specific workload's needs:

```
#Allowed: "AUDIT_WRITE" |
                "CHOWN" |
. . .
```

Save the file and then apply the policy:

```bash
kubectl apply -f /tmp/cip.yaml
```

You will receive output showing the policy is created:

```
clusterimagepolicy.policy.sigstore.dev/non-default-capabilities-cue
```

Next you will test the policy with a failing pod spec. Once you have confirmed that the admission controller is rejecting pods running with privileges, you'll create a pod that runs without unnecessary capabilities and admit it into your cluster.

## Step 3 — Testing a `ClusterImagePolicy`

Now that you have a policy defined, you can test that it successfully rejects or accepts admission requests.

Use `nano` or your preferred editor to create a new file `/tmp/pod.yaml` and copy in the following pod spec that runs with elevated privileges:

```
apiVersion: v1
kind: Pod
metadata:
  name: yolo
spec:
  containers:
  - name: "app"
    image: docker.io/ubuntu
    securityContext:
      capabilities:
        add:
        # Violates restricted-capabilities
        - NET_ADMIN
        drop:
        - ALL
```

Apply the pod spec and check for the Policy Controller admission denied message:

```
kubectl apply -f /tmp/pod.yaml
```

```
Error from server (BadRequest): error when creating "pod.yaml": admission webhook "policy.sigstore.dev" denied the request: validation failed: failed policy: non-default-capabilities-cue: spec.containers[0].image
index.docker.io/library/ubuntu@sha256:2adf22367284330af9f832ffefb717c78239f6251d9d0f58de50b86229ed1427 failed evaluating cue policy for ClusterImagePolicy: failed to evaluate the policy with error: spec.containers.0.securityContext.capabilities.add.0: 12 errors in empty disjunction: (and 12 more errors)
```

The first line shows the error message and the failing `ClusterImagePolicy` name. The second line contains the image ID, along with the specific CUE error message showing the policy violation.

Edit the `/tmp/pod.yaml` file and remove or edit the `add` portion of the `capabilities` section. If there are no extra capabilities then the section should look like the following:

```
    capabilities:
        drop:
        - ALL
```

Save and apply the spec:

```
kubectl apply -f /tmp/pod.yaml
```

The pod will be admitted into the cluster with the following message:

```
pod/yolo created
```

Since the pod spec now ensures the container does not have and extra capabilities, or only those from the `#Allowed` set, the Policy Controller evaluates the pod spec against the CUE policy and admits the pod into the cluster.

Delete the pod once you're done experimenting with it:

```
kubectl delete pod yolo
```

## Options for Continuous Verification

While it is useful to use the Policy Controller to manage admission into a cluster, once a workload is running any vulnerability or policy violations that occur after containers are running will not be detected.

[Chainguard Enforce](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/understanding-continuous-verification/) is designed to address this issue by continuously verifying whether a container or cluster contains any vulnerabilities or policy violations over time. This includes what packages are deployed, SBOMs (software bills of materials), provenance, signature data, and more.

If you're interested in learning more about Chainguard Enforce, you can request access to the product by selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs).