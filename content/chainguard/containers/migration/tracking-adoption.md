---
title: "Tracking adoption of Chainguard Containers"
linktitle: "Tracking adoption"
type: "article"
description: "How to identify Chainguard container images in your environment and measure the progress of a migration."
date: 2026-11-03T00:00:00+00:00
lastmod: 2026-11-06T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Migration", "Conceptual"]
images: []
weight: 45
toc: true
---

As with any change you roll out across an organization, a migration to Chainguard Containers is more likely to succeed if you can see how far it has progressed and whether it's having the effect you want. You can measure that effect through outcomes like fewer Common Vulnerabilities and Exposures (CVEs), better compliance, fewer security exceptions, and more productive engineers.

This article focuses on progress instead: which of your images and containers have moved to Chainguard Containers, and which are still outstanding. Knowing what's outstanding tells you which teams or applications need help and which workloads to migrate next. It's also what lets you attribute changes in your outcomes to Chainguard Containers.

## Identifying Chainguard images

There are several ways to tell whether an image is a Chainguard image, or is based on one. Each has its own trade-offs, and the right choice depends on where you are looking and what kind of images you build.

Identifying the images that aren't Chainguard images matters as much, because they're the migration work that remains. The methods differ in how well they do this: some can tell you what an image is based on, while others can only tell you that they found no evidence of a Chainguard image.

### Image reference

The simplest signal is the image reference itself. An image pulled from `cgr.dev/$ORGANIZATION`, or from your [pull-through cache or mirror](/chainguard/containers/registry/pull-through-guides/) of it, is a Chainguard image.

Image references are available almost everywhere — in manifests, in the Kubernetes API, in registry logs — so this approach is cheap to implement. It works well for application images that you run as-is, like `nginx` or `postgres`.

It doesn't work for images that are based on Chainguard images. An image built `FROM cgr.dev/$ORGANIZATION/python` and pushed to your own registry has a reference like `registry.example.com/my-app`, which tells you nothing about its base image.

Image references are better at identifying images that aren't Chainguard images. A reference to an upstream image, like `docker.io/library/nginx` or `quay.io/prometheus/prometheus`, isn't a Chainguard image, and usually tells you which Chainguard image replaces it. References to your own registry depend on how you organize it. A path that you know mirrors an upstream registry, like `registry.example.com/dockerhub/`, identifies upstream images, and a path that only holds Chainguard images identifies Chainguard ones. Images that your teams build and push, on the other hand, are unknown either way until you inspect them.

### Labels and annotations

