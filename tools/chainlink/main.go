/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"sync"

	"golang.org/x/sync/errgroup"
)

func init() {
	flag.StringVar(&hostname, "hostname", "edu.chainguard.dev", "Hostname to prepend to relative URLs")
	flag.StringVar(&scheme, "scheme", "https", "Scheme to use with hostname. `http` or `https`")
	flag.StringVar(&httpMethod, "method", "HEAD", "HTTP method to use - `HEAD` or `GET`")
	flag.StringVar(&ignoreFile, "ignoreFile", "ignore.json", "Path to json file with a list of URLs and regexes to not check")
	flag.StringVar(&resultsFile, "resultsFile", "results.json", "Path to json file with results of HTTP requests")
	flag.StringVar(&contentDir, "contentDir", "./content", "Path to directory with markdown (.md suffixed) files to scan")
	flag.StringVar(&fileType, "fileType", "md", "Type of files to scan (md or html). md is more accurate")
	flag.IntVar(&jobs, "jobs", 10, "Number of concurrent HTTP requests to make")

	flag.BoolVar(&checkAll, "checkAll", false, "Check all detected URLs, or those belonging to -hostname")
	flag.BoolVar(&extractMode, "extractOnly", false, "Only extract URLs, don't check them")

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
	flag.Parse()

	err := processContentDir()
	if err != nil {
		log.Fatalf("error processing contentDir: %v", err)
	}
}

func processContentDir() error {
	// if not a dir or some other error, stop right here
	if _, err := os.Stat(contentDir); err != nil {
		return fmt.Errorf("invalid contentDir: %v", err)
	}

	w := filepathWalker{}
	if err := filepath.WalkDir(contentDir, w.walkDirFunc); err != nil {
		return fmt.Errorf("error scanning %s: %w", contentDir, err)
	}
	log.Printf("discovered %d files in %s directory", len(w.paths), contentDir)

	switch fileType {
	case "md":
		if err := processMarkdown(&w); err != nil {
			return fmt.Errorf("error processing markdown: %w", err)
		}
	case "html":
		if err := processHTML(&w); err != nil {
			return fmt.Errorf("error processing html: %w", err)
		}
	}

	var mu sync.Mutex
	var errg errgroup.Group
	errg.SetLimit(jobs)
	if !extractMode {
		// make HTTP requests to each detected link
		for _, l := range checked.Links {
			l := l
			errg.Go(func() error {
				mu.Lock()
				defer mu.Unlock()
				l.check()
				return nil
			})
		}
		if err := errg.Wait(); err != nil {
			log.Fatalf("this should never happen: %v\n", err)
		}
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
	return nil
}
