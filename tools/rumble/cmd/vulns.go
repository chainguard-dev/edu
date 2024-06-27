/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

// generate JSON files for detected CVEs in our and third party images

package cmd

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"strings"

	"cloud.google.com/go/bigquery"
	cgbigquery "github.com/chainguard-dev/edu/tools/rumble/pkg/bigquery"
	cloudstorage "github.com/chainguard-dev/edu/tools/rumble/pkg/cloudstorage"
	"github.com/chainguard-dev/edu/tools/rumble/pkg/grype"
	"github.com/spf13/cobra"
	"golang.org/x/sync/errgroup"
	"google.golang.org/api/iterator"
)

type vulnsJson struct {
	ctx           context.Context
	opts          *options
	bqClient      cgbigquery.BqClient
	storageClient cloudstorage.GcsClient
	grypeDb       grype.GrypeDB
	vulns         []grype.Vuln
}

// vulnJsonCmd represents the vulnJson command
func cmdVulns(o *options) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "vulns",
		Short: "JSON file per discovered CVE",
		RunE: func(cmd *cobra.Command, args []string) error {
			db, _ := cmd.Flags().GetString("db")
			project, _ := cmd.Flags().GetString("project")
			gcsProject, _ := cmd.Flags().GetString("gcs-project")
			bucket, _ := cmd.Flags().GetString("bucket")
			up, _ := cmd.Flags().GetBool("upload")

			v := &vulnsJson{
				ctx: cmd.Context(),
				opts: &options{
					dbProject:      project,
					storageProject: gcsProject,
					db:             db,
					storageBucket:  bucket,
					upload:         up,
				},
			}
			return v.generateJSON()
		},
	}
	return cmd
}

func (v *vulnsJson) setupClients() error {
	var err error

	v.bqClient, err = cgbigquery.NewBqClient(v.opts.dbProject, v.opts.db)
	if err != nil {
		log.Fatalf("error initializing bq client: %v", err)
	}

	v.storageClient, err = cloudstorage.NewGcsClient(v.ctx, v.opts.storageBucket)
	if err != nil {
		log.Fatalf("error initializing gcs client: %v", err)
	}

	v.grypeDb, err = grype.NewGrypeClient()
	if err != nil {
		log.Fatalf("error initializing grype client: %v", err)
	}

	return nil
}

func (v *vulnsJson) generateJSON() error {
	var err error

	if err := v.setupClients(); err != nil {
		return err
	}
	defer v.bqClient.Client.Close()
	defer v.storageClient.Client.Close()
	defer v.grypeDb.DB.Close()

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

func (vs *vulnsJson) saveFiles(vulns []grype.Vuln) error {
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
			if err := os.WriteFile(fName, js, 0o644); err != nil {
				return err
			}

			fmt.Printf("Wrote %s\n", fName)
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
			fmt.Printf("querying %v\n", vulnerability.Id)
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
		fmt.Println("Successfully saved all vulnerabilities.")
	}
	return nil
}
