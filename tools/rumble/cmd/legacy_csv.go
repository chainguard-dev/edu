/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

// generate a CSV of vulnerability data for all tracked (public) and third party images

package cmd

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	cgbigquery "github.com/chainguard-dev/edu/tools/rumble/pkg/bigquery"
	"github.com/spf13/cobra"
)

func cmdLegacyCsv(o *options) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "legacy-csv",
		Short: "Single CSV with all scanned images and vulns",
		RunE: func(cmd *cobra.Command, args []string) error {
			l := rumbleBase{
				ctx:  cmd.Context(),
				opts: o,
			}
			return l.generateCsv()
		},
	}
	return cmd
}

func (c *rumbleBase) generateCsv() error {
	closer, err := c.setupClients()
	if err != nil {
		return err
	}
	defer closer()

	q := c.bqClient.Client.Query(cgbigquery.LegacyCsvQuery)

	rows, err := c.bqClient.Query(q, cgbigquery.LegacyScanQueryType)
	if err != nil {
		log.Fatalf("error fetching scan results: %v", err)
	}

	var w *csv.Writer
	switch c.opts.upload {
	case true:
		fName := "cve-data/data.csv"
		gcsCsvWriter, err := c.storageClient.GetCsvWriter(fName)
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
