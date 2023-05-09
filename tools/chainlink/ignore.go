/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"encoding/json"
	"os"
	"regexp"
)

func (i *ignoreURLs) read() error {
	f, err := os.ReadFile(ignoreFile)
	if err != nil {
		return err
	}

	return json.Unmarshal(f, &ignores)
}

func (i *ignoreURLs) compile() error {
	for _, re := range i.Regexps {
		compiledRe, err := regexp.Compile(re)
		if err != nil {
			return err
		}
		i.compiledRegexps = append(i.compiledRegexps, compiledRe)
	}
	return nil
}

func (i *ignoreURLs) check(l string, path *string) bool {
	// skip any URL in the ignore list of URLs and regexes
	for _, u := range i.URLS {
		if l == u {
			//i.appendIgnores(l, path)
			return true
		}
	}
	for _, re := range ignores.compiledRegexps {
		if re.MatchString(l) {
			//i.appendIgnores(l, path)
			return true
		}
	}
	return false
}

// TODO: this panics for some reason, don't use for now
func (i *ignoreURLs) appendIgnores(l string, path *string) {
	var ok bool
	var il link // new link
	if il, ok = ignored.Links[l]; !ok {
		il = link{Files: make(map[string]interface{}), RawURL: l}
	}

	// add file to link files map for quick lookup
	if _, ok := il.Files[*path]; !ok {
		il.Files[*path] = nil
	}

	// add link to checked links map for scanning
	if _, ok := checked.Links[l]; !ok {
		checked.Links[l] = il
	}
}
