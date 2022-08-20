---
title: "How to Generate a Fulcio Certificate"
type: "article"
description: "Tutorial on how to generate a certificate with Fulcio for software security"
date: 2022-19-08T08:49:31+00:00
lastmod: 2022-19-08T08:49:31+00:00
draft: false
images: []
menu:
  docs:
    parent: "fulcio"
weight: 630
toc: true
---

_An earlier version of this material was published in the [Fulcio chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@2fbe6328019c4b1fbf934bd3bfb7e308/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@1f71fcbe8219471fb82e25731b18be11) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

In this tutorial, we are going to create and examine a Fulcio certificate to demonstrate how Fulcio can work in practice. To follow along, you will need Cosign installed on your local system. If you haven't installed Cosign yet, you can follow the instructions described in [How to Install Cosign](../../cosign/how-to-install-cosign), or you can follow one of the installation methods described in the [official documentation](https://docs.sigstore.dev/cosign/installation/).

To get started, set the `COSIGN_EXPERIMENTAL` variable to `1`. This is required in order to enable the keyless signing flow functionality, which is currently in beta.

```sh
export COSIGN_EXPERIMENTAL=1
```

Next, place some text in a text file. For instance:

```sh
echo "test file contents" > test-file.txt
```

Next, let’s generate a key pair with Cosign. Enter a password twice after running the command below. For users that have not yet installed Cosign, Cosign installation instructions are here. Using Cosign requires Go v1.16 or higher. Go provides official download instructions.

Then use Cosign to sign this test-file.txt, outputting a Fulcio certificate named “fulcio.crt.base64”. The sign-blob subcommand allows Cosign to sign a blob. This command will open a browser tab and will require you to sign in through one of the OIDC providers: GitHub, Google, or Microsoft. This step represents the user proving their identity.

```sh
cosign sign-blob test-file.txt --output-certificate fulcio.crt.base64 --output-signature fulcio.sig
```

After authentication, you can close the browser tab. In your terminal, you should see output similar to this:

```
Using payload from: test-file.txt
Generating ephemeral keys...
Retrieving signed certificate...
Your browser will now be opened to:
https://oauth2.sigstore.dev/auth/auth?access_type=online&client_id=sigstore&code_challenge=...
Successfully verified SCT...
using ephemeral certificate:
-----BEGIN CERTIFICATE-----
(...)
-----END CERTIFICATE-----

tlog entry created with index: 2494952
Signature wrote in the file fulcio.sig
Certificate wrote in the file fulcio.crt.base64
```

The output indicates that Sigstore is using ephemeral keys to generate a certificate for `test-file.txt`. The certificate, which we'll verify in the next section, is saved to a file named `fulcio.crt.base64`.
