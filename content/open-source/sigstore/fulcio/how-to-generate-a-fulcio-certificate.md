---
title: "How to Generate a Fulcio Certificate"
linktitle: "Generate Fulcio Certificate"
type: "article"
description: "Tutorial on how to generate a certificate with Fulcio for software security"
date: 2022-08-19T08:49:31+00:00
lastmod: 2022-08-19T08:49:31+00:00
draft: false
tags: ["Fulcio", "Procedural"]
images: []
menu:
  docs:
    parent: "fulcio"
weight: 630
toc: true
---

_An earlier version of this material was published in the [Fulcio chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@2fbe6328019c4b1fbf934bd3bfb7e308/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@1f71fcbe8219471fb82e25731b18be11) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

In this tutorial, we are going to create and examine a Fulcio certificate to demonstrate how Fulcio can work in practice. To follow along, you will need Cosign installed on your local system. If you haven't installed Cosign yet, you can follow the instructions described in [How to Install Cosign](/open-source/sigstore/cosign/how-to-install-cosign/), or you can follow one of the installation methods described in the [official documentation](https://docs.sigstore.dev/cosign/system_config/installation/).

Please note that using Cosign requires Go v1.16 or higher. The Go Project provides [official download instructions](https://go.dev/doc/install).

To get started, place some text in a text file. For instance:

```sh
echo "test file contents" > test-file.txt
```

Next, let’s generate a key pair with Cosign:

```sh
cosign generate-key-pair
```

Enter and confirm a password after running this command.

Then, use Cosign to sign this test-file.txt, outputting a Fulcio certificate named “fulcio.crt.base64”. The sign-blob subcommand allows Cosign to sign a blob. This command will open a browser tab and will require you to sign in through one of the OIDC providers: GitHub, Google, or Microsoft. This step represents the user proving their identity.

```sh
cosign sign-blob test-file.txt --output-certificate fulcio.crt.base64 --output-signature fulcio.sig
```

After authentication, you can close the browser tab. In your terminal, you will receive output similar to this:

```
Using payload from: test-file.txt
Generating ephemeral keys...
Retrieving signed certificate...

	Note that there may be personally identifiable information associated with this signed artifact.
	This may include the email address associated with the account with which you authenticate.
	This information will be used for signing this artifact and will be stored in public transparency logs and cannot be removed later.

By typing 'y', you attest that you grant (or have permission to grant) and agree to have this information stored permanently in transparency logs.
Are you sure you would like to continue? [y/N] y
```

If you agree, enter `y` and continue. You will receive output like this:

Your browser will now be opened to:
https://oauth2.sigstore.dev/auth/auth?access_type=online&client_id=sigstore&code_challenge=...
Successfully verified SCT...
using ephemeral certificate:
-----BEGIN CERTIFICATE-----
(...)
-----END CERTIFICATE-----

tlog entry created with index: 2494952
Signature wrote in the file fulcio.sig
using ephemeral certificate:
-----BEGIN CERTIFICATE-----
(...)
-----END CERTIFICATE-----
Certificate wrote in the file fulcio.crt.base64
```

The output indicates that Sigstore is using ephemeral keys to generate a certificate for `test-file.txt`. The certificate, which we'll verify in the next section, is saved to a file named `fulcio.crt.base64`.
