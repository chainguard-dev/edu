/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"net/http"
	"net/http/httptest"
	"net/url"
	"sync"
	"testing"
)

func TestCheckWithRedirects(t *testing.T) {
	// Create a test server that redirects
	ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		switch r.URL.Path {
		case "/redirect-once":
			http.Redirect(w, r, "/final", http.StatusMovedPermanently)
		case "/redirect-chain":
			http.Redirect(w, r, "/redirect-chain-1", http.StatusFound)
		case "/redirect-chain-1":
			http.Redirect(w, r, "/redirect-chain-2", http.StatusFound)
		case "/redirect-chain-2":
			http.Redirect(w, r, "/final-chain", http.StatusFound)
		case "/final-chain":
			w.WriteHeader(http.StatusOK)
		case "/redirect-to-404":
			http.Redirect(w, r, "/not-found", http.StatusMovedPermanently)
		case "/not-found":
			w.WriteHeader(http.StatusNotFound)
		case "/final":
			w.WriteHeader(http.StatusOK)
		default:
			w.WriteHeader(http.StatusOK)
		}
	}))
	defer ts.Close()

	tests := []struct {
		name               string
		path               string
		followRedirects    bool
		expectedStatus     int
		expectFinalURL     bool
		expectRedirectPath bool
	}{
		{
			name:               "Follow single redirect",
			path:               "/redirect-once",
			followRedirects:    true,
			expectedStatus:     http.StatusOK,
			expectFinalURL:     true,
			expectRedirectPath: true,
		},
		{
			name:               "Don't follow redirect",
			path:               "/redirect-once",
			followRedirects:    false,
			expectedStatus:     http.StatusMovedPermanently,
			expectFinalURL:     false,
			expectRedirectPath: false,
		},
		{
			name:               "Follow redirect chain",
			path:               "/redirect-chain",
			followRedirects:    true,
			expectedStatus:     http.StatusOK,
			expectFinalURL:     true,
			expectRedirectPath: true,
		},
		{
			name:               "Follow redirect to 404",
			path:               "/redirect-to-404",
			followRedirects:    true,
			expectedStatus:     http.StatusNotFound,
			expectFinalURL:     true,
			expectRedirectPath: true,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			// Reset globals
			followRedirects = tc.followRedirects
			checkAll = true // Enable checking all URLs for tests
			checked = linkAccumulator{Links: make(map[string]link), mu: &sync.Mutex{}}

			// Create URL
			u, _ := url.Parse(ts.URL + tc.path)
			
			// Create and check link
			l := link{URL: u, RawURL: u.String()}
			checked.Links[u.String()] = l
			
			// Run check
			l.check()
			
			// Get result
			result := checked.Links[u.String()]
			
			// Verify status code
			if result.Status != tc.expectedStatus {
				t.Errorf("expected status %d, got %d", tc.expectedStatus, result.Status)
			}
			
			// Verify final URL
			if tc.expectFinalURL && result.FinalURL == "" {
				t.Errorf("expected final URL to be set, but it wasn't")
			}
			if !tc.expectFinalURL && result.FinalURL != "" {
				t.Errorf("expected final URL to be empty, but got %s", result.FinalURL)
			}
			
			// Verify redirect path
			if tc.expectRedirectPath && len(result.RedirectPath) == 0 {
				t.Errorf("expected redirect path to be set, but it wasn't")
			}
			if !tc.expectRedirectPath && len(result.RedirectPath) > 0 {
				t.Errorf("expected redirect path to be empty, but got %v", result.RedirectPath)
			}
		})
	}
}

func TestRedirectLogging(t *testing.T) {
	// Test that redirect logging works correctly
	ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == "/start" {
			http.Redirect(w, r, "/end", http.StatusFound)
		} else {
			w.WriteHeader(http.StatusOK)
		}
	}))
	defer ts.Close()

	// Enable redirect following
	followRedirects = true
	checkAll = true // Enable checking all URLs for tests
	checked = linkAccumulator{Links: make(map[string]link), mu: &sync.Mutex{}}

	u, _ := url.Parse(ts.URL + "/start")
	l := link{URL: u, RawURL: u.String()}
	checked.Links[u.String()] = l

	l.check()

	result := checked.Links[u.String()]
	if result.Status != http.StatusOK {
		t.Errorf("expected status 200, got %d", result.Status)
	}
	if result.FinalURL == "" {
		t.Errorf("expected final URL to be set")
	}
	if len(result.RedirectPath) == 0 {
		t.Errorf("expected redirect path to contain entries")
	}
}

