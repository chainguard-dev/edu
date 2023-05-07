/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io/fs"
	"log"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"sync"

	"github.com/yuin/goldmark"
	"github.com/yuin/goldmark/ast"
	"github.com/yuin/goldmark/text"
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

	// url rules
	correctURLregex = &regexp.Regexp{}
	ignores         = ignoreURLs{}

	// url accumulators - should probably be fields of the results struct
	checked   = linkAccumulator{Links: make(map[string]link), mu: &sync.Mutex{}}
	unchecked = linkAccumulator{Links: make(map[string]link)}
)

func init() {
	flag.StringVar(&hostname, "hostname", "edu.chainguard.dev", "Hostname to prepend to relative URLs")
	flag.StringVar(&scheme, "scheme", "https", "Scheme to use with hostname. `http` or `https`")
	flag.StringVar(&httpMethod, "method", "HEAD", "HTTP method to use - `HEAD` or `GET`")
	flag.StringVar(&ignoreFile, "ignoreFile", "ignore.json", "Path to json file with a list of URLs and regexes to not check")
	flag.StringVar(&resultsFile, "resultsFile", "results.json", "Path to json file with results of HTTP requests")
	flag.StringVar(&contentDir, "contentDir", "./content", "Path to directory with markdown (.md suffixed) files to scan")
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
	r := results{}
	// start with a scan of contentDir for files
	w := filepathWalker{}
	if err := filepath.WalkDir(contentDir, w.walkDirFunc); err != nil {
		log.Fatalf("error scanning %s: %v\n", contentDir, err)
	}
	log.Printf("discovered %d files in %s directory\n", len(w.paths), contentDir)

	// range over each file and extract links all in one go
	nodeParser := goldmark.New().Parser()
	for _, path := range w.paths {
		// find markdown files and read them
		p := pathWalker{path: path}
		if err := p.readFile(); err != nil {
			log.Fatalf("error reading file: %s - %v\n", p.path, err)
		}

		// parse found files into a goldmark ast, then extract links
		node := nodeWalker{path: p.path, rawBytes: &p.rawBytes, parser: &nodeParser}
		if err := node.scanMarkdown(); err != nil {
			log.Fatalf("error scanning markdown: %s - %v\n", node.path, err)
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
	if err := r.marshal(); err != nil {
		log.Fatalf("error marshaling results: %v\n", err)
	}

	// save the file to resultsFile
	if err := r.write(); err != nil {
		log.Fatalf("error writing results json file: %v\n", err)
	}
}

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

	return fType == "md"
}

func (n *nodeWalker) scanMarkdown() error {
	reader := text.NewReader(*n.rawBytes)
	p := *n.parser
	node := p.Parse(reader) // node is the root markdown ast.Node

	if err := ast.Walk(node, n.walkNodeFunc); err != nil {
		return fmt.Errorf("error walking markdown node: %v - %v", node, err)
	}

	return nil
}

func (n *nodeWalker) walkNodeFunc(node ast.Node, entering bool) (ast.WalkStatus, error) {
	if !entering {
		return ast.WalkContinue, nil
	}

	// only look for Link nodes
	if node.Kind() != ast.KindLink {
		return ast.WalkContinue, nil
	}

	var l link // link for parsing
	l.RawURL = string(node.(*ast.Link).Destination)
	if ignores.check(l.RawURL) {
		fmt.Printf("ignoring %v in %v\n", l.RawURL, n.path)
		return ast.WalkContinue, nil
	}

	// log errors, but don't include bad URLs in end results
	u, err := l.parseURL()
	if err != nil {
		log.Printf("bad url in %v: %v\n", n.path, l.RawURL)
		return ast.WalkContinue, nil
	}

	var ok bool
	var ul link // unchecked link
	// missing a host according to parseURL so add to unchecked links
	// by checking if it is in the map, and inserting if it is not
	if u.Host == "" {
		if _, ok = unchecked.Links[l.RawURL]; !ok {
			ul = link{URL: u, Files: make(map[string]interface{}), RawURL: l.RawURL}
			ul.Files[n.path] = nil
			unchecked.Links[l.RawURL] = ul
			return ast.WalkContinue, nil
		}
	}

	var nl link // new link
	// found a good link, add to list of URLs to scan
	if nl, ok = checked.Links[u.String()]; !ok {
		nl = link{URL: u, Files: make(map[string]interface{}), RawURL: l.RawURL}
	}

	// add file to link files map for quick lookup
	if _, ok := nl.Files[n.path]; !ok {
		nl.Files[n.path] = nil
	}

	// add link to checked links map for scanning
	if _, ok := checked.Links[u.String()]; !ok {
		checked.Links[u.String()] = nl
	}

	return ast.WalkContinue, nil
}

func (l *link) parseURL() (*url.URL, error) {
	u, err := url.Parse(l.RawURL)
	if err != nil {
		return nil, fmt.Errorf("unable to parse link: %v: %v", string(l.RawURL), err)
	}

	if !correctURLregex.MatchString(u.Path) {
		return u, nil
	}

	if u.Host == "" {
		u.Host = hostname
		u.Scheme = scheme
	}

	return u, nil
}

func (l *link) check(wg *sync.WaitGroup) {
	defer wg.Done()

	if !checkAll {
		// this check is the default and ensures only fetching URLs
		// with the `-hostname` in them e.g. to only check
		// edu.chainguard.dev and nowhere else
		if ok, _ := regexp.MatchString(hostname, l.URL.String()); !ok {
			return
		}
	}
	fmt.Printf("checking %v\n", l.URL.String())

	link, _ := checked.Links[l.URL.String()]

	req, err := http.NewRequest(httpMethod, l.URL.String(), nil)
	if err != nil {
		link.Status = http.StatusTeapot
		checked.mu.Lock()
		checked.Links[l.URL.String()] = link
		checked.mu.Unlock()
		fmt.Printf("client: could not create request to %v: %s\n", l.URL.String(), err)
		return
	}

	req.Header.Add("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0")
	req.Header.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("error requesting %v\n", err)
		link.Status = http.StatusNotFound
		checked.mu.Lock()
		checked.Links[l.URL.String()] = link
		checked.mu.Unlock()
		return
	}

	defer res.Body.Close()
	link.Status = res.StatusCode
	checked.mu.Lock()
	checked.Links[l.URL.String()] = link
	checked.mu.Unlock()
}

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

func (i *ignoreURLs) check(link string) bool {
	// skip any URL in the ignore list of URLs and regexes
	for _, u := range i.URLS {
		if link == u {
			return true
		}
	}
	for _, re := range ignores.compiledRegexps {
		if re.MatchString(link) {
			return true
		}
	}
	return false
}

func (r *results) marshal() error {
	for _, l := range unchecked.Links {
		l.FullURL = l.URL.String()
		r.Unchecked = append(r.Unchecked, l)
	}

	for _, l := range checked.Links {
		l.FullURL = l.URL.String()
		r.Checked = append(r.Checked, l)
	}

	var err error
	if r.json, err = json.MarshalIndent(r, "", "  "); err != nil {
		return err
	}

	return nil
}

func (r *results) write() error {
	return os.WriteFile(resultsFile, r.json, os.ModePerm)
}
