/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"context"
	"fmt"
	"strings"

	"cloud.google.com/go/bigquery"
	"golang.org/x/sync/errgroup"
	"google.golang.org/api/iterator"
)

const cveQueryType = "cve"
const scanQueryType = "scan"

type bqClient struct {
	Client *bigquery.Client
	Ctx    context.Context
}

type cve struct {
	Vulnerability string
}

type scan struct {
	Row                int64
	Image              string
	Scanner            string
	Scanner_version    string
	Scanner_db_version string
	Time               string
	Low_cve_cnt        int64
	Med_cve_cnt        int64
	High_cve_cnt       int64
	Crit_cve_cnt       int64
	Unknown_cve_cnt    int64
	Tot_cve_cnt        int64
	Digest             string
}

func NewBqClient() (bqClient, error) {
	var b bqClient
	var err error
	b.Ctx = context.Background()
	if b.Client, err = bigquery.NewClient(b.Ctx, "prod-images-c6e5"); err != nil {
		return b, err
	}
	return b, nil
}

const allVulnsQuery = `
SELECT DISTINCT vulnerability
FROM prod-images-c6e5.insights_ds.vulnerabilities
`

const affectedImagesQuery = `
SELECT s1.image, s1.time as time,
FROM prod-images-c6e5.insights_ds.vulnerabilities
AS s2
INNER JOIN prod-images-c6e5.insights_ds.image-scan-summary
AS s1
ON s1.id = s2.scan_id
WHERE s2.vulnerability = ?
GROUP BY s1.time, s1.image
ORDER BY s1.image, s1.time
`

func (b *bqClient) queryAffectedImages(qr string, vulns []vuln) ([]vuln, error) {
	eg := new(errgroup.Group)
	eg.SetLimit(50)
	for idx, v := range vulns {
		vulnerability := v
		i := idx
		eg.Go(func() error {
			fmt.Printf("querying %v\n", vulnerability.Id)
			q := b.Client.Query(qr)
			q.Parameters = []bigquery.QueryParameter{
				{
					Value: &bigquery.QueryParameterValue{
						Type: bigquery.StandardSQLDataType{
							TypeKind: "STRING",
						},
						Value: vulnerability.Id,
					},
				},
			}

			it, err := q.Read(b.Ctx)
			if err != nil {
				return fmt.Errorf("%v", err)
			}

			imagesMap := make(map[string]vulnImage)
			for {
				res := &vulnImage{}
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
					vulns[i].Chainguard = append(vulns[i].Chainguard, img)
				} else {
					vulns[i].External = append(vulns[i].External, img)
				}
			}

			return nil
		})
	}

	if err := eg.Wait(); err == nil {
		fmt.Println("Successfully saved all vulnerabilities.")
	}
	return vulns, nil
}

func (b *bqClient) query(qr string, queryType string) ([]interface{}, error) {
	q := b.Client.Query(qr)

	it, err := q.Read(b.Ctx)
	if err != nil {
		return nil, fmt.Errorf("%v", err)
	}

	var records []interface{}
	for {
		var values interface{}
		switch queryType {
		case scanQueryType:
			values = &scan{}
		case cveQueryType:
			values = &cve{}
		}
		err := it.Next(values)
		if err == iterator.Done {
			break
		}
		if err != nil {
			return nil, fmt.Errorf("%v", err)
		}
		records = append(records, values)
	}

	return records, nil
}
