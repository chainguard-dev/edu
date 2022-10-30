In order to put Chainguard Enforce into action within a cluster, we'll now create a Kubernetes cluster using kind. We will name our cluster `enforce-demo` by passing that to the `--name` flag, but you may want to use another name.

```sh
kind create cluster --name enforce-demo
```

Install the Chainguard Enforce agent in your cluster:

```sh
chainctl cluster install --group=$GROUP --private --context kind-enforce-demo
```

If you click on the [**Clusters** tab](https://console.enforce.dev/clusters) in the main navigation menu, you should now see your cluster in the cluster table.

![Cluster list](/images/cluster-list.png)

From here, you can explore a detailed view of the cluster, including any policies that apply to it.
