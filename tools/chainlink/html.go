/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"bytes"
	"fmt"

	nethtml "golang.org/x/net/html"
)

func processHTML(w *filepathWalker) error {
	for _, path := range w.paths {
		// find files matching fileType and read them
		p := pathWalker{path: path}
		if err := p.readFile(); err != nil {
			return fmt.Errorf("error reading file: %s - %v", p.path, err)
		}

		// parse found files into a goldmark ast, then extract links
		html := htmlWalker{path: p.path, rawBytes: &p.rawBytes}
		if err := html.scan(); err != nil {
			return fmt.Errorf("error scanning markdown: %s - %v", html.path, err)
		}
	}
	return nil
}

func (n *htmlWalker) scan() error {
	htmlReader := bytes.NewReader(*n.rawBytes)
	doc, err := nethtml.Parse(htmlReader)
	if err != nil {
		return err
	}

	var f func(*nethtml.Node)
	f = func(node *nethtml.Node) {
		if node.Type == nethtml.ElementNode && node.Data == "a" {
			for _, attr := range node.Attr {
				if attr.Key == "href" {
					l := link{RawURL: attr.Val}
					l.processLink(&n.path)
				}
			}
		}
		for c := node.FirstChild; c != nil; c = c.NextSibling {
			f(c)
		}
	}
	f(doc)
	return nil
}
