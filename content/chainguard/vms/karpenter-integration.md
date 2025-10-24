---
title: "Chainguard VMs with Karpenter"
linktitle: "Karpenter"
description: "Learn how to integrate Chainguard VMs with Karpenter for efficient node provisioning on AWS EKS using custom AMIs."
type: "article"
date: 2025-10-23T18:55:00+00:00
lastmod: 2025-10-23T18:55:00+00:00
draft: false
tags: ["Chainguard VMs", "Karpenter", "AWS EKS", "AMI"]
menu:
  docs:
    parent: "vms"
weight: 005
toc: true
---

## Introduction

Chainguard VMs provide a secure, minimal foundation for running workloads in cloud environments. Integrating them with [Karpenter](https://karpenter.sh/) on AWS EKS allows for efficient, on-demand node provisioning using custom Chainguard AMIs. This guide covers the setup and configuration based on Karpenter v1.x, which uses `EC2NodeClass` for node management.

Karpenter v1.x introduces `EC2NodeClass` to replace the deprecated `Provisioners` from earlier versions (e.g., v0.31 or older). This enables more flexible node configuration, including custom AMI selection and block device mappings.

**Security Note**: This guide follows least privilege principles for IAM permissions. Always audit and minimize permissions after deployment, removing any unused access to maintain a secure posture.

## Prerequisites

- AWS EKS cluster with Karpenter installed (follow [official installation guide](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/))
- AWS CLI configured with appropriate permissions
- Access to a Chainguard AMI ID for your region (e.g., via Chainguard subscription)
- Environment variables set: `CLUSTER_NAME`, `AWS_DEFAULT_REGION`, `KARPENTER_NAMESPACE`, `CUSTOM_AMI_ID`

## AMI Verification

Before configuring Karpenter, verify your Chainguard AMI details to ensure correct configuration:

```bash
# Verify AMI details (replace with your actual AMI ID and region)
aws ec2 describe-images --image-ids ${CUSTOM_AMI_ID} --region ${AWS_DEFAULT_REGION} --query 'Images[*].{Name:Name,RootDeviceName:RootDeviceName,BlockDeviceMappings:BlockDeviceMappings,Architecture:Architecture,Description:Description}'
```

**Key details to verify:**
- **Root Device Name**: Typically `/dev/sda1` for Chainguard AMIs
- **Current Volume Size**: Default is usually 8Gi (you'll override this in Karpenter config)
- **Architecture**: Ensure it matches your requirements (x86_64, arm64)
- **Volume Type**: Usually gp3

Example output:
```json
{
  "Name": "chainguard-eks-1.32-dev-x86_64-20251024-0318",
  "RootDeviceName": "/dev/sda1",
  "BlockDeviceMappings": [
    {
      "DeviceName": "/dev/sda1",
      "Ebs": {
        "VolumeSize": 8,
        "VolumeType": "gp3",
        "Encrypted": false
      }
    }
  ],
  "Architecture": "x86_64",
  "Description": "chainguard-eks-1.32-dev-x86_64-20251024-0318"
}
```

## Installation

Follow the [official Karpenter installation guide](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/) for the complete setup process. This section covers only the Chainguard-specific modifications needed.

### Environment Variables

Set these variables for your Chainguard integration:

```bash
export CLUSTER_NAME="your-cluster-name"
export AWS_DEFAULT_REGION="us-west-2"
export KARPENTER_VERSION="1.8.1"  # Use latest stable version
export KARPENTER_NAMESPACE="karpenter"
export CUSTOM_AMI_ID="ami-01f687414663bd721"  # Your Chainguard AMI ID
```

### IAM Permissions

**Important**: The standard Karpenter CloudFormation stack may not include all permissions needed for custom AMI usage. Based on your setup, additional permissions might be required for the controller role.

Add these permissions to your Karpenter controller role if you encounter access denied errors:

```bash
# Add basic permissions (if not already included in CloudFormation stack)
aws iam put-role-policy --role-name "${CLUSTER_NAME}-karpenter" --policy-name "KarpenterEKS" --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "eks:DescribeCluster",
        "ec2:DescribeInstanceTypes"
      ],
      "Resource": [
        "arn:aws:eks:${AWS_DEFAULT_REGION}:${AWS_ACCOUNT_ID}:cluster/${CLUSTER_NAME}",
        "*"
      ]
    }
  ]
}'

# Add comprehensive permissions for custom AMI operations
aws iam put-role-policy \
  --role-name "${CLUSTER_NAME}-karpenter" \
  --policy-name "KarpenterCompletePermissions" \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "ec2:DescribeInstanceTypes",
          "ec2:DescribeInstanceTypeOfferings",
          "ec2:DescribeAvailabilityZones",
          "ec2:DescribeImages",
          "ec2:DescribeInstances",
          "ec2:DescribeSecurityGroups",
          "ec2:DescribeSubnets"
        ],
        "Resource": "*"
      }
    ]
  }'
```

**Note**: Monitor CloudTrail logs for "Access Denied" errors and add only the minimum permissions needed for your specific environment.

**Security**: Follow least privilege by auditing these permissions after deployment and removing any unused access.

### NodeGroup Management

The initial managed nodegroup created during cluster setup can coexist with Karpenter-managed nodes. For production clusters, consider keeping a small managed nodegroup for stability and core components. Only remove it if you want Karpenter to handle all node provisioning.

## Configuration

To integrate Chainguard VMs, configure a `NodePool` and `EC2NodeClass` in Karpenter. The key components are:

- **amiSelectorTerms**: Specifies the custom Chainguard AMI.
- **amiFamily: AL2023**: Enables automatic bootstrap generation, simplifying setup compared to `amiFamily: Custom`.
- **blockDeviceMappings**: Defines the root volume size and type (e.g., 100Gi gp3 for the Chainguard AMI).

Here's the example configuration:

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    spec:
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64"]
        - key: kubernetes.io/os
          operator: In
          values: ["linux"]
        - key: karpenter.sh/capacity-type
          operator: In
          values: ["on-demand"]
        - key: karpenter.k8s.aws/instance-category
          operator: In
          values: ["c", "m", "r", "t"]
        - key: karpenter.k8s.aws/instance-size
          operator: NotIn
          values: ["metal"]
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: chainguard-eks
  expireAfter: 720h  # 30 days
  limits:
    cpu: 1000
  disruption:
    consolidationPolicy: WhenEmptyOrUnderutilized
    consolidateAfter: 1m
---
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: chainguard-eks
spec:
  amiFamily: AL2023
  role: "KarpenterNodeRole-${CLUSTER_NAME}"
  amiSelectorTerms:
    - id: "${CUSTOM_AMI_ID}"
  blockDeviceMappings:
    - deviceName: /dev/sda1  # Chainguard AMI root device name (verify with: aws ec2 describe-images --image-ids <AMI_ID>)
      ebs:
        volumeSize: 100Gi
        volumeType: gp3
        encrypted: true
        deleteOnTermination: true
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: "${CLUSTER_NAME}"
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: "${CLUSTER_NAME}"
```

Apply the configuration using:

```bash
cat <<EOF | envsubst | kubectl apply -f -
# Paste the YAML above
EOF
```

## Key Learnings and Notes

- **AMI Selection**: Use `amiSelectorTerms` to specify your Chainguard AMI. This is required for custom AMIs and ensures Karpenter provisions nodes with the correct image.
- **amiFamily: AL2023**: This setting automatically handles the bootstrap process, making it easier than `amiFamily: Custom`, where you must manage bootstrapping manually.
- **Block Device Mappings**: The `blockDeviceMappings` in `EC2NodeClass` allows customization of the root volume. For Chainguard AMIs, the `deviceName` is `/dev/sda1` (the AMI's root device name). You can specify the size (e.g., 100Gi) and volume type (gp3). Always verify the AMI's root device name before configuration using: `aws ec2 describe-images --image-ids <AMI_ID>`.
- **Version Compatibility**: This setup is based on Karpenter v1.8. Older versions (e.g., v0.32) used `Provisioners`, which are deprecated. Ensure your cluster is updated for `EC2NodeClass` support.
- **Node Expiration**: The `expireAfter: 720h` setting in the NodePool ensures nodes are replaced after 30 days, aligning with Chainguard VM best practices for node replacement over in-place upgrades.

## Verification

After applying the configuration, verify that nodes are provisioned correctly and the file system aligns with your settings.

Check node details:

```bash
kubectl get nodes
```

To confirm the root volume size, query the node stats (replace with your node IP):

```bash
kubectl get --raw /api/v1/nodes/<node-ip>/proxy/stats/summary | jq '{node_fs: .node.fs, runtime_fs: .runtime.fs, rootfs: .node.rootfs}'
```

Expected output for a 100Gi volume:

```json
{
  "node_fs": {
    "time": "2025-10-22T22:58:07Z",
    "availableBytes": 102086111232,
    "capacityBytes": 106233311232,
    "usedBytes": 4147200000,
    "inodesFree": 51874115,
    "inodes": 51904496,
    "inodesUsed": 30381
  },
  "runtime_fs": null,
  "rootfs": null
}
```

The `capacityBytes` should reflect approximately 100Gi (106,233,311,232 bytes ≈ 100 GiB).

## Troubleshooting

### Common Issues

- **Device Name Mismatch**: Always verify the Chainguard AMI's root device name before configuration. Chainguard AMIs typically use `/dev/sda1` as the root device. Verify using:
  ```bash
  # Check AMI details before configuration
  aws ec2 describe-images --image-ids <AMI_ID> --region <region> --query 'Images[*].{RootDeviceName:RootDeviceName,BlockDeviceMappings:BlockDeviceMappings,ImageId:ImageId}'

  # Alternative: Check from running instance
  aws ec2 describe-instances --instance-ids <instance-id> --region <region> --query 'Reservations[*].Instances[*].{RootDeviceName:RootDeviceName,BDM:BlockDeviceMappings,ImageId:ImageId}'
  ```

- **NodeClaim Cleanup**: If nodes fail to provision, clean up stuck NodeClaims:
  ```bash
  kubectl get nodeclaims.karpenter.sh -A -o name | xargs -I{} kubectl delete {}
  ```

- **IAM Permissions**: Verify the Karpenter controller role has sufficient permissions for custom AMI operations. The standard CloudFormation stack may not include all permissions needed for custom AMI usage. Additional permissions might be required for `ec2:DescribeImages`, `ec2:DescribeInstances`, and other read-only operations. Check CloudTrail logs for "Access Denied" errors and add only the minimum required permissions following least privilege principles.

### Verification Commands

Check if Chainguard AMI is being used:
```bash
# Get node and instance mapping
kubectl get nodes -o wide

# Get instance ID and check AMI
aws ec2 describe-instances --instance-ids <instance-id> --region <region> --query 'Reservations[*].Instances[*].ImageId' --output text
```

Check root volume configuration:
```bash
kubectl get --raw /api/v1/nodes/<node-ip>/proxy/stats/summary | jq '{node_fs: .node.fs, runtime_fs: .runtime.fs, rootfs: .node.rootfs}'
```

For more details on Karpenter, refer to the [official documentation](https://karpenter.sh/).