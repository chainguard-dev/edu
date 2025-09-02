---
title : "Use chainctl to Create an Assumable Identity for a Jenkins Pipeline"
linktitle: "Jenkins with chainctl"
aliases:
lead: ""
description: "How to use chainctl to create a Chainguard identity that can be assumed by a Jenkins Pipeline."
type: "article"
date: 2025-08-27T08:03:42+00:00
lastmod: 2025-08-27T08:03:42+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 025
---

This guide explains how to configure Jenkins to authenticate with Chainguard using an assumable identity. This example uses `chainctl`, Chainguard's command line tool. If you would like to follow this guide using Terraform, you can review [Use Terraform to Create an Assumable Identity for a Jenkins Pipeline](/chainguard/administration/assumable-ids/identity-examples/jenkins-identity-terraform/).

With this setup, Jenkins jobs can securely push and pull container images from the Chainguard registry without managing static credentials.


## Prerequisites

- A running Jenkins controller.
- chainctl installed and accessible from Jenkins agents.
- Access to your Chainguard organization with permission to create IAM identities.


## Create a Jenkins Assumable ID

Use `chainctl` to create an identity that Jenkins can use to authenticate:

```shell
chainctl iam identities create jenkins-oidc \
  --identity-issuer https://chainguard.dev/ \
  --subject jenkins \
  --description "Identity for Jenkins builds" \
  --output json
```

Note the returned identity ID. This guide uses `iam-1234567890` for an example.


## Allow Jenkins to Assume the Identity

Bind the new identity to your Chainguard organization’s default role or a more restrictive one:

```shell
chainctl iam role-bindings create \
  --identity=iam-1234567890 \
  --role=registry.pull
```

This example grants Jenkins permission to authenticate as a member with privileges for pulling from the Chainguard registry.


## Configure Jenkins Credentials

Jenkins needs a way to supply `chainctl` with an API token so it can exchange it for short-lived credentials when a pipeline runs.

In this example, Jenkins mints an OIDC ID token during each build and `chainctl` uses that token to assume your Chainguard identity — no long-lived secrets are required.

> **NOTE**: Why not a “long-lived API token”? Chainguard does not issue general-purpose, long-lived API tokens. This ensures your automation relies only on short-lived, scoped credentials.


### Install & Configure the Jenkins OIDC Plugin

Jenkins does not come with OIDC functionality by default, but it is available in the **Open ID Connect Provider** plugin that you may need to install. Refer to https://plugins.jenkins.io/oidc-provider/ for more information about the plugin.


### Create an OIDC token credential

In the Jenkins UI, go to Manage Jenkins > Credentials > (Global) and from here select **Add Credentials**.

Use the **Kind** dropdown to select **OpenID Connect id token**.

Enter an **ID**, our example uses `jenkins-oidc`.


### Create a Matching Chainguard Identity

The Jenkins OIDC token’s issuer is typically `https://YOUR_JENKINS/oidc`.

Create an identity that uses your Jenkins OIDC URL.

```shell
chainctl iam identities create jenkins-ci \
  --identity-issuer https://YOUR_JENKINS/oidc \
  --subject jenkins \
  --description "Identity for Jenkins builds" \
  --output json
```

Bind a role to the identity.

```shell
chainctl iam role-bindings create \
  --identity=jenkins-oidc \
  --role=registry.pull
```

Now you are ready to use the token.


## Use the token in your Pipeline

Here is a minimal working example Jenkinsfile that uses what we just created.

```groovy
pipeline {
  agent any

  environment {
    CHAINCTL_IDENTITY = "iam-1234567890" // replace with your identity ID
  }

  stages {
    stage('Auth with Chainguard') {
      steps {
        withCredentials([string(credentialsId: 'jenkins-oidc', variable: 'IDTOKEN')]) {
          sh '''
            echo "Logging in to Chainguard using OIDC..."
            chainctl auth login \
              --identity-token "$IDTOKEN" \
              --identity "$CHAINCTL_IDENTITY"
            chainctl auth configure-docker
          '''
        }
      }
    }

    stage('Pull image') {
      steps {
        sh 'docker pull cgr.dev/chainguard/python:latest'
      }
    }
  }
}
```

## Learn More

- [Assumable IDs](/chainguard/administration/assumable-ids/)
- [How to Install chainctl](/chainguard/chainctl-usage/how-to-install-chainctl/)
- [Authenticating with Chainguard Registry](/chainguard/chainguard-images/chainguard-registry/authenticating/)

