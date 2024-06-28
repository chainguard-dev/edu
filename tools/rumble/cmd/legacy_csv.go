/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

// generate a CSV of vulnerability data for all tracked (public) and third party images

package cmd

import (
	"context"
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	cgbigquery "github.com/chainguard-dev/edu/tools/rumble/pkg/bigquery"
	cloudstorage "github.com/chainguard-dev/edu/tools/rumble/pkg/cloudstorage"
	"github.com/spf13/cobra"
)

type legacyCsv struct {
	ctx           context.Context
	bqClient      cgbigquery.BqClient
	storageClient cloudstorage.GcsClient
	opts          *options
}

func cmdLegacyCsv(o *options) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "legacy-csv",
		Short: "Single CSV with all scanned images and vulns",
		RunE: func(cmd *cobra.Command, args []string) error {
			db, _ := cmd.Flags().GetString("db")
			project, _ := cmd.Flags().GetString("project")
			gcsProject, _ := cmd.Flags().GetString("gcs-project")
			bucket, _ := cmd.Flags().GetString("bucket")
			up, _ := cmd.Flags().GetBool("upload")

			l := legacyCsv{
				ctx: cmd.Context(),
				opts: &options{
					dbProject:      project,
					storageProject: gcsProject,
					db:             db,
					storageBucket:  bucket,
					upload:         up,
				},
			}
			return l.generateCsv()
		},
	}
	return cmd
}

func (l *legacyCsv) setupClients() error {
	var err error

	l.bqClient, err = cgbigquery.NewBqClient(l.opts.dbProject, l.opts.db)
	if err != nil {
		log.Fatalf("error initializing bq client: %v", err)
	}

	l.storageClient, err = cloudstorage.NewGcsClient(l.ctx, l.opts.storageBucket)
	if err != nil {
		log.Fatalf("error initializing gcs client: %v", err)
	}
	return nil
}

func (l *legacyCsv) generateCsv() error {
	if err := l.setupClients(); err != nil {
		return err
	}
	defer l.bqClient.Client.Close()
	defer l.storageClient.Client.Close()

	q := l.bqClient.Client.Query(cgbigquery.LegacyCsvQuery)

	rows, err := l.bqClient.Query(q, cgbigquery.LegacyScanQueryType)
	if err != nil {
		log.Fatalf("error fetching scan results: %v", err)
	}

	var w *csv.Writer
	switch l.opts.upload {
	case true:
		fName := "cve-data/data.csv"
		gcsCsvWriter, err := l.storageClient.GetCsvWriter(fName)
		if err != nil {
			return err
		}
		defer gcsCsvWriter.Close()
		w = csv.NewWriter(gcsCsvWriter)
		fmt.Printf("Writing %s to GCS bucket\n", fName)
	default:
		f, err := os.Create("data.csv")
		if err != nil {
			return err
		}
		defer f.Close()
		w = csv.NewWriter(f)
		fmt.Printf("Writing to %s\n", f.Name())
	}

	err = w.Write(strings.Split(cgbigquery.LegacyCsvHeader, ","))
	if err != nil {
		return err
	}
	for i, r := range rows {
		image := r.(*cgbigquery.LegacyScan).Image
		// only want external/third party images, and public chainguard images in the results
		if !strings.Contains(image, "cgr.dev") || strings.Contains(image, "cgr.dev/chainguard/") {
			csvRow := []string{
				strconv.Itoa(i + 1),
				r.(*cgbigquery.LegacyScan).Image,
				r.(*cgbigquery.LegacyScan).Scanner,
				r.(*cgbigquery.LegacyScan).Scanner_version,
				r.(*cgbigquery.LegacyScan).Scanner_db_version,
				r.(*cgbigquery.LegacyScan).Time,
				strconv.FormatInt(r.(*cgbigquery.LegacyScan).Low_cve_cnt, 10),
				strconv.FormatInt(r.(*cgbigquery.LegacyScan).Med_cve_cnt, 10),
				strconv.FormatInt(r.(*cgbigquery.LegacyScan).High_cve_cnt, 10),
				strconv.FormatInt(r.(*cgbigquery.LegacyScan).Crit_cve_cnt, 10),
				strconv.FormatInt(r.(*cgbigquery.LegacyScan).Unknown_cve_cnt, 10),
				strconv.FormatInt(r.(*cgbigquery.LegacyScan).Tot_cve_cnt, 10),
				r.(*cgbigquery.LegacyScan).Digest,
			}
			err := w.Write(csvRow)
			if err != nil {
				return err
			}
		}
	}
	w.Flush()
	return w.Error()
}
