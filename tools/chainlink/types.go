/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"net/url"
	"regexp"
	"sync"

	"github.com/yuin/goldmark/parser"
)

type results struct {
	Checked   []link // `json:"checked"`
	Unchecked []link // `json:"unchecked"`
	json      []byte
}

type linkAccumulator struct {
	Links map[string]link
	mu    *sync.Mutex
}

type filepathWalker struct {
	paths []string
}

type pathWalker struct {
	path     string
	rawBytes []byte // the bytes read from a file
}

type nodeWalker struct {
	path     string
	rawBytes *[]byte // the bytes read from a file
	parser   *parser.Parser
}

type ignoreURLs struct {
	URLS            []string `json:"urls"`
	Regexps         []string `json:"regexps"`
	compiledRegexps []*regexp.Regexp
}

type link struct {
	URL            *url.URL               `json:"url"`
	FullURL        string                 `json:"fullurl"`
	Status         int                    `json:"status"`
	Parents        map[string]interface{} `json:"parents"`
	rawDestination []byte
}
