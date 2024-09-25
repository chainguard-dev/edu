/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

// generate a CSV of vulnerability data for image pairs
// pairs are located in ../../data/rumble.json

package cmd

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"strings"

	"cloud.google.com/go/bigquery"
	cgbigquery "github.com/chainguard-dev/edu/tools/rumble/pkg/bigquery"
	"github.com/spf13/cobra"
)

type rumbleJson []struct {
	Image  string `json:"image"`
	Theirs string `json:"left"`
	Ours   string `json:"right"`
}

type imageCsv struct {
	rumbleBase

	rumbleJsonPath string
	comparisons    *rumbleJson
}

func cmdImageCsvs(o *options) *cobra.Command {
	var rumbleJsonPath string

	cmd := &cobra.Command{
		Use:   "image-csv",
		Short: "CSV for a single external/third party image and a Chainguard image",
		RunE: func(cmd *cobra.Command, args []string) error {
			i := imageCsv{
				rumbleBase: rumbleBase{
					ctx:  cmd.Context(),
					opts: o,
				},
				rumbleJsonPath: rumbleJsonPath,
			}
			return i.generateCsvs()
		},
	}

	cmd.Flags().StringVar(&rumbleJsonPath, "rumble-json-path", "", "Path to rumble.json with image pairs to compare")

	return cmd
}

func (i *imageCsv) parseRumbleJson() error {
	f, err := os.ReadFile(i.rumbleJsonPath)
	if err != nil {
		return err
	}
	i.comparisons = &rumbleJson{}
	err = json.Unmarshal(f, i.comparisons)
	if err != nil {
		return err
	}
	return nil
}

// splitRepoTag splits an image references like foo:bar into
// the repo and tag components. If a ref doesn't have a tag,
// latest is assumed.
func splitRepoTag(ref string) (string, string) {
	if repo, tag, ok := strings.Cut(ref, ":"); ok {
		return repo, tag
	}
	return ref, "latest"
}

func (i *imageCsv) generateCsvs() error {
	if i.rumbleJsonPath == "" {
		return fmt.Errorf("missing --theirs or --ours argument")
	}

	if err := i.parseRumbleJson(); err != nil {
		return err
	}

	closer, err := i.setupClients()
	if err != nil {
		return err
	}
	defer closer()

	for _, img := range *i.comparisons {
		log.Printf("querying %v", img)

		q := i.bqClient.Client.Query(cgbigquery.ImageComparisonCsvQuery)
		theirRepo, theirTag := splitRepoTag(img.Theirs)
		ourRepo, ourTag := splitRepoTag(img.Ours)

		q.DefaultProjectID = i.bqClient.Client.Project()
		q.Parameters = []bigquery.QueryParameter{
			{
				Name: "theirs",
				Value: &bigquery.QueryParameterValue{
					Type: bigquery.StandardSQLDataType{
						TypeKind: "STRING",
					},
					Value: theirRepo,
				},
			},
			{
				Name: "their_tag",
				Value: &bigquery.QueryParameterValue{
					Type: bigquery.StandardSQLDataType{
						TypeKind: "STRING",
					},
					Value: theirTag,
				},
			},
			{
				Name: "ours",
				Value: &bigquery.QueryParameterValue{
					Type: bigquery.StandardSQLDataType{
						TypeKind: "STRING",
					},
					Value: ourRepo,
				},
			},
			{
				Name: "our_tag",
				Value: &bigquery.QueryParameterValue{
					Type: bigquery.StandardSQLDataType{
						TypeKind: "STRING",
					},
					Value: ourTag,
				},
			},
		}

		rows, err := i.bqClient.Query(q, cgbigquery.ImageScanQueryType)
		if err != nil {
			log.Fatalf("error fetching scan results: %v", err)
		}

		fName := fmt.Sprintf("cve-data/%s.csv", img.Image)
		var w *csv.Writer
		switch i.opts.upload {
		case true:
			gcsCsvWriter, err := i.storageClient.GetCsvWriter(fName)
			if err != nil {
				return err
			}
			defer gcsCsvWriter.Close()
			w = csv.NewWriter(gcsCsvWriter)
			log.Printf("Writing %s to GCS bucket", fName)
		default:
			f, err := os.Create(fName)
			if err != nil {
				return err
			}
			defer f.Close()
			w = csv.NewWriter(f)
			log.Printf("Writing to %s", f.Name())
		}

		err = w.Write(strings.Split(cgbigquery.ImageScanCsvHeader, ","))
		if err != nil {
			return err
		}
		for _, r := range rows {
			image := r.(*cgbigquery.ImageScan).Image
			// only want external/third party images, and public chainguard images in the results
			if !strings.Contains(image, "cgr.dev") || strings.Contains(image, "cgr.dev/chainguard/") {
				csvRow := []string{
					image,
					r.(*cgbigquery.ImageScan).Package,
					r.(*cgbigquery.ImageScan).Vulnerability,
					r.(*cgbigquery.ImageScan).Version,
					r.(*cgbigquery.ImageScan).Type,
					r.(*cgbigquery.ImageScan).Severity,
				}
				err := w.Write(csvRow)
				if err != nil {
					return err
				}
			}
		}
		w.Flush()
	}
	return nil
}
