So far, the information we have been seeing about our cluster concerns the containers and images running in the cluster's control plane.

Now, let’s deploy a new image, starting with a generic NGINX image.

```sh
kubectl create deployment nginx --image=nginx
```

Give this a few seconds to populate and then check what’s running again by navigating to the cluster's detail page. You can do this by clicking on the cluster's name from the cluster list table.

In the **Policy violations** table, the image will be listed.

![Image with violations](/images/problem-nginx.png)

Clicking on the **Show diagnostic** button in the table will provide more information about the violation.

Next, let’s pull in an image that has an SBOM and signature. This is an NGINX image from Chainguard.

```sh
kubectl create deployment good-nginx --image=ghcr.io/chainguard-dev/nginx-image-demo
```

This image won't be listed in the violations table, but you can navigate to the **Images** table to retrieve it.

![Image without violations](/images/good-nginx.png)

This image passes the policy because it has both an SBOM and a signature.
