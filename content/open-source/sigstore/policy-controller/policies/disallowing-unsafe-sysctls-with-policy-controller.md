---
title: "Disallowing Unsafe sysctls"
aliases: 
- /open-source/sigstore/policy-controller/disallowing-unsafe-sysctls-with-policy-controller/
type: "article"
description: "Use Policy Controller to limit pods to safe sysctls"
date: 2023-03-01T13:11:29+08:29
lastmod: 2024-05-10T13:11:29+08:29
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

This guide demonstrates how to use the [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) to only allow pods that use `sysctls` to modify kernel behaviour to run with the [safe set](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/#safe-and-unsafe-sysctls) of parameters. You will create a `ClusterImagePolicy` that uses the [CUE](https://cuelang.org/) language to examine a pod spec that uses sysctls, and only allow admission into a cluster if the pod is running a safe set parameters.

## Prerequisites

To follow along with this guide outside of the terminal that is embedded on this page, you will need the following:

* A Kubernetes cluster with administrative access. You can set up a local cluster using [**kind**](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) or use an existing cluster.
* **kubectl** — to work with your cluster. Install `kubectl` for your operating system by following the official [Kubernetes kubectl documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).
* [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) installed in your cluster. Follow our [How To Install Sigstore Policy Controller](/open-source/sigstore/policy-controller/how-to-install-policy-controller/) guide if you do not have it installed, and be sure to label any namespace that you intend to use with the `policy.sigstore.dev/include=true` label.

If you are using the terminal that is embedded on this page, then all the prerequsites are installed for you. Note that it may take a minute or two for the Kubernetes cluster to finish provisioning. If you receive any errors while running commands, retry them after waiting a few seconds.

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
kubectl run --image docker.io/ubuntu ubuntu
```

Since there is no `ClusterImagePolicy` defined yet, the Policy Controller will deny the admission request with a message like the following:

```
Error from server (BadRequest): admission webhook "policy.sigstore.dev" denied the request: validation failed: no matching policies: spec.containers[0].image
index.docker.io/library/ubuntu@sha256:854037bf6521e9c321c101c269272f756e481fb5f167ae032cb53da08aebcd5a
```

In the next step, you will define a `ClusterImagePolicy` that verifies a pod spec is using safe sysctl parameters.

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
  name: unsafe-sysctls-mask-cue
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
      spec: {
        securityContext:
          sysctls: [...{
            name: "kernel.shm_rmid_forced" |
                  "net.ipv4.ip_local_port_range" |
                  "net.ipv4.ip_unprivileged_port_start" |
                  "net.ipv4.tcp_syncookies" |
                  "net.ipv4.ping_group_range"
          }]
      }
```

This policy will ensure that any pod that has a sysctl defined in its spec will only be admitted if it matches a parameter from the list.

Save the file and then apply the policy:

```bash
kubectl apply -f /tmp/cip.yaml
```

You will receive output showing the policy is created:

```
clusterimagepolicy.policy.sigstore.dev/unsafe-sysctls-mask-cue
```

Next, you will test the policy with a failing pod spec. Once you have confirmed that the admission controller is rejecting pods using unsafe sysctls, you'll create a pod with a safe parameter and admit it into your cluster.

## Step 3 — Testing the `ClusterImagePolicy`

Now that you have a policy defined, you can test that it successfully rejects or accepts admission requests.

Use `nano` or your preferred editor to create a new file `/tmp/pod.yaml` and copy in the following pod spec that uses an unsafe sysctl:

```
apiVersion: v1
kind: Pod
metadata:
  name: yolo
spec:
  securityContext:
    sysctls:
    - name: kernel.msgmax
      value: "65536"
  containers:
  - name: "app"
    image: docker.io/ubuntu
```

Apply the pod spec and check for the Policy Controller admission denied message:

```
kubectl apply -f /tmp/pod.yaml
```

```
Error from server (BadRequest): error when creating "/tmp/pod.yaml": admission webhook "policy.sigstore.dev" denied the request: validation failed: failed policy: unsafe-sysctls-mask-cue: spec.containers[0].image
index.docker.io/library/ubuntu@sha256:854037bf6521e9c321c101c269272f756e481fb5f167ae032cb53da08aebcd5a failed evaluating cue policy for ClusterImagePolicy: failed to evaluate the policy with error: spec.securityContext.sysctls.0.name: 5 errors in empty disjunction: (and 5 more errors)
```

The first line shows the error message and the failing `ClusterImagePolicy` name. The second line contains the image ID, along with the specific CUE error message showing the policy violation.

Edit the `/tmp/pod.yaml` file and change the `sysctls` section to use the following safe parameter:

    sysctls:
    - name: net.ipv4.tcp_syncookies
      value: "1"
    - name: net.ipv4.tcp_syncookies
      value: "1"
```

Save and apply the spec:

```
kubectl apply -f /tmp/pod.yaml
```

The pod will be admitted into the cluster with the following message:

```
pod/yolo created
```

Since the `net.ipv4.tcp_syncookies` sysctl is considered safe and only runs in specific Kubernetes namespaces, the Policy Controller evaluates the pod spec against the CUE policy and admits the pod into the cluster.

Delete the pod once you're done experimenting with it:

```
kubectl delete pod yolo
```