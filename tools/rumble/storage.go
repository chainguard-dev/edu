/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"context"
	"encoding/csv"
	"encoding/json"
	"fmt"
	"os"

	"cloud.google.com/go/storage"
	"golang.org/x/sync/errgroup"
)

type gcsClient struct {
	Client *storage.Client
	Ctx    context.Context
}

func NewGcsClient() (g gcsClient, err error) {
	g.Ctx = context.Background()
	if g.Client, err = storage.NewClient(g.Ctx); err != nil {
		return g, err
	}
	return g, nil
}

func (g *gcsClient) saveJSON(vulns []vuln) error {
	eg := new(errgroup.Group)
	fmt.Printf("Found %d vulnerabilities\n", len(vulns))
	eg.SetLimit(50)
	for _, v := range vulns {
		vulnerability := v
		eg.Go(func() error {
			js, err := json.MarshalIndent(vulnerability, "", "")
			if err != nil {
				return err
			}

			fName := fmt.Sprintf("vulnerability-info/%s.json", vulnerability.Id)
			bkt := g.Client.Bucket("chainguard-academy")
			obj := bkt.Object(fName)

			w := obj.NewWriter(g.Ctx)
			w.ContentType = "application/json"
			w.ACL = []storage.ACLRule{
				{
					Entity: storage.AllUsers,
					Role:   storage.RoleReader,
				},
			}

			if _, err := fmt.Fprint(w, string(js)); err != nil {
				return err
			}
			// Close, just like writing a file.
			if err := w.Close(); err != nil {
				return err
			}

			fmt.Printf("Wrote %s\n", fName)
			return nil
		})
	}

	if err := eg.Wait(); err == nil {
		fmt.Println("Successfully saved all vulnerabilities.")
	}
	return nil
}

// unused, but can print a csv to stdout if needed
func printRecords(records []interface{}, queryType string) error {
	w := csv.NewWriter(os.Stdout)

	for _, r := range records {
		var s []string
		switch queryType {
		case scanQueryType:
			s = append(s, r.(*scan).Image, r.(*scan).Scanner)
		case cveQueryType:
			s = append(s, r.(*cve).Vulnerability)
		}
		if err := w.Write(s); err != nil {
			return fmt.Errorf("error writing record to csv: %v", err)
		}
	}

	// Write any buffered data to the underlying writer (standard output).
	w.Flush()

	if err := w.Error(); err != nil {
		return fmt.Errorf("%v", err)
	}

	return nil
}
