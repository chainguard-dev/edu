---
title: "Using Chainguard Enforce to Detect the Log4Shell Vulnerability"
type: "article"
description: "Use chainctl to create a policy and apply it to a cluster to detect vulnerable versions of Log4J"
date: 2022-08-11T11:07:52+02:00
lastmod: 2022-08-11T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 505
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Apache Log4j is a popular logging framework for Java applications, developed and maintained by the Apache Software Foundation. In November 2021, [a vulnerability was discovered in Log4j2](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) that allowed attackers to intercept data and potentially run malicious code remotely on applications where it was installed. The vulnerability became known as "Log4Shell."

Although the exploit was patched shortly after it was announced, the near-ubiquity of Apache Log4j in Java applications meant that millions of devices were vulnerable if they weren't upgraded. Ultimately, Log4Shell became recognized as among the most widespread, if not the most widespread, cybersecurity vulnerabilities of all time.

This tutorial outlines how to set up a Chainguard Enforce policy that will detect any vulnerable versions of Apache Log4j. You will also test this policy by deploying a sample application that includes a vulnerable Log4j package.


## Prerequisites

This tutorial assumes that you have the following in place:

* `chainctl` installed on your local machine. Follow our guide on [How To Install `chainctl`](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainctl-docs/how-to-install-chainctl/) to set this up. 
* A Kubernetes cluster that you can connect to from your local machine. This guide's examples have been validated using remote clusters running on GCP GKE and AWS EKS, as well as on a local cluster running with `kind`. 
* The Chainguard Enforce agent installed on your cluster. To set this up, connect to your cluster and follow **Steps 1 through 3** in our [Chainguard Enforce for Kubernetes User Onboarding](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-enforce-user-onboarding/).


## Step 1 – Setting Environment Variables

This step outlines how to create a pair of environment variables which you will use in `chainctl` commands later on in this guide. This will allow you to manage Chainguard Enforce without always having to interact with `chainctl` menus. 

Begin by logging in to the Chainguard platform.

```sh
chainctl auth login
```

This will launch a browser window for you to log in and, if successful, it will respond with “Chainguard Auth Successful”. Feel free to close the browser window after this.

Following that, run the following to retrieve a list of all your current groups.

```sh
chainctl iam groups list -o table
```

Including the `-o table` option will structure this command's output as a table. It will also provide some more information about the group, including the unique ID that `chainctl` uses to manage the group.

```
                             ID                             |   NAME    |    DESCRIPTION      
------------------------------------------------------------+-----------+---------------------
  53c080777a7d97samplegroupid07928aa3de055                  | log4demo  |                     
  60adedf1d5db70examplerootidf32f6b7e09fc5                  | root      | Default user group  
```

Copy the ID value of the group managing the cluster you'll use to test Chainguard Enforce, and then use that value in place of `$COPIED_ID` in the following command. This will set an environment variable called `GROUP_ID` whose value is equal to the ID number Enforce uses to refer to your IAM group.

```sh
export GROUP_ID=$COPIED_ID
```

Next, run the following command to retrieve a list of all your active clusters. 

```sh
chainctl cluster list
```
```
                  NAME                 |   GROUP   |               REMOTEID               | REGISTERED |    K8S VERSION    | AGENT VERSION | LAST SEEN |     ACTIVITY       
---------------------------------------+-----------+--------------------------------------+------------+-------------------+---------------+-----------+--------------------
  12345678-32fd-44b3-bea9-6046341ceda1 | log4demo  | 12345678-32fd-44b3-bea9-6046341ceda1 |      3m18s | v1.22.12-gke.2300 | 25bffd1-dirty |       12s | cosign-system:14s  
                                       |           |                                      |            |                   |               |           |   eots-system:59s  
                                       |           |                                      |            |                   |               |           | policy-system:12s

```

Notice the first column of information this command returns: the `NAME` column. The values in this column are the names that `chainctl` uses to manage each respective cluster.

As you did with the IAM group, copy the `NAME` value of the cluster you want to use for testing throughout this tutorial and use it in place of `$COPIED_NAME` to create an environment variable named `CLUSTER`.

```sh
export CLUSTER=$COPIED_NAME
```


## Step 2 – Running a Container Image Vulnerable to Log4Shell

You're now ready to test how Chainguard Enforce works by deploying a sample application that includes a vulnerable version of Log4j. You'll then create a policy that will detect this vulnerability. 

The sample container image used in this step is maintained by Chainguard for demonstration purposes only. Because this image includes a vulnerable version of Log4j, you _**should not run this image in a production environment.**_ 

