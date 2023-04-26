---
title: "Getting Started with Chainguard Enforce Signing"
linktitle: "Get Started with Enforce Signing"
type: "article"
description: "Getting Started with Chainguard Enforce Signing"
date: 2023-01-26T15:56:52-07:00
lastmod: 2022-01-26T15:56:52-07:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
menu:
  docs:
    parent: "chainguard-enforce-signing"
weight: 10
toc: true
---

**Chainguard Enforce Signing is in _Beta Preview_. You can request access to the product selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs).**

Powered by the open source security tool suite [Sigstore](https://www.sigstore.dev/), Chainguard Enforce Signing enables you to generate digital signatures for software artifacts inside your own organization using the individual identities of your team members and [ephemeral keys](https://www.chainguard.dev/unchained/the-principle-of-ephemerality). Enforce Signing can be monitoried and audited against your organization's compliance and privacy requirements so you have full control. Learn more about Enforce Signing in our [Overview and FAQs doc](/chainguard/chainguard-enforce/chainguard-enforce-signing/chainguard-enforce-signing-faqs/).

This guide will onboard you to Chainguard Enforce Signing.

## Prerequisites

In addition to having access to Chainguard Enforce (which you can request via our [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)) and an [IAM group](/chainguard/chainguard-enforce/iam-groups/how-to-manage-iam-groups-in-chainguard-enforce/) set up, you will need the following tools and versions noted in order to follow this guide.

* Public cloud access; on-premises workloads are not supported at this time.
* Your own certificate authority (CA), to set one up with GCP or AWS, follow our [CA setup guide](/chainguard/chainguard-enforce/chainguard-enforce-signing/enforce-signing-setup)
* [Go](https://go.dev/doc/install), version 1.19.3 or above
* [Cosign, version 2.0.0](/open-source/sigstore/cosign/how-to-install-cosign/#installing-a-cosign-release-with-go) or above
* [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli), version 1.2.8 or above
* The [Chainguard command line tool `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/), version 0.1 or above.

With these tools and setup in place you are ready to begin.


## Step 1 — Setting Up Account Association

Now that you’ve provided Enforce with references to your CA service, you’ll need to give Chainguard authorization to use those resources.

To set up your account association, you'll be using Terraform. Follow our guidance on [Cloud Account Association](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/cloud-account-associations) to complete this setup for either GCP or AWS.

You can confirm that resources were set up as expected with your cloud provider. In GCP, you can navigate to your [Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools). On this page should be a resource called **Chainguard Pool**. If you click on the pool details and review the **connected service accounts**, you'll have a few service accounts that are now prefixed with `chainguard`. The service account `chainguard-enforce-signer` that the Enforce Signing service will be running under to request certificates.

To confirm that the account association setup was successful, run the relevant `chainctl` command for GCP or AWS, respectively.

```sh
chainctl iam groups check-gcp
```

```sh
chainctl iam groups check-aws
```

You may need to select the Group that you are currently working with.

If everything is set up correctly, you'll receive output similar to the following.

```
... role impersonation was successful!
```

With everything set up, we are now ready to work with a software artifact.

## Step 2 — Set Up and Publish a Container Image

**If you have a container already in a container registry that you can use for demonstration purposes, feel free to skip this step and proceed to [Step 5](/chainguard/chainguard-enforce/chainguard-enforce-signing/getting-started-chainguard-enforce-signing/#step-5-signing-and-verifying-an-image).**

Otherwise, we'll quickly set up a demo image and publish it so that we can sign and verify it with Chainguard Enforce Signing in the next step.

Let's create and move into a directory for our container image. Replace `$USERNAME` below with a username you may use on a container registry, or your name.

```sh
mkdir -p ~/$USERNAME/hello-signing && cd $_
```

In this diretory create a Dockerfile and open it in a text editor. For example, you can use Nano.

```sh
nano Dockerfile
```

Type the following into your editor.

```bash
FROM alpine
CMD ["echo", "Let's sign with Enforce Signing!"]
```

Once you are satisfied that your Dockerfile is the same as the text above, you can save and close the file.

We will publish this container to [ttl.sh](https://ttl.sh/), which is an anonymous and ephemeral container registry. If you would prefer to publish this in another container registry, feel free to do so.

We'll start by building the image. The `1h` tag tells ttl.sh to store the image in their registry for one hour, you can modify the time for your purposes.

```sh
sudo docker build -t ttl.sh/$USERNAME/hello-signing:1h .
```

Next, push the image to the registry.

```sh
docker push ttl.sh/$USERNAME/hello-signing:1h
```

At this point, you will receive output that your container was published and you are ready to continue to the final step.

## Step 3 — Signing and Verifying an Image

You are now ready to sign and verify an image with your brand new Certificate Authority!

First, [log into Chainguard](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/log-in-chainguard-enforce/#signing-in-through-chainctl):

```sh
chainctl auth login
```

This workflow will ask you to go through an [OIDC flow](software-security/glossary/#oidc) to authenticate with Chainguard.

Next, you’ll need to set up your environment to point Cosign to your personal Enforce Signing instance. Here, replace `$ENFORCE_CA_NAME` with the name of your Enforce CA. You can pull this up again by running `chainctl sigstore ca ls `.

```sh
eval $(chainctl sigstore env $ENFORCE_CA_NAME)
```

You will have to authenticate again, to get an authentication token unique to your instance of Enforce Signing. This command will set the required environment variables for Cosign to sign your image with your private CA.

You are now ready to sign by following the steps below. If you followed [Step 4](/chainguard/chainguard-enforce/chainguard-enforce-signing/getting-started-chainguard-enforce-signing/#step-4--set-up-and-publish-a-container-image), replace `$IMAGE` with `ttl.sh/$USERNAME/hello-signing:1h`, otherwise fill in your own image that you would like to sign.

```sh
eval $(chainctl sigstore env $ENFORCE_CA_NAME)
cosign sign $IMAGE
```

Finally, you are ready to verify your image. The `cosign verify` command expects both a certificate identity and an issuer. The issuer, `https://auth.chainguard.dev`, is already set by the `sigstore env` command. The certificate identity will correspond to the email address you used to authenticate to Chainguard. Replace `$EMAIL` below with that email address.

```sh
eval $(chainctl sigstore env $ENFORCE_CA_NAME)
cosign verify $IMAGE --certificate-identity=$EMAIL
```

You can also verify with a wildcard certificate identity, as in the following command.

```sh
eval $(chainctl sigstore env $ENFORCE_CA_NAME)
cosign verify $IMAGE --certificate-identity-regexp=".*"
```

After running this command, you should receive output that returns that the Cosign claims and certificate were verified.

```
Verification for $IMAGE --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - The code-signing certificate was verified using trusted certificate authority certificates

[{"critical":{"identity":{"docker-reference":"$IMAGE"},"image":{"docker-manifest-digest":"sha256:77...9"},"type":"cosign container image signature"},"optional":{"...":"https://auth.chainguard.dev/","Issuer":"https://auth.chainguard.dev/","..."},"Subject":"$EMAIL"}}]
```

This output indicates that software artifact's signature was successfully verified.

## Learn More

To understand more about Enforce Signing, review the [Overview and FAQs](/chainguard/chainguard-enforce/chainguard-enforce-signing/chainguard-enforce-signing-faqs/).

If you would like to learn more about Sigstore, the open source tool suite that Enforce Signing is built on, check out Chainguard Academy's [section on Sigstore](/open-source/sigstore/).


## Next Steps

Now that you have a signed image, you can proceed to create Enforce policies with this tutorial on [Example Policy for Enforce Signed Images](/chainguard/chainguard-enforce/chainguard-enforce-signing/verify-enforce-signed-images/).