---
title: "How to Sign and Upload Metadata to Rekor"
type: "article"
lead: "Use Rekor CLI to make an entry to the Sigstore transparency log"
description: "Use the Rekor CLI to sign and upload metadata to the Sigstore transparency log"
date: 2022-20-087T08:49:31+00:00
lastmod: 2022-24-08T08:49:31+00:00
draft: false
images: []
menu:
  docs:
    parent: "rekor"
weight: 630
toc: true
---

_An earlier version of this material was published in the [Rekor chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@e785fae1be184e2c929db62dbe7444fa/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@a48c33126e2c4ee6ad3bfa6b7bc9c957) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

This tutorial will walk you through signing and uploading metadata to the Rekor transparency log, which is a project of Sigstore. In order to follow along, you'll need the `rekor-cli` installed, which you can accomplish by following the "[How to Install the Rekor CLI](../how-to-install-rekor)" tutorial.

We will use SSH to sign a text document. SSH is often used to communicate securely over an unsecured network and can also be used to generate public and private keys appropriate for signing an artifact.

First, generate a key pair. This command will generate a public key and a private key file. You'll be able to easily identify the public key because it uses  the .pub extension. The command below will create a new file in ~/.ssh called id_ed25519 but you may want to call it something else; you can do that by passing a different filename after the -f flag.

```sh
ssh-keygen -t ed25519 -f id_ed25519
```

Then, create a text file called README.txt with your favorite text editor. You can enter as little or as much text in that file as you would like.

For example, we can use nano:

```sh
nano README.txt
```

Then within the file, we can type some text into it, such as the following.

```
[label README.txt]

Hello, Rekor!
```

Save and close the file. 

Next, sign this file with the following command. This command produces a signature file ending in the .sig extension.

```sh
ssh-keygen -Y sign -n file -f id_ed25519 README.txt
```

You should receive the following output.

```
Signing file README.txt
Write signature to README.txt.sig
```

Then, upload this artifact to the public instance of the Rekor log.

```sh
rekor-cli upload --artifact README.txt --signature README.txt.sig --pki-format=ssh --public-key=id_ed25519.pub
```

The returned value will include a string similar to:

https://rekor.sigstore.dev/api/v1/log/entries/83140d699ebc33dc84b702d2f95b209dc71f47a3dce5cce19a197a401852ee97

Save the UUID returned after using this command. In this example, the UUID is `83140d699ebc33dc84b702d2f95b209dc71f47a3dce5cce19a197a401852ee97`.

Now you can query Rekor for your recently saved entry. Run the following command, replacing UUID with the UUID number obtained in the previous command. 

```sh
rekor-cli get --uuid UUID
```

Once you receive output formatted as a JSON with details on the signature, you will know you have successfully stored a signed metadata entry in Rekor.
