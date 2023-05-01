This walkthrough will quickly get Chainguard Enforce installed and running locally — from setting up an example cluster, to drafting a policy and observing how it behaves, to improving the policy, and finally enforcing that policy. If you'd like more information on working with Chainguard Enforce, we encourage you to to check out the [detailed tutorial on Chainguard Academy](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-user-onboarding/).

Before running Chainguard Enforce locally, you’ll need to ensure you have the following installed:

- **curl** — to retrieve files from the web, follow the relevant [curl download docs](https://curl.se/download.html) for your machine.
- **Docker** — you’ll need [Docker installed](https://docs.docker.com/get-docker/) and running in order to step through this tutorial.
- **kind** — to create a kind Kubernetes cluster on our laptop, you can download and install kind for your relevant operating system by following the [kind install docs](https://kind.sigs.k8s.io/docs/user/quick-start/#installation).
- **kubectl** — to work with your kind cluster, you can install for your operating system by following the official [Kubernetes kubectl documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).
- For macOS users, you'll need to update to bash version 4 or higher, which is not preinstalled in the machine. Please [follow our guide](https://edu.chainguard.dev/open-source/update-bash-macos/) on how to update your version if you are getting version 3 or below when you run `bash --version`.
