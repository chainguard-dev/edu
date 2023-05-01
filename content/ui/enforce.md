At this point, let’s enforce this policy requirement. We can use `kubectl` and the `namespace` label selectors to do this.

```sh
kubectl label ns default policy.sigstore.dev/include=true --overwrite
```

We can check that our policy is enforced by trying to run an unsigned image. We’ll use an unsigned Ubuntu image as an example.

```sh
kubectl run not-signed --image=ubuntu
```

You’ll receive output that this attempt at running an unsigned image has been rejected.

```
Error from server (BadRequest): admission webhook "enforcer.chainguard.dev" denied the request: validation failed: failed policy: sample-policy
```

Congratulations, you have completed onboarding to Chainguard Enforce!

If you would like, you can now clean up your work by uninstalling `chainctl` and then deleting the cluster.

```sh
chainctl cluster uninstall
```

```sh
kind delete cluster --name enforce-demo
```

To get up and running with Chainguard Enforce, you may want to review the following docs and resources:

- [Overview of IAM model](https://edu.chainguard.dev/chainguard/chainguard-enforce/iam-groups/overview-of-enforce-iam-model/)
- [How to manage IAM groups in Chainguard Enforce](https://edu.chainguard.dev/chainguard/chainguard-enforce/iam-groups/how-to-manage-iam-groups-in-chainguard-enforce/)
- [Example policies to use with Chainguard Enforce](https://edu.chainguard.dev/chainguard/chainguard-enforce/policies/chainguard-enforce-policy-examples/)
- [`chainctl` reference](https://edu.chainguard.dev/chainguard/chainctl/) to effective use our CLI tool to interact with the account model that Chainguard Enforce provides, and enable you to make queries into the state of your clusters and policies registered with the platform

Please review more of our [documentation on Chainguard Enforce](https://edu.chainguard.dev/chainguard/chainguard-enforce/) and other resources on [Chainguard Academy](https://edu.chainguard.dev) to learn more about software supply chain security.
