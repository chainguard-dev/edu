---
title: "How to Set Up a CA"
type: "article"
description: "Certificate Authority setup for Chainguard Enforce Signing"
date: 2023-02-01T15:56:52-07:00
lastmod: 2022-02-01T15:56:52-07:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
menu:
  docs:
    parent: "chainguard-enforce-signing"
weight: 30
toc: true
---

Chainguard Enforce Signing will request certificates from a certificate authority (CA) hosted by you. If you don't have one set up already, here are three ways to set up a CA to work with Enforce Signing:

* [**Option 1:** Set up with the Google Certificate Authority service in GCP](#step-1--set-up-google-ca)
* [**Option 2:** Set up with a KMS key in GCP and a root certificate chain provided by you](#option-2-kms-based-certificate-authority-with-gcp)
* [**Option 3:** Set up with a KMS key in AWS and a root certificate chain provided by you](#option-3-kms-based-certificate-authority-with-aws)

Please choose which way you’d like to set up the certificate authority and follow the steps in the relevant section. Be sure you have installed the [Chainguard CLI tool `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) priod to proceeding. 

## Option 1: Google Certificate Authority Service

If you are already using GCP, you can set up a CA with CA Service. 

### Step 1 — Set Up Google CA

If you don't have a certificate authority (CA) already, you'll first need to host your own for Enforce Signing to request certificates from it. We will walk through setting up a Google Certificate Authority Service. 

To set up a Google CA Service, you'll first need an instance of the GCP CA Service in your GCP Project. You can enable the CA service by running the following command. This may take a few minutes.

```sh
gcloud services enable privateca.googleapis.com
```

You'll need create a new CA Pool (alternately, you can use an existing one if you have one set up). For demonstration purposes, we'll use the `devops` tier. Replace `$POOL_NAME` with the name you would like to use for your CA Pool. Depending on your configuration, you may need to pass the location of where you want this CA Pool, with the `--location=` flag. 

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

```sh
projects/$PROJECT_ID/locations/$LOCATION/caPools/$POOL_NAME/certificateAuthorities/$ROOT_CA_NAME
```

With this set up, you're ready to set up your own instance of Chainguard Enforce Signing.

### Step 2 — Create an Enforce Signing Instance

To set up a Chainguard Enforce Signing instance, you'll be using `chainctl`. You can choose any name that is meaningful to you to reference this instance, replace the `$ENFORCE_SIGNING_NAME` variable with the name of your choosing. Also, replace the `$CA_RESOURCE_NAME` with the long resource name (discussed above) of your Google CA Service.

```sh
chainctl sigstore ca create --name=$ENFORCE_SIGNING_NAME --ca=googleca \ 
  --googleca-ref=$CA_RESOURCE_NAME 
```

Each Enforce Signing instance comes with a unique hostname for the certificate authority, which you can find by running:

```sh
chainctl sigstore ca ls 
```

You can use this command to pull up the ID and name of your CA at any time. 

## Option 2: KMS-Based Certificate Authority with GCP

To set up Enforce Signing with a KMS-based Certificate Authority on GCP, you’ll need to provide a root certificate chain and an associated KMS-based signing key. The KMS resources for GCP are expected to be prefixed with `gcpkms://`. We'll initialize that path with a the `$KMS_KEY_REF` variable.

```sh
KMS_KEY_REF=gcpkms://projects/$PROJECT_ID/locations/$KEY_LOCATION/keyRings/$KEY_RING/cryptoKeys/$KEY_NAME/versions/$KEY_VERSION
```

With this in place, you can create your very own instance of Enforce Signing with `chainctl`. You can choose any name that is meaningful to you to reference this instance, replace the `$ENFORCE_SIGNING_NAME` variable with the name of your choosing. The `$PATH_TO_CERT_CHAIN` variable should be replaced with the path to your PEM-encoded root certificate chain.

```sh
chainctl sigstore ca create --name=$ENFORCE_SIGNING_NAME --ca=kmsca \ 
  --kms-cert-chain=$PATH_TO_CERT_CHAIN --kms-key-ref=$KMS_KEY_REF
```

Each Enforce Signing instance comes with a unique hostname for the certificate authority, which you can find by running:

```sh
chainctl sigstore ca ls 
```

You can use this command to pull up the ID and name of your CA at any time. 

## Option 3: KMS-Based Certificate Authority with AWS

To set up Enforce Signing with a KMS-based Certificate Authority on AWS, you’ll need to provide a certificate chain and associated KMS-based signing key. The KMS resources for AWS are expected to be prefixed with `awskms:///` and then contain the key ARN (Amazon Resource Names). Note that three slashes are required). We'll initialize this into the `$KMS_KEY_REF` variable.

```sh
KMS_KEY_REF=awskms:///$ARN
```

With this in place, you can create your very own instance of Enforce Signing with `chainctl`. You can choose any name that is meaningful to you to reference this instance, replace the `$ENFORCE_SIGNING_NAME` variable with the name of your choosing. The `$PATH_TO_CERT_CHAIN` variable should be replaced with the path to your PEM-encoded root certificate chain.

```sh
chainctl sigstore ca create --name=$ENFORCE_SIGNING_NAME --ca=kmsca \ 
  --kms-cert-chain=$PATH_TO_CERT_CHAIN --kms-key-ref=$KMS_KEY_REF
```

Each Enforce Signing instance comes with a unique hostname for the certificate authority, which you can find by running:

```sh
chainctl sigstore ca ls 
```

You can use this command to pull up the ID and name of your CA at any time. 

## Next Steps

Now that you have a Certificate Authority, you can proceed to our tutorial on [Getting Started with Chainguard Enforce Signing](/chainguard/chainguard-enforce/chainguard-enforce-signing/getting-started-chainguard-enforce-signing/).
