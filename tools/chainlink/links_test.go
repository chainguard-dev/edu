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