Chainguard sets a number of [annotations](/chainguard/containers/overview/#annotations) on its images, and sets the same values as labels in the image config:

```shell
crane config cgr.dev/chainguard/python:latest | jq '.config.Labels'
```

The output includes both Chainguard's own labels and the standard OCI ones:

```json
{
  "dev.chainguard.image.title": "python",
  "dev.chainguard.package.main": "",
  "org.opencontainers.image.authors": "Chainguard Team https://www.chainguard.dev/",
  "org.opencontainers.image.created": "2026-11-03T03:08:31Z",
  "org.opencontainers.image.source": "https://github.com/chainguard-images/images/tree/main/images/python",
  "org.opencontainers.image.title": "python",
  "org.opencontainers.image.url": "https://images.chainguard.dev/directory/image/python/overview",
  "org.opencontainers.image.vendor": "Chainguard"
}
```

Docker persists labels from the base image into the images it builds, unless the Dockerfile overrides them. This means labels can identify images that are based on Chainguard images, not only the Chainguard images themselves.

It's common for builds to override the `org.opencontainers.image.*` labels with values that describe the application. For example, this Dockerfile sets its own title and vendor:

```Dockerfile
FROM cgr.dev/chainguard/python:latest
LABEL org.opencontainers.image.title=my-app org.opencontainers.image.vendor="Example Corp"
```

The resulting image keeps `dev.chainguard.image.title` but loses `org.opencontainers.image.vendor="Chainguard"`:

```json
{
  "dev.chainguard.image.title": "python",
  "dev.chainguard.package.main": "",
  "org.opencontainers.image.authors": "Chainguard Team https://www.chainguard.dev/",
  "org.opencontainers.image.created": "2026-11-03T03:08:31Z",
  "org.opencontainers.image.source": "https://github.com/chainguard-images/images/tree/main/images/python",
  "org.opencontainers.image.title": "my-app",
  "org.opencontainers.image.url": "https://images.chainguard.dev/directory/image/python/overview",
  "org.opencontainers.image.vendor": "Example Corp"
}
```

For this reason, the presence of a `dev.chainguard.*` label is a more reliable signal than the value of `org.opencontainers.image.vendor`. The labels the image inherits without overriding also describe the base image rather than your application: `org.opencontainers.image.source` and `org.opencontainers.image.url` still point to Chainguard, and `org.opencontainers.image.created` describes the base image, not your image.

Labels have some other limitations:

- Not every build tool preserves labels from the base image the way Docker does. Check the images your build tool produces before you rely on labels.
- Docker doesn't copy the base image's manifest annotations into the images it builds. Some other tools do; [`ko`](https://ko.build/), for example, copies them and also records the base image, as described in [Base image annotations and provenance](#base-image-annotations-and-provenance).
- Reading labels requires fetching the image config from the registry or from the container runtime, which is more work than reading an image reference.
- The absence of a `dev.chainguard.*` label suggests that an image isn't based on a Chainguard image, but it doesn't prove it, because a build tool may have dropped the label. Labels from other vendors may tell you what an image is based on, but there's no consistent convention that they all follow.

If you want an identifier that you control, you can add your own annotations and labels to your Chainguard images with [Custom Assembly](/chainguard/containers/custom-assembly/custom-assembly-chainctl/#adding-custom-annotations-and-environment-variables).

### OS release information

Every Chainguard image includes an `/etc/os-release` file that identifies the distribution. Images in your organization's registry identify as Chainguard OS:

```output
ID=chainguard
NAME="Chainguard"
PRETTY_NAME="Chainguard"
VERSION_ID="20230214"
HOME_URL="https://chainguard.dev/"
```

The free images in `cgr.dev/chainguard` identify as Wolfi instead:

```output
ID=wolfi
NAME="Wolfi"
PRETTY_NAME="Wolfi"
VERSION_ID="20230201"
HOME_URL="https://wolfi.dev"
BUG_REPORT_URL="https://github.com/wolfi-dev/os/issues"
```

Because `/etc/os-release` is part of the filesystem, it is present in any image built on top of a Chainguard image, and builds rarely change it. This makes it the most reliable signal that an image is based on a Chainguard image.

It's equally useful for images that aren't Chainguard images, because other distributions identify themselves the same way, with values like `ID=debian`, `ID=ubuntu`, or `ID=alpine`. As well as telling you an image still needs migrating, this tells you what it's migrating from, which helps you plan the work. Refer to the [compatibility guides](/chainguard/containers/migration/compatibility/) for the differences to expect from each distribution. Images without an `/etc/os-release` file, like those built `FROM scratch`, aren't Chainguard images either, because every Chainguard image includes one.

It's also the signal that vulnerability scanners use to decide which advisory data applies to an image. Most scanners and cloud-native application protection platforms (CNAPPs) report it as image metadata, so you may already be collecting it. For example, `trivy` reports it as the OS family:

```shell
trivy image --quiet --format json cgr.dev/$ORGANIZATION/python:latest | jq '.Metadata.OS'
```

For an image in your organization, the OS family is `chainguard`. For a public image in `cgr.dev/chainguard`, it's `wolfi`:

```json
{
  "Family": "chainguard",
  "Name": "20230214"
}
```

The drawback is that reading `/etc/os-release` requires access to the image's filesystem. That means pulling and unpacking the image, or, for a running container, privileged access to the host it runs on.

An image can also have a Chainguard `/etc/os-release` without being based on a Chainguard image, for instance if you build it from Wolfi packages with [apko](/open-source/build-tools/apko/getting-started-with-apko/). Whether you count those images as adoption is up to you.

### Signatures

Chainguard signs every image it publishes. You can verify that an image was published by Chainguard with `cosign`:

```shell
cosign verify cgr.dev/chainguard/nginx:latest \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main
```

Images in your organization are signed by different identities. Refer to [Chainguard's signing identities](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/#chainguards-signing-identities) for details.

A signature is the strongest proof that an image came from Chainguard, but on its own it's a limited signal for tracking adoption. Only the images that Chainguard publishes are signed by Chainguard, so Chainguard's signatures can't identify images that are based on Chainguard images. Verification also requires access to the signatures, which your mirror may not copy.

To use signatures to identify images based on Chainguard images, you need to sign those images yourself. Your build system would verify the signature on the Chainguard base image, build your image on top of it, then sign an attestation that records the base image it used. Verifying that attestation tells you an image is based on a Chainguard image, but only as far as you trust the system that signed it, so the signing identity must belong to a build system that you control and that engineers can't bypass.

For the same reason, a missing Chainguard signature doesn't mean an image isn't based on a Chainguard image. If you sign every image you build, though, an image without your attestation tells you something useful: it was built outside your trusted build system, or it's a third-party image.

Signatures are primarily used for [enforcement](/chainguard/containers/security-and-compliance/enforcement/). The [policy engine example](#policy-engines-in-audit-mode) later in this article uses them to measure adoption before you enforce anything.

### Base image annotations and provenance

Some build tools record the base image directly. `ko` sets the `org.opencontainers.image.base.name` and `org.opencontainers.image.base.digest` annotations on the images it builds:

```json
{
  "org.opencontainers.image.base.digest": "sha256:8f9c7533c7709270342660bca209e5fc593483c27f95283e1082424c1e0da967",
  "org.opencontainers.image.base.name": "cgr.dev/chainguard/static:latest"
}
```

Docker doesn't set these annotations by default, but BuildKit can generate a [SLSA provenance attestation](https://docs.docker.com/build/metadata/attestations/slsa-provenance/) with `docker buildx build --provenance=true`. The attestation lists the base image and its digest among the build's materials, such as `pkg:docker/cgr.dev/chainguard/python@latest-dev`.

Both answer the question of what an image is based on, for Chainguard and non-Chainguard images alike, as long as the tools that build your images produce them. Provenance attestations are also the starting point for the signed attestations described in [Signatures](#signatures).

## Where to measure adoption

You can collect the signals described earlier at several points in the lifecycle of an image. Each one gives you a different view of adoption, and many organizations measure more than one.

### Source code

Your Dockerfiles, Kubernetes manifests, Helm values, and CI pipeline definitions describe the images you intend to build and run. Searching them for `cgr.dev` or your mirror's hostname tells you which applications have been migrated, and searching for other base images tells you which haven't. Code search in GitHub or GitLab is often enough to get started.

Source code is where the migration work actually happens, so it maps closely to the tasks that remain. It's also the earliest point you can measure.

[`chainctl images discover`](#chainctl-images-discover) and [Guardener](#guardener) can search your repositories for you, and report the Chainguard image that replaces each reference they find.

However, the source doesn't tell you what is running. An application may have been migrated in its main branch but not yet deployed, or may still run from an old release. Image references in source code may also be templated or indirect, like `FROM ${BASE_IMAGE}`, which makes them hard to search for.

### CI/CD

Your build pipelines produce the images you deploy, so they're a good place to inspect each image after it's built. You can read its labels with `crane config`, or its OS release information with a scanner, and record the result alongside the build. If you already scan your images for vulnerabilities in CI, the OS family is likely part of the output you're storing.

This approach covers every image you build, regardless of whether it ends up deployed, and it catches images based on Chainguard images that you wouldn't find by searching for `cgr.dev`. It doesn't cover third-party images that you deploy without building them.

### Registry

Pull volume from `cgr.dev`, compared with pull volume from other upstream registries, gives you a broad, organization-wide view of adoption over time.

If you route pulls through a [pull-through cache](/chainguard/containers/registry/pull-through-guides/), you can count pulls by upstream from its logs or metrics. You can also subscribe to [pull events](/platform/administration/cloudevents/events-reference/) from the Chainguard registry, which include the repository, tag, digest, and user agent of each pull. A single `docker pull` produces several events, because the client checks the manifest with a `HEAD` request and fetches each layer as a blob, so count only `GET` requests for manifests. Even then, pulling a multi-architecture image fetches two manifests: the index, and the image manifest for the client's platform.

Treat pull counts as directional rather than precise. Rebuilds and redeployments inflate them, while caches and mirrors collapse many pulls into one. Registry pulls also can't identify images based on Chainguard images that are stored in your own registry, unless you can inspect those images.

### Runtime

What is actually running in your environment is usually the measure that matters most. It's what your security team reports on, and it's where the benefits of Chainguard Containers are realized.

Runtime measurement depends on the platform you run on. Kubernetes clusters expose image references and metadata through their API, which most of the [tools in this article](#tools-for-measuring-adoption) build on. For other platforms, like Amazon ECS or fleets of virtual machines, your CNAPP or observability platform is often the most practical source of data.

## Choosing what to count

The same signals can produce quite different numbers depending on what you count. Before you report on adoption, make sure the metric reflects the progress you care about.

Containers are not a good measure of migration work. A Deployment with 100 replicas contributes 100 times as many containers as a StatefulSet with one, but they're likely to take a similar amount of effort to migrate. Similarly, a sidecar injected by a service mesh may account for half the containers in a cluster, while being only one image to migrate. Counting the objects that define your workloads — Deployments, StatefulSets, DaemonSets, ECS task definitions — is a better measure of progress. The Kyverno example later in this article counts workload objects for this reason.

Distinct images are another good measure. The number of distinct images changes less often than the number of running containers, and each one usually corresponds to a single Dockerfile, or to a single Chainguard image to migrate to.

It's also useful to break adoption down by environment, by the team or business unit that owns the workload, by language ecosystem, and by whether an image is used directly or as a base image. This shows you where to focus your migration effort.

## Tools for measuring adoption

Guardener and `chainctl images discover` work on your source code. Scanners and CNAPPs cover running containers, and often your registries and CI too. The remaining tools run in your Kubernetes clusters and report on what's deployed there.

### Guardener

If your code is on GitHub, [Guardener](/chainguard/guardener/github/) scans your repositories for image references continuously, and can [suggest](/chainguard/guardener/github/image-suggestions/) or [migrate to](/chainguard/guardener/github/image-migration/) Chainguard images for the references it finds.

The migration pull requests that Guardener opens give you a measure of the work left to do. You can list the open ones across your GitHub organization with the GitHub CLI:

```shell
gh search prs --owner $GITHUB_ORG --author app/chainguard --state open \
  --match title "Migrate container images to Chainguard equivalents" \
  --json repository,url --limit 1000
```

### `chainctl images discover`

[`chainctl images discover`](/chainguard/containers/migration/migration-tools/images-discover/) reads the image references in a directory, such as a repository checkout, and reports the Chainguard image that replaces each one. For example, in a repository where a Dockerfile uses `cgr.dev/my-org/python:3.13` and a Compose file uses `postgres:17`, run the command from the repository's root:

```shell
chainctl images discover
```

The output lists each reference with its Chainguard replacement and a status, where `my-org` stands for your organization:

```output
--------------|----------------------------|---------------------------------|------------------
 FILE         | CURRENT IMAGE              | CHAINGUARD IMAGE                | STATUS
--------------|----------------------------|---------------------------------|------------------
 Dockerfile   | cgr.dev/my-org/python:3.13 | -                               | on chainguard
--------------|----------------------------|---------------------------------|------------------
 compose.yaml | postgres:17                | cgr.dev/my-org/postgres:17      | entitled
              |                            | cgr.dev/my-org/postgres-fips:17 | available to add
--------------|----------------------------|---------------------------------|------------------
```

The Python image is `on chainguard`, so it's already migrated. `postgres` is an upstream image with a replacement that your organization can pull today, so it's `entitled`. A reference with no Chainguard replacement is `not available`. Counting references by status tells you how many have been migrated, how many are ready to migrate, and how many have no replacement. To count them in a script, pass `-o json`, which reports each status as `already-chainguard`, `entitled`, `available`, or `no-match`.

References to Chainguard images through a mirror, like `registry.example.com/cgr/python`, are reported with a replacement rather than as `on chainguard`. If you use a mirror, count those references separately by matching on its hostname.

### Scanners and CNAPPs

Platforms like Wiz, Prisma Cloud, and Datadog scan running containers and collect metadata about them, including the information in `/etc/os-release` and image labels. If you use one of these platforms, it's likely the quickest route to an adoption metric, because it's already deployed across your clusters and clouds, and it places adoption data next to your CVE data.

The trade-off is that they're not built to report on adoption specifically, so you may need to build a custom query or dashboard to get the view you want.

### Trivy Operator

The [Trivy Operator](https://github.com/aquasecurity/trivy-operator) scans the workloads in a Kubernetes cluster and stores the results as `VulnerabilityReport` resources, which include the OS family of each image. You can configure [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) to export that field as a Prometheus metric, and then calculate the percentage of reports that identify as Chainguard or Wolfi:

```promql
100
  * sum(trivy_operator_vulnerability_report_info{os_family=~"chainguard|wolfi"})
  / sum(trivy_operator_vulnerability_report_info)
```

The metric name comes from the kube-state-metrics configuration in the [`trivy-operator-adoption-metrics`](https://github.com/chainguard-demo/cookbook/tree/main/trivy-operator-adoption-metrics) example in the Chainguard cookbook, which describes the full setup and includes a Grafana dashboard. The Trivy Operator creates a report for each object it scans, and those objects don't map one-to-one to the workloads you define, so treat this as a count of reports rather than of workloads.

### kube-state-metrics

If you already run kube-state-metrics in your Kubernetes clusters, its `kube_pod_container_info` metric includes the image reference of every container in the `image_spec` label. That's enough to measure adoption by image reference without deploying anything else. For example, this query returns the percentage of distinct images that are pulled from `cgr.dev` or from a mirror at `registry.example.com/cgr`:

```promql
100
  * count(count by (image_spec) (kube_pod_container_info{image_spec=~"(cgr\\.dev|registry\\.example\\.com/cgr)/.+"}))
  / count(count by (image_spec) (kube_pod_container_info))
```

Like any approach based on image references, this doesn't count images that are based on Chainguard images.

### OpenTelemetry for Java services

If you instrument your Java services with the [OpenTelemetry Java agent](https://opentelemetry.io/docs/zero-code/java/agent/), the agent reports the vendor of the JVM it runs in as part of the `process.runtime.description` resource attribute. In Prometheus, this appears as a label on the `target_info` metric. A service running on the public Chainguard `jdk` image reports the following:

```output
process_runtime_description="wolfi OpenJDK 64-Bit Server VM 27.0.1.0.3+-wolfi-r1"
process_runtime_name="OpenJDK Runtime Environment"
process_runtime_version="27.0.1.0.3+-wolfi-r1"
```

Other JDK builds report their own vendor, like `Eclipse Adoptium`. This query returns the percentage of instrumented Java services running on a Chainguard JVM:

```promql
100
  * count(count by (service_name) (target_info{telemetry_sdk_language="java", process_runtime_description=~"(?i).*(wolfi|chainguard).*"}))
  / count(count by (service_name) (target_info{telemetry_sdk_language="java"}))
```

This query assumes that Prometheus scrapes the agent's own Prometheus exporter, which adds `service_name` to `target_info`. If your metrics reach Prometheus through OTLP or the OpenTelemetry Collector, the service name usually becomes the `job` label instead, so group by `job`.

This identifies the JVM, not the image. It counts images based on Chainguard images, because they inherit the JVM, but it doesn't count a service that installs a non-Chainguard JDK on top of a Chainguard image. It also only covers services that run the agent. The `os.description` attribute describes the host's kernel, not the container's distribution, so it can't identify Chainguard images.

### Policy engines in audit mode

Admission controllers like [Kyverno](/chainguard/containers/security-and-compliance/enforcement/kyverno/), [OPA Gatekeeper](/chainguard/containers/security-and-compliance/enforcement/opa-gatekeeper/), and [Kubewarden](https://www.kubewarden.io/) are usually used to enforce policy, but in audit mode they record violations without blocking anything. A policy that requires Chainguard images, run in audit mode, gives you a list of the workloads that haven't been migrated yet. Once that list is short enough, you can switch the policy to enforce.

For example, this Kyverno policy audits every container image in the cluster, and passes an image if it's signed by one of your organization's Chainguard [signing identities](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/#chainguards-signing-identities) or by the key your build system uses to sign images it builds on Chainguard images:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-trusted-signature
spec:
  webhookConfiguration:
    timeoutSeconds: 30
  rules:
    - name: require-trusted-signature
      match:
        any:
          - resources:
              kinds:
                - Pod
      verifyImages:
        - imageReferences:
            - "*"
          failureAction: Audit
          mutateDigest: false
          verifyDigest: false
          attestors:
            - count: 1
              entries:
                - keyless:
                    subjectRegExp: "^https://issuer.enforce.dev/(<image-syncer-id>|<custom-image-builder-id>)$"
                    issuer: "https://issuer.enforce.dev"
                    rekor:
                      url: https://rekor.sigstore.dev
                - keys:
                    publicKeys: |-
                      -----BEGIN PUBLIC KEY-----
                      ...
                      -----END PUBLIC KEY-----
```

If you pull Chainguard images through a mirror, the mirror must copy their signatures, or the policy reports those images as untrusted.

Kyverno records the results in `PolicyReport` resources. This command counts the Deployments, StatefulSets, DaemonSets, and CronJobs in the cluster, and how many of them use only images from a trusted signer:

```shell
kubectl get policyreport -A -o json | jq '[.items[] | select(.scope.kind | IN("Deployment", "StatefulSet", "DaemonSet", "CronJob")) | .results[]? | select(.policy == "require-trusted-signature") | .result] | {total: length, trusted: map(select(. == "pass")) | length}'
```

The command returns totals like these:

```json
{
  "total": 12,
  "trusted": 2
}
```

In this example, two of the 12 workloads use only trusted images, so the other 10 still need to be migrated.

### Container Image Exporter

The [Container Image Exporter](https://github.com/chainguard-sandbox/container-image-exporter) is a Prometheus exporter that reports metadata about the images in a Kubernetes cluster. It's an experimental project, maintained on a best-effort basis.

It has two components, which you can deploy independently:

- The cluster exporter watches workloads in the Kubernetes API, including Deployments, StatefulSets, CronJobs, and Tekton, Knative, and Argo resources, and fetches the labels and annotations of their images from the registry.
- The node exporter runs as a DaemonSet and reads `/etc/os-release` from each running container through the container runtime. It requires root access to the host.

For example, using the cluster exporter, this query returns the percentage of the containers defined in workload objects, rather than Pods, whose image has Chainguard labels:

```promql
100
  * count(
      container_image_cluster_container_info{kind!="Pod"}
        * on (digest) group_left
          count by (digest) (
              container_image_cluster_label{key="dev.chainguard.image.title"}
            or container_image_cluster_label{key="dev.chainguard.package.main"}
            or container_image_cluster_label{key="org.opencontainers.image.vendor", value="Chainguard"}
          )
    )
  / count(container_image_cluster_container_info{kind!="Pod"})
```

Refer to the project's documentation for installation instructions, the full list of metrics, and its Grafana dashboards.

## Learn more

If you'd like help measuring adoption in your environment, contact your Chainguard account team.

For more on the topics in this article, refer to the following resources:

- [Chainguard Containers overview](/chainguard/containers/overview/#annotations), which describes the annotations Chainguard sets on its images
- [Policy enforcement](/chainguard/containers/security-and-compliance/enforcement/) with Kyverno and OPA Gatekeeper
- [Migration best practices and checklist](/chainguard/containers/migration/migration-checklist/)