If you'd like, you can inspect the image's [SBOM](https://edu.chainguard.dev/software-security/glossary/#sbom) by retrieving it directly from the container registry with the following `cosign` command. If you don’t already have `cosign` installed, you can install it following our [How to Install Cosign guide](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-install-cosign/).

```sh
cosign download sbom ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0
```

When you're ready, run a pod in the tenant cluster using this sample container image.

```sh
kubectl run log4shell-demo --image=ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0
```

Chainguard Enforce is only able to validate resources in namespaces that have chosen to opt-in. This can be done by adding the label `policy.sigstore.dev/include: "true"` to the namespace resource.

```sh
kubectl label ns default policy.sigstore.dev/include=true --overwrite
```

Following this, the image will appear in the existence records. To verify, list the cluster's records, grepping for “log4shell”.

```sh
chainctl cluster records list $CLUSTER | grep log4shell
```

You will also be able to view this record in the [Chainguard Enforce UI](https://console.enforce.dev) by navigating to the **Cluster details** page and checking the **Images** tab.


## Step 3 – Creating a Chainguard Enforce Policy to Detect Log4Shell

Next, create a policy that will capture the sample image. Run the following command to create a policy file named `log4shell-demo-policy.yaml`.

```sh
cat > log4shell-demo-policy.yaml <<EOF
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: log4shell-demo-policy
spec:
  images:
  - glob: "ghcr.io/chainguard-dev/log4shell-demo/*"
  authorities:
  - name: keyatt
    keyless:
        url: "https://fulcio.sigstore.dev"
        identities:
          - issuer: "*"
            subject: "*"
    attestations:
    - predicateType: cyclonedx
      name: log4shellcyclonedx
      policy:
        type: cue
        data: |
          import (
              "list"
              "strings"
          )
          let log4shell_names = [
              "log4j-api", "log4j-core"
          ]
          let log4shell_versions = [
              "2.0-beta9", "2.0-rc1", "2.0-rc2", "2.0", "2.0.1",
              "2.0.2", "2.1", "2.2", "2.3", "2.4", "2.4.1", "2.5",
              "2.6", "2.6.1", "2.6.2", "2.7", "2.8", "2.8.1",
              "2.8.2", "2.9.0", "2.9.1","2.10.0", "2.11.0", "2.11.1",
              "2.11.2", "2.12.0", "2.12.1", "2.13.0", "2.13.1",
              "2.13.2", "2.13.3", "2.14.0", "2.14.1", "2.15.0"
          ]
          predicate: {
              Data: {
                  components: [...{
                      name: name
                      version: version
                      if list.Contains(log4shell_names, name) &&
                          list.Contains(log4shell_versions, version) {
                          err: strings.Join([
                              "Error: CycloneDX SBOM contains package",
                              name, "version", version, "which is",
                              "vulnerable to Log4Shell (CVE-2021-44228)"
                          ], " ")
                          name: err
                      }
                  }]
              }
          }
    - predicateType: spdxjson
      name: log4shellspdxjson
      policy:
        type: cue
        data: |
          import (
              "list"
              "strings"
          )
          let log4shell_names = [
              "log4j-api", "log4j-core"
          ]
          let log4shell_versions = [
              "2.0-beta9", "2.0-rc1", "2.0-rc2", "2.0", "2.0.1",
              "2.0.2", "2.1", "2.2", "2.3", "2.4", "2.4.1", "2.5",
              "2.6", "2.6.1", "2.6.2", "2.7", "2.8", "2.8.1",
              "2.8.2", "2.9.0", "2.9.1","2.10.0", "2.11.0", "2.11.1",
              "2.11.2", "2.12.0", "2.12.1", "2.13.0", "2.13.1",
              "2.13.2", "2.13.3", "2.14.0", "2.14.1", "2.15.0"
          ]
          predicate: {
              Data: {
                  packages: [...{
                      name: name
                      versionInfo: versionInfo
                      if list.Contains(log4shell_names, name) &&
                          list.Contains(log4shell_versions, versionInfo) {
                          err: strings.Join([
                              "Error: SPDX SBOM contains package",
                              name, "version", versionInfo, "which is",
                              "vulnerable to Log4Shell (CVE-2021-44228)"
                          ], " ")
                          name: err
                      }
                  }]
              }
          }
EOF
```

All Chainguard Enforce policies are stored in YAML files like this one. This example has three particularly important objects:

* `images`: this defines what images the policy applies to. In this example, the value is a `glob` key with a value of `"ghcr.io/chainguard-dev/log4shell-demo/*"`. This means that the policy will apply to any images that originate from the `ghcr.io/chainguard-dev/log4shell-demo/` URL, including the sample application running on your cluster (`ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0`).
* `authorities`: this specifies what authorities the policy will allow to validate signatures and attestations. If at least one authority is satisfied and a signature or attestation is validated, that part of the policy is satisfied. In this case the relevant value is `keyless`, meaning this policy will check the image for any valid signature in the public instance of Sigstore located at `https://fulcio.sigstore.dev`. Note that anyone can add signatures to the public instance, so it is recommended to limit the scope of valid signatures using the fields `issuerRegExp` and `subjectRegExp`. 
* `attestations`: this array within the `authorities` section is where you can configure specific conditions that must be met in order for the policy to be satisfied. In short, this example's `attestations` array requires that any `images` that fall under the policy must have either a [CycloneDX](https://cyclonedx.org/) or an [SPDX](https://spdx.dev/) SBOM in order to satisfy the policy. Additionally, if an image's SBOM indicates that the package contains certain versions of Apache Log4j (specifically, versions `"2.0-beta9",` through `"2.15.0"`), then it will result in the policy failing.

Note that this `attestations` array requires that images must have either a CycloneDX *or* SPDX SBOM attached. Every attestation listed within the same `attestations` array is treated as a logical `OR`. If you want images to satisfy multiple attestations – in other words, combining them with `AND` logic – you would need to create multiple policies. Each policy must then be satisfied individually.

For more information on how policies work in Chainguard Enforce, check out [Sigstore’s documentation on how it handles and reads policies](https://docs.sigstore.dev/policy-controller/overview/).

After creating the policy file, you can use it to activate a policy for your cluster by running the following command.

```sh
chainctl policies create log4shell-demo-policy \
    --group $GROUP_ID \
    -f log4shell-demo-policy.yaml
```

To confirm that the policy was successfully created, run the following command to retrieve a list of all your active policies.

```sh
chainctl policies ls
```

Ensure that your new policy has ended up in the `config-image-policies` configmap by running this command.

```sh
kubectl -n cosign-system get configmap config-image-policies -o yaml
```

This will return a lot of information, but you will know that the policy is in the configmap if this output includes a `log4shell-demo-policy` key.

```
apiVersion: v1
data:
  log4shell-demo-policy: ...
```

You can find all records in the cluster containing SBOMs indicating the Log4Shell vulnerability using the following command.

```sh
chainctl cluster records ls $CLUSTER
```

Under the `POLICIES` column you'll receive output that indicates the policy has failed.

```
                                       IMAGE                                      |            POLICIES            |   WORKLOADS   | PACKAGES | LAST SEEN | LAST REFRESHED  
----------------------------------------------------------------------------------+--------------------------------+---------------+----------+-----------+-----------------
  ghcr.io/chainguard-dev/log4shell-demo/app@sha256:ba4037…                        | log4shell-demo-policy:fail:40s | Pod:1         | maven:2  | 3m49s     | sbom:39s        
. . .
```

Information about the SBOM and the policy violation will also appear in the UI.

![Screenshot of the Chainguard Enforce UI. At the top are cards showing 0% policy compliance, 1 package type, 1 failed policy. The POLICIES tab is highlighted and contains a table with one row, representing the log4shell-demo-policy policy. This row includes the name of the policy, a meter showing 0/1 images are compliant, the policy's group (log4j-demo), and a button allowing the user to view the violation.](log4shell-demo-ui-failure-sm.png)


## Step 4 – Cleaning Up Your System

After confirming that the policy you set causes Chainguard Enforce to detect the images vulnerable to the Log4Shell vulnerability, it's important that you clean up your system.

Start by deleting the pod running the vulnerable application.

```sh
kubectl delete pod log4shell-demo
```

Then delete the policy. 

```sh
chainctl policy delete -y log4shell-demo-policy
```

This will cause the policy to be removed from the policy list in both the CLI and UI.

Lastly, uninstall the agent from your cluster.

```sh
chainctl cluster uninstall
```

You'll receive a confirmation that the agent was removed.


## Learn More

By following this guide, you will have a better understanding of how to set up a Chainguard Enforce policy. You can use this understanding to apply other policies to your cluster. 

To continue your learning, we encourage you to check out this [sample policy for Enforce published by Chainguard](https://github.com/chainguard-dev/text4shell-policy). This policy protects against the [Text4Shell vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2022-42889). When installed into a cluster, this policy will identify and optionally block workloads containing vulnerable versions of Apache Commons Text from running on customer clusters.
