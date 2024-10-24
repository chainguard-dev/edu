/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"fmt"
	"log"
	"net/http"
	"net/url"
	"regexp"
)

func (l *link) processLink(path *string) {
	if ignores.check(l.RawURL, path) {
		fmt.Printf("ignoring %v in %v\n", l.RawURL, path)
		return
	}

	// log errors, but don't include bad URLs in end results
	u, err := l.parseURL()
	if err != nil {
		log.Printf("bad url in %v: %v\n", path, l.RawURL)
		return
	}

	var ok bool
	var ul link // unchecked link
	// missing a host according to parseURL so add to unchecked links
	// by checking if it is in the map, and inserting if it is not
	if u.Host == "" {
		if _, ok = unchecked.Links[l.RawURL]; !ok {
			ul = link{URL: u, Files: make(map[string]interface{}), RawURL: l.RawURL}
			ul.Files[*path] = nil
			unchecked.Links[l.RawURL] = ul
			return
		}
	}

	var nl link // new link
	// found a good link, add to list of URLs to scan
	if nl, ok = checked.Links[u.String()]; !ok {
		nl = link{URL: u, Files: make(map[string]interface{}), RawURL: l.RawURL}
	}

	// add file to link files map for quick lookup
	if _, ok := nl.Files[*path]; !ok {
		nl.Files[*path] = nil
	}

	// add link to checked links map for scanning
	if _, ok := checked.Links[u.String()]; !ok {
		checked.Links[u.String()] = nl
	}

	return
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

func (l *link) check() {
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
