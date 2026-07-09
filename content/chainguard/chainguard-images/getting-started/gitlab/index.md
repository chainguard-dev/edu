---
title: "Getting Started with the GitLab Chainguard Containers"
type: "article"
linktitle: "GitLab"
description: "Learn how to deploy GitLab using Chainguard's security-hardened container images with reduced vulnerabilities, verifiable provenance, and daily security updates"
date: 2026-06-24T00:00:00+00:00
lastmod: 2026-07-07T00:00:00+00:00
tags: ["Chainguard Containers"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 006
toc: true
---

Chainguard's GitLab container images provide a security-hardened foundation for deploying GitLab's DevOps platform with significantly fewer vulnerabilities than the standard upstream images. Built on Wolfi, these images are rebuilt daily with the latest security patches and include verifiable Sigstore signatures and SBOMs for every component.

The Chainguard GitLab offering spans fifteen components that align with the official GitLab Helm chart architecture: `gitlab-base`, `gitlab-certificates`, `gitaly`, `gitlab-agent`, `gitlab-kas`, `gitlab-shell`, `gitlab-exporter`, `gitlab-pages`, `gitlab-container-registry`, `gitlab-runner`, `gitlab-runner-helper`, and the Community Edition services `gitlab-sidekiq-ce`, `gitlab-toolbox-ce`, `gitlab-webservice-ce`, and `gitlab-workhorse-ce`. A FIPS-validated variant is also available for FedRAMP compliance.

This guide shows how to deploy a GitLab instance on a local Kubernetes cluster using the official [GitLab Helm chart](https://docs.gitlab.com/charts/) with Chainguard images. The configuration here is suitable for development and evaluation; for production deployments, follow [GitLab's production recommendations](https://docs.gitlab.com/charts/installation/deployment.html).

{{< details "What is Wolfi?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Containers" >}}
{{< blurb/images >}}
{{< /details >}}

## Prerequisites

This guide requires the following tools installed on your local machine:

- [Docker](https://docs.docker.com/get-docker/)
- [k3d](https://k3d.io/stable/#installation) — a CLI tool for running K3s clusters in Docker
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/install/)
- [chainctl](https://edu.chainguard.dev/chainguard/chainctl/) — the Chainguard CLI

Your machine should have at least 8 GB of RAM available for Docker to allocate to the cluster. GitLab deploys several services simultaneously, and insufficient memory is the most common cause of failed or stuck deployments.

You'll also need access to a Chainguard organization with the GitLab image group enabled. If you don't have access yet, [contact Chainguard](https://www.chainguard.dev/contact) to request a trial.

## Step 1: Authenticate with the Chainguard registry

Log in to the Chainguard registry:

```shell
chainctl auth login
```

Configure Docker to use your Chainguard credentials:

```shell
chainctl auth configure-docker
```

Set your Chainguard organization name as an environment variable. If you don't know your organization name, run `chainctl iam organizations list -o table` to find it.

```shell
export ORGANIZATION=<your-chainguard-organization>
```

## Step 2: Create a local Kubernetes cluster

Create a K3s cluster with k3d, disabling the default Traefik ingress and mapping host ports 80 and 443 to the cluster's load balancer:

```shell
k3d cluster create gitlab-demo \
  --k3s-arg "--disable=traefik@server:*" \
  -p "80:80@loadbalancer" \
  -p "443:443@loadbalancer"
```

The GitLab Helm chart installs its own NGINX ingress controller, so Traefik must be disabled to avoid a conflict. The port mappings let you reach GitLab at the standard HTTP and HTTPS ports on your local machine.

You'll see output similar to the following:

```output
INFO[0000] Created network 'k3d-gitlab-demo'
INFO[0001] Creating node 'k3d-gitlab-demo-server-0'
INFO[0001] Creating LoadBalancer 'k3d-gitlab-demo-serverlb'
INFO[0005] Starting servers...
INFO[0013] Cluster 'gitlab-demo' created successfully!
```

Verify that the cluster is running:

```shell
kubectl get nodes
```

```output
NAME                       STATUS   ROLES                  AGE   VERSION
k3d-gitlab-demo-server-0   Ready    control-plane,master   19s   v1.31.5+k3s1
```

The node should show a `Ready` status before you proceed.

## Step 3: Create an image pull secret

GitLab's Helm chart deploys pods in the `gitlab-system` namespace that pull images from `cgr.dev`. Kubernetes nodes don't inherit credentials from your local Docker configuration, so you need to create a pull secret explicitly before installing.

Create the namespace first so you can pre-populate the secret:

```shell
kubectl create namespace gitlab-system
```

Create a long-lived pull token for your Chainguard organization:

```shell
chainctl auth pull-token create \
  --parent $ORGANIZATION \
  --name gitlab-pull-token \
  --ttl 8760h
```

The command outputs a username and password. Use those values to create a Kubernetes image pull secret:

```shell
kubectl create secret docker-registry cgr-pull-secret \
  --namespace gitlab-system \
  --docker-server=cgr.dev \
  --docker-username=<username-from-pull-token> \
  --docker-password=<password-from-pull-token>
```

```output
secret/cgr-pull-secret created
```

## Step 4: Create the GitLab configuration file

Create a file named `gitlab-values.yaml` with the following content. This file configures the GitLab Helm chart to pull all images from the Chainguard registry, references the pull secret you just created, and sets reduced resource requests appropriate for a local development environment.

Replace every occurrence of `ORGANIZATION` with your Chainguard organization name. If you set `$ORGANIZATION` in [Step 1](#step-1-authenticate-with-the-chainguard-registry), run the following command after saving the file to substitute it automatically:

```shell
sed -i "s/ORGANIZATION/$ORGANIZATION/g" gitlab-values.yaml
```

```yaml
installCertmanager: false

certmanager-issuer:
  email: admin@example.com

global:
  gitlabBase:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-base
      tag: "18.11"
  certificates:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-certificates
      tag: "18.11"
  hosts:
    domain: 127.0.0.1.nip.io
    externalIP: 127.0.0.1
  ingress:
    configureCertmanager: false
  image:
    pullSecrets:
      - name: cgr-pull-secret

gitlab:
  gitlab-exporter:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-exporter
      tag: "18.11"
  gitlab-shell:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-shell
      tag: "18.11"
  gitaly:
    image:
      repository: cgr.dev/ORGANIZATION/gitaly
      tag: "18.11"
  gitlab-pages:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-pages
      tag: "18.11"
  kas:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-kas
      tag: "18.11"
  sidekiq:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-sidekiq-ce
      tag: "18.11"
    resources:
      requests:
        cpu: 100m
        memory: 500Mi
  toolbox:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-toolbox-ce
      tag: "18.11"
  webservice:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-webservice-ce
      tag: "18.11"
    resources:
      requests:
        cpu: 300m
        memory: 1500Mi
    workhorse:
      image: cgr.dev/ORGANIZATION/gitlab-workhorse-ce
      tag: "18.11"

registry:
  image:
    repository: cgr.dev/ORGANIZATION/gitlab-container-registry
    tag: "18.11"

gitlab-runner:
  install: false

prometheus:
  install: false

redis:
  resources:
    requests:
      cpu: 50m
      memory: 64Mi

minio:
  resources:
    requests:
      cpu: 50m
      memory: 128Mi
```

A few notes on this configuration:

- **Image tags**: The `18.11` tag tracks the latest security-patched build within the GitLab 18.11 minor release. This provides a longer guide lifespan than `latest` while still receiving daily security updates.
- **Chart version**: The Helm install command in the next step pins to chart version `9.11.7`, which corresponds to GitLab 18.x. The chart 10.x series (GitLab 19+) requires externally managed PostgreSQL, Redis, and object storage. When Chainguard's `18.11` images are succeeded by a `19.x` series, this guide will require a corresponding update.
- **TLS**: With cert-manager disabled, the chart generates self-signed TLS certificates. Your browser will display a certificate warning when you first access GitLab — this is expected for a local development setup.
- **Workhorse**: The workhorse container runs inside the webservice pod and must use a Chainguard image built from the same commit as `gitlab-webservice-ce`. It is configured separately under `gitlab.webservice.workhorse` rather than as a standalone subchart.

## Step 5: Deploy GitLab with Helm

Add the official GitLab Helm chart repository:

```shell
helm repo add gitlab https://charts.gitlab.io/
helm repo update
```

Deploy GitLab, pinning to the chart version that matches the Chainguard image series:

```shell
helm upgrade --install gitlab gitlab/gitlab \
  --version 9.11.7 \
  --namespace gitlab-system \
  --values gitlab-values.yaml \
  --timeout 600s
```

The `--timeout 600s` flag gives the deployment up to ten minutes to complete. GitLab pulls several container images and initializes multiple services on first install, so the process takes several minutes.

Watch the deployment progress:

```shell
watch kubectl get pods -n gitlab-system
```

When the output stabilizes and all pods show a `Running` or `Completed` status, press `Ctrl+C` to exit. A healthy deployment looks like this:

```output
NAME                                               READY   STATUS      RESTARTS   AGE
gitlab-gitaly-0                                    1/1     Running     0          8m
gitlab-gitlab-exporter-...                         1/1     Running     0          8m
gitlab-gitlab-shell-...                            1/1     Running     0          8m
gitlab-kas-...                                     1/1     Running     0          8m
gitlab-migrations-...-...                          0/1     Completed   0          8m
gitlab-minio-...                                   1/1     Running     0          8m
gitlab-minio-create-buckets-...                    0/1     Completed   0          8m
gitlab-nginx-ingress-controller-...                1/1     Running     0          8m
gitlab-postgresql-0                                2/2     Running     0          8m
gitlab-redis-master-0                              2/2     Running     0          8m
gitlab-registry-...                                1/1     Running     0          8m
gitlab-sidekiq-all-in-1-v2-...                     1/1     Running     0          8m
gitlab-toolbox-...                                 1/1     Running     0          8m
gitlab-webservice-default-...                      2/2     Running     0          8m
```

> **Note**: The KAS pods may restart once on first boot while waiting for Redis to become ready. This is a normal startup ordering effect and resolves on its own within a minute or two.

## Step 6: Access GitLab

Retrieve the initial root password from the Kubernetes secret created during deployment:

```shell
kubectl get secret gitlab-gitlab-initial-root-password \
  -n gitlab-system \
  -o jsonpath='{.data.password}' | base64 --decode; echo
```

Open a browser and navigate to `https://gitlab.127.0.0.1.nip.io`. Proceed past the browser's certificate warning (expected because the deployment uses a self-signed certificate), then log in with the username `root` and the password you retrieved.

After logging in, navigate to **User menu > Edit profile > Password** and set a new password for the root account.

## Step 7: Clean up

When you're done, delete the cluster to remove all resources:

```shell
k3d cluster delete gitlab-demo
```

## Advanced Usage

{{< blurb/images-advanced image="GitLab" >}}

### Enable GitLab Runner

To add GitLab Runner with Chainguard images, update `gitlab-values.yaml` with the following:

```yaml
gitlab-runner:
  install: true
  image:
    registry: cgr.dev
    image: ORGANIZATION/gitlab-runner
    tag: "18.11"
  runners:
    config: |
      [[runners]]
        [runners.kubernetes]
          helper_image = "cgr.dev/ORGANIZATION/gitlab-runner-helper:18.11"
```

Run `helm upgrade` with the updated values file to apply the change.

### Use the FIPS variant

Chainguard provides FIPS-validated variants of all GitLab images for FedRAMP and compliance-sensitive environments. To use them, append `-fips` to every image repository path in your values file. For example:

```yaml
global:
  gitlabBase:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-base-fips
      tag: "18.11"
  certificates:
    image:
      repository: cgr.dev/ORGANIZATION/gitlab-certificates-fips
      tag: "18.11"
```

Apply the same `-fips` suffix to all component image repositories in the `gitlab:` section, the `workhorse` block, and the `registry:` image.
