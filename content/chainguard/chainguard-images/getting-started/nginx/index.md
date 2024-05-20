---
title: "Getting Started with the nginx Chainguard Image"
type: "article"
linktitle: "nginx"
description: "Tutorial on how to get started with the nginx Chainguard Image"
date: 2023-01-09T11:07:52+02:00
lastmod: 2024-05-20T14:49:27+00:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 610
toc: true
---

The nginx images maintained by Chainguard are a mix of development and production distroless images that are suitable for building and running nginx workloads.

In this guide, we'll create a demo application using nginx to serve static content to a local port on your machine. Then we will use the nginx Chainguard Image to build and execute the demo in a containerized environment.

You will need to have nginx installed on your machine to follow along.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Step 1: Setting up a Demo Application

We'll start by creating a basic nginx application to serve as a demo. This app will serve static content to a local web server. 

For this tutorial, you will be copying code to files you create locally. You can find the demo code throughout this tutorial, or you can find the complete demo at the [demo GitHub repository](https://github.com/chainguard-dev/edu-images-demos/tree/main/nginx).

With nginx installed, create a directory for your app. In this guide we'll call the directory `nginxdemo`:

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

The following HTML file displays an image of Inky, our mascot, alongside a fun octopus fact.

```HTML
<!DOCTYPE html>
<html>
<head>
<title>Chainguard NGINX Demo Application</title>
<link rel="stylesheet" href="stylesheet.css">
</head>

<body>

<h1>NGINX Demo Application</h1>

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
Chainguard Academy nginx demo application
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

Next, you will pull down the `inky.png` file using `curl`. Always [inspect the URL](https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/734e6171ee69f0e0dbac95e6ebc1759ac18bf00a/nginx/data/inky.png) before downloading it to ensure it is from a safe and trustworthy location.

```shell
curl -O https://raw.githubusercontent.com/chainguard-dev/edu-images-demos/734e6171ee69f0e0dbac95e6ebc1759ac18bf00a/nginx/data/inky.png
```

Now, return to the `nginxdemo` directory you created. Here we will create the `nginx.conf` configuration file used by nginx to run the local webserver. We will demonstrate this using `nano`.

```shell
nano nginx.conf
```

Copy the following code into the configuration file you created. In the `location` directive, be sure to update the configuration to reference the path from root to the `data` directory you created in a previous step.

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
            root /Users/username/nginxdemo/data; # Update file path accordingly
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

Copy the filepath to your `nginx.conf` file you created earlier. Replacing `<filepath>` with this copied path, execute the following command to initialize the nginx server:

```shell
nginx -c <filepath>
```

To view the HTML content, navigate to `localhost:8080` in your web browser of choice. You should see a simple landing page with a picture of Inky and a fun fact about the Wolfi octopus.

If you make any changes to the files nginx is serving, run `nginx -s reload` in your terminal to allow the changes to render. When you are finished with your application, run `nginx -s quit` to allow nginx to safely exit.



<!-- New content -->
## Step 2: Creating the Dockerfile

To make sure our final image is _distroless_ while still being able to install dependencies with Composer, our build will consist of **two** stages: first, we'll build the application using the `dev` image variant, a Wolfi-based image that includes Composer and other useful tools for development.
Then, we'll create a separate stage for the final image. The resulting image will be based on the distroless PHP Wolfi image, which means it doesn't come with Composer or even a shell.

Create a Dockerfile with:

```shell
touch Dockerfile
```

Then open this file in your code editor of choice, for example `nano`:

```shell
nano Dockerfile
```
The following Dockerfile will:

1. Start a new build stage based on the `nginx:latest` image and call it `builder`;
2. Copy files from the current directory to the `/app` location in the container;
3. Enter the `/app` directory and run `composer install` to install any dependencies;
4. Start a new build stage based on the `php:latest` image;
5. Copy the application from the `builder` stage;
6. Set up the application as entry point for this image.

Copy this content to your own `Dockerfile`:

```Dockerfile
FROM cgr.dev/chainguard/php:latest-dev AS builder
COPY . /app
RUN cd /app && \
	composer install --no-progress --no-dev --prefer-dist

FROM cgr.dev/chainguard/php:latest
COPY --from=builder /app /app

ENTRYPOINT [ "php", "/app/namegen" ]
```
Save the file when you're finished.

You can now build the image with:

```shell
docker build . -t php-namegen
```

Once the build is finished, run the image with:

```shell
docker run --rm php-namegen get
```

And you should get output similar to what you got before, with a random name combination.

```
fortuitous-octopus
```

If you inspect the image with a `docker image inspect php-namegen`, you'll notice that it has only **two** layers, thanks to the use of a multi-staging Docker build.

```shell
docker image inspect php-namegen
```
```shell
...
    	"RootFS": {
        	"Type": "layers",
        	"Layers": [
            	"sha256:23a50695d43b8aea7720c05bff1bdbfbcb45d0b0c7e7387f55d82110084002eb",
            	"sha256:9b900cbd280a3d510588c3b14bc937718ccee43a10b8b7b1756438b030bc3e15"
        	]
    	},
    	"Metadata": {
        	"LastTagTime": "2023-01-10T19:02:13.062958609+01:00"
    	}
	}
]

```
In such cases, the last `FROM` section from the Dockerfile is the one that composes the final image. That's why in our case it only adds one layer on top of the base `php:latest` image, containing the `COPY` command we use to copy the application from the build stage to the final image.

It's worth highlighting that nothing is carried from one stage to the other unless you copy it. That facilitates creating a slim final image with only what's necessary to execute the application.

## Advanced Usage

{{< blurb/images-advanced image="PHP" >}}


