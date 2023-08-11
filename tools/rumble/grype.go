/*
Copyright 2023 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"database/sql"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

const vulnIDquery = `SELECT DISTINCT id, data_source, severity, description
FROM "vulnerability_metadata"
WHERE id = ?
AND (
	data_source LIKE 'https://nvd.nist.gov/%'
	OR data_source LIKE 'https://github.com/%'
	OR data_source LIKE 'https://linux.oracle.com/%'
	OR data_source LIKE 'https://alas.aws.amazon.com/%'
)`

// some vulns do not have an nvd URL so use the distro URL
// e.g. security.debian.org, people.ubuntu.com etc.
const altVulnIDquery = `SELECT DISTINCT id, data_source, severity, description
FROM "vulnerability_metadata"
WHERE id = ?
LIMIT 1`

type grypeDB struct {
	DB *sql.DB
}

type vuln struct {
	Id         string      `json:"id"`
	Source     string      `json:"url"`
	Sev        string      `json:"severity"`
	Desc       string      `json:"description"`
	External   []vulnImage `json:"external_images"`
	Chainguard []vulnImage `json:"chainguard_images"`
}

type vulnImage struct {
	Image string   `json:"image"`
	Dates []string `json:"dates"`
	Time  string   `json:"-"`
}

func NewGrypeClient() (grypeDB, error) {
	var db grypeDB
	err := db.connect()
	if err != nil {
		return db, err
	}
	return db, nil
}

func (d *grypeDB) connect() error {
	var err error
	d.DB, err = sql.Open("sqlite3", "vulnerability.db")
	if err != nil {
		return err
	}

	return nil
}

func (d *grypeDB) extractCVEs(allVulnRecords []interface{}) ([]vuln, error) {
	var vulns []vuln
	var v vuln
	var row *sql.Row
	var altVulnIDs []string

	// nist, github, aws, oracle vulns first
	for _, r := range allVulnRecords {
		vulnID := r.(*cve).Vulnerability
		row = d.DB.QueryRow(vulnIDquery, vulnID)
		err := row.Scan(&v.Id, &v.Source, &v.Sev, &v.Desc)

		if err != nil && err == sql.ErrNoRows {
			altVulnIDs = append(altVulnIDs, vulnID)
			continue
		}
		if err != nil {
			return nil, err
		}
		vulns = append(vulns, v)
	}

	// now distro-specific URLs like security.debian.org, people.ubuntu.com
	for _, r := range altVulnIDs {
		row = d.DB.QueryRow(altVulnIDquery, r)
		err := row.Scan(&v.Id, &v.Source, &v.Sev, &v.Desc)

		if err != nil && err == sql.ErrNoRows {
			log.Printf("missing vulnerability url for %v", r)
			continue
		}
		if err != nil {
			return nil, err
		}
		vulns = append(vulns, v)
	}

	return vulns, nil
}
