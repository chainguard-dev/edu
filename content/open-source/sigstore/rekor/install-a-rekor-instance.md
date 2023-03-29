---
title: "How to Set Up An Instance of Rekor Instance Locally"
type: "article"
lead: "Make your own transparency log instance"
description: "Create your own instance of the Rekor transparency log"
date: 2022-20-087T08:49:31+00:00
lastmod: 2022-24-08T08:49:31+00:00
draft: false
tags: ["Rekor", "Procedural"]
images: []
menu:
  docs:
    parent: "rekor"
weight: 005
toc: true
---

_An earlier version of this material was published in the [Rekor chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@e785fae1be184e2c929db62dbe7444fa/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@a48c33126e2c4ee6ad3bfa6b7bc9c957) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

While individual developers may not generally need to set up their own instance of Rekor, it may be worthwhile to set up your own local instance in order to further understand how Rekor works under the hood. We will have multiple terminal sessions running to set up the Rekor server. You may want to use a tool such as [tmux](https://github.com/tmux/tmux/wiki) to keep terminal sessions running in the background within the same window. 

## Create and run a database backend

To start, we’ll need to create a database backend; while Sigstore accepts several different databases, we’ll work with MariaDB here, so make sure you have it installed. 

If you are on Debian or Ubuntu, you can install it with the following command.

```sh
sudo apt install -y mariadb-server
```

If you are on macOS, you can install it with Homebrew. If you don’t already have Homebrew installed, visit [brew.sh](https://brew.sh) to set it up.

```sh
brew install mariadb
```

If you’re using another operating system, review the [official MariaDB installation documentation](https://cloud.google.com/blog/products/open-source/supporting-the-python-ecosystem).

With MariaDB installed, start the database. 

For Debian or Ubuntu, you can run:

```sh
sudo mysql_secure_installation
```

For macOS, you can run:

```sh
brew services start mariadb && sudo mysql_secure_installation
```

Once you run the above command, you will be prompted to enter your system password, and then will receive a number of prompts as terminal output. You can answer “no” or `N` to the first question on changing the root password, and “yes” or `Y` to the remaining prompts. 

```
Switch to unix_socket authentication [Y/n] n
…
Change the root password? [Y/n] n
…
Remove anonymous users? [Y/n] Y
…
Disallow root login remotely? [Y/n] Y
…
Remove test database and access to it? [Y/n] Y
…
Thanks for using MariaDB!
```

Once you receive the `Thanks for using MariaDB!` output, you’re ready to create your database. We’ll create a directory to store our work in this example, feel free to create a directory or move into a directory that is meaningful for you. 

```sh
mkdir lf-sigstore && cd $_
```

From this directory, we’ll clone the Rekor GitHub repository.

```sh
git clone https://github.com/sigstore/rekor.git
```

Now, move into the directory of Rekor where the database creation script is held.

```sh
cd $HOME/lf-sigstore/rekor/scripts
```

From here, you can run the database creation script.

```sh
sudo sh -x createdb.sh
```

You should receive output that indicates that the test database and user were created.

```
+ DB=test
+ USER=test
+ PASS=zaphod
+ ROOTPASS=
+ echo -e 'Creating test database and test user account'
-e Creating test database and test user account
+ mysql
+ echo -e 'Loading table data..'
-e Loading table data..
+ mysql -u test -pzaphod -D test
```

At this point, we are ready to move onto installing Trillian. 

## Install and set up Trillian

Trillian offers a transparent, append-only, and cryptographically verifiable data store. Trillian will store its records in the MariaDB database we just created. We can install Trillian with Go.

```sh
go install github.com/google/trillian/cmd/trillian_log_server@latest
go install github.com/google/trillian/cmd/trillian_log_signer@latest
go install github.com/google/trillian/cmd/createtree@latest
```

We’ll start the Trillian log server, providing the API used by Rekor and the Certificate Transparency frontend. 

```sh
$(go env GOPATH)/bin/trillian_log_server --logtostderr \
  -http_endpoint=localhost:8090 -rpc_endpoint=localhost:8091
```

Your output will indicate that the server has started, and the session will hang.

```
I0629 18:11:27.222341    7395 quota_provider.go:46] Using MySQL QuotaManager
I0629 18:11:27.222847    7395 main.go:141]          HTTP server starting on localhost:8090
I0629 18:11:27.222851    7395 main.go:180]          RPC server starting on localhost:8091
I0629 18:11:27.223757    7395 main.go:188]          Deleted tree GC started
```

Next, let’s start the log signer in a new terminal session (while keeping the previous session running), which will sequence data into cryptographically verifiable Merkle trees and periodically check the database.

```sh
$(go env GOPATH)/bin/trillian_log_signer --logtostderr --force_master --http_endpoint=localhost:8190 -rpc_endpoint=localhost:8191
```

You’ll receive output that indicates that the log signer has started. This session will also hang.

```
I0629 18:13:42.226319    8513 main.go:98] **** Log Signer Starting ****
W0629 18:13:42.227281    8513 main.go:129] **** Acting as master for all logs ****
…
```

The Trillian system can support multiple independent Merkle trees. We’ll have Trillian send a request to create a tree and save the log ID for future use. Run the following command in a third terminal session (while keeping the previous two sessions running). 

```sh
$(go env GOPATH)/bin/createtree --admin_server localhost:8091 \
  | tee $HOME/lf-sigstore/trillian.log_id
```

In the Trillian log server terminal, you should have output similar to the following:

```
Acting as master for 2 / 2 active logs: master for: <log-2703303398771250657> <log-5836066877012007666>
```

This log string will match the string output of the new terminal session. Trillian uses the gRPC API for requests, which is an open source Remote Procedure Call (RPC) framework that can run in any environment. We can now move onto the Rekor server.

## Install and set up Redis

Rekor server also requires a Redis instance. If you are on Debian or Ubuntu, you can install it with the following command.

```sh
sudo apt install -y redis-server
```

If you are on macOS, you can install it with Homebrew. If you don’t already have Homebrew installed, visit [brew.sh](https://brew.sh) to set it up.

```sh
brew install redis
```

If you’re using another operating system, review the [official Redis documentation](https://redis.io/docs/getting-started/).

With Redis installed, start it. 

For Debian or Ubuntu, you can run:

```sh
sudo systemctl start redis-server
```

For macOS, you can run:

```sh
brew services start redis
```

Now you can proceed to the next step, where you will install the Rekor server itself.

## Install Rekor server

Rekor provides a restful API-based server with a transparency log that allows for validating and storing. Let’s move into the main `rekor/` directory we set up.

```sh
cd $HOME/lf-sigstore/rekor
```

Now we’ll install the Rekor server from source with Go.

```sh
go install ./cmd/rekor-cli ./cmd/rekor-server
```

You can now start the Rekor server with Trillian and can leave this running.

```sh
$(go env GOPATH)/bin/rekor-server serve --trillian_log_server.port=8091 \
  --enable_retrieve_api=false
```

Next, we’ll ensure that Rekor is working correctly.

## Test Rekor 

Let’s upload a test artifact to Rekor. Open another terminal session and ensure that you are in your main Rekor directory.

```sh
cd $HOME/lf-sigstore/rekor
```

Now, let’s upload a test artifact to our Rekor instance.

```sh
$(go env GOPATH)/bin/rekor-cli upload --artifact tests/test_file.txt \
  --public-key tests/test_public_key.key \
  --signature tests/test_file.sig \
  --rekor_server http://localhost:3000
```

Your terminal will output that you have created a log entry, and where it’s available. Note that your string will be different than what is indicated below. You can input the URL in a browser of your choice to inspect the resulting JSON. 

Created entry at index 0, available at: http://localhost:3000/api/v1/log/entries/d2f305428d7c222d7b77f56453dd4b6e6851752ecacc78e5992779c8f9b61dd9

Next, we’ll upload the key to our Rekor instance and attach it to the container we built in the Cosign chapter. If you have not created a key or the container, you can do so now, or alternately use a key and software artifact of your choice. 

```sh
$HOME/go/bin/cosign sign \
  --key $HOME/cosign.key \
  --rekor-url=http://localhost:3000 \
  docker-username/hello-container
```

Now you can verify the container against both the mutable OCI attestation and the immutable Rekor record. If you signed your container using Gmail account with Google as the OIDC issuer, you can verify the image with the following command: 

```sh
$HOME/go/bin/cosign verify \
  --key $HOME/cosign.pub \
  --rekor-url=http://localhost:3000 \
  --certificate-identity username@gmail.com \
  --certificate-oidc-issuer https://accounts.google.com \
  docker-username/hello-container
```

If everything goes well, your resulting output after running the above command should be similar to this:

```
Verification for index.docker.io/docker-username/hello-container:latest --
The following checks were performed on each of these signatures:
- The cosign claims were validated
- The claims were present in the transparency log
- The signatures were integrated into the transparency log when the certificate was valid
- The signatures were verified against the specified public key
- Any certificates were verified against the Fulcio roots.
[{"critical":{"identity":{"docker-reference":"index.docker.io/docker-username/hello-container"},"image":{"docker-manifest-digest":"sha256:35b25714b56211d548b97a858a1485b254228fe9889607246e96ed03ed77017d"},"type":"cosign container image signature"},"optional":{"Bundle":{"SignedEntryTimestamp":"MEUCIG...yoIY=","Payload":{"body":"...","integratedTime":1643917737,"logIndex":1,"logID":"4d2e4...97291"}}}}]
```

You can now also review the logs of your Rekor server, which will give you a URL on your localhost for this second log entry (at log entry 1). Once you are done with your Rekor instance, it is safe to exit each of the terminal sessions. 

Congratulations, you have set up your own Rekor server!