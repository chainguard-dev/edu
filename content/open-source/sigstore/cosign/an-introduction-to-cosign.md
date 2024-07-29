---
title: "An Introduction to Cosign"
type: "article"
lead: "A primer to signing software artifacts with Cosign"
description: "Understanding Cosign, a project under Sigstore"
date: 2022-19-07T08:49:31+00:00
lastmod: 2024-07-29T15:12:18+00:00
draft: false
tags: ["Cosign", "Overview"]
images: []
menu:
  docs:
    parent: "cosign"
weight: 001
toc: true
---

_An earlier version of this material was published in the [Cosign chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@204b98f35bca48c194d1868e0356bef1/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@2f0ad9cb8f124a39ab555ac8bf1a114c) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Cosign supports software artifact signing, verification, and storage in an OCI (Open Container Initiative) registry. While Cosign was developed with containers and container-related artifacts in mind, it can also be used for open source software packages and other file types. Cosign can therefore be used to sign blobs (binary large objects), files like READMEs, SBOMs (software bills of materials), Kubernetes Helm Charts, Tekton bundles (an OCI artifact containing Tekton CI/CD resources like tasks), and more. 

By signing software, you can authenticate that you are who you say you are, which can in turn enable a trust root so that developers and consumers who leverage your software can verify that you created the software artifact that you have said you’ve created. They can also ensure that the artifact was not tampered with by a third party. As someone who may use software libraries, containers, or other artifacts as part of your development lifecycle, a signed artifact can give you greater assurance that the code or container you are incorporating is from a trusted source.  

## Code Signing with Cosign

Software artifacts are distributed widely, can be incorporated into the software of other individuals and organizations, and are often updated throughout their life spans. End users and developers who build upon existing software are increasingly aware of the possibility of threats and vulnerabilities in packages, containers, and other artifacts. How can users and developers decide whether to use software created by others? One answer that has been increasingly gaining traction is *code signing*.

