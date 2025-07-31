## Purpose

This tool is designed to parse Markdown or HTML files, scan for links, and then make HTTP requests to them to determine their status.

### Running

```
go run . -contentDir ../../content
```

Results will be in `results.json` unless otherwise specified with `-resultsFile` flag.

### Flags

```
  -checkAll
    	Check all detected URLs, or those belonging to -hostname
  -contentDir string
    	Path to directory with markdown (.md suffixed) files to scan (default "./content")
  -extractOnly
    	Only extract URLs, don't check them
  -fileType string
    	Type of files to scan (md or html). md is more accurate (default "md")
  -hostname string
    	Hostname to prepend to relative URLs (default "edu.chainguard.dev")
  -ignoreFile string
    	Path to json file with a list of URLs and regexes to not check (default "ignore.json")
  -method HEAD
    	HTTP method to use - HEAD or `GET` (default "HEAD")
  -resultsFile string
    	Path to json file with results of HTTP requests (default "results.json")
  -scheme http
    	Scheme to use with hostname. http or `https` (default "https")
  -followRedirects
    	Follow HTTP redirects to check final destination (default true)
```

### Redirect Support

By default, chainlink follows HTTP redirects (301/302) and validates the final destination URL. This helps identify:
- URLs that redirect to 404 pages
- Broken redirect chains
- URLs that should be updated to their final destinations

The `-followRedirects` flag controls this behavior:
- `true` (default): Follows redirects and checks the final destination
- `false`: Only checks the initial URL without following redirects

When redirects are followed, the results include:
- `finalurl`: The final URL after all redirects (if different from the original)
- `redirect_path`: An array showing the complete redirect chain

### Parsing Results

Parse the resulting json for checked URLs that 404:

```
jq '[.checked [] | select(.status == 404) | {(.url.Path): {"pages":(.files |keys)}}]' results.json
```

And get a list of relative/bad URLs that were not checked:

```
jq '[.unchecked [] | {(.url.Path): {"pages":(.files |keys)}}]' results.json
```

Find URLs that redirect and show their final destinations:

```
jq '[.checked [] | select(.finalurl) | {original: .url, final: .finalurl, status: .status}]' results.json
```

### Errata

The types are just a naive first pass and need a refactor, especially the accumulator logic.

The `ignoreURLs.appendIgnores()` function panics, so isn't used. Ignored URLs are still printed out.
