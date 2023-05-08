package main

import (
	"fmt"

	"github.com/yuin/goldmark"
	"github.com/yuin/goldmark/ast"
	"github.com/yuin/goldmark/text"
)

func processMarkdown(w *filepathWalker) error {
	// range over each file and extract links all in one go
	nodeParser := goldmark.New().Parser()
	for _, path := range w.paths {
		// find files matching fileType and read them
		p := pathWalker{path: path}
		if err := p.readFile(); err != nil {
			return fmt.Errorf("error reading file: %s - %v", p.path, err)
		}

		// parse found files into a goldmark ast, then extract links
		md := mdWalker{path: p.path, rawBytes: &p.rawBytes, parser: &nodeParser}
		if err := md.scan(); err != nil {
			return fmt.Errorf("error scanning markdown: %s - %v", md.path, err)
		}
	}
	return nil
}

func (n *mdWalker) scan() error {
	reader := text.NewReader(*n.rawBytes)
	p := *n.parser
	node := p.Parse(reader) // node is the root markdown ast.Node

	if err := ast.Walk(node, n.walkNodeFunc); err != nil {
		return fmt.Errorf("error walking markdown node: %v - %v", node, err)
	}

	return nil
}

func (n *mdWalker) walkNodeFunc(node ast.Node, entering bool) (ast.WalkStatus, error) {
	if !entering {
		return ast.WalkContinue, nil
	}

	// only look for Link nodes
	if node.Kind() != ast.KindLink {
		return ast.WalkContinue, nil
	}

	// got a link, extract it
	l := link{RawURL: string(node.(*ast.Link).Destination)}
	l.processLink(&n.path)
	return ast.WalkContinue, nil
}
