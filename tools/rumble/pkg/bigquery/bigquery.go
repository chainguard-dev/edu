/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package cgbigquery

import (
	"context"
	"fmt"

	"cloud.google.com/go/bigquery"
	"github.com/chainguard-dev/edu/tools/rumble/pkg/grype"
	"google.golang.org/api/iterator"
)

const (
	CveQueryType        = "cve"
	ImageScanQueryType  = "scan"
	LegacyScanQueryType = "legacyscan"
)

type BqClient struct {
	Client *bigquery.Client
	Ctx    context.Context
}

type LegacyScan struct {
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

type ImageScan struct {
	Image         string
	T             string
	Package       string
	Vulnerability string
	Version       string
	Type          string
	Severity      string
}

func NewBqClient(project, db string) (BqClient, error) {
	var b BqClient
	if project == "" {
		return b, fmt.Errorf("missing project")
	}
	if db == "" {
		return b, fmt.Errorf("missing db")
	}

	var err error
	b.Ctx = context.Background()
	if b.Client, err = bigquery.NewClient(b.Ctx, project); err != nil {
		return b, err
	}
	return b, nil
}

func (b *BqClient) Query(q *bigquery.Query, queryType string) ([]interface{}, error) {
	q.DefaultProjectID = b.Client.Project()
	it, err := q.Read(b.Ctx)
	if err != nil {
		return nil, fmt.Errorf("%v", err)
	}

	var records []interface{}
	for {
		var values interface{}
		switch queryType {
		case ImageScanQueryType:
			values = &ImageScan{}
		case LegacyScanQueryType:
			values = &LegacyScan{}
		case CveQueryType:
			values = &grype.Cve{}
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
