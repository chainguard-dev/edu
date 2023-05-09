/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"io/fs"
	"os"
	"strings"
)

// find slice of urls in a file add each to global map of urls
// including file path where url occurs
func (fp *filepathWalker) walkDirFunc(path string, d fs.DirEntry, _ error) error {
	if d.IsDir() {
		return nil
	}

	fp.paths = append(fp.paths, path)
	return nil
}

func (p *pathWalker) readFile() error {
	if !p.checkFileExtension() {
		return nil
	}

	b, err := os.ReadFile(p.path)
	if err != nil {
		return err
	}

	p.rawBytes = b
	return nil
}

// split path name to only scan specified files
// currently only md files are supported but can extend with a -mode flag
func (p *pathWalker) checkFileExtension() bool {
	pathSplit := strings.Split(p.path, ".")
	fType := pathSplit[len(pathSplit)-1][0:]

	return fType == fileType
}
