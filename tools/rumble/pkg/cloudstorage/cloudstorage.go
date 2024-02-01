/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package cmd

import (
	"context"
	"encoding/json"
	"fmt"

	"cloud.google.com/go/storage"
	"github.com/chainguard-dev/edu/tools/rumble/pkg/grype"
	"golang.org/x/oauth2/google"
	"golang.org/x/sync/errgroup"
	"google.golang.org/api/option"
)

type GcsClient struct {
	Client *storage.Client
	Ctx    context.Context
	Bucket string
}

func NewGcsClient(project, bucket string) (g GcsClient, err error) {
	ctx := context.Background()
	creds, err := google.FindDefaultCredentials(ctx)
	if err != nil {
		return g, err
	}
	creds.ProjectID = project

	g.Ctx = context.Background()
	if g.Client, err = storage.NewClient(g.Ctx, option.WithCredentials(creds)); err != nil {
		return g, err
	}
	g.Bucket = bucket
	return g, nil
}

// this should live over in vulns.go and be a vulnsJson method
func (g *GcsClient) SaveVulnJSON(vulns []grype.Vuln) error {
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
			bkt := g.Client.Bucket(g.Bucket)
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

func (g *GcsClient) GetCsvWriter(fName string) (*storage.Writer, error) {
	bkt := g.Client.Bucket(g.Bucket)
	obj := bkt.Object(fName)

	w := obj.NewWriter(g.Ctx)
	w.ContentType = "text/csv"
	w.CacheControl = "public, max-age=60"
	w.ACL = []storage.ACLRule{
		{
			Entity: storage.AllUsers,
			Role:   storage.RoleReader,
		},
	}
	return w, nil
}
