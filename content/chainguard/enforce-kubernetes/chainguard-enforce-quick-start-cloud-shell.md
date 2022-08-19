---
title: "Chainguard Enforce Quickstart with Google Cloud Shell"
type: "article"
description: "Set up Chainguard Enforce quickly with Google Cloud Shell and Kind"
lead: "Quick setup of Chainguard Enforce using Kind and Cloud Shell"
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

Open a Google Cloud Shell Session

```sh
kind create cluster
```

Open a second terminal tab while Kind cluster is being created, we'll install chainctl and set it up.

```sh
wget -O chainctl "https://storage.googleapis.com/us.artifacts.chainguard-poc.appspot.com/chainctl_$(uname -s)_$(uname -m)"
```

```sh
chmod +x chainctl
alias chainctl=$PWD/chainctl
```

Check installation

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

GitVersion:    6b9bcae
GitCommit:     6b9bcaeb3fd2cf8d3ec3febc81766df14dec905c
GitTreeState:  clean
BuildDate:     2022-07-13T06:19:55Z
GoVersion:     go1.17.12
Compiler:      gc
Platform:      linux/amd64
```

Login

```sh
chainctl auth login --register
```

List IAM groups

```sh
chainctl iam groups ls -o table
```

Create a test group under a parent root group

```sh
chainctl iam groups create demo-test-group --parent {GROUPID}
```

Confirm you want to create the group. Then grab the ID number and set it to a variable

```sh
export GROUPID={GROUPID}
```

Install Chainguard Enforce.

```sh
chainctl cluster install --group=$GROUPID
```

You can check current policies with the following (optional).

```sh
chainctl policies ls
```

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

Save the file as `sample-policy.yaml`.

Return to the terminal.

Apply the new policy.

```sh
chainctl policies apply -f sample-policy.yaml --group $GROUPID
```

Check what is running 

```sh
chainctl cluster records ls   $(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

Deploy an NGINX image to the cluster

```sh
kubectl create deployment nginx --image=nginx
```

Give this a few seconds to populate.

Check what's running again.

```sh
chainctl cluster records ls   $(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

You should get feedback that this fails the policy.

```
                                                              IMAGE                                                              | LAST SEEN | LAST REFRESHED |    POLICIES
---------------------------------------------------------------------------------------------------------------------------------+-----------+----------------+------------------------
  index.docker.io/library/nginx:latest@sha256:2bcabc23b45489fb0885d69a06ba1d648aeda973fae7bb981bafbb884165e514                   | 13s       |                | sample-policy:fail:4s
```
  
Pull in Chainguard image with SBOM.

```sh
kubectl create deployment sbom-log4j --image=ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0
```

Check the output.

```sh
chainctl cluster records ls   $(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

You'll get feedback that this has an SBOM but no signature (thus fails).

```
                                                              IMAGE                                                              | LAST SEEN |  LAST REFRESHED  |        POLICIES
---------------------------------------------------------------------------------------------------------------------------------+-----------+------------------+-------------------------
  ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0@sha256:ba4037061b76ad8f306dd9e442877236015747ec42141caf504dc0df4d10708d       | 16s       | sbom:8s          | sample-policy:fail:8s
```

Pull an image with an SBOM and signature.

```sh
kubectl create deployment good-nginx --image=ghcr.io/chainguard-dev/nginx-image-demo
```

Check the output

```sh
chainctl cluster records ls   $(kubectl get ns gulfstream -ojson | jq -r .metadata.uid)
```

You'll get feedback that this passes the policy with both an SBOM and signature.

```
                                                              IMAGE                                                              | LAST SEEN |  LAST REFRESHED  |        POLICIES
---------------------------------------------------------------------------------------------------------------------------------+-----------+------------------+-------------------------
  ghcr.io/chainguard-dev/nginx-image-demo:latest@sha256:0fb2d846fece2561501a912301c255bcd1e328f682f38b312011705595e9634e         | 52s       | sig:40s sbom:40s | sample-policy:pass:40s
 ```
 
 To uninstall

```sh
chainctl cluster uninstall
```