func TestTrailingSlashFallback(t *testing.T) {
	// Create a test server that serves content with trailing slashes
	ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		switch r.URL.Path {
		case "/no-slash":
			// This path returns 404
			w.WriteHeader(http.StatusNotFound)
		case "/no-slash/":
			// This path (with trailing slash) returns 200
			w.WriteHeader(http.StatusOK)
		case "/already-has-slash/":
			// This path already has a trailing slash and works
			w.WriteHeader(http.StatusOK)
		case "/truly-broken":
			// This path returns 404
			w.WriteHeader(http.StatusNotFound)
		case "/truly-broken/":
			// Even with trailing slash, this returns 404
			w.WriteHeader(http.StatusNotFound)
		default:
			w.WriteHeader(http.StatusOK)
		}
	}))
	defer ts.Close()

	tests := []struct {
		name           string
		path           string
		expectedStatus int
		shouldFallback bool
	}{
		{
			name:           "Path without slash that works with slash",
			path:           "/no-slash",
			expectedStatus: http.StatusOK,
			shouldFallback: true,
		},
		{
			name:           "Path that already has trailing slash",
			path:           "/already-has-slash/",
			expectedStatus: http.StatusOK,
			shouldFallback: false,
		},
		{
			name:           "Path that doesn't work even with slash",
			path:           "/truly-broken",
			expectedStatus: http.StatusNotFound,
			shouldFallback: false,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			// Reset globals
			followRedirects = true
			checkAll = true
			checked = linkAccumulator{Links: make(map[string]link), mu: &sync.Mutex{}}

			// Parse test server URL to get host
			testURL, _ := url.Parse(ts.URL)

			// Set hostname to match test server
			originalHostname := hostname
			hostname = testURL.Host

			// Create URL with test server host
			u, _ := url.Parse(ts.URL + tc.path)

			// Create and check link
			l := link{URL: u, RawURL: u.String()}
			checked.Links[u.String()] = l

			// Run check
			l.check()

			// Restore hostname
			hostname = originalHostname

			// Get result
			result := checked.Links[u.String()]

			// Verify status code
			if result.Status != tc.expectedStatus {
				t.Errorf("expected status %d, got %d", tc.expectedStatus, result.Status)
			}
		})
	}
}
func TestFallbackStrategies(t *testing.T) {
	// Create a test server that simulates various problematic scenarios  
	ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		switch r.URL.Path {
		case "/no-head-support":
			// Only respond properly to GET requests, not HEAD
			if r.Method == "HEAD" {
				w.WriteHeader(http.StatusMethodNotAllowed)
				return
			}
			w.WriteHeader(http.StatusOK)
		case "/works-fine":
			w.WriteHeader(http.StatusOK)
		default:
			w.WriteHeader(http.StatusNotFound)
		}
	}))
	defer ts.Close()

	tests := []struct {
		name           string
		path           string
		method         string
		expectedStatus int
	}{
		{
			name:           "Normal working URL",
			path:           "/works-fine",
			method:         "HEAD",
			expectedStatus: http.StatusOK,
		},
		{
			name:           "Server doesn't support HEAD, fallback to GET works",
			path:           "/no-head-support",
			method:         "HEAD",
			expectedStatus: http.StatusOK,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			// Reset globals
			followRedirects = true
			checkAll = true
			httpMethod = tc.method
			checked = linkAccumulator{Links: make(map[string]link), mu: &sync.Mutex{}}

			// Create URL with test server host
			u, _ := url.Parse(ts.URL + tc.path)

			// Create and check link
			l := link{URL: u, RawURL: u.String()}
			checked.Links[u.String()] = l

			// Run check
			l.check()

			// Get result
			result := checked.Links[u.String()]

			// Verify status code
			if result.Status != tc.expectedStatus {
				t.Errorf("expected status %d, got %d", tc.expectedStatus, result.Status)
			}
		})
	}
}
