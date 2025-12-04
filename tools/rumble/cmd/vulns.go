/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

// generate JSON files for detected CVEs in our and third party images

package cmd

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"strings"

	cgbigquery "github.com/chainguard-dev/edu/tools/rumble/pkg/bigquery"
	"github.com/chainguard-dev/edu/tools/rumble/pkg/grype"
	"github.com/spf13/cobra"
	"golang.org/x/sync/errgroup"
)

type vulnsJson struct {
	rumbleBase

	grypeDb grype.GrypeDB
	vulns   []grype.Vuln
}

// vulnJsonCmd represents the vulnJson command
func cmdVulns(o *options) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "vulns",
		Short: "JSON file per discovered CVE",
		RunE: func(cmd *cobra.Command, args []string) error {
			v := &vulnsJson{
				rumbleBase: rumbleBase{
					ctx:  cmd.Context(),
					opts: o,
				},
			}
			return v.generateJSON()
		},
	}
	return cmd
}

func (v *vulnsJson) setupClients() (func(), error) {
	closer, err := v.rumbleBase.setupClients()
	if err != nil {
		return closer, err
	}

	v.grypeDb, err = grype.NewGrypeClient()
	if err != nil {
		log.Fatalf("error initializing grype client: %v", err)
	}

	return func() {
		closer()
		if err := v.grypeDb.DB.Close(); err != nil {
			log.Println(err)
		}
	}, nil
}

func (v *vulnsJson) generateJSON() error {
	closer, err := v.setupClients()
	if err != nil {
		return err
	}
	defer closer()

	// Single query to get all vulnerability-image relationships
	q := v.bqClient.Client.Query(cgbigquery.AllVulnsWithImagesQuery)
	allRecords, err := v.bqClient.Query(q, cgbigquery.VulnWithImagesQueryType)
	if err != nil {
		log.Fatalf("error performing AllVulnsWithImagesQuery: %v", err)
	}

	// Group results by vulnerability ID
	vulnImageMap := make(map[string][]cgbigquery.VulnWithImages)
	for _, record := range allRecords {
		vwi := record.(*cgbigquery.VulnWithImages)
		vulnImageMap[vwi.Vulnerability] = append(vulnImageMap[vwi.Vulnerability], *vwi)
	}

	// Extract unique CVE IDs for enrichment
	cveRecords := make([]interface{}, 0, len(vulnImageMap))
	for vulnID := range vulnImageMap {
		cveRecords = append(cveRecords, &grype.Cve{Vulnerability: vulnID})
	}

	// Enrich with Grype metadata from local SQLite DB
	v.vulns, err = v.grypeDb.ExtractCVEs(cveRecords)
	if err != nil {
		log.Fatalf("error querying grype DB: %v", err)
	}

	// Populate image data for each vulnerability
	for i := range v.vulns {
		vulnID := v.vulns[i].Id
		imageRecords := vulnImageMap[vulnID]

		// Group by image to aggregate dates
		imagesMap := make(map[string]grype.VulnImage)
		for _, record := range imageRecords {
			img := imagesMap[record.Image]
			img.Dates = append(img.Dates, record.Time.Format("2006-01-02"))
			img.Image = record.Image
			imagesMap[record.Image] = img
		}

		// Split into Chainguard vs External
		for _, img := range imagesMap {
			if strings.Contains(img.Image, "cgr.dev") {
				v.vulns[i].Chainguard = append(v.vulns[i].Chainguard, img)
			} else {
				v.vulns[i].External = append(v.vulns[i].External, img)
			}
		}
	}

	switch v.opts.upload {
	case true:
		err = v.storageClient.SaveVulnJSON(v.vulns)
		if err != nil {
			log.Fatalf("error uploading vulnerability json files to GCS: %v", err)
		}
	default:
		err = v.saveFiles(v.vulns)
		if err != nil {
			log.Fatalf("error saving local vulnerability json files: %v", err)
		}
	}

	return nil
}

func (v *vulnsJson) saveFiles(vulns []grype.Vuln) error {
	eg := new(errgroup.Group)
	log.Printf("Found %d vulnerabilities", len(vulns))
	eg.SetLimit(50)
	for _, v := range vulns {
		vulnerability := v
		eg.Go(func() error {
			js, err := json.MarshalIndent(vulnerability, "", "")
			if err != nil {
				return err
			}

			fName := fmt.Sprintf("vulnerability-info/%s.json", vulnerability.Id)
			if err := os.WriteFile(fName, js, 0o644); err != nil {
				return err
			}

			log.Printf("Wrote %s", fName)
			return nil
		})
	}
	return eg.Wait()
}
