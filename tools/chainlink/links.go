/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"crypto/tls"
	"fmt"
	"log"
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

// sanitizeURL removes newline and carriage return characters from URLs to prevent log injection
func sanitizeURL(u *url.URL) string {
	s := u.String()
	s = strings.ReplaceAll(s, "\n", "")
	s = strings.ReplaceAll(s, "\r", "")
	return s
}

func (l *link) processLink(path string) {
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
			ul.Files[path] = nil
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
	if _, ok := nl.Files[path]; !ok {
		nl.Files[path] = nil
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

	link, ok := checked.Links[l.URL.String()]
	if !ok {
		fmt.Printf("client: %v not found in checked links\n", l.URL.String())
		return
	}

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

	// Track redirect path
	var redirectPath []string

	// Create a custom HTTP client that follows redirects
	client := &http.Client{
		CheckRedirect: func(req *http.Request, via []*http.Request) error {
			// Allow up to 10 redirects (Go's default)
			if len(via) >= 10 {
				return fmt.Errorf("stopped after 10 redirects")
			}

			// Track redirect URLs
			if len(via) == 0 {
				redirectPath = append(redirectPath, req.URL.String())
			} else {
				// Add the current request URL to redirect path
				redirectPath = append(redirectPath, req.URL.String())
				// Log redirect for debugging
				if followRedirects {
					fmt.Printf("redirect: %v -> %v\n", sanitizeURL(via[len(via)-1].URL), sanitizeURL(req.URL))
				}
			}

			// If not following redirects, stop after first redirect
			if !followRedirects {
				return http.ErrUseLastResponse
			}
			return nil
		},
	}

	res, err := client.Do(req)
	if err != nil {
		// Try fallback strategies for common network/protocol issues
		if shouldTryFallback(err) {
			fmt.Printf("HEAD request failed (%v), trying fallback strategies for %v\n", err, l.URL.String())

			// Strategy 1: Try GET request (some servers don't support HEAD properly)
			if httpMethod == "HEAD" {
				getReq, getErr := http.NewRequest("GET", l.URL.String(), nil)
				if getErr == nil {
					getReq.Header.Add("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0")
					getReq.Header.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")

					getRes, getErr := client.Do(getReq)
					if getErr == nil {
						defer getRes.Body.Close()
						fmt.Printf("GET fallback succeeded for %v (status: %d)\n", l.URL.String(), getRes.StatusCode)
						res = getRes
						err = nil
						goto processResponse
					}
				}
			}

			// Strategy 2: Try with no redirect following for redirect loop issues
			if isRedirectLoopError(err) {
				fmt.Printf("trying with no redirects for %v\n", l.URL.String())
				noRedirectClient := &http.Client{
					CheckRedirect: func(req *http.Request, via []*http.Request) error {
						return http.ErrUseLastResponse
					},
				}

				noRedirectReq, noRedirectErr := http.NewRequest(httpMethod, l.URL.String(), nil)
				if noRedirectErr == nil {
					noRedirectReq.Header.Add("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0")
					noRedirectReq.Header.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")

					noRedirectRes, noRedirectErr := noRedirectClient.Do(noRedirectReq)
					if noRedirectErr == nil {
						defer noRedirectRes.Body.Close()
						// Accept any non-error status (2xx, 3xx) as success
						if noRedirectRes.StatusCode >= 200 && noRedirectRes.StatusCode < 400 {
							fmt.Printf("no-redirect strategy succeeded for %v (status: %d)\n", l.URL.String(), noRedirectRes.StatusCode)
							res = noRedirectRes
							err = nil
							goto processResponse
						}
					}
				}
			}

			// Strategy 3: Try with relaxed TLS verification for certificate issues
			if isTLSError(err) {
				fmt.Printf("trying with relaxed TLS verification for %v\n", l.URL.String())
				relaxedClient := &http.Client{
					Transport: &http.Transport{
						TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
					},
					CheckRedirect: client.CheckRedirect,
				}

				relaxedReq, relaxedErr := http.NewRequest(httpMethod, l.URL.String(), nil)
				if relaxedErr == nil {
					relaxedReq.Header.Add("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0")
					relaxedReq.Header.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")

					relaxedRes, relaxedErr := relaxedClient.Do(relaxedReq)
					if relaxedErr == nil {
						defer relaxedRes.Body.Close()
						fmt.Printf("relaxed TLS verification succeeded for %v (status: %d)\n", l.URL.String(), relaxedRes.StatusCode)
						res = relaxedRes
						err = nil
						goto processResponse
					}
				}
			}
		}

		// If all fallbacks failed, mark as 404
		fmt.Printf("error requesting %v\n", err)
		link.Status = http.StatusNotFound
		checked.mu.Lock()
		checked.Links[l.URL.String()] = link
		checked.mu.Unlock()
		return
	}

processResponse:

	defer res.Body.Close()
	link.Status = res.StatusCode

	// Try fallbacks for certain status codes (like 405 Method Not Allowed)
	if shouldTryFallbackForStatus(res.StatusCode) {
		fmt.Printf("received status %d for %v, trying fallback strategies\n", res.StatusCode, l.URL.String())

		// Strategy: Try GET request if we got 405 (Method Not Allowed) with HEAD
		if res.StatusCode == http.StatusMethodNotAllowed && httpMethod == "HEAD" {
			getReq, getErr := http.NewRequest("GET", l.URL.String(), nil)
			if getErr == nil {
				getReq.Header.Add("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0")
				getReq.Header.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")

				getRes, getErr := client.Do(getReq)
				if getErr == nil {
					defer getRes.Body.Close()
					if getRes.StatusCode == http.StatusOK || (getRes.StatusCode >= 200 && getRes.StatusCode < 400) {
						fmt.Printf("GET fallback for method not allowed succeeded for %v (status: %d)\n", l.URL.String(), getRes.StatusCode)
						link.Status = getRes.StatusCode
						// Update final URL if the GET version had redirects
						if getRes.Request.URL.String() != l.URL.String() {
							link.FinalURL = getRes.Request.URL.String()
						}
					}
				}
			}
		}
	}

	// Store final URL and redirect path if redirects occurred
	if res.Request.URL.String() != l.URL.String() {
		link.FinalURL = res.Request.URL.String()
		link.RedirectPath = redirectPath
	}

	// If we got a 404 for a relative path without trailing slash, try with trailing slash
	if res.StatusCode == http.StatusNotFound && l.URL.Host == hostname && !strings.HasSuffix(l.URL.Path, "/") && l.URL.Path != "" {
		trailingSlashURL := *l.URL
		trailingSlashURL.Path = l.URL.Path + "/"

		fmt.Printf("404 for %v, trying with trailing slash: %v\n", l.URL.String(), trailingSlashURL.String())

		req2, err := http.NewRequest(httpMethod, trailingSlashURL.String(), nil)
		if err == nil {
			req2.Header.Add("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0")
			req2.Header.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")

			res2, err := client.Do(req2)
			if err == nil {
				defer res2.Body.Close()
				if res2.StatusCode == http.StatusOK || (res2.StatusCode >= 200 && res2.StatusCode < 400) {
					fmt.Printf("trailing slash version works! updating status from %d to %d\n", link.Status, res2.StatusCode)
					link.Status = res2.StatusCode
					// Update final URL if the trailing slash version worked
					if res2.Request.URL.String() != trailingSlashURL.String() {
						link.FinalURL = res2.Request.URL.String()
					}
				}
			}
		}
	}

	checked.mu.Lock()
	checked.Links[l.URL.String()] = link
	checked.mu.Unlock()
}

// shouldTryFallback determines if we should try fallback strategies based on the error
func shouldTryFallback(err error) bool {
	errStr := strings.ToLower(err.Error())

	// Network/protocol issues that might work with fallbacks
	return strings.Contains(errStr, "tls handshake timeout") ||
		strings.Contains(errStr, "certificate") ||
		strings.Contains(errStr, "x509") ||
		strings.Contains(errStr, "stopped after 10 redirects") ||
		strings.Contains(errStr, "timeout") ||
		strings.Contains(errStr, "connection refused") ||
		strings.Contains(errStr, "no such host")
}

// shouldTryFallbackForStatus determines if we should try fallback strategies based on status code
func shouldTryFallbackForStatus(statusCode int) bool {
	// Try fallbacks for method not allowed and other client errors that might work with different methods
	return statusCode == http.StatusMethodNotAllowed ||
		statusCode == http.StatusBadRequest ||
		statusCode == http.StatusForbidden
}

// isTLSError determines if the error is specifically a TLS/certificate issue
func isTLSError(err error) bool {
	errStr := strings.ToLower(err.Error())

	return strings.Contains(errStr, "certificate") ||
		strings.Contains(errStr, "x509") ||
		strings.Contains(errStr, "tls")
}

// isRedirectLoopError determines if the error is caused by too many redirects
func isRedirectLoopError(err error) bool {
	errStr := strings.ToLower(err.Error())

	return strings.Contains(errStr, "stopped after 10 redirects")
}
