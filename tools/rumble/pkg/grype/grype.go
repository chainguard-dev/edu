/*
Copyright 2024 Chainguard, Inc.
SPDX-License-Identifier: Apache-2.0
*/

package grype

import (
	"archive/tar"
	"database/sql"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"os"

	"github.com/klauspost/compress/gzip"
	_ "github.com/mattn/go-sqlite3"
)

const (
	grypeDbURL = "https://toolbox-data.anchore.io/grype/databases/listing.json"
)

type grypeDbJSON struct {
	Available map[string]interface{} `json:"available"`
	Version   interface{}            `json:"5"`
	Revision  []map[string]string
}

type grypeBuild struct {
	Built    string `json:"built"`
	Checksum string `json:"checksum"`
	URL      string `json:"url"`
	Version  string `json:"version"`
}

type GrypeDB struct {
	DB      *sql.DB
	jsonURL string
}

type Vuln struct {
	Id         string      `json:"id"`
	Source     string      `json:"url"`
	Sev        string      `json:"severity"`
	Desc       string      `json:"description"`
	External   []VulnImage `json:"external_images"`
	Chainguard []VulnImage `json:"chainguard_images"`
}

type Cve struct {
	Vulnerability string
}

type VulnImage struct {
	Image string   `json:"image"`
	Dates []string `json:"dates"`
	Time  string   `json:"-"`
}

func NewGrypeClient() (GrypeDB, error) {
	var db GrypeDB
	err := db.connect()
	if err != nil {
		return db, err
	}
	return db, nil
}

func (d *GrypeDB) fetchGrypeJSON() error {
	res, err := http.Get(grypeDbURL)
	if err != nil {
		return err
	}
	body, err := io.ReadAll(res.Body)
	if err != nil {
		return err
	}
	defer res.Body.Close()

	grypeJSON := &grypeDbJSON{
		Available: map[string]interface{}{
			"5": []grypeBuild{},
		},
	}

	err = json.Unmarshal(body, &grypeJSON)
	if err != nil {
		return err
	}
	newestBuild := grypeJSON.Available["5"].([]interface{})[0]
	d.jsonURL = newestBuild.(map[string]interface{})["url"].(string)
	return nil
}

func (d *GrypeDB) fetchGrypeDB() error {
	log.Printf("Fetching updated Grype database from %s\n", d.jsonURL)
	res, err := http.Get(d.jsonURL)
	if err != nil {
		return err
	}
	defer res.Body.Close()

	r, err := gzip.NewReader(res.Body)
	if err != nil {
		return err
	}
	defer r.Close()

	tr := tar.NewReader(r)
	for {
		hdr, err := tr.Next()
		if err == io.EOF {
			break // End of archive
		}
		if err != nil {
			return err
		}
		if hdr.Name != "vulnerability.db" {
			continue
		}

		f, err := os.Create(hdr.Name)
		if err != nil {
			return err
		}
		defer f.Close()

		i, err := io.Copy(f, tr)
		if err != nil {
			return err
		}
		log.Printf("Unpacked %s with length %dMB\n", hdr.Name, i/1024/1024)
	}
	return nil
}

func (d *GrypeDB) connect() error {
	f, err := os.Stat("vulnerability.db")
	if f == nil || err != nil {
		err := d.fetchGrypeJSON()
		if err != nil {
			return err
		}
		err = d.fetchGrypeDB()
		if err != nil {
			return err
		}
	}

	d.DB, err = sql.Open("sqlite3", "vulnerability.db")
	if err != nil {
		return err
	}

	return nil
}

func (d *GrypeDB) ExtractCVEs(allVulnRecords []interface{}) ([]Vuln, error) {
	var vulns []Vuln
	var v Vuln
	var row *sql.Row
	var altVulnIDs []string

	// nist, github, aws, oracle vulns first
	for _, r := range allVulnRecords {
		vulnID := r.(*Cve).Vulnerability
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
