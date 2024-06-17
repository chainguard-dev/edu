---
title: "Getting Started with the nginx Chainguard Image"
type: "article"
linktitle: "nginx"
description: "Tutorial on how to get started with the nginx Chainguard Image"
date: 2023-01-09T11:07:52+02:00
lastmod: 2024-06-17T18:32:10+00:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 610
toc: true
---

The nginx images maintained by Chainguard include development and production distroless images that are suitable for building and running nginx workloads. Images tagged with `:latest-dev` include additional packages to facilitate project development and testing. Images tagged with `:latest` strip back these extra packages to provide a secure, production-ready container image.

In this tutorial, we will create a local demo website using nginx to serve static HTML content to a local port on your machine. Then we will use the nginx Chainguard Image to build and execute the demo in a lightweight containerized environment.

You will need to have [nginx](https://nginx.org/en/download.html) and [Docker Engine](https://docs.docker.com/engine/install/) installed on your machine to follow along.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Step 1: Setting up a Demo Website 

We'll start by serving static content to a local web server with nginx.

For this tutorial, you will be copying code to files you create locally. You can find the demo code throughout this tutorial, or you can find the complete demo at the [demo GitHub repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/nginx).

With nginx installed, create a directory for your demo. In this guide we'll call the directory `nginxdemo`:

```shell
mkdir ~/nginxdemo/ && cd $_
```

Within this directory, we will create a `data` directory to contain our content to be hosted by the web server.

```shell
mkdir data && cd $_
```

Using a text editor of your choice, create a new file `index.html` for the HTML content that will be served. We will use `nano` as an example.

```shell
nano index.html
```

The following HTML file displays an image of Inky alongside a fun octopus fact.

```HTML
<!DOCTYPE html>
<html>
<head>
<title>Chainguard nginx Demo Website</title>
<link rel="stylesheet" href="stylesheet.css">
</head>

<body>

<h1>nginx Demo Website</h1>

<h2>from the <a href="https://edu.chainguard.dev/" target="_blank">Chainguard Academy</a></h2>

<img src="inky.png" class="corners" width="250px">

<i><h3>Did you know?</h3></i>
<p>The Wolfi octopus is the world's smallest octopus, weighing in on average at less than a gram!</p>
<p>They are found near the coastlines of the west Pacific Ocean.</p>

</body>

</html>
```

Copy this code to your `index.html` file, save, and close it.

Next, create a CSS file named `stylesheet.css` using the text editor of your choice. We'll use `nano` to demonstrate.

```shell
nano stylesheet.css
```

Copy the following code to your `stylesheet.css` file. 

```CSS
/*
Chainguard Academy nginx Demo Website
*/

body {
    text-align: center;
    background-color: #fcebfc;
    font-family: Arial, sans-serif;
}

h1 {
    color: #df45e6;
}

h2, h3 {
    color: #9745e6;
}

p {
    color: #583ce8
}

.corners {
    border-radius: 10px;
}

```

After copying the code into the `stylesheet.css` file, save and close it.

Next, you will pull down the `inky.png` file using `curl`. Always [inspect the URL](https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/734e6171ee69f0e0dbac95e6ebc1759ac18bf00a/nginx/data/inky.png) before downloading it to ensure it comes from a safe and trustworthy location.

```shell
curl -O https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/734e6171ee69f0e0dbac95e6ebc1759ac18bf00a/nginx/data/inky.png
```

Now, return to the `nginxdemo` directory you made earlier. 

```shell
cd ../
```

Here we will create the `nginx.conf` configuration file used by nginx to run the local web server. We will demonstrate this using `nano`.

```shell
nano nginx.conf
```

Copy the following code into the configuration file you created. In the `location` directive, be sure to update the configuration to reference the path from root to the `data` directory you created in a previous step. The file path which you are not using should be commented out using the `#` symbol to prevent syntax errors.

```nginx
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;

    keepalive_timeout  65;

    server {

        listen 8080;
        server_name localhost;
        charset koi8-r;

        location / {
            root /Users/username/nginxdemo/data; # Update the file path for your system
            #root /home/username/nginxdemo/data; # Linux file path example

        }

    }

    include servers/*;

}
```

Once you are finished editing the configuration file, save and close it.

Create a new file named `mime.types` using a text editor of your choice. We will use `nano` to demonstrate.

```shell
nano mime.types
```

Copy and paste the following code into your `mime.types` file. This file will allow nginx to handle the HTML, CSS, and png files we created when rendering the webserver. 

```nginx
types {
    text/html                                        html htm shtml;
    text/css                                         css;
    image/png                                        png;
}
```

Save and close the `mime.types` file when you are finished editing it.

Next, copy the absolute filepath to the `nginx.conf` file you created earlier. Replacing the example path with this copied path, execute the following command to initialize the nginx server:

```shell
nginx -c /Users/username/nginxdemo/nginx.conf
```

Please note that you may encounter some permissions errors when executing this command. You will need to update the permissions of the default nginx logging directory on some systems to proceed. For example, nginx installed with Homebrew stores its log files at `/opt/homebrew/var/log/nginx/`, while on a Linux machine, the logs are stored in `/var/log/nginx/`. To update the permissions of these directories, execute the following command, replacing `username` with your local username and updating the log file path if need be.

```shell
chmod +wx /opt/homebrew/var/log/nginx/
```

With the directory permissions updated, you should now be able to initialize the nginx server.

To view the HTML content, navigate to `localhost:8080` in your web browser of choice. You will see a simple landing page with a picture of Inky and a fun fact about the Wolfi octopus.

If you make any changes to the files nginx is serving, run `nginx -s reload` in your terminal to allow the changes to render. When you are finished with your website, run `nginx -s quit` to allow nginx to safely shut down.

## Step 2: Creating the Dockerfile

We will now use a Dockerfile to build an image containing the demo. 

In the `nginxdemo` directory, create the `Dockerfile` with the text editor of your choice. We will use `nano`:

```shell
nano Dockerfile
```
The following Dockerfile will:

1. Start a new build based on the `cgr.dev/chainguard/nginx:latest` image;
2. Note which container port we need to expose for nginx to listen on;
3. Copy the HTML content from the data directory into the image.

Copy this content to your own `Dockerfile`:

```Dockerfile
FROM cgr.dev/chainguard/nginx:latest

EXPOSE 8080

COPY data /usr/share/nginx/html/
```
Save the file when you're finished.

You can now build the image with:

```shell
docker build . -t nginx-demo
```

Once the build is complete, run the image with:

```shell
docker run -d --name nginxcontainer -p 8080:8080 nginx-demo
```

The `-d` flag configures our container to run as a background process. The `--name` flag will name our container `nginxcontainer`, making it easy to identify from other containers. The `-p` flag publishes the port that the container listens on to a port on your local machine. This allows us to navigate to `localhost:8080` in a web browser of our choice to view the HTML content served by the container. You should see the same HTML page as before, with Inky and an octopus fun fact.

If you wish to publish to a different port on your machine, such as `1313`, you can do so by altering the command-line argument as shown:

```shell
docker run -d --name nginxcontainer -p 1313:8080 nginx-demo
```

When you are done with your container, you can stop it with the following command:

```shell
docker container stop nginxcontainer
```

## Advanced Usage

In this demo, we did not copy the configuration file into the image built from the Dockerfile. This is because the default configuration file in the image was sufficient for the scope of this demo. If you wish to use a custom configuration file, you must ensure that file paths, ports, and other system-specific settings are configured to match the container environment. You can find more information about making these changes at the [Chainguard nginx Image Overview](/chainguard/chainguard-images/reference/nginx/image_specs/).

{{< blurb/images-advanced image="nginx" >}}

