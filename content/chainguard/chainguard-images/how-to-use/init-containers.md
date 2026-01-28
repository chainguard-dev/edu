---
title: "Using Init Containers with Chainguard Containers"
linktitle: "Using Init Containers"
lead: ""
description: "Example showing how to use an init container to configure Chainguard's minimal nginx container image."
type: "article"
date: 2025-08-04T15:21:01+00:00
lastmod: 2025-08-04T15:21:01+00:00
draft: false
tags: ["Chainguard Containers", "Overview", "Procedural"]
images: []
menu:
  docs:
    parent: "how-to-use"
weight: 110
toc: true
---

Chainguard Containers are designed with minimalism and security in mind. By including fewer packages and tools, Chainguard Containers have a smaller attack surface than their counterparts. However, there are cases where the external counterparts have certain desirable features, like useful startup scripts or configuration defaults.

There are several ways to customize Chainguard Containers. For example, you can use [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/) to add packages to an otherwise minimal Chainguard container image. Changing a Chainguard container image's configuration — such as updating its entrypoint or adding startup scripts — requires a different strategy. One method for doing so in Kubernetes deployments is to use *init containers*. 

This guide provides a brief overview of what init containers are as well as their benefits. It then outlines an example of how you can build an init container and use it to reconfigure Chainguard's nginx container image.

## Prerequisites

In order to follow this guide, you will need the following:

