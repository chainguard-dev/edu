---
title: "Chainguard Enforce User Onboarding"
description: "Walkthrough of Chainguard Enforce"
lead: ""
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard"
weight: 100
toc: true
---

Chainguard Enforce is a supply chain security solution for containerized workloads. Enforce enables you to build, manage, ensure continuous compliance, and enforce policies that protect organizations from supply chain threats. Using open source projects and standards that are trusted by the community — like Cosign and Fulcio from the Sigstore project — Chainguard Enforce offers a robust approach to securing your workloads.

This guide will walk you through a demonstration of Chainguard Enforce on a Kubernetes cluster running on Google Cloud Platform (GCP). We will be using Enforce to achieve the following:

* Policy management — we will create a policy and show it being applied to the cluster, this will involve the use of signed containers and SBOMs (software bills of materials)
* Observation and monitoring — we will use the chainctl command line tool to understand our images from a security standpoint
* Automation — we will use GitHub Actions to call and implement our policy automatically
* Enforce — we will verify that Chainguard Enforce stops the deployment of an unsigned image

We will walk through a product journey together in this guide — from setting up an example cluster, to drafting a policy and observing how it behaves, to improving the policy, and finally enforcing that policy. Ultimately, our goal is to improve our software security in deployment contexts by enforcing the use of signed containers and rejecting any containers that are unsigned.

## Prerequisites

Before running Chainguard Enforce on GCP, you’ll need to ensure you have the following installed:

