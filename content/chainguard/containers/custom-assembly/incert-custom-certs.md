---
title: "How to use incert to create container images with built-in custom certificates"
linktitle: "Custom certs with incert"
aliases:
- /chainguard/chainguard-images/working-with-images/incert-custom-certs/
- /chainguard/chainguard-images/features/incert-custom-certs/
- /chainguard/containers/working-with-images/incert-custom-certs/
- /chainguard/containers/features/incert-custom-certs/
type: "article"
description: "An overview of how to use incert — a Go program from Chainguard — to create container images with custom certificates built-in to them."
date: 2023-07-03T11:07:52+02:00
lastmod: 2026-11-23T12:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "working-with-images"
weight: 70
toc: true
---

> NOTE: If you are looking for a way to add certificates to existing Chainguard images, check out our doc on [adding custom certificates with Custom Assembly](/chainguard/containers/custom-assembly/custom-assembly-certs/).

In many enterprise settings, an organization will have its own certificate authority which it uses to issue certificates for its internal services. This is often for security or control reasons but could also be related to regulatory requirements.

If you're using a container that needs to communicate with your organization's services and your organization has its own certificate authority, you'll need to add a valid certificate into your container. One way to do this is to mount the certificate as a [volume](https://docs.docker.com/storage/volumes/) at runtime. This works, but it means that everyone who uses the container has to go through the process of mounting the certificate.