* Docker, which you will use to create an image to be used by an init container, installed on your local machine. Refer to the [Docker documentation](https://docs.docker.com/engine/install/) to set this up.
* A container registry you can push the init container image to. This guide assumes you have access to a [Docker Hub registry](https://hub.docker.com/), though the example can be adjusted for other registries.
* Access to a Kubernetes cluster. This could be a cluster that you run locally with a tool like [minikube](https://minikube.sigs.k8s.io/docs/) or [kind](https://kind.sigs.k8s.io/), or a cloud-hosted cluster such as [Amazon EKS](https://aws.amazon.com/eks/) or [Google GKE](https://cloud.google.com/kubernetes-engine).


## Benefits of Init Containers 

Init containers are specialized containers that run before application containers within a Kubernetes pod. Init containers are temporary: they run and complete their given tasks before the main application container starts, and then immediately exit.

Init containers are useful for preparing the application environment, since they allow you to create configuration files or modify settings before your app starts. They can be used to set up prerequisites for the application, such as database migrations or environment variable configurations.

You can also use init containers to create directories, set file permissions, install dependencies, or populate data stores with initial data. In some cases, they can retrieve secrets and place them in a shared volume for the application.

Put together, this allows you to separate initialization logic from your app code, making both more manageable. Init containers can also run in sequence, so you can control the order of operations. If one init container fails, Kubernetes will restart the pod and run the init containers again until they succeed. 


## Configuring Chainguard's `nginx` Container with an Init Container

Say your organization uses an nginx container to host an application. You've typically used the [default nginx container image from Docker Hub](https://hub.docker.com/_/nginx) for this purpose.

This image runs startup scripts inside the `/docker-entrypoint.d` directory of the image. Although this allows for flexibility, it introduces various security risks:

* **Arbitrary Code Execution**: If anyone (whether through build scripts, other layers, mounted volumes) adds or modifies a script file within `/docker-entrypoint.d`, it will get executed automatically on container startup.
* **Unintended Script Execution**: If you accidentally include a shell script (or malicious one gets included through CI/CD or shared build layers), it will be executed, regardless of its purpose or trustworthiness.
* **Privilege Escalation**: If the container runs as root (which is common in base images), any `*.sh` script executed at startup runs with full privileges. Malicious scripts can add users, exfiltrate secrets, overwrite configs, etc.

Rather than exposing yourself to such risks, you can instead run the default nginx image from Docker Hub as an init container, which you'll then use to reconfigure Chainguard's more minimal and secure nginx container image. This involves running the startup configuration in the init container, mounting the resulting configuration to a shared volume, and thereby decoupling the `docker-entrypoint.sh` script from the core nginx image. This avoids introducing the aforementioned security risks into the minimal Chainguard nginx container image.

This section illustrates how to set up an nginx init container based on the default nginx container from Docker Hub and then run it inside a Kubernetes deployment to reconfigure a Chainguard nginx container image. This example involves creating a sample `nginx.conf` file, building an init container with `docker`, and deploying it in a Kubernetes pod.


### Creating a sample `nginx.conf` file

To get started, run the following command to create an `nginx.conf` file:

```shell
cat > nginx.conf <<EOF
worker_processes  1;
pid /tmp/nginx.pid;

events {
    worker_connections  1024;
}

http {
    default_type  application/octet-stream;

    server {
        listen 80;
        server_name localhost;

        location / {
            return 200 "Hello from minimal NGINX!\n";
            add_header Content-Type text/plain;
        }
    }
}
EOF
```

This `nginx.conf` file configures a minimal nginx web server. It configures nginx to listen on port `80` and returns a custom response (`Hello from minimal NGINX!`) for any HTTP request. 

After creating this `nginx.conf` file, continue by using `docker` to create a container image that will be used for an init container.

### Creating an init container image

Run the following command to create a Dockerfile. You will use this Dockerfile to build an init container image:

```shell
cat > Dockerfile.init <<EOF
FROM nginx

COPY nginx.conf /custom/nginx.conf

CMD cp /custom/nginx.conf /etc/nginx/nginx.conf && \
   chmod 644 /etc/nginx/* && \
   /docker-entrypoint.sh true
EOF
```

This Dockerfile builds an image using the default nginx container image from Docker Hub (`FROM nginx`). This image includes `docker-entrypoint.d` and `docker-entrpoint.sh` by default. It will copy the `nginx.conf` file you created previously into the new image when you build it. Then, when you run the container in a Kubernetes deployment, it will prepare and copy the nginx configuration at startup using the entrypoint script.

After creating this Dockerfile, build the image. 

Recall from the Prerequisites section that this guide assumes you have a Docker Hub registry. The following examples expect you to have an environment variable with the namespace on Docker Hub to which you will push images. This could be your username or your organization's name. For example, if you log in to Docker Hub and navigate to your list of repositories, the URL in your browser will have an address like `hub.docker.com/repositories/EXAMPLE`. In this case, `EXAMPLE` would be your Docker Hub namespace.

Create an environment variable to hold your Docker Hub namespace:

```shell
export NAMESPACE=<your-dockerhub-name>
```

> **Note**: If you aren't using Docker Hub as your container registry, you will need to include the host name of your registry in this variable. Docker defaults to Docker Hub (`docker.io`) if this is omitted.

After creating this environment variable, build the init container image:

```shell
docker build -f Dockerfile.init -t $NAMESPACE/nginx-init .
```

Next, push the init container image to your registry so you can reference it from your Kubernetes deployment:

```shell
docker push $NAMESPACE/nginx-init
```

Once you have built and pushed this init image to your registry it is now available to be run inside pipelines where you have your `nginx.conf` available for shared mounting and configuration in the init step.

### Setting up a Kubernetes configuration

Since you are building the entrypoint logic into the init container image itself, the Kubernetes deployment YAML for your init container would follow a similar structure to this:

```yaml
initContainers:
  - name: run-entrypoint
    image: $NAMESPACE/nginx-init
    volumeMounts:
      - name: nginx-config
        mountPath: /etc/nginx
```

This instructs the init container to execute the startup scripts for the nginx configuration in the `docker-entrypoint.d` directory. In your main nginx configuration for the deployment, it would follow a structure similar to this:

```yaml
containers:
  - name: nginx
    image: cgr.dev/chainguard/nginx:latest
    ports:
      - containerPort: 80
    volumeMounts:
      - name: nginx-config
        mountPath: /etc/nginx
```

Because your nginx container would mount the configurations from the shared volumeMount nginx-config in this case, you would now avoid having to run startup steps outside of the init. 

The following command creates a deployment manifest named `init-deployment.yaml` that performs these steps using the init container image you created earlier:

```shell
cat > init-deployment.yaml <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-chainguard
spec:
 replicas: 1
 selector:
   matchLabels:
     app: nginx-chainguard
 template:
   metadata:
     labels:
       app: nginx-chainguard
   spec:
     volumes:
       - name: nginx-config
         emptyDir: {}

     initContainers:
       - name: run-entrypoint
         image: $NAMESPACE/nginx-init
         volumeMounts:
           - name: nginx-config
             mountPath: /etc/nginx

     containers:
       - name: nginx
         image: cgr.dev/chainguard/nginx:latest
         ports:
           - containerPort: 80
         volumeMounts:
           - name: nginx-config
             mountPath: /etc/nginx
EOF
```

### Testing the example deployment

Using the manifest you just created, create a Kubernetes deployment:

```shell
kubectl create -f init-deployment.yaml
```

If you retrieve information about your Kubernetes pod immediately after deployment, you will find the init pod initializing:

```shell
kubectl get pods
```
```
NAME                               READY   STATUS     RESTARTS   AGE
nginx-chainguard-d49d7496c-stxcj   0/1     Init:0/1   0          6s
```

If you do so again shortly after, you will find the init container has completed and the application is running:

```output
NAME                               READY   STATUS    RESTARTS   AGE
nginx-chainguard-d49d7496c-stxcj   1/1     Running   0          55s
```

Once the workload is running, you can test whether nginx is working as expected. To do so, first forward your local machine's port `8080` to port `80` within the pod:

```shell
kubectl port-forward deploy/nginx-chainguard 8080:80
```
```
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
```

Then, **in a separate terminal window**, use `curl` to reach the pod:

```shell
curl http://localhost:8080
```
```
Hello from minimal NGINX!
```

This confirms that the workload is indeed running and nginx is working as expected.

Note that this example copies over only an `nginx.conf` file, but you can use this strategy to set up other nginx configurations. For example, you could also copy a `mime.types` file over to the Chainguard nginx container image.



## Learn More

Init Containers provide a powerful, flexible mechanism to set up application environments and help with migration challenges associated with nginx images. By providing a fresh environment without requiring modifications to existing app containers, init containers can streamline the setup process for migrating to Chainguard images and enhance compatibility with existing workflows.

This tutorial is centered around Chainguard's nginx container image, but the concepts outlined here are applicable when migrating to other Chainguard Containers as well. We have a number of resources available on migrating to Chainguard Containers, and we encourage you to get started with our [Overview of Migrating to Chainguard Containers](/chainguard/migration/migrations-overview/). For more information on working with Chainguard's nginx container image, check out our guide on [Getting Started with nginx](/chainguard/chainguard-images/getting-started/nginx/).
