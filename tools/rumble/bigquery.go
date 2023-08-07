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
	if b.Client, err = bigquery.NewClient(b.Ctx, "base-image-rumble"); err != nil {
		return b, err
	}
	return b, nil
}

const csvQuery = `
SELECT
ROW_NUMBER() OVER (ORDER BY time),
image,
scanner,
scanner_version,
scanner_db_version,
FORMAT_DATETIME("%Y-%m-%d %H:%M:%S", DATE(time)) as time,
low_cve_count as low_cve_cnt,
med_cve_count as med_cve_cnt,
high_cve_count as high_cve_cnt,
crit_cve_count as crit_cve_cnt,
unknown_cve_count as unknown_cve_cnt,
low_cve_count + med_cve_count + high_cve_count + crit_cve_count + unknown_cve_count AS tot_cve_cnt,
digest FROM base-image-rumble.rumble.scheduled
WHERE DATE(time) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND CURRENT_DATE()
	AND scanner = "grype"
	LIMIT 10
`

const allVulnsQuery = `
SELECT DISTINCT vulnerability
FROM base-image-rumble.rumble.scheduled_vulns
`

const cveQuery = `
WITH ruuuumble AS (
	SELECT s1.image,
			s1.time as t,
			s1.raw_grype_json,
			s2.vulnerability,
			s2.installed as version,
			s2.type,
			s2.severity
	FROM base-image-rumble.rumble.scheduled_vulns
	AS s2
	INNER JOIN base-image-rumble.rumble.scheduled
	AS s1
	ON s1.id = s2.scan_id
	WHERE s1.image = "golang:latest"
	OR s1.image = "cgr.dev/chainguard/golang:latest"
  )
  SELECT image, t, vulnerability, version, type, severity FROM ruuuumble
  WHERE DATE(t) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) AND CURRENT_DATE()
  GROUP BY vulnerability, t, image, version, type, severity
`

const affectedImagesQuery = `
SELECT s1.image, s1.time as time,
FROM base-image-rumble.rumble.scheduled_vulns
AS s2
INNER JOIN base-image-rumble.rumble.scheduled
AS s1
ON s1.id = s2.scan_id
WHERE s2.vulnerability = ?
GROUP BY s1.time, s1.image
ORDER BY s1.image, s1.time
`

func (b *bqClient) queryAffectedImages(qr string, vulns []vuln) ([]vuln, error) {
	eg := new(errgroup.Group)
	eg.SetLimit(50)
	for i, v := range vulns {
		eg.Go(func() error {
			vulnerability := v
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
