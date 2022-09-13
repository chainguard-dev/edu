This walkthrough will quickly get Chainguard Enforce installed and running locally — from setting up an example cluster, to drafting a policy and observing how it behaves, to improving the policy, and finally enforcing that policy. If you'd like more information on working with Chainguard Enforce, we encourage you to to check out the [detailed tutorial on Chainguard Academy](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-enforce-user-onboarding/).


## Prerequisites

Before running Chainguard Enforce locally, you’ll need to ensure you have the following installed:

* **`kind`** — install kind for local Kubernetes orchestration via the [kind install docs][kind].
* **`curl`** — follow the relevant [curl download docs](curl) for your machine.
* **`jq`**  — visit the [jq downloads page](jq) to set it up.
* **Docker** — [install for your machine](https://docs.docker.com/get-docker/) and run it in order to complete this tutorial.

[kind]: https://kind.sigs.k8s.io/docs/user/quick-start/#installation
[curl]: https://curl.se/download.html
[jq]: https://stedolan.github.io/jq/download/

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


## Step 2 — Create an IAM group to try Enforce

Authenticate to the Chainguard Enforce platform.

```sh
chainctl auth login
```

A web browser window will open to prompt you to log in via an OIDC flow. Select the account you wish to register with and create a group.  For demonstration purposes, we’ll create a group called `enforce-demo-group`, but feel free to replace it with an alternate name. 

```sh
chainctl iam groups create enforce-demo-group --no-parent
```

You’ll be asked whether you want to continue and to confirm logging in again. Press `y` in response to each prompt.


Next, find the ID for the group you just created.

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


## Step 3 — Prepare your Kubernetes cluster

In order to put Chainguard Enforce into action within a cluster, we'll now create a Kubernetes cluster using kind. We will name our cluster `enforce-demo` by passing that to the `--name` flag, but you may want to use another name.

```sh
kind create cluster --name enforce-demo
```

Inside the Kubernetes cluster, create a Pod to run the unsigned image.

```sh
chainctl cluster install --group=$GROUP --private --context kind-enforce-demo
```


## Step 4 — Create a policy to require signatures on images

Now we will associate a `sample-policy.yaml` file with the demo group in our IAM.

```sh
cat > sample-policy.yaml <<EOF
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
EOF
```

This policy creates a cluster image policy with the Sigstore alpha API, and with Fulcio as a keyless authority. Here, we are requiring that all images from container registries be signed.

Let’s now associate this new policy with our group.

```sh
chainctl policies apply -f sample-policy.yaml --group=$GROUP
```

You will get feedback about the group selected and that the policy was applied.

```
                             ID                             |     NAME      | DESCRIPTION  
------------------------------------------------------------+---------------+--------------
  a4de00fd08b377db719e52b0b19f58bc7ac5b45e/f265297c59250570 | sample-policy | 
```

Now we can ensure that everything is as expected by listing the policies with `chainctl`.

```sh
chainctl policies ls
```

A few policies will be in place in addition to the policy you just created. 

## Step 5 — Inspect compliance of containers

We can check that the **sample-policy** was distributed to the cluster by using `kubectl`.

```sh
kubectl get clusterimagepolicies
```

We’ll get feedback that the **sample-policy** was distributed and how long ago.

```
NAME                AGE
sample-policy     68s
```

Next, we’ll verify the compliance records of containers via the CLI. First, obtain the cluster ID and load it into a variable for usage. 

```sh
export CLUSTER_ID=$(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

With this set up, we can run the following command to list the records of the scanned images.

```sh
chainctl cluster records list $CLUSTER_ID
```

From this output, you will be able to determine the different categories of containers on your cluster, including containers from the vendor, the Chainguard agent, and the application image itself.

Let’s deploy a new image, starting with a generic NGINX image.

```sh
kubectl create deployment nginx --image=nginx
```

Give this a few seconds to populate and then check what’s running again.

```sh
chainctl cluster records list $CLUSTER_ID
```

You should get feedback that this fails the policy because this generic NGINX image has neither a signature nor an SBOM.

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

You’ll get feedback that this passes the policy with both an SBOM and signature.


```
                              IMAGE                             |        POLICIES        |   WORKLOADS   | PACKAGES | LAST SEEN | LAST REFRESHED  
----------------------------------------------------------------+------------------------+---------------+----------+-----------+-----------------
  ghcr.io/chainguard-dev/nginx-image-demo@sha256:4b3990…        | sample-policy:pass:2s  | Pod:1         | apk:45   | 47s       | sbom:1s         
                                                                |                        |               |          |           | sig:2s  

 ```
 
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

