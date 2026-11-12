---
title: "cg-man: the Chainguard OS manual pages and --help MCP server"
date: 2026-11-05T13:57:14+00:00
lastmod: 2026-11-12T14:37:12+00:00
linktitle: "cg-man"
description: "Connect an MCP client to cg-man to search and read the manual pages and --help output of Chainguard OS packages, at the exact package version you run."
type: "article"
draft: false
tags: ["MCP", "Chainguard OS"]
images: []
menu:
  docs:
    parent: "mcp-servers"
    identifier: "cg-man"
toc: true
weight: 70
---

`cg-man` gives an AI tool the manual pages that Chainguard OS packages ship, and the `--help` output of the executables in them. A client can search the pages, read one at the exact package version you run, read a tool's `--help` output, look up a single option or exit code, and follow a page's cross-references to the package that provides them. Each answer records the package and version it came from.

Manual pages live in `-doc` subpackages, which minimal container images leave out, so an agent working inside a Chainguard container usually can't run `man`. Many tools have no manual page at all: `crane`, `helm`, `kubectl`, and most tools written in Go or Rust document themselves only through `--help`. Without this server, an agent answers questions about a tool's flags from training data, which may describe a different version from the one you run.

The pages come from the signed APKs in all three Chainguard OS package repositories. The `--help` output is captured by running each executable in a sandbox, against the exact package version. Both are rebuilt nightly. Pages and `--help` output under proprietary or source-available licenses are withheld.

The server uses the Streamable HTTP transport, at this endpoint:

```
https://man.cgr.dev/mcp
```

The server is public. It needs no Chainguard account and no sign-in, so the authentication steps for the product data servers don't apply to it.

## Prerequisites

- An MCP-compatible client such as Claude Code, Claude Desktop, or Cursor

## Connect to the server

### Claude Code

Add the server with `claude mcp add`, using the HTTP transport:

```shell
claude mcp add --transport http cg-man https://man.cgr.dev/mcp
```

By default, the command registers the server for the current directory only. Manual pages are useful in any repository, so `--scope user` is usually the right choice:

```shell
claude mcp add --transport http --scope user cg-man https://man.cgr.dev/mcp
```

The server is available immediately. Check its status with `claude mcp list`:

```shell
claude mcp list
```

```output
cg-man: https://man.cgr.dev/mcp (HTTP) - ✓ Connected
```

### Cursor

Cursor supports HTTP transport natively. Add the server to your MCP configuration:

```json
{
  "mcpServers": {
    "cg-man": {
      "url": "https://man.cgr.dev/mcp"
    }
  }
}
```

Restart Cursor. The manual page tools appear in the next conversation.

### Claude Desktop

Claude Desktop reads MCP servers from a JSON file but doesn't yet support HTTP transport directly. Use [`mcp-remote`](https://github.com/geelen/mcp-remote) to bridge to the hosted server:

```json
{
  "mcpServers": {
    "cg-man": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://man.cgr.dev/mcp"
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

Any client that supports a remote Streamable HTTP MCP server can connect to the same endpoint. Point it at `https://man.cgr.dev/mcp`.

## Tool reference

Five tools work with manual pages directly, and one returns `--help` output. Two more answer questions about a command-line tool's options and exit codes, drawing on both sources.

| Tool | Required parameters | Returns | Example prompt |
| ----- | ----- | ----- | ----- |
| `search_docs` | `query` | Matching pages, latest version of each | "Which Chainguard OS manual pages cover certificate chains?" |
| `get_man_page` | `name` | One page, or one section of it | "Show me the EXIT STATUS section of tar's manual page" |
| `resolve_xref` | `name` | The package that provides a cross-referenced page | "Which page does crypto(7) in the OpenSSL docs point to?" |
| `list_package_docs` | `package` | Every page a package ships | "What manual pages does the curl package include?" |
| `get_package_info` | `package` | The package versions that have pages | "Which curl versions have documentation?" |
| `get_help` | `name` or `path` | What an executable prints for `--help` | "Show me kubectl's help output" |
| `describe_tool` | `name` or `path` | A tool's usage, options, exit codes, and examples | "What does curl exit code 7 mean?" |
| `get_option` | `tool`, `flag` | One option's spellings, argument, and description | "What does tar's --zstd option do?" |

