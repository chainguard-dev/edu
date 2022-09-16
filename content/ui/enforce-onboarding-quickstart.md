This walkthrough will quickly get Chainguard Enforce installed and running locally — from setting up an example cluster, to drafting a policy and observing how it behaves, to improving the policy, and finally enforcing that policy. If you'd like more information on working with Chainguard Enforce, we encourage you to to check out the [detailed tutorial on Chainguard Academy](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-enforce-user-onboarding/).


## Prerequisites

Before running Chainguard Enforce locally, you’ll need to ensure you have the following installed:

* **`kind`** — install kind for local Kubernetes orchestration via the [kind install docs](https://kind.sigs.k8s.io/docs/user/quick-start/#installation).
* **`curl`** — follow the relevant [curl download docs]( https://curl.se/download.html) for your machine.
* **`jq`**  — visit the [jq downloads page](https://stedolan.github.io/jq/download/) to set it up.
* **Docker** — [install for your machine](https://docs.docker.com/get-docker/) and run it in order to complete this tutorial.

If you are running macOS, you’ll need to ensure you are using bash version 4 or higher, which is not preinstalled in the machine. Please [follow our guide](https://edu.chainguard.dev/open-source/update-bash-macos/) on how to update your version if you are getting version 3 or older when you run `bash --version`.


## Step 1 — Install chainctl

Create a new directory called `enforce-demo`.

```sh
mkdir ~/enforce-demo && cd $_
```

To simplify later commands, create the following variables and export them to be used by child processes.

```sh
export BUCKET="us.artifacts.prod-enforce-fabc.appspot.com"
export BASE_URL="https://storage.googleapis.com/${BUCKET}"
```

Then use `curl` to pull the application down.

```sh
curl -o chainctl "$BASE_URL/chainctl_$(uname -s)_$(uname -m)"
```

Next, elevate the permissions of chainctl so that it can execute as needed.

```sh
chmod +x chainctl
```

Finally, add chainctl to our PATH so that we can use chainctl on the command line.

```sh
alias chainctl=$PWD/chainctl
```

You can verify that everything was set up correctly by checking the chainctl version.

```sh
chainctl version
```
```
   ____   _   _      _      ___   _   _    ____   _____   _
  / ___| | | | |    / \    |_ _| | \ | |  / ___| |_   _| | |
 | |     | |_| |   / _ \    | |  |  \| | | |       | |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___    | |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control

GitVersion:    2c1ff2c
GitCommit:     2c1ff2cf9e038e1fd3bbc9ec01df619e23b4a27a
GitTreeState:  clean
BuildDate:     2022-09-12T17:50:34Z
GoVersion:     go1.18.6
Compiler:      gc
Platform:      darwin/arm64
```


## Step 2 — Check your IAM group

Authenticate to the Chainguard Enforce platform with the invite code you have received.

```sh
chainctl auth login --invite-code <YOUR-CODE>
```

A web browser window will open to prompt you to log in via an OIDC flow. 

Once authenticated, you can check for the ID of the your group.

```sh
chainctl iam groups ls -o table
```

You'll receive output in the form of a table of your current groups, similar to the following.

```
                     ID                    |       NAME       | DESCRIPTION  
-------------------------------------------+------------------+--------------

  b9adda06841c1d34dfa73d5902ed44b5448b7958 | enforce-demo-group |              
```

Create a variable that stores the ID in the left column for later steps in the tutorial. In the following command, replace `$GROUP_ID` with the relevant ID.

```sh
export GROUP=$GROUP_ID
```

In the UI, you will also be able to check for any groups to which you belong from the filter modal, which you can open by clicking on the icon.

<screenshot>

At any time, you can check here to see the groups to which you belong and filter resources based on group ownership.

## Step 3 — Prepare your Kubernetes cluster

In order to put Chainguard Enforce into action within a cluster, we'll now create a Kubernetes cluster using kind. We will name our cluster `enforce-demo` by passing that to the `--name` flag, but you may want to use another name.

```sh
kind create cluster --name enforce-demo
```

Install the Enforce agent in your cluster:

```sh
chainctl cluster install --group=$GROUP --private --context kind-enforce-demo
```

If you navigate to the **Clusters** in the UI, you should now see your cluster in the cluster list table.

<screenshot>

From here, you can explore a detailed view of the cluster, including any policies that apply to it.


## Step 4 — Create a policy to require signatures on images

You can create a policy directly from the UI by navigating to the **Policies** tab. In the policy list table menu, you will see a **Create policy** button. Clicking this button will open a dropdown menu, which will allow you to create a policy from scratch or use a predefined template, to require that images have signatures.

For now, we can create a policy using the **Custom** option from the dropdown.

<screenshot>

On the policy create page, ensure that the correct group is displayed in the group field, `enforce-demo`. Then paste the following code into the code editor:

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

This policy creates a cluster image policy with the Sigstore alpha API, and with Fulcio as a keyless authority. Here, we are requiring that all images from container registries be signed.

After you click the **Publish** button at the bottom of the create modal, your new policy will be active. The next time you land on the policy list page, you will see the policy listed, as well as any violations it has and its group hierarchy.

You can also list your policies with `chainctl`.

```sh
chainctl policies ls
```

A few policies will be in place in addition to the policy you just created.

## Step 5 — Inspect compliance of containers

The first place we can look for information about container compliance is the clusters main page, which you can find by clicking on the **Clusters** tab in the main navigation menu.

With our new policy, `sample-policy`, in place, information about policy compliance should be visible in the **Policy** column, next to the cluster name.

<screenshot>

You can also find more information about policy compliance by clicking on either of the cards in the cluster list page, which will take you to views that provide more information on any policies that have failed, and the exact images that are failing policies.

Additionally, the buttons on top of the cluster table will allow you to filter your clusters by compliance.

<screenshot>

You can also check that the **sample-policy** was distributed to the cluster by using `kubectl`.

```sh
kubectl get clusterimagepolicies
```

We’ll get feedback that the **sample-policy** was distributed and how long ago.

```
NAME                AGE
sample-policy     68s
```

## Step 6 — Test new record compliance

So far, the information we have been seeing about our cluster is information about the containers and images in the cluster's control plane.

Now, let’s deploy a new image, starting with a generic NGINX image.

```sh
kubectl create deployment nginx --image=nginx
```

Give this a few seconds to populate and then check what’s running again by navigation to the cluster's detail page. You can do this by clicking on the cluster's name from the cluster list table.

In the **Policy violations** table, you will see the image listed.

<screenshot>

Clicking on the **Show diagnostic** button in the table will provide more information about the violation.

<screenshot>

Next, let’s pull in an image that has an SBOM and signature. This is an NGINX image from Chainguard.

```sh
kubectl create deployment good-nginx --image=ghcr.io/chainguard-dev/nginx-image-demo
```
You won't see this image listed in the violations table, but if you navigate to the **Images** table, you will see it there.

<screenshot>

This image passes the policy because it has both an SBOM and a signature.


## Step 6 – Enforce policy

At this point, let’s enforce this policy requirement. We can use `kubectl` and the `namespace` label selectors to do this.

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

Congratulations, you have completed onboarding to Chainguard Enforce!

If you would like, you can now clean up your work by uninstalling `chainctl` and then deleting the cluster.

```sh
chainctl cluster uninstall
```

```sh
kind delete cluster --name enforce-demo
```

To learn more about Chainguard Enforce, please review our documentation and other resources on Chainguard Academy.
