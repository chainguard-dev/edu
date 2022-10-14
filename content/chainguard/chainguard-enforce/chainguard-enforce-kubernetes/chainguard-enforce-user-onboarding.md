---
title: "Chainguard Enforce User Onboarding"
type: "article"
description: "Walkthrough of Chainguard Enforce"
date: 2022-15-07T15:22:20+01:00
lastmod: 2022-13-09T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 100
toc: true
---

> _This provides user onboarding for Chainguard Enforce. In order to follow the onboarding, you will need access to Chainguard Enforce. You can request access through selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Chainguard Enforce is a supply chain security solution for containerized workloads. Chainguard Enforce enables you to build, manage, ensure continuous compliance, and enforce policies that protect organizations from supply chain threats. Using open source projects and standards that are trusted by the community — like [Cosign](https://docs.sigstore.dev/cosign/overview) and [Fulcio](https://docs.sigstore.dev/fulcio/overview) from the [Sigstore](https://sigstore.dev) project — Chainguard Enforce offers a robust approach to securing your workloads.

This guide will walk you through using Chainguard Enforce on a Kubernetes cluster running on your laptop with [kind](https://kind.sigs.k8s.io/). We will be using Chainguard Enforce to achieve the following:

* Policy management — we will create a policy and show it being applied to the cluster, this will involve the use of signed containers and SBOMs (software bills of materials)
* Observation and monitoring — we will use the `chainctl` command line tool to understand our images from a security standpoint
* Enforce — we will verify that Chainguard Enforce stops the deployment of an unsigned image

In this guide, we will set up an example cluster, draft a policy and observe how it behaves, and finally enforce that policy. Ultimately, our goal is to improve our software security in deployment contexts by enforcing the use of signed containers and rejecting any containers that are unsigned.

## Prerequisites

Before running Chainguard Enforce locally, you’ll need to ensure you have the following installed:

* **curl** — to retrieve files from the web, follow the relevant [curl download docs](https://curl.se/download.html) for your machine.
* **Docker** — you’ll need [Docker installed](https://docs.docker.com/get-docker/) and running in order to step through this tutorial. 
* **kind** — to create a kind Kubernetes cluster on our laptop, you can download and install kind for your relevant operating system by following the [kind install docs](https://kind.sigs.k8s.io/docs/user/quick-start/#installation).
* **kubectl** — to work with your kind cluster, you can install for your operating system by following the official [Kubernetes kubectl documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).
* **jq**  — to process JSON, visit the [jq downloads page](https://stedolan.github.io/jq/download/) to set it up.
* For macOS users, you'll need to update to bash version 4 or higher, which is not preinstalled in the machine. Please [follow our guide](../../../../open-source/update-bash-macos) on how to update your version if you are getting version 3 or below when you run `bash --version`.

With these prerequisites in place, you’re ready to begin.

## Step 1 — Install chainctl

Our command line interface (CLI) tool, `chainctl`, will help you interact with the account model that Chainguard Enforce provides, and enable you to make queries into the state of your clusters and policies registered with the platform. The tool uses the familiar `<context> <noun> <verb>` style of CLI interactions. For example, to list groups within the context of Chainguard Identity and Access Management (IAM), you can run `chainctl iam groups list` to receive relevant output.

Before we begin, let’s move into a directory that we can work in. For our example, we’ll create a new directory called `enforce-demo`.

```sh
mkdir ~/enforce-demo && cd $_
```

To install `chainctl`, we’ll use the `curl` command to pull the application down.

```sh
curl -o chainctl "https://dl.enforce.dev/chainctl_$(uname -s)_$(uname -m)"
```

Move `chainctl` into your `/usr/local/bin` directory.

```sh
sudo mv ./chainctl /usr/local/bin/chainctl
```

Next, elevate the permissions of `chainctl` so that it can execute as needed.

```sh
chmod +x /usr/local/bin/chainctl
```

Finally, alias its path so that you can use `chainctl` on the command line.

```sh
alias chainctl=/usr/local/bin/chainctl
```

You can verify that everything was set up correctly by checking the `chainctl` version.

```sh
chainctl version
```

You should receive output similar to the following.

```
   ____   _   _      _      ___   _   _    ____   _____   _
  / ___| | | | |    / \    |_ _| | \ | |  / ___| |_   _| | |
 | |     | |_| |   / _ \    | |  |  \| | | |       | |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___    | |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control

GitVersion:    e01c38b
GitCommit:     e01c38b452ee34e44cf5f8663d7730a2cf69f0c3
GitTreeState:  clean
BuildDate:     2022-09-21T00:10:26Z
GoVersion:     go1.18.6
Compiler:      gc
Platform:      darwin/arm64
```

If you received different output, check your bash profile to make sure that your system is using the expected PATH. If your version of `chainctl` is a few weeks or months old, you may consider updating it by following the steps above so that you can use the most up to date version.

With `chainctl` successfully installed, we can continue through the demo.

## Step 2 — Check IAM group

Chainguard provides a way to organize Policies and Clusters into a hierarchy of **groups** through its [Identity and Access Management (IAM) model](../overview-of-enforce-iam-model). Chainguard Enforce provides a rich IAM model similar to those available through AWS and GCP.

Each Chainguard Policy needs to be associated with a group, and will be effective for that group as well as all the groups descending from it. Each Cluster needs to be associated with a group and will be enforced based on that group’s policies.

When you are invited to Chainguard Enforce, your account will already be associated with a group. You can check which group or groups you belong to, and grab the ID of the group with `chainctl`. 

```sh
chainctl iam groups ls -o table
```

You may be asked to authenticate to the Chainguard Enforce platform through an OIDC flow within a browser window. Go through the authentication by selecting the relevant accounts. 

You’ll receive output in the form of a table of your current group (or groups), similar to the following.

```
                     ID                    |       NAME          | DESCRIPTION  
-------------------------------------------+---------------------+--------------
  b9adda06841c1d34dfa73d5902ed44b5448b7958 | enforce-demo-group  |         
```

> **Note**: If you don't receive output like the above at all, you can create a new group by running `chainctl iam groups create --no-parent` to create a new group. After group creation, you can run `chainctl iam groups ls -o table` again.

Let’s create a variable that stores that ID for later steps in the tutorial. Replace `$GROUP_ID` below with the relevant ID; for exmaple, in the case of `enforce-demo-group` above, you would enter `b9adda06841c1d34dfa73d5902ed44b5448b7958` instead of `$GROUP_ID` in the command below. 

```sh
export GROUP=$GROUP_ID
```

You can learn more about our IAM model by reading our [Overview of Chainguard Enforce IAM](../overview-of-enforce-iam-model) article. This document will provide you with guidance on creating a group hierarchy that enables policies to be inherited from parent groups, and discrete policies for different groups depending on your needs.

## Step 3 — Prepare Kubernetes cluster

In order to put Chainguard Enforce into action within a cluster, we’ll now create a Kubernetes cluster using kind. For demonstration purposes, we will name our cluster `enforce-demo` by passing that to the `--name` flag, but you may opt to use an alternate name. 

```sh
kind create cluster --name enforce-demo
```

Install the Chainguard Enforce agent in your cluster:

```sh
chainctl cluster install --group=$GROUP --private --context kind-enforce-demo
```

 Once everything is set up, your terminal output will indicate that the cluster was successfully configured. We now have a Kubernetes cluster setup that’s running an application.

## Step 4 — Create a security policy

At this point, we want to roll out a policy ensuring that our development teams only deploy containers that have signatures and SBOMs without disruption.

To achieve this, we will create a new policy to require that only signed containers with SBOMs are deployed. We’ll associate a `sample-policy.yaml` file with the demo group in our IAM.

```sh
cat > sample-policy.yaml <<EOF
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: sample-policy
spec:
  images:
  - glob: "ghcr.io/chainguard-dev/*/*"
  - glob: "ghcr.io/chainguard-dev/*"
  - glob: "index.docker.io/*"
  - glob: "index.docker.io/*/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
      identities:
        - issuer: "*"
          subject: "*"
EOF
```

This policy creates a cluster image policy with the Sigstore beta API, and with Fulcio as a keyless authority. Here, we are requiring not only that Chainguard demo images be signed, but that all images from Docker be signed as well.

We have already set up the `GROUP` variable in with the group we created above in Step 2. Let’s now associate this new policy with that group.

```sh
chainctl policies apply -f sample-policy.yaml --group=$GROUP
```

You should get feedback about the group selected and that the policy was applied, similar to the following.

```
                             ID                             |     NAME      | DESCRIPTION  
------------------------------------------------------------+---------------+--------------
  a4de00fd08b377db719e52b0b19f58bc7ac5b45e/f265297c59250570 | sample-policy |  
```

We have confirmed that we’ve created the **sample-policy** based on the `sample-policy.yaml` file, and we are applying it to the demo group that we have set up in our environment. We can ensure that everything is as expected by listing the policies with `chainctl`. Note that you can pass `policy` or `policies` to the command.

```sh
chainctl policies ls
```

Here, you’ll get output on the policy you created as well as other policies that come with Chainguard Enforce. 

You should now be able to review the policy that you set up. With this policy described and connected to our group, we are ready to install Chainguard Enforce into our cluster to gain insight into where our cluster currently stands from a security perspective.

## Step 5 — Inspect compliance of containers

Under the hood, Chainguard Enforce leverages upstream Sigstore components like `ClusterImagePolicy`, a Kubernetes CustomResourceDefinition (CRD). Verify that the **sample-policy** was distributed to the cluster by using `kubectl`.

```sh
kubectl get clusterimagepolicies
```

We’ll get feedback that the **sample-policy** was distributed and how long ago.

```
NAME              AGE
sample-policy     68s
```

Next, verify the compliance records of containers via the CLI.

First, obtain the cluster ID and load it into a variable for usage. We are using `kubectl` to get an UUID (universally unique identifier) that Chainguard Enforce uses to identify the agent running on your cluster.

```sh
export CLUSTER_ID=$(chainctl cluster list -o json | jq -r '.items[0].name')
```

With this set up, we can run the following command to list the records of the scanned images.

```sh
chainctl cluster records list $CLUSTER_ID
```

If you didn’t specify the `$CLUSTER_ID`, the CLI will ask you to select from a menu instead.

Your output may be wide, and may have some extra lines. From this output, you should be able to determine the different categories of containers on your cluster, including containers from the vendor (such as GKE or EKS), the Chainguard agent, and the application image itself.

Let’s step through adding new images to the cluster to see how the policy is working. We’ll begin by deploying a generic NGINX image.


```sh
kubectl create deployment nginx --image=nginx
```

Give this some time (a few seconds up to a few minuts) to populate and then check what’s running now that we have a new image in the cluster.

```sh
chainctl cluster records list $CLUSTER_ID
```

You should get feedback that this fails the policy. That is because this generic NGINX image has neither a signature nor an SBOM. 

```
                              IMAGE                             |        POLICIES        |   WORKLOADS   | LAST SEEN  
----------------------------------------------------------------+------------------------+---------------+------------
  index.docker.io/library/nginx@sha256:0b9700…                  | sample-policy:fail:11s | Pod:1         | 82s

```

Next, let’s pull in an image that has an SBOM and signature. This is an NGINX image from Chainguard.

```sh
kubectl create deployment good-nginx --image=ghcr.io/chainguard-dev/nginx-image-demo
```

Again, check the output with `chainctl cluster records list $CLUSTER_ID`.


```
                              IMAGE                             |        POLICIES        |   WORKLOADS   | PACKAGES | LAST SEEN | LAST REFRESHED  
----------------------------------------------------------------+------------------------+---------------+----------+-----------+-----------------
  ghcr.io/chainguard-dev/nginx-image-demo@sha256:4b3990…        | sample-policy:pass:2s  | Pod:1         | apk:45   | 47s       | sbom:1s         
                                                                |                        |               |          |           | sig:2s  

 ```
 
This image passes the policy we set up above because it has both an SBOM and a signature.

## Step 6 – Enforce policy

We have improved our compliance by introducing and requiring a signing and SBOM policy. We now want to enforce this policy requirement. We can use `kubectl` and `namespace` label selectors to achieve this.

```sh
kubectl label ns default policy.sigstore.dev/include=true --overwrite
```

We can check that our policy is enforced by trying to run an unsigned image. We’ll use an unsigned Ubuntu image as an example.

```sh
kubectl run not-signed --image=ubuntu
```

You’ll receive output that this attempt at running an unsigned image has been rejected.

```
Error from server (BadRequest): admission webhook "enforcer.chainguard.dev" denied the request: validation failed: failed policy: sample-policy
```

Congratulations! You now have a policy in place to install Cosign, sign container images, and enforce that only signed images are deployed.

## Clean up and next steps

If you would like, you can now clean up your work by uninstalling `chainctl` from the cluster.

```sh
chainctl cluster uninstall
```

You may also want to delete the kind cluster you created.

```sh
kind delete cluster --name enforce-demo
```

To learn more visit our [Chainguard Enforce for Kubernetes](../) documentation page.

If you would like to learn about how you can use this product alongside signing Git commits, check out [Chainguard Enforce for Git](../../chainguard-enforce-github/). 

You can read all about software supply chain security on[Chainguard Academy](https://edu.chainguard.dev). 
