---
aliases:
- /chainguard/administration/policies/
title: "Container Pull Policies"
linktitle: "Container Pull Policies"
type: "article"
description: "Configure and enforce policies that control which Chainguard container and artifact versions your organization can pull, using chainctl"
date: 2026-05-21T08:48:45+00:00
lastmod: 2026-07-31T18:41:00+00:00
draft: false
tags: ["Overview"]
images: []
toc: true
weight: 025
---

Policies enable you to filter and restrict Chainguard artifact updates. You do this by defining policies that control and restrict versions that will be pulled from Chainguard.

## Definitions

This is how policies uses the following terms.

- **Policy** — A reusable rule that determines whether an image is allowed. Each policy has a name, a description, and the resource type it applies to. The system policies on this page apply to registry repositories.
- **Binding** — A link between a policy and an organization. While a binding exists, the policy is active for image pulls under that organization. Without a binding, the policy has no effect.
- **Mode** — A binding's mode controls what happens when the policy denies an image:
    - `ENFORCE` — Block the pull.
    - `DRY_RUN` — Allow the pull but record the violation.
- **Parameter** — A configurable value declared by a policy's schema (for example, `days` on the `cooldown` policy). Supply values when you enable a policy with `--param=KEY=VALUE` (repeatable). Omitted parameters fall back to the schema's declared default. Use `chainctl policies describe --policy=$POLICY` to see which parameters a policy accepts and what defaults apply.
- **Policy type** — Whether a policy is authored by Chainguard or by you. See [Policy types](#policy-types).

The `--mode` flag is required when you enable a policy. Chainguard recommends starting with `DRY_RUN` so you can review a policy's impact before promoting it to `ENFORCE`.

Multiple policies can be active at the same time, and they compose: an image is allowed only when *every* active policy allows it. A single policy in `ENFORCE` mode returning `DENIED` is enough to block the pull.

## Policy types

Every policy belongs to one of two types.

**System policies** are authored and maintained by Chainguard and are available to every organization. You cannot create, edit, or delete one. You choose whether to activate it and, where the policy declares parameters, what values to give it. The `no-eol`, `cooldown`, and `support-window` policies documented on this page are all system policies.

**Custom policies** are authored by you. A custom policy is a [Rego](https://www.openpolicyagent.org/docs/policy-language) expression paired with a single supported resource type and an optional parameter schema, submitted as a YAML manifest. Custom policies are visible only to the organization that owns them.

Both types are the same kind of object. They are evaluated by the same engine, activated through the same bindings, produce the same decisions, and can be waived by the same overrides. The difference is who owns the definition, and therefore what you are allowed to do to it.

Reach for a system policy when it already expresses the guardrail you want. Write a custom policy when no system policy expresses the rule you require.

Because policies compose this way, a custom policy cannot loosen a system policy. To let one specific image through, use an [override](#granting-an-exception-with-an-override) instead.

Both types appear together in `chainctl policies list`, distinguished by a type column.

To author and manage your own policies, see:

- [Writing custom policies](#writing-custom-policies) — the `allow` rule convention, the input fields a policy can read, and the Rego subset available to it.
- [Managing custom policies with chainctl](#managing-custom-policies-with-chainctl) — the manifest format and the `validate`, `create`, `update`, and `delete` subcommands.
- [Custom policies FAQ](#custom-policies-faq) — debugging denials, write-time rejections, and testing a policy before you enforce it.

## Available policies

Chainguard ships a set of system policies that are available to every organization. The list below describes each one and its configurable parameters. To confirm which policies are available to you and see their full definitions, use `chainctl policies list` and `chainctl policies describe` as shown under [Usage](#usage).

### no-eol

The `no-eol` policy denies any image whose primary package has reached its end-of-life (EOL) date. An image is allowed when it has no recorded EOL date, or when that date is still in the future. This policy takes no parameters.

```shell
chainctl policies enable --policy=no-eol --mode=DRY_RUN --parent=$ORGANIZATION
```

### cooldown

The `cooldown` policy denies images that are newer than a minimum age, measured from the image's build timestamp. Use it to hold off on adopting a version until it has been published long enough to shake out early regressions. An image is allowed once its age is greater than or equal to the configured number of days.

It accepts one parameter, `days`, an integer number of days an image must exist before it is allowed. The default is `7`, and accepted values range from `1` to `365`.

```shell
chainctl policies enable --policy=cooldown --mode=DRY_RUN --param=days=14 --parent=$ORGANIZATION
```

### support-window

The `support-window` policy requires an image's primary package to have a minimum remaining support period, measured as the span between the package's release date and its EOL date. An image is allowed when that span is greater than or equal to the configured number of months, or when the package has no recorded EOL date.

It accepts one parameter, `months`, an integer minimum number of months of support. The default is `6`, and accepted values range from `1` to `24`.

```shell
chainctl policies enable --policy=support-window --mode=DRY_RUN --param=months=12 --parent=$ORGANIZATION
```

## Usage

Policies are managed using `chainctl`. System policies are shipped with the platform; to author your own, see [Managing custom policies with chainctl](#managing-custom-policies-with-chainctl).

See which policies are available to your organization:

```shell
chainctl policies list --parent=$ORGANIZATION
```

Inspect a policy to see its full definition and configurable parameters before enabling it:

```shell
chainctl policies describe --policy=$POLICY --parent=$ORGANIZATION
```

See which policies are currently active:

```shell
chainctl policies binding list --parent=$ORGANIZATION
```

Activate a policy in `DRY_RUN` mode. This example activates the "no end-of-life" artifacts policy. Chainguard recommends that you roll out policies using `DRY_RUN` mode first and track for a time to be certain it has the impact you intend before moving to `ENFORCE`.

```shell
chainctl policies enable --policy=no-eol --mode=DRY_RUN --parent=$ORGANIZATION
```

Some policies accept parameters. Use `--param=KEY=VALUE` to supply them:

```shell
chainctl policies enable --policy=cooldown --mode=DRY_RUN --param=days=7 --parent=$ORGANIZATION
```

Promote a policy to `ENFORCE`:

```shell
chainctl policies enable --policy=no-eol --mode=ENFORCE --parent=$ORGANIZATION
```

Disable a policy:

```shell
chainctl policies disable --policy=no-eol --parent=$ORGANIZATION
```

## Checking whether an image is allowed

Before you depend on a specific image (pinning it in a deployment, promoting it through an environment, or adding it to a base image), you often want to know whether your active policies will let it through. `chainctl policies check` answers that for one image on demand, without waiting for a pull to happen.

Pass a full image reference, by tag or by digest:

```shell
chainctl policies check cgr.dev/$ORGANIZATION/python:latest
```

The reference identifies the organization and repository; a tag is resolved to its current digest, and a digest is used as-is. The image is then evaluated against every policy active for that organization, and each result is printed:

```output
  POLICY  |  MODE   | PARAMETERS | RESULT
----------|---------|------------|---------
 cooldown | DRY_RUN | days=7     | DENIED
 no-eol   | ENFORCE |            | ALLOWED
```

Read the table per policy. The image is blocked at pull time only when a policy in `ENFORCE` mode returns `DENIED`. A `DENIED` from a `DRY_RUN` policy is reported here but would not block a real pull; it is a preview of what enforcing that policy would do. If no policies apply to the image, the command says so rather than printing a table.

Because the check evaluates against the policies you have enabled right now, it reflects your current configuration, not a historical record. To review outcomes from pulls that already happened, use [policy decisions](#policy-decisions) instead.

`check` is also built for automation. Its exit status is non-zero whenever any policy returns `DENIED` or `ERROR`, regardless of that policy's mode, so you can gate a CI pipeline on it:

```shell
chainctl policies check cgr.dev/$ORGANIZATION/python@sha256:abc... || echo "image violates a policy"
```

Note that a `DRY_RUN` denial also produces a non-zero exit, so a passing `check` is stricter than what enforcement alone would block, which is useful as an early warning while you stage policies.

## Policy decisions

Every time an image is pulled and evaluated against an active policy, the platform records the outcome as a *decision*. A decision is the result of evaluating a single image digest against a single policy at pull time. It captures the policy, the digest, the mode the policy ran under (`ENFORCE` or `DRY_RUN`), the outcome (`ALLOWED`, `DENIED`, or `ERROR`), and the day the pull happened.

Decisions are recorded for all evaluations, regardless of mode or outcome. Together they form an audit log of what your policies did against real pull traffic. Use them to answer questions like "why was this image blocked?", "what has this policy decided over the past month?", and "what would this policy block if I enforced it?".

This is distinct from `chainctl policies check`, which evaluates one image against your active policies on demand. Decisions are the historical record of evaluations that already happened during real pulls.

List the decisions recorded for your organization:

```shell
chainctl policies decision list --parent=$ORGANIZATION
```

```output
 REPOSITORY |     DIGEST     |  POLICY  |   MODE   | RESULT  | PULLED ON
------------|----------------|----------|----------|---------|------------
 nginx      | sha256:1a2b3c… | cooldown | DRY_RUN  | DENIED  | 2026-06-28
 nginx      | sha256:4d5e6f… | no-eol   | ENFORCED | DENIED  | 2026-06-28
 bash       | sha256:7a8b9c… | no-eol   | ENFORCED | ALLOWED | 2026-06-27
```

Narrow the results with filters. To see only the pulls a policy denied, filter by outcome:

```shell
chainctl policies decision list --parent=$ORGANIZATION --result=DENIED
```

You can also restrict to a single policy, a single mode (`ENFORCE` or `DRY_RUN`), a time window, or a single image, and request JSON for further processing. The `--since` flag takes a number of days with a `d` suffix (for example `7d`), and `--repo` accepts an image as `REPO` or `REPO:TAG`:

```shell
chainctl policies decision list --parent=$ORGANIZATION --policy=no-eol --mode=ENFORCE --since=30d -o json
chainctl policies decision list --parent=$ORGANIZATION --repo=nginx:latest
```

Decisions are deduplicated per day, so repeated pulls of the same digest under the same policy and outcome appear once for that day rather than once per pull.

Decisions are listed newest first. The command returns at most 20 decisions by default; use `--limit` to change the page size, which accepts a value from `1` to `100`:

```shell
chainctl policies decision list --parent=$ORGANIZATION --limit=50
```

## Example: staging a policy with dry run

`DRY_RUN` decisions let you measure a policy's impact before it can block anything. Because a `DRY_RUN` binding records outcomes without blocking pulls, you can enable a policy, watch what it would have denied against your real traffic, and only promote it to `ENFORCE` once the results match your expectations.

First, enable the policy in `DRY_RUN` mode:

```shell
chainctl policies enable --policy=no-eol --mode=DRY_RUN --parent=$ORGANIZATION
```

Let your normal pull traffic flow for a representative period. Then review what the policy denied while in dry run. Use `--since` to limit the review to a recent window, here the last seven days:

```shell
chainctl policies decision list --parent=$ORGANIZATION --policy=no-eol --mode=DRY_RUN --result=DENIED --since=7d
```

Each `DENIED` row is a pull that would have been blocked under `ENFORCE`. Inspect the digests to confirm the policy is catching what you intend and nothing critical to your workloads. If the results look wrong, adjust the policy's parameters or disable it; if they look right, promote the binding to enforcement:

```shell
chainctl policies enable --policy=no-eol --mode=ENFORCE --parent=$ORGANIZATION
```

After promoting, keep reviewing decisions to confirm enforcement behaves as expected. The same command now returns `ENFORCE`-mode rows for the pulls the policy is actively blocking.

## Granting an exception with an override

Once a policy is enforcing, it blocks every image that violates it. Sometimes you need to let one specific image through anyway: a known-good build that trips a policy, an artifact approved through a separate review, or an urgent fix that cannot wait for the policy itself to change. An override is an admin-granted waiver that flips a `DENIED` result to `ALLOWED` for one policy and one image, without disabling the policy or changing its binding. Every other image stays subject to the policy.

An override is deliberate and attributable. It applies to exactly one policy and one image digest, requires a reason, and records who created it and when. The engine applies it after evaluation, so the recorded decision still reflects the policy's verdict while the override is what ultimately allows the pull.

Creating an override requires the `policies.override.create` capability, which is typically held by organization owners.

Waive a policy for a specific image, identified by digest, with a reason:

```shell
chainctl policies override create \
  --policy=no-eol \
  --digest=sha256:abc123... \
  --reason="approved exception, ticket OPS-42" \
  --parent=$ORGANIZATION
```

The `--digest` value must be a manifest digest rather than a tag, so the waiver targets one exact artifact. A given policy and image can carry at most one override; to change an existing one, delete it and create it again.

Review the active overrides for an organization to see what has been waived, by whom, and why:

```shell
chainctl policies override list --parent=$ORGANIZATION
```

```output
 OVERRIDE ID  | POLICY |       TARGET        |           REASON           |    CREATED BY     |       CREATED AT
--------------|--------|---------------------|----------------------------|-------------------|-------------------------
 <id>         | no-eol | image sha256:abc12… | approved exception, OPS-42 | alice@example.com | 2026-06-28 14:30:00 UTC
```

When the exception is no longer needed, delete the override to restore the policy's result for that image. Use `chainctl policies override list` to find the ID:

```shell
chainctl policies override delete <override-id>
```

Once deleted, the image is again subject to whatever the policy decides.

## Writing custom policies

A [custom policy](#policy-types) is driven by a [Rego](https://www.openpolicyagent.org/docs/policy-language) expression that Chainguard evaluates against one artifact at a time. This section covers what that expression must look like, what data it can read, and which parts of the Rego language are available to it.

### Anatomy of a policy expression

Every custom policy expression follows the same shape:

```rego
package chainguard.policies

import rego.v1

default allow := false

allow if {
    input.main_package_version.lts
}
```

Three rules are non-negotiable, and Chainguard rejects the policy at write time if any is missing:

- **The package must be `chainguard.policies`.** Any other package name is an error.
- **The expression must define a rule named `allow`.** This is the only rule Chainguard reads. Its value decides the outcome: `true` allows the artifact, anything else denies it.
- **The expression must compile**, using only the builtins listed under [The available Rego subset](#the-available-rego-subset).

Beyond that, the module is ordinary Rego. You can define helper rules, comprehensions, and functions freely, as long as `allow` ends up defined.

#### Always declare a default

`default allow := false` is a convention worth following in every policy. Without it, an expression whose body is undefined leaves `allow` undefined rather than `false`. An undefined `allow` denies the artifact, so the outcome is the same either way, but the explicit default makes that fail-closed behavior obvious to whoever reads the policy next.

#### Multiple allow rules are ORed

Rego evaluates every `allow` rule and the artifact is allowed if any one of them succeeds. This is the idiomatic way to express alternatives. The `no-eol` system policy uses it to allow both "no end-of-life date recorded" and "end-of-life date is still in the future":

```rego
package chainguard.policies

import rego.v1

default allow := false

allow if {
    not input.main_package_version.eolDate
}

allow if {
    eol_ns := time.parse_ns("2006-01-02", input.main_package_version.eolDate)
    eol_ns > time.now_ns()
}
```

To express "all of these conditions must hold" instead, put the conditions in a single rule body — the statements inside one `allow if { … }` block are ANDed.

### The input document

Your expression reads the artifact under evaluation from the `input` document. At launch this surface is deliberately narrow: it carries lifecycle data about the artifact's main package and nothing else.

The fields below are what is available for policies whose resource type is `registry.chainguard.dev/Repo@v1` (the `Repo` shorthand).

| Field | Type | Description |
|---|---|---|
| `input.main_package` | string | Name of the image's main package. |
| `input.main_package_version` | object | Version metadata for the main package. See below. |
| `input.create_time` | string | When the image was created, as an RFC 3339 timestamp. Derived from the image's `org.opencontainers.image.created` annotation. |
| `input.parameters` | object | Values for the parameters your policy declares. See [Parameters](#parameters-in-custom-policies). |

`input.main_package_version` carries these fields:

| Field | Type | Description |
|---|---|---|
| `version` | string | The version stream identifier. |
| `latestVersion` | string | The latest version within this version stream. |
| `eolDate` | string | The date this version reaches end-of-life, as `YYYY-MM-DD`. |
| `releaseDate` | string | The date this version was released, as `YYYY-MM-DD`. |
| `exists` | boolean | Whether the package exists in an apk repository. |
| `fips` | boolean | Whether a FIPS-enabled build of the package exists. |
| `lts` | boolean | Whether upstream considers this a long-term support version. |
| `eolBroken` | boolean | Whether an end-of-life version can no longer be supported. |
| `versionSource` | object | Source reference for the version, with `ref` and `sha` fields. |

### Parameters in custom policies

A parameter is a value your policy declares but does not hardcode. Whoever enables the policy supplies the value on the binding with `--param=KEY=VALUE`, so one policy definition can serve several thresholds without being edited.

Declare parameters in the `parameters` block of the policy manifest, then read them at `input.parameters.<name>`. The `cooldown` system policy is a good template:

```yaml
name: cooldown
description: Denies images with a build timestamp less than the specified number of days old.
supported_resource_type: registry.chainguard.dev/Repo@v1
parameters:
  - name: days
    type: PARAMETER_TYPE_INTEGER
    description: Minimum age in days before access is allowed.
    default: 7
    minimum: 1
    maximum: 365
expression: |
  package chainguard.policies

  import rego.v1

  default cooldown_days := 7

  cooldown_days := input.parameters.days if {
    is_number(input.parameters.days)
  }

  default allow := false

  allow if {
    create_ns := time.parse_rfc3339_ns(input.create_time)
    age_days := (time.now_ns() - create_ns) / (24 * 60 * 60 * 1000000000)
    age_days >= cooldown_days
  }
```

Available parameter types are `PARAMETER_TYPE_STRING`, `PARAMETER_TYPE_INTEGER`, `PARAMETER_TYPE_STRING_LIST`, and `PARAMETER_TYPE_BOOLEAN`. The `minimum` and `maximum` constraints apply to integer parameters.

#### Undeclared parameters are rejected at write time

Chainguard type-checks your expression against the parameters your manifest declares. Referencing `input.parameters.days` when the manifest does not declare a `days` parameter is an error at create, update, and validate time, rather than a policy that silently denies everything once it is live.

### The available Rego subset

Custom policies may use most of the OPA standard library. Referencing a blocked builtin is a compile error, reported at validate, create, and update time rather than at evaluation.

The blocked builtins are:

- `http.send`
- Everything under `net.`, including `net.lookup_ip_addr`
- Everything under `opa.`, including `opa.runtime`
- Everything under `rego.`, for example `rego.metadata.chain`
- `trace` and `print`
- The certificate and key parsers: `crypto.x509.parse_certificates`, `crypto.x509.parse_and_verify_certificates`, `crypto.x509.parse_certificate_request`, `crypto.x509.parse_keypair`, `crypto.x509.parse_rsa_private_key`, and `crypto.parse_private_keys`

The `import rego.v1` statement is not affected by the `rego.` entry above — that entry covers builtin functions, not language imports. Use `import rego.v1` as shown in the examples on this page.

Everything else in the OPA standard library is available, including the namespaces most policies need:

- String handling — `strings.*`, `sprintf`, `format_int`, `concat`, `contains`, `startswith`, `endswith`, `upper`, `lower`, `split`, `trim`
- Numbers and aggregates — `numbers.*`, `count`, `sum`, `min`, `max`, `product`, `sort`, `all`, `any`, `round`, `abs`
- Collections — `arrays.*`, `objects.*`, `sets.*`
- Time — `time.*`, including `time.now_ns`, `time.parse_ns`, `time.parse_rfc3339_ns`, and `time.add_date`
- Pattern matching — `regex.*`, `glob.*`
- Encoding — `json.*`, `yaml.*`, `base64.*`, `hex.*`
- Versions — `semver.*`, useful for comparing `input.main_package_version.version` against a floor
- Hashing — the non-parsing parts of `crypto.*`, and `units.*`

## Managing custom policies with chainctl

Custom policies are managed with the `chainctl policies custom` command group, which provides four subcommands: `validate`, `create`, `update`, and `delete`.

Creating, updating, and deleting custom policies requires that the feature be enabled for your organization. If it is not, these commands return:

```output
You are not entitled to use Policies.

To enable this feature, contact your Customer Success Team.
```

### The policy manifest

A custom policy is defined by a YAML manifest. Because the manifest is a single file, it can be checked into git, reviewed on a pull request, and validated in CI alongside the rest of your infrastructure.

```yaml
name: lts-only
description: Allow only images whose main package is a long-term support version.
supported_resource_type: registry.chainguard.dev/Repo@v1
expression_type: EXPRESSION_TYPE_REGO
parameters:
  - name: allow_non_lts
    type: PARAMETER_TYPE_BOOLEAN
    description: When true, also allow images whose main package is not an LTS version.
    default: false
expression: |
  package chainguard.policies

  import rego.v1

  default allow := false

  allow if {
    input.main_package_version.lts
  }

  allow if {
    input.parameters.allow_non_lts
  }
```

#### Manifest fields

| Field | Required | Description |
|---|---|---|
| `name` | Yes | The policy name. Must be unique within the organization for the given resource type. |
| `expression` | Yes | The Rego expression. See [Writing custom policies](#writing-custom-policies). |
| `supported_resource_type` | Yes | The single resource type this policy applies to. |
| `description` | No | A human-readable description, shown in `chainctl policies list` and `describe`. |
| `expression_type` | No | Defaults to `EXPRESSION_TYPE_REGO`, which is the only accepted value. |
| `parameters` | No | The parameters the policy declares. Omit entirely for a parameterless policy. |

Each entry under `parameters` accepts `name`, `type`, `description`, `default`, `minimum`, `maximum`, `allowed_values`, `required`, and `deprecated`.

#### Resource types

Every custom policy declares exactly one supported resource type. Where a command takes a `--resource-type` flag, it accepts either a shorthand or the fully-qualified type:

| Shorthand | Fully-qualified type |
|---|---|
| `Repo` | `registry.chainguard.dev/Repo@v1` |
| `Python` | `libraries.chainguard.dev/PythonPackage@v1` |
| `Java` | `libraries.chainguard.dev/JavaPackage@v1` |
| `Javascript` | `libraries.chainguard.dev/NPMPackage@v1` |

The resource type is fixed at creation and cannot be changed afterwards. To move a policy to a different resource type, create a new policy and delete the old one.

Within an organization, a policy is identified by the combination of its name and its resource type. The same name may be reused across different resource types — you can have both a `Repo` and a `Python` policy called `minimum-version`. Where that ambiguity exists, `update` and `delete` accept `--resource-type` to disambiguate.

### Validating a policy

`chainctl policies custom validate` checks a policy without persisting anything. It is the fastest way to iterate while authoring, and it is what you should run in CI on any repository that holds policy manifests.

Validate a full manifest, checking both the expression and the parameter schemas:

```shell
chainctl policies custom validate --file policy.yaml
```

```output
Policy is valid.
```

Validate just a Rego expression, for a quick parse-and-compile check while writing:

```shell
chainctl policies custom validate --expression policy.rego
```

```output
Expression is valid.
```

The two flags are mutually exclusive, and exactly one is required.

On failure, the command prints one diagnostic per problem and exits non-zero. Expression errors carry the line and column in the Rego source; parameter schema errors identify the offending field:

```output
line 7:3: rego_type_error: undefined ref: input.mian_package
line 12:5: rego_type_error: undefined ref: input.parameters.day
```

### Creating a policy

`chainctl policies custom create` creates a policy in your organization. It supports two modes.

**From a manifest.** This is the primary path, and the only one that supports parameters:

```shell
chainctl policies custom create --file policy.yaml --parent=$ORGANIZATION
```

**From a raw Rego file.** A shortcut for parameterless policies, where writing a manifest for two fields is more ceremony than it is worth. `--name` and `--resource-type` are both required in this mode; `--description` is optional:

```shell
chainctl policies custom create \
  --expression lts-only.rego \
  --name lts-only \
  --resource-type Repo \
  --description "Allow only LTS versions of the main package" \
  --parent=$ORGANIZATION
```

If a policy declares parameters, it must be created from a manifest — there is no flag equivalent for a parameter schema. In `--file` mode the manifest is authoritative.

Creation validates the policy before storing it. A rejected policy reports one diagnostic per problem, covering both the name and the expression at once.

#### Policy names

Names are validated on create and update. A name must:

- Be at most 255 characters
- Start and end with an alphanumeric character, which rejects leading and trailing whitespace
- Contain no control characters
- Be unique within the organization for its resource type

### Updating a policy

`chainctl policies custom update` modifies an existing policy, identified by `--policy` with either its name or its UIDP. Only custom policies can be updated; system policies are managed by Chainguard and are rejected with an error. It supports two modes.

**Full replacement from a manifest.** The manifest supplants the entire definition — the resulting policy is exactly what the manifest declares, and any field the manifest omits is cleared:

```shell
chainctl policies custom update --policy lts-only --file policy.yaml --parent=$ORGANIZATION
```

**Partial update from flags.** Only the fields you pass are changed; everything else is preserved:

```shell
# Rename
chainctl policies custom update --policy lts-only --name lts-strict --parent=$ORGANIZATION

# Change just the description
chainctl policies custom update --policy lts-only --description "Allow only LTS main packages"

# Replace the expression from a new .rego file
chainctl policies custom update --policy lts-only --expression new-lts-only.rego
```

Flag mode is restricted to policies that do **not** declare parameter schemas. For a parameterized policy, use `--file`.

#### Constraints on update

The supported resource type is immutable. A `--file` update whose manifest declares a resource type different from the current policy's is rejected.

Where a policy name is shared across resource types, pass `--resource-type` to disambiguate. It is ignored when `--policy` is given as a UIDP, which is already unambiguous:

```shell
chainctl policies custom update --policy minimum-version --resource-type Python --description "python-only variant"
```

#### Parameter changes and existing bindings

Because a `--file` update is a full replacement, a policy can gain, lose, or change parameters between versions. Existing bindings are **not** re-validated against the new schema — a binding created against the old parameter shape stays as it was.

When an update changes the parameter schema, `chainctl` warns you:

```output
Note: parameter_schemas changed. Existing bindings were not re-validated against the new schema; run `chainctl policies binding list` to check for stale bindings.
```

### Deleting a policy

`chainctl policies custom delete` permanently removes a custom policy:

```shell
chainctl policies custom delete --policy lts-only --parent=$ORGANIZATION
```

Only custom policies can be deleted; system policies are managed by Chainguard and are rejected with an error.

Deletion is permanent — a deleted policy cannot be recovered.

Deletion also cascades. Every binding that referenced the policy is removed, and every override waiving it is removed as well. Before deleting, `chainctl` reports how many of each will go and asks you to confirm:

```output
Will delete custom policy "lts-only" (720a...c81).
This also removes 2 binding(s) and 1 override(s) that reference this policy.
```

Pass `--force` to skip the confirmation prompt:

```shell
chainctl policies custom delete --policy 720a...c81 --force
```

As with `update`, pass `--resource-type` when a name is shared across resource types:

```shell
chainctl policies custom delete --policy minimum-version --resource-type Python --parent=$ORGANIZATION
```

### A full custom policy lifecycle

The following walks a policy from authoring to enforcement and back out again.

Write the manifest and validate it locally:

```shell
chainctl policies custom validate --file lts-only.yaml
```

Create the policy. This defines it but does not activate it — a policy with no binding has no effect:

```shell
chainctl policies custom create --file lts-only.yaml --parent=$ORGANIZATION
```

Confirm it is there. Custom policies appear alongside system policies, distinguished by the type column:

```shell
chainctl policies list --parent=$ORGANIZATION
```

Activate it in `DRY_RUN` mode, which records outcomes without blocking any pulls:

```shell
chainctl policies enable --policy=lts-only --mode=DRY_RUN --parent=$ORGANIZATION
```

Check a specific image against your active policies without waiting for a pull:

```shell
chainctl policies check cgr.dev/$ORGANIZATION/python:latest
```

Let your normal pull traffic run for a representative period, then review what the policy would have denied:

```shell
chainctl policies decision list --parent=$ORGANIZATION --policy=lts-only --result=DENIED --since=7d
```

Each `DENIED` row is a pull that would have been blocked under `ENFORCE`. If the results are as
expected, promote the binding:

```shell
chainctl policies enable --policy=lts-only --mode=ENFORCE --parent=$ORGANIZATION
```

To stop enforcing without deleting the policy, disable the binding. The definition stays in place and can be re-enabled later:

```shell
chainctl policies disable --policy=lts-only --parent=$ORGANIZATION
```

To remove the policy entirely, along with its bindings and overrides:

```shell
chainctl policies custom delete --policy lts-only --parent=$ORGANIZATION
```

## Custom policies FAQ

Common questions that come up when authoring and operating custom policies.

### Why was my image denied, and how do I debug it?

Start by confirming *which* policy denied it. An image is allowed only when every active policy allows it, so a denial you attribute to your new custom policy may be coming from an entirely different one.

```shell
chainctl policies check cgr.dev/$ORGANIZATION/python:latest
```

```output
  POLICY  |  MODE   | PARAMETERS | RESULT
----------|---------|------------|---------
 cooldown | DRY_RUN | days=7     | DENIED
 lts-only | ENFORCE |            | DENIED
 no-eol   | ENFORCE |            | ALLOWED
```

Read the table per row. The pull is blocked only when a policy in `ENFORCE` mode returns `DENIED`. A `DENIED` from a `DRY_RUN` policy is a preview of what enforcing it would do, not a block.

Once you know which policy is responsible, work through the usual causes in this order:

**1. A field you referenced is absent.** This is by far the most common cause. Fields with no value are omitted from the input document entirely, so a reference to an absent field makes the surrounding rule body undefined, `allow` falls through to its default of `false`, and everything is denied. See [The input document](#the-input-document) for the fields a policy can read.

**2. A nested field name is misspelled.** Write-time validation catches typos in the top-level fields (`input.crete_time` fails), but it does **not** check inside `input.main_package_version`. A misspelled `input.main_package_version.eolDte` compiles cleanly and never matches. Watch the casing in particular: top-level fields are snake_case (`main_package`, `create_time`) while the fields under `main_package_version` are camelCase (`eolDate`, `releaseDate`, `latestVersion`).

**3. The rule logic is inverted.** Remember that `allow` decides what is *permitted*. A policy meant to block end-of-life images allows everything that is *not* end-of-life, rather than matching the images you want to stop.

To see what a policy has actually decided against real pull traffic, use the decision log rather than `check`:

```shell
chainctl policies decision list --parent=$ORGANIZATION --policy=lts-only --result=DENIED --since=7d
```

Note that `check` evaluates against your current configuration on demand, while decisions are the historical record of evaluations that already happened during real pulls.

Finally, if you need to let one specific image through while you sort the policy out, an [override](#granting-an-exception-with-an-override) waives a single policy for a single digest without disabling the policy for everything else.

### What input fields are available to a policy?

At launch, the input document carries lifecycle data about the artifact's main package and nothing else:

- `input.main_package` — the main package name
- `input.main_package_version` — version metadata, including `version`, `latestVersion`, `eolDate`, `releaseDate`, `exists`, `fips`, `lts`, `eolBroken`, and `versionSource`
- `input.create_time` — the image creation timestamp, as RFC 3339
- `input.parameters.<name>` — values for the parameters your policy declares

The [input document reference](#the-input-document) has the full table with types and descriptions.

To see the shape of the input against a real policy, inspect a system policy, which reads the same document:

```shell
chainctl policies describe --policy=no-eol --parent=$ORGANIZATION -o json
```

### Why was my Rego rejected at write time?

Chainguard validates every expression before storing it, so a policy that would have been broken at pull time is rejected at authoring time instead. Errors come back with the line and column in your Rego source. The causes, in rough order of frequency:

**Wrong package name.** The expression must declare `package chainguard.policies`. Any other package is rejected.

**No `allow` rule.** The expression must define a rule named `allow`. It is the only rule Chainguard reads.

**A reference to an undeclared parameter.** Referencing `input.parameters.days` when your manifest does not declare a `days` parameter is an error. This is strict in both directions: a parameterless policy may not reference `input.parameters` at all. Add the declaration to the manifest in the same change as the reference.

**A typo in a top-level input field.** `input.crete_time` and `input.mian_package` both fail validation. Only the top level is checked this way — misspellings inside `input.main_package_version` are not caught.

**A blocked builtin.** Some OPA builtins cannot be used in a custom policy. See [The available Rego subset](#the-available-rego-subset) for the full list and what remains available.

**An ordinary syntax or type error.** Standard Rego compile errors surface the same way, with line and column.

A manifest can also be rejected before the expression is ever compiled, if the YAML itself is wrong. The manifest is parsed strictly, so an unrecognized key is an error naming the offending field rather than being silently ignored.

If you passed a raw `.rego` file to `--file`, the error suggests the fix: `--file` expects a full YAML manifest, and `--expression` is the flag for a bare Rego file.

Validation errors are aggregated, so the command reports every problem it found across both the name and the expression rather than making you fix them one at a time.

### How do I test a policy before committing to it?

There are two levels of checking, from fastest to most realistic.

#### Validate the manifest

`chainctl policies custom validate` runs the same checks that `create` and `update` apply, without persisting anything:

```shell
chainctl policies custom validate --file policy.yaml
```

While iterating on just the Rego, skip the manifest:

```shell
chainctl policies custom validate --expression policy.rego
```

This is the authoritative check. A manifest that validates cleanly will not be rejected on create for expression reasons.

#### Stage it in DRY_RUN against real traffic

The most realistic check is the platform itself. Create the policy and enable it in `DRY_RUN` mode, which records outcomes without blocking any pulls:

```shell
chainctl policies custom create --file policy.yaml --parent=$ORGANIZATION
chainctl policies enable --policy=lts-only --mode=DRY_RUN --parent=$ORGANIZATION
```

Check a specific image immediately:

```shell
chainctl policies check cgr.dev/$ORGANIZATION/python:latest
```

Then let normal pull traffic run for a representative period and review what the policy would have blocked:

```shell
chainctl policies decision list --parent=$ORGANIZATION --policy=lts-only --result=DENIED --since=7d
```

Every `DENIED` row is a pull that would have failed under `ENFORCE`. Promote the binding only once those results match your expectations.

### Can a custom policy allow something a system policy denies?

No. Every active policy is evaluated independently, and an image is allowed only when all of them allow it. A single `ENFORCE` denial blocks the pull regardless of what other policies decided, so a custom policy cannot loosen a system policy.

To let a specific image through a policy that denies it, use an [override](#granting-an-exception-with-an-override), which waives one policy for one digest. To stop a system policy from applying at all, disable its binding.

### Can I change a policy's resource type?

No. The supported resource type is fixed when the policy is created. A `--file` update whose manifest declares a different resource type is rejected.

To move a rule to a different resource type, create a new policy with the new type and delete the old one. Note that deleting cascades — the old policy's bindings and overrides go with it, so recreate those against the new policy.

### Why do I have two policies with the same name?

Policy names are unique per resource type, not per organization, so a `Repo` policy and a `Python` policy can both be called `minimum-version`.

When a name is ambiguous, `chainctl policies custom update` and `delete` accept `--resource-type` to disambiguate:

```shell
chainctl policies custom delete --policy minimum-version --resource-type Python --parent=$ORGANIZATION
```

The flag is ignored when `--policy` is given as a UIDP, which already identifies a single policy.

### I changed a policy's parameters and its bindings stopped working

Updating a policy from a manifest is a full replacement, so a policy can gain, lose, or change parameters between versions. Existing bindings are **not** re-validated against the new schema — a binding created against the old parameter shape stays exactly as it was.

`chainctl` warns you when an update changes the parameter schema. Review your bindings afterwards:

```shell
chainctl policies binding list --parent=$ORGANIZATION
```

Re-enable any binding whose parameters no longer match the policy's schema, supplying the current parameters with `--param=KEY=VALUE`.

## Known issues

Policies are in open beta, and we are continuously working to improve the experience. The items below are current limitations you may run into when working with overrides, along with the workaround for each.

### An override/binding mutation is not effective immediately

After you create an override, it does not take effect right away. The platform caches policy decisions, and it takes a short while for that cache to refresh before the override is applied. If a pull is still blocked immediately after you create an override, wait a moment and try again.

The same delay applies to binding mutations, such as updating a policy's parameters. After you change a binding (for example, adjusting the `days` parameter on a `cooldown` policy), wait a moment before the new configuration takes effect.

### A single image can require two overrides

Pulling an image with a client such as Docker involves two separate requests: a manifest pull followed by an image pull. Both requests are now evaluated against your policies, and they resolve to different digests, so a single `docker pull` can produce two `DENIED` decisions. An override targets one digest, so waiving only the first digest still leaves the second one blocked.

To work around this, create an override for each denied digest. First attempt the pull so both decisions are recorded, then use [policy decisions](#policy-decisions) to find the digests that were blocked:

```shell
chainctl policies decision list --parent=$ORGANIZATION --result=DENIED
```

```output
 REPOSITORY |     DIGEST     |  POLICY  |   MODE   | RESULT | PULLED ON
------------|----------------|----------|----------|--------|------------
 curl       | sha256:609aeb… | cooldown | ENFORCED | DENIED | 2026-07-02
 curl       | sha256:db532b… | cooldown | ENFORCED | DENIED | 2026-07-02
```

Create an override for each of the denied digests:

```shell
chainctl policies override create \
  --policy=cooldown \
  --digest=sha256:609aeb... \
  --reason="approved exception, ticket OPS-42" \
  --parent=$ORGANIZATION

chainctl policies override create \
  --policy=cooldown \
  --digest=sha256:db532b... \
  --reason="approved exception, ticket OPS-42" \
  --parent=$ORGANIZATION
```

With both digests waived, the pull is allowed. Remember that the override is subject to the cache refresh described above, so allow a short delay before retrying the pull.

See `chainctl policies --help` or the [chainctl reference pages](/platform/chainctl/) for more information.
