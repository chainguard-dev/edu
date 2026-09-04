---
title: "Pull token output formats and credential names"
linktitle: "Pull token output"
aliases:
- /chainguard/chainctl-usage/pull-token-output/
type: "article"
description: "A reference for the output formats chainctl auth pull-token create supports and the names each format gives to the identity ID and token."
lead: "Every pull token is a pair of values — an identity ID and a token — and each output format labels that pair differently. This page maps the labels to each other."
date: 2026-09-03T00:00:00+00:00
lastmod: 2026-09-04T16:13:45+00:00
draft: false
tags: ["chainctl", "Reference"]
images: []
menu:
  docs:
    parent: "chainctl-usage"
toc: true
weight: 025
---

`chainctl auth pull-token create` returns two values:

* An **identity ID**, the identifier of the pull token identity that `chainctl` just created. It takes the form `ORGANIZATION_ID/TOKEN_ID`, where both parts are hexadecimal strings.
* A **token**, a JSON Web Token that authenticates as that identity until the token's time to live expires.

Every tool that consumes a pull token takes that pair as a username and a password for [HTTP basic authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Authentication#basic_authentication_scheme): the identity ID is the username, and the token is the password. What changes between output formats is only the label.

## Terminology mapping

| Value | Default output | `--output=json` | `--output=env` |
| --- | --- | --- | --- |
| Identity ID | `Username` | `identity_id` | `CHAINGUARD_IDENTITY_ID` or `CHAINGUARD_<ECOSYSTEM>_IDENTITY_ID` |
| Token | `Password` | `token` | `CHAINGUARD_TOKEN` or `CHAINGUARD_<ECOSYSTEM>_TOKEN` |

The Chainguard Console labels the same two values **Username** and **Password** when it displays a new access token.

`chainctl auth pull-token` without a subcommand is equivalent to `chainctl auth pull-token create`, so the formats described here apply to both.

`chainctl auth pull-token create` supports two output formats, `env` and `json`, plus the default output you get when you pass no `--output` flag at all.

## Default output

With no `--output` flag, `chainctl` prints instructions for the repository type you asked for.

For `--repository=oci`, the default, it prints a ready-to-run `docker login` command:

```sh
chainctl auth pull-token create
```

```output
To use this pull token in another environment, run this command:

    docker login "cgr.dev" --username "<identity-id>" --password "<pull-token>"
```

The `--username` value is the identity ID and the `--password` value is the token. Both work with any tool that logs in to an OCI registry, including Podman, Helm, and registry mirroring tools. Refer to [Authenticate to Chainguard's Registry](/chainguard/containers/registry/authenticating/#using-a-pull-token-with-podman-helm-and-other-tools) for examples.

For every other repository type, `chainctl` prints the pair as a username and a password:

```sh
chainctl auth pull-token create --repository=java
```

```output
To use this pull token in another environment, supply the following for Basic authorization:

Username: <identity-id>

Password: <pull-token>
```

## JSON output

`--output=json` prints one compact object with an `identity_id` field and a `token` field:

```sh
chainctl auth pull-token create --repository=java --output=json
```

```output
{"identity_id":"<identity-id>","token":"<pull-token>"}
```

The field names stay the same for every repository type. Pipe the object to `jq` or another JSON processor to extract either value:

```sh
TOKEN_JSON=$(chainctl auth pull-token create --repository=java --output=json)
USERNAME=$(echo "$TOKEN_JSON" | jq -r '.identity_id')
PASSWORD=$(echo "$TOKEN_JSON" | jq -r '.token')
```

## Environment output

`--output=env` prints two `export` statements, one per value:

```sh
chainctl auth pull-token create --repository=java --output=env
```

```output
export CHAINGUARD_JAVA_IDENTITY_ID=<identity-id>
export CHAINGUARD_JAVA_TOKEN=<pull-token>
```

Wrap the command in `eval` to run those `export` statements, which sets both variables in your current session:

```sh
eval $(chainctl auth pull-token create --repository=java --output=env)
```

The variable names depend on the repository type. For a library ecosystem, `chainctl` uppercases the `--repository` value and inserts it into the name; for `oci` and `apk` it uses the unqualified names.

| `--repository` | Identity ID variable | Token variable |
| --- | --- | --- |
| `oci` (default) | `CHAINGUARD_IDENTITY_ID` | `CHAINGUARD_TOKEN` |
| `apk` | `CHAINGUARD_IDENTITY_ID` | `CHAINGUARD_TOKEN` |
| `java` | `CHAINGUARD_JAVA_IDENTITY_ID` | `CHAINGUARD_JAVA_TOKEN` |
| `javascript` | `CHAINGUARD_JAVASCRIPT_IDENTITY_ID` | `CHAINGUARD_JAVASCRIPT_TOKEN` |
| `python` | `CHAINGUARD_PYTHON_IDENTITY_ID` | `CHAINGUARD_PYTHON_TOKEN` |

Because the ecosystem name is part of the variable, credentials for two ecosystems can coexist in one shell session or one secrets file:

```sh
eval $(chainctl auth pull-token create --repository=java --output=env)
eval $(chainctl auth pull-token create --repository=python --output=env)
```

Each invocation creates a new pull token identity. Write the `export` statements to a file or a secrets manager rather than rerunning the command whenever you need the values again, because `chainctl` displays the token only once.

### Chainguard and tool-specific variables

`chainctl` emits variables starting with `CHAINGUARD_`. However, build tools that read credentials from the environment typically use their own names, and don't read the `CHAINGUARD_*` variables directly. In such cases, you must map one to the other explicitly.

For example, `uv` reads index-scoped credentials from `UV_INDEX_<NAME>_USERNAME` and `UV_INDEX_<NAME>_PASSWORD`, where `<NAME>` is the index name in uppercase, with underscores replacing hyphens. For an index named `chainguard`:

```sh
export UV_INDEX_CHAINGUARD_USERNAME="${CHAINGUARD_PYTHON_IDENTITY_ID}"
export UV_INDEX_CHAINGUARD_PASSWORD="${CHAINGUARD_PYTHON_TOKEN}"
```

The same pattern applies wherever a tool defines its own variable, such as the `HTTP_AUTH` variable used for [private APK repositories](/chainguard/containers/features/packages/private-apk-repos/#pull-token-automation):

```sh
export HTTP_AUTH="basic::${CHAINGUARD_IDENTITY_ID}:${CHAINGUARD_TOKEN}"
```

Names you choose yourself, such as GitHub Actions secrets, are also independent of the `CHAINGUARD_*` convention. Whatever you call them, the identity ID is the username and the token is the password.

## Why the `--output` help text lists more formats

If you pass any other value, `chainctl` prints a warning to standard error, then falls back to default output. Requesting `csv`, for example, produces a warning along these lines:

```output
"csv" is not a supported output. Supported: [ env json]. Using print to command line
```

Even when a command returns this warning, it still creates the pull token. It refuses only the formatting request, so a script that expects machine-readable output on standard output receives prose instead. This matters most for `eval`: `eval $(chainctl auth pull-token --output=csv)` creates a token, sends the warning to your terminal, and then tries to run the human-readable text as shell commands.

The `--output` flag is global, so `chainctl --help` and every reference page describe it the same way:

```output
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
```

That list is the union of every format any `chainctl` command supports, not a list of formats that all commands support. Each command declares its own subset. Table-shaped commands such as `chainctl iam identities list` accept `csv` and `markdown`; `pull-token create` returns a single credential pair and accepts only `env` and `json`.

## Related pages

* [Authenticate to Chainguard's Registry](/chainguard/containers/registry/authenticating/#authenticating-with-a-pull-token) for container pull tokens
* [Chainguard Libraries access](/chainguard/libraries/introduction/access/#pull-token) for library pull tokens
* [Private APK repositories](/chainguard/containers/features/packages/private-apk-repos/#pull-token-automation) for APK pull tokens
* [chainctl auth pull-token create](/platform/chainctl/chainctl-docs/chainctl_auth_pull-token_create/) for the generated flag reference
* [Automating with chainctl](/platform/chainctl-usage/automating-chainctl/) for other scripting patterns
