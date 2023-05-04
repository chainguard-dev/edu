## Purpose

This tool is designed to parse Markdown files, scan for links, and then make HTTP requests to them to determine their status.

### Running

```
go run . -contentDir ../../content
```

Results will be in `results.json` unless otherwise specified with `-resultsFile` flag.

### Parsing Results

Parse the resulting json for checked URLs that 404:

```
jq '[.Checked [] | select(.status == 404) | {(.url.Path): {"pages":(.parents |keys)}}]' results.json
```

And get a list of relative/bad URLs that were not checked:

```
jq '[.Unchecked [] | {(.url.Path): {"pages":(.parents |keys)}}]' results.json
```

### Errata

There is a bug with the unchecked URLs regex, which seems to only pick up a single ../ URL. It should also find ./ URLs, and URLs with no leading /. There are a number of files with these kinds of URLs in the content directory.

The types are just a naive first pass and need a refactor, especially the accumulator logic.