Another solution is to build the certificate directly into the container. This tutorial outlines how to use [`incert`](https://github.com/chainguard-dev/incert) — a Go tool from Chainguard that builds container images with certificates inserted into them.

## Prerequisites

To follow along with this tutorial, you will need to have the following tools installed.

* `incert`, a Go program that appends CA certificates to Docker images and pushes the modified image to a specified registry. You can install this by following [the instructions](https://github.com/chainguard-dev/incert#installation) listed in the project's GitHub repository.
* Docker, the open-source containerization platform. Set this up by following [the platform-specific instructions](https://docs.docker.com/get-docker/) on the project's website.
* A tool for creating a self-signed certificate. This guide highlights using `cfssl`, a public key infrastructure toolkit from CloudFlare, but alternatives like `openssl` could also be used for this purpose. Follow [the `cfssl` installation instructions](https://github.com/cloudflare/cfssl#installation) to set this up.
    * Note that if you use `cfssl`, you will also need the `cfssljson` utility installed as well.

## Creating a self-signed certificate

First, let's create a directory to hold your certificate infrastructure.

```sh
mkdir ~/incert-example/ && cd $_
```

In the new directory, create a certificate signing request (CSR) by running the following command.

```sh
cat > csr.json <<EOF
{
 "hosts": [
     "example.com",
     "www.example.com"
 ],
 "CN": "www.example.com",
 "key": {
     "algo": "rsa",
     "size": 2048
 },
 "names": [{
     "C": "US",
     "L": "San Francisco",
     "O": "Example Company, LLC",
     "OU": "Operations",
     "ST": "California"
 }]
}
EOF
```

We want to create some certificates for `example.com` and `www.example.com`, so we include these here in a list for the CSR's `hosts` value. This means the certificates will only be valid for these domains.

Next, create your certificates by running the following `cfssl selfsign` command.

```sh
cfssl selfsign www.example.com csr.json | cfssljson -bare selfsigned
```

Here we include the hostname we specified previously (`www.example.com`) as well as the CSR file. We then pipe the command's output into a `cfssljson` command; this will process the `.json` files output by the `cfssl selfsign` command into the `.pem` files we need.

This command will return a warning that self-signed certificates are insecure. This is the expected behavior for `cfssl`, and since we are only using these certificates to demonstrate how `incert` works there won't be any security concerns.

```output
. . .

*** WARNING ***

Self-signed certificates are dangerous. Use this self-signed
certificate at your own risk.

It is strongly recommended that these certificates NOT be used
in production.

*** WARNING ***
```

Following that, if you check the contents of your working directory you will find the self-signed CSR, the key, and the certificate.

```sh
ls
```

```output
csr.json  selfsigned.csr  selfsigned-key.pem  selfsigned.pem
```

With these files in place you can move on to creating an nginx container that uses these certificates to provide TLS.

## Create an nginx container that uses self-signed certificates for TLS

Now that you've created the certificate infrastructure, you can create an nginx container that uses them to provide TLS. Later on, we will attempt to reach this nginx container with a `curl` container we built using `incert`, testing that `incert` correctly installed the `selfsigned.pem` certificate into it.

First run the following command to create an nginx configuration file named `nginx.default.conf`. This example is a fairly barebones configuration but will be adequate for the purposes of this guide. Note that it specifies the server should listen on port `8443` and will serve requests for `example.com` and `www.example.com`. It also specifies the location of the certificate and key to be used by the container, namely the `/etc/nginx/conf.d/` directory.

```sh
cat > nginx.default.conf <<EOF
server {
 listen    8443 ssl;
 server_name  example.com www.example.com;
 ssl_certificate /etc/nginx/conf.d/cert.pem;
 ssl_certificate_key /etc/nginx/conf.d/key.pem;
 location / {
     root   /usr/share/nginx/html;
     index  index.html index.htm;
 }
 error_page   500 502 503 504  /50x.html;
 location = /50x.html {
     root   /usr/share/nginx/html;
 }
}
EOF
```

The Chainguard nginx image runs as a non-root user, but `cfssljson` saves `selfsigned-key.pem` so that only your user can read it. If nginx can't read the key, the container exits as soon as it starts. Make the key readable by all users:

```sh
chmod 644 selfsigned-key.pem
```

This key exists only for this tutorial. Don't loosen the permissions on a private key that you use for anything else.

Then run the following command to create the nginx container. This command uses Chainguard's public nginx image and mounts the `cert.pem`, `key.pem`, and `nginx.default.conf` files we've created into the `/etc/nginx/conf.d` directory within the container. It also includes the `-p` option, allowing you to forward requests on your host's port `8443` to the container's port `8443`.

```sh
docker run -p 8443:8443 -d \
-v ./nginx.default.conf:/etc/nginx/conf.d/nginx.default.conf \
-v ./selfsigned.pem:/etc/nginx/conf.d/cert.pem \
-v ./selfsigned-key.pem:/etc/nginx/conf.d/key.pem \
cgr.dev/chainguard/nginx
```

## Test connections to the nginx service with `curl`

At this point, if you use `curl` to access the running nginx container, the command fails. `curl` checks the server's certificate by default, and this certificate is self-signed and issued for `www.example.com`, not `localhost`:

```sh
curl https://localhost:8443
```

```output
curl: (60) SSL: no alternative certificate subject name matches target hostname 'localhost'
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.
```

Depending on your version of `curl`, the error might name the self-signed certificate instead of the hostname.

You can force `curl` to skip these certificate checks by passing it the `-k` argument, as in `curl -k https://localhost:8443`. However, our goal is to connect to the service securely using the certificate infrastructure created previously.

In the next section we will use `incert` to create a new container image (using Chainguard's `curl` image as the foundation) with your `selfsigned.pem` certificate built into it. Before doing this, though, let's attempt to reach the nginx service with a `curl` container that does not have the certificate included.

To do this you'll need to find the nginx container's IP address. First, find the name of the container with `docker ps`.

```sh
docker ps
```

```output
CONTAINER ID   IMAGE                      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
9e211033635b   cgr.dev/chainguard/nginx   "/usr/sbin/nginx -c …"   2 minutes ago   Up 2 minutes   0.0.0.0:8443->8443/tcp, :::8443->8443/tcp   agitated_jones
```

As this output shows, the name of the nginx container in this example is `agitated_jones`. Replace this with the name of your own container in the following command:

```sh
docker inspect --format '{{ range .NetworkSettings.Networks }}{{ .IPAddress }}{{ end }}' agitated_jones
```

This will return the container's IP address:

```output
172.17.0.2
```

Next, use Chainguard's `curl` image to attempt to reach the container. Be sure to replace `172.17.0.2` with your nginx container's actual IP address, if different.

```sh
docker run -it --add-host example.com:172.17.0.2 cgr.dev/chainguard/curl:latest-dev https://example.com:8443
```

> **Note**: You might have noticed that [example.com](https://example.com) is a real website. Instead of using the `curl` container to reach the actual `example.com`, this command includes the `--add-host` option to map the hostname `example.com` to the local IP address currently being used by the nginx container.

However, the public Chainguard `curl` image doesn't have the certificate inside it, so this command will fail.

```output
curl: (60) rustls_connection_process_new_packets: invalid peer certificate: UnknownIssuer
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
```

The next step is to create an image that has our self-signed certificate built into it. For that, we'll use `incert`.

## Using `incert` to insert a custom certificate into an image

`incert` is a Go program from Chainguard that appends CA certificates to Docker images and pushes the modified image to a specified registry. This tool is still in active development, so feedback is welcome.

Run the following command to build a new image using Chainguard's `curl` image as its base and insert the `selfsigned.pem` certificate into it.

```sh
IMAGE="lockers.cgruser.dev/$(uuidgen | tr 'A-F' 'a-f')/curl-with-cert:1h"
incert -ca-certs-file selfsigned.pem -platform linux/arm64 -image-url cgr.dev/chainguard/curl:latest -dest-image-url "$IMAGE"
```

This command uses the `-ca-certs-file` option to specify that `incert` should use the `selfisgned.pem` certificate file and the `-platform` option to specify that it wants to build an image for `linux/arm64`. Be aware that you should change the value passed to the `-platform` argument to reflect that of the host platform. It also includes the `-image-url` option to specify the image we want to build on as our base image (here we specify Chainguard's `curl` image) and the `-dest-image-url` to pass the registry where we want the resulting image to be uploaded to.

For this final option, this example specifies [Chainguard Lockers](/chainguard/containers/registry/temporary-registry/) (`lockers.cgruser.dev`), a free, anonymous registry for temporary images. The first line of the command stores a destination with a random repository name in the `IMAGE` variable, and the `1h` tag means the tag stops working after one hour. Lockers doesn't require a login, which makes it useful for testing. However, Lockers is experimental and not meant for production, so don't push production images to it. It's also public, so be sure that you **do not** upload any important private certificates there.

This command will take a few moments to complete, but once it finishes you will receive output showing the image that was created and uploaded to the destination repo.

```output
lockers.cgruser.dev/7586706b-686c-4c28-97da-7c6bcb4d8486/curl-with-cert:1h@sha256:cc52dbbbc43333713ed95140b1cab12ca68e8170f2a75a7d1e9ea238b4fd2f0f
```

Following that, you can re-execute the `docker run` command from the previous section, but replace the standard Chainguard `curl` image with the image you just built. Replace `[[IP_ADDRESS]]` with your nginx container's IP address:

```sh
docker run -it --add-host example.com:[[IP_ADDRESS]] "$IMAGE" https://example.com:8443
```

This time, the `curl` container is able to reach the running nginx container.

```output
. . .
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

This shows that `incert` built the certificate into the `curl` container as expected and it was able to reach the nginx container.

## Learn more

If you'd like to learn more about how you can use Chainguard Containers effectively, we encourage you to check out all of our resources on [Working with Chainguard Containers](/chainguard/containers/using-and-deploying/). Additionally, our [Recommended practices](/chainguard/containers/security-and-compliance/) resources can be useful for ensuring the security of your container images.
