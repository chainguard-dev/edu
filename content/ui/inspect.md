The first place we can look for information about container compliance is the clusters main page, which you can find by clicking on the [**Clusters** tab](https://console.enforce.dev/clusters) in the main navigation menu.

With our new policy, `sample-policy`, in place, information about policy compliance should be visible in the **Policy** column, next to the cluster name.

![Cluster compliance](/images/cluster-compliance.png)

You can also find more information about policy compliance by clicking on either of the cards in the cluster list page. The links on these cards will take you to views that provide more information on policies that have failed, and the exact images that are failing policies.

Additionally, the buttons on top of the cluster table will allow you to filter your clusters by compliance.

You can also check that the **sample-policy** was distributed to the cluster by using `kubectl`.

```sh
kubectl get clusterimagepolicies
```

You’ll get feedback that the **sample-policy** was distributed and how long ago.

```
NAME                AGE
sample-policy     68s
```
