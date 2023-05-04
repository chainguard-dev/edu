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
	checked   = linkAccumulator{Links: make(map[string]link), mu: &sync.Mutex{}}
	unchecked = linkAccumulator{Links: make(map[string]link), mu: &sync.Mutex{}}

	hostname         = ""
	scheme           = ""
	httpMethod       = ""
	ignoreFile       = ""
	resultsFile      = ""
	crawlAll         = false
	contentDir       = ""
	relativeURLregex = &regexp.Regexp{}

	ignores = ignoreURLs{}
)

func init() {
	flag.StringVar(&hostname, "hostname", "edu.chainguard.dev", "Hostname to prepend to relative URLs")
	flag.StringVar(&scheme, "scheme", "https", "Scheme to use with hostname. `http` or `https`")
	flag.StringVar(&httpMethod, "method", "HEAD", "HTTP method to use - `HEAD` or `GET`")
	flag.StringVar(&ignoreFile, "ignoreFile", "ignore.json", "Path to json file with a list of URLs and regexes to not check")
	flag.StringVar(&resultsFile, "resultsFile", "results.json", "Path to json file with results of HTTP requests")
	flag.StringVar(&contentDir, "contentDir", "./content", "Path to directory with markdown (.md suffixed) files to scan")
	flag.BoolVar(&crawlAll, "crawlAll", false, "Crawl all detected, or only hostname URLs")
	flag.Parse()

	// looks for things like `../` or `./` or non-leading `/` URLs
	// matching urls will go into the unchecked result accumulator
	relativeURLregex = regexp.MustCompile(`^(\.\.\/|\./|a-zA-Z0-9)`)

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

	// make HTTP requests to each detected link
	var wg = &sync.WaitGroup{}
	for _, l := range checked.Links {
		wg.Add(1)
		l.check(wg)
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
// currently only md files are supported but can extend with -mode flag
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
		return fmt.Errorf("error walking markdown node: %v - %v\n", node, err)
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

	var l link
	l.rawDestination = node.(*ast.Link).Destination

	log.Println(string(l.rawDestination))

	if ignores.check(l.rawDestination) {
		return ast.WalkContinue, nil
	}

	// log errors, but don't include bad URLs in end results
	u, err := l.parseURL()
	if err != nil {
		log.Printf("bad url in %v: %v\n", n.path, string(l.rawDestination))
		return ast.WalkContinue, nil
	}

	var ok bool
	// missing a host according to parseURL so add to bad links
	// by checking if it is in the map, and inserting if it is not
	if u.Host == "" {
		if _, ok = unchecked.Links[string(l.rawDestination)]; !ok {
			l = link{URL: u, Parents: make(map[string]interface{})}
			l.Parents[n.path] = nil
			unchecked.Links[string(l.rawDestination)] = l
			return ast.WalkContinue, nil
		}
	}

	// found a good link, add to list of URLs to scan
	if l, ok = checked.Links[u.String()]; !ok {
		l = link{URL: u, Parents: make(map[string]interface{})}
	}

	// add file to link parents map for quick lookup
	if _, ok := l.Parents[n.path]; !ok {
		l.Parents[n.path] = nil
	}

	// add link to checked links map for scanning
	if _, ok := checked.Links[u.String()]; !ok {
		checked.Links[u.String()] = l
	}

	return ast.WalkContinue, nil
}

func (l *link) parseURL() (*url.URL, error) {
	rawURL := strings.Split(string(l.rawDestination), "#")[0]

	u, err := url.Parse(rawURL)
	if err != nil {
		return nil, fmt.Errorf("unable to parse link: %v: %v\n", string(l.rawDestination), err)
	}

	if relativeURLregex.MatchString(u.Path) {
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

	if !crawlAll {
		// this check is the default and ensures only fetching URLs
		// with the `-hostname` in them e.g. to only check
		// edu.chainguard.dev and nowhere else
		if ok, _ := regexp.MatchString(hostname, l.URL.String()); !ok {
			return
		}
	}

	localWg := sync.WaitGroup{}
	localWg.Add(1)

	go func() {
		defer localWg.Done()

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

	}()
	localWg.Wait()
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

func (i *ignoreURLs) check(link []byte) bool {
	// skip any URL in the ignore list of URLs and regexes
	for _, u := range i.URLS {
		if string(link) == u {
			fmt.Printf("ignoring %s\n", string(link))
			return true
		}
	}
	for _, re := range ignores.compiledRegexps {
		if re.Match(link) {
			fmt.Printf("ignoring %s\n", string(link))
			return true
		}
	}
	return false
}

func (r *results) write() error {
	return os.WriteFile(resultsFile, r.json, os.ModePerm)
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
