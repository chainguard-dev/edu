---
aliases:
- /chainguard/fips/eks-add-ons/
title: "Overview of Chainguard EKS add-ons"
linktitle: "EKS add-ons"
description: "Learn about Chainguard EKS add-ons, which provide zero-CVE and FIPS-validated container images for core Amazon EKS cluster components through AWS Marketplace."
type: "article"
date: 2026-04-10T00:00:00+00:00
lastmod: 2026-09-28T14:00:04+00:00
draft: false
tags: ["FIPS", "Chainguard Containers"]
images: []
menu:
  docs:
    parent: "fips"
weight: 50
toc: true
---

Chainguard EKS add-ons are hardened, minimal container images for the foundational software components that power Amazon Elastic Kubernetes Service (EKS) clusters. Available through [AWS Marketplace](https://aws.amazon.com/marketplace), they serve as FIPS-validated drop-in replacements for AWS default add-ons, providing zero known CVEs and FIPS 140-3 validated cryptography without requiring custom image builds or manifest overrides.

## What are EKS add-ons?

Amazon EKS add-ons are software components that provide supporting operational capabilities to Kubernetes applications — things like networking drivers, storage integrations, and observability agents that allow the cluster to interact with underlying AWS resources, but aren't specific to any application running on it.

They handle cluster functions like internal DNS resolution, pod networking, persistent storage, and traffic routing, and are managed independently from your application workloads. AWS installs several add-ons in every EKS cluster by default.

For a full explanation of how EKS add-ons work (including how to install, configure, and update them), refer to the [Amazon EKS add-ons documentation](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html).

## Available Chainguard EKS add-ons

Chainguard provides hardened images for five widely used EKS add-ons. All are FIPS-validated.

| Add-on | Description |
| -------- | ------------- |
| **kube-proxy** | Routes network traffic between pods within the cluster |
| **CoreDNS** | Handles internal DNS — how services discover and communicate with each other |
| **Amazon VPC CNI** | Connects pods to the AWS VPC network backbone |
| **Amazon EBS CSI Driver** | Enables persistent block storage volumes backed by Amazon EBS |
| **Amazon EFS CSI Driver** | Enables shared, persistent file storage backed by Amazon EFS |

## Why use Chainguard EKS add-ons?

### Zero known CVEs

Default EKS add-on images ship with known CVEs. Because customers do not own the upstream source code, they aren't able to patch these vulnerabilities.

Chainguard rebuilds each add-on using its minimal, hardened container image approach, removing unnecessary packages and dependencies that are the most common source of CVEs. Like Chainguard Containers, Chainguard EKS add-ons are rebuilt continuously to incorporate available security patches, keeping the known CVE count at or near zero.

### FIPS 140-3 validated cryptography

For organizations operating under FedRAMP, NIST, or other compliance frameworks that require FIPS-validated cryptography, existing options create additional developer toil to maintain the image. Chainguard EKS add-ons are the only available option that provides FIPS 140-3 validated cryptography for core EKS cluster infrastructure. No other provider offers FIPS-validated replacements for these components.

To learn more about how Chainguard approaches FIPS, refer to the [Chainguard FIPS documentation](/platform/fips/).

### Drop-in compatibility

Chainguard EKS add-ons are designed as direct replacements for the corresponding AWS-managed components. They use the same Helm-based deployment workflow as any other EKS add-on, and they accept the configuration values of AWS's own add-ons in the same shape. Some defaults differ from AWS's, and replacing an AWS add-on that's already installed takes a few adoption settings. For details, refer to [Configure Chainguard EKS add-ons](#configure-chainguard-eks-add-ons).

Chainguard EKS add-ons are available through AWS Marketplace and can be found through the AWS Console. There's no manual setup, you don't need a Chainguard account to subscribe, and billing is consolidated with your existing AWS bill.

## Who should use Chainguard EKS add-ons?

Chainguard EKS add-ons are well-suited for:

- **Regulated industries**: Healthcare, financial services, defense, and government organizations that require FIPS 140-3 validated cryptography or operate under FedRAMP, NIST 800-53, or similar compliance frameworks.
- **Security-conscious engineering teams**: Platform and DevOps teams that want a clean, auditable baseline for cluster infrastructure without maintaining custom image builds or accepting audit exceptions.
- **Organizations requiring infrastructure control**: Enterprises that need more control over their EKS deployments than EKS Auto Mode provides, and for whom FIPS compliance through Auto Mode is not a viable option.

## Using Chainguard EKS add-ons

### Prerequisites

In order to use Chainguard EKS add-ons, you will need the following:

- An active AWS account
- An existing Amazon EKS cluster, or permission to create one
- AWS IAM permissions sufficient to subscribe to AWS Marketplace offerings

### Subscribe through AWS Marketplace

Chainguard EKS add-ons are listed in AWS Marketplace and can be found within the EKS Console. To subscribe:

1. In the AWS Console, navigate to your EKS cluster and open the **Add-ons** tab.
2. Search for the Chainguard add-on you want to install.
3. Subscribe.

### Deploy with Helm

Once subscribed, deployment follows the standard EKS Helm workflow, and you can deploy the add-ons with AWS CLI or in your GitOps workflows. Unlike a standalone Helm chart, which is self-managed, EKS will automatically handle lifecycle management of your add-ons. You don't need new tooling or a Chainguard account. To replace an AWS add-on that's already installed, refer to [Replace an AWS add-on](#replace-an-aws-add-on).

For step-by-step installation guidance, refer to the deployment instructions included with each add-on listing in AWS Marketplace.

### Known limitations

AWS Marketplace container products, including EKS add-ons, are not available in AWS GovCloud. As noted in the [AWS GovCloud User Guide](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-marketplace.html), "Currently, container products and Amazon Machine Learning products are not available." Consequently, you cannot deploy Chainguard EKS add-ons through AWS Marketplace in GovCloud.

Instead, deploy the add-ons using self-managed Helm charts or rendered manifests. Do not modify an add-on’s image references after deployment. These fields are effectively immutable, and modifying them prevents the add-on from receiving updates.

## Configure Chainguard EKS add-ons

You can pass configuration values to a Chainguard EKS add-on the same way you do for AWS's own add-ons: with the `--configuration-values` option of `aws eks create-addon` and `aws eks update-addon`. EKS checks the values against the add-on's configuration schema and rejects any that the schema doesn't accept.

Each schema starts from the schema of AWS's own add-on for the same component, so the settings you pass to AWS's add-on work here in the same shape, with the exceptions listed for each add-on later on this page. The schemas also check values more strictly than AWS's do. Most values that Kubernetes would reject fail when you create or update the add-on, rather than when EKS applies it.

The following table lists each Chainguard EKS add-on's name in EKS, alongside the name of AWS's own add-on for the same component:

| Component | Chainguard EKS add-on name | AWS's own add-on name |
| -------- | ------------- | ------------- |
| kube-proxy | `chainguard_kube-proxy-fips` | `kube-proxy` |
| CoreDNS | `chainguard_coredns-fips` | `coredns` |
| Amazon VPC CNI | `chainguard_aws-vpc-cni-fips` | `vpc-cni` |
| Amazon EBS CSI Driver | `chainguard_aws-ebs-csi-driver-fips` | `aws-ebs-csi-driver` |
| Amazon EFS CSI Driver | `chainguard_aws-efs-csi-driver-fips` | `aws-efs-csi-driver` |

### View an add-on's configuration schema

The schema that EKS returns is the source of truth for what a version accepts, including every setting, its type, and its default. To view it, find the add-on's versions, and then request the schema for one of them:

```sh
aws eks describe-addon-versions --addon-name chainguard_coredns-fips \
  --query 'addons[].addonVersions[].addonVersion'

aws eks describe-addon-configuration --addon-name chainguard_coredns-fips \
  --addon-version <version> \
  --query configurationSchema --output text
```

The schema's defaults come from the add-on's chart, so they can differ from the defaults of AWS's own add-on.

### Pass configuration values

Pass configuration values as a JSON or YAML string. For example, the following command runs kube-proxy in `iptables` mode, the mode that AWS's own add-on uses:

```sh
aws eks update-addon --cluster-name <cluster-name> \
  --addon-name chainguard_kube-proxy-fips \
  --configuration-values '{"mode": "iptables"}'
```

To read values from a file, pass `file://<path>` instead of the string.

If you manage add-ons with Terraform and `jsonencode`, leave out optional attributes that you don't set. Terraform sends an unset attribute as `null`, and the schemas reject `null` in most settings, because in Helm values a `null` deletes the chart's default.

### What every schema leaves out

EKS applies an add-on with cluster administrator permissions, so no Chainguard EKS add-on schema accepts settings for any of the following, even where AWS's own add-on does:

* Container image references and pull secrets. The add-on decides which images it runs.
* Security contexts, privileged mode, Linux capabilities, and role-based access control (RBAC) rules.
* Service account identity, such as the IAM role annotation for IAM Roles for Service Accounts (IRSA), or environment variables that set AWS SDK credentials. Use EKS Pod Identity to grant the add-on's IAM permissions.
* Secret material, including volumes backed by a Secret. A setting can name a Secret, such as an environment variable's `secretKeyRef`, but never carries its contents.
* Settings that EKS sets for each cluster, such as the API server endpoint.
* Object names and namespaces.
* Volume sources that EKS can't use, such as other clouds' disks and deprecated in-tree volume plugins.

The schemas also reject annotation keys that start with `container.apparmor.security.beta.kubernetes.io/`, `seccomp.security.alpha.kubernetes.io/`, or `container.seccomp.security.alpha.kubernetes.io/`, and pod labels that would change the chart's own selector labels.

### Replace an AWS add-on

Kubernetes doesn't let a Deployment's or DaemonSet's selector change. Each Chainguard chart selects its pods by different labels than AWS's own add-on does, so to take over the objects that AWS's add-on created, pass the add-on's adoption settings, listed in the section for each add-on. On a cluster that never ran AWS's add-on, leave them out.

Pass the adoption settings when you first create the Chainguard add-on, and keep them in the configuration values of every later update. Removing an adoption setting changes a selector, which Kubernetes rejects, so the update fails.

To replace an AWS add-on:

1. Remove AWS's add-on and keep the objects it created in the cluster. The following commands use CoreDNS as an example; for other add-ons, use the names in the [table of add-on names](#configure-chainguard-eks-add-ons):

   ```sh
   aws eks delete-addon --cluster-name <cluster-name> --addon-name coredns --preserve
   ```

2. Save the add-on's adoption settings to a file, such as `coredns-values.json`. Then create the Chainguard add-on with those settings, and let it take over the existing objects:

   ```sh
   aws eks create-addon --cluster-name <cluster-name> \
     --addon-name chainguard_coredns-fips \
     --resolve-conflicts OVERWRITE \
     --configuration-values file://coredns-values.json
   ```

3. Compare the defaults listed for the add-on with the settings you relied on in AWS's add-on, and set any that you need.

### kube-proxy

The schema accepts every setting of AWS's own kube-proxy add-on (`v1.37.0-eksbuild.19`): `mode`, `ipvs.scheduler`, `conntrack.tcpBeLiberal`, `podAnnotations`, `podLabels`, and `resources`. Label and annotation values must be strings.

To take over the kube-proxy DaemonSet that AWS's add-on created, pass the following adoption setting:

```json
{"selectorLabelsOverride": {"k8s-app": "kube-proxy"}}
```

The following kube-proxy defaults differ from those of AWS's own add-on:

| Setting | Chainguard add-on | AWS's own add-on |
| -------- | ------------- | ------------- |
| `mode` | `nftables` | `iptables` |
| `resources` | No requests | `cpu: 100m` request, according to AWS's archived kube-proxy manifest |

To keep AWS's mode, pass `{"mode": "iptables"}`.

### CoreDNS

The schema accepts the settings of AWS's own CoreDNS add-on (`v1.14.7-eksbuild.11`), with these exceptions:

* `computeType` isn't accepted. The Chainguard add-on never pins CoreDNS to EC2 nodes, so its pods run on Fargate when a Fargate profile selects them. AWS's documented Fargate profile selects `k8s-app=kube-dns`, which matches the Chainguard pods only with the adoption settings that follow. With `autoScaling.enabled`, the profile must also select the autoscaler pod.
* `trafficDistribution` accepts only `PreferClose`.
* `podDisruptionBudget` accepts only `enabled`, `maxUnavailable`, and `minAvailable`.
* `service.clusterIP` isn't accepted. EKS sets it to the cluster's DNS address.

`autoScaling` runs the cluster-proportional-autoscaler as a separate Deployment. It sizes CoreDNS the same way EKS's own CoreDNS autoscaling does, but it checks every 10 seconds instead of scaling down gradually from 10-minute peaks.

To take over the CoreDNS objects that AWS's add-on created, pass the following adoption settings:

```json
{
  "k8sAppLabelOverride": "kube-dns",
  "podLabels": { "eks.amazonaws.com/component": "coredns" },
  "deployment": { "selector": { "matchLabels": { "k8s-app": "kube-dns", "eks.amazonaws.com/component": "coredns" } } },
  "service": { "selector": { "k8s-app": "kube-dns" } }
}
```

The Chainguard add-on also takes over AWS's `coredns` ServiceAccount. It doesn't create AWS's `system:coredns` ClusterRole and ClusterRoleBinding, so if they remain from AWS's add-on, they still grant their permissions to that ServiceAccount.

The following CoreDNS defaults differ from those of AWS's own add-on:

| Setting | Chainguard add-on | AWS's own add-on |
| -------- | ------------- | ------------- |
| `replicaCount` | 1 | 2 |
| `podDisruptionBudget` | None | `enabled: true`, `maxUnavailable: 1` |
| `affinity` | None | Requires Linux nodes on amd64 or arm64, and prefers one CoreDNS pod per node |
| `tolerations` | None | `CriticalAddonsOnly`, and `NoSchedule` for `node-role.kubernetes.io/control-plane` |
| `autoScaling.minReplicas` | 2, or 1 on a single-node cluster | 2 |
| `resources` | CPU and memory limits and requests of `100m` and `128Mi` | Memory limit of `170Mi`; requests of `100m` CPU and `70Mi` memory; no CPU limit |

To match AWS's first four defaults, pass the following values:

```json
{
  "replicaCount": 2,
  "podDisruptionBudget": { "enabled": true, "maxUnavailable": 1 },
  "affinity": {
    "nodeAffinity": {
      "requiredDuringSchedulingIgnoredDuringExecution": {
        "nodeSelectorTerms": [
          {
            "matchExpressions": [
              { "key": "kubernetes.io/os", "operator": "In", "values": ["linux"] },
              { "key": "kubernetes.io/arch", "operator": "In", "values": ["amd64", "arm64"] }
            ]
          }
        ]
      }
    },
    "podAntiAffinity": {
      "preferredDuringSchedulingIgnoredDuringExecution": [
        {
          "podAffinityTerm": {
            "labelSelector": {
              "matchExpressions": [
                { "key": "app.kubernetes.io/name", "operator": "In", "values": ["coredns"] }
              ]
            },
            "topologyKey": "kubernetes.io/hostname"
          },
          "weight": 100
        }
      ]
    }
  },
  "tolerations": [
    { "key": "CriticalAddonsOnly", "operator": "Exists" },
    { "effect": "NoSchedule", "key": "node-role.kubernetes.io/control-plane" }
  ]
}
```

You can't remove the chart's 100m CPU limit. To come close to AWS's `resources`, set AWS's memory limit and requests, and set `limits.cpu` above what CoreDNS uses.

### Amazon VPC CNI

The schema accepts the settings of AWS's own VPC CNI add-on (`v1.22.4-eksbuild.5` and `v1.23.2-eksbuild.3`), with these exceptions:

| Setting | Why the schema leaves it out |
| -------- | ------------- |
| `env.CLUSTER_ENDPOINT` | The add-on sets it to your cluster's API server endpoint. |
| `env.ANNOTATE_POD_IP` | It adds a permission to the `aws-node` ClusterRole. |
| `minReadySeconds` | The chart doesn't read it. |
| `env.ENABLE_V6_EGRESS`, `env.ENABLE_V4_EGRESS`, `env.DISABLE_POD_V6`, and `init.env.ENABLE_V6_EGRESS` | IPv6 settings aren't supported. |

`extraEnv`, `extraVolumes`, and `extraVolumeMounts`, which AWS's schema leaves untyped, accept only the fields of their Kubernetes types.

The VPC CNI add-on doesn't need adoption settings. It always selects `aws-node` pods by `k8s-app: aws-node`, as AWS's own add-on does.

### Amazon EBS CSI Driver

The schema accepts the settings of AWS's own EBS CSI driver add-on (`v1.67.2-eksbuild.1`), except for these settings, which the chart ignores:

* `node.envFrom`
* The `envFrom`, `enablePrometheusAnnotations`, `serviceMonitor.forceEnable`, `serviceMonitor.labels`, and `serviceAccount.automountServiceAccountToken` settings of each `additionalDaemonSets` entry

`controller.serviceAccount.automountServiceAccountToken` and `node.serviceAccount.automountServiceAccountToken` accept only `true`, the default.

To take over the EBS CSI driver objects that AWS's add-on created, pass the following adoption setting:

```json
{"useAwsAddonSelectors": true}
```

Never change `useAwsAddonSelectors` on an existing installation, because the update fails. With the setting on, list the add-on's pods by the `app.kubernetes.io/name` label:

```sh
kubectl get pods -n kube-system -l app.kubernetes.io/name=aws-ebs-csi-driver
```

### Amazon EFS CSI Driver

The schema accepts the settings of AWS's own EFS CSI driver add-on (`v3.5.2-eksbuild.1`), with these exceptions:

* `controller.containerSecurityContext`, `controller.serviceAccount.annotations`, and `node.serviceAccount.annotations` aren't accepted. The add-on's IAM permissions attach through EKS Pod Identity to the `efs-csi-controller-sa` and `efs-csi-node-sa` service accounts.
* `controller.adaptiveRetryMode` isn't accepted, because the chart doesn't pass it to the driver. The driver keeps its default, adaptive retry mode.
* `controller.livenessProbe` and `node.livenessProbe` accept only `httpGet` and the timing fields.

To take over the EFS CSI driver objects that AWS's add-on created, set `controller.selectorLabelsOverride` and `node.selectorLabelsOverride` to the selectors of the `efs-csi-controller` Deployment and the `efs-csi-node` DaemonSet. To find them, run the following commands:

```sh
kubectl get deployment efs-csi-controller -n kube-system -o jsonpath='{.spec.selector.matchLabels}'
kubectl get daemonset efs-csi-node -n kube-system -o jsonpath='{.spec.selector.matchLabels}'
```

Each override accepts only the keys `app`, `app.kubernetes.io/name`, and `app.kubernetes.io/instance`, and it must set `app` to `efs-csi-controller` or `efs-csi-node`.

The following EFS CSI driver defaults differ from those of AWS's own add-on:

| Setting | Chainguard add-on | AWS's own add-on |
| -------- | ------------- | ------------- |
| `controller.tolerations` | `CriticalAddonsOnly` and `efs.csi.aws.com/agent-not-ready` | Every taint |
| `node.maxInflightMountCalls` and `node.volumeAttachLimit`, when you opt in and leave them unset | 10 and 20 | -1 |

To keep AWS's tolerations, set `controller.tolerations` to `[{"operator": "Exists"}]`.
