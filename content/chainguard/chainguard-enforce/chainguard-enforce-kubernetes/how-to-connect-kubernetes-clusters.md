---
title: "How to Connect Kubernetes Clusters to Chainguard Enforce"
type: "article"
lead: ""
description: "Connecting containerized workloads to Chainguard Enforce for Kubernetes"
date: 2022-09-13T15:56:52-07:00
lastmod: 2022-09-13T15:56:52-07:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 700
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Connecting Kubernetes clusters to Chainguard Enforce allows you to assess the
current state of the supply chain of your containerized workloads and enforce
policy once your workloads match your desired state. There are two ways to
connect Kubernetes clusters to enforce:

- [Chainguard Enforce Agent](#chainguard-enforce-agent) – A lightweight agent that runs in your cluster
- [Chainguard Enforce Agentless](#agentless-connections) – A zero footprint connection for
  Kubernetes clusters running in supported cloud providers. Currently supports
  AWS EKS and GCP GKE clusters.

In this article, we’ll discuss when and how to use each of these options.

## Chainguard Enforce Agent

The Enforce Agent is a flexible, general purpose way to connect your clusters
to Chainguard Enforce. Clusters using the Enforce Agent are required to have [Service
Account Token Volume Projection][k8s-docs-volume-projection] and [Service
Account Issuer Discovery][k8s-docs-issuer-discover] enabled. 

[k8s-docs-volume-projection]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection
[k8s-docs-issuer-discover]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-issuer-discovery

You can test that token volume projection is enabled by creating a pod
with a projected volume. First create a service account.

You will first need to create a service account for your cluster if you have not done so already. The following example command creates a service account named `example-sa`.

```sh
kubectl create serviceaccount example-sa
```

Then run the following command to create a pod manifest named `pod.yaml`. Be sure to change the `serviceAccountName` value if yours is different from the given example.

```sh
cat <<EOF > pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: projection-test
spec:
  containers:
  - image: nginx
    name: nginx
    volumeMounts:
    - mountPath: /var/run/secrets/tokens
      name: enforce-token
  serviceAccountName: example-sa
  volumes:
  - name: enforce-token
    projected:
      sources:
      - serviceAccountToken:
          path: enforce-token
          expirationSeconds: 7200
          audience: https://issuer.enforce.dev
EOF
```

Then, run the following command to create the pod.

```sh
kubectl create -f pod.yaml
```

Verify that it was created. 

```sh
kubectl get pods
```

If Service Account Token Volume Projection is functioning, you should receive
the following output.

```
NAME              READY   STATUS    RESTARTS   AGE
projection-test   1/1     Running   0          66s
```

If Service Account Token Volume Projection is not enabled the pod will be
rejected.

To clean up, delete the pod.

```sh
kubectl delete -f pod.yaml
```

To check if your cluster has Service Account Issuer Discovery enabled you can
check the issuer OIDC discovery endpoint

```sh
kubectl get --raw /.well-known/openid-configuration
```

If Service Account Issuer Discover is enabled, this command will return JSON output similar to the following.  

```json
{
  "issuer":"https://kubernetes.default.svc.cluster.local",
  "jwks_uri":"https://172.19.0.2:6443/openid/v1/jwks",
  "response_types_supported":["id_token"],
  "subject_types_supported":["public"],
  "id_token_signing_alg_values_supported":["RS256"]
}
```

If it is not enabled, you will receive an error message similar to the following example. 

```text
Error from server (NotFound): the server could not find the requested resource
```

### How to connect a public cluster using Enforce Agent

If your cluster has a public API endpoint and the issuer discovery endpoints
are accessible without authentication, your cluster is considered public. This
is the default configuration of GKE and EKS clusters with public API endpoints.
You can check if your issuer discovery endpoints are public by using `curl`

```sh
curl "$(kubectl get --raw /.well-known/openid-configuration | jq .issuer -r)/.well-known/openid-configuration"
```

If the request succeeds, your cluster is public. If your cluster has a public
endpoint, but the issuer discovery requires authentication, you can make it
public by binding the `system:service-account-issuer-discovery` ClusterRole to
the `system:unauthenticated` group.

```sh
kubectl create clusterrolebinding public-issuer-discovery \
  --clusterrole=system:service-account-issuer-discovery \
  --group=system:unauthenticated
```

To connect a public cluster to Chainguard Enforce, run the following command. 

```sh
chainctl cluster install
```

### How to connect a private cluster using Enforce Agent

If your cluster API endpoint isn’t public, or the issuer discovery endpoints
require authentication, you can still use the Chainguard Enforce Agent to connect your
Kubernetes cluster. In this case your cluster is considered private and to
connect you would run the following command.

```sh
chainctl cluster install --private
```

> Note: The agent does require network connectivity to our SaaS endpoints. If
> your cluster is running behind NAT, for example, the `--private` flag will
> work, but the agent will not work in an air-gapped environment.

#### Limitations of private clusters

When running in private clusters, the agent needs to be re-installed under two
circumstances:

- If the service account issuer signing key is rotated 
- At least every 25 days

This is accomplished by running `chainctl cluster install --private` once
again.

## Agentless Connections

Chainguard Enforce Agentless connections allow you to connect a cluster with zero resource
footprint. Agentless connections are currently limited to GKE and EKS clusters.
Agentless connections also require clusters to have a public API endpoint.

Agentless connection work by allowing Enforce to access your cloud account
resources on your behalf using [Cloud Account
Associations](../cloud-account-associations). 

### How to connect GKE clusters using Agentless

To connect a GKE cluster using agentless, first you must set up a cloud account
association between the GCP project hosting the cluster and the Chainguard Enforce IAM
group you want to connect the cluster to. If you don’t already have this set
up, you can check out [our article on how to set up Cloud Account
Associations](../cloud-account-associations). To verify your Cloud account
association is correctly configured, run the following command. Be sure to change $GROUP_ID to reflect the Enforce IAM group you associated with your cluster.

```sh
chainctl iam group check-gcp $GROUP_ID
```

To connect your cluster, use the `--managed` flag to ensure the connection is
agentless. Again, be sure to update $GROUP_ID and $CLUSTER_NAME to reflect your own setup.

```sh
chainctl cluster install --group=$GROUP_ID --managed=gke --cluster=$CLUSTER_NAME
```

Once connected, you can list your cluster. 

```sh
chainctl cluster ls --group=$GROUP_ID
```

### How to connect EKS clusters using Agentless

To connect an EKS cluster using agentless, first you must set up a cloud
account association between the AWS account hosting the cluster and the Enforce
IAM group you want to connect the cluster to. If you don’t already have this
set up, you can check out [our article on how to set up Cloud Account
Associations](../cloud-account-associations). To verify your Cloud account
association is correctly configured run the following command. 

```sh
chainctl iam group check-aws $GROUP_ID
```

Next, allow the agentless AWS IAM role to access your EKS cluster by editing
the aws-auth config map:

```sh
kubectl edit configmap -n kube-system aws-auth
```

> Note: your EKS cluster should have at least one node configured. Otherwise, the config map won't contain the relevant aws-auth section.

Add the following to the `mapRoles` section of the config map:

```yaml
- rolearn: arn:aws:iam::<your AWS Account number>:role/chainguard-agentless
  username: agentless-user
  groups:
  - system:masters
```

To connect your cluster, use the `--managed` flag to ensure the connection is
agentless

```sh
chainctl cluster install --group={group id} --managed=eks --cluster={cluster-name}
```

Once connected, you should see your cluster listed.

```sh
chainctl cluster ls --group={group-id}
```
