---
title: "Getting Started"
type: "article"
description: "Getting Started with Chainguard Enforce Signing"
date: 2023-01-26T15:56:52-07:00
lastmod: 2022-01-26T15:56:52-07:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-signing"
weight: 10
toc: true
---

> _This documentation is related to Chainguard Enforce Signing. You can request access to the product selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Powered by the open source security tool suite [Sigstore](https://www.sigstore.dev/), Chainguard Enforce Signing enables you to generate digital signatures for software artifacts inside your own organization using the individual identities of your team members and [ephemeral keys](https://www.chainguard.dev/unchained/the-principle-of-ephemerality). Enforce Signing can be monitoried and audited against your organization's compliance and privacy requirements so you have full control. Learn more about Enforce Signing in our [Overview and FAQs doc](/chainguard/chainguard-enforce/chainguard-enforce-signing/chainguard-enforce-signing-faqs/).

This guide will onboard you to Chainguard Enforce Signing on Google Cloud Platform (GCP).

## Prerequisites

In addition to having access to Chainguard Enforce (which you can request via our [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)) and an [IAM group](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/how-to-manage-iam-groups-in-chainguard-enforce/) set up, you will need the following tools and versions noted in order to follow this guide.

* [Go](https://go.dev/doc/install), version 1.19.3 or above
* [Cosign, version 2.0.0-rc.1](/open-source/sigstore/cosign/how-to-install-cosign/#installing-a-cosign-pre-release-with-go) or above
* [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli), version 1.2.8 or above
* The [Chainguard command line tool `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/), version 0.1.

You will also need access to a GCP account, Google Kubernetes Engine (GKE), and the relevant [tools and configuration to orchestrate GKE](https://cloud.google.com/anthos/fleet-management/docs/before-you-begin/gke), including the [gcloud CLI tool](https://cloud.google.com/sdk/gcloud).  

With these tools in place you are reading to begin.

## Step 1 — Set Up a Certificate Authority

If you don't have a certificate authority (CA) already, you'll first need to host your own for Enforce Signing to request certificates from it. We will walk through setting up a Google Certificate Authority Service. 

To set up a Google CA Service, you'll first need an instance of the GCP CA Service in your GCP Project. You can enable the CA service by running the following command. This may take a few minutes.

```sh
gcloud services enable privateca.googleapis.com
```

You'll need create a new CA Pool (alternately, you can use an existing one if you have one set up). For demonstration purposes, we'll use the `devops` tier. Replace `$POOL_NAME` with the name you would like to use for your CA Pool. 

```sh
gcloud privateca pools create $POOL_NAME --tier=devops
```

Read the [full documentation about Google CA Pools](https://cloud.google.com/certificate-authority-service/docs/creating-ca-pool) for more details.

Then you’ll create a new root certificate authority. The below is an example command to set this up. You can also set this up in the Console user interface. Please read the full [Creating certificate authorities doc](https://cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities) from GCP to understand all your options.

Pass a name you will remember to `$ROOT_CA_NAME`, and the name you gave to your CA Pool in place of `$POOL_NAME`.

```sh
gcloud privateca roots create $ROOT_CA_NAME --pool=$POOL_NAME \
  --subject="CN=my-ca, O=Test LLC"
```

You can optionally use a `--key-algorithm` flag in the command above. Without it, the above command defaults to `rsa-pkcs1-4096-sha256`. Read more about the [crypto algorithm to use for creating a managed KMS key](https://cloud.google.com/sdk/gcloud/reference/beta/privateca/roots/create#--key-algorithm) for a CA and its options. 

Once you’ve set up your CA, keep its resource name readily available. You may have to click **View CA certificate** in the Console user interface to find the resource name, under **Resource name**. It is expected to be in a format similar to the following, with the variables referring to your own project details.

```
projects/$PROJECT_ID/locations/$LOCATION/caPools/$POOL_NAME/certificateAuthorities/$CA_ID
```

With this set up, you're ready to set up your own instance of Chainguard Enforce Signing.

## Step 2 — Create an Enforce Signing Instance

to set up a Chainguard Enforce Signing instance, you'll be using `chainctl`, the Chainguard CLI tool. You can choose any name that is meaningful to you to reference this instance, replace the `$ENFORCE_SIGNING_NAME` variable with the name of your choosing. Also, replace the `$CA_RESOURCE_NAME` with the long resource name (discussed above) of your Google CA Service.

```sh
chainctl sigstore ca create --name=$ENFORCE_SIGNING_NAME --ca=googleca  --googleca-ref=$CA_RESOURCE_NAME 
```

Each Enforce Signing instance comes with a unique hostname for the certificate authority, which you can find by running:

```sh
chainctl sigstore ca ls 
```

You can use this command to pull up the ID and name of your CA at any time. 

## Step 3 — Setting Up Account Association

Now that you’ve provided Enforce with references to your CA service, you’ll need to give Chainguard authorization to use those resources.

To set up your account association, you'll be using Terraform. Follow our guidance on [Cloud Account Association for GCP](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/cloud-account-associations/#setting-up-a-cloud-account-association-for-gcp) to complete this setup.

To confirm resources were set up as expected, you can navigate to your [Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools) within your GCP Project. On this page should be a resource called **Chainguard Pool**. If you click on the pool details and review the **connected service accounts**, you'll have a few service accounts that are now prefixed with `chainguard`. The service account `chainguard-enforce-signer` that the Enforce Signing service will be running under to request certificates. 

To confirm that the account association setup was successful, run this `chainctl` command.

```sh
chainctl iam groups check-gcp
```

You may need to select the Group that you are currently working with.

If everything is set up correctly, you'll receive output similar to the following.

```
GCP role impersonation was successful!
```

With everything set up, we are now ready to work with a software artifact.

## Step 4 — Set Up and Publish a Container Image

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

## Step 5 — Signing and Verifying an Image

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

Congratulations! You have signed and verified a software artifact with Chainguard Enforce Signing!

## Learn More

To understand more about Enforce Signing, review the [Overview and FAQs](/chainguard/chainguard-enforce/chainguard-enforce-signing/chainguard-enforce-signing-faqs/).

If you would like to learn more about Sigstore, the open source tool suite that Enforce Signing is built on, check out Chainguard Academy's [section on Sigstore](/open-source/sigstore/).