You can create a policy directly from the UI by navigating to the [**Policies** tab](https://console.enforce.dev/policies). In the policy table menu, there will be a **Create policy** button. Clicking this button will open a dropdown menu, which will allow you to create a policy from scratch or use a predefined template.

For now, we can create a policy using the [**Custom** option from the dropdown](https://console.enforce.dev/policies/create/custom).

![Create policy](/images/create-policy.png)

On the policy create page, ensure that the correct group is displayed in the group field: `enforce-demo`. Then paste the following code into the code editor:

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: sample-policy
spec:
  images:
  - glob: "ghcr.io/chainguard-dev/*/*"
  - glob: "ghcr.io/chainguard-dev/*"
  - glob: "index.docker.io/*"
  - glob: "index.docker.io/*/*"
  - glob: "cgr.dev/chainguard/**"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
```

This policy creates a cluster image policy with the Sigstore beta API, and with Fulcio as a keyless authority. Here, we are requiring that all images from container registries be signed.

After you click the **Publish** button at the bottom of the modal, your new policy will be active. The next time you land on the policy list page, you will see the policy listed, as well as any violations it has and its group hierarchy.

You can also list your policies with `chainctl`.

```sh
chainctl policies ls
```

Depending on the policies your group has in place, you may see a few policies listed in the output, along with the policy you just created.
