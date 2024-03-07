---
title: "Getting Started with the Node Chainguard Image"
type: "article"
linktitle: "Node"
aliases: 
- /chainguard/chainguard-images/getting-started/getting-started-node
description: "Tutorial on how to get started with the Node Chainguard Image"
date: 2023-02-01T11:07:52+02:00
lastmod: 2023-09-22T11:07:52+02:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 610
toc: true
---

The [Node Chainguard Image](https://edu.chainguard.dev/chainguard/chainguard-images/reference/node/overview/) is a distroless container image that has the tooling necessary to build and execute Node applications, including  `npm`.

In this guide, we'll set up a demo application and create a Dockerfile to build and execute the demo using the Node Chainguard Image as base.

This tutorial requires Docker, Node, and Npm to be installed on your local machine.

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

We'll start by creating a small Node application to serve as a demo. This application uses a mock server to test GET and POST requests, and is based on the [Docker Node example](https://docs.docker.com/language/nodejs/build-images/).

First, create a directory for your app. In this guide we'll use `wolfi-node`:

```shell
mkdir ~/wolfi-node && cd ~/wolfi-node
```

Run the following command to create a new `package.json` file.

```shell
npm init -y
```

Exit the `init` process.  You do not need to fill out the metadata as this is a demo.

Install `npm`:

```shell
npm install
```

Next, install the application dependencies. We'll need `ronin-server` and `ronin-mocks`, which are used together to create a "mock" server that saves JSON data in memory and returns it in subsequent GET requests to the same endpoint.

```shell
npm install ronin-server ronin-mocks
```

Using your code editor of choice, create a new file named `server.js` for your application. Here we'll use `nano`:

```shell
nano server.js
```

Copy the following code to your `server.js` file:

```js
const ronin = require('ronin-server')
const mocks = require('ronin-mocks')

const server = ronin.server()

server.use('/', mocks.server(server.Router(), false, true))
server.start()
```

Save the file when you're done. Then, run the server with:

```shell
node server.js
```

This command will start the application and wait for connections on port `8000`. The mocking server will save any JSON data submitted by a POST request

From a new terminal window, run the following command, which will make a POST request to your application sending a JSON payload:

```shell
curl --request POST \
  --url http://localhost:8000/test \
  --header 'content-type: application/json' \
  --data '{"msg": "testing" }'
```

When the connection is successful, you should get output like this on the terminal that is running the application:

```shell
2023-02-07T15:48:54:2450  INFO: POST /test
```
You can now test that the content was saved by running a GET request to the same endpoint:

```shell
curl http://localhost:8000/test
```

You'll get output similar to this:

```shell
{"code":"success","meta":{"total":1,"count":1},"payload":[{"msg":"testing","id":"f427f835-3e93-43ad-91c8-d150dffba0f9","createDate":"2023-02-07T14:48:54.256Z"}]}
```

The demo application is now ready. In the next step, you'll create a Dockerfile to run your app. Before moving along, make sure to stop the server running on your terminal by typing `CTRL+C` (or `CMD+C` for macOS users).

## Step 2: Creating the Dockerfile

In your code editor of choice, create a new Dockerfile:

```shell
nano Dockerfile
```
The following Dockerfile will:

1. Start a new image based on the `cgr.dev/chainguard/node:latest` image;
2. Set the work dir to `/app` inside the container;
3. Copy application files from the current directory to the `/app` location in the container;
4. Run `npm install` to install production-only dependencies;
7. Set up additional arguments to the default entrypoint (`node`), specifying which script to run.

Copy this content to your own `Dockerfile`:

```Dockerfile
FROM cgr.dev/chainguard/node
ENV NODE_ENV=production

WORKDIR /app

COPY --chown=node:node ["package.json", "package-lock.json", "server.js", "./"]

RUN npm install --omit-dev

CMD [ "server.js" ]
```
Save the file when you're finished.

You can now build the image with:

```shell
docker build . -t wolfi-node-server
```

Once the build is finished, run the image with:

```shell
docker run --rm -it -p 8000:8000 wolfi-node-server
```

And it should work the same way as before: the terminal will be blocked with the application waiting for connections on port `8000`. The difference is that this is running inside the container, so we set up a port redirect to receive requests on `localhost:8000`.

```shell
curl --request POST \
  --url http://localhost:8000/test \
  --header 'content-type: application/json' \
  --data '{"msg": "testing node wolfi image" }'
```
You can now query the same endpoint to receive the data that was stored in memory when you run the previous command:

```shell
curl http://localhost:8000/test
```
```shell
{"code":"success","meta":{"total":1,"count":1},"payload":[{"msg":"testing node wolfi image","id":"6011f987-b9f8-4442-8253-d54166df5966","createDate":"2023-02-07T15:57:23.520Z"}]}
```

## Advanced Usage

{{< blurb/images-advanced image="Node" >}}
