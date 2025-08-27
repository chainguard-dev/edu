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
weight: 030
---

This guide explains how to configure Jenkins to authenticate with Chainguard using an assumable identity. This example uses `chainctl` directly, instead of Terraform like in [the other example](/chainguard/administration/assumable-ids/identity-examples/jenkins-identity-terraform/).

With this setup, Jenkins jobs can securely push and pull container images from the Chainguard registry without managing static credentials.


## Prerequisites

- A running Jenkins controller or agent with:
    - chainctl installed and available in $PATH.
    - Docker or another container runtime installed.
- Admin access to your Chainguard organization.
- An existing assumable ID created for Jenkins, or permissions to create one.


## Create a Jenkins Assumable ID

Use chainctl to create an identity that Jenkins can use to authenticate:

```sh
chainctl iam identities create \
  --name jenkins-ci \
  --description "Identity for Jenkins builds" \
  --output json
```

Note the returned identity ID. This guide uses `iam-1234567890` for an example.


## Allow Jenkins to Assume the Identity

Bind the new identity to your Chainguard organization’s default role or a more restrictive one:

```sh
chainctl iam roles bindings create \
  --role chainguard:member \
  --identity iam-1234567890
```

This grants Jenkins permission to authenticate as a member.


## Configure Jenkins Credentials

There are two ways to do this, via the Jenkins UI or using Jenkins Configuration as Code (JCasC).

### Via the Jenkins UI

In your Jenkins instance, open Manage Jenkins → Credentials → Global credentials (unrestricted).

Add a new Secret text credential as described in the [Jenkins documentation](https://www.jenkins.io/doc/book/using/using-credentials/). Enter the following in these fields:

- ID: `chainctl-token`
- Secret text: Enter a [long-lived API token](/chainguard/administration/api-tokens/) for your Jenkins service account.

This token will allow Jenkins to call chainctl and exchange the API token for short-lived OIDC tokens when needed.

### Via Jenkins Configuration as Code

Insert this YAML information into your configuration.

```yaml
credentials:
  system:
    domainCredentials:
      - credentials:
          - string:
              id: "chainctl-token"
              description: "Chainguard API token for chainctl"
              secret: "${CHAINCTL_TOKEN_VALUE}"

```


## Use the Identity in a Jenkins Pipeline

This example [Jenkins pipeline](https://www.jenkins.io/doc/book/pipeline/):
- Logs chainctl in using the stored API token
- Assumes the Jenkins identity to obtain short-lived credentials
  - `chainctl auth login` authenticates Jenkins with Chainguard using the stored API token.
  - `chainctl iam identities assume` exchanges that authentication for a short-lived identity credential and runs `docker login cgr.dev`.
- Builds and pushes an image

```groovy
pipeline {
  agent any
  environment {
    CHAINCTL_TOKEN = credentials('chainctl-token')
    IDENTITY = "iam-1234567890"
  }
  stages {
    stage('Login to Chainguard') {
      steps {
        sh '''
          echo "$CHAINCTL_TOKEN" | chainctl auth login --token-stdin
          chainctl iam identities assume $IDENTITY -- docker login cgr.dev
        '''
      }
    }
    stage('Build and Push Image') {
      steps {
        sh '''
          docker build -t cgr.dev/my-org/my-image:$BUILD_NUMBER .
          docker push cgr.dev/my-org/my-image:$BUILD_NUMBER
        '''
      }
    }
  }
}
```


## Learn More

- [Assumable IDs](https://chatgpt.com/chainguard/administration/assumable-ids/)
- [chainctl API](/chainguard/chainguard-cli/install/)
- [Authenticating with Chainguard Registry](https://chatgpt.com/chainguard/chainguard-images/chainguard-registry/authenticating/)