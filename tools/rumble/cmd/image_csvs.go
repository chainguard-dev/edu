/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

// generate a CSV of vulnerability data for image pairs
// pairs are located in ../../data/rumble.json

package cmd

import (
	"context"
	"encoding/csv"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"strings"

	"cloud.google.com/go/bigquery"
	cgbigquery "github.com/chainguard-dev/edu/tools/rumble/pkg/bigquery"
	cloudstorage "github.com/chainguard-dev/edu/tools/rumble/pkg/cloudstorage"
	"github.com/spf13/cobra"
)

type rumbleJson []struct {
	Image  string `json:"image"`
	Theirs string `json:"left"`
	Ours   string `json:"right"`
}

type imageCsv struct {
	ctx            context.Context
	bqClient       cgbigquery.BqClient
	storageClient  cloudstorage.GcsClient
	opts           *options
	rumbleJsonPath string
	comparisons    *rumbleJson
}

func cmdImageCsvs(o *options) *cobra.Command {
	var rumbleJsonPath string

	cmd := &cobra.Command{
		Use:   "image-csv",
		Short: "CSV for a single external/third party image and a Chainguard image",
		RunE: func(cmd *cobra.Command, args []string) error {
			db, _ := cmd.Flags().GetString("db")
			project, _ := cmd.Flags().GetString("project")
			gcsProject, _ := cmd.Flags().GetString("gcs-project")
			bucket, _ := cmd.Flags().GetString("bucket")
			up, _ := cmd.Flags().GetBool("upload")

			i := imageCsv{
				ctx: cmd.Context(),
				opts: &options{
					dbProject:      project,
					storageProject: gcsProject,
					db:             db,
					storageBucket:  bucket,
					upload:         up,
				},
				rumbleJsonPath: rumbleJsonPath,
			}
			return i.generateCsvs()
		},
	}

	cmd.Flags().StringVar(&rumbleJsonPath, "rumble-json-path", "", "Path to rumble.json with image pairs to compare")

	return cmd
}

func (i *imageCsv) setupClients() error {
	var err error

	i.bqClient, err = cgbigquery.NewBqClient(i.opts.dbProject, i.opts.db)
	if err != nil {
		log.Fatalf("error initializing bq client: %v", err)
	}

	i.storageClient, err = cloudstorage.NewGcsClient(i.ctx, i.opts.storageBucket)
	if err != nil {
		log.Fatalf("error initializing gcs client: %v", err)
	}
	return nil
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

func (i *imageCsv) generateCsvs() error {
	if i.rumbleJsonPath == "" {
		return fmt.Errorf("missing --theirs or --ours argument")
	}

	if err := i.parseRumbleJson(); err != nil {
		return err
	}

	if err := i.setupClients(); err != nil {
		return err
	}
	defer i.bqClient.Client.Close()
	defer i.storageClient.Client.Close()

	for _, img := range *i.comparisons {
		q := i.bqClient.Client.Query(cgbigquery.ImageComparisonCsvQuery)
		q.DefaultProjectID = i.bqClient.Client.Project()
		q.Parameters = []bigquery.QueryParameter{
			{
				Name: "theirs",
				Value: &bigquery.QueryParameterValue{
					Type: bigquery.StandardSQLDataType{
						TypeKind: "STRING",
					},
					Value: img.Theirs,
				},
			},
			{
				Name: "ours",
				Value: &bigquery.QueryParameterValue{
					Type: bigquery.StandardSQLDataType{
						TypeKind: "STRING",
					},
					Value: img.Ours,
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
			fmt.Printf("Writing %s to GCS bucket\n", fName)
		default:
			f, err := os.Create(fName)
			if err != nil {
				return err
			}
			defer f.Close()
			w = csv.NewWriter(f)
			fmt.Printf("Writing to %s\n", f.Name())
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
