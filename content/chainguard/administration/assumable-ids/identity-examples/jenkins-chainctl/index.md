---
title: "Use chainctl to Create an Assumable Identity for a Jenkins Pipeline"
linktitle: "Jenkins with chainctl"
description: "How to use chainctl to create a Chainguard identity that can be assumed by a Jenkins Pipeline."
type: "article"
date: 2025-09-07T08:48:45+00:00
lastmod: 2025-09-07T08:48:45+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 025
---

[Jenkins](https://www.jenkins.io/) is an open source automation server that supports building, deploying, and automating projects.

This guide explains how to use `chainctl` to create an assumable identity and configure Jenkins to use that identity to authenticate to Chainguard. To accomplish this, we will create an OIDC token credential in Jenkins and then a matching Chainguard identity that uses the Jenkins OIDC URL and put the process into an example Jenkins build pipeline.

If you would like to follow this guide using Terraform, you can review [Use Terraform to Create an Assumable Identity for a Jenkins Pipeline](/chainguard/administration/assumable-ids/identity-examples/jenkins-identity-terraform/).


## Prerequisites

- A running [Jenkins](https://www.jenkins.io/doc/pipeline/tour/getting-started/) instance.
    - This Jenkins instance should have the [**Open ID Connect Provider** plugin](https://plugins.jenkins.io/oidc-provider/) installed, allowing you to create an OIDC token with Jenkins.
- [`chainctl`](https://edu.chainguard.dev/chainguard/chainctl-usage/how-to-install-chainctl/) installed locally.
- Administrative privileges within your Chainguard organization to create IAM identities (`identity.create`); this capability is available to users with [the owner role](https://edu.chainguard.dev/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/#chainguard-role-capabilities).


## Configure Jenkins Credentials

Jenkins needs a way to supply `chainctl` with an API token so it can exchange it for short-lived credentials when a pipeline runs.

In this example, Jenkins mints an OIDC ID token during each build and `chainctl` uses that token to allow the build pipeline to assume your Chainguard identity — no long-lived secrets are required.

> **NOTE**: Why not a “long-lived API token”? Chainguard does not issue general-purpose, long-lived API tokens. This ensures your automation relies only on short-lived, scoped credentials.


### Create an OIDC token credential

To get started, create an OIDC token with Jenkins:

1. Log in to the Jenkins UI
2. Navigate to the **Manage Jenkins** page by clicking the settings gear (**⚙**) in the upper-right corner
3. Navigate to the **Credentials** page by clicking **Credentials**
4. In the Domain column, click **(global)**
5. On the **Global credentials (unrestricted)** page, click **Add Credentials**
6. Use the **Kind** dropdown to select **OpenID Connect id token**
7. Enter an **ID**, our example uses `jenkins-oidc`.
8. Click **Create**


## Create a Matching Chainguard Identity

Create an identity that uses your Jenkins OIDC URL. This is typically `https://YOUR_JENKINS/oidc`:

```shell
chainctl iam identities create jenkins-ci \
  --identity-issuer https://YOUR_JENKINS/oidc \
  --subject jenkins \
  --description "Identity for Jenkins builds" \
  --output json
```

Bind the identity to a role. We chose `registry.pull` for this example, but you should adjust according to your needs. Refer to [Overview of Roles and Role-bindings in Chainguard](https://edu.chainguard.dev/chainguard/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) to learn more:

```shell
chainctl iam role-bindings create \
  --identity=jenkins-oidc \
  --role=registry.pull
```

You can now use this identity in your build pipeline to authenticate to Chainguard.


## Use the Identity and Create a Token in Your Jenkins Pipeline

Here is an example Jenkinsfile that uses what we just created. In this pipeline:

- `jenkins-oidc` is the credential ID you created in Jenkins for an OpenID Connect (OIDC) token.
- The `withCredentials` step injects the value of that credential into the environment variable `IDTOKEN` for the duration of the block.
- Inside the `sh` section of the `withCredentials` step, `$IDTOKEN` refers to that environment variable containing the actual OIDC token issued by Jenkins at build time while `chainctl auth login --identity-token "$IDTOKEN"` uses that token to authenticate to Chainguard and assume the Jenkins identity.

Be sure to replace the `ORGANIZATION` placeholder with the name used for your organization's private repository within the Chainguard Registry.


```groovy
pipeline {
  agent any

  environment {
    CHAINCTL_IDENTITY = "iam-1234567890" // replace with your identity ID
  }

  stages {
    stage('Install chainctl') {
      steps {
        sh '''
          mkdir -p .bin
          curl -fsSL -o .bin/chainctl \
            "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/aarch64/arm64/; s/x86_64/amd64/')"
          chmod +x .bin/chainctl
        '''
      }
    }

    stage('Auth with Chainguard') {
      steps {
        withCredentials([string(credentialsId: 'jenkins-oidc', variable: 'IDTOKEN')]) {
          sh '''
            echo "Logging in to Chainguard using OIDC..."
            chainctl auth login \
              --identity "$CHAINCTL_IDENTITY"
            chainctl auth configure-docker
          '''
        }
      }
    }

    stage('Pull image') {
      steps {
        sh 'docker pull cgr.dev/ORGANIZATION/python:latest' //replace with your org
      }
    }
  }
}
```

> **NOTE**: `$IDTOKEN` is not something you create manually; it comes from the Jenkins credentials plugin at runtime. You just need to make sure that you created the credential in Jenkins with ID `jenkins-oidc` and that the credential type is OpenID Connect ID token.

After you run this pipeline, check to see that the requested Chainguard image was pulled to confirm everything is set up properly.

## Learn More

In this guide you used `chainctl` to create an assumable identity and configure Jenkins to use that identity to authenticate to Chainguard. Refer to the following to learn more about how Chainguard has designed assumable IDs, `chainctl`, and authentication.

- [Assumable IDs](/chainguard/administration/assumable-ids/)
- [How to Install chainctl](/chainguard/chainctl-usage/how-to-install-chainctl/)
- [Authenticating with Chainguard Registry](/chainguard/chainguard-images/chainguard-registry/authenticating/)
