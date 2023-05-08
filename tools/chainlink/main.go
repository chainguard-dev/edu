/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"flag"
	"log"
	"path/filepath"
	"regexp"
	"sync"
)

func init() {
	flag.StringVar(&hostname, "hostname", "edu.chainguard.dev", "Hostname to prepend to relative URLs")
	flag.StringVar(&scheme, "scheme", "https", "Scheme to use with hostname. `http` or `https`")
	flag.StringVar(&httpMethod, "method", "HEAD", "HTTP method to use - `HEAD` or `GET`")
	flag.StringVar(&ignoreFile, "ignoreFile", "ignore.json", "Path to json file with a list of URLs and regexes to not check")
	flag.StringVar(&resultsFile, "resultsFile", "results.json", "Path to json file with results of HTTP requests")
	flag.StringVar(&contentDir, "contentDir", "./content", "Path to directory with markdown (.md suffixed) files to scan")
	flag.StringVar(&fileType, "fileType", "md", "Type of files to scan (md or html). md is more accurate")

	flag.BoolVar(&checkAll, "checkAll", false, "Check all detected URLs, or those belonging to -hostname")
	flag.BoolVar(&extractMode, "extractOnly", false, "Only extract URLs, don't check them")

	flag.Parse()

	// won't match anything like `../` or `./` or non-leading `/` URLs
	// unmatched urls will go into the unchecked result accumulator
	correctURLregex = regexp.MustCompile(`^(http|https|\/).+`)

	if err := ignores.read(); err != nil {
		log.Fatalf("error loading ignores json: %v\n", err)
	}
	if err := ignores.compile(); err != nil {
		log.Fatalf("error compiling ignores json: %v\n", err)
	}
}

func main() {
	// start with a scan of contentDir for files
	w := filepathWalker{}
	if err := filepath.WalkDir(contentDir, w.walkDirFunc); err != nil {
		log.Fatalf("error scanning %s: %v\n", contentDir, err)
	}
	log.Printf("discovered %d files in %s directory\n", len(w.paths), contentDir)

	switch fileType {
	case "md":
		if err := processMarkdown(&w); err != nil {
			log.Fatalf("error processing markdown: %v\n", err)
		}
	case "html":
		if err := processHTML(&w); err != nil {
			log.Fatalf("error processing html: %v\n", err)
		}
	}

	if !extractMode {
		// make HTTP requests to each detected link
		var wg = &sync.WaitGroup{}
		for _, l := range checked.Links {
			wg.Add(1)
			l.check(wg)
		}
		wg.Wait()
	}

	// marshal the results to json
	r := results{}
	if err := r.marshal(); err != nil {
		log.Fatalf("error marshaling results: %v\n", err)
	}

	// save the file to resultsFile
	if err := r.write(); err != nil {
		log.Fatalf("error writing results json file: %v\n", err)
	}
}
