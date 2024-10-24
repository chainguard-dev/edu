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

var (
	// flags
	hostname    = ""
	scheme      = ""
	httpMethod  = ""
	ignoreFile  = ""
	resultsFile = ""
	checkAll    = false
	extractMode = false
	contentDir  = ""
	fileType    = ""
	jobs        = 10

	// url rules
	correctURLregex = &regexp.Regexp{}
	ignores         = ignoreURLs{}

	// url accumulators - should probably be fields of the results struct
	checked   = linkAccumulator{Links: make(map[string]link), mu: &sync.Mutex{}}
	unchecked = linkAccumulator{Links: make(map[string]link)}
	ignored   = linkAccumulator{Links: make(map[string]link)}
)

type results struct {
	Checked   []link `json:"checked"`
	Unchecked []link `json:"unchecked"`
	Ignored   []link `json:"ignored"`
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

// for markdown
type mdWalker struct {
	path     string
	rawBytes *[]byte // the bytes read from a file
	parser   *parser.Parser
}

// for html
type htmlWalker struct {
	path     string
	rawBytes *[]byte // the bytes read from a file
}

type ignoreURLs struct {
	URLS            []string `json:"urls"`
	Regexps         []string `json:"regexps"`
	compiledRegexps []*regexp.Regexp
}

type link struct {
	URL     *url.URL               `json:"url"`
	FullURL string                 `json:"fullurl"`
	Status  int                    `json:"status"`
	Files   map[string]interface{} `json:"files"`
	RawURL  string                 `json:"rawurl"`
}
