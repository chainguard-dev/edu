---
title: "Chainguard Enforce on Cloud Shell User Onboarding"
type: "article"
lead: "Setup of Chainguard Enforce with Google Cloud Shell and Kind"
description: "Set up Chainguard Enforce with Google Cloud Shell and Kind"
date: 2022-15-07T15:22:20+01:00
lastmod: 2022-15-07T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "enforce-kubernetes"
weight: 620
toc: true
---

Chainguard Enforce is a supply chain security solution for containerized workloads. Enforce enables you to build, manage, ensure continuous compliance, and enforce policies that protect organizations from supply chain threats. Using open source projects and standards that are trusted by the community — like Cosign and Fulcio from the Sigstore project — Chainguard Enforce offers a robust approach to securing your workloads. 

This guide will walk you through a demonstration of Chainguard Enforce on a Kubernetes cluster running on Google Cloud Platform (GCP). We will be using Enforce to achieve the following:

* **Policy management** — we will create a policy and show it being applied to the cluster, this will involve the use of signed containers and SBOMs (software bills of materials)
* **Observation and monitoring** — we will use the chainctl command line tool to understand our images from a security standpoint
* **Automation** — we will use GitHub Actions to call and implement our policy automatically
* **Enforce** — we will verify that Chainguard Enforce stops the deployment of an unsigned image

We will walk through a product journey together in this guide — from setting up an example cluster, to drafting a policy and observing how it behaves, to improving the policy, and finally enforcing that policy. Ultimately, our goal is to improve our software security in deployment contexts by enforcing the use of signed containers and rejecting any containers that are unsigned. 

## Create a Kind cluster