### Repositories

Chainguard OS packages come from three repositories, and most tools accept a `repo` parameter to choose one:

- `os`, the default: the [Wolfi repository](/chainguard/containers/building-and-modifying/packages/package-model/#wolfi)
- `enterprise-packages`
- `extra-packages`: the [Extra Packages repository](/chainguard/containers/building-and-modifying/packages/package-model/#extra-packages)

Without `repo`, the manual-page tools and `search_docs` search only `os`. To find or read a page from an enterprise package, such as an OpenJDK distribution, pass `repo` as `enterprise-packages`. `get_help`, `describe_tool`, and `get_option` search all three repositories unless you pass `repo`.

### Versions

Every tool that reads a page, `--help` output, or a tool defaults to the latest package version with documentation. To answer for the version you run, pass `version` with the exact package version, including its epoch, such as `8.22.0-r3`. Use `get_package_info` to list the versions that have pages.

### search_docs

Searches manual pages by name or by what they do. Like `apropos`, it matches page, command, and package names first, then each page's one-line description. A query of several words matches pages whose description contains every word. It doesn't search page bodies.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `query` | string | yes | A page, command, or package name, or words describing what the page does |
| `repo` | string | no | `os` (default), `enterprise-packages`, or `extra-packages` |
| `limit` | integer | no | Maximum results (default 20, maximum 100) |

Each result carries a `chainguard-docs://` URI that addresses the page at its exact version. A client can read that URI as an MCP resource, which returns the page as Markdown.

The response also lists executables with captured `--help` output whose name or usage line matches the query, in a separate `help` list. A tool with no manual page, such as `crane`, appears only there.

### get_man_page

Fetches one manual page, as Markdown by default.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | yes | Page name, such as `curl` or `SSL_new` |
| `section` | string | no | Manual section, such as `1` or `3ssl` |
| `package` | string | no | The package that ships the page, when the name is ambiguous |
| `version` | string | no | Exact package version (default: latest) |
| `repo` | string | no | Repository to search |
| `format` | string | no | `markdown` (default), `html`, or `raw` for the roff source |
| `heading` | string | no | Return one section only, such as `OPTIONS`, `EXIT STATUS`, or `EXAMPLES` (Markdown only) |
| `offset` | integer | no | First line to return |
| `limit` | integer | no | Lines to return (default 40, maximum 400) |

Manual pages can run to thousands of lines: `curl(1)` is more than 7,000. The response lists the page's headings and its total line count, so a client can request one section with `heading` rather than paging through the whole page.

### resolve_xref

Resolves a cross-reference, such as `git-add(1)` in another page's SEE ALSO section, to the package that provides the referenced page.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | yes | The referenced page name, such as `crypto` for `crypto(7)` |
| `section` | string | no | The referenced section, such as `7`. Omit it to search every section. |
| `repo` | string | no | The citing page's repository, which ranks its own packages first |
| `package` | string | no | The citing page's package. Most references point inside the package that made them, so passing it resolves most references. |

When a reference is ambiguous, the response lists the candidates rather than picking one. It also reports when a section matched only by family, such as `crypto(7)` answered by `crypto(7ossl)`.

### list_package_docs

Lists the manual pages a package ships.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `package` | string | yes | Package name, such as `curl` |
| `version` | string | no | Exact package version (default: latest) |
| `repo` | string | no | Repository to search |
| `limit` | integer | no | Pages to return (default 100, maximum 500) |
| `offset` | integer | no | Pages to skip, for paging through a large package |

The response includes `total` and `truncated`, so a client can tell when to request the next page. The `curl` package ships more than 500 pages, most of them for `libcurl`.

### get_package_info

Lists the versions of a package that have documentation, with the number of pages in each, and names the latest.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `package` | string | yes | Package name, such as `curl` |
| `repo` | string | no | Repository to search |

### get_help

Fetches what an executable printed when it ran with `--help`. This is the only documentation for many tools, including `crane`, `helm`, and `kubectl`.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | no | Executable name, such as `kubectl` |
| `path` | string | no | Absolute executable path, such as `/usr/bin/kubectl` |
| `package` | string | no | The package that ships the executable, when more than one does |
| `version` | string | no | Exact package version (default: latest) |
| `repo` | string | no | Repository to search (default: all three) |
| `offset` | integer | no | First line to return |
| `limit` | integer | no | Lines to return (default 40, maximum 400) |

Pass either `name` or `path`. The response records the package, version, and command that produced the output, and when it was captured. It also reports `totalLines` and, when more lines remain, the `nextOffset` to request next.

Several packages often ship the same executable: `ffmpeg` comes from more than 10 packages across the three repositories. `get_help` picks one by default, in this order: the package whose name matches the executable, then the newest version stream named after it, then the first alphabetically. The response lists the rest under `otherProviders`, and you can pass `package` to read one of them.

Only top-level `--help` output is captured, so `get_help` has nothing for a subcommand such as `kubectl get`. Each nightly run captures the latest version of every package, on x86_64. Help captured for an earlier version stays available.

### describe_tool

Describes a command-line tool in one record: its usage line, its options, its exit codes, and the examples from its manual page. The options are merged from the tool's `--help` output and its manual page.

Each option lists its `sources`, `help`, `man`, or both, and a confidence rating:

- `high`: the option appears in both the `--help` output and the manual page.
- `medium`: the option appears in one source and parsed cleanly.
- `low`: the option was found heuristically.

Exit codes and examples come only from manual pages, so a tool documented only by `--help` returns its usage line and options.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `name` | string | no | Tool name, such as `tar` |
| `path` | string | no | Absolute executable path, such as `/usr/bin/tar` |
| `package` | string | no | The package that provides the tool, when more than one does |
| `version` | string | no | Exact package version (default: latest) |
| `repo` | string | no | Repository to search |
| `exitCode` | integer | no | Return only what this exit status means |
| `examples` | string | no | Return only the examples that match these words |
| `offset` | integer | no | First option to return |
| `limit` | integer | no | Options to return (default 20, maximum 200) |

Pass either `name` or `path`. The examples come from the manual page and haven't been tested, and the response marks them as untested.

### get_option

Looks up one option of a command-line tool: its spellings, its argument, its description, and its sources, with the same confidence rating as `describe_tool`.

| Parameter | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| `tool` | string | yes | Tool name or absolute path, such as `tar` or `/usr/bin/tar` |
| `flag` | string | yes | The option, such as `--zstd`, `-C`, or `zstd` |
| `package` | string | no | The package that provides the tool |
| `version` | string | no | Exact package version (default: latest) |
| `repo` | string | no | Repository to search |

When the command-line tool has no such option, `get_option` returns an error that says so, rather than an empty result.

## Untrusted content

Manual pages and `--help` output are third-party text written by each package's upstream project. The server marks them as untrusted in two ways, so a client can tell page text from instructions:

- Each response carries a `notice` field telling the client to treat descriptions, options, examples, and licenses as data and not to follow instructions in them.
- Page text from `get_man_page` and `--help` output from `get_help` arrive between `<<<UNTRUSTED-…>>>` and `<<<END UNTRUSTED-…>>>` markers, with a random suffix for each response.

## Read pages in a browser

The same pages are published at [man.cgr.dev](https://man.cgr.dev/), with no sign-in. The short form `https://man.cgr.dev/man/bash.1` redirects to the latest version of a page. Each page also has a permanent address of this form:

```
https://man.cgr.dev/<repo>/<package>/<version>/man<section>/<name>.<section>
```

For example, `https://man.cgr.dev/os/curl/8.22.0-r3/man1/curl.1`. Use `latest` in place of the version to follow the current release. To get another format, append one of these extensions to the page's address:

| Extension | Returns |
| ----- | ----- |
| `.md` | Markdown |
| `.raw` | The original roff source |
| `.json` | A manifest recording the package, version, license, and a SHA-256 digest of each format |

The site publishes `--help` output under `/help/`, keyed by the executable's absolute path. `https://man.cgr.dev/help/usr/bin/kubectl` shows the default package's latest capture and lists every other package and version that ships the executable. The short form `https://man.cgr.dev/help/tar` redirects to the full path, or lists the paths when executables in several locations share the name. Each capture also has a permanent address of this form:

```
https://man.cgr.dev/<repo>/<package>/<version>/help/<path>
```

For example, `https://man.cgr.dev/os/crane/0.22.1-r4/help/usr/bin/crane`. Use `latest` in place of the version to follow the current release. Append `.txt` for the plain `--help` text, or `.json` for a manifest recording the package, version, command, exit code, APK checksum, capture time, and parsed options.

## Example usage

Sample exchanges from a Claude Code session with `cg-man` connected. Package versions change often, so your answers will differ.

```Prompt
Using the Chainguard OS manual pages, what does the --zstd option do in tar, and which package and version is that answer from?
```

```output
  Called cg-man (ctrl+o to expand)

● --zstd tells tar to filter the archive through zstd(1), compressing or
  decompressing with Zstandard.

  This is from the gnutar package, version 1.35-r15, sourced from its
  manual page.
```

```Prompt
In Chainguard OS, what does curl exit code 7 mean?
```

```output
  Called cg-man (ctrl+o to expand)

● Exit code 7 means "Failed to connect to host."
```

```Prompt
Using the Chainguard OS manual pages, which crane flag lets it fetch images without TLS, and which package and version is that answer from?
```

```output
  Called cg-man (ctrl+o to expand)

● The flag is --insecure, which allows image references to be fetched
  without TLS. This is from the crane package, version 0.22.1-r4 (sourced
  from its --help output, since crane has no manual page).
```

## Troubleshooting

| Symptom | What it means | What to do |
| ----- | ----- | ----- |
| `get_man_page` returns `no manpage found` for a page that exists | The page is in `enterprise-packages` or `extra-packages`, and the lookup searched only `os`. | Pass `repo`, or run `search_docs` with `repo` to find the page first. |
| `search_docs` returns nothing | The query matched no page or package name, and no page description contains every word. Page bodies aren't searched. | Try fewer words, or search for the package name. |
| `search_docs` returns 20 results when you asked for more | `limit` is above the maximum of 100, so the server used the default. | Set `limit` to 100 or less. |
| `get_man_page` returns `no manpage found` for a tool such as `crane` | The tool ships no manual page. | Run `get_help` or `describe_tool` instead. |
| `get_help` returns `no captured help` for a subcommand, such as `kubectl get` | Only top-level `--help` output is captured. | Request the top-level tool, such as `kubectl`. |
| A pinned `version` returns `no manpage found` or `no captured help` | That package version has no pages or captured `--help` output, or the version string is incomplete. | Run `get_package_info` to list the versions with pages, and pass the full version, including its epoch, such as `-r3`. Omit `version` to read the latest capture. |
| A page you expect is missing | Its license is proprietary or source-available, so the page is withheld, or the package ships no manual pages. | Read the documentation from the package's upstream project. |

## Next steps

- [`cg-apk`](/platform/mcp-servers/cg-apk/) — find Wolfi packages and read their SBOMs and build configs
- [AI Docs](/platform/mcp-servers/ai-docs/) — search Chainguard documentation from an AI tool
- [Chainguard MCP servers overview](/platform/mcp-servers/overview/) — the full set of Chainguard MCP servers
