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

	"cloud.google.com/go/bigquery"
	cgbigquery "github.com/chainguard-dev/edu/tools/rumble/pkg/bigquery"
	"github.com/chainguard-dev/edu/tools/rumble/pkg/grype"
	"github.com/spf13/cobra"
	"golang.org/x/sync/errgroup"
	"google.golang.org/api/iterator"
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

	q := v.bqClient.Client.Query(cgbigquery.AllVulnsQuery)
	allVulnRecords, err := v.bqClient.Query(q, cgbigquery.CveQueryType)
	if err != nil {
		log.Fatalf("error performing AllVulnsQuery: %v", err)
	}

	v.vulns, err = v.grypeDb.ExtractCVEs(allVulnRecords)
	if err != nil {
		log.Fatalf("error querying grype DB: %v", err)
	}

	err = v.queryAffectedImages()
	if err != nil {
		log.Fatalf("error correlating vulnerabilities and images: %v", err)
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

func (v *vulnsJson) queryAffectedImages() error {
	eg := new(errgroup.Group)
	eg.SetLimit(50)
	for idx, vuln := range v.vulns {
		vulnerability := vuln
		i := idx
		eg.Go(func() error {
			log.Printf("querying %v", vulnerability.Id)
			q := v.bqClient.Client.Query(cgbigquery.AffectedImagesQuery)
			q.DefaultProjectID = v.bqClient.Client.Project()
			q.Parameters = []bigquery.QueryParameter{
				{
					Name: "vulnerability",
					Value: &bigquery.QueryParameterValue{
						Type: bigquery.StandardSQLDataType{
							TypeKind: "STRING",
						},
						Value: vulnerability.Id,
					},
				},
			}

			it, err := q.Read(v.bqClient.Ctx)
			if err != nil {
				return fmt.Errorf("%v", err)
			}

			imagesMap := make(map[string]grype.VulnImage)
			for {
				res := &grype.VulnImage{}
				err := it.Next(res)
				if err == iterator.Done {
					break
				}
				if err != nil {
					return fmt.Errorf("%v", err)
				}
				img := imagesMap[res.Image]
				img.Dates = append(img.Dates, res.Time)
				img.Image = res.Image
				imagesMap[res.Image] = img
			}

			for _, img := range imagesMap {
				if strings.Contains(img.Image, "cgr.dev") {
					v.vulns[i].Chainguard = append(v.vulns[i].Chainguard, img)
				} else {
					v.vulns[i].External = append(v.vulns[i].External, img)
				}
			}

			return nil
		})
	}

	if err := eg.Wait(); err == nil {
		log.Println("Successfully saved all vulnerabilities.")
	}
	return nil
}