While code signing is not new technology, the growing prevalence of software in our everyday lives coupled with a rising number of attacks like [SolarWinds](https://www.businessinsider.com/solarwinds-hack-explained-government-agencies-cyber-security-2020-12) and [Codecov](https://www.reuters.com/technology/codecov-hackers-breached-hundreds-restricted-customer-sites-sources-2021-04-19/) has created a more pressing need for solutions that build trust, prevent forgery and tampering, and ultimately lead to a more secure software supply chain. Similar in concept to a signature on a document that was signed in the presence of a notary or other professional who can certify your identity, a signature on a software artifact attests that you are who you say you are and that the code was not altered after signing. Instead of a recognized notary when you sign software, it is a recognized **certificate authority** (CA) that validates your identity. These checks that go through recognized bodies able to establish a developer’s identity support the root of trust that security relies on so that bad actors cannot compromise software.

Code signing involves a developer, software publisher, or entity (like an automated workload) digitally signing a software artifact to confirm their identity and ensure that the artifact was not tampered with since having been signed. Code signing has several implementations, and Cosign is one such implementation, but all code signing technology follows a similar process as Cosign. 

The recommended practice for a developer (or organization) looking to sign their code with Cosign is to use *keyless signing*. This process will first generate an ephemeral key pair which will then be used to create a digital signature for a given software artifact. A **key pair** is a combination of a signing key to sign data, and a verification key that is used to verify data signed with the corresponding signing key. With the `cosign sign` command, the developer will sign their software artifact, and that signature will be stored in the registry (if applicable). This signature can later be verified by others through searching for an artifact, finding its signature, and then verifying it. 

## Keyless Signing

Code signing is a solution for many use cases related to attestation and verification with the goal of a more secure software supply chain. While key pairs are a technology standard that have a long history in technology (SSH keys, for instance), they create their own challenges for developers and engineering teams. The contents of a public key are very opaque; humans cannot readily discern who the owner of a given key is. Traditional public key infrastructure, or PKI, has done the work to create, manage, and distribute public-key encryption and digital certificates. A new form of PKI is keyless signing, which prevents the challenges of long-lived and opaque signing keys. 

In keyless signing, short-lived certificates are generated and linked into the chain of trust through completing an identity challenge that confirms the identity of the signer. Because these keys persist only long enough for signing to take place, signature verification ensures that the certificate was valid at the time of signing. Policy enforcement is supported through an encoding of the identity information onto the certificate, allowing others to verify the identity of the developer who signed.

Through offering short-lived credentials, keyless signing can support the recommended practice of operating your build environment like a production environment. This prevents the opportunity for long-lived keys to be stolen and used to sign malicious artifacts. Even if these short-lived keys used in keyless signing were stolen, they’d be useless!

While keyless signing can be used by individuals in the same manner as long-lived key pairs, it is also well suited for continuous integration and continuous deployment workloads. Keyless signing works by sending an OpenID Connect (OIDC) token to a certificate authority like [Fulcio](/open-source/sigstore/fulcio) to be signed by a workload’s authenticated OIDC identity. This allows the developer to cryptographically demonstrate that the software artifact was built by the continuous integration pipeline of a given repository, for example. 

Cosign uses ephemeral keys and certificates, gets them signed automatically by the Fulcio root certificate authority, and stores these signatures in the [Rekor](/open-source/sigstore/rekor) transparency log, which automatically provides an attestation at the time of creation. 

You can manually create a keyless signature with the following `cosign` command. In our example, we’ll use [Docker Hub](https://hub.docker.com/) to store the signature. If you would like to follow along, ensure you are logged into Docker Hub on your local machine and that you have a Docker repository with an image available. The following example assumes a username of `docker-username` and a repository name of `demo-container`. 

```sh
cosign sign docker-username/demo-container
```

You'll be taken through a workflow that requests you to grant permission to have your information stored permanently in transparency logs, and moves to a workflow with an OIDC provider.

```
Generating ephemeral keys...
Retrieving signed certificate...

	Note that there may be personally identifiable information associated with this signed artifact.
	This may include the email address associated with the account with which you authenticate.
	This information will be used for signing this artifact and will be stored in public transparency logs and cannot be removed later.

By typing 'y', you attest that you grant (or have permission to grant) and agree to have this information stored permanently in transparency logs.
Are you sure you would like to continue? [y/N] 
Your browser will now be opened to:
...
```

At this point, a browser window will open and you will be directed to a page that asks you to log in to Sigstore. You can authenticate with GitHub, Google, or Microsoft. Note that the email address that is tied to these credentials will be permanently visible in the Rekor transparency log. This makes it publicly visible that you are the one who signed the given artifact, and helps others trust the given artifact. That said, it is worth keeping this in mind when choosing your authentication method. Once you log in and are authenticated, you’ll receive feedback of “`Sigstore Auth Successful`”, and you may now safely close the window. 

On the terminal, you’ll receive output that you were successfully verified, and you’ll get confirmation that the signature was pushed. 

```
Successfully verified SCT...
tlog entry created with index: 
Pushing signature to: index.docker.io/docker-username/demo-container
```

If you followed along with Docker Hub, you can check the user interface of your repository and verify that you pushed a signature. 

You can then further verify that the keyless signature was successful by using `cosign verify` to check. You will need to know some information in order to verify the entry. You'll need to use the identity flags `--certificate-identity` which corresponds to the email address of the signer, and `--certificate-oidc-issuer` which corresponds to the OIDC provider that the signer used. For example, a Gmail account using Google as the OIDC issuer, will be able to be verified with the following command.

```sh
cosign verify \
    --certificate-identity username@gmail.com \
    --certificate-oidc-issuer https://accounts.google.com \
    docker-username/demo-container 
```

```
Verification for index.docker.io/docker-username/demo-container:latest --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - Existence of the claims in the transparency log was verified offline
  - The code-signing certificate was verified using trusted certificate authority certificates

[{"critical":{"identity":{"docker-reference":"index.docker.io/docker-username/demo-container"},"image":{"docker-manifest-digest":"sha256:e..."},"type":"cosign container image signature"},"optional":{"1.3.6.1.4.1.57264.1.1":"https://accounts.google.com","Bundle":{"SignedEntryTimestamp":"...","Payload":{"body":"eyJhcGlWZX...X19","integratedTime":...,"logIndex":...,"logID":"..."}},"Issuer":"https://accounts.google.com","Subject":"username@gmail.com"}}]
```

As part of the JSON output, you should get feedback on the issuer that you used and the email address associated with it. For example, if you used Google as your OIDC provider, you will have `"Issuer":"https://accounts.google.com","Subject":"username@gmail.com"}}]` as the last part of your output. 

## Cosign with Keys

You can also use Cosign with long-lived key pairs. If you would like to follow along, please first [install Cosign](/open-source/sigstore/cosign/how-to-install-cosign/).

```sh
cosign generate-key-pair 
```

```
Enter password for private key:
Enter again:
Private key written to cosign.key
Public key written to cosign.pub
```

You can sign a container and store the signature in the registry with the cosign sign command. 

```sh
cosign sign --key cosign.key sigstore-course/demo 
```

```
Enter password for private key:
Pushing signature to: index.docker.io/sigstore-course/demo:sha256-87ef60f558bad79beea6425a3b28989f01dd417164150ab3baab98dcbf04def8.sig
```

Finally, you can verify a software artifact against a public key with the cosign verify command. This command will return 0 if at least one Cosign formatted signature for the given artifact is found that matches the public key. Any valid formats are printed to standard output in a JSON format.

```sh
cosign verify --key cosign.pub sigstore-course/demo
```

```
The following checks were performed on these signatures:
  - The cosign claims were validated
  - The signatures were verified against the specified public key
{"Critical":{"Identity":{"docker-reference":""},"Image":{"Docker-manifest-digest":"sha256:87ef60f558bad79beea6425a3b28989f01dd417164150ab3baab98dcbf04def8"},"Type":"cosign container image signature"},"Optional":null}
```

You should now have some familiarity with the process of signing and verifying code in Cosign. For a more thorough tutorial, please review [How to Sign a Container with Cosign](/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/).

Code signing provides developers and others who release code a way to attest to their identity, and in turn, those who are consumers (whether end users or developers who incorporate existing code) can verify those signatures to ensure that the code is originating from where it is said to have originated, and check that that particular developer (or vendor) is trusted. 