* **gcloud CLI** tool — to interact with GCP infrastructure on the command line. You can download and install gcloud for your relevant operating system by following the [Installing the gcloud CLI guide](https://cloud.google.com/sdk/docs/install).
* **[Wget](https://www.gnu.org/software/wget/)** — to retrieve files from the web.
    * On Ubuntu or Debian Linux, you can install Wget with `apt install wget`
    * On Red Hat, Fedora, or CentOS Linux, you can install it with `dnf install wget`
    * On macOS, install with Homebrew by running `brew install wget`
    * On Windows, use Chocolatey to install Wget with `choco install wget` or get Wget binaries via [SourceForge](http://gnuwin32.sourceforge.net/packages/wget.htm)
* **[jq](https://stedolan.github.io/jq/)**  — to process JSON on the CLI.
    * On Ubuntu or Debian Linux, you can install jq with `apt install jq`
    * On Red Hat, Fedora, or CentOS Linux, you can install it with `dnf install jq`
    * On macOS, install with Homebrew by running `brew install jq`
    * On Windows, use Chocolatey to install Wget with `choco install jq`

One last note — if you are running macOS, you’ll need to ensure you are using bash version 4 or higher, which is not preinstalled in the machine. Please follow our guide on how to update your version if you are getting version 3 or below when you run `bash --version`.

With gcloud CLI, Wget, and jq installed you’re ready to begin.

## Step 1 — Install chainctl

Our command line interface (CLI) tool, chainctl, will help you interact with the account model that Chainguard Enforce provides, and enable you to make queries into the state of your clusters and policies registered with the platform. The tool uses the familiar `<context> <noun> <verb>` style of CLI interactions For example, to list groups within the context of Chainguard Identity and Access Management (IAM) groups, you can run `chainctl iam groups list` to receive relevant output.

To install chainctl, let’s create variables that simplify our commands and export them to be used by child processes.

```sh
export BUCKET="us.artifacts.chainguard-poc.appspot.com"
export BASE_URL="https://storage.googleapis.com/${BUCKET}"
```

Here, we are using the bucket of our Chainguard POC, and calling that bucket within the base URL of our application hosted by Google.

We’ll use the `wget` command to pull the application down.

```sh
wget -O chainctl "$BASE_URL/chainctl_$(uname -s)_$(uname -m)"
```

Next, we need to elevate the permissions of chainctl so that it can execute as needed.

```sh
chmod +x chainctl
```

Finally, let’s add chainctl to our PATH so that we can use chainctl on the command line.

```sh
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

GitVersion:    f1165a9
GitCommit:     f1165a93c277766cdf60c998bc2847236b92c705
GitTreeState:  clean
BuildDate:     2022-05-04T17:21:47Z
...
…
```

If you received different output, check your bash profile to make sure that your system is using the expected GOPATH. If your version of chainctl is a few weeks or months old, you may consider updating it so that you can use the most up to date version.

With chainctl successfully installed, we can continue through the demo.

## Step 2 — Create an IAM group to try Enforce

Chainguard provides a way to organize Policies and Clusters into a hierarchy of **groups** through its Identity and Access Management (IAM) model. Chainguard Enforce provides a rich IAM model similar to the likes of AWS and GCP.

Each Chainguard Policy needs to be associated with a group, and will be effective for that group as well as all the groups descending from it. Each Cluster needs to be associated with a group and will be enforced based on that group’s policies.

Let’s begin by authenticating to the Chainguard Enforce platform.

```sh
chainctl auth login
```

A web browser window will open to prompt you to login via Google’s OIDC flow (more methods to authenticate are coming soon). Select an account with which you wish to register. Once authenticated, you can create a group.

Now you can create a root group for your organization. This will be tied to the account you just used to authenticate to Chainguard Enforce.

Use a group name that will be meaningful to you, and replace `$GROUP_NAME` in the command below with the relevant name. The `--no-parent` flag sets this up as a standalone group that can be a parent group to other child groups.

```sh
chainctl iam groups create $GROUP_NAME --no-parent
```

You’ll be asked whether you want to continue. Press `y`. Once the group is created you’ll receive output that the group exists with a relevant ID.

```
Continue? [Y,n]: y
                                      ID                                   |        NAME        | DESCRIPTION
---------------------------------------------------------------------------+--------------------+--------------
  ... <Group ID> ...                                                       | tutorial-group     |
```


To invite others to your group, you can generate invite codes with the command below.

```sh
chainctl iam invite create $GROUP_ID
```

You will be prompted for the scope that the invite code will be granted.  After selecting the role bindings, the invite code will be generated.

To invite team members, auditors, or others to your desired groups, securely distribute the invite code and have them log in with chainctl as follows.

```sh
chainctl auth login --invite-code $INVITE_CODE
```

Let’s create a variable that stores the ID of the group for later steps in the tutorial.

```sh
export SAMPLE_GROUP=<Group ID>
```

Be sure to replace the `<Group ID>` above with the actual string you have in the ID output from your terminal window when you created the group. You can get the ID at any time by running `chainctl iam groups list`.

You can learn more about our IAM model by reading our Overview of Chainguard Enforce IAM. This document will provide you with guidance on creating a group hierarchy that enables policies to be inherited from parent groups, and discrete policies for different groups depending on your needs.

## Step 3 — Prepare your Kubernetes cluster

For simplicity with regard to image pull secrets, we will perform this tutorial using a public container registry. After you go through the tutorial once, check out additional information after the last step to use your own image pull secrets.

```sh
export TUTORIAL_IMAGE=ttl.sh/$USER/enforce-tutorial/busybox
docker pull busybox
docker tag busybox $TUTORIAL_IMAGE

docker push $TUTORIAL_IMAGE
```

Inside your Kubernetes cluster, let’s create a Pod to run the unsigned image.

```sh
kubectl run example --image=$TUTORIAL_IMAGE
```

We now have a Kubernetes cluster setup that’s running an application.

## Step 4 — Create a policy to require signatures on images

At this point, we want to roll out a policy ensuring that our development teams only deploy signed containers with no disruptions.

Now we will create a new policy to require that developers only deploy signed containers. We’ll associate a `sample-policy.yaml` file with the demo group in our IAM.

```sh
cat > sample-policy.yaml <<EOF
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: sample-policy
spec:
  images:
  - glob: "gcr.io/chainguard-demo/*"
  - glob: “ttl.sh/*”
  - glob: "index.docker.io/*"
  - glob: "index.docker.io/*/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
EOF
```

This policy creates a cluster image policy with the Sigstore alpha API, and with Fulcio as a keyless authority. Here, we are requiring not only that Chainguard demo images be signed, but that all images from Docker be signed as well.

We have already set up the `SAMPLE_GROUP` variable in with the group we created above in Step 2. Let’s now associate this new policy with that group.

```sh
chainctl policies create sample-policy \
    --group $SAMPLE_GROUP \
    -f sample-policy.yaml
```

You should get feedback that a policy was created, similar to the following.

```
Created policy 3e4c5a761d8a4837ea9aa1c1839c7775a702f238/1957c887aa051b92
```

We have confirmed that we’ve created the **sample-policy** based on the `sample-policy.yaml` file, and we are applying it to the demo group that we have set up in our environment. We can ensure that everything is looking as we expect by listing the policies with chainctl. Note that you can pass `policy` or `policies` to the command.

```sh
chainctl policies ls
```

You should now be able to review the policy that you set up. With this policy described and connected to our group, we are ready to install Chainguard Enforce into our cluster so that we can gain insight into where our cluster currently stands.

## Step 5 — Install Chainguard Enforce

Now that we have a policy created that we would like to roll out, we can install Chainguard Enforce so that we can use it to check our team’s compliance with the new policy. This will ensure that our processes are improved through first checking — and then enforcing — that containers are signed.

We’ll use chainctl to install Chainguard Enforce into our cluster, and at the same time assign the cluster to the `$SAMPLE_GROUP` that you created.

```sh
chainctl cluster install --group=$SAMPLE_GROUP
```

When you run this command, you’ll get a few lines of output that end with the confirmation that the cluster was successfully configured and that the temporary invite code was cleaned up, similar to the output below.

```
...
Cluster has been successfully configured with ID: 'ba5eba11-ba5e-ba11-aa6a-95fc2398fe16'
Cleaning up temporary invite code 3e4c5a761d8a4837ea9aa1c1839c7775a702f238/d43855cfa3a20a31...
```

With Chainguard Enforce installed to our group, we will immediately gain an understanding of what we have running. Let’s first review the clusters we currently have under chainctl’s management.

```sh
chainctl cluster ls
```

Depending on your cluster and group, you will get output of the multiple clusters that chainctl is running on.

## Step 6 — Inspect compliance of containers

We’ll first check that the **sample-policy** was distributed to our cluster.

Under the hood, we leverage upstream Sigstore components like the ClusterImagePolicy CRD.  We can check that the **sample-policy** was distributed to the cluster by using kubectl.

```sh
kubectl get clusterimagepolicies
```

We’ll get feedback that the **sample-policy** was distributed and how long ago.

```
NAME                AGE
sample-policy     68s
```

Next, we’ll verify the compliance records of containers via the CLI.

First, obtain the cluster ID and load it into a variable for usage. We are using kubectl to get an UUID that Chainguard uses to identify the agent running on your cluster.

```sh
export CLUSTER_ID=$(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

With this set up, we can run the following command to list the records of the scanned images.

```sh
chainctl cluster records list $CLUSTER_ID
```

If you didn’t specify the `$CLUSTER_ID`, the CLI will ask you to select from a drop-down instead.

Your output may be wide, and may have some extra lines. From this output, you should be able to determine the different categories of containers on your cluster, including containers from the vendor (such as GKE or EKS), the Chainguard agent, and the application image itself.

```
                CLUSTER                |                                                                     IMAGE                                                                     |        LAST SEEN         |         LAST REFRESHED
---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+---------------------------------
...
  d823a5fb-8335-4c17-aa6a-95fc2398fe16 | gcr.io/chainguard-demo/demo-app@sha256:aa3fe90bee1aa72caad355a18916eb0cb315697a0cee2bdbead4ccd50003b26c                                       | 2022-03-31T17:42:39.168Z | sbom:2022-03-31T17:42:47.47Z
...
```

You may notice that the Chainguard image also has one additional feature. In the above image output, we have confirmation that the **chainguard-demo** image has an SBOM associated with it. In the sample output above, it reads as `sbom:2022-03-31T17:42:47.47Z`.

Alternatively, you can run the following command to find out your cluster ID, and click on the corresponding cluster at [https://console.guak.dev/clusters](https://console.guak.dev/clusters) to see the same information using the Enforce Console. This will allow you to verify the compliance records of containers using the web UI.

```sh
kubectl get ns gulfstream -ojson | jq -r .metadata.uid
```

Whether you are checking via the CLI or the web UI, you should notice that the unsigned image has been flagged.

## Step 7 — Sign the unsigned image

As we now understand that one of the images is unsigned, we will now sign the image using Cosign. We’ll perform keyless signing using Fulcio which will rely on an OIDC authentication. This process will issue short-lived certificates that enable us to sign without needing to hold onto keys.

```sh
COSIGN_EXPERIMENTAL=1 cosign sign $TUTORIAL_IMAGE
```

After we run this, the Chainguard Enforce periodic continuous verification will check compliance with stated policies, and the flag about the out-of-policy unsigned image will be removed.

## Step 8 — Verify signing

Continuous verification will rescan policies to ensure that our update satisfies our sample-policy. At this point, when we list the records again, we should notice that cluster records are signed but without SBOMs.

```sh
chainctl cluster records list \
   $(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

You’ll receive output that the container was signed and validated.

```
Verification for gcr.io/chainguard-demo/demo-app@sha256:b6eb1074c8058171ae57db872530b3ab3f1bdfbea64b3390cbbd8b5d788ceb1a --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - Existence of the claims in the transparency log was verified offline
  - Any certificates were verified against the Fulcio roots.
...
```

Within the JSON file, you can notice that it was the GitHub Action that signed the image.

```
...
      "Issuer": "https://token.actions.githubusercontent.com",
      "Subject": "https://github.com/chainguard-dev/gke-demo/.github/workflows/release.yaml@refs/heads/main"
...
```

This was achieved through the keyless signing we completed in the previous step.

You can also check the Chainguard Enforce UI available via [https://console.guak.dev/](https://console.guak.dev/).

## Step 9 – Enforce policy

We have improved our compliance by introducing and requiring a signing policy. We now want to enforce this policy requirement. We can use kubectl and namespace label selectors to do this.

```sh
kubectl label ns default policy.sigstore.dev/include=true --overwrite
```

We can check that our policy is enforced by trying to run an unsigned image. We’ll use the Ubuntu image as an example.

```sh
kubectl run not-signed --image=ubuntu
```

You’ll receive output that this attempt at running an unsigned image has been rejected.

```
Error from server (BadRequest): admission webhook "enforcer.chainguard.dev" denied the request: validation failed: no matching signatures:
: spec.containers[0].image
index.docker.io/library/ubuntu@sha256:bea6d19168bbfd6af8d77c2cc3c572114eb5d113e6f422573c93cb605a0e2ffb
```

Congratulations! You now have a policy in place to install Cosign, sign container images, and enforce that only signed images are deployed.


## Customization options on the policy

### Enforce the identity of the signer

The following is an example of a policy that enforces signer identity.

```sh
cat > demo-policy.yaml <<EOF
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: policy-name
spec:
  images:
  - glob: "gcr.io/your-image-here/*"
  authorities:
  - keyless:
      identities: # <<<-- REPLACE the following with your OIDC provider & subject --> #
      - issuer: https://token.actions.githubusercontent.com
        subject: https://github.com/chainguard-dev/gke-demo/.github/workflows/release.yaml@refs/heads/main
EOF
```

Another example of OIDC issuer and subject.

```sh
      - issuer: https://accounts.google.com
        subject: your-gmail@gmail.com
```

## How to use private registries

Chainguard Enforce supports several methods of authenticating to private registries. Depending on your organization’s setup, you may leverage one or multiple of the supported authentication strategies.

### Generic private registries

To support the widest set of private registries, authentication via an `imagePullSecret` can be used. This is configured on a per-policy basis, and applies to all the images scoped to that policy.

#### From a private registry

If your images come from a completely private registry, first create an `imagePullSecret` in the **cosign-system** namespace:

```sh
kubectl create secret docker-registry regcreds -n cosign-system --docker-server=$privateregistry --docker-username=$username --docker-password=$password --docker-email=$email
```

> **NOTE**: It is important to ensure the secret is created in the cosign-system namespace, as this ensures the Chainguard Enforce agent can use this secret to authenticate images from all namespaces in the cluster.


From there, any policy defined that references images from `$privateregistry` can be linked to the appropriate `imagePullSecret` which is regcreds in this example.

```sh
cat > demo-policy-private-dockerhub.yaml <<EOF
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: policy-name
spec:
  images:
  - glob: "$privateregistry/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
    source:
      - oci: "$privateregistry"
        signaturePullSecrets:
          - name: regcreds
EOF
```

#### From Docker Hub

For images that come from a private namespace within Docker Hub (or any private registry), the credentials can be scoped to that specific namespace, rather than the whole registry.

Assuming the same regcreds secret as above, use the registry namespace to scope the credentials in each policy as follows:

```sh
cat > demo-policy-private-dockerhub.yaml <<EOF
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: policy-name
spec:
  images:
  - glob: "privatedockernamespace/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
    source:
      - oci: "index.docker.io/privatedockernamespace/image"
        signaturePullSecrets:
          - name: regcreds
EOF
```

> **NOTE**: For legacy Docker Hub reasons that have propagated to how container runtimes identify images, `privatedockernamespace/*` is equivalent to `index.docker.io/privatedockernamespace/*` —  both will work!

### Generic private registry using a pull secret

Associate GCR with an IAM group
Associate ECR with an IAM group




