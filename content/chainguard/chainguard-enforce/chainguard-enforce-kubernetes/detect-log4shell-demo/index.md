---
title: "Using Chainguard Enforce to Detect the Log4Shell Vulnerability"
type: "article"
description: "Use chainctl to create a policy and apply it to a cluster to detect vulnerable versions of Log4J"
date: 2022-08-11T11:07:52+02:00
lastmod: 2023-05-01T11:07:52+02:00
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
* `jq` installed on your local machine. `jq` is a command-line JSON processor that allows you to filter and manipulate streaming JSON data. Although it isn't strictly necessary to create a policy to detect for vulnerable Log4J installations, this tutorial includes commands that use `jq` to filter attestation details that would otherwise be unintelligible. You can install `jq` by following the instructions on [the project's Download `jq` page](https://stedolan.github.io/jq/download/).


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
                         	ID                         	|   NAME	|	DESCRIPTION 	 
------------------------------------------------------------+-----------+---------------------
  53c080777a7d97samplegroupid07928aa3de055              	| log4demo  |                	 
  60adedf1d5db70examplerootidf32f6b7e09fc5              	| root  	| Default user group  
```

Copy the ID value of the group managing the cluster you'll use to test Chainguard Enforce, and then use that value in place of `$COPIED_ID` in the following command. This will set an environment variable called `GROUP` whose value is equal to the ID number Enforce uses to refer to your IAM group.

```sh
export GROUP=$COPIED_ID
```

Next, run the following command to retrieve a list of all your active clusters.

```sh
chainctl cluster list
```
```
              	NAME             	|   GROUP   |           	REMOTEID           	| REGISTERED |	K8S VERSION	| AGENT VERSION | LAST SEEN | 	ACTIVITY  	 
---------------------------------------+-----------+--------------------------------------+------------+-------------------+---------------+-----------+--------------------
  12345678-32fd-44b3-bea9-6046341ceda1 | log4demo  | 12345678-32fd-44b3-bea9-6046341ceda1 |  	3m18s | v1.22.12-gke.2300 | 25bffd1-dirty |   	12s | cosign-system:14s  
                                   	|       	|                                  	|        	|               	|           	|       	|   eots-system:59s  
                                   	|       	|                                  	|        	|               	|           	|       	| policy-system:12s

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
cosign download attestation ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0 | jq -r .payload | base64 -d | jq > log4shell-sbom.json
```

This command downloads an attestation containing the image's SBOM from the same location where the image is found. However, this SBOM data is encoded in base64, making it unreadable without further processing. This is why the output from the first part of the command is piped into `jq` in order to filter out the `payload` section of the output containing the SBOM. 

This filtered output is then passed into the `base64` command to be decoded before that output is piped into another `jq` command. This final `jq` command processes the decoded JSON and writes it to a file named `log4shell-sbom.json`.

Following that, you can inspect the SBOM by reading the content of this new file.

```sh
cat log4shell-sbom.json
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

Chainguard Enforce policies are typically written in YAML like this sample policy. This example has three particularly important objects:

* `images`: this defines what images the policy applies to. In this example, the value is a `glob` key with a value of `"ghcr.io/chainguard-dev/log4shell-demo/*"`. This means that the policy will apply to any images that originate from the `ghcr.io/chainguard-dev/log4shell-demo/` URL, including the sample application running on your cluster (`ghcr.io/chainguard-dev/log4shell-demo/app:v0.1.0`).
* `authorities`: this specifies what authorities the policy will allow to validate signatures and attestations. If at least one authority is satisfied and a signature or attestation is validated, that part of the policy is satisfied. In this case the relevant value is `keyless`, meaning this policy will check the image for any valid signature in the public instance of Sigstore located at `https://fulcio.sigstore.dev`. Note that anyone can add signatures to the public instance, so it is recommended to limit the scope of valid signatures using the fields `issuerRegExp` and `subjectRegExp`.
* `attestations`: this array within the `authorities` section is where you can configure specific conditions that must be met in order for the policy to be satisfied. In short, this example's `attestations` array requires that any `images` that fall under the policy must have either a [CycloneDX](https://cyclonedx.org/) or an [SPDX](https://spdx.dev/) SBOM in order to satisfy the policy. Additionally, if an image's SBOM indicates that the package contains certain versions of Apache Log4j (specifically, versions `"2.0-beta9",` through `"2.15.0"`), then it will result in the policy failing.

Note that this `attestations` array requires that images must have either a CycloneDX *or* SPDX SBOM attached. Every attestation listed within the same `attestations` array is treated as a logical `OR`. If you want images to satisfy multiple attestations – in other words, combining them with `AND` logic – you would need to create multiple policies. Each policy must then be satisfied individually.

For more information on how policies work in Chainguard Enforce, check out [Sigstore’s documentation on how it handles and reads policies](https://docs.sigstore.dev/policy-controller/overview/).

After creating the policy file, you can use it to activate a policy for your cluster by running the following command.

```sh
chainctl policies create log4shell-demo-policy \
	--group $GROUP \
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
                                   	IMAGE                                  	|        	POLICIES        	|   WORKLOADS   | PACKAGES | LAST SEEN | LAST REFRESHED  
----------------------------------------------------------------------------------+--------------------------------+---------------+----------+-----------+-----------------
  ghcr.io/chainguard-dev/log4shell-demo/app@sha256:ba4037…                    	| log4shell-demo-policy:fail:40s | Pod:1     	| maven:2  | 3m49s 	| sbom:39s   	 
. . .
```

Information about the SBOM and the policy violation will also appear in the UI.

![Screenshot of the Chainguard Enforce UI. At the top are cards showing 0% policy compliance, 1 package type, 1 failed policy. The POLICIES tab is highlighted and contains a table with one row, representing the log4shell-demo-policy policy. This row includes the name of the policy, a meter showing 0/1 images are compliant, the policy's group (log4j-demo), and a button allowing the user to view the violation.](log4shell-demo-ui-failure-sm.png)


### Supplement: Detecting Text4Shell

In 2022, a vulnerability was discovered within the Java library "Apache Commons Text". By injecting specific keywords, a malicious actor can execute arbitrary code on any server where Apache Commons Text is running. Because of its similarities with Log4Shell, this vulnerability ([CVE-2022-42889](https://nvd.nist.gov/vuln/detail/CVE-2022-42889)) has come to be known as "Text4Shell".

This supplemental section outlines how to set up a Chainguard Enforce policy that will detect any vulnerable versions of Apache Commons Text as well as how to test this policy by deploying a vulnerable sample application. Because much of the process is similar to the one for detecting Log4Shell outlined previously, this extra section won't go into the same level of detail.

First, run a container image vulnerable to Text4Shell. As with the Log4Shell demo image, Chainguard maintains a sample container image that you can use. Although it is safe to use as an example for testing, **do not run this image in a production environment**.

Feel free to download this image's SBOM with the following command.

```sh
cosign download attestation ghcr.io/chainguard-dev/text4shell-policy:main | jq -r .payload | base64 -d | jq > text4shell-sbom.json
```

Then inspect the SBOM.

```sh
cat text4shell-sbom.json
```

After checking its contents, run the container image with `kubectl`.

```sh
kubectl run text4shell-demo --image=ghcr.io/chainguard-dev/text4shell-policy:main
```

Now that the container is running, create a policy file named `text4shell-demo-policy.yaml` using the following command.

```sh
cat > text4shell-demo-policy.yaml <<EOF
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: vuln-cve-2022-42889-text4shell
spec:
  images:
  - glob: "ghcr.io/chainguard-dev/*"
  authorities:
  - name: sigstore
    keyless:
      url: "https://fulcio.sigstore.dev"
    attestations:
    - predicateType: cyclonedx
      name: text4shellcyclonedx
      policy:
        type: cue
        data: |
          import (
            "list"
            "strings"
          )
          let text4shell_names = ["commons-text"]
          let text4shell_versions = ["1.5", "1.6", "1.7", "1.8", "1.9"]
          predicate: components: [...{
            name:    name
            version: version
            if list.Contains(text4shell_names, name) &&
              list.Contains(text4shell_versions, version) {
              err: strings.Join([
                "Error: CycloneDX SBOM contains package",
                name, "version", version, "which is",
                "vulnerable to text4shell (CVE-2022-42889)",
              ], " ")
              name: err
            }
          }]
EOF
```

Similar to the sample Log4Shell policy from Step 3, this policy will cover any images originating from `ghcr.io/chainguard-dev/text4shell-policy`. Any applicable images containing vulnerable versions of Apache Commons Text (versions `1.5` through `1.9`) will trigger a violation.

Apply this policy with the following command.

```sh
chainctl policies create text4shell-demo-policy \
	--group $GROUP \
	-f text4shell-demo-policy.yaml
```

You can confirm that the Text4Shell policy was created successfully by retrieving a list of all your active policies.

```sh
chainctl policies ls
```

You can also confirm that it has ended up in the `config-image-policies` configmap with this command.

```sh
kubectl -n cosign-system get configmap config-image-policies -o yaml
```

If this output contains a `vuln-cve-2022-42889-text4shell` key, then it confirms that this policy ended up in the configmap.

```
apiVersion: v1
Data:
. . .
  vuln-cve-2022-42889-text4shell: . . .
```

You can find all records in the cluster containing SBOMs indicating the Text4Shell vulnerability using the following command.

```sh
chainctl cluster records ls $CLUSTER
```

Under the `POLICIES` column you'll receive output that indicates the policy has failed.

```
                                   	IMAGE                                  	|        	POLICIES        	|   WORKLOADS   | PACKAGES | LAST SEEN | LAST REFRESHED  
----------------------------------------------------------------------------------+--------------------------------+---------------+----------+-----------+-----------------
  ghcr.io/chainguard-dev/text4shell-policy@sha256:4a2a87…   	| vuln-cve-2022-42889-text4shell:fail:8m39s | Pod:1     	| 3m44s		 
. . .
```

As before, information about the SBOM and the policy violation will also appear in the UI. This example shows an example cluster's policy violations for both the Log4Shell and Text4Shell sample policies, along with the diagnostics for both violations.

![Screenshot of the Chainguard Enforce UI showing with the CLUSTER DETAILS page. At the top are three cards showing 0% POLICY COMPLIANCE, 1 PACKAGE TYPE, and 2 FAILED POLICIES. Below, the POLICY VIOLATIONS tab is highlighted, showing two rows for violations relating to the "log4shell-demo" policy and the "vuln-cve-2022-42889-text4shell" policy, respectively. Each row has three columns. The IMAGE column lists the noncompliant image; the POLICY column lists the name of the policy being violated; the CHECKED column indicates how recently the image was checked for compliance. Additionally, both rows have a SHOW DIAGNOSTIC button that has been selected and now reads HIDE DIAGNOSTIC" This highlights the diagnosis for each recorded policy violation.](text4shell-violation.png)




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

> **Note:** If you followed the supplemental Text4Shell section, be sure to delete the pod and policy you created there as well.

```sh
kubectl delete pod text4shell-demo
chainctl policy delete -y text4shell-demo-policy
```

Lastly, uninstall the agent from your cluster.

```sh
chainctl cluster uninstall --context $CLUSTER
```

You'll receive a confirmation that the agent was removed.


## Learn More

By following this guide, you will have a better understanding of how to set up a Chainguard Enforce policy. You can use this understanding to apply other policies to your cluster.

To continue your learning, we encourage you to check out Chainguard's [catalog of sample policies](https://console.enforce.dev/policies/catalog) found in the UI. You can use these sample policies as written in your own environments or build on them to suit them to your own custom needs.