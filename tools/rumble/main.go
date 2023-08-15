/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"log"
)

func init() {}

func main() {

	bq, err := NewBqClient()
	if err != nil {
		log.Fatalf("error initializing bq client: %v", err)
	}
	defer bq.Client.Close()

	gcs, err := NewGcsClient()
	if err != nil {
		log.Fatalf("error initializing bq client: %v", err)
	}
	defer gcs.Client.Close()

	gDB, err := NewGrypeClient()
	if err != nil {
		log.Fatalf("error initializing grype client: %v", err)
	}
	defer gDB.DB.Close()

	allVulnRecords, err := bq.query(allVulnsQuery, cveQueryType)
	if err != nil {
		log.Fatalf("error performing allVulnsQuery: %v", err)
	}

	vulns, err := gDB.extractCVEs(allVulnRecords)
	if err != nil {
		log.Fatalf("error querying grype DB: %v", err)
	}

	vs, err := bq.queryAffectedImages(affectedImagesQuery, vulns)
	if err != nil {
		log.Fatalf("error correlating vulnerabilities and images: %v", err)
	}

	err = gcs.saveJSON(vs)
	if err != nil {
		log.Fatalf("error saving vulnerability json files: %v", err)
	}

	// csvRecords, err := bq.query(csvQuery, &scan{})
	// if err != nil {
	// 	log.Fatalf("error performing csvQuery: %v", err)
	// }

	// err = printRecords(csvRecords, &scan{})
	// if err != nil {
	// 	log.Fatalf("error printing/writing csv records: %v", err)
	// }
}