Open up a [Google Cloud Shell](https://console.cloud.google.com) session and set up a Kubernetes [kind](https://kind.sigs.k8s.io/) cluster. We recommend opening up an ephemeral session so that what you create does not persist. 

```sh
kind create cluster
```

You can leave this going and open up a new tab.

## Install chainctl

Our command line interface (CLI) tool, chainctl, will help you interact with the account model that Chainguard Enforce provides, and enable you to make queries into the state of your clusters and policies registered with the platform. The tool uses the familiar `<context> <noun> <verb>` style of CLI interactions For example, to list groups within the context of Chainguard Identity and Access Management (IAM) groups, you can run `chainctl iam groups list` to receive relevant output. 

In a second terminal window, you can pull chainctl down.

```sh
wget -O chainctl "https://storage.googleapis.com/us.artifacts.chainguard-poc.appspot.com/chainctl_$(uname -s)_$(uname -m)"
```

Next, we need to elevate the permissions and add chainctl to our PATH so that it can execute as needed.

```sh
chmod +x chainctl
alias chainctl=$PWD/chainctl
```

You can verify that everything was set up correctly by checking the chainctl version.

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

GitVersion:    6b9bcae
GitCommit:     6b9bcaeb3fd2cf8d3ec3febc81766df14dec905c
GitTreeState:  clean
BuildDate:     2022-07-13T06:19:55Z
GoVersion:     go1.17.12
Compiler:      gc
Platform:      linux/amd64
```

If you received different output, run `which chainctl` to check that you are using the right chainctl. 

If your version of chainctl is a few weeks or months old, you may consider updating it so that you can use the most up to date version. You can update by following the steps in this section again.

With chainctl successfully installed, we can continue through the demo.

## Create an IAM group to try Enforce

Chainguard provides a way to organize Policies and Clusters into a hierarchy of **groups** through its Identity and Access Management (IAM) model. Chainguard Enforce provides a rich IAM model similar to the likes of AWS and GCP. 

Each Chainguard Policy needs to be associated with a group, and will be effective for that group as well as all the groups descending from it. Each Cluster needs to be associated with a group and will be enforced based on that group’s policies.

Let’s begin by authenticating to the Chainguard Enforce platform.

```sh
chainctl auth login
```

A web browser window will open to prompt you to login via Google’s OIDC flow (more methods to authenticate are coming soon). Select an account with which you wish to register. Once authenticated, you can create a group.

Now you can create a root group for your organization. This will be tied to the account you just used to authenticate to Chainguard Enforce. 

You’ll next create a group. For demonstration purposes, we’re using `demo-test-group` as the name, but if you are persisting the group, you may want to use a name that is more meaningful to your use case. The `--no-parent` flag sets this up as a standalone group that can be a parent group to other child groups. 

```sh
chainctl iam groups create demo-test-group
```

You’ll be asked whether you want to continue. Press `y`. Once the group is created you’ll receive output that the group exists with a relevant ID. 

Let’s create a variable that stores the ID of the group for later steps in the tutorial. Grab the ID number from the output you received upon group creation, and pass it to the variable.

```sh
export GROUPID=<ID-number-here>
```

Be sure to replace the <Group ID> above with the actual string you have in the ID output from your terminal window when you created the group. You can get the ID at any time by running chainctl iam groups list -o table.

You can learn more about our IAM model by reading our [Overview of Chainguard Enforce IAM](/overview-of-enforce-iam-model). This document will provide you with guidance on creating a group hierarchy that enables policies to be inherited from parent groups, and discrete policies for different groups depending on your needs. 

With the group set up, you can install Chainguard Enforce.

```sh
chainctl cluster install --group=$GROUPID
```

You’re now ready to set up a policy that you can enforce within your cluster.

## Create a policy to require signatures on images

At this point, we want to roll out a policy ensuring that our development teams only deploy signed containers with no disruptions. 

We can check and see any policies that currently exist first. 

```sh
chainctl policies ls
```

You can review the existing policy.

```sh
chainctl policy list -o json \
    | jq '[.[] | select(.name == "chainguard-policy")][0].document' \
    | jq -r
```

Policies will be propagated to all clusters associated with the group we invited the cluster to, so every new cluster onboarded will automatically inherit these policies.

```
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: chainguard-policy
spec:
  images:
  # Chainguard images are signed.
  - glob: "us.gcr.io/chainguard-staging/*"
  - glob: "us.gcr.io/chainguard-poc/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
```

_We have decided we want to roll out a policy that developers only deploy signed containers, but we don’t actually know where we stand today!_

Create a sample policy. Open the text editor in Google Cloud Shell by clicking the **Open Editor** button, and then create a new file.

```
apiVersion: policy.sigstore.dev/v1alpha1
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
```

This policy creates a cluster image policy with the Sigstore alpha API, and with Fulcio as a keyless authority. Here, we are requiring not only that Chainguard demo images be signed with an SBOM, but that all images from Docker be signed with an SBOM as well. 

Save the file as `sample-policy.yaml`.

Return to the terminal and apply the new policy.

```sh
chainctl policies apply -f sample-policy.yaml --group $GROUPID
```

At this point, the policy is associated with the group we set up.

## Review how the policy is enforced

Now that the policy is running in the group we set up, we can review what is running in our cluster. 

```sh
chainctl cluster records ls   $(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

Let’s step through adding new images to the cluster to see how the policy is working. 

First, we’ll deploy a generic NGINX image.

```sh
kubectl create deployment nginx --image=nginx
```

Give this a few seconds to populate and then check what’s running again.

```sh
chainctl cluster records ls   $(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

You should get feedback that this fails the policy. That is because this generic NGINX image has neither a signature nor an SBOM. 
```
                                                              IMAGE                                                              | LAST SEEN | LAST REFRESHED |    POLICIES
---------------------------------------------------------------------------------------------------------------------------------+-----------+----------------+------------------------
  index.docker.io/library/nginx:latest@sha256:2bcabc23b45489fb0885d69a06ba1d648aeda973fae7bb981bafbb884165e514                   | 13s       |                | sample-policy:fail:4s
```
  
Check the output again using `chainctl cluster records ls`.

You’ll get feedback that this has an SBOM but no signature, thus it still fails the policy.

```sh
kubectl create deployment sbom-log4j --image=ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0
```

Check the output again using `chainctl cluster records ls`.

You’ll get feedback that this has an SBOM but no signature, thus it still fails the policy.


```
                                                              IMAGE                                                              | LAST SEEN |  LAST REFRESHED  |        POLICIES
---------------------------------------------------------------------------------------------------------------------------------+-----------+------------------+-------------------------
  ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0@sha256:ba4037061b76ad8f306dd9e442877236015747ec42141caf504dc0df4d10708d       | 16s       | sbom:8s          | sample-policy:fail:8s
```

Finally, let’s pull in an image that has an SBOM and signature. This is an NGINX image from Chainguard. 

```sh
kubectl create deployment good-nginx --image=ghcr.io/chainguard-dev/nginx-image-demo
```

Again, check the output with `chainctl cluster records ls`.

You’ll now get feedback that this passes the policy with both an SBOM and signature.


```
                                                              IMAGE                                                              | LAST SEEN |  LAST REFRESHED  |        POLICIES
---------------------------------------------------------------------------------------------------------------------------------+-----------+------------------+-------------------------
  ghcr.io/chainguard-dev/nginx-image-demo:latest@sha256:0fb2d846fece2561501a912301c255bcd1e328f682f38b312011705595e9634e         | 52s       | sig:40s sbom:40s | sample-policy:pass:40s
 ```
 
This image passes the policy because it has both an SBOM and a signature.

At this point you can uninstall chainctl from the cluster. 

```sh
chainctl cluster uninstall
```

You can now exit Google Cloud Shell.
