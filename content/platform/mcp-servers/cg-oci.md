---
title: "cg-oci: the Chainguard container registry MCP server"
linktitle: "cg-oci"
description: "Connect an MCP client to cg-oci and read manifests, image configs, SBOMs, apko configs, and SLSA provenance directly from the Chainguard container registry."
type: "article"
date: 2026-09-16T00:00:00+00:00
lastmod: 2026-09-16T00:00:00+00:00
draft: false
tags: ["MCP", "Containers"]
images: []
menu:
  docs:
    parent: "mcp-servers"
    identifier: "cg-oci"
toc: true
weight: 040
---

`cg-oci` gives an AI tool read-only access to the Chainguard container registry at `cgr.dev`. Through it, a client can list the repositories and tags your account can reach, fetch a manifest or image config by tag or digest, and read the signed attestations attached to an image — its SPDX SBOM, its apko build configuration, and its SLSA build provenance. Every response comes from the registry as it exists at the moment of the call, so an AI tool can answer what a specific image actually contains rather than what its documentation says it contains.

The server uses the Streamable HTTP transport, at this endpoint:

```
https://cgr.dev/mcp
```

## Prerequisites

- An MCP-compatible client such as Claude Code, Claude Desktop, or Cursor
- A [Chainguard account](https://console.chainguard.dev/)

## Connect to the server

### Claude Code

Add the server with `claude mcp add`, using the HTTP transport:

```shell
claude mcp add --transport http cg-oci https://cgr.dev/mcp
```

Pick the scope that fits how you want to use it: `local` (the default — only you, in the current directory), `project` (writes a shared `.mcp.json` at the repository root, checked in for teammates), or `user` (only you, across every project). A registry lookup is useful almost everywhere, so `--scope user` is usually the right choice:

```shell
claude mcp add --transport http --scope user cg-oci https://cgr.dev/mcp
```

The server is added unauthenticated. To complete OAuth, start a session and run the `/mcp` command:

```Prompt
/mcp
```

Select **cg-oci**, choose **Authenticate**, and approve the connection in the browser window that opens. Check the status any time with:

```shell
claude mcp list
```

```output
cg-oci: https://cgr.dev/mcp (HTTP) - ✓ Connected
```

### Cursor

Cursor supports HTTP transport natively. Add the server to your MCP configuration:

```json
{
  "mcpServers": {
    "cg-oci": {
      "url": "https://cgr.dev/mcp"
    }
  }
}
```

Restart Cursor, then connect the server from **Tools & MCPs** in settings and complete the browser sign-in.

### Claude Desktop

Claude Desktop reads MCP servers from a JSON file but does not yet support HTTP transport directly. Use [`mcp-remote`](https://github.com/geelen/mcp-remote) to bridge to the hosted server:

```json
{
  "mcpServers": {
    "cg-oci": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://cgr.dev/mcp"
      ]
    }
  }
}
```

The configuration file lives at:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

`npx` downloads and runs `mcp-remote` on demand, so you need Node.js installed on the host. Restart Claude Desktop after saving the file.

### Other MCP clients

Any client that supports a remote Streamable HTTP MCP server with OAuth can connect to the same endpoint. Point it at `https://cgr.dev/mcp` and complete the browser sign-in when prompted. Consult your client's documentation for where its MCP configuration lives.

## Authentication

Authentication is OAuth 2.0 against the Chainguard issuer. You can read an image through `cg-oci` only if your account can pull it from the registry.

{{< alert context="warning" >}}
**Each Chainguard MCP server requires its own login.** Authenticating to `cg-oci` does not authenticate you to `cg-apk`, `cg-versions`, or `cg-api`. Connecting all four means completing the browser sign-in four times. As of this writing, there is no unified sign-in across the four servers.
{{< /alert >}}

On a remote or headless workstation, you can supply a token from `chainctl` instead of completing the browser flow. Refer to [Authenticate with chainctl instead of a browser](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser) for the full recipe; `cg-oci`'s audience is `https://cgr.dev/mcp`.

### Access scope

Results are scoped to your account, which has two effects:

- **`list_repos` does not list the public Chainguard catalog.** It lists every repository your token can reach, across every organization you belong to, in `_catalog` order. If your organization mirrors images into its own namespace, those repositories appear alongside the public ones.
- **Public `chainguard/*` repositories expose only `latest` and `latest-dev`.** Version tags such as `3.12` live in your organization's own namespace and require an entitlement. `chainguard/python:3.12` is not a valid reference for an unentitled caller, even though 3.12 builds of the Python image exist.

To browse the public catalog and its documented tags, use the [Chainguard Containers directory](https://images.chainguard.dev/) instead.

## Tool reference

The tools fall into two groups. The `list_*` tools return one bounded page at a time — 50 items by default, 200 at most — and you continue by passing a cursor back. The `get_*` tools return a single object exactly as the registry stores it.

Every tool identifies an image with two separate parameters rather than one fully qualified reference:

- `repo` — the repository name without the registry host, for example `chainguard/python`
- `reference` — a tag such as `latest`, or a digest such as `sha256:5a673f...`

Passing `cgr.dev/chainguard/python:3.12` as a single string does not work.

| Tool | Parameters | Returns | Example prompt |
| ----- | ----- | ----- | ----- |
| `list_repos` | `page_size`, `cursor` | `{repos, count, has_more}` | "What Chainguard repositories can I access?" |
| `list_tags` | `repo`, `page_size`, `cursor`, `include_digest_tags` | `{tags, count, has_more, next_cursor}` | "What tags exist for chainguard/python?" |
| `get_manifest` | `repo`, `reference` | `{digest, manifest, media_type, size}` | "Get the manifest for chainguard/python:latest" |
| `get_config` | `repo`, `reference`, `architecture` | `{digest, config}` | "What's the entrypoint of the chainguard/python image?" |
| `get_sbom` | `repo`, `reference`, `architecture` | `{subject_digest, size_bytes, attestations}` | "Show me the SBOM for chainguard/python:latest" |
| `list_sbom_packages` | `repo`, `reference`, `architecture`, `page_size`, `cursor` | `{subject_digest, documents, packages, count, total_packages, has_more, next_cursor}` | "What packages are in the amd64 chainguard/python image?" |
| `get_apko_config` | `repo`, `reference`, `architecture` | `{subject_digest, attestations}` | "What apko config built chainguard/python:latest?" |
| `get_provenance` | `repo`, `reference`, `architecture` | `{subject_digest, attestations}` | "Show me the build provenance for chainguard/python:latest" |

Depending on your organization's entitlements, the server may advertise additional tools — a vulnerability listing, for instance, where that feature is enabled. Run `/mcp` in Claude Code to see the tool list your own token receives.

### list_repos

Lists the repositories your token can reach, through the registry's `/v2/_catalog` endpoint. The registry offers no server-side name filtering, so to find a specific repository, an MCP client must page through the whole list and filter the results itself.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `page_size` | integer | no | Repositories per page (default 50, max 200) |
| `cursor` | string | no | The last repository name from the previous page; omit to start at the first page |

The cursor here is a repository name rather than an opaque token, unlike the other `list_*` tools on this server.

### list_tags

Lists the tags in one repository. Each call requests a single page from the registry, so a repository with thousands of tags responds as quickly as a small one.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `repo` | string | yes | Repository name without the registry host, for example `chainguard/python` |
| `page_size` | integer | no | Tags per page (default 50, max 200) |
| `cursor` | string | no | The `next_cursor` from the previous page |
| `include_digest_tags` | boolean | no | Include the `sha256-` prefixed tags that Cosign uses for signatures, attestations, and SBOMs (default `false`) |

Digest tags are omitted by default because they outnumber an image's real tags by a wide margin. Set `include_digest_tags=true` only when you are looking for the attachment tags themselves.

### get_manifest

Fetches an OCI manifest by tag or digest. The server returns the manifest body as a raw JSON string, which preserves the exact bytes the registry computed the digest over.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `repo` | string | yes | Repository name without the registry host |
| `reference` | string | yes | A tag such as `latest`, or a digest such as `sha256:...`. Prefer digests for content-addressable lookups. |

For a multi-architecture tag this returns the image *index*, whose `manifests` array names the per-architecture children. The index's `annotations` carry useful metadata, including `org.opencontainers.image.created` — which is how you find out when an image was built.

### get_config

Fetches the OCI image config: the build-time description of the image's entrypoint, environment, working directory, and user.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `repo` | string | yes | Repository name without the registry host |
| `reference` | string | yes | Tag or manifest digest |
| `architecture` | string | no | Which child manifest to descend into when the reference resolves to a multi-arch index (default `amd64`) |

### get_sbom

Fetches the signed SPDX SBOM attestation (`predicateType` `https://spdx.dev/Document`). Each `predicate` in the response is the raw SPDX document exactly as it was signed.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `repo` | string | yes | Repository name without the registry host |
| `reference` | string | yes | Tag or manifest digest |
| `architecture` | string | no | Descend into this architecture's child manifest. Omit to read the attestation attached to the reference itself — the index, for a multi-arch tag. |

The server refuses a document larger than 8192 KB outright rather than truncating it; the error names the size and the `cosign` command that fetches the file directly. Use `list_sbom_packages` when you only need the package list. An image with no SBOM attestation returns an empty `attestations` list rather than an error.

### list_sbom_packages

Pages through the packages in an image's SPDX SBOM, returning package names, versions, PURLs, licenses, and SPDX purposes without pulling the whole document into context.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `repo` | string | yes | Repository name without the registry host |
| `reference` | string | yes | Tag or manifest digest |
| `architecture` | string | no | Descend into this architecture's child manifest |
| `page_size` | integer | no | Packages per page (default 50, max 200) |
| `cursor` | string | no | The `next_cursor` from the previous page |

{{< alert context="warning" >}}
**Pass `architecture` to get real packages.** Omitting it on a multi-architecture tag reads the *index*-level SBOM, which describes the index and its child manifests rather than the software inside the image — for `chainguard/python:latest` that is three entries. Passing `architecture=amd64` reads the per-architecture SBOM instead, which for the same image holds 134.
{{< /alert >}}

The package list mixes several kinds of entry, distinguishable by their `purpose` and `purl`:

- `CONTAINER` — the image and its layer descriptors, with `pkg:oci/...` PURLs
- `OPERATING_SYSTEM` and `APPLICATION` — the Wolfi base and its APK packages, with `pkg:apk/wolfi/...` PURLs
- `INSTALL` — the melange build definitions that produced those packages
- `SOURCE` — the upstream source a package was built from, such as a CPython commit
- `FILE` — individual files the SBOM records

The `OPERATING_SYSTEM` and `APPLICATION` entries are the OS packages most readers are looking for. The OCI descriptors sort first, so the APK packages start after about a dozen `CONTAINER` rows on the first page.

### get_apko_config

Fetches the apko image-configuration attestation (`predicateType` `https://apko.dev/image-configuration`) — the declarative build-time description of the image's contents, accounts, entrypoint, and environment.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `repo` | string | yes | Repository name without the registry host |
| `reference` | string | yes | Tag or manifest digest |
| `architecture` | string | no | Descend into this architecture's child manifest |

### get_provenance

Fetches the SLSA build provenance attestation (`predicateType` `https://slsa.dev/provenance/v1`), describing the build that produced the image.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `repo` | string | yes | Repository name without the registry host |
| `reference` | string | yes | Tag or manifest digest |
| `architecture` | string | no | Descend into this architecture's child manifest |

The predicate's `buildDefinition.internalParameters` pins every package version that went into the image, and `runDetails.builder` names the builder and its version. This makes `get_provenance` a fast way to read exact package versions without paging through an SBOM.

## Example usage

Sample exchanges from a Claude Code session with `cg-oci` connected. You don't call the tools yourself — you describe what you want, and the AI tool decides which calls to make. Images are rebuilt often, so your answers will differ.

```Prompt
What tags are available for chainguard/python?
```

```output
  Called cg-oci (ctrl+o to expand)

● The chainguard/python repository exposes two tags: latest and
  latest-dev. Version-specific tags such as 3.12 live in an entitled
  namespace rather than the public chainguard/ one.
```

```Prompt
When was chainguard/python:latest built, and what Python version is in it?
```

```output
  Called cg-oci (ctrl+o to expand)

● chainguard/python:latest was built on 2026-09-20. Its build provenance
  pins the python-3.14 package, so latest is currently Python 3.14.
```

```Prompt
What OS packages are in the amd64 build of chainguard/python:latest?
```

```output
  Called cg-oci (ctrl+o to expand)

● The amd64 image's SBOM lists 134 entries. The APK packages include
  wolfi-baselayout, glibc, openssl's libcrypto3 and libssl3, sqlite-libs,
  and python-3.14 itself.
```

## Troubleshooting

| Symptom | What it means | What to do |
| ----- | ----- | ----- |
| `MANIFEST_UNKNOWN: Unknown manifest` | The repository is readable but that tag or digest is not. Most often the tag genuinely doesn't exist in the namespace you're reading — for example `chainguard/python:3.12`, where public `chainguard/*` repositories carry only `latest` and `latest-dev`. | Call `list_tags` on the repository to see the tags your token can actually read, then use one of those. |
| `FORBIDDEN: Forbidden` | Your token cannot read the repository at all. The registry returns this for a repository that doesn't exist and for one you aren't entitled to, without distinguishing them. | Confirm the repository name with `list_repos`, and check your organization's entitlement for it. |
| Server shows as not connected in `claude mcp list` | OAuth was never completed, or the token expired. Claude Code's tokens against the Chainguard issuer last about an hour and carry no refresh token. | Run `/mcp`, select **cg-oci**, and authenticate again. To stop re-authenticating, switch to the [`chainctl` helper](/platform/mcp-servers/overview/#authenticate-with-chainctl-instead-of-a-browser). |
| `401 invalid token` when using the `chainctl` helper | The audience was registered as a bare hostname. MCP audiences must include the `/mcp` path. | Run `chainctl auth login --audience=https://cgr.dev/mcp` and try again. |
| `no chainctl token for audience ...` | The helper script ran but that audience was never logged in. | Run the `chainctl auth login` command the error prints. |
| An SBOM request is refused for size | The SPDX document exceeds the server's 8192 KB ceiling. Documents are never truncated. | Use `list_sbom_packages` instead, or fetch the file with the `cosign` command named in the error. |
| `list_sbom_packages` returns only two or three entries | The call read the index-level SBOM rather than a per-architecture one. | Pass `architecture=amd64` (or `arm64`). |
| The AI tool can't find an image you know exists | It may be searching `list_repos`, which reflects your token rather than the public catalog, and offers no server-side name filter. | Name the repository explicitly, as `chainguard/<name>`, or look it up in the [Containers directory](https://images.chainguard.dev/). |

## Next steps

- [`cg-apk`](/platform/mcp-servers/cg-apk/) — search the Wolfi package index and read package SBOMs and build recipes
- [`cg-versions`](/platform/mcp-servers/cg-versions/) — check upstream releases and end-of-life dates
- [`cg-api`](/platform/mcp-servers/cg-api/) — query organizations, IAM, and registry metadata through the platform API
- [Chainguard MCP servers overview](/platform/mcp-servers/overview/) — the full set, and the `chainctl` authentication recipe
